"""Check key comb-context claims directly from all row pairs, without audit imports."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    corpus_path = ROOT / 'data/processed/lipi_strict.jsonl'
    output_path = ROOT / 'results/comb_family_contexts.json'
    corpus = [json.loads(line) for line in corpus_path.read_text().splitlines()]
    reported = json.loads(output_path.read_text())
    for p, digest in reported['input_sha256'].items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == digest, p
    codes = {'W525', 'W526', 'W527'}
    selected = [r for r in corpus if codes.intersection(r['sequence'])]
    assert selected == reported['selected_rows']
    checked = {}
    for code in sorted(codes):
        rows = [r for r in selected if code in r['sequence']]
        strings = {tuple(r['sequence']) for r in rows}
        summary = reported['summary_by_code'][code]
        assert len(rows) == summary['row_count']
        assert len(strings) == summary['distinct_whole_strings']
        for field in ('site', 'type', 'preservation'):
            assert dict(Counter(r[field] for r in rows)) == summary['all_rows']['metadata_row_counts'][field]
        # Determine reading-edge category directly in file coordinates.
        def categories(sequences):
            values = []
            for seq in sequences:
                for i, token in enumerate(seq):
                    if token == code:
                        values.append('singleton' if len(seq) == 1 else 'final' if i == 0 else 'initial' if i == len(seq)-1 else 'medial')
            return dict(Counter(values))
        row_cats = categories([r['sequence'] for r in rows])
        assert row_cats == summary['all_rows']['occurrence_position_counts']['category']
        assert categories(strings) == summary['one_per_distinct_whole_string']['occurrence_position_counts']['category']
        checked[code] = {'rows': len(rows), 'strings': len(strings), 'categories': row_cats}
    direct_pairs = []
    for a in selected:
        if 'W525' not in a['sequence']:
            continue
        for b in corpus:
            if len(a['sequence']) != len(b['sequence']):
                continue
            differences = [(x, y) for x, y in zip(a['sequence'], b['sequence']) if x != y]
            if len(differences) == 1 and differences[0][0] == 'W525' and differences[0][1] in ('W526', 'W527'):
                direct_pairs.append((a['id'], b['id']))
    assert direct_pairs == reported['exact_counterpart_sequence_pairs'] == []
    assert not [r for r in selected if len(codes.intersection(r['sequence'])) > 1]
    assert not [r for r in selected if any(r['sequence'].count(c) > 1 for c in codes)]
    for name, rows in [('shared_site_type_length_strata', selected),
                       ('retrospective_H1123_exclusion_strata', [r for r in selected if r['cisi_original'] != 'H-1123'])]:
        key = lambda r: (r['site'], r['type'], len(r['sequence']))
        keys = {key(r) for r in rows}
        shared = {k for k in keys if any(key(r) == k and 'W525' in r['sequence'] for r in rows)
                  and any(key(r) == k and {'W526', 'W527'}.intersection(r['sequence']) for r in rows)}
        assert len(keys) == reported[name]['observed_strata'] == 35
        assert len(shared) == reported[name]['shared_strata'] == 1
        for entry in reported[name]['strata']:
            k = (entry['site'], entry['type'], entry['token_length'])
            assert entry['shared'] == (k in shared)
            for side, targets in [('W525', {'W525'}), ('W526_or_W527', {'W526', 'W527'})]:
                members = [r for r in rows if key(r) == k and targets.intersection(r['sequence'])]
                assert members == entry[side]['rows']
    final_w525 = [r['id'] for r in selected if r['sequence'][0] == 'W525']
    assert final_w525 == ['313.1']
    sensitivity = reported['retrospective_H1123_exclusion_W525_distribution']
    assert sensitivity['row_count'] == 9 and sensitivity['distinct_whole_strings'] == 5
    assert sensitivity['all_row_positions']['category'] == {'medial': 9}
    result = {'all_checks_passed': True, 'summary': checked, 'exact_replacement_pairs': direct_pairs,
              'sole_final_W525_row': final_w525, 'shared_strata': 1,
              'method': 'No audit imports; direct unequal-position scan over selected-vs-all row pairs; edge categories in original file coordinates; independent set-based strata and full member-list checks.',
              'scope': 'Computational agreement, not direction certification, artifact identity, allography or meaning.',
              'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (corpus_path, output_path)},
              'established_semantic_values': 0, 'established_phonetic_values': 0}
    (ROOT / 'results/comb_family_contexts_independent.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Comb-family counts, exact-counterpart null, sole final W525 and all shared-stratum members independently agree.')


if __name__ == '__main__':
    main()
