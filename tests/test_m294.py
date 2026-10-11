import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_m294 import classify


class M294DirectionTest(unittest.TestCase):
    def test_extensions_preserve_reported_direction_and_token_boundaries(self):
        target = ['W740', 'W220', 'W003']
        h = classify(target + ['W999'], target, 'R/L')[0]
        self.assertTrue(h['reading_prefix_extension_if_reported_RL'])
        self.assertFalse(h['reading_suffix_extension_if_reported_RL'])
        self.assertFalse(h['exact'])
        terminal_side = classify(['W999'] + target, target, 'R/L')[0]
        self.assertTrue(terminal_side['reading_suffix_extension_if_reported_RL'])
        self.assertFalse(terminal_side['reading_prefix_extension_if_reported_RL'])
        self.assertIsNone(classify(target + ['W999'], target, 'unknown')[0]
                          ['reading_prefix_extension_if_reported_RL'])
        self.assertEqual([], classify(['W740','W220','W000','W003'],target,'R/L'))
        self.assertEqual([], classify(['W520','W220','W003'],target,'R/L'))


if __name__ == '__main__':
    unittest.main()
