import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_numeral_equations import all_positive_solutions, positive_divisors, residuals


class NumeralEquationTests(unittest.TestCase):
    def test_complete_solution_set(self):
        self.assertEqual(all_positive_solutions(),[
            {'L':4,'S':20,'v':36}, {'L':6,'S':8,'v':10},
            {'L':10,'S':8,'v':6}, {'L':36,'S':20,'v':4}])

    def test_independent_bounded_enumeration(self):
        brute=[{'L':L,'S':S,'v':2*S-L} for L in range(1,501) for S in range(1,501)
               if 2*S-L>0 and (2*S-L)*L+1==3*S+5+4*S]
        self.assertEqual(brute,all_positive_solutions())

    def test_counterexample_to_uniqueness_without_anchor(self):
        self.assertEqual(residuals(36,20,4),(0,0))
        self.assertEqual(4*36+1,3*20+5+4*20)
        self.assertNotEqual(36,10)

    def test_integer_quotient_does_not_force_even_base(self):
        self.assertEqual(residuals(10,9,8)[0],0)
        self.assertNotEqual(residuals(10,9,8)[1],0)

    def test_divisor_identity_and_enumeration(self):
        self.assertEqual(positive_divisors(65),[1,5,13,65])
        for L in range(1,101):
            self.assertEqual(4*(L*L+4),(2*L-7)*(2*L+7)+65)


if __name__=='__main__':
    unittest.main()
