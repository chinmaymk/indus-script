import csv
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from common import ROOT
from screen_numeral_pairs import adjacent_runs, literal_tokens, inspect_group, FIELDS, constant_long_stroke_ratio_audit


CANDIDATES = [dict(L=10, S=8, v=6), dict(L=36, S=20, v=4)]


def artifact(cisi):
    with (ROOT/'data/raw/lipi_inscriptions.csv').open() as f:
        return [{k:r[k] for k in FIELDS} for r in csv.DictReader(f) if r['cisi']==cisi]


class NumeralScreenTests(unittest.TestCase):
    def test_no_skipping_or_partial_number_matching(self):
        self.assertEqual(literal_tokens('+1700-700-8400+'), ['W700'])
        runs = adjacent_runs(['W032', 'W257', 'W840'], 'W840')
        self.assertEqual(runs['left'], [])
        self.assertEqual(runs['residual_before'], ['W032', 'W257'])

    def test_direction_sensitivity_retains_positive_base_contradiction(self):
        rows = artifact('H-306')
        self.assertFalse(inspect_group('1328', rows, CANDIDATES)['eligible'])
        record = inspect_group('1328', rows, CANDIDATES, True)
        self.assertTrue(record['eligible'])
        self.assertEqual(record['equation_difference'], dict(L=1, S=0, v=0, constant=0))
        self.assertTrue(all(not e['balances'] for e in record['evaluations']))

    def test_matched_pattern_does_not_identify_unique_values(self):
        record = inspect_group('1786', artifact('H-904'), CANDIDATES)
        self.assertTrue(record['eligible'])
        self.assertEqual(record['equation_difference'], dict(L=1, S=-2, v=1, constant=0))
        self.assertTrue(all(e['balances'] for e in record['evaluations']))
        self.assertEqual(record['faces']['W700']['residual_after'], ['W645', 'W368', 'W817'])

    def test_sensitivity_never_accepts_damage_or_ambiguous_markers(self):
        damaged = inspect_group('1361', artifact('H-340'), CANDIDATES, True)
        self.assertFalse(damaged['eligible'])
        self.assertIn('W840:not_marked_complete', damaged['exclusion_reasons'])
        ambiguous = inspect_group('829', artifact('H-2211'), CANDIDATES, True)
        self.assertFalse(ambiguous['eligible'])
        self.assertIn('marker_occurrence_not_unique', ambiguous['exclusion_reasons'])

    def test_constant_unit_conversion_cannot_rescue_conflicting_ratios(self):
        same = inspect_group('567', artifact('H-1923'), CANDIDATES, True)
        different = inspect_group('1328', artifact('H-306'), CANDIDATES, True)
        compatible = constant_long_stroke_ratio_audit([same, same])
        self.assertFalse(compatible['incompatible_with_any_positive_constant_pair'])
        conflict = constant_long_stroke_ratio_audit([same, different])
        self.assertEqual(conflict['distinct_required_b_over_a'], ['1', '3/2'])
        self.assertTrue(conflict['incompatible_with_any_positive_constant_pair'])


if __name__ == '__main__':
    unittest.main()
