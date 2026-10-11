"""Check later CISI2 evidence while retaining unresolved identities and readings.

Hashes protect the recorded observations; they cannot mechanically prove visual
interpretations. Earlier reviews and model protocols remain historical inputs.
"""
import json
from common import ROOT, sha256, write_json


def main():
    paths = {
        'H1123': 'data/processed/h1123_cisi2_review.json',
        'M897': 'data/processed/m897_cisi2_review.json',
        'M897_independent': 'data/processed/m897_cisi2_independent.json',
        'M934': 'data/processed/m934_cisi2_review.json',
    }
    reviews = {name: json.loads((ROOT / path).read_text()) for name, path in paths.items()}
    counts = {}
    for name, review in reviews.items():
        for item in review['evidence_files']:
            p = ROOT / item['path']
            assert p.stat().st_size == item['bytes'], item['path']
            assert sha256(p) == item['sha256'], item['path']
        counts[name] = len(review['evidence_files'])
        assert review.get('semantic_values', review.get('semantic_value')) is None
        assert review.get('phonetic_values', review.get('phonetic_value')) is None

    h, m, independent, c = [reviews[k] for k in paths]
    assert h['primary_coverage']['target_not_in_stated_range']
    assert not h['existing_conflict']['field9015_to_item360_authenticated']
    assert not h['existing_conflict']['correction_applied']
    assert m['identity']['modern_alias_to_field_verified']
    assert not m['identity']['finnish_number_used_as_M77_identity']
    assert m['graphic_review']['fine_sign_status'] == 'unresolved'
    assert not m['graphic_review']['specific_diagnostic_stroke_loss_authenticated']
    assert not m['secondary_record']['raw_changed']
    assert not m['model_update']['core_changed'] and not m['model_update']['sensitivity_changed']
    assert independent['artifact_count'] == 1 and independent['complementary_views'] == 2
    assert independent['fine_sign_conclusion']['W550_vs_W555'] == 'unresolved'
    assert independent['physical_condition']['fragmentary_object_supported']
    assert not independent['fine_sign_conclusion']['secure_recode_to_W555']
    assert c['conflict']['CISI2'] == 'DM56' and c['conflict']['Marshall_MIC158'] == 'DM50'
    assert not c['conflict']['resolved'] and c['conflict']['preferred_corrected_value'] is None
    assert c['photographs']['directly_labelled_M934_graphic_comparison_supported']
    assert c['photographs']['comb_stagger_opposite_L89_in_corresponding_impression_orientation']
    assert not c['global_allography_established']
    write_json('results/cisi2_dispute_audit.json', {
        'reviews': reviews, 'evidence_pin_checks_by_review': counts,
        'limits': 'Hash and disposition audit, not an automated visual proof. Parent and agent reviews were source-exposed; repeated images and shared catalogue sources are not independent archaeological witnesses.',
        'outcome': 'M897/DK9111 alias authenticated, fine crossed-sign reading unresolved. M934 photographs directly recovered, DM56/DM50 conflict retained. H1123 outside stated CISI2 coverage, 9015/356/360 conflict retained.',
        'new_downloads': 0, 'new_exact_sign_correspondences': 0,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'input_sha256': {p: sha256(ROOT / p) for p in paths.values()},
    })
    print(f'CISI2 dispute audit: {sum(counts.values())} evidence-pin checks; unresolved fields retained.')


if __name__ == '__main__':
    main()
