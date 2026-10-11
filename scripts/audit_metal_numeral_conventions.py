"""Constructive non-identifiability of the nine proposed metal-tool expressions.

Models assign abstract arithmetic values, not meanings, sounds, M sign IDs or
grams. Mass calibration is a separate explicitly conditional experiment.
"""
from fractions import Fraction as F
import json
from common import ROOT, sha256, write_json
from audit_metal_weight_anchors import encoded

ORDER=('t','i','u','x')
# Transcriptions of the analytical expressions, not fresh artifact readings.
CASES=[
 ('C-39','2x 3u (?)',{'x':2,'u':3}),
 ('C-40','3u 5(?) i',{'u':3,'i':5}),
 ('DK-7800','4i 4t',{'i':4,'t':4}),
 ('DK-7857','7i 4t',{'i':7,'t':4}),
 ('DK-7855','6i',{'i':6}),
 ('DK-7856','1u 5i 4t',{'u':1,'i':5,'t':4}),
 ('DK-7835','7u 6i',{'u':7,'i':6}),
 ('K-121','1u (or ???)',{'u':1}),
 ('K-122','5i',{'i':5})]
ALTERNATIVES=[('K-121:2u',{'u':2}),('K-121:u+2i',{'u':1,'i':2})]


def value(coefficients, units):
    return sum((F(n)*units[k] for k,n in coefficients.items()),F(0))


def canonical(coefficients, units):
    """Integer successive ratios and no lower coefficient reaching its carry.

    The highest denomination may repeat without bound; an unobserved higher
    denomination is not invented. This is a tested convention, not a fact.
    """
    for lower,upper in zip(ORDER,ORDER[1:]):
        ratio=units[upper]/units[lower]
        if ratio.denominator!=1 or ratio<2 or coefficients.get(lower,0)>=ratio:
            return False
    return True


def uniform_units(radix):
    if not isinstance(radix,int) or radix<2:
        raise ValueError('An integer radix >=2 is required')
    return {k:F(radix**j) for j,k in enumerate(ORDER)}


def model(name,units):
    cases=[(o,c) for o,_,c in CASES]+ALTERNATIVES
    return {'name':name,'units':{k:encoded(v) for k,v in units.items()},
            'half_unit_equation_4t_equals_i_over_2':4*units['t']==units['i']/2,
            'cases':[{'object_or_alternative':o,'coefficients':c,
                      'abstract_value':encoded(value(c,units)),
                      'canonical_under_stated_convention':canonical(c,units)} for o,c in cases]}


def pair_calibration(b,c,tang=F(165),axe=F(1910)):
    """b=u/i, c=i/t; axe fixes scale, original-chisel mass is a prediction."""
    b,c,tang,axe=map(F,(b,c,tang,axe))
    i=axe/(7*b+6)
    u,t=b*i,i/c
    chisel=u+5*i+4*t
    return {'u_over_i':encoded(b),'i_over_t':encoded(c),'i_g':encoded(i),
            'chisel_g':encoded(chisel),'required_whole_to_tang_ratio':encoded(chisel/tang),
            'fits_hypothetical_strict_2_6_cap':chisel<F('2.6')*tang,
            'small_axe_6i_prediction_g':encoded(6*i)}


def axes_constraint(small,large,minimum_ratio=8):
    small,large,minimum_ratio=map(F,(small,large,minimum_ratio))
    i=small/6; u=(large-small)/7
    minimum_large=(7*minimum_ratio+6)*i
    return {'observed_large_over_small':encoded(large/small),
            'calibrated_u_over_i':encoded(u/i),
            'minimum_u_over_i_assumed':encoded(minimum_ratio),
            'minimum_large_mass_g':encoded(minimum_large),
            'large_minus_minimum_g':encoded(large-minimum_large),
            'satisfies_minimum_ratio_bound':large>=minimum_large,
            'ratio_is_integer':(u/i).denominator==1,
            'compatible':large>=minimum_large and (u/i).denominator==1}


def unrestricted_loss_fit(units,masses):
    """A deliberately unfalsifiable fit when each original mass may grow freely."""
    coefficients={o:c for o,_,c in CASES}
    quantities={o:value(coefficients[o],units) for o in masses}
    scale=max(F(masses[o])/quantities[o] for o in masses)
    return {'scale_g_per_abstract_unit':encoded(scale),
            'objects':[{'object':o,'surviving_mass_g':encoded(F(m)),
                        'invented_original_mass_g':encoded(scale*quantities[o]),
                        'unmeasured_loss_g':encoded(scale*quantities[o]-F(m))}
                       for o,m in masses.items()],
            'status':'Constructive overfitting demonstration; not an archaeological damage estimate. Chisel geometry bound is not imposed.'}


def main():
    ledger_path=ROOT/'data/processed/metal_tool_weight_anchors.json'
    ledger=json.loads(ledger_path.read_text())
    rows=ledger['nine_object_table']['rows']
    assert [(r['object'],r['expression_literal']) for r in rows]==[(o,s) for o,s,_ in CASES]
    models=[model('uniform_'+str(r),uniform_units(r)) for r in (8,9,10,12)]
    models.append(model('mixed_8_10_10',{'t':F(1),'i':F(8),'u':F(80),'x':F(800)}))
    assert all(c['canonical_under_stated_convention'] for m in models for c in m['cases'])
    maximum={k:max(c.get(k,0) for _,_,c in CASES) for k in ORDER}
    original_path=ROOT/'data/processed/metal_original_records.json'
    original=json.loads(original_path.read_text())
    byplate={r['stable_primary_locator']:r for r in original['records']}
    small=byplate['Plate CXXVI, no. 3']['mass_grams_literal']
    large=byplate['Plate CXXVI, no. 5']['mass_grams_literal']
    for source in original['raw_sources']:
        assert sha256(ROOT/source['path'])==source['sha256'],source['path']
    evidence_path=ROOT/'data/processed/metal_numeral_convention_review.json'
    review=json.loads(evidence_path.read_text())
    for source in review['evidence']:
        assert sha256(ROOT/source['path'])==source['sha256'],source['path']
    plate_path=ROOT/'data/processed/metal_plate_audit.json'
    plate=json.loads(plate_path.read_text())
    plate_counts=[]
    for record in plate['records']:
        for source in (record['crop'],record['source']):
            assert sha256(ROOT/source['path'])==source['sha256'],source['path']
        group=record['target_group']
        plate_counts.append({'item':record['item'],'upright_strokes':group['upright_strokes'],
                             'transverse_strokes':group['transverse_strokes'],'arches':group['arches']})
    assert plate_counts==[
        {'item':'2','upright_strokes':5,'transverse_strokes':4,'arches':1},
        {'item':'3','upright_strokes':6,'transverse_strokes':0,'arches':0},
        {'item':'5','upright_strokes':6,'transverse_strokes':0,'arches':7}]
    write_json('results/metal_numeral_conventions.json',{
        'scope':'Countermodels to unique base inference for proposed expression counts; not translations or verified numeral values.',
        'source_ledger_sha256':sha256(ledger_path),'original_ledger_sha256':sha256(original_path),
        'review_sha256':sha256(evidence_path),'distinct_objects':len(CASES),
        'primary_plate_review_sha256':sha256(plate_path),'published_drawing_counts':plate_counts,
        'additional_reading_alternatives':len(ALTERNATIVES),'maximum_coefficients':maximum,
        'constructive_models':models,
        'complete_uniform_canonical_family':{
            'integer_radices':'all R >=8','proof':'All lower coefficients are at most7; seven occurs for i and u. For t=1,i=R,u=R^2,x=R^3, canonical carrying is equivalent to every lower coefficient<R. Thus exactly all integersR>=8 fit; there is no finite upper bound.',
            'mass_pair_also_fits_for_all_R_ge_8':'Required ratio p=M*(R+5+4/R)/(m*(7R+6)) decreases forR>0: derivative sign is -(29R^2+56R+24). AtR=8 it is<2.6 for roundedM1910,m165. This uses the hypothetical original-chisel bound, not observed original mass.'},
        'pair_calibrations_rounded':[pair_calibration(r,r) for r in (8,9,10,12)]+[pair_calibration(10,8)],
        'two_axes_primary_mass_constraint':axes_constraint(small,large),
        'two_axes_only_canonical_constraint':axes_constraint(small,large,7),
        'two_axes_rounded_mass_constraint':axes_constraint('262','1910'),
        'mass_constraint_scope':'Requires shared units, the proposed complete expressions6i and7u+6i, exact surviving masses, and u/i>=8 from canonical integer carrying. No chisel reconstruction required. Corrosion, missing signs or another denotation change the model.',
        'two_axes_only_scope':'Even without the other seven objects, six i signs in7u+6i require integer u/i>=7 under canonical carrying. These two masses also fail that weaker bound.',
        'free_loss_counterexamples':{str(r):unrestricted_loss_fit(uniform_units(r),{
            'DK-7856':byplate['Plate CXXVI, no. 2']['mass_grams_literal'],
            'DK-7855':small,'DK-7835':large,'K-121':'210','K-122':'476'}) for r in (8,10)},
        'free_loss_completeness_proof':'For any positive abstract quantities q_j and surviving masses m_j, choose scale s=max_j(m_j/q_j). Then losses L_j=s*q_j-m_j>=0 reproduce every mass. Thus completely unconstrained per-object loss cannot identify the unit system.',
        'new_established_sign_values':0})
    print('Numeral conventions: all integer radices>=8 fit proposed counts; mixed units also fit; two surviving axe masses fail shared canonical-unit model.')


if __name__=='__main__':
    main()
