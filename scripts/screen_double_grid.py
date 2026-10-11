"""One explicitly declared 1-to-2 catalogue mapping, not semantic composition."""
import json
from collections import Counter, defaultdict
from common import ROOT, read_jsonl, sha256, write_json
from screen_pincer_contexts import feature_map, TARGETS

def aligned_segments(w_sequence,m_sequence,support):
    segments=[];cursor=0
    for i,w in enumerate(reversed(w_sequence)):
        if w=='W617':
            if m_sequence[cursor:cursor+2]!=['M245','M245']:return None
            segments.append({'reversed_W_position':i,'W':w,'M_positions':[cursor,cursor+1],
                             'M':['M245','M245'],'basis':'source_exposed_double_grid_tokenization'})
            cursor+=2
        else:
            candidates=TARGETS[w] if w in TARGETS else support.get(w,{})
            if cursor>=len(m_sequence) or m_sequence[cursor] not in candidates:return None
            m=m_sequence[cursor]
            segments.append({'reversed_W_position':i,'W':w,'M_positions':[cursor],'M':[m],
                             'basis':'target_hypothesis' if w in TARGETS else 'feature_membership',
                             'feature_ids':[] if w in TARGETS else support[w][m]})
            cursor+=1
    return segments if cursor==len(m_sequence) else None

def main():
    paths=['data/processed/double_grid_protocol.json','results/pincer_context_screen.json',
           'data/processed/catalogue_features.json','data/processed/lipi_strict.jsonl',
           'data/processed/m77_candidate_strict.jsonl','data/processed/double_grid_primary_review.json']
    protocol=json.loads((ROOT/paths[0]).read_text());old=json.loads((ROOT/paths[1]).read_text())
    primary=json.loads((ROOT/paths[5]).read_text())
    for pin in primary['evidence_files']:
        assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
        assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
    support=feature_map(json.loads((ROOT/paths[2]).read_text()))
    lipi=read_jsonl(paths[3]);m77=read_jsonl(paths[4]);by_length=defaultdict(list)
    for r in m77:by_length[len(r['sequence'])].append(r)
    old_ids={r['lipi_row']['id'] for r in old['selected_rows']}
    old_pairs={p['pair_id'] for p in old['candidate_pairs']}
    rows=[];pairs=[]
    for r in lipi:
        if r['id'] not in old_ids and 'W617' not in r['sequence']:continue
        n=len(r['sequence'])+r['sequence'].count('W617');hits=[]
        for m in by_length[n]:
            segments=aligned_segments(r['sequence'],m['sequence'],support)
            if segments is None:continue
            pid=r['id']+'__'+m['id'];hits.append(pid)
            pairs.append({'pair_id':pid,'lipi_row':r,'m77_candidate_row':m,'segments':segments,
                          'previous_pincer_candidate':pid in old_pairs,'archaeological_identity':None})
        rows.append({'lipi_row':r,'W_tokens':len(r['sequence']),'expected_M_tokens':n,
                     'W617_occurrences':r['sequence'].count('W617'),'candidate_pair_ids':hits,
                     'in_previous_pincer_selection':r['id'] in old_ids})
    pincer=[r for r in rows if r['in_previous_pincer_selection']]
    grids=[r for r in rows if r['W617_occurrences']]
    new_ids={p['pair_id'] for p in pairs if p['lipi_row']['id'] in old_ids}
    assert old_pairs<=new_ids,'Expansion must preserve all prior non-W617 matches'
    summary={}
    for name,rs in [('pincer',pincer),('all_W617',grids)]:
        summary[name]={'selected_rows':len(rs),'rows_with_candidates':sum(bool(r['candidate_pair_ids']) for r in rs),
                       'candidate_pairs':sum(len(r['candidate_pair_ids']) for r in rs),
                       'rows_with_multiple_candidates':sum(len(r['candidate_pair_ids'])>1 for r in rs)}
    summary['prior_pincer_pairs_preserved']=len(old_pairs)
    summary['new_pincer_pairs']=len(new_ids-old_pairs)
    summary['new_pincer_candidate_rows']=[r['lipi_row']['cisi_original'] for r in pincer
        if r['candidate_pair_ids'] and not any(p in old_pairs for p in r['candidate_pair_ids'])]
    seed=[p for p in pairs if p['lipi_row']['id']==primary['object']['secondary_W_row']
          and p['m77_candidate_row']['source_reference']==str(primary['object']['mahadevan_text'])]
    assert len(seed)==1
    assert seed[0]['lipi_row']['sequence']==primary['W_sequence']
    assert seed[0]['m77_candidate_row']['sequence']==primary['M_sequence_reading_order']
    write_json('results/double_grid_screen.json',{'protocol':protocol,'summary':summary,'rows':rows,'candidate_pairs':pairs,
        'separate_primary_review':paths[5],
        'primary_scope':'M81 identity independently established by reviewed source catalogues; screen candidates are not promoted by sequence similarity',
        'input_sha256':{p:sha256(ROOT/p) for p in paths},
        'established_semantic_values':0,'established_phonetic_values':0,'promoted_artifact_identifications':0})
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
