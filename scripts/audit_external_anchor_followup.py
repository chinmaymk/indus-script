"""Check new source/review pins, native crop, search scope and inventory integrity.

Integrity checks do not establish a semantic reading or prove global absence.
"""
import csv
import json
from collections import Counter
from PIL import Image
from common import ROOT, sha256, write_json


def main():
    inputs = [
        'data/processed/chanhu_public_records_followup.json',
        'data/processed/new_external_anchor_screen.json',
        'data/processed/inscribed_weight_external_search.json',
        'data/processed/umma_renewed_search.json',
        'data/processed/umma_reproduced_image_review.json',
        'data/processed/kotada_anchor_followup.json',
        'data/processed/umma_reproduced_crop_manifest.json',
        'results/external_anchor_source_integration.json',
    ]
    values = [json.loads((ROOT / p).read_text()) for p in inputs]
    pins = set()
    historical_pin_resolutions = []

    def visit(node):
        if isinstance(node, dict):
            if 'path' in node and 'sha256' in node:
                p = ROOT / node['path']
                # The screen pinned README before the parent added this phase's
                # navigation link. Verify the exact historical bytes, never
                # silently repin the review to a changed document.
                if node['path'] == 'README.md' and node['sha256'] == '6277a19b644ec812681c3a412468c9b672f6430382222f678d62bcb4cf2559b6':
                    p = ROOT/'results/external_anchor_screen_readme_input.md'
                    historical_pin_resolutions.append({'original_path': node['path'], 'snapshot_path': str(p.relative_to(ROOT)), 'sha256': node['sha256']})
                assert sha256(p) == node['sha256'], node['path']
                if 'bytes' in node:
                    assert p.stat().st_size == node['bytes'], node['path']
                pins.add(str(p.relative_to(ROOT)))
            for p, digest in node.get('input_sha256', {}).items():
                assert sha256(ROOT / p) == digest, p
                pins.add(p)
            for child in node.values():
                visit(child)
        elif isinstance(node, list):
            for child in node:
                visit(child)

    for value in values:
        visit(value)
    crop = values[6]
    with Image.open(ROOT / crop['source']) as source, Image.open(ROOT / crop['output']) as output:
        expected = source.crop(crop['crop_box_pixels'])
        assert (expected.size, expected.mode, expected.tobytes()) == (output.size, output.mode, output.tobytes())
        assert source.size == tuple(crop['source_dimensions'])
    image_review = values[4]
    assert image_review['exact_sign_ids'] is None
    assert image_review['transcription'] is None
    assert image_review['semantic_values'] is None
    assert not image_review['provisional_field_id']['authenticated']
    assert not image_review['display_orientation']['mirrored']
    assert image_review['display_orientation']['rotation_applied'] == 0
    assert values[0]['queries_total'] == values[3]['queries_total'] == 5
    assert values[0]['HU_clarification']['HU817_HU804_are_museum_accessions'] is False
    assert values[3]['outcomes']['review_figure_recovered_and_visually_inspected']
    assert not values[3]['outcomes']['original_2017_report_page_recovered']
    samples = values[5]['samples']
    assert len(samples) == 11 and len({s['sample_id'] for s in samples}) == 11
    assert all(not s['photo_pixels_inspected'] and s['sign_sequence'] is None for s in samples)
    assert len(values[5]['queries_executed']) == 3

    # Catalogue coverage is not archaeological absence: persist the actual labels.
    with (ROOT/'data/raw/lipi_inscriptions.csv').open() as stream:
        types = Counter(row['type'] for row in csv.DictReader(stream))
    idx = json.loads((ROOT/'results/sign_evidence_417.json').read_text())
    assert len(idx['signs']) == 417
    assert all(r['semantic_value'] is None and r['phonetic_value'] is None for r in idx['signs'])
    write_json('results/external_anchor_followup_audit.json', {
        'distinct_evidence_pins_verified': len(pins),
        'exact_native_crops_verified': 1,
        'historical_pin_resolutions': historical_pin_resolutions,
        'residue_sample_ids_accounted_for': 11,
        'source_artifacts_in_phase': values[7]['phase_artifacts'],
        'all_sign_inventory_entries': 417,
        'semantic_or_phonetic_values_assigned': 0,
        'catalogue_object_type_counts': dict(sorted(types.items())),
        'catalogue_type_limit': 'No explicit WEIGHT label does not imply that inscribed weights do not exist or cannot be included under another type.',
        'scope': 'Byte and pixel integrity, recorded review constraints and corpus labels; not independent proof of archaeological facts or exhaustive absence.',
        'input_sha256': {p: sha256(ROOT/p) for p in inputs + [
            'data/raw/lipi_inscriptions.csv',
            'docs/EXTERNAL_ANCHOR_RENEWED_RESULTS.md',
            'docs/UMMA_RENEWED_SOURCE_SEARCH.md']},
    })
    print(f'External-anchor follow-up: {len(pins)} evidence pins and 1 exact crop verified; 417 values remain unassigned.')


if __name__ == '__main__':
    main()
