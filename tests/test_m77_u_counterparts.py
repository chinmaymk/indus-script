import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_m77_u_counterparts import collect, paired_states, relation_groups, eligible, apply_context_corrections


class UCounterpartTests(unittest.TestCase):
    def field(self,ref='4508',count='M095',side='2'):
        return {'id':f'M77:{ref}:side{side}:line0','reference':ref,'side':side,'line':'0',
                'tokens':[count,'M328'],'primary_object_type_code':'3'}

    def review(self,ref='4508',tokens=None,side='1'):
        return {'reference':ref,'all_counterpart_lines_accounted_for':True,
                'counterpart_lines':[{'side':side,'line':'0','tokens':tokens or ['M048','M342','M176'],
                                      'full_sequence_primary_checked':True}]}

    def test_fields_and_duplicate_lines_cannot_be_reused_as_context(self):
        r=self.review(side='2')
        with self.assertRaises(ValueError): collect({'test':{'rows':[r]}},[self.field()])
        r=self.review();r['counterpart_lines']*=2
        with self.assertRaises(ValueError): collect({'test':{'rows':[r]}},[self.field()])

    def test_uncertainty_or_incomplete_bundle_prevents_identity_claim(self):
        for tokens in (['UNKNOWN','M342'],['LOSS','M342'],['*M048','M342']):
            reviews=collect({'test':{'rows':[self.review(tokens=tokens)]}},[self.field()])
            self.assertFalse(eligible(reviews['4508']))
        r=self.review();r['all_counterpart_lines_accounted_for']=False
        self.assertFalse(eligible(collect({'test':{'rows':[r]}},[self.field()])['4508']))

    def test_same_context_with_different_counts_has_exact_exception_bound(self):
        fields=[self.field(),self.field('4509','M089'),self.field('4548','M087')]
        reviews=collect({'test':{'rows':[self.review(f['reference']) for f in fields]}},fields)
        groups=relation_groups(paired_states(fields,reviews))
        self.assertEqual(len(groups),1)
        self.assertEqual(groups[0]['distinct_stroke_states'],3)
        self.assertEqual(groups[0]['minimum_reference_exceptions_to_single_valued_map'],2)

    def test_two_fields_on_one_reference_form_one_multifield_state(self):
        fields=[self.field('5413','M089','2'),self.field('5413','M095','3')]
        reviews=collect({'test':{'rows':[self.review('5413')]}},fields)
        pairs=paired_states(fields,reviews)
        self.assertEqual(len(pairs),1)
        self.assertEqual(pairs[0]['field_state'],(('2','0',3),('3','0',4)))
        self.assertEqual(relation_groups(pairs)[0]['distinct_stroke_states'],1)

    def test_historical_correction_requires_exact_old_reading_and_preserves_input(self):
        old={'id':'M77:3234:side1:line0','tokens':['UNKNOWN','M326','M328','M280']}
        fix={'rows':[{'id':old['id'],'old_tokens':old['tokens'].copy(),
                      'new_tokens':['UNKNOWN','M326','M328','M283']}]}
        result=apply_context_corrections([old],fix)
        self.assertEqual(old['tokens'][-1],'M280')
        self.assertEqual(result[0]['tokens'][-1],'M283')
        self.assertTrue(result[0]['has_reviewer_unknown'])
        with self.assertRaises(ValueError):apply_context_corrections(result,fix)

    def test_type_and_field_layout_are_retained_in_grouping(self):
        fields=[self.field(),self.field('4509','M089')];fields[1]['primary_object_type_code']='2'
        reviews=collect({'test':{'rows':[self.review(f['reference']) for f in fields]}},fields)
        pairs=paired_states(fields,reviews)
        self.assertEqual(len(relation_groups(pairs)),2)
        self.assertEqual(len(relation_groups(pairs,include_type=False)),1)
        fields[1]['side']='3';fields[1]['id']='M77:4509:side3:line0'
        pairs=paired_states(fields,reviews)
        self.assertEqual(len(relation_groups(pairs,include_type=False)),2)


if __name__=='__main__':unittest.main()
