"""Prove infinite split-value families; do not infer different ancient values."""
import json
from common import ROOT, sha256, write_json


def evaluate(coefficients, t):
    return sum(c*t**i for i,c in enumerate(coefficients))


def add(*polynomials):
    out = [0]*max(map(len, polynomials))
    for p in polynomials:
        for i,c in enumerate(p): out[i] += c
    while len(out)>1 and out[-1] == 0: out.pop()
    return out


def scale(p, n): return [n*c for c in p]


def multiply(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j] += a*b
    while len(out)>1 and out[-1] == 0: out.pop()
    return out


FAMILIES = [
    {'name':'vB_four', 't_min':2, 'L':[1,7], 'S':[0,4], 'vA':[-1,1], 'vB':[4], 'shared_value_t':5},
    {'name':'vB_six', 't_min':1, 'L':[3,7], 'S':[2,6], 'vA':[1,5], 'vB':[6], 'shared_value_t':1},
]


def main():
    rows = []
    for spec in FAMILIES:
        L,S,a,b = [spec[k] for k in ('L','S','vA','vB')]
        first = add(L, a, scale(S,-2))
        second = add(multiply(b,L), scale(S,-7), [-4])
        assert first == second == [0]
        bounds = {'L_minus_10':add(L,[-10]), 'S_minus_8':add(S,[-8]),
                  'vA_minus_1':add(a,[-1]), 'vB_minus_1':add(b,[-1]),
                  'L_minus_vA_minus_1':add(L,scale(a,-1),[-1]),
                  'S_minus_vA_minus_1':add(S,scale(a,-1),[-1]),
                  'L_minus_vB_minus_1':add(L,scale(b,-1),[-1]),
                  'S_minus_vB_minus_1':add(S,scale(b,-1),[-1])}
        # Each affine bound is nonnegative at t_min and never decreases.
        for name,p in bounds.items():
            assert len(p)<=2 and (len(p)==1 or p[1]>=0), name
            assert evaluate(p,spec['t_min'])>=0, name
        equality = add(a,scale(b,-1))
        assert len(equality)==2 and equality[1]!=0
        assert evaluate(equality,spec['shared_value_t'])==0
        # L grows strictly with t, proving infinitely many distinct tuples.
        assert L[1]>0
        examples = []
        for t in sorted({spec['t_min'],spec['t_min']+1,spec['shared_value_t'],1000000}):
            example={'t':t, **{k:evaluate(spec[k],t) for k in ('L','S','vA','vB')}}
            example['shared_value']=example['vA']==example['vB']
            examples.append(example)
        rows.append({'parameterization':spec,'equation_residual_polynomials':[first,second],
                     'bound_polynomials_nonnegative_on_domain':bounds,
                     'vA_minus_vB_polynomial':equality,'examples':examples})
    source='results/numeral_equation_audit.json'
    shared=json.loads((ROOT/source).read_text())['after_conditional_digit_bounds']
    intersections=[{k:evaluate(s[k],s['shared_value_t']) for k in ('L','S')} |
                   {'v':evaluate(s['vA'],s['shared_value_t'])} for s in FAMILIES]
    assert sorted(intersections,key=lambda x:x['L']) == shared
    write_json('results/numeral_identity_sensitivity.json', {
        'scope':'Sensitivity to relaxing one shared-value assumption; not a proposed reading or proof the signs differ.',
        'split_equations':['3L+vA=2L+2S','vB*L+1=7S+5'],
        'bounds':['integer L>=10','integer S>=8','0<vA<min(L,S)','0<vB<min(L,S)'],
        'coefficient_order':'constant term first', 'families':rows,
        'infinite_solution_certificate':'In each family t ranges over infinitely many integers; affine bounds are nonnegative at t_min and nondecreasing; both residual polynomials vanish identically; L strictly increases.',
        'shared_value_intersections':intersections,
        'exhaustive_parameterization_claimed':False,
        'new_ancient_values_established':0,
        'limitations':[
            'Different modern catalogue codes do not prove different ancient signs or numerical values.',
            'Matching ancient shapes would not by itself prove context-independent numerical value.',
            'The published proposal may intentionally use one value; this calculation does not misstate its algebra.',
            'The prior two-candidate calibration result remains valid within its explicit shared-value model.',
            'The two exhibited families demonstrate infinitude; they do not enumerate every split-value solution.',
        ],
        'input_sha256':{p:sha256(ROOT/p) for p in [source,'data/processed/numeral_equation_claims.json',
            'data/processed/m331_visual_evidence.json','docs/NUMERAL_IMAGES.md','results/numeral_calibration_design.json']},
    })
    print('Split-value sensitivity: two exact infinite integer families, both shared-value candidates recovered as intersections.')


if __name__=='__main__': main()
