"""Check finite-frame integrity, source/crop pins and exact local contrast bounds."""
import itertools
import json
from fractions import Fraction
from PIL import Image
from common import ROOT, sha256, write_json


def read(path):
    return json.loads((ROOT/path).read_text())


def main():
    paths = [
        'data/processed/chanhu_recording_method_review.json',
        'data/processed/chanhu_deposit_seal_register.json',
        'data/processed/chanhu_deposit_exposure_review.json',
        'data/processed/chanhu_deposit_test_design_review.json',
        'data/processed/chanhu_fieldcard_archive_search.json',
        'results/chanhu_deposit_join_independent.json',
        'results/chanhu_deposit_metadata_joins.json',
        'results/chanhu_deposit_support.json',
        'results/chanhu_local_contrast.json',
        'results/chanhu_fieldcard_targets.json',
        'results/chanhu_deposit_source_integration.json',
    ]
    values = [read(p) for p in paths]
    pins = set()

    def check(node):
        if isinstance(node, dict):
            if 'path' in node and 'sha256' in node:
                p = ROOT/node['path']
                assert sha256(p) == node['sha256'], node['path']
                if 'bytes' in node:
                    assert p.stat().st_size == node['bytes'], node['path']
                pins.add(node['path'])
            if 'input_sha256' in node:
                for p, h in node['input_sha256'].items():
                    assert sha256(ROOT/p) == h, p
                    pins.add(p)
            for child in node.values():
                check(child)
        elif isinstance(node, list):
            for child in node:
                check(child)
    for value in values:
        check(value)

    register, independent, joins, support, local = values[1], values[5], values[6], values[7], values[8]
    expected_ids = {f'LI.{n}' for n in range(1, 34)} | {f'LII.{n}' for n in range(1, 33)}
    assert {r['row_id'] for r in register['rows']} == expected_ids
    assert len(register['rows']) == 65
    assert {r['primary']['row_id'] for r in joins['rows']} == expected_ids
    assert {r['primary_row'] for r in support['rows']} == expected_ids
    assert independent['mismatches'] == []
    assert independent['all_full_rows_equal'] and independent['all_summary_fields_equal']
    assert support['support_matrix'] == []
    assert all(r['sign_outcome'] is None for r in support['rows'])

    crops = 0
    for row in register['crop_pins']:
        with Image.open(ROOT/row['parent_image']) as source, Image.open(ROOT/row['path']) as target:
            im = source.crop(row['crop_box_xyxy'])
            if row.get('resize_output'):
                im = im.resize(tuple(row['resize_output']))
            assert (im.mode, im.size, im.tobytes()) == (target.mode, target.size, target.tobytes()), row['path']
        crops += 1
    for row in read('data/processed/chanhu_deposit_crop_manifest.json') + independent['crop_manifest']:
        output = row['output']['path'] if isinstance(row['output'], dict) else row['output']
        box = row.get('crop_box_pixels', row.get('box_xyxy'))
        with Image.open(ROOT/row['source']) as source, Image.open(ROOT/output) as target:
            im = source.crop(box)
            assert (im.mode, im.size, im.tobytes()) == (target.mode, target.size, target.tobytes()), output
        crops += 1

    # Independent brute force over actual unknown labels verifies every endpoint.
    objects = {r['primary_row']: r for r in local['objects']}
    checks = 0
    scenarios = local['omission_sensitivity']['scenarios']
    assert len(scenarios) == 32 and len({tuple(s['retained_primary_rows']) for s in scenarios}) == 32
    for scenario in scenarios + [{'retained_primary_rows': list(objects),
                                 'family': local['fixed_five_object_contrasts']['fish'],
                                 'plain': local['fixed_five_object_contrasts']['plain_fish']}]:
        rows = [objects[k] for k in scenario['retained_primary_rows']]
        for field, label in [('fish', 'family'), ('plain_fish', 'plain')]:
            groups = [[r for r in rows if r['group'] == group] for group in ['associated_complex', 'bath_vicinity']]
            if not all(groups):
                assert scenario[label]['difference_bounds'] is None and not scenario[label]['available']
            else:
                unknown = [r['primary_row'] for r in rows if r[field] == 'unknown']
                differences = []
                for completion in itertools.product([0, 1], repeat=len(unknown)):
                    assigned = dict(zip(unknown, completion))
                    fractions = [Fraction(sum(assigned[r['primary_row']] if r[field] == 'unknown' else int(r[field] == 'positive') for r in g), len(g)) for g in groups]
                    differences.append(fractions[0]-fractions[1])
                assert scenario[label]['difference_bounds'] == [str(min(differences)), str(max(differences))]
            checks += 1
    assert local['omission_sensitivity']['available'] == 21
    assert local['omission_sensitivity']['unavailable'] == 11
    assert not local['strict_test_repaired'] and not local['assumptions_verified']
    assert values[4]['archive_located']
    assert all(not r['card_contents_acquired'] and not r['individual_card_presence_verified'] for r in values[9]['targets'])

    write_json('results/chanhu_deposit_review_audit.json', {
        'distinct_evidence_pins_verified': len(pins), 'exact_crops_verified': crops,
        'primary_frame_rows_verified': 65, 'independent_bound_checks': checks,
        'semantic_values_assigned': 0, 'phonetic_values_assigned': 0,
        'scope': 'Verifies evidence integrity, fixed frame and calculations; does not authenticate archaeological comparability or decipher signs.',
        'input_sha256': {p: sha256(ROOT/p) for p in paths + ['docs/CHANHU_DEPOSIT_RESULTS.md']},
    })
    print(f'Chanhudaro deposit audit: {len(pins)} pins, {crops} crops, 65 frame rows, {checks} exact bound checks.')


if __name__ == '__main__':
    main()
