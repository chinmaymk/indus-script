"""Check and serialize hand-reviewed lines without overwriting source corpora.

Image identity is a documented human/model visual judgment, not proved by this
validator. The checks protect boundaries, uncertainty and primary count constraints.
"""
from collections import Counter
import csv
import json
from common import ROOT, sha256, write_json


def verify_fingerprints(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            if sha256(ROOT/value['path']) != value['sha256']:
                raise ValueError('Stale reviewed file: '+value['path'])
        for x in value.values(): verify_fingerprints(x)
    elif isinstance(value, list):
        for x in value: verify_fingerprints(x)


def normalize_segments(segments):
    out=[]
    for s in segments:
        if s['kind']=='unknown_span':
            out.append({'kind':'unknown_span', 'sign':None, 'minimum_signs':1, 'maximum_signs':None})
        elif s['kind']=='identified_sign':
            sign=s.get('mahadevan_id',s.get('sign'))
            if sign not in {f'M{i:03d}' for i in range(1,418)}:
                raise ValueError('Invalid primary sign ID')
            out.append({'kind':'identified_sign', 'sign':sign,
                        'doubtful':s.get('primary_doubtful_asterisk_observed',s.get('doubtful_in_printed_source',False))})
        else:
            raise ValueError('Unsupported reviewed segment kind')
    return out


def main():
    names=['data/processed/m77_1001_recovered_lines.json','data/processed/m77_2405_recovered_lines.json']
    docs=[json.loads((ROOT/p).read_text()) for p in names]
    for d in docs:verify_fingerprints(d)
    records=[]
    for ref,doc,path in zip(('1001','2405'),docs,names):
        for line in doc.get('entries',doc.get('lines',[])):
            side=str(line.get('side_code',doc.get('metadata',{}).get('side_code')))
            direction=str(line.get('original_direction_code',line.get('direction_code')))
            segments=normalize_segments(line['segments'])
            record={'reference':ref,'side':side,'line':str(line['line_code']),
                    'original_direction_code':direction,'normalized_reading_order':'right_to_left',
                    'segments':segments,'review_ledger':path,
                    'complete_printed_sequence':not any(s['kind']=='unknown_span' for s in segments),
                    'ancient_continuity_between_lines':'unknown; do not concatenate'}
            record['id']=f'M77:{ref}:side{side}:line{record["line"]}'
            records.append(record)
    if len({r['id'] for r in records})!=len(records):raise ValueError('Repeated side-line key')
    primary={r['sign']:r for r in csv.DictReader((ROOT/'data/processed/mahadevan_1977_table_i.csv').open())}
    counts=Counter();complete_positions=Counter()
    for r in records:
        counts.update(s['sign'] for s in r['segments'] if s['sign'])
        if not r['complete_printed_sequence']:continue
        seq=[s['sign'] for s in r['segments']]
        for i,s in enumerate(seq):
            pos='solus' if len(seq)==1 else 'initial' if i==0 else 'final' if i==len(seq)-1 else 'medial'
            complete_positions[s,pos]+=1
    for sign,n in counts.items():
        if n>int(primary[sign]['total']):raise ValueError('Recovered counts exceed full primary total: '+sign)
    for (sign,pos),n in complete_positions.items():
        if n>int(primary[sign][pos]):raise ValueError(f'Position conflict requiring image review: {sign} {pos} {n}>{primary[sign][pos]}')
    exported={r['source_reference']:r for r in [json.loads(l) for l in (ROOT/'data/processed/m77_candidate_records.jsonl').read_text().splitlines()]}
    comparisons=[]
    for ref in ('1001','2405'):
        lines=[r for r in records if r['reference']==ref]
        first='+'+'-'.join('000' if s['sign'] is None else ('*' if s.get('doubtful') else '')+s['sign'][1:] for s in lines[0]['segments'])+'+'
        if first!=exported[ref]['diplomatic']:raise ValueError('Reviewed first line no longer matches export')
        comparisons.append({'reference':ref,'reviewed_line_count':len(lines),'first_line_matches_export':True,
                            'additional_lines_absent_from_export':len(lines)-1})
    (ROOT/'data/processed/m77_primary_recovered_lines.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
    summary={'lines':len(records),'complete_printed_sequences':sum(r['complete_printed_sequence'] for r in records),
             'identified_sign_positions':sum(counts.values()),'distinct_identified_signs':len(counts),
             'unknown_spans':sum(s['kind']=='unknown_span' for r in records for s in r['segments']),
             'comparisons':comparisons,'complete_line_position_check':'No count exceeds the full primary positional marginal; compatibility does not prove identity.'}
    write_json('results/m77_primary_recovery_audit.json',{'summary':summary,
        'ledger_sha256':{p:sha256(ROOT/p) for p in names},
        'scope':'Selected, visually reviewed primary lines. Separate from the unmodified canonical corpus and strict subset. No sounds or meanings assigned.'})
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
