import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from screen_double_grid import aligned_segments

class ExplicitExpansionTest(unittest.TestCase):
    def test_one_source_token_requires_exactly_two_grid_tokens(self):
        support={'W070':{'M155':['P114']}}
        self.assertIsNotNone(aligned_segments(['W617','W070'],['M155','M245','M245'],support))
        self.assertIsNone(aligned_segments(['W617','W070'],['M155','M245'],support))
        self.assertIsNone(aligned_segments(['W617','W070'],['M155','M245','M245','M245'],support))
        self.assertIsNone(aligned_segments(['W617','W999'],['M155','M245','M245'],support))
    def test_repeated_compounds_keep_each_boundary(self):
        segments=aligned_segments(['W617','W617'],['M245']*4,{})
        self.assertEqual([s['M_positions'] for s in segments],[[0,1],[2,3]])
        self.assertIsNone(aligned_segments(['W617','W617'],['M245']*3,{}))

if __name__=='__main__':unittest.main()
