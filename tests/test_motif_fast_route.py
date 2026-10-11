"""Synthetic-only checks: never open the real corpus or calculate its associations."""
import itertools
import json
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_motif_fast_route import (eligible_pairs, greater_equal_with_roundoff,
    holm, make_design, moments,
    parse_row, permutation_z, prepare_artifacts, read_allowed_rows,
    run_discovery, run_fixed_transfer, sequence_families, shuffle_indices,
    write_new, COLUMNS)

ABSENT = ['', '-', '--', '?', 'None', 'Unknown']


def row(id='1', cisi='a', site='MD', motif='Unicorn', text='+001-002+', **overrides):
    value = {'id': id, 'cisi': cisi, 'site': site, 'type': 'SEAL:S',
             'condition': 'Good', 'complete': 'Y', 'dir.': 'R/L',
             'class': '', 'signs': str(len(text[1:-1].split('-'))),
             'text': text, 'symbol': motif}
    value.update(overrides)
    return value


def family(sequence, motifs):
    return {'sequence': sequence, 'length': len(sequence), 'motifs': motifs,
            'artifact_count': 1}


class MotifFastRouteTest(unittest.TestCase):
    def test_entire_conflicting_or_invalid_artifact_dropped(self):
        rows = [row(cisi='motif'), row(cisi='motif', motif='Bull'),
                row(cisi='site'), row(cisi='site', site='H'),
                row(cisi='sequence'), row(cisi='sequence', text='+001-003+'),
                row(cisi='invalid'), row(cisi='invalid', complete='N'),
                row(cisi='absent'), row(cisi='absent', motif='Unknown'),
                row(cisi='valid'), row(cisi='valid', type='TABLET', complete='N')]
        artifacts, ledger = prepare_artifacts(rows, ABSENT)
        self.assertEqual([a['artifact'] for a in artifacts], ['valid'])
        reasons = {r['artifact']: r['reasons'] for r in ledger}
        self.assertIn('inconsistent_raw_motif', reasons['motif'])
        self.assertIn('inconsistent_site', reasons['site'])
        self.assertIn('inconsistent_complete_sequence', reasons['sequence'])
        self.assertIn('not_marked_complete', reasons['invalid'])
        self.assertIn('absent_motif', reasons['absent'])

    def test_nr_only_single_literal_and_no_unknown_token(self):
        self.assertEqual(parse_row(row(text='+001+', **{'dir.': 'NR'})), (['W001'], []))
        self.assertIn('direction_not_R/L', parse_row(row(**{'dir.': 'NR'}))[1])
        self.assertIn('unknown_or_separator_token', parse_row(row(text='+999+', **{'dir.': 'NR'}))[1])
        self.assertTrue(parse_row(row(text='+001?+', **{'dir.': 'NR'}))[1])

    def test_duplicates_do_not_dominate_mixed_motif_vector(self):
        rows = [row(cisi='a')] * 100 + [row(cisi='b', motif='Bull'), row(cisi='c', motif='Bull')]
        artifacts, _ = prepare_artifacts(rows, ABSENT)
        families = sequence_families(artifacts, 'MD')
        self.assertEqual(len(families), 1)
        self.assertEqual(families[0]['artifact_count'], 3)
        self.assertEqual(families[0]['motifs'], {'Bull': 2 / 3, 'Unicorn': 1 / 3})
        self.assertEqual(sum(families[0]['motifs'].values()), 1.)

    def test_fallback_id_groups_sides_before_exclusion(self):
        artifacts, ledger = prepare_artifacts([row(id='a.1', cisi='None'),
                                               row(id='a.2', cisi='', motif='Bull')], ABSENT)
        self.assertEqual(artifacts, [])
        self.assertEqual(ledger[0]['artifact'], 'lipi_id:a')

    def test_quality_applied_after_whole_group_and_recomputes_vectors(self):
        rows = [row(cisi='a'), row(cisi='a', condition='Poor'),
                row(cisi='b', motif='Bull', condition='Fair'),
                row(cisi='bad', condition='Good'),
                row(cisi='bad', motif='Bull', condition='Poor')]
        artifacts, _ = prepare_artifacts(rows, ABSENT)
        self.assertEqual(sequence_families(artifacts, 'MD')[0]['motifs'],
                         {'Bull': .5, 'Unicorn': .5})
        self.assertEqual(sequence_families(artifacts, 'MD', good_fair=True)[0]['motifs'],
                         {'Bull': 1.})

    def test_scope_and_quality_are_exact_export_codes(self):
        artifacts, _ = prepare_artifacts([row(cisi='a', type='SEAL:S '),
                                          row(cisi='b', condition='Good ')], ABSENT)
        self.assertEqual([a['artifact'] for a in artifacts], ['b'])
        self.assertEqual(sequence_families(artifacts, 'MD', True), [])

    def test_exact_variance_matches_exhaustive_shuffle_distribution(self):
        f = np.array([[1., 0], [1, 1], [0, 1], [0, 0], [1, 1]])
        y = np.array([[0., 1], [.3, .7], [1, 0], [.5, .5], [.9, .1]])
        strata = [np.arange(4), np.array([4])]
        covariance, variance = moments(f, y, strata)
        brute = []
        for order in itertools.permutations(range(4)):
            yp = y[list(order) + [4]]
            brute.append(moments(f, yp, strata)[0])
        np.testing.assert_allclose(np.mean(brute, axis=0), 0., atol=1e-15)
        np.testing.assert_allclose(np.var(brute, axis=0), variance, atol=1e-15)
        np.testing.assert_allclose(covariance, f[:4].T @ (y[:4] - y[:4].mean(axis=0)))

    def test_permutations_preserve_length_and_whole_vectors(self):
        families = [family(['W001', 'W002'], {'A': .2, 'B': .8}),
                    family(['W003', 'W004'], {'A': .7, 'B': .3}),
                    family(['W001'], {'A': 1.}), family(['W002'], {'B': 1.})]
        design = make_design(families)
        rng = np.random.default_rng(7)
        for _ in range(20):
            order = shuffle_indices(design['strata'], 4, rng)
            np.testing.assert_array_equal(design['lengths'][order], design['lengths'])
            np.testing.assert_allclose(design['y'][order].sum(axis=0), design['y'].sum(axis=0))
            for indices in design['strata']:
                self.assertEqual(sorted(map(tuple, design['y'][order[indices]])),
                                 sorted(map(tuple, design['y'][indices])))

    def test_permutation_batches_reproduce_seed_and_statistic(self):
        families = [family(['W001', 'W002'], {'A': .2, 'B': .8}),
                    family(['W003', 'W004'], {'A': .7, 'B': .3}),
                    family(['W001', 'W004'], {'A': 1.}),
                    family(['W002', 'W003'], {'B': 1.})]
        d = make_design(families)
        pairs = [(0, 0), (1, 1)]
        a = np.concatenate(list(permutation_z(d, pairs, 17, 12, batch_size=3)))
        b = np.concatenate(list(permutation_z(d, pairs, 17, 12, batch_size=8)))
        np.testing.assert_allclose(a, b, atol=1e-14)
        rng = np.random.default_rng(12)
        direct = []
        for _ in range(17):
            order = shuffle_indices(d['strata'], 4, rng)
            c, v = moments(d['f'], d['y'][order], d['strata'])
            direct.append([c[i, j] / np.sqrt(v[i, j]) for i, j in pairs])
        np.testing.assert_allclose(a, direct, atol=1e-14)

    def test_holm_includes_untestable_candidate_at_one(self):
        np.testing.assert_allclose(holm([.02, .01, 1., .04]), [.06, .04, 1., .08])
        self.assertEqual(holm([]), [])
        with self.assertRaises(ValueError):
            holm([float('nan')])

    def test_float_ties_match_exact_rational_shuffle_ordering(self):
        from fractions import Fraction
        amounts = [Fraction(1, 10), Fraction(2, 10), Fraction(7, 10), Fraction(4, 10)]
        families = [family([('W001' if i in (0, 2) else 'W002'), f'W{i + 100:03d}'],
                           {'A': float(a), 'B': float(1 - a)}) for i, a in enumerate(amounts)]
        d = make_design(families)
        a, b = d['signs'].index('W001'), d['motifs'].index('A')
        observed = d['covariance'][a, b] / np.sqrt(d['variance'][a, b])
        exact_observed = amounts[0] + amounts[2] - sum(amounts) / 2
        rng = np.random.default_rng(48)
        exact = []
        for _ in range(99):
            order = shuffle_indices(d['strata'], 4, rng)
            exact.append(amounts[order[0]] + amounts[order[2]] - sum(amounts) / 2 >= exact_observed)
        sampled = np.concatenate(list(permutation_z(d, [(a, b)], 99, 48))).ravel()
        np.testing.assert_array_equal(greater_equal_with_roundoff(sampled, observed), exact)
        self.assertTrue(greater_equal_with_roundoff(np.nextafter(observed, -np.inf), observed))
        self.assertFalse(greater_equal_with_roundoff(observed - 1e-7, observed))

    def test_disjoint_transfer_sequences_and_quality(self):
        artifacts, _ = prepare_artifacts([
            row(cisi='a', site='MD'), row(cisi='b', site='H'),
            row(cisi='c', site='H', text='+002-001+'),
            row(cisi='d', site='H', text='+001-003+', condition='Poor')], ABSENT)
        seen = [f['sequence'] for f in sequence_families(artifacts, 'MD')]
        transfer = sequence_families(artifacts, 'H', excluded_sequences=seen)
        self.assertEqual(len(transfer), 2)
        self.assertTrue(set(map(tuple, seen)).isdisjoint(tuple(f['sequence']) for f in transfer))
        quality = sequence_families(artifacts, 'H', True, seen)
        self.assertEqual([f['sequence'] for f in quality], [['W002', 'W001']])

    def test_null_invalid_support_and_zero_variance_are_not_negative_findings(self):
        families = [family(['W001', f'W{i + 100:03d}'], {'A': 1.}) for i in range(12)]
        d = make_design(families)
        self.assertFalse(eligible_pairs(d).any())
        candidates = [{'sign': 'W001', 'raw_motif': 'A'}, {'sign': 'W099', 'raw_motif': 'B'}]
        result = run_fixed_transfer(families, candidates, 9, 1)
        self.assertEqual(result['tested_candidates'], 0)
        self.assertEqual(result['holm_family_size'], 2)
        for r in result['candidates']:
            self.assertEqual(r['status'], 'insufficient_configured_support')
            self.assertIsNone(r['z'])
            self.assertEqual(r['holm_p'], 1.)
        self.assertEqual(run_discovery(families, 9, 1)['status'], 'no_eligible_pairs')
        self.assertEqual(run_fixed_transfer([], candidates, 9, 1)['tested_candidates'], 0)

    def test_synthetic_discovery_and_fixed_transfer(self):
        families = [family([('W001' if i < 10 else 'W002'), f'W{i + 100:03d}'],
                           {'A' if i < 10 else 'B': 1.}) for i in range(20)]
        result = run_discovery(families, 199, 77)
        self.assertEqual(len(result['null_max_positive_z']), 199)
        self.assertTrue(1 <= len(result['candidates']) <= 5)
        self.assertTrue(all(r['z'] > 0 and r['maxT_p'] <= .01 for r in result['candidates']))
        transfer = run_fixed_transfer(families, result['candidates'], 199, 78)
        self.assertEqual(transfer['tested_candidates'], len(result['candidates']))
        self.assertEqual(transfer['holm_family_size'], len(result['candidates']))

    def test_ingestion_excludes_unconfigured_fields_and_freeze_cannot_overwrite(self):
        import csv
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'synthetic.csv'
            with source.open('w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[*COLUMNS, 'translation'])
                writer.writeheader(); writer.writerow({**row(), 'translation': 'never import'})
            self.assertEqual(set(next(read_allowed_rows(source))), set(COLUMNS))
            frozen = Path(tmp) / 'frozen.json'
            write_new(frozen, {'candidates': []})
            original = frozen.read_bytes()
            with self.assertRaises(FileExistsError):
                write_new(frozen, {'candidates': ['changed']})
            self.assertEqual(frozen.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
