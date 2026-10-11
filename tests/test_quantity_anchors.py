import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_quantity_anchors import integer_weights, fit_unit, photo_scale


class QuantityAnchorTests(unittest.TestCase):
    def test_interval_does_not_uniquely_fix_decimal(self):
        pairs = integer_weights([1,7], 15,20)
        self.assertEqual(len(pairs),12)
        self.assertIn((10,1),pairs)
        self.assertIn((9,1),pairs)
        self.assertIn((4,2),pairs)
        self.assertNotIn((1,1),pairs)
        self.assertEqual([a for a,b in pairs if b == 1], list(range(8,14)))

    def test_exact_count_can_identify_under_explicit_restriction(self):
        self.assertEqual([(a,b) for a,b in integer_weights([1,7],17,17) if b==1],[(10,1)])

    def test_scale_symmetry_preserves_fit_even_with_noise(self):
        n, v = [3,6,7], [121,242,284]
        u = fit_unit(n,v)
        for k in [Fraction(1,2), Fraction(10), Fraction(7,3)]:
            scaled = fit_unit([k*x for x in n],v)
            self.assertEqual(scaled,u/k)
            self.assertEqual([u*x for x in n],[scaled*k*x for x in n])

    def test_unknown_image_scale_absorbs_units(self):
        for coefficient in [0.01,2,1000]:
            for volume in [4.04,40.4,404]:
                s = photo_scale(volume,coefficient)
                self.assertAlmostEqual(coefficient*s**3,volume)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            integer_weights([0,7],15,20)
        with self.assertRaises(ValueError):
            fit_unit([3],[])
        with self.assertRaises(ValueError):
            photo_scale(1,0)


if __name__ == '__main__':
    unittest.main()
