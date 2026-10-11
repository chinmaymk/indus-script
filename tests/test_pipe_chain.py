import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_pipe_chain import matched_tail,certain_tokens


class PipeChainTest(unittest.TestCase):
    def test_exact_fixed_margin_tail(self):
        rows = [{'site':'A','type':'SEAL:S','cisi':str(i),'sequence':s} for i,s in enumerate([
            ['C','F'],['C','N'],['F','N'],['N','N']])]
        x=matched_tail(rows,{'F'},{'C'})
        self.assertEqual(x['exact_fraction'],'5/6')
        self.assertEqual(x['conditional_expected'],1)
        # Different-length texts cannot supply controls for this stratum.
        y=matched_tail(rows+[dict(rows[0],sequence=['C','F','N'])],{'F'},{'C'})
        self.assertEqual(y['exact_fraction'],'5/6')
        self.assertEqual(y['observed_both'],2)

    def test_uncertain_token_is_not_positive(self):
        self.assertEqual(certain_tokens('+215-*216-220?-0215-480+'),['W215','W480'])
        self.assertEqual(certain_tokens('+215-442/425-000-216+'),['W215','W216'])


if __name__=='__main__':unittest.main()
