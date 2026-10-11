import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_metal_numeral_conventions import canonical,uniform_units,pair_calibration,axes_constraint,unrestricted_loss_fit


class ConventionTests(unittest.TestCase):
    def test_carry_boundary_and_unbounded_leading_unit(self):
        units=uniform_units(8)
        self.assertTrue(canonical({'i':7,'x':100},units))
        self.assertFalse(canonical({'i':8},units))
        self.assertTrue(canonical({'i':8},uniform_units(9)))

    def test_half_unit_does_not_fix_upper_ratio(self):
        units={'t':F(1),'i':F(8),'u':F(80),'x':F(800)}
        self.assertEqual(4*units['t'],units['i']/2)
        self.assertEqual(units['u']/units['i'],10)
        self.assertTrue(canonical({'u':7,'i':6},units))

    def test_pair_survives_two_distinct_radices(self):
        for r in (8,10):
            self.assertTrue(pair_calibration(r,r)['fits_hypothetical_strict_2_6_cap'])
        # Earlier t=i/base10 failure is consistent with this different assumption.
        self.assertFalse(pair_calibration(10,1)['fits_hypothetical_strict_2_6_cap'])

    def test_axes_incompatible_and_compatible_control(self):
        self.assertFalse(axes_constraint('262.233','1910.030')['compatible'])
        self.assertTrue(axes_constraint(6,62)['compatible'])
        self.assertEqual(axes_constraint(6,62)['calibrated_u_over_i']['exact'],'8')
        self.assertFalse(axes_constraint('262.233','1910.030',7)['compatible'])
        self.assertTrue(axes_constraint(6,55,7)['compatible'])
        noninteger=axes_constraint(6,F('65.5'))
        self.assertTrue(noninteger['satisfies_minimum_ratio_bound'])
        self.assertFalse(noninteger['ratio_is_integer'])
        self.assertFalse(noninteger['compatible'])

    def test_unrestricted_losses_make_distinct_bases_fit(self):
        for r in (8,10):
            fit=unrestricted_loss_fit(uniform_units(r),{'DK-7855':'262.233','DK-7835':'1910.030'})
            losses=[F(o['unmeasured_loss_g']['exact']) for o in fit['objects']]
            self.assertEqual(min(losses),0)
            self.assertGreater(max(losses),0)
            for o in fit['objects']:
                self.assertEqual(F(o['invented_original_mass_g']['exact'])-F(o['unmeasured_loss_g']['exact']),F(o['surviving_mass_g']['exact']))


if __name__=='__main__':unittest.main()
