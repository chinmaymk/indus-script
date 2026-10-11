"""Retrospective preservation sensitivity of candidate mapping compatibility."""
import csv
import json
from collections import Counter
from common import ROOT, sha256, write_json

def pair_fits(pair,model):
    return all(model[p['w']]==p['m'] for p in pair['target_assignments'])

def row_fits(pairs,model):
    return any(pair_fits(pair,model) for pair in pairs)

def main():
    paths=['data/processed/pincer_preservation_protocol.json',
           'results/pincer_context_screen.json','data/raw/lipi_inscriptions.csv',
           'data/processed/ending_india_review.json',
           'data/processed/m897_primary_review.json','data/processed/m897_mapping_review.json']
    protocol=json.loads((ROOT/paths[0]).read_text());screen=json.loads((ROOT/paths[1]).read_text())
    for source in paths[4:]:
        for pin in json.loads((ROOT/source).read_text())['evidence_files']:
            assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
            assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
    primary_corner_loss={r['cisi']:r.get('gross_text_bearing_corner_loss')
                         for r in json.loads((ROOT/paths[3]).read_text())['objects']}
    with (ROOT/paths[2]).open() as f:
        raw={r['id']:{k:r[k] for k in ['id','cisi','preservation','complete','type','excavation-idno']}
             for r in csv.DictReader(f)}
    pairs={p['pair_id']:p for p in screen['candidate_pairs']}
    rows=[]
    for r in screen['selected_rows']:
        seq=r['lipi_row']['sequence'];rs=raw[r['lipi_row']['id']]
        candidates=[pairs[p] for p in r['candidate_pair_ids']]
        rows.append({'source':rs,'sequence':seq,'candidate_pair_ids':r['candidate_pair_ids'],
                     'previous_primary_review_corner_loss':primary_corner_loss.get(rs['cisi']),
                     'has_candidate':bool(candidates),
                     'non_target_positions':sum(w not in ('W550','W555') for w in seq),
                     'model_compatible':{label:row_fits(candidates,model) if candidates else None
                                         for label,model in protocol['models'].items()}})
    subsets={'all':rows,'source_complete':[r for r in rows if r['source']['preservation']=='complete'],
             'source_complete_two_context_positions':[r for r in rows if r['source']['preservation']=='complete' and r['non_target_positions']>=2]}
    branches={}
    for name,subset in subsets.items():
        branches[name]={'selected_rows':len(subset),'with_candidates':sum(r['has_candidate'] for r in subset),
            'preservation_counts':dict(Counter(r['source']['preservation'] for r in subset)),
            'models':{label:{
                'compatible':[r['source']['cisi'] for r in subset if r['model_compatible'][label] is True],
                'incompatible_given_candidate_set':[r['source']['cisi'] for r in subset if r['model_compatible'][label] is False],
                'no_candidate_uninformative':[r['source']['cisi'] for r in subset if r['model_compatible'][label] is None]}
                for label in protocol['models']}}
    write_json('results/pincer_preservation_audit.json',{
        'protocol':protocol,'rows':rows,'partitions':branches,
        'M897_primary_disposition':'FEM545=DK9111 and M77text2545 joins verified; normalized M222 retained alongside unresolved fine photographic W550/W555 geometry. Raw code unchanged.',
        'input_sha256':{p:sha256(ROOT/p) for p in paths},
        'established_semantic_values':0,'established_phonetic_values':0})
    for name,b in branches.items():
        print(name,b['selected_rows'],b['with_candidates'],
              {m:{k:len(v) for k,v in s.items()} for m,s in b['models'].items()})
        print('local split exceptions',b['models']['local_split']['incompatible_given_candidate_set'])

if __name__=='__main__':main()
