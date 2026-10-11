import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_pincer_preservation import row_fits

class WholePairCompatibilityTest(unittest.TestCase):
    def test_positions_cannot_be_combined_across_witnesses(self):
        model={'W550':'M216','W555':'M222'}
        a={'target_assignments':[{'w':'W550','m':'M216'},{'w':'W555','m':'M216'}]}
        b={'target_assignments':[{'w':'W550','m':'M222'},{'w':'W555','m':'M222'}]}
        self.assertFalse(row_fits([a,b],model))
        actual={'target_assignments':[{'w':'W550','m':'M216'},{'w':'W555','m':'M222'}]}
        self.assertTrue(row_fits([a,b,actual],model))

if __name__=='__main__':unittest.main()
