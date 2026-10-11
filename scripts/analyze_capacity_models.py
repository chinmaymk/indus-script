"""Conditional capacity/count fits; source tables remain provisionally transcribed.

The three geometry columns are alternatives for the SAME objects, not replicas.
Permutation ranks and leave-one-out fits are descriptive, not discovery tests.
"""
import itertools
import json
import math
from common import ROOT, sha256, write_json


def fit(counts, volumes):
    if len(counts) != len(volumes) or not counts:
        raise ValueError('Equal nonempty vectors required')
    if any(not math.isfinite(x) or x <= 0 for x in [*counts, *volumes]):
        raise ValueError('Positive finite counts and volumes required')
    unit = sum(n*v for n,v in zip(counts, volumes))/sum(n*n for n in counts)
    residuals = [v-unit*n for n,v in zip(counts,volumes)]
    return {'litres_per_stroke': unit, 'residuals_litres': residuals,
            'sse': sum(r*r for r in residuals),
            'relative_residuals': [r/v for r,v in zip(residuals,volumes)]}


def leave_one_out(counts, volumes):
    if len(counts) < 2 or len(counts) != len(volumes):
        raise ValueError('At least two paired observations required')
    rows = []
    for i,(n,v) in enumerate(zip(counts,volumes)):
        unit = fit(counts[:i]+counts[i+1:], volumes[:i]+volumes[i+1:])['litres_per_stroke']
        rows.append({'index':i,'training_unit':unit,'prediction_litres':n*unit,
                     'observed_model_litres':v,'relative_prediction_error':(n*unit-v)/v})
    return rows


def main():
    path=ROOT/'data/processed/capacity_table_followup.json'
    source=json.loads(path.read_text())
    visual=ROOT/'data/processed/capacity_primary_review.json'
    review=json.loads(visual.read_text())
    if sha256(ROOT/review['source']) != review['source_sha256']:
        raise ValueError('Primary photograph source hash changed')
    counts_by_id={r['cisi']:r['observed_strokes'] for r in review['vessels']}
    rows=source['table2']['rows']
    ids=[r['cisi'] for r in rows]
    counts=[counts_by_id[x] for x in ids]
    models={}
    for model in ['sphere','ellipsoid','profile']:
        values=[r.get(model, r.get(model+'_approximate')) for r in rows]
        fitted=fit(counts,values)
        permutations=[{'counts':list(p),'sse':fit(list(p),values)['sse']}
                      for p in itertools.permutations(counts)]
        models[model]={**fitted,'capacities_litres':values,
            'litres_per_stroke_each':[v/n for v,n in zip(values,counts)],
            'leave_one_out':leave_one_out(counts,values),
            'permutation_rank':1+sum(p['sse']<fitted['sse']-1e-9 for p in permutations),
            'all_six_permutations':permutations}
    leads={r['object']:r for r in source['other_specific_leads']}
    # Counts reported in Fuls Table3; unlike the Harappa counts these are not
    # independently authenticated here except K90's two visible rim strokes.
    external=[('H95-2661',4,leads['H95-2661']['computed_profile_capacity_litres']),
              ('MD-1374',6,leads['MD-1374']['computed_below_rim_litres']),
              ('K-90',2,leads['K-90']['computed_profile_capacity_litres'])]
    transfer=[]
    for name,n,v in external:
        predictions={}
        for model,result in models.items():
            p=n*result['litres_per_stroke']
            predictions[model]={'prediction_litres':p,'relative_prediction_error':(p-v)/v}
        count_notes={'H95-2661':'Four rim strokes reported in Fuls section3.2/Table3; later Kenoyer drawing review provisionally supports four, with three as sensitivity. Separate profile trace saved in h95_profile_volume.json; this row retains the Fuls88.3L value.',
                     'MD-1374':'Three vertical plus three slanted strokes counted equally, conditionally; original profile not inspected.',
                     'K-90':'Two rim strokes visually checked; 30cm bar length not authenticated.'}
        transfer.append({'object':name,'reported_count':n,'count_assumption':count_notes[name],
                         'reported_model_capacity_litres':v,
                         'litres_per_stroke':v/n,'predictions':predictions})
    write_json('results/capacity_model_audit.json',{
        'status':'Conditional on provisional public-text Table2 transcription and CISI-number identity',
        'input_hashes':{str(p.relative_to(ROOT)):sha256(p) for p in [path,visual]},
        'objects':ids,'stroke_counts':counts,'models':models,'transfer_without_refitting':transfer,
        'limits':['Three selected pots; geometry alternatives share measurements.',
                  'Leave-one-out does not undo prior source/hypothesis selection.',
                  'Permutation ranks are descriptive, not confirmatory p-values.',
                  'External vessels appeared in the same publication; not blind predictions.',
                  'Model disagreement is not a calibrated measurement confidence interval.',
                  'Excavation-number conflict unresolved; no measurements reassigned.',
                  'No phonetic value, universal volume unit, commodity or absolute stroke value established.']})
    print('Capacity analysis: 3 provisional objects, 3 alternative geometries, 3 transfer checks')


if __name__=='__main__':
    main()
