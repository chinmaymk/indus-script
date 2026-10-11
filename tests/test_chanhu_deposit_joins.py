"""Guard artifact identity and signed levels against plausible silent misjoins."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_chanhu_deposit_joins import excavation_key, plate_key, provenance, level


class ChanhudaroJoinTests(unittest.TestCase):
    def test_suffix_is_identity(self):
        self.assertEqual(excavation_key('CH 2529 (CC)Pl. LII:23'), ('2529', 'CC'))
        self.assertEqual(excavation_key('CH 3492Pl. LII::32'), ('3492', ''))
        self.assertNotEqual(excavation_key('3485, b'), excavation_key('CH 3485 (a)Pl. LI:30'))

    def test_no_substring_or_numeric_suffix_collapse(self):
        for value in ['CH 1954 (2)Pl. LII:35', '-Pl. LII:35', 'possibly 2285', '2285/2286']:
            self.assertIsNone(excavation_key(value))

    def test_plate_item_not_interchangeable(self):
        self.assertEqual(plate_key('CH 3492Pl. LII::32'), 'LII.32')
        self.assertNotEqual(plate_key('CH 3817Pl. LI:25'), plate_key('CH 3817Pl. LI:26'))

    def test_signed_level_and_missing(self):
        self.assertEqual(level('-2.8 ft'), -2.8)
        self.assertEqual(level('+10.4 ft'), 10.4)
        self.assertIsNone(level('-'))
        self.assertIsNone(level('about 10 ft'))

    def test_location_without_spaces(self):
        self.assertEqual(provenance('loc. 297sq. 8/C'), {'square': '8/C', 'locus': '297'})
        self.assertEqual(provenance('loc. 65-'), {'square': None, 'locus': '65'})


if __name__ == '__main__':
    unittest.main()
