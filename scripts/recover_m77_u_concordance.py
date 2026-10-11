"""Recover separately indexed M328 lines without inflating repeated occurrences.

All inputs are manual primary reviews. Unknown visible glyphs, primary doubt,
and unknown-length physical loss remain different types. No semantic key is fit.
"""
from collections import Counter, defaultdict
import csv
import json
import re
from common import ROOT, sha256, write_json, write_jsonl, read_jsonl
from analyze_m77_u_fields import PILOTS, normalize, verify_fingerprints, simple_field

EXTENSIONS = ['data/processed/m77_u_extension_boundary.json',
              'data/processed/m77_u_extension_structure.json',
              'data/processed/m77_u_extension_iconography.json',
              'data/processed/m77_u_extension_parent.json']
CORRECTION = 'data/processed/m77_u_4316_primary_review.json'
CROSSCHECK = 'data/processed/m77_u_extension_crosscheck.json'


def validate_tokens(tokens):
    if not tokens:
        raise ValueError('Empty sequence')
    for t in tokens:
        if not re.fullmatch(r'\*?(?:M\d{3}|UNKNOWN)|LOSS',t):
            raise ValueError('Invalid token syntax '+t)
        base=t.lstrip('*')
        if base in ('UNKNOWN','LOSS'):
            if t=='*LOSS': raise ValueError('LOSS is not a doubt-marked glyph')
        elif not re.fullmatch(r'M\d{3}',base) or not 1<=int(base[1:])<=417:
            raise ValueError('Invalid token '+t)


def merge_sightings(rows):
    """A repeated R listing is one line, but each indexed U has a separate key."""
    lines={}; indexed=set()
    for r in rows:
        validate_tokens(r['tokens'])
        key=(str(r['reference']),str(r['side']),str(r['line']))
        index=r.get('indexed_M328_token_index_zero_based',r.get('indexed_U_position'))
        if not isinstance(index,int) or not 0<=index<len(r['tokens']) or r['tokens'][index].lstrip('*')!='M328':
            raise ValueError('Invalid indexed U '+str(key))
        if (*key,index) in indexed: raise ValueError('Duplicate indexed occurrence '+str((*key,index)))
        indexed.add((*key,index))
        if key in lines and lines[key]['tokens']!=r['tokens']:
            raise ValueError('Conflicting full-line transcriptions '+str(key))
        if key not in lines:
            tokens=r['tokens'].copy()
            lines[key]={'id':f'M77:{key[0]}:side{key[1]}:line{key[2]}',
                'reference':key[0],'side':key[1],'line':key[2], 'tokens':tokens,
                'has_primary_loss': 'LOSS' in tokens,
                'has_reviewer_unknown':any(t.lstrip('*')=='UNKNOWN' for t in tokens),
                'has_primary_doubt':any(t.startswith('*') for t in tokens),
                'full_sequence_primary_checked':bool(r['full_sequence_primary_checked']),
                'normalized_reading_order':'right_to_left',
                'actual_direction_code':None,
                'ancient_continuity_between_lines':'unknown; do not concatenate',
                'sightings':[]}
        lines[key]['sightings'].append({'pdf_page':r['pdf_page'],'printed_page':r['printed_page'],
            'indexed_U_position':index,'ledger':r['ledger'],
            'review_basis':r.get('review_basis','explicit extension review flag and ledger protocol'),
            'source_complete_line_flag':r.get('source_complete_line_flag',r.get('complete_line')),
            'source_notes':r.get('source_notes',r.get('notes',[])),
            'superseded_ledger':r.get('superseded_ledger')})
    return sorted(lines.values(),key=lambda r:(r['reference'],r['side'],r['line']))


def u_positions(tokens):
    """Position relative to all printed slots, including positive loss spans.

    Internal span extent does not affect initial/medial/final status. Whether
    Table I allocates damaged edges this way is a separately assessed convention.
    """
    return Counter('solus' if len(tokens)==1 else 'initial' if i==0 else
                   'final' if i==len(tokens)-1 else 'medial'
                   for i,t in enumerate(tokens) if t.lstrip('*')=='M328')


def export_comparisons(lines, candidate):
    by_ref=defaultdict(list)
    for r in lines:by_ref[r['reference']].append(r)
    comparisons=[]
    for ref,rs in sorted(by_ref.items()):
        c=candidate[ref]
        tokens=['LOSS' if t['unknown_span'] else ('*' if t['doubtful'] else '')+t['sign'] for t in c['tokens']]
        matches=[r['id'] for r in rs if r['tokens']==tokens]
        reviewed_count=sum(sum(t.lstrip('*')=='M328' for t in r['tokens']) for r in rs)
        exported_count=sum(t.lstrip('*')=='M328' for t in tokens)
        comparisons.append({'reference':ref, 'export_tokens':tokens,
            'reviewed_line_ids':[r['id'] for r in rs], 'exact_sequence_match_line_ids':matches,
            'line_identity_established_by_sequence_match':False,
            'reviewed_U_count':reviewed_count,'export_U_count':exported_count,
            'conditional_missing_U_count_lower_bound':max(0,reviewed_count-exported_count),
            'fully_identified_lines_different_from_export':[
                r['id'] for r in rs if r['full_sequence_primary_checked'] and
                not r['has_reviewer_unknown'] and r['tokens']!=tokens]})
    return comparisons


def main():
    verified={};rows=[];paths=PILOTS+EXTENSIONS+[CORRECTION,CROSSCHECK]
    docs={p:json.loads((ROOT/p).read_text()) for p in paths}
    for d in docs.values():verify_fingerprints(d,verified)
    for p in PILOTS:
        normalized=normalize(docs[p],p)
        originals=docs[p].get('rows',docs[p].get('records',[]))
        for row,original in zip(normalized,originals):
            row['review_basis']=('explicit source-row flag' if 'full_sequence_primary_checked' in original
                                 else 'primary visual-review protocol in source ledger; no explicit per-row flag')
            row['source_complete_line_flag']=original.get('complete_line')
            row['source_notes']=original.get('notes',original.get('note'))
        rows.extend(normalized)
    for p in EXTENSIONS:
        rows.extend(dict(r,ledger=p) for r in docs[p].get('rows',docs[p].get('records',[])))
    corrections=docs[CORRECTION]['rows']
    for correction in corrections:
        key=tuple(str(correction[k]) for k in ['reference','side','line'])
        hits=[i for i,r in enumerate(rows) if tuple(str(r[k]) for k in ['reference','side','line'])==key]
        if len(hits)!=1:raise ValueError('Correction must replace one existing sighting')
        previous=rows[hits[0]]
        rows[hits[0]]=dict(correction,ledger=CORRECTION,superseded_ledger=previous['ledger'])
    lines=merge_sightings(rows)
    incomplete_index=[]
    for r in lines:
        observed={s['indexed_U_position'] for s in r['sightings']}
        all_u={i for i,t in enumerate(r['tokens']) if t.lstrip('*')=='M328'}
        if observed!=all_u:incomplete_index.append(r['id'])
    if incomplete_index:raise ValueError('Some U tokens lack their own indexed sighting: '+str(incomplete_index))
    primary={r['sign']:r for r in csv.DictReader((ROOT/'data/processed/mahadevan_1977_table_i.csv').open())}
    positions=Counter();complete_positions=Counter();counts=Counter()
    for r in lines:
        positions.update(u_positions(r['tokens']))
        if not r['has_primary_loss']:complete_positions.update(u_positions(r['tokens']))
        counts.update(t.lstrip('*') for t in r['tokens'] if t.lstrip('*') not in ('LOSS','UNKNOWN'))
    conflicts={s:{'reviewed':n,'primary':int(primary[s]['total'])} for s,n in counts.items() if n>int(primary[s]['total'])}
    if conflicts:raise ValueError('Known-sign totals conflict with primary table: '+str(conflicts))
    expected_positions={k:int(primary['M328'][k]) for k in ['solus','initial','medial','final']}
    if len(rows)!=int(primary['M328']['total']) or counts['M328']!=len(rows):
        raise ValueError('Complete M328 concordance inventory does not match primary total')
    if dict(positions)!=expected_positions:
        raise ValueError('M328 positions require primary review; do not force a match')
    candidate={r['source_reference']:r for r in read_jsonl('data/processed/m77_candidate_records.jsonl')}
    comparisons=export_comparisons(lines,candidate)
    all_export_u=sum(t['sign']=='M328' for r in candidate.values() for t in r['tokens'])
    eligible=[r for r in lines if r['full_sequence_primary_checked'] and not
              (r['has_primary_loss'] or r['has_reviewer_unknown'] or r['has_primary_doubt'])]
    simple=Counter(simple_field(r['tokens']) for r in eligible if simple_field(r['tokens']) is not None)
    summary={'indexed_sightings':len(rows),'distinct_reviewed_lines':len(lines),
        'distinct_references':len({r['reference'] for r in lines}),
        'indexed_sightings_by_pdf_page':dict(sorted(Counter(r['pdf_page'] for r in rows).items())),
        'reviewed_M328_occurrences':counts['M328'],
        'primary_M328_total':int(primary['M328']['total']),
        'M328_positions_with_loss_spans_retained':dict(positions),
        'M328_positions_on_loss_free_lines':dict(complete_positions),
        'primary_M328_positions':{k:int(primary['M328'][k]) for k in ['solus','initial','medial','final']},
        'source_doubt_lines':sum(r['has_primary_doubt'] for r in lines),
        'source_loss_lines':sum(r['has_primary_loss'] for r in lines),
        'reviewer_unknown_lines':sum(r['has_reviewer_unknown'] for r in lines),
        'fully_identified_undoubted_loss_free_lines':len(eligible),
        'undoubted_two_sign_long_stroke_U_fields_by_graphic_count':dict(sorted(simple.items())),
        'graphic_counts_are_not_independently_established_numerical_values':True,
        'known_sign_occurrences':sum(counts.values()),'known_sign_types':len(counts),
        'export_M328_occurrences_all_references':all_export_u,
        'export_M328_occurrences_on_reviewed_references':sum(c['export_U_count'] for c in comparisons),
        'conditional_missing_U_lower_bound':sum(c['conditional_missing_U_count_lower_bound'] for c in comparisons),
        'export_U_positive_without_exact_reviewed_line_match':[c['reference'] for c in comparisons if c['export_U_count'] and not c['exact_sequence_match_line_ids']],
        'no_missing_indexed_sightings_in_recovered_lines':not incomplete_index,
        'new_semantic_or_phonetic_values':0}
    write_jsonl('data/processed/m77_u_recovered_lines.jsonl',lines)
    write_json('results/m77_u_recovery_audit.json',{'summary':summary,
        'inputs_sha256':{p:sha256(ROOT/p) for p in paths+['data/processed/m77_candidate_records.jsonl','data/processed/mahadevan_1977_table_i.csv']},
        'verified_source_fingerprints':verified,'export_comparisons':comparisons,
        'known_counts_by_sign':dict(sorted(counts.items())),
        'limits':['Manual glyph identification is not proved by count agreement.',
                  'Missing-count bounds assume matching reference identities and injective, correctly identified exported U tokens.',
                  'A matching string is not proof of a particular side/line when export lacks those identifiers.',
                  'Same catalogue reference is not guaranteed physical independence from another reference.',
                  'This sign-selected corpus is unsuitable for unbiased population language tests.',
                  'The original export and strict candidate subset are unchanged.']})
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
