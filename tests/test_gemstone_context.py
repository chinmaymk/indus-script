"""Guard source identity, counting units and hypothetical probability scope."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_gemstone_context import exact_catalogue_join, binomial_tail


class GemstoneContextTests(unittest.TestCase):
    def test_find_group_does_not_collapse_distinct_objects_or_import_readings(self):
        rows = [dict(id='1.1', site='Harappa', **{'excavation-idno': '8650b433'}, text='+001+', translation='bad'),
                dict(id='2.1', site='Harappa', **{'excavation-idno': '8650b458'}, text='+002+'),
                dict(id='2.2', site='Harappa', **{'excavation-idno': '8650b458'}, text='+003+'),
                dict(id='3.1', site='Mohenjo-daro', **{'excavation-idno': '8650b433'}, text='+004+'),
                dict(id='4.1', site='Harappa', **{'excavation-idno': '8650b4330'}, text='+005+')]
        catalogue = [dict(find_number='8650b', eh_item=n) for n in (433, 458)]
        result = exact_catalogue_join(rows, catalogue)
        self.assertEqual(len(result), 2)
        self.assertEqual([len(r['lines']) for r in result], [1, 2])
        self.assertNotEqual(result[0]['full_raw_text_signature'], result[1]['full_raw_text_signature'])
        self.assertTrue(all(r['fish_presence_independently_verified'] is None for r in result))
        self.assertNotIn('translation', result[0]['lines'][0])

    def test_binomial_sensitivity_against_polynomial(self):
        for p in (0, .2, .3, .4, .5, 1):
            self.assertAlmostEqual(binomial_tail(6, 4, p), 15*p**4-24*p**5+10*p**6)
        self.assertAlmostEqual(binomial_tail(6, 4, .5), 22/64)
        with self.assertRaises(ValueError):
            binomial_tail(6, 7, .3)


if __name__ == '__main__':
    unittest.main()
