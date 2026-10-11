"""Check the bound's equality boundary and distinguish loss requirements from fits."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_arch_mass_bound import bound


class ArchBoundTests(unittest.TestCase):
    def test_equal_cap_is_feasible_and_negative_residual_can_escape_bound(self):
        self.assertFalse(bound('10','45','5','1')['combined_premises_inconsistent'])
        self.assertTrue(bound('10','46','5','1')['combined_premises_inconsistent'])
        # A=11,u=5 yieldsL46,S10 only by r=-1; this is outside nonnegative residual premise.
        self.assertEqual(11+7*5,46)
        self.assertEqual(10-11,-1)

    def test_missing_chisel_mass_threshold_is_conditional(self):
        r=bound('262.233','1910.030','210','1')
        self.assertEqual(r['deficit_g']['fraction'],'177797/1000')
        corrected_k=r['minimum_chisel_mass_if_axes_held_fixed_g']['fraction']
        self.assertFalse(bound('262.233','1910.030',corrected_k,'1')['combined_premises_inconsistent'])
        self.assertEqual(bound('262.233','1910.030','210','2')['deficit_g']['fraction'],'912797/1000')


if __name__=='__main__':
    unittest.main()
