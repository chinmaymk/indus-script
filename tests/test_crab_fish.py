import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_crab_fish import scan,suffix_cases


class CrabFishTests(unittest.TestCase):
    def test_reading_neighbor_does_not_cross_damage_or_change_direction(self):
        texts=['+231-798+','+231/798+','+231-000-798+','+231-*798+','+231-798+']
        rows=[{'id':str(i),'text':t,'dir.':'L/R' if i==4 else 'R/L','cisi':''} for i,t in enumerate(texts)]
        h=scan(rows,{'0'},{'798'})
        self.assertEqual(h[0]['following_in_reported_RL'],'W231')
        self.assertTrue(h[0]['strict'])
        self.assertTrue(all(x['following_in_reported_RL'] in (None,'') for x in h[1:]))

    def test_suffix_is_anchored_and_entire_earlier_text_is_retained(self):
        rows=[{'id':'a','sequence':['W226','W032','W231','W798','W002']},
              {'id':'b','sequence':['W032','W226','W798']},
              {'id':'c','sequence':['W226','W032']}]
        hits=suffix_cases(rows)
        self.assertEqual(len(hits),1)
        self.assertEqual(hits[0]['next_two_after_file_prefix'],['W231','W798'])
        self.assertEqual(hits[0]['sequence'][-1],'W002')


if __name__=='__main__':unittest.main()
