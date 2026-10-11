"""Explicit post-review sensitivities; never replace frozen source classifications."""
import itertools
import json
from common import ROOT, sha256, write_json
from analyze_chanhu_specificity import interval


def main():
    paths = ['results/chanhu_local_specificity.json',
             'data/processed/chanhu_local_primary_comparators_review.json',
             'data/processed/chanhu_local_primary_positive_review.json']
    specificity, comparators, positive = [json.loads((ROOT/p).read_text()) for p in paths]
    rows = {r['code']: r for r in specificity['all_code_results']}
    # The catalogue's W368 is retained. This alternative asks for independent
    # diagnostic graphic authentication at the damaged C22 corner.
    controls = []
    for code in ['W220', 'W368', 'W790']:
        profile = rows[code]['local_status_vector'].copy()
        if code == 'W368':
            assert profile[0] == 'positive'
            profile[0] = 'unknown'
        controls.append({'code': code, 'source_profile': rows[code]['local_status_vector'],
                         'review_conditioned_profile': profile,
                         'source_bounds': rows[code]['difference_bounds'],
                         'review_conditioned_bounds': interval(profile)})
    # No evidence says both bath texts lost signs. Enumerate the consequences
    # of withholding the source's original-whole-text absence assumption.
    scenarios = []
    for left, right in itertools.product([False, True], repeat=2):
        profile = rows['W220']['local_status_vector'].copy()
        for index, unknown in [(3, left), (4, right)]:
            if unknown:
                profile[index] = 'unknown'
        scenarios.append({'CH3215_original_absence_withheld': left,
                          'CH3207_original_absence_withheld': right,
                          'profile': profile, 'difference_bounds': interval(profile)})
    write_json('results/chanhu_photo_sensitivity.json', {
        'scope': 'Post-outcome, post-photo sensitivities; no source correction or new family definition.',
        'fixed_order': specificity['local_primary_order'],
        'control_morphology_sensitivity': controls,
        'comparison_original_text_edge_sensitivity': scenarios,
        'interpretation': [
            'W368 is partly supported morphologically but its full diagnostic form is not independently secure; W790 oval graphic is clear.',
            'Neither bath object has a securely visible fixed-family fish. Withholding original-whole-text absence is a sensitivity, not evidence a missing fish existed.',
            'Core-object and archaeological assumptions remain unchanged in these limited alternatives.',
            'No photographs establish meanings or exhaustive fine-code equivalence.',
        ],
        'semantic_values_assigned': 0, 'phonetic_values_assigned': 0,
        'input_sha256': {p: sha256(ROOT/p) for p in paths},
    })
    print(json.dumps({'control_sensitivity': controls, 'edge_sensitivity': scenarios}, indent=2))


if __name__ == '__main__':
    main()
