"""Exact conditional mass constraints; no local numeral is mapped to an M sign."""
from fractions import Fraction as F
import json
from common import ROOT, sha256, write_json


def encoded(q):
    return {'exact': str(q), 'decimal': float(q)}


def eliminate(first, second):
    """Eliminate u by positive scaling; retain coefficients and exact RHS."""
    a = {k: F(v) for k, v in first['coefficients'].items()}
    b = {k: F(v) for k, v in second['coefficients'].items()}
    scale = b['u'] / a['u']
    if scale <= 0 or second['relation'] != '=':
        raise ValueError('Requires positive scaling and an equality to subtract')
    c = {k: scale*a.get(k, F(0))-b.get(k, F(0)) for k in a.keys() | b.keys()}
    rhs = scale*F(first['rhs_g'])-F(second['rhs_g'])
    return scale, c, rhs


def reconstructed_bounds(tang, axe, p):
    """Assumes u+5i+4t < p*tang, 7u+6i=axe and t=i>0."""
    tang, axe, p = map(F, (tang, axe, p))
    rhs = 7*p*tang-axe
    if rhs <= 0:
        return {'positive_solution_possible': False, 'eliminated_rhs_g': encoded(rhs)}
    i_max = rhs/57
    u_min = (axe-6*i_max)/7
    return {'positive_solution_possible': True, 'eliminated_rhs_g': encoded(rhs),
            'i_upper_exclusive_g': encoded(i_max),
            'u_lower_exclusive_g': encoded(u_min),
            'u_over_i_lower_exclusive': encoded(u_min/i_max)}


def required_p(tang, axe, base):
    """Minimum original/tang ratio if t=i and u=base*i (no damage correction)."""
    tang, axe, base = map(F, (tang, axe, base))
    return axe*(base+9)/(tang*(7*base+6))


def three_object_constraint(tang, axe, six_i_mass):
    tang, axe, six_i_mass = map(F, (tang, axe, six_i_mass))
    i = six_i_mass/6
    u = (axe-six_i_mass)/7
    minimum = u+5*i  # t >= 0
    return {'i_g': encoded(i), 'u_g': encoded(u),
            'chisel_mass_lower_inclusive_g': encoded(minimum),
            'p_lower_inclusive': encoded(minimum/tang),
            'compatible_with_strict_p_2_6': minimum < F('2.6')*tang}


def signed_three_object_fit(tang, axe, six_i_mass):
    """Unique signed fit; a negative parameter is not by itself a rejected fit."""
    tang, axe, six_i_mass = map(F, (tang, axe, six_i_mass))
    if min(tang, axe, six_i_mass) <= 0:
        raise ValueError('Positive reported masses required')
    i = six_i_mass/6
    u = (axe-six_i_mass)/7
    t = (tang-u-5*i)/4
    residuals = [6*i-six_i_mass, 7*u+6*i-axe, u+5*i+4*t-tang]
    assert residuals == [0, 0, 0]
    return {
        'i_g': encoded(i), 'u_g': encoded(u), 't_g': encoded(t),
        'residuals_g': [encoded(v) for v in residuals],
        'all_nonnegative': min(i, u, t) >= 0,
        'negative_i_possible_under_small_axe_equation': i < 0,
        't_equals_i_compatible': t == i,
        'parameters': 3, 'equations': 3, 'independent_validation_equations': 0,
        'scope': 'Algebraic signed fit to assumed complete current-mass expressions; negative t is a fitted subtraction, not evidence of ancient arithmetic',
    }


def free_small_axe_residual(tang, axe, small_axe, chosen_i):
    """An explicitly fitted residual leaves one free parameter, not a new reading."""
    tang, axe, small_axe, i = map(F, (tang, axe, small_axe, chosen_i))
    u = (axe-6*i)/7
    t = (tang-u-5*i)/4
    r = small_axe-6*i
    residuals = [6*i+r-small_axe, 7*u+6*i-axe, u+5*i+4*t-tang]
    assert residuals == [0, 0, 0]
    return {'chosen_i_g': encoded(i), 'u_g': encoded(u), 't_g': encoded(t),
            'fitted_small_axe_other_signs_g': encoded(r),
            'residuals_g': [encoded(v) for v in residuals],
            'free_parameters_after_three_equations': 1,
            'scope': 'Counterexample with an invented aggregate residual for other signs; not observed mass or deciphered meaning'}


def audit(ledger):
    pair = ledger['mohenjo_pair']
    # These coefficients define the published hypothesis being audited.
    expected = [{'u':'1','i':'5','t':'4'}, {'u':'7','i':'6','t':'0'}]
    cases = {}
    for name, field in [('rounded','author_rounded_surviving_equations'),
                        ('reported_precision','precise_surviving_equations_for_optional_check')]:
        equations = pair[field]
        assert [e['coefficients'] for e in equations] == expected
        scale, c, rhs = eliminate(*equations)
        cases[name] = {'scale': encoded(scale), 'coefficients': {k: str(v) for k,v in c.items()},
                       'rhs_g': encoded(rhs),
                       'nonnegative_solution_impossible': all(v>=0 for v in c.values()) and rhs<0}
    rec = pair['reconstructed_chisel_equations_as_printed']
    assert [e['coefficients'] for e in rec] == expected
    assert rec[0]['relation']=='<' and F(rec[0]['rhs_g'])==F(rec[0]['p'])*165
    _, c, rhs = eliminate(*rec)
    sensitivity = []
    for precision, tang, axe in [('rounded','165','1910'),('reported_precision','165.343','1910.030')]:
        for p in ('2.6','2.8'):
            sensitivity.append({'mass_input': precision,'p': p, **reconstructed_bounds(tang,axe,p)})
    bases = [{'u_over_i': b, 't_equals_i': True,
              'required_p': encoded(required_p('165','1910',b)),
              'compatible_with_strict_p_2_6': required_p('165','1910',b)<F('2.6')}
             for b in (8,10,16)]
    kalibangan=[]
    for family in ledger['kalibangan_equation_families']:
        e1,e2=family['equations']
        i=F(e2['rhs_g'])/F(e2['coefficients']['i'])
        u=(F(e1['rhs_g'])-F(e1['coefficients']['i'])*i)/F(e1['coefficients']['u'])
        assert u==F(family['solutions_g']['u']) and i==F(family['solutions_g']['i'])
        kalibangan.append({'model':family['id'],'u_g':encoded(u),'i_g':encoded(i),
                          'u_over_i':encoded(u/i),'independent_validation_objects':0})
    rows=ledger['nine_object_table']['rows']
    third=next(r for r in rows if r['object']=='DK-7855')
    assert third['expression_literal']=='6i'
    return {'scope':'Conditional algebra of disputed readings and mass reconstructions; not a decipherment.',
            'surviving_mass_certificates':cases,
            'reconstruction_elimination':{'coefficients':{k:str(v) for k,v in c.items()},
                'rhs_exclusive_g':encoded(rhs),'normalized_t_coefficient':encoded(c['t']/c['i']),
                'printed_t_coefficient': '4/29', 'printed_coefficient_correct': c['t']/c['i']==F(4,29)},
            't_equals_i_sensitivity':sensitivity,'fixed_ratio_sensitivity':bases,
            'three_object_extension': {
                'assumption':'DK-7855 six strokes alone encode whole surviving axe; adjacent signs ignored. Each branch states its mass precision.',
                'rounded':three_object_constraint('165','1910',third['reported_surviving_mass_g']),
                'reported_precision':three_object_constraint('165.343','1910.030',third['reported_surviving_mass_g'])},
            'kalibangan_calibrations':kalibangan,
            'assumed_original_500g_variant':{'i_g':100,'u_g':10,'measured_K122_mass_g':476,
                'unmeasured_added_mass_g':24,'status':'Changes the mass assumption; not held-out confirmation'},
            'table_objects':len(rows),
            'objects_with_reported_mass':sum(r['reported_surviving_mass_g'] is not None for r in rows),
            'new_established_sign_values':0}


def main():
    path=ROOT/'data/processed/metal_tool_weight_anchors.json'
    ledger=json.loads(path.read_text())
    for item in [ledger['primary_pdf'],ledger['errata']['capture']]+[p['evidence'] for p in ledger['visually_checked_primary_pages']]:
        assert sha256(ROOT/item['path'])==item['sha256'], item['path']
    result=audit(ledger)
    original_path = ROOT/'data/processed/metal_original_records.json'
    original = json.loads(original_path.read_text())
    by_locator = {r['stable_primary_locator']: r for r in original['records']}
    masses = [by_locator[f'Plate CXXVI, no. {n}']['mass_grams_literal'] for n in (2, 5, 3)]
    for n in (2, 5, 3):
        pin = by_locator[f'Plate CXXVI, no. {n}']['mass_evidence']
        assert sha256(ROOT/pin['path']) == pin['sha256']
    result['three_object_extension']['original_metric'] = three_object_constraint(*masses)
    result['three_object_extension']['original_metric_inputs_g'] = dict(zip(('tang', 'large_axe', 'small_axe'), masses))
    result['three_object_extension']['original_metric_source_sha256'] = sha256(original_path)
    result['three_object_extension']['precision_note'] = 'Historical reported_precision used rounded262g for small axe; original_metric uses262.233g. Decimal strings do not establish balance accuracy.'
    result['signed_three_object_original_metric'] = signed_three_object_fit(*masses)
    result['signed_small_axe_free_residual_counterexample'] = free_small_axe_residual(*masses, '-30')
    result['input_ledger_sha256']=sha256(path)
    write_json('results/metal_weight_anchor_audit.json',result)
    print('Metal weights: 2 exact present-mass contradictions; corrected 28/29 coefficient; 0 established sign values.')


if __name__=='__main__':
    main()
