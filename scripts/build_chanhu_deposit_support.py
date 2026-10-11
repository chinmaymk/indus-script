"""Save context-only eligibility for the finite seal frame before any new outcomes."""
import json
from collections import Counter
from common import ROOT, sha256, write_json

DIRECT_REVIEWS = {
    '2285': ('associated_production_complex', '215/286/297',
             'Seal room-list +10.4 ft; bead floor +9.3 ft. Same room does not establish same floor event.'),
    '2428': ('associated_production_complex', '215/286/297',
             'Passage 286 floor at +9.7 ft; production attributed to adjoining complex, not this exact floor assemblage.'),
    '2529, CC': ('associated_production_complex', '215/286/297',
                'Courtyard spread +10.4 ft; unfinished beads reported in courtyard, but their event/level is not independently joined.'),
    '2297': ('production_context_level_conflict', '174',
             'Catalogue +10.0 ft conflicts with narrative below beads +6.8 ft; do not select one silently.'),
    '3207': ('lower_evidence_comparison_candidate', '442-vicinity',
             'Bath floor +6.7 ft; seal catalogue +7.7 ft. Narrative says vicinity/near level, not floor deposition.'),
    '3215': ('lower_evidence_comparison_candidate', '442-vicinity',
             'Bath vicinity in narrative; seal catalogue locus283 +6.9 ft; square discrepancy also retained.'),
    '2390': ('alternative_craft_vicinity_only', '235-near284',
             'Seal235 +9.9 ft is nearby, not inside metalhoard284 +9.5 ft.'),
}


def main():
    paths = ['data/processed/chanhu_deposit_seal_register.json',
             'data/processed/chanhu_deposit_exposure_review.json',
             'data/processed/chanhu_primary_review.json',
             'docs/CHANHU_WORKSHOP_CONTEXT_REVIEW.md',
             'docs/CHANHU_DEPOSIT_PROTOCOL.md',
             'docs/CHANHU_DEPOSIT_TEST_DESIGN_REVIEW.md']
    register, exposure = [json.loads((ROOT/p).read_text()) for p in paths[:2]]
    rows = []
    for seal in register['rows']:
        candidates = [c for c in exposure['contexts'] if seal['locus_raw'] in c['locus_identifiers']]
        reviewed = DIRECT_REVIEWS.get(seal['excavation_number_raw'])
        rows.append({
            'primary_row': seal['row_id'], 'excavation_number': seal['excavation_number_raw'],
            'locus': seal['locus_raw'], 'elevation_ft': seal['elevation_ft'],
            'context_locator_candidates_NOT_deposit_joins': [c['id'] for c in candidates],
            'reviewed_association_tier': reviewed[0] if reviewed else 'no_secured_deposit_join_in_current_review',
            'potential_dependence_block': reviewed[1] if reviewed else None,
            'reason': reviewed[2] if reviewed else 'Catalogue position and any same-locus narrative lead do not yet establish a phase-compatible deposit assemblage.',
            'strict_deposit_exposure': 'D?',
            'eligible_for_strict_matched_test_now': False,
            'sign_outcome': None,
        })
    context_coverage = []
    for c in exposure['contexts']:
        context_coverage.append({'context_id': c['id'], 'reported_exposure': c['exposure_category'],
            'association': c['deposit_association'],
            'same_locus_catalogue_candidates_NOT_joins': [r['primary_row'] for r in rows if c['id'] in r['context_locator_candidates_NOT_deposit_joins']]})
    summary = {
        'framed_objects': len(rows),
        'reviewed_named_seal_associations': len(DIRECT_REVIEWS),
        'reviewed_association_tiers': dict(Counter(r['reviewed_association_tier'] for r in rows)),
        'strict_eligible_objects': 0, 'strict_matched_strata': 0,
        'new_sign_outcomes_examined': 0, 'semantic_values_assigned': 0,
        'status': 'No secured matched deposit contrast in the reviewed evidence; broader area-based comparison remains assumption-dependent.',
    }
    write_json('results/chanhu_deposit_support.json', {
        'summary': summary, 'rows': rows, 'context_coverage': context_coverage,
        'support_matrix': [],
        'eligibility_decision_before_new_sign_counts': True,
        'limits': [
            'D? means unresolved association/reporting/phase, not absence of production.',
            'The narrative screen is not an exhaustive reanalysis of every framed locus; unreviewed or uncertain records remain explicit.',
            'No test statistic computed: there are no secured phase/deposit/reporting strata containing both exposure classes.',
            'A broader building/vicinity analysis requires a separate declared assumption set; it is not disproved by this strict gate.',
            '215/286/297 cannot be counted as three independent production complexes.',
        ],
        'input_sha256': {p: sha256(ROOT/p) for p in paths},
    })
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
