import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_m77_u_object_types import metadata_code, collect_reviews, join_lines, summarize


class UObjectTypeTests(unittest.TestCase):
    def row(self, **changes):
        row = {'reference':'1527','printed_metadata_code':'110012',
               'object_type_code':'1','first_line_side':'1','first_line_line':'1','verified':True}
        row.update(changes)
        return row

    def test_metadata_column_order_and_missing_object_digit(self):
        self.assertEqual(metadata_code(self.row()), '110012')
        self.assertEqual(metadata_code(self.row(printed_metadata_code='1527 110012')), '110012')
        for code in ('10012','810012'):
            with self.assertRaises(ValueError): metadata_code(self.row(printed_metadata_code=code))
        with self.assertRaises(ValueError): metadata_code(self.row(first_line_line='0'))

    def test_duplicate_and_incomplete_coverage_fail(self):
        with self.assertRaises(ValueError):
            collect_reviews({'a':{'rows':[self.row(),self.row()]}}, {'1527'})
        with self.assertRaises(ValueError):
            collect_reviews({'a':{'rows':[self.row()]}}, {'1527','2604'})

    def test_unverified_metadata_remains_unknown(self):
        reviews = collect_reviews({'a':{'rows':[self.row(verified=False)]}}, {'1527'})
        self.assertIsNone(reviews['1527']['object_type_code'])

    def test_type_join_does_not_propagate_first_line_direction(self):
        reviews = collect_reviews({'a':{'rows':[self.row()]}}, {'1527'})
        original = {'reference':'1527','side':'2','actual_direction_code':None}
        joined = join_lines([original], reviews)[0]
        self.assertIsNone(joined['actual_direction_code'])
        self.assertNotIn('primary_object_type_code',original)

    def test_occurrences_are_separate_from_references_and_lines(self):
        row = {'reference':'4653','primary_object_type_code':'2',
               'tokens':['M328','M328','M328'],'full_sequence_primary_checked':True,
               'has_primary_loss':False,'has_primary_doubt':False,'has_reviewer_unknown':False}
        result = summarize([row])['2']
        self.assertEqual((result['references'],result['lines'],result['U_occurrences']),(1,1,3))
        self.assertEqual(result['U_positions'],{'solus':0,'initial':1,'medial':1,'final':1})
        self.assertEqual(result['exact_undoubted_stroke_U_lines'],0)


if __name__ == '__main__': unittest.main()
