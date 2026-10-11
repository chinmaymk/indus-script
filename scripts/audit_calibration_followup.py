"""Verify retained follow-up evidence and independent calibration certificate."""
import json
from PIL import Image
from common import ROOT, sha256, write_json


def main():
    inputs = [
        'data/processed/umma_original_entry_followup.json',
        'data/processed/kotada_sample_photo_review.json',
        'data/processed/all_inventory_next_test_review.json',
        'results/numeral_calibration_design.json',
        'results/calibration_followup_source_integration.json',
        'results/kotada_supplement_independent.json',
    ]
    values = [json.loads((ROOT/p).read_text()) for p in inputs]
    pins = set()

    def visit(node):
        if isinstance(node, dict):
            if 'path' in node and 'sha256' in node:
                p = ROOT/node['path']
                assert sha256(p) == node['sha256'], node['path']
                if 'bytes' in node: assert p.stat().st_size == node['bytes'], node['path']
                pins.add(node['path'])
            for p, h in node.get('input_sha256', {}).items():
                assert sha256(ROOT/p) == h, p
                pins.add(p)
            for v in node.values(): visit(v)
        elif isinstance(node, list):
            for v in node: visit(v)
    for value in values: visit(value)
    for crop in values[1]['crops']:
        with Image.open(ROOT/crop['source']) as source, Image.open(ROOT/crop['path']) as actual:
            expected = source.crop(crop['rectangle_xyxy'])
            assert (expected.mode, expected.size, expected.tobytes()) == (actual.mode, actual.size, actual.tobytes())
    independent = values[2]['calibration_independent_validation']
    assert independent['mismatches'] == 0 and not independent['producer_imported']
    assert independent['polynomial_coefficients_descending'] == [403, -6026, 403]
    assert len(independent['error_cases']) == 4
    assert values[3]['current_authenticated_commensurate_quantity_pairs'] == 0
    assert values[2]['established_semantic_values'] == values[2]['established_phonetic_values'] == 0
    assert len(values[5]['exact_sample_labels_in_first_table']) == 10
    assert values[5]['unmatched_target_labels'] == ['KB-61']
    write_json('results/calibration_followup_audit.json', {
        'evidence_pins_verified': len(pins),
        'independent_calibration_error_cases': 4,
        'independent_calibration_mismatches': 0,
        'source_artifacts_in_phase': values[4]['phase_artifacts'],
        'independent_residue_label_matches': 10,
        'exact_native_crops_verified': len(values[1]['crops']),
        'unmatched_residue_label': 'KB-61',
        'new_authenticated_quantity_pairs_in_reviewed_cases': 0,
        'semantic_values_assigned': 0, 'phonetic_values_assigned': 0,
        'scope': 'Evidence integrity and conditional algebra; not a decipherment or exhaustive absence proof.',
        'input_sha256': {p: sha256(ROOT/p) for p in inputs + ['docs/NUMERAL_CALIBRATION_DESIGN.md']},
    })
    print(f'Calibration follow-up: {len(pins)} evidence pins; 4 independent error cases, zero mismatches.')


if __name__ == '__main__': main()
