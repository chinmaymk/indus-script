"""Conditional identifiability checks, not estimates of Indus sign values.

The bangle interval is an unverified published reconstruction claim. The volume
example is synthetic. Neither is imported into the inscription corpus.
"""
from fractions import Fraction
import json
from common import ROOT, write_json


def integer_weights(counts, lower, upper):
    """All positive integer weights for two positive multiplicities in an interval."""
    x, y = counts
    if min(x, y) <= 0 or lower < 0 or upper < lower:
        raise ValueError('Require positive counts and an ordered nonnegative interval')
    return [(a, b) for a in range(1, upper // x + 1)
            for b in range(1, upper // y + 1) if lower <= x*a + y*b <= upper]


def fit_unit(counts, volumes):
    """Exact least-squares through origin, with positive proposed numerical values."""
    if len(counts) != len(volumes) or not counts or any(n <= 0 for n in counts):
        raise ValueError('Require matched nonempty arrays and positive values')
    return sum(Fraction(n)*Fraction(v) for n, v in zip(counts, volumes)) / sum(
        Fraction(n)**2 for n in counts)


def photo_scale(volume, shape_coefficient):
    """Scale when a fixed pixel geometry has V = coefficient * scale**3."""
    if min(volume, shape_coefficient) <= 0:
        raise ValueError('Volume and coefficient must be positive')
    return (volume / shape_coefficient)**(1/3)


def main():
    ledger = json.loads((ROOT/'data/processed/quantity_anchor_ledger.json').read_text())
    bangle = next(a for a in ledger['anchors'] if a['id'] == 'bangle_claim')
    counts = bangle['conditional_counts_long_short']
    lower, upper = bangle['claimed_reconstructed_count_interval']
    pairs = integer_weights(counts, lower, upper)
    # Synthetic data deliberately not represented as archaeological measurements.
    n, volumes = [3, 6, 7], [Fraction(120), Fraction(245), Fraction(280)]
    unit = fit_unit(n, volumes)
    rescaled = fit_unit([10*k for k in n], volumes)
    original_predictions = [unit*k for k in n]
    rescaled_predictions = [rescaled*10*k for k in n]
    assert original_predictions == rescaled_predictions
    write_json('results/quantity_anchor_audit.json', {
        'scope': 'Conditional calculations; no established Indus numerical values.',
        'bangle': {
            'source_status': bangle['status'],
            'counts_long_short': counts, 'interval': [lower, upper],
            'all_positive_integer_weights': [{'long':a,'short':b,
                'total':counts[0]*a+counts[1]*b} for a,b in pairs],
            'with_short_fixed_to_one': [a for a,b in pairs if b == 1],
            'with_long_greater_than_short': [[a,b] for a,b in pairs if a > b],
            'decimal_pair_compatible': [10,1] in [list(p) for p in pairs],
            'equal_unit_strokes_compatible': [1,1] in [list(p) for p in pairs],
            'uniquely_identifies_decimal': len(pairs) == 1 and pairs[0] == (10,1)},
        'synthetic_volume_symmetry': {'is_archaeological_data':False,
            'counts':n, 'volumes':[str(v) for v in volumes],
            'unit':str(unit), 'unit_after_tenfold_values':str(rescaled),
            'predictions_equal':original_predictions == rescaled_predictions},
        'unknown_photo_scale': {'is_archaeological_measurement':False,
            'scale_ratio_for_doubled_unit':photo_scale(2,1),
            'squared_radius_times_height_volume_ratio':photo_scale(2,1)**3},
        'new_established_sign_readings':0})
    print(f'Conditional bangle model: {len(pairs)} compatible positive integer weight pairs; no unique decimal value.')


if __name__ == '__main__':
    main()
