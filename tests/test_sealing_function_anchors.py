import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_sealing_function_anchors import shared_label


class DomainTests(unittest.TestCase):
    def test_unknown_is_not_a_counterexample(self):
        self.assertEqual(shared_label([None,None])['status'],'unconstrained')
        self.assertEqual(shared_label([['pottery'],None])['possible_labels'],['pottery'])

    def test_ambiguity_can_preserve_or_break_a_shared_label(self):
        self.assertEqual(shared_label([['pottery'],['wood','pottery']])['status'],'compatible')
        self.assertEqual(shared_label([['pottery'],['wood','pottery'],['leather_bag']])['status'],'incompatible')

    def test_empty_domain_is_a_data_error(self):
        with self.assertRaises(ValueError):shared_label([[]])


if __name__=='__main__':unittest.main()
