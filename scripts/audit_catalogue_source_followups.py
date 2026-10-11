"""Verify bounded source-recovery outcomes without rewriting earlier reviews."""
import json
from common import ROOT, sha256, write_json


def main():
    paths = ['data/processed/h843_identity_followup.json', 'data/processed/h1817_identity_followup.json',
             'data/processed/m735_alias_followup.json', 'data/processed/catalogue_method_review.json']
    h843, h1817, m735, method = reviews = [json.loads((ROOT / p).read_text()) for p in paths]
    counts = {}
    for path, review in zip(paths, reviews):
        for item in review['evidence_files']:
            assert sha256(ROOT / item['path']) == item['sha256'], item['path']
            assert (ROOT / item['path']).stat().st_size == item['bytes'], item['path']
        counts[path] = len(review['evidence_files'])
    assert h843['identity']['H843_to_14307'] == 'primary_catalogue_authenticated'
    assert h843['identity']['H843_to_M775326'] == 'unresolved'
    assert not h843['M775326_comparison']['explicit_catalogue_join']
    assert not h1817['H1817_identity_authenticated'] and not h1817['H1817_graphics_authenticated']
    assert m735['modern_alias_to_field_verified'] and not m735['finnish_number_used_as_M77_identity']
    assert not method['particular_decomposition_certified']
    assert h843['semantic_values'] is None and h843['phonetic_values'] is None
    for review in (h1817, m735, method):
        assert review['semantic_value'] is None and review['phonetic_value'] is None
    write_json('results/catalogue_source_followup_audit.json', {
        'H843': h843, 'H1817': h1817, 'M735_alias': m735, 'editorial_method': method,
        'evidence_pin_checks_by_review': counts,
        'state_update_scope': 'Later evidence verifies H843/14307 and M735/DK-C3070 aliases. Earlier source-exposed reviews are retained unchanged as historical records. H843/M77:5326 and H1817 remain unresolved.',
        'new_numbered_graphic_assignments': 0, 'global_conversion_promoted': False,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'input_sha256': {p: sha256(ROOT / p) for p in paths}})
    print('Source follow-up hashes verified; two alias updates retained separately from unresolved joins and sign values.')


if __name__ == '__main__':
    main()
