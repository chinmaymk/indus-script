"""Verify review integrity and that incomplete object joins remain incomplete."""
import json
from PIL import Image
from common import ROOT,sha256,write_json

def read(path):return json.loads((ROOT/path).read_text())

def main():
    names=['jar44_contained_goblets_review','jar54_contained_seal_review','jar156_165_contained_marks_review',
           'vats_pottery_inscription_review','repeated_goblet_stamp_review']
    paths=[f'data/processed/{n}.json' for n in names];reviews=[read(p) for p in paths]
    pins=set()
    def check(value):
        if isinstance(value,dict):
            if 'path' in value and 'sha256' in value:
                p=ROOT/value['path'];assert sha256(p)==value['sha256'],value['path']
                if 'bytes' in value:assert p.stat().st_size==value['bytes'],value['path']
                pins.add(value['path'])
            for child in value.values():check(child)
        elif isinstance(value,list):
            for child in value:check(child)
    for r in reviews:check(r)
    manifests=['data/processed/jar54_crop_manifest.json','data/processed/vats_pottery_text_crop_manifest.json']
    crops=reviews[0]['crop_manifest']+reviews[2]['crop_manifest']+[reviews[4]['crop']]
    for m in manifests:crops+=read(m)
    for crop in crops:
        source=crop.get('source',crop.get('parent'));output=crop['output']
        source=source['path'] if isinstance(source,dict) else source
        output=output['path'] if isinstance(output,dict) else output
        box=crop.get('box_xyxy',crop.get('crop_box_xyxy',crop.get('pixel_box')))
        with Image.open(ROOT/source) as im,Image.open(ROOT/output) as out:
            expected=im.crop(box)
            assert (expected.size,expected.mode,expected.tobytes())==(out.size,out.mode,out.tobytes()),output
    coverage=read('results/contained_mark_join_coverage.json')
    prior=read('results/inscribed_jar_frame.json')
    required=sorted(prior['summary']['rows_with_contained_marked_object_reports']+prior['summary']['rows_with_seal_fragment_but_no_explicit_preserved_text'])
    assert coverage['row_serials']==required==[44,54,116,156,165]
    established=[r for r in coverage['rows'] if r['primary_text_reference'] is not None]
    assert len(established)==1 and established[0]['serial']==116
    assert coverage['newly_established_contained_text_bridges']==coverage['newly_established_own_jar_texts']==0
    assert not reviews[0]['co_reference']['exact_contained_item_identified']
    assert reviews[1]['contained_seal']['M77'] is None and reviews[1]['contained_seal']['field_number'] is None
    repeat=reviews[4]['source_statement']
    assert repeat['goblets_reported']==2 and repeat['each_stamped_with_same_seal']
    assert all(x is None for x in reviews[4]['individual_goblet_field_numbers'])
    assert reviews[4]['established_semantic_values']==reviews[4]['established_phonetic_values']==0
    assert reviews[3]['new_semantic_values']==0
    for p,h in coverage['input_sha256'].items():assert sha256(ROOT/p)==h,p
    inputs=paths+manifests+['results/contained_mark_join_coverage.json','docs/CONTAINED_MARKS_RESULTS.md','scripts/audit_contained_mark_reviews.py']
    write_json('results/contained_mark_review_audit.json',dict(evidence_pins_verified=len(pins),exact_crops_verified=len(crops),
        fixed_contained_mark_rows_verified=5,new_text_bridges=0,
        shared_stamp_inference_scope='Conditional source-reported noninjectivity on individual vessels, not a decoded name or unique numerical meaning.',
        semantic_values_assigned=0,phonetic_values_assigned=0,
        input_sha256={p:sha256(ROOT/p) for p in inputs}))
    print(f'Contained-mark review: {len(pins)} distinct evidence pins, {len(crops)} exact crops, all five fixed rows accounted for.')

if __name__=='__main__':main()
