"""Audit primary graphic witnesses and exact shared-value sensitivity certificates."""
import json
from PIL import Image
from common import ROOT, sha256, write_json


def main():
    paths = [
        'data/processed/h904_numeral_glyph_review.json',
        'data/processed/h1923_primary_numeral_review.json',
        'data/processed/h1923_numeral_locator_audit.json',
        'data/processed/fuls_numeral_figure_followup.json',
        'results/numeral_identity_sensitivity.json',
        'results/numeral_identity_source_integration.json',
    ]
    values = [json.loads((ROOT/p).read_text()) for p in paths]
    pins = set()
    def visit(node):
        if isinstance(node,dict):
            if 'path' in node and 'sha256' in node:
                p=ROOT/node['path']
                assert sha256(p)==node['sha256'],node['path']
                if 'bytes' in node: assert p.stat().st_size==node['bytes'],node['path']
                pins.add(node['path'])
            for p,h in node.get('input_sha256',{}).items():
                assert sha256(ROOT/p)==h,p
                pins.add(p)
            for v in node.values():visit(v)
        elif isinstance(node,list):
            for v in node:visit(v)
    for v in values:visit(v)
    crops = values[0]['crop_records']+values[2]['crops']
    for crop in crops:
        src=crop['source']['path'] if isinstance(crop['source'],dict) else crop['source']
        dst=crop['output']['path'] if isinstance(crop['output'],dict) else crop['output']
        box=crop.get('box',crop.get('box_xyxy'))
        with Image.open(ROOT/src) as image, Image.open(ROOT/dst) as actual:
            expected=image.crop(box)
            assert (expected.mode,expected.size,expected.tobytes())==(actual.mode,actual.size,actual.tobytes()),dst
    assert not values[0]['global_W899_W900_alias_established']
    assert not values[0]['same_numeric_value_established']
    assert not values[0]['identity']['figure16_id3786_identity_authenticated']
    assert values[0]['established_semantic_values']==values[0]['established_phonetic_values']==0
    assert values[0]['independent_split_value_validation']['mismatches']==0
    assert not values[0]['independent_split_value_validation']['producer_imported']
    assert not values[1]['primary_image_recovered']
    assert values[1]['primary_stroke_counts'] is None
    # Check independently specified witnesses and all coefficient identities;
    # no import of the producer's polynomial operations.
    for family in values[4]['families']:
        spec=family['parameterization']
        c={k:(spec[k]+[0])[:2] for k in ('L','S','vA','vB')}
        assert c['vB'][1]==0
        assert c['L'][0]+c['vA'][0]-2*c['S'][0]==0
        assert c['L'][1]+c['vA'][1]-2*c['S'][1]==0
        assert c['vB'][0]*c['L'][0]-7*c['S'][0]-4==0
        assert c['vB'][0]*c['L'][1]-7*c['S'][1]==0
        assert c['L'][1]>0
        for p in family['bound_polynomials_nonnegative_on_domain'].values():
            assert len(p)<=2
            assert (p[1] if len(p)>1 else 0)>=0
            assert p[0]+(p[1] if len(p)>1 else 0)*spec['t_min']>=0
        for row in family['examples']:
            L,S,a,b=[row[k] for k in ('L','S','vA','vB')]
            assert 3*L+a==2*L+2*S and b*L+1==7*S+5
            assert 0<a<min(L,S) and 0<b<min(L,S)
    write_json('results/numeral_identity_followup_audit.json',{
        'distinct_evidence_pins_verified':len(pins), 'exact_pixel_crops_verified':len(crops),
        'infinite_families_independently_checked':len(values[4]['families']),
        'source_artifacts_in_phase':values[5]['phase_artifacts'],
        'global_code_aliases_added':0,'semantic_values_assigned':0,'phonetic_values_assigned':0,
        'scope':'Integrity, pixel identity and conditional algebra; no proof of ancient meaning or context-invariant value.',
        'input_sha256':{p:sha256(ROOT/p) for p in paths+['docs/NUMERAL_IDENTITY_SENSITIVITY.md']},
    })
    print(f'Numeral identity audit: {len(pins)} pins, {len(crops)} exact crops, two infinite-family certificates.')


if __name__=='__main__':main()
