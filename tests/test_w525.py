import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from screen_w525 import masked_alignment

class MaskedMappingTest(unittest.TestCase):
    def test_repeated_unknown_requires_consistent_value(self):
        self.assertIsNotNone(masked_alignment(['W525','W525'],['M001','M001'],{}))
        self.assertIsNone(masked_alignment(['W525','W525'],['M001','M002'],{}))
        self.assertIsNone(masked_alignment(['W525'],['M418'],{}))
    def test_no_other_unknowns_or_deleted_material(self):
        self.assertIsNone(masked_alignment(['W525','W999'],['M001','M002'],{}))
        self.assertIsNone(masked_alignment(['W525'],['M001','M001'],{}))
        self.assertIsNotNone(masked_alignment(['W525','W617'],['M245','M245','M001'],{}))

if __name__=='__main__':unittest.main()
