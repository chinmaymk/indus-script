"""Validate pinned tablet-photo reviews without promoting fine graphic certainty."""
import json
from PIL import Image
from common import ROOT, sha256, write_json
from audit_roof_variant_artifacts import check_crop


def main():
    paths = ['data/processed/roof_fish_4493_review.json',
             'data/processed/roof_fish_5477_review.json']
    reviews = [json.loads((ROOT / p).read_text()) for p in paths]
    pins = 0
    for review in reviews:
        for pin in review['evidence_files']:
            assert sha256(ROOT / pin['path']) == pin['sha256'], pin['path']
            assert (ROOT / pin['path']).stat().st_size == pin['bytes'], pin['path']
            pins += 1
        assert review['semantic_values'] is None and review['phonetic_values'] is None
    a, b = reviews
    assert a['metadata']['field'] == '8650b'
    assert a['metadata']['field_key_kind'] == 'shared_find_group_not_unique_artifact'
    assert a['published_object']['catalogued_physical_objects'] == 1
    assert not a['photographic_fields'][0]['exact_M066_feature_bundle_photographically_certified']
    assert not a['photographic_fields'][1]['exact_four_long_strokes_independently_certified']
    assert b['m77_reference'] == '5477' and b['excavation_number'] == '13592'
    assert b['cisi_alias'] == 'H-889' and b['museum'] == 'HM332'
    assert b['frozen_prediction']['source_direction'] == 2
    assert b['second_field']['field_symbol'] == '83' and not b['second_field']['script_tokens']
    assert not b['photograph_views'][0]['unqualified_roof_absence_certified']
    assert not b['strict_corpus_changed'] and not b['source_tokens_reversed']
    assert not b['historical_photo_itself_recovered'] and b['independent_artifacts_represented'] == 1
    frozen_path = 'data/processed/roof_m176_primary_review.json'
    fields = {f['field_id']: f for f in json.loads((ROOT / frozen_path).read_text())['fields']}
    for f in a['normalized_fields_from_frozen_review']:
        assert fields[f['field_id']]['normalized_tokens'] == f['tokens']
    assert fields['5477:1:0']['normalized_tokens'] == b['frozen_prediction']['first_field']
    count = 0
    for path in ['data/processed/roof_fish4493_crop_manifest.json',
                 'data/processed/roof_fish5477_crop_manifest.json']:
        paths.append(path)
        for c in json.loads((ROOT / path).read_text()):
            with Image.open(ROOT / c['source']) as source:
                box = [round(v * (source.width if i % 2 == 0 else source.height))
                       for i, v in enumerate(c['fractional_box'])]
            check_crop(c['source'], c.get('crop', c.get('output')), box)
            count += 1
    paths += [frozen_path, 'scripts/audit_roof_fish_photos.py',
              'scripts/audit_roof_variant_artifacts.py']
    write_json('results/roof_fish_photo_audit.json', {
        'reviews': reviews, 'evidence_pin_checks': pins, 'exact_pixel_crop_checks': count,
        'original_artifacts_reviewed': 2, 'fine_photo_transcriptions_certified': 0,
        'corpus_recoded': False, 'established_semantic_values': 0, 'established_phonetic_values': 0,
        'scope': 'Exact source identity plus qualified broad morphology; hashes/pixels do not prove manual visual judgments. No same-die independence certification.',
        'input_sha256': {p: sha256(ROOT / p) for p in paths}})
    print(f'Roof fish photographs: {pins} evidence pins, {count} pixel checks; fine readings remain qualified.')


if __name__ == '__main__':
    main()
