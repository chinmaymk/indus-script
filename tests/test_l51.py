import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_l51 import conditioned,is_ending,summarize


class L51Test(unittest.TestCase):
    def test_terminal_specific_comparison(self):
        def row(i,s):return dict(cisi=str(i),site='A',type='SEAL:S',sequence=s)
        rows=[row(0,['W527','W555','F']),row(1,['W527','X','F']),
              row(2,['W527','X','N']),row(3,['Y','X','N'])]
        self.assertEqual(conditioned(rows,{'F'})['exact_fraction'],'1/2')
        self.assertEqual(conditioned(rows[:3],{'F'})['exact_fraction'],'2/3')
        self.assertFalse(is_ending(['X','W527','W555']))
        x=summarize([dict(id='a.1',hit=True),dict(id='b.1',hit=None)],'hit')
        self.assertEqual(x['possible_positive_fraction_bounds'],[.5,1])


if __name__=='__main__':unittest.main()
