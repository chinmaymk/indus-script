import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from screen_comb_tablets import align


class CombTabletMaskTest(unittest.TestCase):
    def test_target_only_is_masked_and_repeats_agree(self):
        self.assertIsNotNone(align(['W195', 'W195'], ['M054', 'M054'], 'W195', {}))
        self.assertIsNone(align(['W195', 'W195'], ['M054', 'M055'], 'W195', {}))
        self.assertIsNone(align(['W195', 'W999'], ['M054', 'M054'], 'W195', {}))
        self.assertIsNone(align(['W195'], ['M418'], 'W195', {}))

    def test_local_w525_extension_is_explicit_and_does_not_mask_other_codes(self):
        seq = ['W400', 'W525', 'W554']
        support = {'W400': {'M176'}, 'W554': {'M226'}}
        self.assertIsNone(align(seq, ['M054', 'M254', 'M176'], 'W554', support))
        self.assertIsNotNone(align(seq, ['M054', 'M254', 'M176'], 'W554', support, True))
        self.assertIsNone(align(seq, ['M054', 'M253', 'M176'], 'W554', support, True))
        self.assertIsNone(align(seq, ['M054', 'M254', 'M175'], 'W554', support, True))


if __name__ == '__main__':
    unittest.main()
