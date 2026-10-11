"""Verify source pins, crop pixels, independent screen agreement and typed joins."""
import json
from PIL import Image
from common import ROOT,sha256,write_json

def read(path):return json.loads((ROOT/path).read_text())

def main():
    paths=[f'data/processed/{name}.json' for name in ('jar3822_text_review','inscribed_jar_contents_review','inscribed_jar_text_bridges','inscribed_jar_frame_independent')]
    pins=set()
    def walk(value):
        if isinstance(value,dict):
            if 'path' in value and 'sha256' in value:
                p=ROOT/value['path'];assert sha256(p)==value['sha256'],value['path']
                if 'bytes' in value:assert p.stat().st_size==value['bytes'],value['path']
                pins.add(value['path'])
            for child in value.values():walk(child)
        elif isinstance(value,list):
            for child in value:walk(child)
    reviews=[read(p) for p in paths]
    for review in reviews:walk(review)
    manifests=['data/processed/jar3822_crop_manifest.json','data/processed/inscribed_jar_bridge_crop_manifest.json','data/processed/inscribed_jar_frame_independent_crop_manifest.json']
    crop_rows=reviews[1]['crop_manifest'][:]
    for p in manifests:crop_rows+=read(p)
    for row in crop_rows:
        source=row['source']['path'] if isinstance(row['source'],dict) else row['source']
        output=row['output']['path'] if isinstance(row['output'],dict) else row['output']
        box=row.get('box_xyxy',row.get('crop_box_xyxy',row.get('pixel_box')))
        assert box is not None,row
        with Image.open(ROOT/source) as im,Image.open(ROOT/output) as out:
            expected=im.crop(box)
            assert (expected.size,expected.mode,expected.tobytes())==(out.size,out.mode,out.tobytes()),output
    frame=read('results/inscribed_jar_frame.json');independent=reviews[3]
    assert frame['observed_printed_serial_count']==independent['serial_count']==176
    assert frame['design_sha256']==sha256(ROOT/'docs/INSCRIBED_JAR_FRAME_DESIGN.md')
    actual=[r['serial'] for r in frame['rows'] if r['cereal_related_mention']]
    assert actual==[r['serial'] for r in independent['plant_mention_rows']]
    assert independent['plant_mention_count']==len(actual)==60
    assert independent['plant_categories']==dict(reported_cereal_grain_wheat=58,historical_inference=1,cereal_like_impression_only=1)
    assert independent['main_container_positive_serials']==[18,116]
    assert sorted(r['row'] for r in reviews[1]['rows'])==[35,116]
    assert frame['summary']['container_inscription_reported_rows']==[18,35,116]
    expected_positive=set(frame['summary']['rows_with_contained_marked_object_reports']+frame['summary']['rows_with_seal_fragment_but_no_explicit_preserved_text']+[18,116])
    assert set(independent['all_positive_serials'])==expected_positive
    for a,b in zip(frame['pages'],independent['pages']):
        assert (a['printed_page'],a['first_serial'],a['last_serial'])==(b['printed_page'],b['serial_first'],b['serial_last'])
        assert sha256(ROOT/a['source'])==a['sha256']
    for key in ('results/inscribed_jar_frame.json','results/inscribed_jar_bounds_independent.json'):
        for path,digest in read(key)['input_sha256'].items():assert sha256(ROOT/path)==digest,path
    assert reviews[0]['photo_verified_sign_count'] is None and reviews[0]['sign_sequence'] is None
    assert reviews[1]['established_semantic_values']==reviews[1]['established_phonetic_values']==reviews[2]['new_semantic_values']==0
    assert all(r['measurements'] is None for r in reviews[1]['rows'])
    all_paths=paths+manifests+['results/inscribed_jar_frame.json','results/inscribed_jar_bounds_independent.json','docs/INSCRIBED_JAR_RESULTS.md','scripts/audit_inscribed_jar_reviews.py']
    write_json('results/inscribed_jar_review_audit.json',dict(evidence_pins_verified=len(pins),exact_crops_verified=len(crop_rows),
        independently_checked_table_pages=9,independently_checked_serials=176,
        independent_cereal_mention_set_agrees=True,main_container_and_contained_object_distinctions_agree=True,
        new_semantic_values=0,new_phonetic_values=0,
        input_sha256={p:sha256(ROOT/p) for p in all_paths}))
    print(f'Inscribed-jar review audit: {len(pins)} distinct pins, {len(crop_rows)} exact crops; independent176-row screen agrees.')

if __name__=='__main__':main()
