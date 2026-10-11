"""Verify the photo layer and independently enumerate sensitivity endpoints."""
import itertools
import json
from fractions import Fraction
from PIL import Image
from common import ROOT, sha256, write_json


def main():
    paths = [
        'data/processed/chanhu_local_primary_positive_review.json',
        'data/processed/chanhu_local_primary_comparators_review.json',
        'data/processed/chanhu_local_specificity_design_review.json',
        'results/chanhu_local_specificity.json',
        'results/chanhu_local_specificity_independent.json',
        'results/chanhu_photo_sensitivity.json',
        'data/processed/chanhu_local_primary_crop_manifest.json',
        'data/processed/chanhu_local_comparators_crop_manifest.json',
    ]
    values = [json.loads((ROOT/p).read_text()) for p in paths]
    pins = set()

    def visit(node):
        if isinstance(node, dict):
            if 'path' in node and 'sha256' in node:
                p = ROOT/node['path']
                assert sha256(p) == node['sha256'], node['path']
                if 'bytes' in node:
                    assert p.stat().st_size == node['bytes'], node['path']
                pins.add(node['path'])
            for p, h in node.get('input_sha256', {}).items():
                assert sha256(ROOT/p) == h, p
                pins.add(p)
            for v in node.values():
                visit(v)
        elif isinstance(node, list):
            for v in node:
                visit(v)
    for value in values:
        visit(value)

    crops = values[6]+values[7]
    for crop in crops:
        src = crop['source']['path'] if isinstance(crop['source'], dict) else crop['source']
        out = crop['output']['path'] if isinstance(crop['output'], dict) else crop['output']
        box = crop.get('crop_box_xyxy', crop.get('box_pixels'))
        with Image.open(ROOT/src) as parent, Image.open(ROOT/out) as target:
            expected = parent.crop(box)
            assert (expected.mode, expected.size, expected.tobytes()) == (target.mode, target.size, target.tobytes()), out
    independent = values[4]
    assert independent['all_checks_passed'] and independent['mismatches'] == []
    assert independent['background_statuses_compared'] == 4920
    assert independent['local_statuses_compared'] == 410
    actual_ids = {o['excavation_number'] for o in values[0]['objects']}
    actual_ids |= {o['excavation'].removeprefix('CH') for o in values[1]['objects']}
    assert actual_ids == {'2428', '2529, CC', '2285', '3215', '3207'}
    assert all(o['semantic_value'] is None for o in values[0]['objects'])
    assert not values[1]['new_downloads']

    checks = []
    for r in values[5]['control_morphology_sensitivity']:
        checks.append((r['review_conditioned_profile'], r['review_conditioned_bounds']))
    for r in values[5]['comparison_original_text_edge_sensitivity']:
        checks.append((r['profile'], r['difference_bounds']))
    for profile, interval in checks:
        unknown = [i for i, status in enumerate(profile) if status == 'unknown']
        differences = []
        for bits in itertools.product([0, 1], repeat=len(unknown)):
            assignment = dict(zip(unknown, bits))
            presence = [assignment[i] if status == 'unknown' else int(status == 'positive') for i, status in enumerate(profile)]
            differences.append(Fraction(sum(presence[:3]), 3)-Fraction(sum(presence[3:]), 2))
        assert interval == [str(min(differences)), str(max(differences))]

    write_json('results/chanhu_local_graphics_audit.json', {
        'distinct_evidence_pins_verified': len(pins), 'exact_crops_verified': len(crops),
        'five_physical_objects_accounted_for': True,
        'independently_reconstructed_code_statuses': 5330,
        'photo_sensitivity_intervals_brute_force_verified': len(checks),
        'semantic_values_assigned': 0, 'phonetic_values_assigned': 0,
        'scope': 'Pins, crop identity and arithmetic; not proof of whole-text completeness, archaeological comparability or meaning.',
        'input_sha256': {p: sha256(ROOT/p) for p in paths + ['docs/CHANHU_LOCAL_GRAPHICS_AND_SPECIFICITY.md']},
    })
    print(f'Local graphics audit: {len(pins)} pins, {len(crops)} exact crops, 5 objects, {len(checks)} sensitivity intervals.')


if __name__ == '__main__':
    main()
