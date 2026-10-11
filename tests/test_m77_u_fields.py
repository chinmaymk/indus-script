import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_m77_u_fields import simple_field, group_contexts


class UFieldsTest(unittest.TestCase):
    def pair(self, ref, field, main=None):
        return {'reference':ref,'main':main or ['M048','M342','M176'],
                'field':field,'main_side':'1','main_line':'0','field_side':'2','field_line':'0'}

    def test_graphic_height_damage_and_doubt_are_not_silently_collapsed(self):
        self.assertEqual(simple_field(['M087','M328']),2)
        for seq in [['M099','M328'],['*M087','M328'],['M087','M328','LOSS'],
                    ['M059','M087','M328'],['M095','M059','M328'],['M328','M087']]:
            self.assertIsNone(simple_field(seq))

    def test_same_main_can_have_multiple_fields_without_duplicate_inflation(self):
        a=self.pair('a',['M087','M328']); b=self.pair('b',['M089','M328'])
        group=group_contexts([a,a,b])[0]
        self.assertEqual(group['observed_stroke_counts'],[2,3])
        self.assertEqual(group['reference_count'],2)
        self.assertEqual(len(group['witnesses']),2)

    def test_uncertain_contexts_cannot_create_contrast(self):
        a=self.pair('a',['M087','M328'])
        for marker in ['LOSS','UNKNOWN','*M048','M999']:
            b=self.pair('b',['M089','M328'],[marker,'M342','M176'])
            groups=group_contexts([a,b])
            self.assertEqual(len(groups),1)
            self.assertEqual(groups[0]['observed_stroke_counts'],[2])

    def test_conflicting_same_line_transcriptions_rejected(self):
        with self.assertRaises(ValueError):
            group_contexts([self.pair('a',['M087','M328']), self.pair('a',['M089','M328'])])


if __name__ == '__main__':
    unittest.main()
