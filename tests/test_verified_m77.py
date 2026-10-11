import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_verified_m77 import compare_page, length_bounds, validate_review, verify_pin, candidate_comparison

def row(reference='1001', line='0', index=1):
    return {'printed_row_index':index,'reference':reference,'side':'0','line':line,
            'object_type_code':'1','field_symbol_code':'35','direction_code':'3',
            'printed_metadata_literal':'1035'+line+'3','expanded_metadata_code':'1035'+line+'3',
            'inherited_from_row':None,'normalized_order':'right_to_left',
            'tokens':['M001','*M002'],
            'segments':[{'position_from_right':i,'kind':'identified_sign','sign':f'M{i:03d}',
                         'source_doubt':i==2,'reviewer_uncertainty':False,'candidate_signs':[]} for i in (1,2)],
            'line_bbox_render_pixels':[0,0,90,10],'record_kind':'text_line'}

def inputs(rows=None):
    rows=rows or [row()]
    page={'source_pdf_page':50,'source_printed_page':39,
          'expected_rows':[{k:r[k] for k in ('reference','side','line')} for r in rows]}
    a={'schema_version':'m77-review-submission-1','source_pdf_page':50,'source_printed_page':39,
       'reviewer':'A','page_render_dimensions':[100,100],'rows':rows}
    b=copy.deepcopy(a);b['reviewer']='B'
    return page,a,b

class VerifiedM77Tests(unittest.TestCase):
    def test_missing_second_line_rejected_even_when_reference_present(self):
        page,a,_=inputs([row(line='1'),row(line='2',index=2)])
        a['rows'].pop()
        with self.assertRaisesRegex(ValueError,'coverage mismatch'):validate_review(a,page)

    def test_duplicate_keys_rejected(self):
        page,a,_=inputs([row(),row(reference='1002',index=2)])
        a['rows'][1]['reference']='1001'
        with self.assertRaisesRegex(ValueError,'duplicate row keys'):validate_review(a,page)

    def test_original_direction_does_not_reverse_normalized_tokens(self):
        page,a,b=inputs();rows,diffs=compare_page(page,a,b)
        self.assertEqual(rows[0]['direction_code'],'3')
        self.assertEqual(rows[0]['tokens'],['M001','*M002'])
        self.assertEqual(diffs,[])

    def test_unreviewed_difference_is_not_published(self):
        page,a,b=inputs();b['rows'][0]['tokens'][0]='M003';b['rows'][0]['segments'][0]['sign']='M003'
        rows,diffs=compare_page(page,a,b)
        self.assertEqual(rows,[]);self.assertFalse(diffs[0]['adjudicated'])

    def test_explicit_adjudication_requires_reason_and_evidence(self):
        page,a,b=inputs();b['rows'][0]['tokens'][0]='M003';b['rows'][0]['segments'][0]['sign']='M003'
        decision={'resolution':'B','reason':'Primary sign-list comparison','source_pins':[{'path':'example.png','sha256':'test'}]}
        rows,diffs=compare_page(page,a,b,{('1001','0','0'):decision})
        self.assertEqual(rows[0]['tokens'][0],'M003');self.assertTrue(diffs[0]['adjudicated'])
        decision['reason']=''
        with self.assertRaisesRegex(ValueError,'reason'):compare_page(page,a,b,{('1001','0','0'):decision})

    def test_loss_unknown_and_doubt_are_distinct(self):
        page,a,b=inputs()
        for review in [a,b]:
            r=review['rows'][0];r['tokens']+=['LOSS','UNKNOWN']
            r['segments'] += [dict(position_from_right=3,kind='unknown_length_loss',sign=None,source_doubt=False,minimum_signs=1,maximum_signs=None),dict(position_from_right=4,kind='visible_unidentified_glyph',sign=None,source_doubt=False,minimum_signs=1,maximum_signs=1)]
        rows,_=compare_page(page,a,b)
        self.assertEqual(rows[0]['length_bounds'],{'minimum_signs':4,'maximum_signs':None,'unknown_length_loss_spans':1,'visible_unidentified_glyphs':1})
        a['rows'][0]['segments'][2]['minimum_signs']=0
        with self.assertRaisesRegex(ValueError,'LOSS must'):validate_review(a,page)

    def test_loss_cannot_be_forced_to_one_sign(self):
        page,a,_=inputs();r=a['rows'][0]
        r['tokens']=['LOSS'];r['segments']=[dict(position_from_right=1,kind='unknown_length_loss',sign=None,source_doubt=False,minimum_signs=1,maximum_signs=1)]
        with self.assertRaisesRegex(ValueError,'unbounded'):validate_review(a,page)

    def test_source_doubt_cannot_disappear(self):
        page,a,_=inputs();a['rows'][0]['tokens'][1]='M002'
        with self.assertRaisesRegex(ValueError,'source doubt'):validate_review(a,page)

    def test_optional_single_sign_bounds_are_equivalent_but_annotations_retained(self):
        page,a,b=inputs()
        a['rows'][0]['segments'][0].update(minimum_signs=1,maximum_signs=1)
        del a['rows'][0]['segments'][0]['reviewer_uncertainty']
        rows,diffs=compare_page(page,a,b)
        self.assertEqual(diffs,[])
        self.assertIn('reviewer_uncertainty',rows[0]['reviewer_segments']['B'][0])
        b['rows'][0]['segments'][0]['reviewer_uncertainty']=True
        rows,diffs=compare_page(page,a,b)
        self.assertFalse(rows);self.assertIn('reviewer_uncertainty',diffs[0]['fields'])

    def test_custom_unknown_adjudication_does_not_force_candidate_reading(self):
        page,a,b=inputs();b['rows'][0]['tokens'][0]='M003';b['rows'][0]['segments'][0]['sign']='M003'
        custom=copy.deepcopy(a['rows'][0]);custom['tokens'][0]='UNKNOWN'
        custom['segments'][0]=dict(position_from_right=1,kind='unidentified_visible_sign',sign=None,source_doubt=False,minimum_signs=1,maximum_signs=1,candidate_signs=['M001','M003'])
        decision={'resolution':'custom','row':custom,'reason':'Visible glyph unresolved','source_pins':[{'path':'image.png','sha256':'test'}]}
        rows,_=compare_page(page,a,b,{('1001','0','0'):decision})
        self.assertEqual(rows[0]['tokens'][0],'UNKNOWN')
        self.assertEqual(rows[0]['length_bounds']['maximum_signs'],2)

    def test_modified_pinned_file_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'a.json';p.write_text('{}')
            pin={'path':'a.json','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            verify_pin(pin,Path(temp));p.write_text('{"changed":true}')
            with self.assertRaisesRegex(ValueError,'hash mismatch'):verify_pin(pin,Path(temp))

    def test_multiline_export_never_silently_flattened(self):
        rows=[row(line='1'),row(line='2',index=2)]
        result=candidate_comparison(rows,[{'source_reference':'1001','id':'candidate','tokens':['M001','*M002']}])
        self.assertEqual(result[0]['status'],'not_comparable_multiple_lines_or_export_records')

    def test_candidate_export_dictionary_tokens_normalized_before_comparison(self):
        r=row();r['tokens']=['*M373','M244','LOSS']
        candidate={'source_reference':'1001','id':'secondary','tokens':[
            {'raw':'*373','sign':'M373','doubtful':True,'unknown_span':False,'diplomatic':'*373'},
            {'raw':'244','sign':'M244','doubtful':False,'unknown_span':False,'diplomatic':'244'},
            {'raw':'0','sign':None,'doubtful':False,'unknown_span':True,'diplomatic':'000'}]}
        result=candidate_comparison([r],[candidate])[0]
        self.assertEqual(result['status'],'exact_tokens')
        self.assertEqual(result['candidate_normalized_tokens'],[['*M373','M244','LOSS']])
        self.assertIsInstance(result['candidate_tokens'][0][0],dict)

    def test_printed_metadata_must_reconstruct_expanded_fields(self):
        page,a,_=inputs();a['rows'][0]['printed_metadata_literal']='100101'
        with self.assertRaisesRegex(ValueError,'printed metadata/inheritance'):validate_review(a,page)
        first=row(line='1');second=row(line='2',index=2)
        second.update(inherited_from_row=1,printed_metadata_literal='23')
        page,a,_=inputs([first,second]);validate_review(a,page)
        a['rows'][1]['printed_metadata_literal']='21'
        with self.assertRaisesRegex(ValueError,'printed metadata/inheritance'):validate_review(a,page)

if __name__=='__main__':unittest.main()
