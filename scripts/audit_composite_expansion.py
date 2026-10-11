"""All-sign one-token/two-token exact-frame screen; never assigns equality."""
from collections import Counter, defaultdict
import json
from common import ROOT, read_jsonl, sha256, write_json, write_jsonl
from audit_repetition_expansion import corpus


def screen(sequences):
    """Count distinct string/frame rewrites with a different-object witness."""
    singles=defaultdict(list)
    pairs=defaultdict(list)
    for seq,refs in sorted(sequences.items()):
        for i,sign in enumerate(seq):
            frame=(seq[:i],seq[i+1:])
            if frame!=((),()):
                singles[frame].append((sign,seq,i,sorted(set(refs))))
        for i in range(len(seq)-1):
            frame=(seq[:i],seq[i+2:])
            if frame!=((),()):
                pairs[frame].append((seq[i:i+2],seq,i,sorted(set(refs))))
    matches=[]
    for frame in sorted(singles.keys() & pairs.keys()):
        for sign,short,si,srefs in singles[frame]:
            for pair,long,li,lrefs in pairs[frame]:
                if not any(a!=b for a in srefs for b in lrefs):
                    continue
                matches.append({'target':sign,'replacement':list(pair),
                    'prefix':list(frame[0]),'suffix':list(frame[1]),
                    'outside_context_length':len(frame[0])+len(frame[1]),
                    'short_sequence':list(short),'long_sequence':list(long),
                    'short_token_index':si,'long_pair_index':li,
                    'short_references':srefs,'long_references':lrefs,
                    'target_retained_in_pair':sign in pair,
                    'same_reference_also_present':bool(set(srefs)&set(lrefs))})
    return matches


def verify_pairwise(sequences,matches):
    """Independent brute-force check by string pairs, without a frame index."""
    expected=set()
    for short,srefs in sequences.items():
        if len(short)<2:continue
        for long,lrefs in sequences.items():
            if len(long)!=len(short)+1 or not any(a!=b for a in srefs for b in lrefs):continue
            for i in range(len(short)):
                if short[:i]==long[:i] and short[i+1:]==long[i+2:]:
                    expected.add((short,long,i))
    actual={(tuple(m['short_sequence']),tuple(m['long_sequence']),m['short_token_index']) for m in matches}
    assert actual==expected
    assert len(actual)==len(matches)
    return len(expected)


def summarize(records,strict):
    seqs,n,excluded=corpus(records,strict)
    matches=screen(seqs)
    profiles=[]
    for number in range(1,418):
        sign=f'M{number:03d}';selected=[m for m in matches if m['target']==sign]
        profiles.append({'sign':sign,'matches':len(selected),
            'matches_context_at_least_two':sum(m['outside_context_length']>=2 for m in selected),
            'matches_without_target_in_pair':sum(not m['target_retained_in_pair'] for m in selected),
            'distinct_replacement_pairs':len({tuple(m['replacement']) for m in selected}),
            'semantic_value':None,'phonetic_value':None})
    return {'included_records':n,'distinct_strings':len(seqs),'excluded':excluded,
        'matches':matches,'match_count':len(matches),
        'independent_pairwise_matches_verified':verify_pairwise(seqs,matches),
        'matches_retaining_target_in_pair':sum(m['target_retained_in_pair'] for m in matches),
        'signs_with_matches':sum(r['matches']>0 for r in profiles),
        'signs_with_context_at_least_two':sum(r['matches_context_at_least_two']>0 for r in profiles),
        'context_length_distribution':dict(sorted(Counter(m['outside_context_length'] for m in matches).items())),
        'signs':profiles}


def main():
    path='data/processed/m77_candidate_records.jsonl'
    protocol='data/processed/composite_expansion_protocol.json'
    shape_path='data/processed/arch_component_review.json'
    primary_path='data/processed/composite_primary_review.json'
    records=read_jsonl(path)
    primary=json.loads((ROOT/primary_path).read_text())
    shapes=json.loads((ROOT/shape_path).read_text())
    for review in (primary,shapes):
        for pin in review['evidence_files']:
            p=ROOT/pin['path'];assert p.stat().st_size==pin['bytes'] and sha256(p)==pin['sha256']
    byref={r['source_reference']:r for r in records}
    for line in primary['lines']:
        if line['compare_with_export']:
            r=byref[line['reference']]
            assert [t['sign'] for t in r['tokens']]==line['tokens']
            assert int(r['source_direction_code'])==line['direction_code']
    write_jsonl('data/processed/composite_primary_lines.jsonl',primary['lines'])
    results={label:summarize(records,strict) for label,strict in
        [('complete_undoubted_export',False),('strict_candidate_sensitivity',True)]}
    metadata={r['source_reference']:{k:r[k] for k in ('id','source_doc_count','source_direction_code','source_object_code','strict_candidate')} for r in records}
    write_json('results/composite_expansion_audit.json',{
        'input_sha256':{p:sha256(ROOT/p) for p in (path,protocol,shape_path,primary_path)},
        'protocol':json.loads((ROOT/protocol).read_text()),
        'results':results,'reference_metadata':metadata,
        'primary_review':primary,'component_review':shapes,
        'selected_M317_test':{'eligible_primary_complete_fields':0,
            'status':'Untestable: sole indexed M317 field has loss and doubtful direction; no negative semantic inference'},
        'limits':['Selected secondary export with omissions and transcription errors; witnesses need primary checking.',
                  'Exact substitution does not imply semantic or phonetic equality.',
                  'Empty frames excluded; all matches are exploratory and dependent.',
                  'Different reference numbers do not guarantee independent ancient manufacture or texts.']})
    for label,r in results.items():
        print(label,json.dumps({k:v for k,v in r.items() if k not in ('matches','signs')}))


if __name__=='__main__':
    main()
