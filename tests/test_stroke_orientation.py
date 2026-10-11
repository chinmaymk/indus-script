"""Guard against overclaiming from total fits and constant-count support."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_stroke_orientation import local_and_total_fit, component_predictions


class OrientationTests(unittest.TestCase):
    def test_total_agreement_does_not_imply_local_agreement(self):
        r = local_and_total_fit('8', '1')
        self.assertEqual(r['oriented_total'], r['normalized_total'])
        self.assertFalse(r['occurrence_level_equal_value_possible'])
        self.assertEqual(r['vertical_group_residual'], '-14')
        self.assertEqual(r['horizontal_group_residual'], '14')
        self.assertTrue(local_and_total_fit('1', '1')['occurrence_level_equal_value_possible'])

    def test_variable_count_breaks_fixed_component_equivalence(self):
        self.assertTrue(component_predictions([0, 4, 4], '3/7')['same_predictions'])
        self.assertFalse(component_predictions([0, 4, 3], '3/7')['same_predictions'])
        # A zero-valued component cannot discriminate even on variable support.
        self.assertTrue(component_predictions([0, 4, 3], '0')['same_predictions'])


if __name__ == '__main__':
    unittest.main()
