"""Compare independently transcribed overlapping objects through attributed sign sets.

Compatibility is weaker than equality: many-to-many catalogue links are permitted.
Never select an object-side match based on its agreement score.
"""
from collections import defaultdict,Counter
import json
import re
from common import ROOT,read_jsonl,write_csv,write_json

def main():
    features={f['id']:f for f in json.loads((ROOT/'data/processed/catalogue_features.json').read_text())}
    wells,parpola=defaultdict(list),defaultdict(list)
    for r in read_jsonl('data/processed/lipi_strict.jsonl'):
        wells[r['artifact']].append(r)
    for r in read_jsonl('data/processed/mayig_strict.jsonl'):
        parpola[re.sub(r'[A-Za-z]+$','',r['id'])].append(r)
    ledger=[]
    for artifact,ps in sorted(parpola.items()):
        ws=wells.get(artifact,[])
        row={'artifact':artifact,'status':'','parpola_sequence':'','wells_sequence':'',
             'file_order_compatible':'','reversed_compatible':'','mismatching_positions_1based':''}
        if len(ps)!=1 or len(ws)!=1:
            row['status']='missing_or_ambiguous_object_side_match'
        else:
            p,w=ps[0]['sequence'],ws[0]['sequence']
            row['parpola_sequence']=' '.join(p);row['wells_sequence']=' '.join(w)
            allowed=[set(features[x]['wells_graphemes']) for x in p]
            if len(p)!=len(w):
                row['status']='length_disagreement'
            elif not all(allowed):
                row['status']='incomplete_catalogue_correspondence'
            else:
                row['status']='compared'
                row['file_order_compatible']=all(x in st for x,st in zip(w,allowed))
                row['reversed_compatible']=all(x in st for x,st in zip(w[::-1],allowed))
                row['mismatching_positions_1based']=';'.join(str(i+1) for i,(x,st) in enumerate(zip(w,allowed)) if x not in st)
        ledger.append(row)
    write_csv('results/transcription_comparison.csv',ledger)
    compared=[r for r in ledger if r['status']=='compared']
    write_json('results/transcription_comparison.json',{
        'status_counts':dict(Counter(r['status'] for r in ledger)),
        'compared':len(compared),
        'file_order_compatible':sum(r['file_order_compatible'] for r in compared),
        'reversed_compatible':sum(r['reversed_compatible'] for r in compared),
        'note':'Mohenjo-daro convenience sample; catalogue-set compatibility does not validate allographs or original artifacts. Preserve all mismatches.'})

if __name__=='__main__':
    main()
