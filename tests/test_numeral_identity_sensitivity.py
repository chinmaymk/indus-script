import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_numeral_identity_sensitivity import FAMILIES, evaluate, add, multiply


class IdentitySensitivityTests(unittest.TestCase):
    def test_polynomial_operations_keep_quadratic_cancellation(self):
        self.assertEqual(multiply([1,2],[-3,4]),[-3,-2,8])
        self.assertEqual(add([-3,-2,8],[3,2,-8]),[0])

    def test_direct_integer_witnesses_including_large_parameter(self):
        for f in FAMILIES:
            for t in [f['t_min'],f['t_min']+1,17,1000000]:
                L,S,a,b=[evaluate(f[k],t) for k in ('L','S','vA','vB')]
                self.assertEqual(3*L+a,2*L+2*S)
                self.assertEqual(b*L+1,7*S+5)
                self.assertTrue(L>=10 and S>=8 and 0<a<min(L,S) and 0<b<min(L,S))

    def test_split_witness_fails_shared_equation(self):
        # t2 in first family: (L,S,vA,vB)=(15,8,1,4).
        self.assertEqual(3*15+1,2*15+2*8)
        self.assertEqual(4*15+1,7*8+5)
        self.assertNotEqual(1*15+1,7*8+5)
        self.assertNotEqual(3*15+4,2*15+2*8)


if __name__=='__main__': unittest.main()
