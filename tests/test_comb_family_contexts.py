import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_comb_family_contexts import exact_counterparts, positions


class CombFamilyContextsTest(unittest.TestCase):
    def test_exact_one_position_preserves_other_tokens_and_duplicate_rows(self):
        index = {('W525', 'W525', 'W100'): [{'id': 'a'}, {'id': 'b'}],
                 ('W526', 'W525', 'W100'): [{'id': 'c'}],
                 ('W527', 'W527', 'W100'): [{'id': 'd'}],
                 ('W527', 'W525', 'W101'): [{'id': 'e'}]}
        pairs = exact_counterparts(index)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(len(pairs[0]['W525_rows']), 2)
        self.assertEqual(pairs[0]['reading_position_zero_based'], 2)

    def test_reading_positions_and_singleton_are_explicit(self):
        self.assertEqual(positions(['W525', 'W100', 'W525'], 'W525'), [
            {'reading_index_zero_based': 0, 'offset_from_reading_end': 2, 'relative_position': '0', 'category': 'initial'},
            {'reading_index_zero_based': 2, 'offset_from_reading_end': 0, 'relative_position': '1', 'category': 'final'}])
        self.assertEqual(positions(['W525'], 'W525')[0]['category'], 'singleton')


if __name__ == '__main__':
    unittest.main()
