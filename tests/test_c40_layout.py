"""Exclude whole discovery objects and damaged strings from projection matches."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_c40_layout import compare_deletions


class LayoutTests(unittest.TestCase):
    def test_object_exclusion_and_doubt_change_available_evidence(self):
        def row(ref, signs, doubtful=False):
            return {'source_reference':ref, 'tokens':[{'sign':s,'doubtful':doubtful,'unknown_span':False} for s in signs],
                    'source_doc_count':2,'source_direction_code':'1','source_object_code':'6'}
        rs=[row('target',['A','D']), row('clear',['A','D']),
            row('doubtful',['A','D'],True),row('near',['A','E'])]
        r=compare_deletions(['A','B','C','D'],rs,'target')
        selected=r['deletions'][1]
        self.assertEqual([x['reference'] for x in selected['exact_matches']],['clear'])
        self.assertEqual([x['reference'] for x in selected['one_token_difference_matches']],['near'])
        self.assertEqual(r['comparison_records'],2)
        self.assertEqual(len(r['deletions']),3)


if __name__ == '__main__':
    unittest.main()
