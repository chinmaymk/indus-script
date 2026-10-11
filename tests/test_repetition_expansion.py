import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_repetition_expansion import maximal_runs,rewrite_matches,corpus


class ExpansionTest(unittest.TestCase):
    def test_maximal_not_overlapping_run_windows(self):
        self.assertEqual(list(maximal_runs(('a','a','a','a','b','b'))),[(0,4,'a'),(4,6,'b')])

    def test_exact_context_and_alternatives_are_retained(self):
        seqs={('p','a','a','q'):['x'],('p','two','a','q'):['y'],
              ('p','other','a','q'):['z'],('r','two','a','q'):['notmatch']}
        _,matches=rewrite_matches(seqs,{2:{'two':'test'}})
        self.assertEqual(len(matches),2)
        self.assertEqual(sum(m['graphic_count_match'] for m in matches),1)
        self.assertEqual({m['alternative_references'][0] for m in matches},{'y','z'})

    def test_no_unchanged_self_match_and_keep_order_distinct(self):
        seqs={('a','a'):['x'],('a','two'):['y'],('two','a'):['z']}
        _,matches=rewrite_matches(seqs,{2:{'two':'test'}})
        self.assertEqual(len(matches),2)
        self.assertEqual({m['replacement_order'] for m in matches},{'before','after'})

    def test_repeated_reference_does_not_multiply_string_matches(self):
        _,m=rewrite_matches({('a','a'):['x','x2'],('two','a'):['y','y2']},{2:{'two':'test'}})
        self.assertEqual(len(m),1)
        self.assertEqual(len(m[0]['expanded_references']),2)

    def test_loss_is_not_deleted_to_create_run(self):
        records=[{'source_reference':'x','strict_candidate':False,'tokens':[
            {'sign':'a','unknown_span':False,'doubtful':False},
            {'sign':None,'unknown_span':True,'doubtful':False},
            {'sign':'a','unknown_span':False,'doubtful':False}]}]
        seqs,n,excluded=corpus(records)
        self.assertEqual(seqs,{})
        self.assertEqual(n,0)
        self.assertEqual(excluded,{'any_doubt_or_loss':1})


if __name__=='__main__':unittest.main()
