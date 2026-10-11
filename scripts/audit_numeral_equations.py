"""Solve two published conditional equations completely, without fixing a base.

This audits an interpretation; it does not establish that inscriptions are equations.
The divisor argument and its assumptions are in docs/NUMERAL_EQUATIONS.md.
"""
import csv
import json
from math import isqrt
from common import ROOT, sha256, write_json, write_csv


def positive_divisors(n):
    if n <= 0:
        raise ValueError('Require a positive integer')
    return sorted({d for k in range(1,isqrt(n)+1) if n % k == 0 for d in (k,n//k)})


def residuals(L,S,v):
    return (3*L+v-2*L-2*S, v*L+1-7*S-5)


def all_positive_solutions():
    # d=2L-7 divides 65, since 4(L^2+4)=d(2L+7)+65.
    solutions=[]
    for d in positive_divisors(65):
        if (d+7) % 2:
            continue
        L=(d+7)//2
        if (L*L+4) % d:
            continue
        S=(L*L+4)//d
        v=2*S-L
        if min(L,S,v)>0:
            assert residuals(L,S,v)==(0,0)
            solutions.append({'L':L,'S':S,'v':v})
    return solutions


def source_records():
    """Retain literal rows for auditing; proposed readings never imported."""
    selected=[]
    fields=['id','cisi','excavation-idno','type','dir.','complete','text']
    with (ROOT/'data/raw/lipi_inscriptions.csv').open() as f:
        for row in csv.DictReader(f):
            if row['cisi'] in ('M-331','M-1383') or row['id'].split('.')[0]=='3786':
                selected.append({k:row[k] for k in fields})
    return selected


def main():
    claims_path=ROOT/'data/processed/numeral_equation_claims.json'
    claims=json.loads(claims_path.read_text())
    # Fail rather than silently solving a different edited input specification.
    assert [r['reduced'] for r in claims['equations']]==[
        'v = 2*S-L','v*L+1 = 7*S+5']
    solutions=all_positive_solutions()
    bounds=claims['conditional_screens']['digit_inventory_bounds']
    screened=[s for s in solutions if s['L']>=bounds['L_min'] and s['S']>=bounds['S_min']]
    interval=claims['conditional_screens']['bangle_interval']
    with_bangles=[s for s in screened if interval['L_min']<=s['L']<=interval['L_max']]
    records=source_records()
    write_csv('results/numeral_source_records.csv',records)
    write_json('results/numeral_equation_audit.json',{
        'scope':'Exact conditional algebra, not a decipherment or independent artifact replication',
        'claims_sha256':sha256(claims_path),
        'complete_positive_integer_solutions':solutions,
        'completeness_certificate':{'divisor_constant':65,'positive_divisors':positive_divisors(65),
            'identity':'4*(L*L+4) = (2*L-7)*(2*L+7)+65',
            'reason_positive_divisor':'S>0 and L^2+4>0 force 2L-7>0'},
        'after_conditional_digit_bounds':screened,
        'after_additional_bangle_interval':with_bangles,
        'minimum_L_candidate':min(screened,key=lambda s:s['L']),
        'minimum_L_is_selection_preference_not_identification':True,
        'equation_one_parity_counterexample':{'L':10,'S':9,'v':8,
            'satisfies_equation_one':residuals(10,9,8)[0]==0,
            'satisfies_both':residuals(10,9,8)==(0,0)},
        'literal_source_rows':len(records),
        'crosswalk_warnings':[
            'The local 3786.1 record identifies M-1540, with one listed face; article ID alone cannot authenticate Figure 16.',
            'Local M-331 uses W899 on two faces; source proposal uses sign 900. No equality is assumed.',
            'M-331 face ordinals differ, but reviewed CISI images map local rows to A, B, F, D; article prose appears to use A, B, D, F. See docs/NUMERAL_IMAGES.md.'],
        'new_established_sign_values':0})
    print(f'{len(solutions)} positive integer solutions; {len(screened)} after digit bounds; '
          f'{len(with_bangles)} after disputed bangle interval.')


if __name__=='__main__':
    main()
