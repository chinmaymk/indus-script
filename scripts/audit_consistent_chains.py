"""Require one middle-string parse when composing two relation-template matches.

Three-string feasibility is weaker than a globally consistent segmentation and
does not establish that the bundles represent names or that the links are kinship.
"""
from collections import Counter, defaultdict
import json
from common import ROOT, sha256, write_json
from analyze_m77_foreign import sequence


def parse_key(parse):
    return tuple(parse['left']), tuple(parse['right'])


def compose_paths(witnesses):
    incoming, outgoing = defaultdict(list), defaultdict(list)
    seen = set()
    for w in witnesses:
        key = tuple((tuple(w[side]['sequence']), parse_key(w[side]))
                    for side in ['first', 'second'])
        if key in seen:
            raise ValueError('Duplicate pair witness would inflate realization counts')
        seen.add(key)
        incoming[tuple(w['second']['sequence'])].append(w)
        outgoing[tuple(w['first']['sequence'])].append(w)
    triples = {}
    for middle in sorted(incoming.keys() & outgoing.keys()):
        for ab in incoming[middle]:
            a = tuple(ab['first']['sequence'])
            for bc in outgoing[middle]:
                c = tuple(bc['second']['sequence'])
                if len({a, middle, c}) != 3:
                    continue
                key = (a, middle, c)
                row = triples.setdefault(key, {
                    'strings': [list(a), list(middle), list(c)],
                    'pair_witness_combinations': 0,
                    'compatible_parse_realizations': 0,
                    'incoming_middle_parses': set(),
                    'outgoing_middle_parses': set(),
                    'compatible_realizations': [],
                })
                row['pair_witness_combinations'] += 1
                row['incoming_middle_parses'].add(parse_key(ab['second']))
                row['outgoing_middle_parses'].add(parse_key(bc['first']))
                if parse_key(ab['second']) == parse_key(bc['first']):
                    row['compatible_parse_realizations'] += 1
                    row['compatible_realizations'].append([
                        ab['first'], ab['second'], bc['second']])
    rows = []
    for key in sorted(triples):
        row = triples[key]
        for field in ['incoming_middle_parses', 'outgoing_middle_parses']:
            row[field] = [{'left': list(l), 'right': list(r)}
                          for l, r in sorted(row[field])]
        rows.append(row)
    lengths = Counter((len(p[1]['left']), len(p[1]['right']))
                      for row in rows for p in row['compatible_realizations'])
    return {
        'naive_distinct_ordered_triples': len(rows),
        'compatible_distinct_ordered_triples': sum(
            r['compatible_parse_realizations'] > 0 for r in rows),
        'incompatible_distinct_ordered_triples': sum(
            r['compatible_parse_realizations'] == 0 for r in rows),
        'pair_witness_combinations': sum(r['pair_witness_combinations'] for r in rows),
        'compatible_parse_realizations': sum(r['compatible_parse_realizations'] for r in rows),
        'middle_bundle_lengths_by_realization': [
            {'left_length': l, 'right_length': r, 'realizations': count}
            for (l, r), count in sorted(lengths.items())],
        'triples': rows,
    }


def main():
    source = 'results/relation_template_audit.json'
    data = json.loads((ROOT / source).read_text())
    controls = []
    for row in data['all_417_controls']:
        result = compose_paths(row['witnesses'])
        controls.append({'marker': row['marker'], 'template': row['template'],
                         'eligible_strings': row['eligible_unique_strings'], **result})
    primary_path = 'data/processed/consistent_chain_primary_review.json'
    primary = json.loads((ROOT / primary_path).read_text())
    for item in primary['evidence_files']:
        path = ROOT / item['path']
        assert path.stat().st_size == item['bytes'] and sha256(path) == item['sha256'], item['path']
    corpus = [json.loads(line) for line in (ROOT / 'data/processed/m77_candidate_records.jsonl').read_text().splitlines()]
    for checked in primary['rows']:
        matches = [r for r in corpus if r['source_reference'] == checked['reference']]
        assert len(matches) == 1 and list(sequence(matches[0])) == checked['tokens']
    checked_strings = [r['tokens'] for r in primary['rows']]
    checked_control = next(r for r in controls if r['marker'] == primary['marker']
                           and r['template'] == primary['template'])
    checked_match = [t for t in checked_control['triples'] if t['strings'] == checked_strings]
    assert len(checked_match) == 1 and checked_match[0]['compatible_parse_realizations'] == 1
    measures = ['naive_distinct_ordered_triples', 'compatible_distinct_ordered_triples',
                'incompatible_distinct_ordered_triples', 'pair_witness_combinations',
                'compatible_parse_realizations']
    totals = {}
    for template in ['prefix', 'internal', 'suffix']:
        rows = [r for r in controls if r['template'] == template]
        totals[template] = {k: sum(r[k] for r in rows) for k in measures}
        totals[template]['markers_with_naive_triples'] = sum(
            r['naive_distinct_ordered_triples'] > 0 for r in rows)
        totals[template]['markers_with_compatible_triples'] = sum(
            r['compatible_distinct_ordered_triples'] > 0 for r in rows)
    result = {
        'status': 'Exploratory three-string segmentation feasibility, not semantic identification',
        'samples': data['samples'],
        'totals_summed_over_markers': totals,
        'all_417_by_3_templates': controls,
        'limitations': [
            'Counts share strings, signs and hypotheses; not independent observations or p-values',
            'Feasible triples may require incompatible segmentations across different triples',
            'String inequality does not establish archaeological independence',
            'No name, kinship or descent direction follows from any path',
            'Three distinct strings required: closed two-string walks are excluded',
            'Zero paths does not refute a kinship hypothesis in a sparse sample',
        ],
        'new_semantic_values': 0,
        'new_phonetic_values': 0,
        'primary_checked_triple': {
            'references_in_chain_order': [r['reference'] for r in primary['rows']],
            'result': checked_match[0],
            'scope': primary['scope'],
        },
        'input_sha256': {name: sha256(ROOT / name) for name in [source,
            primary_path,
            'data/processed/consistent_chain_protocol.json',
            'scripts/audit_relation_templates.py', 'data/processed/m77_candidate_records.jsonl']},
    }
    write_json('results/consistent_chain_audit.json', result)
    print(json.dumps(totals, indent=2))


if __name__ == '__main__':
    main()
