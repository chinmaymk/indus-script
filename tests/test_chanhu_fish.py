import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_chanhu_fish import square,fish_status,summarize,exact_tail


class ChanhuTests(unittest.TestCase):
    def test_square_boundaries_and_damage(self):
        self.assertEqual(square('loc. 215sq. 9/D'),'9/D')
        self.assertEqual(square('loc.159sq;6/F'),'6/F')
        self.assertIsNone(square('loc.9-'))
        base={'complete':'Y','preservation':'complete','symbol':'None'}
        self.assertEqual(fish_status([dict(base,text='+000-220+')],{'W220'}),'positive')
        self.assertEqual(fish_status([dict(base,text='+000-031+')],{'W220'}),'unknown')
        self.assertEqual(fish_status([dict(base,text='+*220+')],{'W220'}),'unknown')
        self.assertEqual(fish_status([dict(base,text='+220?+')],{'W220'}),'unknown')
        self.assertEqual(fish_status([dict(base,text='+031-705+')],{'W220'}),'negative')

    def test_missingness_bounds_and_exact_tail(self):
        s=summarize([{'fish':x,'cisi':[]} for x in ['positive','negative','unknown']],'fish')
        self.assertEqual(s['presence_fraction_bounds'],[1/3,2/3])
        self.assertAlmostEqual(exact_tail(2,0,0,2),1/6)
        self.assertEqual(exact_tail(0,2,2,0),1)
        self.assertIsNone(exact_tail(0,0,2,2))
        with self.assertRaises(ValueError):exact_tail(-1,1,1,1)


if __name__=='__main__':unittest.main()
