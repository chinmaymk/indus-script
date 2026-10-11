import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_hind_leg_hypothesis import occurrences,scan,CANDIDATES

class HindLegAuditTests(unittest.TestCase):
    def test_exact_code_not_substring_or_nearby_code(self):
        hits=occurrences('+1278-280-278-2790+',CANDIDATES)
        self.assertEqual([h['code'] for h in hits],['W278'])
        self.assertEqual(hits[0]['file_right'],'')

    def test_does_not_bridge_damage_or_newline(self):
        hits=occurrences('+220]278/220-279+',CANDIDATES)
        self.assertEqual(hits[0]['file_left'],'')
        self.assertEqual(hits[0]['file_right'],'')
        self.assertEqual(hits[1]['file_left'],'W220')

    def test_reading_order_is_explicit_and_direction_required(self):
        base=dict(id='1',cisi='M-1690',text='+220-278+')
        rows=scan([dict(base,**{'dir.':'R/L'}),dict(base,**{'dir.':'L/R'})],{'1'},CANDIDATES)
        self.assertTrue(rows[0]['plain_fish_after_in_reported_RL'])
        self.assertFalse(rows[1]['plain_fish_after_in_reported_RL'])
        self.assertEqual(rows[0]['paper_exposure'],'discovery_context')

    def test_non_discovery_source_exposure_not_claimed_blind(self):
        rows=scan([dict(id='1',cisi='M-71',text='+279+',**{'dir.':'R/L'}),
                   dict(id='2',cisi='M-290',text='+279+',**{'dir.':'R/L'})],set(),CANDIDATES)
        self.assertEqual([r['paper_exposure'] for r in rows],['shape_illustration','author_proposed_followup'])

if __name__=='__main__':
    unittest.main()
