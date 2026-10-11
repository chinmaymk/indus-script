"""Exact, conditional unit-free discrimination of two numerical candidates.

No new measured quantity or ancient reading is supplied by this calculation.
"""
import json
from fractions import Fraction as F
from math import sqrt
from common import ROOT, sha256, write_json


def ratio_interval(predictions, error):
    a, b = map(F, predictions)
    e = F(error)
    if min(a, b) <= 0 or not 0 <= e < 1:
        raise ValueError('Positive predictions and 0 <= relative error < 1 required')
    r = b / a
    return (r * (1-e)/(1+e), r * (1+e)/(1-e))


def feasible_unit_interval(predictions, observations, error):
    """u*n_i lies in q_i*[1-e,1+e]; no independently fixed unit."""
    e = F(error)
    if len(predictions) != len(observations) or not predictions or not 0 <= e < 1:
        raise ValueError('Nonempty equal lengths and 0 <= error < 1 required')
    pairs = [(F(n), F(q)) for n, q in zip(predictions, observations)]
    if any(min(n, q) <= 0 for n, q in pairs):
        raise ValueError('Positive predictions and observations required')
    low = max(q*(1-e)/n for n, q in pairs)
    high = min(q*(1+e)/n for n, q in pairs)
    return (low, high) if low <= high else None


def disjoint(a, b):
    return a[1] < b[0] or b[1] < a[0]


def main():
    source = 'results/numeral_equation_audit.json'
    candidates = json.loads((ROOT/source).read_text())['after_conditional_digit_bounds']
    assert candidates == [{'L': 10, 'S': 8, 'v': 6}, {'L': 36, 'S': 20, 'v': 4}]
    rows = []
    for c in candidates:
        L, S, v = (c[k] for k in ('L', 'S', 'v'))
        a, b = 3*L+v, v*L+1
        assert a == 2*L+2*S and b == 7*S+5
        rows.append({'candidate': c, 'A': a, 'B': b, 'B_over_A': str(F(b, a))})
    vectors = [(r['A'], r['B']) for r in rows]
    ratios = [F(r['B'], r['A']) for r in rows]
    R = max(ratios)/min(ratios)
    # Strict exact criterion R*(1-e)^2 > (1+e)^2; float only for display.
    comparisons = []
    for e in (F(0), F(1, 50), F(1, 20), F(1, 10)):
        intervals = [ratio_interval(v, e) for v in vectors]
        direct = disjoint(*intervals)
        certificate = R*(1-e)**2 - (1+e)**2
        assert direct == (certificate > 0)
        comparisons.append({'per_object_error': str(e),
                            'ratio_intervals': [[str(x) for x in i] for i in intervals],
                            'strictly_disjoint': direct,
                            'exact_separation_certificate': str(certificate)})
    # A known single total fixes only a different positive unit in each model.
    one_total = F(100)  # Explicitly hypothetical, not an archaeological observation.
    single_units = [str(one_total/F(v[0])) for v in vectors]
    assert all(feasible_unit_interval((v[0],), (one_total,), F(0)) for v in vectors)
    threshold = (sqrt(float(R))-1)/(sqrt(float(R))+1)
    write_json('results/numeral_calibration_design.json', {
        'scope': 'Conditional calibration design, not measured data or validation of either numerical interpretation.',
        'candidates': rows,
        'relative_error_definition': 'A shared positive unit u must satisfy q_i*(1-e) <= u*n_i <= q_i*(1+e) for every independently linked observed total q_i.',
        'single_hypothetical_total': {'q_A': str(one_total), 'candidate_units': single_units,
                                     'distinguishes_candidates_without_fixed_unit': False},
        'ratio_of_candidate_ratios': str(R),
        'disjoint_criterion': 'R*(1-e)^2 > (1+e)^2; equality permits touching intervals',
        'integer_polynomial_certificate': '403*e^2 - 6026*e + 403 > 0, for 0 <= e < 1',
        'critical_error_approximation': threshold,
        'error_sensitivity': comparisons,
        'essential_unverified_assumptions': [
            'A and B are intended numerical totals with the proposed grouping and operations.',
            'Sign identities and object crosswalks are correct; W899/source900 is not silently equated.',
            'The independently measured quantities are what the inscriptions represent.',
            'Both measured quantities use the same physical dimension and one common positive unit within each candidate.',
            'Object-specific uncertainty is honestly bounded; quantities are not merely surviving object masses.',
        ],
        'current_authenticated_commensurate_quantity_pairs': 0,
        'scope_limits': [
            'An ambiguous or lost sign adds discrete prediction uncertainty not included in e.',
            'Independent free units per object remove ratio discrimination.',
            'Overlapping intervals do not imply every possible observation is ambiguous.',
            'A future observation can reject both candidates; the candidates are not exhaustive historical systems.',
            'Even discriminating these candidates would not decipher the remaining inventory.',
        ],
        'input_sha256': {p: sha256(ROOT/p) for p in [source,
            'data/processed/numeral_equation_claims.json', 'docs/NUMERAL_EQUATIONS.md',
            'docs/NUMERAL_SCREEN.md', 'docs/NUMERAL_IMAGES.md']},
    })
    print(f'Conditional ratio design: {ratios}; critical error {threshold:.8%}; no new quantity anchor.')


if __name__ == '__main__':
    main()
