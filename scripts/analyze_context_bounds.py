"""Exact bounds from primary position and context marginals, not joint-data imputation.

See docs/CONTEXT_BOUNDS.md for the proof and limits. Fractions avoid threshold
rounding. These are deterministic constraints on the catalogue, not p-values.
"""
import csv
from fractions import Fraction
import json
from common import ROOT,sha256,write_csv,write_json
from extract_primary_table import validate_rows

POSITIONS=['solus','initial','medial','final']
PAIRS=[('M342','M343','final'),('M342','M344','final'),('M342','M345','final'),
       ('M087','M099','initial'),('M059','M065','initial')]

def probability(counts):
    if not counts or any(not isinstance(v,int) or v<0 for v in counts) or sum(counts)==0:
        raise ValueError('Expected nonnegative integer counts with positive total')
    return [Fraction(v,sum(counts)) for v in counts]

def total_variation(p,q):
    if len(p)!=len(q) or sum(p)!=1 or sum(q)!=1:
        raise ValueError('Probability distributions must have aligned categories and sum to one')
    return sum(abs(a-b) for a,b in zip(p,q))/2

def intersection_bounds(total,event_count,stratum_count):
    if not 0<=event_count<=total or not 0<=stratum_count<=total:
        raise ValueError('Invalid marginal counts')
    return max(0,event_count+stratum_count-total),min(event_count,stratum_count)

def validate_context(data,positions):
    seen=set()
    for row in data['rows']:
        key=(row['dimension'],row['sign'])
        if key in seen:
            raise ValueError('Duplicate context row')
        seen.add(key)
        codes=data['dimensions'][row['dimension']]['codes']
        counts=row['counts'];probability(counts)
        if len(counts)!=len(codes) or sum(counts)!=row['printed_total']:
            raise ValueError(f'Context row sum/width mismatch: {key}')
        if row['printed_total']!=positions[row['sign']]['total']:
            raise ValueError(f'Context total disagrees with Table I: {key}')

def main():
    data=json.loads((ROOT/'data/processed/primary_context_subset.json').read_text())
    if sha256(ROOT/data['source_pdf'])!=data['source_pdf_sha256']:
        raise ValueError('Context transcription source changed')
    with (ROOT/'data/processed/mahadevan_1977_table_i.csv').open() as f:
        rows=list(csv.DictReader(f))
    validate_rows(rows)
    positions={r['sign']:{k:int(r[k]) for k in POSITIONS+['total']} for r in rows}
    validate_context(data,positions)
    contexts={(r['dimension'],r['sign']):r for r in data['rows']}
    bounds=[];strata=[]
    for dimension,definition in data['dimensions'].items():
        for a,b,event in PAIRS:
            if (dimension,a) not in contexts or (dimension,b) not in contexts:
                continue
            ra,rb=contexts[dimension,a],contexts[dimension,b]
            pa,pb=positions[a],positions[b]
            context_tv=total_variation(probability(ra['counts']),probability(rb['counts']))
            position_tv=total_variation(probability([pa[f] for f in POSITIONS]),probability([pb[f] for f in POSITIONS]))
            event_gap=abs(Fraction(pa[event],pa['total'])-Fraction(pb[event],pb['total']))
            bounds.append({'dimension':dimension,'first':a,'second':b,'event':event,
                'context_total_variation':float(context_tv),'context_tv_exact':str(context_tv),
                'event_rate_difference':float(event_gap),'event_gap_exact':str(event_gap),
                'event_gap_exceeds_context_bound':event_gap>context_tv,
                'position_total_variation':float(position_tv),'position_tv_exact':str(position_tv),
                'position_gap_exceeds_context_bound':position_tv>context_tv,
                'same_within_context_position_rates_can_fit_exact_marginals':False if position_tv>context_tv else 'not decided by this necessary condition',
                'scope':'Exact empirical marginals; no causal, semantic or population-level significance claim'})
            for code,label,na,nb in zip(definition['codes'],definition['labels'],ra['counts'],rb['counts']):
                if not na or not nb:
                    continue
                alo,ahi=intersection_bounds(pa['total'],pa[event],na)
                blo,bhi=intersection_bounds(pb['total'],pb[event],nb)
                low=Fraction(alo,na)-Fraction(bhi,nb)
                high=Fraction(ahi,na)-Fraction(blo,nb)
                strata.append({'dimension':dimension,'context_code':code,'context_label':label,
                    'first':a,'second':b,'event':event,'first_context_tokens':na,'second_context_tokens':nb,
                    'first_event_count_min':alo,'first_event_count_max':ahi,
                    'second_event_count_min':blo,'second_event_count_max':bhi,
                    'first_event_rate_min':float(Fraction(alo,na)),'first_event_rate_max':float(Fraction(ahi,na)),
                    'second_event_rate_min':float(Fraction(blo,nb)),'second_event_rate_max':float(Fraction(bhi,nb)),
                    'first_minus_second_rate_min':float(low),'first_minus_second_rate_max':float(high),
                    'difference_min_exact':str(low),'difference_max_exact':str(high),
                    'interval_excludes_zero':low>0 or high<0})
    write_csv('results/primary_context_bounds.csv',bounds)
    write_csv('results/primary_within_context_bounds.csv',strata)
    write_json('results/primary_context_audit.json',{'transcribed_rows':len(contexts),
        'row_sums_and_table_I_totals_match':True,'comparisons':len(bounds),
        'comparisons_exceeding_context_tv_bound':sum(b['position_gap_exceeds_context_bound'] for b in bounds),
        'strata_with_guaranteed_event_rate_difference':[r for r in strata if r['interval_excludes_zero']],
        'missing_source_data':data['missing_source_data'],
        'caveats':['Single-pass transcription of a selected subset.',
          'Site and object type are tested separately, not jointly.',
          'The bounds do not assume independent occurrences; population inference would require sampling assumptions.',
          'Position-conditioned allography, object subtype, chronology and other unmeasured contexts remain possible.',
          'This tests exact shared empirical context rates; it is not a statistical rejection of shared population probabilities.']})
    for b in bounds:
        print(f"{b['dimension']} {b['first']}/{b['second']}: event gap {b['event_rate_difference']:.4f}, mixture bound {b['context_total_variation']:.4f}")

if __name__=='__main__':
    main()
