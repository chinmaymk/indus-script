"""Independent feasibility examples for the conditional measurement design."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_numeral_calibration_design import ratio_interval, feasible_unit_interval, disjoint


class CalibrationDesignTests(unittest.TestCase):
    def test_one_measurement_never_fixes_unrestricted_unit(self):
        for n in (1, 36, 112, 1000):
            self.assertEqual(feasible_unit_interval([n], [37], 0), (F(37,n), F(37,n)))

    def test_proportional_predictions_cannot_be_distinguished(self):
        self.assertEqual(ratio_interval([2,3], F(1,20)), ratio_interval([14,21], F(1,20)))
        self.assertIsNotNone(feasible_unit_interval([2,3], [10,15], 0))
        self.assertIsNotNone(feasible_unit_interval([14,21], [10,15], 0))

    def test_touching_intervals_allow_both_exact_endpoints(self):
        # r=1 and r=4 at e=1/3 meet at observed ratio2.
        e=F(1,3)
        self.assertFalse(disjoint(ratio_interval([1,1],e), ratio_interval([1,4],e)))
        self.assertEqual(feasible_unit_interval([1,1],[1,2],e), (F(4,3), F(4,3)))
        self.assertEqual(feasible_unit_interval([1,4],[1,2],e), (F(2,3), F(2,3)))

    def test_hypothetical_two_measurements_distinguish_or_reject_both(self):
        # Synthetic observations only, never claimed as artifact measurements.
        e=F(1,20)
        self.assertIsNotNone(feasible_unit_interval([36,61], [360,610], e))
        self.assertIsNone(feasible_unit_interval([112,145], [360,610], e))
        self.assertIsNone(feasible_unit_interval([36,61], [100,1000], e))
        self.assertIsNone(feasible_unit_interval([112,145], [100,1000], e))

    def test_invalid_inputs_rejected(self):
        for e in (-1, 1, 2):
            with self.assertRaises(ValueError): ratio_interval([1,2],e)
        with self.assertRaises(ValueError): feasible_unit_interval([1], [1,2], 0)
        with self.assertRaises(ValueError): ratio_interval([0,2],0)


if __name__ == '__main__': unittest.main()
