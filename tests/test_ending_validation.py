import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_ending_validation import without_second


class EndingCounterpartTest(unittest.TestCase):
    def test_removal_is_exactly_one_specified_position(self):
        self.assertEqual(without_second(['W527','W555','W555','W235']),['W527','W555','W235'])
        self.assertIsNone(without_second(['W555','W527','W235']))
        self.assertIsNone(without_second(['W740','W555','W235']))
        self.assertEqual(without_second(['W527','W555']),['W527'])


if __name__=='__main__':unittest.main()
