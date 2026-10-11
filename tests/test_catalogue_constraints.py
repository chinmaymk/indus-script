import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_catalogue_constraints import MODELS, violations


class CatalogueConstraintsTest(unittest.TestCase):
    def test_cardinality_and_injection_are_different_requirements(self):
        anchors = [{'id': 'a', 'W': 'W1', 'M': ['M254']},
                   {'id': 'b', 'W': 'W2', 'M': ['M254']},
                   {'id': 'c', 'W': 'W3', 'M': ['M245', 'M245']}]
        self.assertEqual({v['kind'] for v in violations(anchors, MODELS['bijective_single'])},
                         {'span_cardinality', 'different_W_same_M_span'})
        self.assertEqual([v['kind'] for v in violations(anchors, MODELS['deterministic_single'])],
                         ['span_cardinality'])
        self.assertEqual(violations(anchors, MODELS['deterministic_span']), [])

    def test_duplicate_assertions_do_not_conflict_but_different_order_does(self):
        a = {'id': 'a', 'W': 'W1', 'M': ['M001', 'M002']}
        b = {'id': 'b', 'W': 'W1', 'M': ['M001', 'M002']}
        c = {'id': 'c', 'W': 'W1', 'M': ['M002', 'M001']}
        self.assertEqual(violations([a, b], MODELS['deterministic_span']), [])
        self.assertEqual(len(violations([a, b, c], MODELS['deterministic_span'])), 2)
        self.assertEqual(violations([a, b, c], MODELS['span_relation']), [])


if __name__ == '__main__':
    unittest.main()
