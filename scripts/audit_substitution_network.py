"""Exact one-position substitutions, with complete source witnesses.

This descriptive graph is not an equivalence relation, sign merger or decipherment.
Input is the pre-existing strict corpus; no damaged strings are reconstructed.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json
from common import ROOT, read_jsonl, sha256, write_csv, write_json, write_jsonl

SOURCE_FIELDS = ('id','artifact','cisi_original','site','type','condition','preservation','complete','order','namespace')


def masked(sequence, index):
    return tuple(sequence[:index])+('?',)+tuple(sequence[index+1:])


def find_open_wedge(neighbors, pairs):
    """An observed A-B-C path with no observed A-C edge; absence is not incompatibility."""
    candidates=[]
    for b in sorted(neighbors):
        for a,c in combinations(sorted(neighbors[b]),2):
            if c in neighbors[a]:
                continue
            ab=pairs[tuple(sorted((a,b)))]
            bc=pairs[tuple(sorted((b,c)))]
            candidates.append((min(len(ab),len(bc)),len(ab)+len(bc),a,b,c))
    if not candidates:
        return None
    # Prefer two well-supported arms; lexicographic order deterministically resolves ties.
    _,_,a,b,c=min(candidates,key=lambda r:(-r[0],-r[1],r[2:]))
    return {'a':a,'b':b,'c':c,'ab_frame_ids':pairs[tuple(sorted((a,b)))],
            'bc_frame_ids':pairs[tuple(sorted((b,c)))], 'ac_edge_observed':False,
            'selection':'Largest minimum arm frame-count, then total arm frame-count; deterministic lexical tie-break.',
            'meaning':'Observed exact-substitution relation need not be transitive; absent A-C evidence is not proof of incompatibility.'}


def audit(records):
    by_sequence=defaultdict(list)
    for row in records:
        sequence=tuple(row['sequence'])
        if not sequence or '?' in sequence:
            raise ValueError('Nonempty, fully specified sequences required')
        by_sequence[sequence].append({k:row[k] for k in SOURCE_FIELDS if k in row})
    texts=[]
    seq_to_id={}
    by_sign=defaultdict(set)
    sign_tokens=Counter()
    sign_repeat=defaultdict(list)
    frames=defaultdict(dict)
    for number,sequence in enumerate(sorted(by_sequence),1):
        tid=f'T{number:04d}'
        seq_to_id[sequence]=tid
        text={'text_id':tid,'sequence':list(sequence),'length':len(sequence),
              'source_records':sorted(by_sequence[sequence],key=lambda r:json.dumps(r,sort_keys=True))}
        texts.append(text)
        for sign,count in Counter(sequence).items():
            by_sign[sign].add(tid)
            sign_tokens[sign]+=count
            if count>1:
                sign_repeat[sign].append({'text_id':tid,'occurrences':count,
                                          'positions':[i for i,x in enumerate(sequence) if x==sign]})
        for i,sign in enumerate(sequence):
            frames[masked(sequence,i)][sign]=tid
    shared=[]
    pairs=defaultdict(list)
    neighbors=defaultdict(set)
    sign_frames=defaultdict(list)
    for frame,members in sorted(frames.items()):
        if len(members)<2:
            continue
        fid=f'F{len(shared)+1:04d}'
        item={'frame_id':fid,'frame':list(frame),'position_zero_based':frame.index('?'),
              'length':len(frame),'replacement_count':len(members),
              'members':[{'sign':sign,'text_id':members[sign]} for sign in sorted(members)]}
        shared.append(item)
        for sign in members:
            sign_frames[sign].append(fid)
        for a,b in combinations(sorted(members),2):
            pairs[a,b].append(fid)
            neighbors[a].add(b)
            neighbors[b].add(a)
    frame_map={f['frame_id']:f for f in shared}
    text_map={t['text_id']:t for t in texts}
    pair_rows=[]
    for (a,b),fids in sorted(pairs.items()):
        contexts=[]
        for fid in fids:
            f=frame_map[fid]
            members={m['sign']:m['text_id'] for m in f['members']}
            contexts.append({'frame_id':fid,'length':f['length'],
                'position_zero_based':f['position_zero_based'],'a_text_id':members[a],'b_text_id':members[b]})
        cooccurring=sorted(by_sign[a]&by_sign[b])
        pair_rows.append({'a':a,'b':b,'shared_frame_count':len(fids),
            'lengths':sorted({f['length'] for f in contexts}),
            'positions_zero_based':sorted({f['position_zero_based'] for f in contexts}),
            'contexts':contexts,'cooccurring_complete_text_count':len(cooccurring),
            'cooccurring_text_witnesses':[{'text_id':tid,
                'a_positions':[i for i,x in enumerate(text_map[tid]['sequence']) if x==a],
                'b_positions':[i for i,x in enumerate(text_map[tid]['sequence']) if x==b]}
                for tid in cooccurring]})
    signs={sign:{'distinct_text_count':len(by_sign[sign]),'token_count':sign_tokens[sign],
            'substitution_partner_count':len(neighbors[sign]),
            'observed_partner_members':sorted(neighbors[sign]),
            'shared_frame_count':len(sign_frames[sign]),'shared_frame_ids':sign_frames[sign],
            'repeated_sign_text_count':len(sign_repeat[sign]),
            'repeated_sign_text_witnesses':sign_repeat[sign]}
            for sign in sorted(by_sign)}
    cutoffs={}
    for minimum in [2,3,4,5]:
        sf=[f for f in shared if f['length']>=minimum]
        sp={pair for pair,fids in pairs.items() if any(frame_map[f]['length']>=minimum for f in fids)}
        cutoffs[minimum]={'unique_texts':sum(t['length']>=minimum for t in texts),
            'observed_signs':len({x for t in texts if t['length']>=minimum for x in t['sequence']}),
            'shared_frames':len(sf),'pair_edges':len(sp),
            'signs_with_edge':len({x for pair in sp for x in pair}),
            'pair_frame_incidences':sum(f['replacement_count']*(f['replacement_count']-1)//2 for f in sf),
            'largest_frame_replacement_count':max((f['replacement_count'] for f in sf),default=0)}
    wedge=find_open_wedge(neighbors,pairs)
    if wedge:
        wedge['first_ab_frame']=frame_map[wedge['ab_frame_ids'][0]]
        wedge['first_bc_frame']=frame_map[wedge['bc_frame_ids'][0]]
        for arm in ('ab','bc'):
            longer=[frame_map[fid] for fid in wedge[arm+'_frame_ids'] if frame_map[fid]['length']>=3]
            wedge[arm+'_illustration_length_ge_3']=min(longer,key=lambda f:(f['length'],f['frame_id'])) if longer else None
    summary={'source_rows':len(records),'unique_complete_texts':len(texts),
        'tokens_unique_texts':sum(sign_tokens.values()),'observed_signs':len(signs),
        'shared_frames':len(shared),'pair_edges':len(pairs),
        'pair_frame_incidences':sum(len(f) for f in pairs.values()),
        'signs_with_edge':sum(bool(x['substitution_partner_count']) for x in signs.values()),
        'signs_without_edge':sum(not x['substitution_partner_count'] for x in signs.values()),
        'edges_with_cooccurrence':sum(bool(p['cooccurring_complete_text_count']) for p in pair_rows),
        'pair_text_cooccurrence_incidences':sum(p['cooccurring_complete_text_count'] for p in pair_rows),
        'distinct_texts_with_same_sign_repeated':len({w['text_id'] for s in signs.values() for w in s['repeated_sign_text_witnesses']}),
        'signs_observed_repeating':sum(bool(s['repeated_sign_text_count']) for s in signs.values()),
        'edge_frame_count_histogram':dict(sorted(Counter(len(fs) for fs in pairs.values()).items())),
        'length_minimum_sensitivities':cutoffs,'open_wedge_witness':wedge,'signs':signs,
        'largest_shared_frames':sorted(shared,key=lambda f:(-f['replacement_count'],f['frame_id']))[:10]}
    return summary,texts,shared,pair_rows


def main():
    source='data/processed/lipi_strict.jsonl'
    records=read_jsonl(source)
    summary,texts,frames,pairs=audit(records)
    allowed_conditions=['Good','Fair','Fine']
    quality_rows=[r for r in records if r.get('condition') in allowed_conditions]
    quality,_,_,_=audit(quality_rows)
    quality={k:v for k,v in quality.items() if k not in ['signs','largest_shared_frames','open_wedge_witness']}
    quality['allowed_source_condition_values']=allowed_conditions
    quality['included_condition_counts']=dict(sorted(Counter(r['condition'] for r in quality_rows).items()))
    quality['excluded_source_rows']=len(records)-len(quality_rows)
    quality['interpretation']='Source-condition sensitivity only; rows are filtered before whole-text deduplication. A text survives if at least one source record has an allowed condition. No primary-image validation is implied. Main witness IDs are not reused for this recomputation.'
    summary['quality_sensitivity']=quality
    summary['input_hashes']={p:sha256(ROOT/p) for p in [source,'data/raw/lipi_inscriptions.csv']}
    summary['protocol']={
        'status':'Exploratory exhaustive descriptive enumeration; no permutation test or significance claim.',
        'input':'Existing strict complete single-line direction-marked transcription subset; filtering inherited from prepare_corpora.py.',
        'weighting':'One observation per distinct literal complete text; every associated source record retained in text ledger.',
        'edge':'Two distinct W signs fill exactly the same single masked position in complete texts of equal length.',
        'weight':'Number of distinct exact masked frames; not number of repeated objects or a probability.',
        'order':'Literal source file order; positions zero-based.',
        'cooccurrence':'Both distinct signs anywhere in the same complete text, counted once per pair/text, with all occurrence positions retained.',
        'same_sign_repetition':'At least two occurrences of identical W code within one complete text; one witness per sign/text.',
        'limits':['Exact shared contexts do not establish sound, meaning, grammatical class or allography.',
                  'Missing edges may reflect sparse data, selection or transcription, not impossibility.',
                  'Open-wedge closure is a graph operation, not evidence that its endpoints are equivalent.',
                  'Cooccurrence only contradicts a strong at-most-one-listed-member-per-whole-inscription rule; it does not contradict contextual substitution or allography.',
                  'Short frames can connect many signs and dominate graph density; length-cutoff summaries retain this sensitivity.',
                  'No M/P crosswalk, proposed semantic columns, graph clustering or sign merging is used.',
                  'Source complete/direction labels and W distinctions remain provisional; photos not individually audited here.']}
    summary['witness_files']={'texts':'results/substitution_network_texts.jsonl',
        'frames':'results/substitution_network_frames.jsonl','pairs':'results/substitution_network_pairs.jsonl',
        'pair_summary':'results/substitution_network_pairs.csv'}
    write_jsonl(summary['witness_files']['texts'],texts)
    write_jsonl(summary['witness_files']['frames'],frames)
    write_jsonl(summary['witness_files']['pairs'],pairs)
    write_csv(summary['witness_files']['pair_summary'],[{
        'a':p['a'],'b':p['b'],'shared_frame_count':p['shared_frame_count'],
        'lengths':';'.join(map(str,p['lengths'])),'positions_zero_based':';'.join(map(str,p['positions_zero_based'])),
        'cooccurring_complete_text_count':p['cooccurring_complete_text_count'],
        'frame_ids':';'.join(c['frame_id'] for c in p['contexts']),
        'cooccurring_text_ids':';'.join(c['text_id'] for c in p['cooccurring_text_witnesses'])} for p in pairs])
    write_json('results/substitution_network.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in ['signs','largest_shared_frames','open_wedge_witness','protocol','input_hashes','witness_files']},indent=2))


if __name__=='__main__':
    main()
