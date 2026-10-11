"""Check documentary pins, exact crops, and the restricted height comparison."""
import json
from decimal import Decimal
from PIL import Image
from common import ROOT,sha256,write_json

def main():
    reviews=['data/processed/capacity_h370_identities.json',
             'data/processed/capacity_md1374_cisi2_review.json',
             'data/processed/capacity_table_primary_review.json',
             'data/processed/capacity_context_independent_review.json',
             'data/processed/capacity_context_crop_manifest.json',
             'data/processed/capacity_h370_crop_manifest.json']
    pins=set(); crops=0
    def check(value):
        if isinstance(value,dict):
            if 'path' in value and 'sha256' in value:
                p=ROOT/value['path']; assert sha256(p)==value['sha256'],value['path']
                if 'bytes' in value: assert p.stat().st_size==value['bytes'],value['path']
                pins.add(value['path'])
            for child in value.values():check(child)
        elif isinstance(value,list):
            for child in value:check(child)
    for name in reviews:check(json.loads((ROOT/name).read_text()))
    manifest=json.loads((ROOT/'data/processed/capacity_context_crop_manifest.json').read_text())
    for row in manifest:
        assert sha256(ROOT/row['source'])==row['source_sha256']
        assert sha256(ROOT/row['output'])==row['output_sha256']
    manifest+=json.loads((ROOT/'data/processed/capacity_h370_crop_manifest.json').read_text())
    for review in ('capacity_md1374_cisi2_review','capacity_context_independent_review'):
        manifest+=json.loads((ROOT/f'data/processed/{review}.json').read_text())['crop_manifest']
    for row in manifest:
        src=row['source']['path'] if isinstance(row['source'],dict) else row['source']
        out=row['output']['path'] if isinstance(row['output'],dict) else row['output']
        box=row.get('box_xyxy',row.get('pixel_box'))
        with Image.open(ROOT/src) as source,Image.open(ROOT/out) as output:
            expected=source.crop(box)
            assert output.size==expected.size and output.mode==expected.mode and output.tobytes()==expected.tobytes()
        crops+=1
    measured=json.loads((ROOT/'results/capacity_context_measurements.json').read_text())
    for path,digest in measured['input_sha256'].items():assert sha256(ROOT/path)==digest,path
    for r in measured['reviewed_rows']:
        independent_cm=(Decimal(r['primary_height_feet'])*12+r['primary_height_inches'])*Decimal('2.54')
        assert independent_cm==Decimal(str(r['primary_height_cm']))
        assert abs(independent_cm-Decimal(str(r['fuls_public_text_external_height_cm'])))==Decimal('0.04')
        assert r['numeral_value'] is None and r['directly_measured_capacity_litres'] is None
    assert measured['new_complete_external_test_pairs']==0 and not measured['calibration_refit_performed']
    write_json('results/capacity_context_audit.json',dict(evidence_file_pins_verified=len(pins),exact_pixel_crops_verified=crops,
        height_comparisons_verified=2,new_complete_external_test_pairs=0,
        scope='Integrity and arithmetic checks do not independently certify visual readings or semantic hypotheses.',
        input_sha256={p:sha256(ROOT/p) for p in reviews+['results/capacity_context_measurements.json','docs/CAPACITY_CONTEXT_RESULTS.md','scripts/audit_capacity_context.py']}))
    print(f'Capacity context: {len(pins)} distinct evidence pins, {crops} exact crops, two height conversions; no new semantic calibration.')

if __name__=='__main__':main()
