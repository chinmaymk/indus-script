"""Keep local published-sign correspondences separate from unjoined tablet locators."""
import json
from common import ROOT, sha256, write_json


def main():
    paths = ['data/processed/m735_primary_review.json', 'data/processed/comb_tablet_primary_review.json',
             'results/comb_tablet_screen.json', 'results/comb_tablet_independent.json',
             'data/processed/h133_w554_primary_review.json']
    m735, tablets, screen, verifier, h133 = [json.loads((ROOT / p).read_text()) for p in paths]
    pins = 0
    for review in (m735, tablets, h133):
        for item in review['evidence_files']:
            assert sha256(ROOT / item['path']) == item['sha256'], item['path']
            assert (ROOT / item['path']).stat().st_size == item['bytes'], item['path']
            pins += 1
        assert review['semantic_value'] is None and review['phonetic_value'] is None
    assert verifier['all_checks_passed']
    for p, digest in verifier['input_sha256'].items():
        assert sha256(ROOT / p) == digest, p
    experiment = next(e for e in screen['experiments'] if e['target'] == 'W195'
                      and e['pool'] == 'strict' and not e['experimental_W525_M254_extension'])
    matches = [p for p in experiment['pairs'] if p['lipi_row']['id'] == m735['secondary_row_id']
               and str(p['M_record']['source_reference']) == str(m735['M77_reference'])]
    assert len(matches) == 1
    assert matches[0]['masked_M_candidate'] == m735['local_M'] == 'M054'
    assert matches[0]['lipi_row']['sequence'] == m735['W_file_sequence']
    h_experiment = next(e for e in screen['experiments'] if e['target'] == 'W554'
                        and e['pool'] == 'strict' and not e['experimental_W525_M254_extension'])
    h_matches = [p for p in h_experiment['pairs'] if p['lipi_row']['id'] == h133['secondary_row']
                 and str(p['M_record']['source_reference']) == str(h133['m77_bridge']['reference'])]
    assert len(h_matches) == 1
    assert h_matches[0]['masked_M_candidate'] == h133['target_correspondence']['M'] == 'M226'
    assert h_matches[0]['lipi_row']['sequence'] == h133['secondary_source_sequence']
    assert not h133['H1817_authenticated_by_this_review'] and not h133['global_mapping_promoted']
    assert tablets['authenticated_requested_artifacts'] == 0
    assert not tablets['actual_pair_graphic_comparison_possible']
    candidate = next(p for e in screen['experiments'] if e['target'] == 'W195'
                     and not e['experimental_W525_M254_extension'] and e['pool'] == 'multi_document_locator_only'
                     for p in e['pairs'] if str(p['M_record']['source_reference']) == '5326')
    assert [t['sign'] for t in candidate['M_record']['tokens']] == tablets['candidate_5326']['normalized_right_to_left']
    write_json('results/comb_tablet_review_audit.json', {
        'local_M735_review': m735, 'local_H133_review': h133, 'unresolved_tablet_review': tablets,
        'matching_H133_candidate': h_matches[0],
        'matching_M735_candidate': matches[0], 'unjoined_5326_candidate': candidate,
        'evidence_pin_checks': pins,
        'conclusion': 'Local W195/M054 and W554/M226 correspondences are supported through MIC60/C3070/M77 1060 and EH261/8360/M77 4261. The requested H1817/H843 actual graphic comparison remains unresolved.',
        'global_mapping_established': False, 'H843_identity_promoted': False,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'input_sha256': {p: sha256(ROOT / p) for p in paths}})
    print('Primary review pins and candidates agree; requested tablet identities remain unresolved.')


if __name__ == '__main__':
    main()
