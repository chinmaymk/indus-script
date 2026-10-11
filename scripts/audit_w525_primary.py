"""Join reviewed primary W525 anchors to separate diagnostic source locators."""
import csv
import json
from common import ROOT, sha256, write_json


def main():
    paths = ['data/processed/w525_primary_review.json', 'results/w525_screen.json',
             'results/w525_independent.json', 'data/processed/m77_candidate_strict.jsonl',
             'data/processed/mahadevan_1977_table_i.csv']
    review, screen, verification = [json.loads((ROOT / p).read_text()) for p in paths[:3]]
    for pin in review['evidence_files']:
        assert sha256(ROOT / pin['path']) == pin['sha256'], pin['path']
        assert (ROOT / pin['path']).stat().st_size == pin['bytes'], pin['path']
    assert verification['all_checks_passed']
    for p, digest in verification['input_sha256'].items():
        assert sha256(ROOT / p) == digest, p
    assert not review['global_rule_promoted']
    assert review['semantic_value'] is None and review['phonetic_value'] is None
    strict_refs = {str(json.loads(line)['source_reference'])
                   for line in (ROOT / paths[3]).read_text().splitlines() if line.strip()}
    anchors = []
    excluded = []
    for case in review['cases']:
        if case['status'] != 'supported_local_catalogue_correspondence':
            assert case['local_W525_to'] is None
            excluded.append(case)
            continue
        matches = [p for p in screen['post_null_multidocument_locator_candidates']
                   if p['lipi_row']['id'] in case['secondary_rows']
                   and str(p['source_locator_record']['source_reference']) == str(case['m77_reference'])]
        assert len(matches) == 1
        pair = matches[0]
        assert pair['W525_candidate'] == case['local_W525_to'] == 'M254'
        assert pair['source_locator_record']['source_doc_count'] > 1
        assert str(case['m77_reference']) not in strict_refs
        reconstructed = '+' + '-'.join(w.removeprefix('W') for w in pair['lipi_row']['sequence']) + '+'
        assert reconstructed in case['raw_texts']
        if 'normalized_right_to_left' in case:
            assert [t['sign'] for t in pair['source_locator_record']['tokens']] == case['normalized_right_to_left']
        anchors.append({'primary_case': case, 'diagnostic_locator': pair,
                        'identity_basis': 'Original excavation number, numbered illustration and explicit M77 appendix bridge; not sequence compatibility',
                        'correspondence_scope': 'Artifact-local W525/M254 identification in the published transcription; fine photographic strokes limited'})
    assert len(anchors) == 2 and len(excluded) == 1
    with (ROOT / paths[4]).open() as f:
        profiles = [{k: int(v) if k in ('solus', 'initial', 'medial', 'final', 'total') else v
                     for k, v in r.items()} for r in csv.DictReader(f) if r['sign'] == 'M254']
    write_json('results/w525_primary_audit.json', {
        'reviewed_anchors': anchors, 'excluded_identity_cases': excluded,
        'primary_evidence_files_verified': len(review['evidence_files']),
        'strict_search_summary': screen['summary'],
        'separate_diagnostic_locator_count': len(screen['post_null_multidocument_locator_candidates']),
        'primary_Table_I_position_profiles': profiles,
        'profile_scope': 'Historical M254 editorial category, not a new count of the W525 form or independent evidence of equal values',
        'global_mapping_established': False, 'face_level_corpus_recovery_promoted': False,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'input_sha256': {p: sha256(ROOT / p) for p in paths}})
    print('W525: 44 primary pins, two local catalogue anchors, one excluded identity conflict; no global mapping.')


if __name__ == '__main__':
    main()
