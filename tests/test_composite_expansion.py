import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_composite_expansion import screen, verify_pairwise


class CompositeExpansionTests(unittest.TestCase):
    def test_entire_context_and_order_are_preserved(self):
        data={('A','C','Z'):['1'],('A','B','D','Z'):['2'],
              ('A','D','B','Z'):['3'],('X','B','D','Z'):['4']}
        selected=[m for m in screen(data) if m['target']=='C']
        self.assertEqual({tuple(m['replacement']) for m in selected},{('B','D'),('D','B')})
        self.assertTrue(all(m['outside_context_length']==2 for m in selected))
        self.assertFalse(any('4' in m['long_references'] for m in selected))
        self.assertEqual(verify_pairwise(data,screen(data)),len(screen(data)))

    def test_empty_context_and_same_object_alone_are_excluded(self):
        self.assertEqual(screen({('C',):['1'],('B','D'):['2']}),[])
        self.assertEqual(screen({('A','C'):['1'],('A','B','D'):['1']}),[])
        matches=screen({('A','C'):['1','1'],('A','B','D'):['1','2','2']})
        self.assertEqual(len(matches),1)
        self.assertTrue(matches[0]['same_reference_also_present'])
        self.assertEqual(matches[0]['long_references'],['1','2'])


if __name__=='__main__':unittest.main()
