import sys
import unittest
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_metal_weight_anchors import eliminate, reconstructed_bounds, required_p, three_object_constraint, signed_three_object_fit, free_small_axe_residual


class MetalWeightTests(unittest.TestCase):
    def test_negative_mass_certificate_and_feasible_control(self):
        a={'coefficients':{'u':'1','i':'5','t':'4'},'rhs_g':'165.343','relation':'='}
        b={'coefficients':{'u':'7','i':'6','t':'0'},'rhs_g':'1910.030','relation':'='}
        _,c,rhs=eliminate(a,b)
        self.assertEqual((c['i'],c['t'],rhs),(29,28,F('-752.629')))
        # A known positive assignment (u,i,t)=(10,2,1) must not be rejected.
        a['rhs_g']='24'; b['rhs_g']='82'
        _,c,rhs=eliminate(a,b)
        self.assertEqual(rhs,c['i']*2+c['t'])
        self.assertGreater(rhs,0)

    def test_corrected_bound_and_boundary(self):
        bounds=reconstructed_bounds('165','1910','2.6')
        i=F(bounds['i_upper_exclusive_g']['exact'])
        u=F(bounds['u_lower_exclusive_g']['exact'])
        self.assertEqual(i,F(1093,57))
        self.assertEqual(u,F(4872,19))
        self.assertEqual(u+9*i,429)  # equality is excluded by the strict hypothesis
        self.assertEqual(7*u+6*i,1910)

    def test_precision_and_base_sensitivity(self):
        precise=reconstructed_bounds('165.343','1910.030','2.6')
        self.assertEqual(F(precise['eliminated_rhs_g']['exact']),F('1099.2126'))
        self.assertGreater(required_p(165,1910,10),F('2.6'))
        self.assertLess(required_p(165,1910,16),F('2.6'))
        self.assertFalse(reconstructed_bounds(165,1910,1)['positive_solution_possible'])

    def test_third_object_contradiction(self):
        result=three_object_constraint(165,1910,262)
        self.assertEqual(F(result['chisel_mass_lower_inclusive_g']['exact']),F(9529,21))
        self.assertFalse(result['compatible_with_strict_p_2_6'])
        self.assertGreater(F(result['p_lower_inclusive']['exact']),F('2.6'))

    def test_signed_fit_is_not_nonnegative_fit_or_validation(self):
        r=signed_three_object_fit('165.343','1910.030','262.233')
        self.assertEqual(F(r['t_g']['exact']),F(-4040177,56000))
        self.assertTrue(all(F(x['exact'])==0 for x in r['residuals_g']))
        self.assertFalse(r['all_nonnegative'])
        self.assertFalse(r['negative_i_possible_under_small_axe_equation'])
        self.assertEqual(r['independent_validation_equations'],0)
        positive=signed_three_object_fit('24','82','12')
        self.assertTrue(positive['all_nonnegative'])
        self.assertEqual([F(positive[k]['exact']) for k in ('i_g','u_g','t_g')],[2,10,1])
        relaxed=free_small_axe_residual('165.343','1910.030','262.233','-30')
        self.assertGreater(F(relaxed['t_g']['exact']),0)
        self.assertGreater(F(relaxed['fitted_small_axe_other_signs_g']['exact']),0)
        self.assertTrue(all(F(x['exact'])==0 for x in relaxed['residuals_g']))
        self.assertEqual(relaxed['free_parameters_after_three_equations'],1)


if __name__=='__main__':
    unittest.main()
