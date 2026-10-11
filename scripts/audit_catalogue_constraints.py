"""Minimal contradiction witnesses for explicitly scoped catalogue correspondences."""
import json
from itertools import combinations
from collections import defaultdict
from common import ROOT, sha256, write_json

MODELS = {
    'bijective_single': {'max_span': 1, 'deterministic': True, 'injective': True},
    'deterministic_single': {'max_span': 1, 'deterministic': True, 'injective': False},
    'deterministic_span': {'max_span': 2, 'deterministic': True, 'injective': False},
    'span_relation': {'max_span': 2, 'deterministic': False, 'injective': False},
}


def violations(assertions, model):
    result = []
    for a in assertions:
        if not 1 <= len(a['M']) <= model['max_span']:
            result.append({'kind': 'span_cardinality', 'assertion_ids': [a['id']]})
    for a, b in combinations(assertions, 2):
        if model['deterministic'] and a['W'] == b['W'] and a['M'] != b['M']:
            result.append({'kind': 'same_W_different_M_span', 'assertion_ids': [a['id'], b['id']]})
        if model['injective'] and a['W'] != b['W'] and a['M'] == b['M']:
            result.append({'kind': 'different_W_same_M_span', 'assertion_ids': [a['id'], b['id']]})
    return result


def main():
    review_paths = ['data/processed/pincer_primary_review.json', 'data/processed/ending_mapping_review.json',
                    'data/processed/comb_variation_review.json', 'data/processed/double_grid_primary_review.json',
                    'data/processed/w525_primary_review.json', 'data/processed/m735_primary_review.json',
                    'data/processed/h133_w554_primary_review.json', 'data/processed/m897_mapping_review.json']
    reviews = {p: json.loads((ROOT / p).read_text()) for p in review_paths}
    for review in reviews.values():
        for item in review['evidence_files']:
            assert sha256(ROOT / item['path']) == item['sha256'], item['path']
    core = []
    def add(key, w, m, source, object_id, scope):
        core.append({'id': key, 'W': w, 'M': m, 'review': source,
                     'primary_object_reference': object_id, 'scope': scope})
    p = review_paths[0]
    for entry in reviews[p]['local_target_correspondences']:
        add('M63_' + entry['W'], entry['W'], [entry['M']], p, 'DK8333/M77:3068', 'Explicit local target correspondence')
    p = review_paths[1]
    add('L89_W555', 'W555', [reviews[p]['catalogue_conflict']['primary_comparison_M']], p, '15337/M77:7090', 'Explicit crossed-sign target')
    add('L89_W527', 'W527', [reviews[p]['primary_artifact_bridge']['M77_candidate_reading_order'][-1]], p, '15337/M77:7090', 'Comb correspondence stated in primary bridge finding')
    p = review_paths[2]
    add('MIC158_W526', 'W526', [reviews[p]['observed_normalized_reading_order'][-1]], p, 'DM50/MIC158/M77:1158', 'Frozen input review: modern M934 alias not separately checked. Later CISI2 review supplies labelled photos but retains DM56/DM50 conflict; no change to this selected MIC158 target.')
    p = review_paths[3]
    span = reviews[p]['span_alignment']
    assert len(span['W']) == 1
    add('M81_W617', span['W'][0], span['M'], p, 'C3133/MIC180/M77:1180', 'Explicit local span, not ancient grapheme boundaries')
    p = review_paths[4]
    for case in reviews[p]['cases']:
        if case['status'] == 'supported_local_catalogue_correspondence':
            add(case['secondary_cisi'] + '_W525', 'W525', [case['local_W525_to']], p,
                case['field_number'] + '/M77:' + str(case['m77_reference']), 'Primary old-publication bridge; modern CISI alias not separately checked')
    p = review_paths[5]
    add('MIC60_W195', reviews[p]['local_target'], [reviews[p]['local_M']], p, 'C3070/MIC60/M77:1060', reviews[p]['correspondence_status'])
    p = review_paths[6]
    target = reviews[p]['target_correspondence']
    add('EH261_W554', target['W'], [target['M']], p, '8360/EH261/M77:4261', 'Target only; other six numeric codes not newly certified')
    uncertain = {'id': 'FEM545_W550_uncertain', 'W': 'W550', 'M': ['M222'],
                 'review': review_paths[7], 'primary_object_reference': 'DK9111/FEM545/M77:2545',
                 'scope': reviews[review_paths[7]]['scope']}
    grouped = defaultdict(list)
    for a in core:
        grouped[(a['W'], tuple(a['M']))].append(a['id'])
    unique = [{'W': w, 'M': list(ms), 'assertion_ids': ids} for (w, ms), ids in sorted(grouped.items())]
    outcomes = {}
    for population, assertions in [('core_local_targets', core), ('with_uncertain_M897', core + [uncertain])]:
        outcomes[population] = {name: {'satisfiable_on_these_assertions': not (bad := violations(assertions, definition)),
                                       'minimal_contradiction_witnesses': bad}
                                for name, definition in MODELS.items()}
    m_codes = {m for a in core for m in a['M']}
    coverage = [{'M': f'M{i:03d}', 'local_assertion_ids': [a['id'] for a in core if f'M{i:03d}' in a['M']],
                 'semantic_value': None, 'phonetic_value': None,
                 'status': 'local catalogue evidence only' if f'M{i:03d}' in m_codes else 'not constrained by this selected audit'} for i in range(1, 418)]
    paths = ['data/processed/catalogue_constraint_protocol.json', *review_paths]
    write_json('results/catalogue_constraint_audit.json', {
        'protocol': json.loads((ROOT / paths[0]).read_text()), 'models': MODELS,
        'core_assertions': core, 'uncertain_sensitivity_assertion': uncertain,
        'deduplicated_W_to_span_assertions': unique, 'outcomes': outcomes, 'M_inventory_coverage': coverage,
        'summary': {'core_local_assertions': len(core), 'distinct_W_to_span_assertions': len(unique),
                    'constrained_W_codes': sorted({a['W'] for a in core}), 'M_members': sorted(m_codes),
                    'M_inventory_members': 417},
        'proof_scope': 'For these models, every rule is unary or binary. Absence of the listed violations is sufficient to construct the finite function/relation; unconstrained codes remain free. This is not evidence that the model generalizes.',
        'input_sha256': {p: sha256(ROOT / p) for p in paths},
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'global_conversion_promoted': False})
    print(json.dumps({p: {m: o['satisfiable_on_these_assertions'] for m, o in v.items()} for p, v in outcomes.items()}, indent=2))


if __name__ == '__main__':
    main()
