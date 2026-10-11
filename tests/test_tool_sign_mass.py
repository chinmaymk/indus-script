"""Check strict reconstruction boundary and avoid treating missing mass as observed."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_tool_sign_mass import certificate


class ToolSignMassTests(unittest.TestCase):
    def test_equality_fits_current_mass_but_not_strict_upper_cap(self):
        r = certificate('5', '5', '1')
        self.assertFalse(r['exact_surviving_mass_model_inconsistent'])
        self.assertTrue(r['strict_cap_model_inconsistent'])

    def test_larger_original_cap_can_remove_only_reconstruction_conflict(self):
        r = certificate('476', '165.343', '3')
        self.assertTrue(r['exact_surviving_mass_model_inconsistent'])
        self.assertFalse(r['strict_cap_model_inconsistent'])
        self.assertEqual(r['minimum_original_over_surviving_factor']['fraction'], '476000/165343')


if __name__ == '__main__':
    unittest.main()
