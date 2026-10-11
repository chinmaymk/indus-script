"""Validate the manually visually reviewed Table 1 and recompute its totals.

This audits published classifications, not the objects or their inscriptions.
No inference about vocabulary or sign values is made here.
"""
from collections import Counter, defaultdict
import json
from common import ROOT, sha256, write_json


def summarize(rows):
    ids = [r['cisi_id'] for r in rows]
    assert ids == [f'L-{n}' for n in range(124, 217)]
    assert len(set(ids)) == 93
    assert all(r['context'] in {'W', 'W1', 'W2', 'O', '?'} for r in rows)
    assert all(type(r['impressions']) is int and r['impressions'] > 0 for r in rows)
    by_context = Counter(r['context'] for r in rows)
    by_type = Counter(r['type'] for r in rows)
    cross = defaultdict(Counter)
    for r in rows:
        cross[r['context']][r['type']] += 1
    warehouse = [r for r in rows if r['context'] in {'W', 'W1', 'W2'}]
    reported_warehouse = [r for r in rows if r['context'] == 'W']
    return {
        'rows': len(rows),
        'context_counts': dict(sorted(by_context.items())),
        'type_counts': dict(sorted(by_type.items())),
        'context_by_type': {k: dict(sorted(v.items())) for k, v in sorted(cross.items())},
        'impression_count_distribution': dict(sorted(Counter(r['impressions'] for r in rows).items())),
        'sum_of_reported_impressions': sum(r['impressions'] for r in rows),
        'impressions_on_multiple_impression_objects': sum(r['impressions'] for r in rows if r['impressions'] > 1),
        'multiple_impression_objects': [r['cisi_id'] for r in rows if r['impressions'] > 1],
        'W_only_group': {
            'definition': 'Published W only; excluding seal-recurrence inference W1 and general-area W2',
            'rows': len(reported_warehouse),
            'type_counts': dict(sorted(Counter(r['type'] for r in reported_warehouse).items())),
            'single_impression_rows': sum(r['impressions'] == 1 for r in reported_warehouse),
            'multiple_impression_rows': sum(r['impressions'] > 1 for r in reported_warehouse),
            'sum_of_reported_impressions': sum(r['impressions'] for r in reported_warehouse),
        },
        'warehouse_group': {
            'definition': 'Published W + W1 + W2; different evidence levels retained',
            'rows': len(warehouse),
            'type_counts': dict(sorted(Counter(r['type'] for r in warehouse).items())),
            'single_impression_rows': sum(r['impressions'] == 1 for r in warehouse),
            'multiple_impression_rows': sum(r['impressions'] > 1 for r in warehouse),
            'sum_of_reported_impressions': sum(r['impressions'] for r in warehouse),
        },
        'prose_comparison': {
            'prose_context_counts': {'W': 35, 'W1': 18, 'W2': 11, 'O': 11, '?': 17},
            'prose_W2_basis': '64 minus 53 in printed p.72, not an explicit isolated W2 count',
            'prose_categories_sum': 92,
            'table_minus_prose': {k: by_context[k] - v for k, v in {'W': 35, 'W1': 18, 'W2': 11, 'O': 11, '?': 17}.items()},
        },
        'impression_prose_comparison': {
            'prose_printed_page': 82,
            'prose': {'total_impressions': 130, 'single_impression_objects': 63, 'impressions_on_multiple_impression_objects': 67},
            'table': {
                'total_impressions': sum(r['impressions'] for r in rows),
                'single_impression_objects': sum(r['impressions'] == 1 for r in rows),
                'impressions_on_multiple_impression_objects': sum(r['impressions'] for r in rows if r['impressions'] > 1),
            },
            'table_minus_prose': {
                'total_impressions': sum(r['impressions'] for r in rows) - 130,
                'single_impression_objects': sum(r['impressions'] == 1 for r in rows) - 63,
                'impressions_on_multiple_impression_objects': sum(r['impressions'] for r in rows if r['impressions'] > 1) - 67,
            },
            'status': 'Unresolved source inconsistency; no row repaired to match prose.',
        },
        'individual_prose_comparisons': [
            {
                'cisi_id': 'L-174', 'prose_printed_page': 80,
                'table_impressions': next(r['impressions'] for r in rows if r['cisi_id'] == 'L-174'),
                'prose_impressions': 2,
                'status': 'Explicit disagreement; table cell retained as 1. Two impressions from one seal are not two different matrices.',
            },
            {
                'cisi_id': 'L-209', 'prose_printed_page': 82,
                'table_context': next(r['context'] for r in rows if r['cisi_id'] == 'L-209'),
                'prose_context': 'not contextualized',
                'status': 'Possible difference of spatial precision: W2 is a general SRG3-area assignment, not an exact findspot. No reconciliation established.',
            },
        ],
        'limits': [
            'Impression counts are per clay object, not counts of script signs or unique seal matrices.',
            'W1 is assigned through recurring seal impressions, not independent excavated provenience.',
            'Types and contexts are the authors\' published classifications; this is not direct artifact examination.',
            'Question marks describe indeterminate discovery context, not uncertain transcription of the cell.',
            'No sign meanings, phonetic values, ancient owner identities or commodities are assigned.',
        ],
    }


def main():
    path = ROOT / 'data/processed/lothal_sealing_table.json'
    ledger = json.loads(path.read_text())
    for record in ledger['evidence_files']:
        assert sha256(ROOT / record['path']) == record['sha256'], record['path']
    result = summarize(ledger['rows'])
    result['input_sha256'] = sha256(path)
    result['source'] = ledger['source']
    write_json(ROOT / 'results/lothal_sealing_table_audit.json', result)
    print(json.dumps({k: result[k] for k in ('rows', 'context_counts', 'type_counts', 'sum_of_reported_impressions', 'prose_comparison')}, indent=2))


if __name__ == '__main__':
    main()
