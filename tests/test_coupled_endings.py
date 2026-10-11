"""Synthetic-only validation: no real source or protocol access."""
from collections import Counter
import csv
from itertools import permutations, product
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_coupled_endings import (COLUMNS, analyze_families, coupled,
    support_upper_bounds, is_simple, sample_simple_stratum, length_strata, pair_support, permutation_maxima,
    prepare_artifacts, read_allowed_rows, sequence_families, shuffle_endings, write_new)

A, B, C = ('W001', 'W002'), ('W003', 'W004'), ('W001', 'W005')


def row(cisi='a', **overrides):
    r = {'id': '1.1', 'cisi': cisi, 'site': 'Mohenjo-daro', 'type': 'SEAL:S',
         'condition': 'Good', 'complete': 'Y', 'dir.': 'R/L', 'class': '',
         'signs': '3', 'text': '+010-001-002+'}
    r.update(overrides)
    return r


def families(stems, endings):
    return [{'stem': s, 'ending': e} for s, e in zip(stems, endings)]


class CoupledEndingsTest(unittest.TestCase):
    def test_whole_artifact_before_site_and_duplicate_family(self):
        records = [row('bad-site'), row('bad-site', site='Harappa'),
                   row('bad-seq'), row('bad-seq', text='+011-001-002+'),
                   row('bad-parse'), row('bad-parse', complete='N'),
                   row('other-site', site='Harappa'), row('a'), row('a'), row('b'),
                   row('a', type='TABLET', complete='N'),
                   row('short', signs='2', text='+001-002+'),
                   row('near', type='SEAL:S ')]
        artifacts, ledger, rows = prepare_artifacts(records)
        self.assertEqual([r['artifact'] for r in artifacts], ['a', 'b'])
        by_key = {r['artifact']: r for r in ledger}
        self.assertEqual(by_key['bad-site']['reasons'], ['inconsistent_site'])
        self.assertIn('inconsistent_complete_sequence', by_key['bad-seq']['reasons'])
        self.assertIn('not_marked_complete', by_key['bad-parse']['reasons'])
        self.assertEqual(by_key['other-site']['selection_reason'], 'site_not_Mohenjo-daro')
        self.assertEqual(by_key['short']['selection_reason'], 'sequence_shorter_than_3')
        f = sequence_families(artifacts)
        self.assertEqual(len(f), 1)
        self.assertEqual(len(f[0]['witnesses']), 2)
        self.assertEqual(f[0]['witnesses'][0]['source_rows'], [9, 10])
        self.assertEqual(len(rows), len(records))

    def test_fallback_grouping_all_missing_markers(self):
        records = [row(marker, id='same.' + str(i))
                   for i, marker in enumerate(('', '-', '--', '?', 'None', 'Unknown'))]
        artifacts, ledger, _ = prepare_artifacts(records)
        self.assertEqual(len(artifacts), 1)
        self.assertEqual(ledger[0]['artifact'], 'lipi_id:same')
        self.assertEqual(len(artifacts[0]['source_rows']), 6)

    def test_strict_parser_no_nr_exception_or_reversal(self):
        records = [row('valid'), row('nr', **{'dir.': 'NR'}),
                   row('unknown', text='+010-999-002+'), row('multi', **{'class': '2L'}),
                   row('count', signs='4'), row('damage', text='+010-001?-002+')]
        artifacts, ledger, _ = prepare_artifacts(records)
        self.assertEqual([a['artifact'] for a in artifacts], ['valid'])
        self.assertEqual(artifacts[0]['sequence'], ('W010', 'W001', 'W002'))
        reasons = {a['artifact']: a['reasons'] for a in ledger}
        self.assertIn('direction_not_R/L', reasons['nr'])
        self.assertIn('unknown_or_separator_token', reasons['unknown'])
        self.assertIn('multiline_class', reasons['multi'])
        self.assertIn('sign_count_mismatch', reasons['count'])
        self.assertIn('not_complete_simple_single_line', reasons['damage'])

    def test_column_whitelist_and_inert_missing_suffix(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'synthetic.csv'
            with p.open('w', newline='') as f:
                w = csv.writer(f)
                w.writerow([*COLUMNS, 'translation', 'symbol'])
                w.writerow([row()[c] for c in COLUMNS])
            self.assertEqual(list(read_allowed_rows(p)), [row()])
            p.write_text('id,id\n1,2\n')
            with self.assertRaises(ValueError):
                list(read_allowed_rows(p))

    def test_both_coordinates_required_collisions_collapse(self):
        stems = [('S',)] * 4 + [('T',)] * 2
        endings = [A, A, B, C, A, B]
        counts, witnesses = pair_support(stems, endings)
        self.assertEqual(counts[(A, B)], 2)
        self.assertEqual(witnesses[(A, B)], [('S',), ('T',)])
        self.assertNotIn((A, C), counts)
        self.assertFalse(coupled(A, ('W009', A[1])))
        self.assertEqual(pair_support([], []), ({}, {}))
        with self.assertRaises(ValueError):
            pair_support([()], [A])

    def test_collision_relaxed_bound_exhaustive_small_cases(self):
        # Every label assignment for three distinct slot structures, including
        # residual slots and duplicate edges; compare all distinct shuffles.
        structures = [[('S',), ('S',), ('T',), ('T',)],
                      [('S',), ('S',), ('S',), ('T',)],
                      [('S',), ('S',), ('S',), ('T',), ('T',)]]
        for stems in structures:
            for endings in product((A, B, C), repeat=len(stems)):
                maxima = Counter()
                for shuffled in set(permutations(endings)):
                    counts, _ = pair_support(stems, shuffled)
                    for pair, count in counts.items():
                        maxima[pair] = max(maxima[pair], count)
                for record in support_upper_bounds(stems, endings):
                    pair = tuple(record['endings'])
                    self.assertEqual(record['upper_bound'], maxima[pair])

    def test_crosslength_support_is_additive(self):
        stems = [('S',), ('S',), ('X', 'Y'), ('X', 'Y')]
        endings = [A, B, A, B]
        record = support_upper_bounds(stems, endings)[0]
        self.assertEqual(record['upper_bound'], 2)
        self.assertEqual([r['upper_bound'] for r in record['by_length']], [1, 1])
        self.assertEqual(pair_support(stems, endings)[0][(A, B)], 2)

    def test_shuffle_preserves_intact_endings_and_exact_lengths(self):
        stems = [('S',)] * 3 + [('X', 'Y')] * 3
        endings = [A, A, B, C, B, B]
        strata = length_strata(stems)
        rng = np.random.default_rng(1)
        for _ in range(30):
            shuffled = shuffle_endings(endings, strata, rng)
            for indices in strata:
                self.assertEqual(Counter(endings[i] for i in indices),
                                 Counter(shuffled[i] for i in indices))
        self.assertEqual(endings, [A, A, B, C, B, B])

    def test_null_max_includes_unobserved_pairs_from_simple_input(self):
        d = ('W003', 'W006')
        stems = [('S',)] * 2 + [('T',)] * 2 + [('U',)] * 2 + [('V',)] * 2
        endings = [A, C, A, C, B, d, B, d]
        self.assertTrue(is_simple(stems, endings))
        self.assertEqual(pair_support(stems, endings)[0], {})
        sampled = permutation_maxima(stems, endings, 30, 7)
        self.assertIn(2, sampled['maxima'])
        self.assertEqual(sampled, permutation_maxima(stems, endings, 30, 7))
        self.assertEqual(sampled['status'], 'completed')
        self.assertEqual(sampled['strata'][0]['accepted'], 30)
        with self.assertRaises(ValueError):
            permutation_maxima([('S',), ('S',)], [A, A], 3, 1)

    def test_simple_rejection_preserves_degrees_and_ending_counts(self):
        stems = [('S',), ('S',), ('T',), ('T',)]
        endings = [A, B, A, C]
        encoded, labels, info = sample_simple_stratum(
            stems, endings, 30, np.random.default_rng(1), 10000)
        self.assertTrue(info['complete'])
        self.assertGreater(info['rejected'], 0)
        for encoded_row in encoded:
            draw = [labels[int(i)] for i in encoded_row]
            self.assertTrue(is_simple(stems, draw))
            self.assertEqual(Counter(draw), Counter(endings))

    def test_multiple_lengths_sample_independently_and_combine_same_draw_index(self):
        stems = [('S',), ('S',), ('T',), ('T',), ('X', 'Y'), ('X', 'Y')]
        endings = [A, B, A, C, B, C]
        seed, replicates = 49, 20
        result = permutation_maxima(stems, endings, replicates, seed, 10000)
        self.assertEqual([r['length'] for r in result['strata']], [3, 4])
        self.assertEqual([r['accepted'] for r in result['strata']], [20, 20])
        rng = np.random.default_rng(seed)
        x, lx, _ = sample_simple_stratum(stems[:4], endings[:4], replicates, rng, 10000)
        y, ly, _ = sample_simple_stratum(stems[4:], endings[4:], replicates, rng, 10000)
        expected = []
        for i in range(replicates):
            draw = [lx[int(j)] for j in x[i]] + [ly[int(j)] for j in y[i]]
            self.assertTrue(is_simple(stems, draw))
            self.assertEqual(Counter(draw[:4]), Counter(endings[:4]))
            self.assertEqual(Counter(draw[4:]), Counter(endings[4:]))
            expected.append(max(pair_support(stems, draw)[0].values(), default=0))
        self.assertEqual(result['maxima'], expected)

    def test_conditioned_slot_permutations_have_constant_graph_multiplicity(self):
        stems = [('S',), ('S',), ('T',), ('T',)]
        endings = [A, B, A, C]
        graphs = Counter()
        for draw in set(permutations(endings)):
            if is_simple(stems, draw):
                graph = tuple(sorted(zip(stems, draw)))
                graphs[graph] += 1
        self.assertEqual(len(graphs), 2)
        self.assertEqual(set(graphs.values()), {4})  # 2! x 2! per simple graph

    def test_relaxed_bound_not_attainable_under_simple_constraint(self):
        stems = [(str(i),) for i in range(4) for _ in range(2)]
        endings = [A, C, A, C, B, C, B, C]
        self.assertTrue(is_simple(stems, endings))
        records = support_upper_bounds(stems, endings)
        ab = next(r for r in records if tuple(r['endings']) == (A, B))
        self.assertEqual(ab['upper_bound'], 2)
        simple = [draw for draw in set(permutations(endings)) if is_simple(stems, draw)]
        self.assertTrue(simple)
        self.assertEqual(max(pair_support(stems, draw)[0].get((A, B), 0)
                             for draw in simple), 0)

    def test_proposal_cap_gives_no_partial_p_values(self):
        f = families([('S',)] * 2 + [('T',)] * 2, [A, B, A, B])
        result = analyze_families(f, replicates=2, proposal_cap=1)
        self.assertEqual(result['status'], 'computationally_unavailable')
        self.assertIsNone(result['global_p'])
        self.assertEqual(result['candidates'], [])
        self.assertEqual(result['null_maxima'], [])
        self.assertEqual(result['completed_replicates'], 0)
        self.assertTrue(all(r['maxT_p'] is None for r in result['observed_pairs']))
        self.assertEqual(result['sampling_diagnostics'][0]['proposals'], 1)
        self.assertLess(result['sampling_diagnostics'][0]['accepted'], 2)

    def test_early_stop_skips_monte_carlo_and_p_null(self):
        with patch('analyze_coupled_endings.permutation_maxima', side_effect=AssertionError('No MC')):
            impossible = analyze_families(families([('S',), ('S',)], [A, B]), 9)
            self.assertEqual(impossible['status'], 'insufficient_support')
            self.assertIsNone(impossible['observed_pairs'][0]['maxT_p'])
            d = ('W003', 'W006')
            absent = analyze_families(families([('S',)] * 2 + [('T',)] * 2 + [('U',)] * 2 + [('V',)] * 2, [A, C, A, C, B, d, B, d]), 9)
            self.assertEqual(absent['status'], 'no_observed_support_at_least_2')
            self.assertIsNone(absent['global_p'])
            self.assertIsNone(absent['sampled_constant_null'])
            self.assertEqual(absent['completed_replicates'], 0)

    def test_maxT_denominator_and_constant_null_caution(self):
        f = families([('S',)] * 2 + [('T',)] * 2, [A, B, A, B])
        with patch('analyze_coupled_endings.permutation_maxima', return_value={'status': 'completed', 'strata': [], 'maxima': [0] * 99}):
            result = analyze_families(f, 99)
            self.assertEqual(result['global_p'], .01)
            self.assertEqual(result['observed_pairs'][0]['maxT_p'], .01)
            self.assertEqual(len(result['candidates']), 1)
            self.assertTrue(result['sampled_constant_null'])
            self.assertIn('not proof', result['caution'])
        with patch('analyze_coupled_endings.permutation_maxima', return_value={'status': 'completed', 'strata': [], 'maxima': [2] * 99}):
            result = analyze_families(f, 99)
            self.assertEqual(result['global_p'], 1.)
            self.assertEqual(result['candidates'], [])

    def test_exclusive_output(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'result.json'
            write_new(p, {'a': 1})
            with self.assertRaises(FileExistsError):
                write_new(p, {'a': 2})
            self.assertEqual(p.read_text().strip(), '{\n  "a": 1\n}')


if __name__ == '__main__':
    unittest.main()
