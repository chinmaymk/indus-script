"""A conditional whole-sign mass bound, without assigning Indus numeral values."""
from fractions import Fraction as F
import json
from common import ROOT, sha256, write_json


def exact(value):
    return {'fraction': str(value), 'decimal': float(value)}


def certificate(axe_mass, tang_mass, factor):
    q, tang, p = map(F, (axe_mass, tang_mass, factor))
    if q <= 0 or tang <= 0 or p <= 0:
        raise ValueError('Positive masses and reconstruction factor required')
    cap = p*tang
    return {
        'assumed_M106_mass_component_g': exact(q),
        'tang_surviving_mass_g': exact(tang),
        'minimum_tang_expression_mass_g': exact(q),
        'current_mass_shortfall_g': exact(q-tang),
        'exact_surviving_mass_model_inconsistent': tang < q,
        'hypothetical_reconstruction_factor': exact(p),
        'strict_reconstruction_cap_g': exact(cap),
        'strict_cap_shortfall_g': exact(q-cap),
        'strict_cap_model_inconsistent': q >= cap,
        'minimum_original_over_surviving_factor': exact(q/tang),
        'minimum_missing_fraction_of_original_if_model_holds': exact(max(F(0), 1-tang/q)),
        'proof': 'M_K122=q; M_tang=q+r with r>=0. Hence M_tang>=q. Exact observed mass below q, or an assumed strict upper cap <=q, contradicts this model.',
    }


def main():
    identity_path = 'data/processed/bronze2923_identity_review.json'
    bridge_path = 'data/processed/tool_sign_bridge_review.json'
    identity = json.loads((ROOT/identity_path).read_text())
    bridge = json.loads((ROOT/bridge_path).read_text())
    for review in [identity, bridge]:
        for item in review['evidence_files']:
            p = ROOT/item['path']
            assert p.stat().st_size == item['bytes'] and sha256(p) == item['sha256'], item['path']
    byref = {r['m77_reference']: r for r in bridge['objects']}
    assert byref['8301']['normalized_tokens'] == ['M106']
    assert byref['2923']['normalized_tokens'].count('M106') == 1
    assert byref['2923']['residual_tokens'] == ['M387', 'M015']
    mass_path = 'data/processed/metal_original_records.json'
    mass_review = json.loads((ROOT/mass_path).read_text())
    tang = next(r for r in mass_review['records'] if r['stable_primary_locator'] == 'Plate CXXVI, no. 2')
    paper_path = 'data/processed/metal_tool_weight_anchors.json'
    paper = json.loads((ROOT/paper_path).read_text())
    axe = next(r for r in paper['nine_object_table']['rows'] if r['object'] == 'K-122')
    assert axe['expression_literal'] == '5i'
    result = {
        'scope': 'Conditional invariant whole-sign mass hypothesis, not a sign reading or a new mass observation',
        'identity_review': identity_path, 'graphical_bridge_review': bridge_path,
        'certificate': certificate(str(axe['reported_surviving_mass_g']), tang['mass_grams_literal'], '2.6'),
        'assumptions': json.loads((ROOT/'data/processed/tool_sign_mass_protocol.json').read_text()),
        'new_independent_mass_observations': 0,
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'limits': [
            'An invariant numeral value can coexist with different units; this test concerns invariant mass contribution',
            'Complete ancient tang mass is unmeasured; its surviving mass is not an original-mass observation',
            'The factor2.6 is a disputed reconstruction hypothesis, not authenticated conservation evidence',
            'Other signs or operations may change the interpretation; no global arithmetic grammar is established',
            'Original plate orientations are not preserved by treating normalized M104 as a universal t symbol',
        ],
    }
    paths = [identity_path, bridge_path, mass_path, paper_path,
             'data/processed/tool_sign_mass_protocol.json']
    result['input_sha256'] = {p: sha256(ROOT/p) for p in paths}
    write_json('results/tool_sign_mass_audit.json', result)
    print(json.dumps(result['certificate'], indent=2))


if __name__ == '__main__':
    main()
