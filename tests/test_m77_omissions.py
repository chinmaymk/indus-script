"""Exhaustively verify the sharp category bounds on small finite populations."""
import itertools
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_m77_omissions import omission_bounds


class OmissionBoundsTests(unittest.TestCase):
    def test_bounds_equal_exhaustive_feasible_extrema(self):
        for primary in itertools.product(range(4),repeat=4):
            for represented in range(sum(primary)+1):
                feasible=[r for r in itertools.product(*(range(p+1) for p in primary)) if sum(r)==represented]
                calculated=omission_bounds(primary,represented)
                for i,p in enumerate(primary):
                    missed=[p-r[i] for r in feasible]
                    self.assertEqual(calculated[i],{'minimum':min(missed),'maximum':max(missed)})

    def test_impossible_subset_is_rejected_not_clipped(self):
        for primary,n in [([1,2],4),([1,-1],0),([1,2],-1),([1.5],1)]:
            with self.assertRaises(ValueError):omission_bounds(primary,n)


if __name__=='__main__':
    unittest.main()
