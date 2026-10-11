"""Audit source distinctions and exact conditional limits of normalized stroke codes."""
from fractions import Fraction as F
import json
import re
from common import ROOT, sha256, write_json


def local_and_total_fit(i, t):
    """Total agreement must never be mistaken for occurrence-level agreement."""
    i, t = F(i), F(t)
    if i <= 0 or t <= 0:
        raise ValueError('Positive hypothetical units required')
    v = 2 * (i + t)
    return {
        'i': str(i), 't': str(t), 'v104_matching_total': str(v),
        'oriented_total': str(4*i + 4*t), 'normalized_total': str(2*v),
        'occurrence_level_equal_value_possible': i == t,
        'total_only_equal_value_possible': True,
        'vertical_group_residual': str(v-4*i),
        'horizontal_group_residual': str(v-4*t),
    }


def component_predictions(coefficients, t):
    """Replace each nonzero proposed t component with ONE fixed component c."""
    t = F(t)
    if t < 0 or any(k < 0 for k in coefficients):
        raise ValueError('Nonnegative counts and unit required')
    c = 4*t
    tally = [k*t for k in coefficients]
    whole = [c if k else F(0) for k in coefficients]
    return {
        't': str(t), 'c': str(c),
        'tally_contributions': list(map(str, tally)),
        'whole_component_contributions': list(map(str, whole)),
        'same_predictions': tally == whole,
    }


def main():
    paths = {
        'original': 'data/processed/stroke_orientation_tools_review.json',
        'catalogue': 'data/processed/orientation_corpus_coverage_review.json',
        'later_table': 'data/processed/metal_tool_weight_anchors.json',
        'protocol': 'data/processed/stroke_orientation_protocol.json',
        'attribution': 'data/processed/pettersson_orientation_attribution_review.json',
    }
    data = {k: json.loads((ROOT/p).read_text()) for k, p in paths.items()}
    for name in ('original', 'catalogue', 'attribution'):
        for pin in data[name]['evidence_files']:
            p = ROOT/pin['path']
            assert p.stat().st_size == pin['bytes'] and sha256(p) == pin['sha256'], pin['path']
    catalogue = {r['excavation_number']: r for r in data['catalogue']['rows']}
    assert catalogue['DK7800']['normalized_tokens'] == ['M104', 'M104']
    assert catalogue['DK7800']['actual_direction_code'] == 5
    assert catalogue['DK7857']['normalized_tokens'] == ['M104', 'M110']
    objects = []
    for row in data['original']['rows']:
        cat = catalogue[row['field_number']]
        objects.append({
            'reference': cat['m77_reference'], 'field_number': row['field_number'],
            'normalized_tokens': cat['normalized_tokens'],
            'direction_code': cat['actual_direction_code'],
            'direction_definition': cat['actual_direction_definition'],
            'primary_text_counts': row['primary_text_counts'],
            'drawn_mark_groups': row['drawn_mark_groups'],
            'photo_reading': row['photo_reading'],
            'later_notation_status': row['comparison_with_later_notation'],
            'per_token_orientation_assignment': None,
            'scope': 'Object-level source comparison; no universal reading or ancient token order inferred',
        })
    selected = []
    for row in data['later_table']['nine_object_table']['rows']:
        matches = re.findall(r'(\d+)\s*t\b', row['expression_literal'])
        assert len(matches) <= 1
        selected.append({'object': row['object'], 'expression': row['expression_literal'],
                         't_coefficient': int(matches[0]) if matches else 0})
    coefficients = [r['t_coefficient'] for r in selected]
    assert {k for k in coefficients if k} == {4}
    result = {
        'scope': data['protocol']['scope'], 'objects': objects,
        'local_proof': 'v104=4i and v104=4t imply 4(i-t)=0, hence i=t. Conversely i=t permits v104=4i.',
        'total_only_control': local_and_total_fit('8', '1'),
        'equal_units_boundary': local_and_total_fit('1', '1'),
        'selected_later_expressions': selected,
        'fixed_component_proof': 'For every selected coefficient k in {0,4}, kt = 1[k>0]c under c=4t. This map is bijective on nonnegative real units. Other terms unchanged, all additive predictions agree.',
        'fixed_component_example': component_predictions(coefficients, '3/7'),
        'sensitivity_counterexample': component_predictions([4, 3], '3/7'),
        'fixed_component_limits': 'Conditional on later notation; DK7857 tilted-row notation is compatible with its drawing; its numerical meaning remains unverified. Two t-free objects also have questioned readings. No mass fitting or semantic evidence supplied by this reparameterization.',
        'new_mass_observations': 0, 'new_recovered_lines': 0,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'protocol': data['protocol'],
        'input_sha256': {p: sha256(ROOT/p) for p in paths.values()},
    }
    write_json('results/stroke_orientation_audit.json', result)
    print(json.dumps({k: result[k] for k in ('local_proof', 'total_only_control', 'fixed_component_proof')}, indent=2))


if __name__ == '__main__':
    main()
