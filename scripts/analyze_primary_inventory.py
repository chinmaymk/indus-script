"""All-sign descriptive constraints directly from Mahadevan's printed Table I.

No W/P crosswalk, translation, language hypothesis, or deduplication is involved.
Position refers to a line, using Mahadevan's reading-order convention.
"""
from collections import Counter
import csv
import json
from common import ROOT,write_csv,write_json
from extract_primary_table import validate_rows

POSITIONS=['solus','initial','medial','final']

def describe(counts):
    n=counts['total']
    if n<10:
        return 'rare; no stable positional role assigned'
    for field,threshold in [('solus',.6),('initial',.6),('final',.6),('medial',.8)]:
        if counts[field]/n>=threshold:
            return field+'-heavy (descriptive threshold)'
    return 'mixed positions'

def main():
    audit=json.loads((ROOT/'results/primary_table_audit.json').read_text())
    if (audit['rows']!=417 or audit['unresolved_or_sum_disagreement_signs']
        or not audit['column_sums_match'] or not audit['all_bands_match']):
        raise SystemExit('Primary transcription does not pass its source checks; no profiles generated.')
    rows=list(csv.DictReader((ROOT/'data/processed/mahadevan_1977_table_i.csv').open()))
    validate_rows(rows)
    profiles=[]
    for r in rows:
        counts={f:int(r[f]) for f in POSITIONS+['total']}
        profiles.append({'sign':r['sign'],**counts,
          **{f+'_fraction':counts[f]/counts['total'] for f in POSITIONS},
          'distributional_description':describe(counts),
          'primary_pdf_page':int(r['pdf_page']),'primary_printed_page':int(r['printed_page']),
          'unit':'sign occurrence in line of text, including repeated inscriptions',
          'meaning':'undetermined','sound':'undetermined',
          'caveat':'Historical catalogue counts; descriptive role is not a translation or significance claim.'})
    write_csv('results/primary_sign_profiles_417.csv',profiles)
    bysign={r['sign']:r for r in profiles}
    contrasts=[]
    for first,second,reason in [('M342','M343','jar / jar with one inner stroke'),
       ('M342','M344','jar / jar with two inner strokes'),
       ('M342','M345','jar / jar with three inner strokes'),
       ('M087','M099','two tall strokes / two short top-aligned strokes'),
       ('M059','M065','fish-like base / fish-like form with overhead caret')]:
        a,b=bysign[first],bysign[second]
        contrasts.append({'first':first,'second':second,'visual_comparison':reason,
          'first_total':a['total'],'second_total':b['total'],
          'first_initial_fraction':a['initial_fraction'],'second_initial_fraction':b['initial_fraction'],
          'first_medial_fraction':a['medial_fraction'],'second_medial_fraction':b['medial_fraction'],
          'first_final_fraction':a['final_fraction'],'second_final_fraction':b['final_fraction'],
          'conclusion':'Distribution differs. Distinct functions, context-conditioned allography, or sample confounding remain possible.'})
    write_csv('results/primary_shape_contrasts.csv',contrasts)
    summary={'signs':len(profiles),'tokens':sum(r['total'] for r in profiles),
       'hapax_signs':sum(r['total']==1 for r in profiles),
       'signs_with_fewer_than_10_occurrences':sum(r['total']<10 for r in profiles),
       'position_type_counts':{f:sum(r[f]>0 for r in profiles) for f in POSITIONS},
       'printed_position_type_counts':dict(zip(POSITIONS,[88,290,286,173])),
       'description_counts':dict(Counter(r['distributional_description'] for r in profiles)),
       'tokens_top_67':sum(sorted((r['total'] for r in profiles),reverse=True)[:67]),
       'jar_primary_counts':{f:bysign['M342'][f] for f in POSITIONS+['total']},
       'jar_line_end_only_counteroccurrences':bysign['M342']['initial']+bysign['M342']['medial'],
       'notes':['Solus is a separate category; a standalone sign can be both first and last, so it is not counted as a line-end counterexample.',
          'No historical-semantic or phonetic values follow from these counts.',
          'No crosswalk is required for the M-number positional profiles.']}
    write_json('results/primary_inventory_findings.json',summary)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
