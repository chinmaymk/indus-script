import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from profile_public_context_tables import join_mackay, normalized, numeric


def table(field='DK 001a'):
    return dict(field_no=field, block='1', house='', room='2', street='', level_ft='-2.3')


def lipi(field='dk 001a', cisi='M-1', id='1.1'):
    return dict(id=id, cisi=cisi, site='Mohenjo-daro', **{'excavation-idno': field})


class PublicContextTests(unittest.TestCase):
    def test_normalization_does_not_infer_identifiers(self):
        self.assertEqual(normalized(' dK\t001a '), 'DK001A')
        self.assertNotEqual(normalized('DK.H. 1'), normalized('DK-H 1'))
        self.assertNotEqual(normalized('DK 1a'), normalized('DK 1'))
        self.assertNotEqual(normalized('DK 01'), normalized('DK 1'))
        self.assertNotEqual(normalized('SD 1'), normalized('DK 1'))

    def test_repeated_rows_same_artifact_allowed(self):
        result = join_mackay([table()], [lipi(), lipi(id='1.2')])
        self.assertEqual(result['eligible_join_count'], 1)
        self.assertEqual(result['eligible_locus_and_raw_numeric_depth_count'], 1)
        self.assertEqual(len(result['eligible_joins'][0]['lipi_rows']), 2)

    def test_duplicate_table_key_rejected_even_identical(self):
        result = join_mackay([table(), table()], [lipi()])
        self.assertEqual(result['eligible_join_count'], 0)
        self.assertIn('nonunique_mackay_field_key', result['rejected_table_keys'][0]['reasons'])

    def test_multiple_artifacts_rejected(self):
        result = join_mackay([table()], [lipi(), lipi(cisi='M-2')])
        self.assertEqual(result['eligible_join_count'], 0)
        self.assertEqual(len(result['lipi_field_keys_multiple_artifacts']), 1)

    def test_conflicting_artifact_fields_rejected(self):
        result = join_mackay([table()], [lipi(), lipi(field='DK 2')])
        self.assertEqual(result['eligible_join_count'], 0)
        self.assertIn('M-1', result['lipi_artifact_keys_multiple_fields'])

    def test_unmatched_and_missing_preserved(self):
        result = join_mackay([table(), table(field='')], [lipi(field='SD 001a'), lipi(field='?')])
        self.assertEqual(result['eligible_join_count'], 0)
        self.assertEqual(len(result['mackay_missing_field_rows']), 1)
        self.assertEqual(len(result['lipi_missing_field_rows']), 1)
        self.assertIn('SD001A', result['lipi_field_keys_absent_from_mackay'])

    def test_numeric_requires_finite_number(self):
        for value in ('NaN', 'inf', 'surface', 'B.P.', ''):
            self.assertFalse(numeric(value))
        self.assertTrue(numeric('-2.3'))


if __name__ == '__main__':
    unittest.main()
