"""Masked one-code discovery over a declared inventory, not a decipherment."""
import json
from collections import defaultdict, Counter
from common import ROOT, read_jsonl, sha256, write_json
from screen_pincer_contexts import feature_map, TARGETS

DOMAIN={f'M{i:03d}' for i in range(1,418)}

def masked_alignment(wseq,mseq,support):
    cursor=0;value=None;segments=[]
    for i,w in enumerate(reversed(wseq)):
        if w=='W617':
            values=mseq[cursor:cursor+2]
            if values!=['M245','M245']:return None
            basis='declared_double_grid_span'
        else:
            if cursor>=len(mseq):return None
            m=mseq[cursor];values=[m]
            if w=='W525':
                if m not in DOMAIN or (value is not None and m!=value):return None
                value=m;basis='masked_candidate_not_established_mapping'
            else:
                possible=TARGETS[w] if w in TARGETS else support.get(w,{})
                if m not in possible:return None
                basis='source_exposed_pincer_candidates' if w in TARGETS else 'catalogue_family_membership'
        segments.append({'reversed_W_position':i,'W':w,'M_positions':list(range(cursor,cursor+len(values))),
                         'M':values,'basis':basis})
        cursor+=len(values)
    return {'W525_candidate':value,'segments':segments} if cursor==len(mseq) and value is not None else None

def main():
    paths=['data/processed/w525_protocol.json','data/processed/lipi_strict.jsonl',
           'data/processed/m77_candidate_strict.jsonl','data/processed/catalogue_features.json',
           'results/pincer_context_screen.json','data/processed/m77_candidate_records.jsonl']
    protocol=json.loads((ROOT/paths[0]).read_text())
    support=feature_map(json.loads((ROOT/paths[3]).read_text()))
    assert not support.get('W525'),'Source mapping changed; masked discovery needs review'
    prior={r['lipi_row']['id'] for r in json.loads((ROOT/paths[4]).read_text())['selected_rows']}
    by_length=defaultdict(list)
    for r in read_jsonl(paths[2]):by_length[len(r['sequence'])].append(r)
    rows=[];pairs=[]
    for r in read_jsonl(paths[1]):
        if 'W525'not in r['sequence']:continue
        n=len(r['sequence'])+r['sequence'].count('W617');hits=[]
        for m in by_length[n]:
            aligned=masked_alignment(r['sequence'],m['sequence'],support)
            if aligned is None:continue
            p={'pair_id':r['id']+'__'+m['id'],'lipi_row':r,'m77_candidate_row':m,
               **aligned,'archaeological_identity':None}
            hits.append(p);pairs.append(p)
        rows.append({'lipi_row':r,'in_previous_pincer_selection':r['id']in prior,
                     'W525_candidates':sorted({p['W525_candidate'] for p in hits}),
                     'candidate_pair_ids':[p['pair_id'] for p in hits],
                     'unmapped_non_target_codes':sorted({w for w in r['sequence'] if w not in {'W525','W617',*TARGETS} and not support.get(w)})})
    summary={'selected_rows':len(rows),'matched_rows':sum(bool(r['candidate_pair_ids']) for r in rows),
             'candidate_pairs':len(pairs),'rows_with_multiple_candidate_codes':sum(len(r['W525_candidates'])>1 for r in rows),
             'candidate_code_pair_incidences':dict(Counter(p['W525_candidate'] for p in pairs)),
             'previous_pincer_rows':sum(r['in_previous_pincer_selection'] for r in rows),
             'matched_previous_pincer_rows':sum(r['in_previous_pincer_selection'] and bool(r['candidate_pair_ids']) for r in rows)}
    diagnostic_records=[]
    for r in read_jsonl(paths[5]):
        if r['source_doc_count']<=1 or str(r['source_direction_code'])!='1':continue
        if not r['tokens'] or any(t['sign'] is None or t['doubtful'] or t['unknown_span'] for t in r['tokens']):continue
        diagnostic_records.append(r)
    diagnostic=[]
    for row in rows:
        r=row['lipi_row']
        for m in diagnostic_records:
            seq=[t['sign'] for t in m['tokens']]
            aligned=masked_alignment(r['sequence'],seq,support)
            if aligned is None:continue
            diagnostic.append({'lipi_row':r,'source_locator_record':m,**aligned,
                               'status':'Unverified multi-document flat-array source locator only; not a recovered face-level text'})
    write_json('results/w525_screen.json',{'protocol':protocol,'summary':summary,'rows':rows,'candidate_pairs':pairs,
        'post_null_multidocument_locator_candidates':diagnostic,
        'locator_scope':'Do not pool these with strict pairs. Source_doc_count exceeds1 and line/face recovery is not certified.',
        'input_sha256':{p:sha256(ROOT/p) for p in paths},
        'established_semantic_values':0,'established_phonetic_values':0,'promoted_artifact_identifications':0})
    print(json.dumps(summary,indent=2))
    for r in rows:
        if r['candidate_pair_ids']:print(r['lipi_row']['cisi_original'],r['W525_candidates'],r['candidate_pair_ids'])
    print('POST-NULL LOCATORS',[(r['lipi_row']['cisi_original'],r['source_locator_record']['source_reference'],r['W525_candidate']) for r in diagnostic])

if __name__=='__main__':main()
