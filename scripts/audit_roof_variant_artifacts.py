"""Check roof-review provenance and constraints; visual judgments remain manual."""
import csv
import json
import re
from PIL import Image
from common import ROOT, sha256, write_json

REVIEW_PATHS = [
    'data/processed/roof_fish_stroke_variant_review.json',
    'data/processed/roof_nonfish_variant_review.json',
    'data/processed/roof_m092_artifact_review.json',
    'data/processed/roof_x_identity_review.json',
]


def check_crop(source_path, target_path, box, rotation=0):
    with Image.open(ROOT / source_path) as source, Image.open(ROOT / target_path) as target:
        crop = source.crop(box)
        if rotation:
            crop = crop.rotate(rotation, expand=True)
        assert crop.size == target.size and crop.mode == target.mode, target_path
        assert crop.tobytes() == target.tobytes(), target_path


def main():
    reviews = [json.loads((ROOT / p).read_text()) for p in REVIEW_PATHS]
    fish, nonfish, artifact, cross = reviews
    pin_count = 0
    for review in reviews:
        for pin in review['evidence_files']:
            path = ROOT / pin['path']
            assert path.stat().st_size == pin['bytes'], pin['path']
            assert sha256(path) == pin['sha256'], pin['path']
            pin_count += 1
    assert fish['semantic_values'] is None and fish['phonetic_values'] is None
    assert cross['semantic_values'] is None and cross['phonetic_values'] is None
    for review in (nonfish, artifact):
        assert review['established_semantic_values'] == review['established_phonetic_values'] == 0
    assert artifact['semantic_value'] is None and artifact['phonetic_value'] is None
    assert not fish['candidate_pairs_changed'] and not fish['context_screen_recoded']
    assert not fish['universal_fixed_base_geometry_supported']
    assert not fish['all_roofed_counterparts_verified']

    # Source drawings, not independent ancient-object frequencies.
    assert {r['sign'] for r in fish['entries']} == {'M059', 'M060', 'M089'}
    assert all(not roof for r in fish['entries'] for roof in r['roof_present'])
    assert {r['code'] for r in nonfish['records']} == {'M137', 'M162', 'M334'}
    drawing_count = sum(len(r['references']) for r in fish['entries'])
    drawing_count += sum(r['appendix_drawings'] for r in nonfish['records'])
    assert drawing_count == 15
    crop_count = 0
    for record in nonfish['crop_records']:
        check_crop(record['source'], record['crop'], record['box_xyxy'])
        crop_count += 1
    from render_roof_fish_variants import CROPS
    for sign, (source, box) in CROPS.items():
        source_path = 'results/primary_pages/' + source
        with Image.open(ROOT / source_path) as image:
            pixels = tuple(round(v * (image.width if i % 2 == 0 else image.height))
                           for i, v in enumerate(box))
        check_crop(source_path, f'results/primary_pages/roof-variants-{sign}.png', pixels)
        crop_count += 1
    for record in json.loads((ROOT / 'data/processed/roof_m092_artifact_crop_manifest.json').read_text()):
        check_crop(record['source'], record['output'], record['pixel_crop'], record['counterclockwise_degrees'])
        crop_count += 1
    for record in json.loads((ROOT / cross['crop_manifest']).read_text()):
        with Image.open(ROOT / record['source']) as image:
            pixels = tuple(round(v * (image.width if i % 2 == 0 else image.height))
                           for i, v in enumerate(record['fractional_box']))
        check_crop(record['source'], record['crop'], pixels)
        crop_count += 1
    inference_text = (ROOT / 'docs/ROOF_INFERENCE_REVIEW.md').read_text()
    inference_pins = re.findall(r'`([^`]+)`: SHA256 `([0-9a-f]{64})`', inference_text)
    assert inference_pins
    for path, digest in inference_pins:
        assert sha256(ROOT / path) == digest, path

    assert artifact['m77_text'] == '8018' and artifact['cisi_alias'] == 'K-29'
    assert artifact['excavation_number'] == '8219'
    assert artifact['museum_registration'] == 'ASI 68.1.48'
    assert artifact['finnish_number_is_not_m77_reference']
    assert artifact['whole_field_remains_excluded_for_loss'] and not artifact['strict_corpus_changed']
    assert artifact['visual_observations']['independent_artifacts_represented'] == 1
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open() as stream:
        source_rows = [row for row in csv.DictReader(stream) if row['id'] == '1903.1']
    assert len(source_rows) == 1
    # Compare only recorded identity, condition and token columns; no translation fields.
    assert all(source_rows[0][k] == value for k, value in artifact['secondary_relevant_fields_only'].items())
    features = json.loads((ROOT / 'data/processed/catalogue_features.json').read_text())
    feature = next(f for f in features if f['id'] == 'P149')
    assert feature['wells_graphemes'] == ['W044'] and feature['mahadevan_graphemes'] == ['M092']
    assert not artifact['local_catalogue_mapping']['complete_W_M_transcription_equivalence_asserted']
    assert not artifact['local_catalogue_mapping']['unspecified_000_interpreted']
    assert not artifact['local_catalogue_mapping']['proposed_translation_fields_used']

    refs = {r['reference']: r for r in cross['references']}
    assert refs['4407']['excavation'] == '1722' and refs['4407']['original_photo_inspected']
    assert refs['4407']['damage']['source_classification'] == 'entire'
    assert refs['5444']['excavation'] == '3027(2)' and not refs['5444']['original_photo_inspected']
    assert not cross['rejected_automatic_join']['join_to_5444']
    assert not cross['identity_conclusions']['distinct_physical_artifacts_established']
    assert not cross['identity_conclusions']['duplicate_physical_artifact_established']
    assert cross['identity_conclusions']['safe_verified_photo_object_count'] == 1

    registry = json.loads((ROOT / 'data/sources.json').read_text())
    pending = json.loads((ROOT / cross['new_source_registry']).read_text())
    registered = {r['path']: r for r in registry['downloads']}
    for record in pending['downloads']:
        actual = registered[record['path']]
        for key in ('url', 'bytes', 'sha256'):
            assert actual[key] == record[key], record['path']
        assert sha256(ROOT / record['path']) == record['sha256']

    inputs = REVIEW_PATHS + [
        'scripts/audit_roof_variant_artifacts.py', 'scripts/render_roof_nonfish_variants.py',
        'docs/ROOF_VARIANT_ARTIFACT_RESULTS.md', 'docs/ROOF_INFERENCE_REVIEW.md',
        'data/processed/roof_x_identity_new_sources.json',
        'data/processed/roof_m092_artifact_crop_manifest.json',
        'data/processed/roof_x_identity_crop_manifest.json',
        'data/raw/lipi_inscriptions.csv', 'data/processed/catalogue_features.json',
        'results/roof_modifier_audit.json',
    ]
    write_json('results/roof_variant_artifact_audit.json', {
        'reviews': dict(zip(REVIEW_PATHS, reviews)),
        'evidence_pin_checks': pin_count,
        'exact_pixel_crop_checks': crop_count,
        'inference_review_pin_checks': len(inference_pins),
        'appendix_rows_reviewed': 6, 'appendix_drawings_reviewed': drawing_count,
        'original_artifacts_authenticated': ['K-29 / 8219 / ASI68.1.48', 'EH407 / 1722'],
        'unresolved_original_artifact': 'M77 5444 / 3027(2) / Pu35:3863',
        'new_source_records': len(pending['downloads']),
        'strict_corpus_changed': False, 'candidate_pairs_changed': False,
        'universal_fixed_base_geometry_supported': False,
        'common_roof_semantics_established': False, 'common_roof_semantics_refuted': False,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'limits': 'Hashes and crop pixels are machine-checked; artifact identities and graphic descriptions depend on explicitly recorded manual source reviews. No new independent context rectangle or semantic anchor.',
        'input_sha256': {p: sha256(ROOT / p) for p in inputs},
    })
    print(f'Roof follow-up: {pin_count} source pins, {crop_count} pixel checks, {drawing_count} Appendix drawings; two artifacts authenticated, no readings assigned.')


if __name__ == '__main__':
    main()
