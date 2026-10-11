"""Sharp omission bounds without assigning positions beside unknown spans.

Conditional on the exported occurrences being an injective subset of the primary
counted occurrences. This checks compatibility, not transcription authentication.
"""
from collections import Counter
import csv
import json
from common import ROOT, sha256, write_json

POSITIONS = ('solus', 'initial', 'medial', 'final')


def omission_bounds(primary, represented):
    if any(type(x) is not int or x < 0 for x in primary) or type(represented) is not int or represented < 0:
        raise ValueError('Counts must be nonnegative integers')
    total = sum(primary)
    if represented > total:
        raise ValueError('Export cannot be an injective subset of these counts')
    missing = total - represented
    return [{'minimum': max(0, p-represented), 'maximum': min(p, missing)} for p in primary]


def main():
    paths = ['data/processed/mahadevan_1977_table_i.csv',
             'data/processed/m77_candidate_records.jsonl',
             'data/processed/m77_candidate_strict.jsonl']
    primary = list(csv.DictReader((ROOT/paths[0]).open()))
    records = [json.loads(l) for l in (ROOT/paths[1]).read_text().splitlines()]
    strict = [json.loads(l) for l in (ROOT/paths[2]).read_text().splitlines()]
    # Table I includes doubtful legible readings. Count *M as M for this explicit
    # sensitivity comparison, while retaining every original uncertainty flag.
    all_counts = Counter(t['sign'] for r in records for t in r['tokens'] if t['sign'])
    strict_positions = {s: Counter() for s in all_counts}
    for r in strict:
        for i, s in enumerate(r['sequence']):
            key = 'solus' if len(r['sequence'])==1 else 'initial' if i==0 else 'final' if i==len(r['sequence'])-1 else 'medial'
            strict_positions[s][key] += 1
    rows = []
    violations = []
    for r in primary:
        sign = r['sign']; p = [int(r[k]) for k in POSITIONS]
        if sum(p) != int(r['total']):
            raise ValueError('Primary position/total mismatch')
        a = all_counts[sign]
        bounds = omission_bounds(p, a)
        q = strict_positions.get(sign, Counter())
        for k, n in zip(POSITIONS, p):
            if q[k] > n: violations.append({'sign':sign,'position':k,'primary':n,'strict':q[k]})
        rows.append({'sign': sign, 'primary_total': sum(p),
                     'export_named_occurrences_including_doubtful': a,
                     'conditional_missing_occurrences': sum(p)-a,
                     'primary_positions': dict(zip(POSITIONS,p)),
                     'conditional_missing_position_bounds': dict(zip(POSITIONS,bounds)),
                     'strict_candidate_positions': {k:q[k] for k in POSITIONS}})
    result = {
        'sources_sha256': {p:sha256(ROOT/p) for p in paths},
        'assumption': 'Each counted exported named-sign occurrence corresponds to a distinct primary occurrence of that same sign; doubtful readings included as in Table I. This is not proved corpus-wide.',
        'formula': 'For category p out of total T with A represented occurrences but unknown represented categories: max(0,p-A) <= missing_in_category <= min(p,T-A). Bounds are individually sharp; category missing counts must jointly sum to T-A.',
        'unknown_span_policy': '000 contributes no identified sign count. Its unknown length is not inferred. No endpoint allocation is made around damage.',
        'summary': {'inventory':len(rows), 'primary_named_occurrences':sum(r['primary_total'] for r in rows),
                    'export_named_occurrences':sum(all_counts.values()),
                    'conditional_missing_occurrences':sum(r['conditional_missing_occurrences'] for r in rows),
                    'signs_with_deficit':sum(r['conditional_missing_occurrences']>0 for r in rows),
                    'signs_completely_absent':sum(r['export_named_occurrences_including_doubtful']==0 for r in rows),
                    'strict_position_subset_violations':violations},
        'signs': rows,
        'limits': ['Count compatibility does not prove correct sequences, preserved boundaries or faithful source references.',
                   'Individually sharp category intervals are not independent free choices.',
                   'Cannot attribute every deficit to dropped lines: transcription, edition or convention differences remain possible.',
                   'These constraints establish neither semantic nor phonetic values.']}
    write_json('results/m77_omission_bounds.json',result)
    print(json.dumps(result['summary'],indent=2))
    print(json.dumps(sorted(rows,key=lambda r:r['conditional_missing_occurrences'],reverse=True)[:3],indent=2))


if __name__ == '__main__':
    main()
