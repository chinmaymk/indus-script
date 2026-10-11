import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from screen_pincer_contexts import compatible_positions, feature_map


class PincerContextTest(unittest.TestCase):
    def test_reversal_context_gate_and_exact_token_count(self):
        support = {'W060': {'M123': ['P001']}, 'W526': {'M254': ['P002']}}
        w = ['W526', 'W555', 'W060', 'W550']
        self.assertIsNotNone(compatible_positions(w, ['M216', 'M123', 'M222', 'M254'], support))
        self.assertIsNone(compatible_positions(w, ['M254', 'M222', 'M123', 'M216'], support))
        self.assertIsNone(compatible_positions(w, ['M216', 'M124', 'M222', 'M254'], support))
        self.assertIsNone(compatible_positions(w, ['M216', 'M123', 'M222'], support))
        self.assertIsNone(compatible_positions(w, ['M216', 'M123', 'M222', 'M254'], {}))

    def test_feature_union_preserves_ambiguity_and_provenance(self):
        features = [{'id': 'P1', 'wells_graphemes': ['W010'], 'mahadevan_graphemes': ['M001', 'M002']},
                    {'id': 'P2', 'wells_graphemes': ['W010'], 'mahadevan_graphemes': ['M002']}]
        support = feature_map(features)
        positions = compatible_positions(['W010', 'W555'], ['M222', 'M002'], support)
        self.assertEqual(positions[1]['feature_ids'], ['P1', 'P2'])
        self.assertEqual(positions[1]['all_feature_M_candidates'], ['M001', 'M002'])


if __name__ == '__main__':
    unittest.main()
