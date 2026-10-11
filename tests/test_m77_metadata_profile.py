import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from profile_m77_metadata import profile


def corpus():
    def row(ref, side, line, code):
        return dict(reference=ref, side=side, line=line, field_symbol_code=code,
                    object_type_code='1')
    return dict(schema_version='verified-m77-1', coverage_complete_for_manifest=True,
                unresolved_rows=0, rows=[row('1','1','1','00'), row('1','1','2','00'),
                                         row('1','2','0','01'), row('2','0','0','35')])


class MetadataProfileTests(unittest.TestCase):
    def test_multiline_and_multiside_counts_are_not_independent_objects(self):
        p = profile(corpus())
        self.assertEqual(p['counts'], dict(lines=4, represented_sides=3, references=2))
        self.assertEqual(p['line_field_code_counts'], {'00':2, '01':1, '35':1})
        self.assertEqual(p['side_field_code_counts'], {'00':1, '01':1, '35':1})
        self.assertEqual(p['reference_field_code_incidence_overlapping'], {'00':1, '01':1, '35':1})
        self.assertEqual(p['references_with_multiple_codes'], [{'reference':'1','codes':['00','01']}])

    def test_conflicts_and_duplicate_rows_are_rejected(self):
        for mode in ('field', 'type', 'duplicate'):
            c = corpus()
            if mode == 'field': c['rows'][1]['field_symbol_code'] = '01'
            elif mode == 'type': c['rows'][1]['object_type_code'] = '2'
            else: c['rows'].append(copy.deepcopy(c['rows'][0]))
            with self.assertRaises(ValueError): profile(c)

    def test_incomplete_input_and_noncanonical_codes_are_rejected(self):
        c = corpus(); c['coverage_complete_for_manifest'] = False
        with self.assertRaises(ValueError): profile(c)
        for code in ('1', 1, None, 'XX'):
            c = corpus(); c['rows'][0]['field_symbol_code'] = code
            with self.assertRaises(ValueError): profile(c)


if __name__ == '__main__':
    unittest.main()
