"""Keep matching, singleton treatment and deduplication scientifically explicit."""
from collections import Counter
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_joint_context import position,select_records,summarize_cells

class JointContextTests(unittest.TestCase):
    def test_singles_do_not_become_final_tokens(self):
        self.assertEqual(position(0,1),'single')
        self.assertEqual([position(i,3) for i in range(3)],['reading_final','medial','reading_initial'])

    def test_deduplication_preserves_context_and_artifacts_as_specified(self):
        base={'site':'S','type':'T','artifact':'A','sequence':['x','y']}
        rows=[base,dict(base),dict(base,artifact='B'),dict(base,site='Q'),dict(base,site='--')]
        self.assertEqual(len(select_records(rows,'all_rows')),4)
        self.assertEqual(len(select_records(rows,'artifact_sequence_context')),3)
        self.assertEqual(len(select_records(rows,'sequence_context')),2)

    def test_unmatched_contexts_do_not_affect_matched_rates(self):
        cells={'shared':[Counter(event=3,other=1),Counter(event=1,other=3)],
               'unmatched':[Counter(event=1000),Counter()]}
        r=summarize_cells(cells,'event')
        self.assertEqual(r['matched_strata'],1)
        self.assertEqual(r['weighted_first_minus_second'],.5)
        self.assertEqual(r['matched_first_tokens'],4)

    def test_sparse_support_is_absent_not_zero_effect(self):
        r=summarize_cells({'small':[Counter(event=1),Counter(other=3)]},'event',5)
        self.assertEqual(r['matched_strata'],0)
        self.assertIsNone(r['weighted_first_minus_second'])

if __name__=='__main__':
    unittest.main()
