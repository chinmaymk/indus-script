import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_numeral_class_constraints import classify,solve


def edge(u,v,a,b): return {'nodes':[u,v],'counts':[a,b],'cisi':['synthetic']}


class ClassConstraintTests(unittest.TestCase):
    def test_classes_are_not_silently_merged(self):
        self.assertEqual(classify(['W013']),('stacked',3))
        self.assertEqual(classify(['W033']),('long',3))
        self.assertIsNone(classify(['W033','W900']))
        self.assertIsNone(classify(['W001','W031']))

    def test_consistent_and_inconsistent_triangle(self):
        edges=[edge('a','b',2,1),edge('b','c',3,1),edge('a','c',6,1)]
        self.assertEqual(solve(edges)['normalized_component_values'],{'a':'1','b':'2','c':'6'})
        edges[-1]=edge('a','c',5,1)
        self.assertFalse(solve(edges)['positive_solution_exists'])

    def test_disconnected_components_have_independent_scales(self):
        self.assertEqual(solve([edge('a','b',2,1),edge('c','d',7,3)])['free_positive_scales_if_consistent'],2)


if __name__=='__main__':unittest.main()
