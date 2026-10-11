"""Conditional replication using secondary W transcriptions and joint metadata.

No semantic columns are read. M-family labels are conditional on the saved,
unverified crosswalk. This is descriptive matching, not causal adjustment or a
population significance test. The primary M77 marginals are never pooled in.
"""
from collections import Counter,defaultdict
import csv
import json
from common import ROOT,read_jsonl,write_csv,write_json

PAIRS=[('M342','M343','reading_final'),('M342','M344','reading_final'),
       ('M342','M345','reading_final'),('M087','M099','reading_initial'),
       ('M059','M065','reading_initial')]
MISSING={'','-','--','?','unknown','none'}

def position(i,length):
    if length==1:return 'single'
    if i==0:return 'reading_final'
    if i==length-1:return 'reading_initial'
    return 'medial'

def select_records(records,regime):
    seen=set();out=[]
    for r in records:
        if r['site'].strip().lower() in MISSING or r['type'].strip().lower() in MISSING:
            continue
        context=(r['site'],r['type'],tuple(r['sequence']))
        key=(r['artifact'],*context) if regime=='artifact_sequence_context' else context
        if regime!='all_rows' and key in seen:continue
        seen.add(key);out.append(r)
    return out

def summarize_cells(cells,event,minimum=1):
    matched=[]
    for key,(a,b) in cells.items():
        na,nb=sum(a.values()),sum(b.values())
        if min(na,nb)<minimum:continue
        # Harmonic overlap weight reduces domination by one-sided strata.
        weight=2*na*nb/(na+nb)
        matched.append((weight,a[event]/na,b[event]/nb,na,nb))
    w=sum(x[0] for x in matched)
    return {'matched_strata':len(matched),'matched_first_tokens':sum(x[3] for x in matched),
        'matched_second_tokens':sum(x[4] for x in matched),'overlap_weight_sum':w,
        'weighted_first_event_rate':sum(x[0]*x[1] for x in matched)/w if w else None,
        'weighted_second_event_rate':sum(x[0]*x[2] for x in matched)/w if w else None,
        'weighted_first_minus_second':sum(x[0]*(x[1]-x[2]) for x in matched)/w if w else None}

def main():
    records=read_jsonl('data/processed/lipi_strict.jsonl')
    with (ROOT/'data/processed/candidate_crosswalk.csv').open() as f:
        cross=list(csv.DictReader(f))
    wanted={s for a,b,_ in PAIRS for s in [a,b]}
    mapping={m:{r['wells'] for r in cross if r['mahadevan']==m and r['wells']} for m in wanted}
    if any(not group for group in mapping.values()):raise ValueError('Missing candidate mapping')
    if len(set.union(*mapping.values()))!=sum(map(len,mapping.values())):
        raise ValueError('Selected candidate groups overlap')
    reverse=defaultdict(set)
    for row in cross:reverse[row['wells']].add(row['mahadevan'])
    summaries=[];details=[];record_counts={}
    for regime in ['all_rows','artifact_sequence_context','sequence_context']:
        selected=select_records(records,regime);record_counts[regime]=len(selected)
        for context_mode in ['site_type','site_type_length']:
            for a,b,event in PAIRS:
                cells=defaultdict(lambda:[Counter(),Counter()])
                for row in selected:
                    key=(row['site'],row['type'])
                    if context_mode=='site_type_length':key+= (len(row['sequence']),)
                    for i,sign in enumerate(row['sequence']):
                        which=0 if sign in mapping[a] else 1 if sign in mapping[b] else None
                        if which is not None:cells[key][which][position(i,len(row['sequence']))]+=1
                na=sum(sum(c[0].values()) for c in cells.values());nb=sum(sum(c[1].values()) for c in cells.values())
                for minimum in [1,5]:
                    summaries.append({'regime':regime,'context':context_mode,'first_candidate_M':a,
                        'second_candidate_M':b,'first_W_codes':' '.join(sorted(mapping[a])),
                        'second_W_codes':' '.join(sorted(mapping[b])),
                        'first_reverse_M_candidates':' '.join(sorted(set.union(*(reverse[w] for w in mapping[a])))),
                        'second_reverse_M_candidates':' '.join(sorted(set.union(*(reverse[w] for w in mapping[b])))),
                        'event':event,
                        'minimum_each_sign_tokens_per_stratum':minimum,
                        'all_first_tokens':na,'all_second_tokens':nb,**summarize_cells(cells,event,minimum),
                        'mapping_status':'conditional_on_secondary_crosswalk'})
                for key,(ca,cb) in sorted(cells.items()):
                    na,nb=sum(ca.values()),sum(cb.values())
                    details.append({'regime':regime,'context':context_mode,'first_candidate_M':a,
                        'second_candidate_M':b,'site':key[0],'type_code':key[1],
                        'length':key[2] if len(key)>2 else 'all','event':event,
                        'first_tokens':na,'second_tokens':nb,'first_event_tokens':ca[event],
                        'second_event_tokens':cb[event],
                        'first_event_rate':ca[event]/na if na else None,
                        'second_event_rate':cb[event]/nb if nb else None,
                        'first_minus_second':ca[event]/na-cb[event]/nb if na and nb else None,
                        'shared_stratum':bool(na and nb)})
    write_csv('results/joint_context_summary.csv',summaries)
    write_csv('results/joint_context_strata.csv',details)
    write_json('results/joint_context_audit.json',{'input_rows':len(records),'retained_record_counts':record_counts,
        'candidate_mappings':{m:sorted(v) for m,v in sorted(mapping.items())},
        'inverse_mapping_conflicts':{w:sorted(ms) for w,ms in reverse.items() if w in set.union(*mapping.values()) and len(ms)>1},
        'selection':'Five contrasts selected before this joint-context replication, but exploratory overall.',
        'order':'File-left edge treated as reading-final only for the prefiltered R/L, single-line corpus. Singles remain separate.',
        'weight':'2*n_first*n_second/(n_first+n_second), normalized over shared strata meeting the stated minimum',
        'limitations':['M labels are candidate groups in a secondary W corpus; mapping is not independently verified.',
          'Site/type strings are retained verbatim. Codes are not silently merged or assigned primary-book meanings.',
          'No primary-book rows are pooled into these counts.',
          'Matching changes the target population to observed shared contexts; unmatched tokens are reported.',
          'Deduplication changes weights but does not guarantee independent artifacts or eliminate shared templates.',
          'No p-values, confidence intervals, causal claims or semantic identifications are made.']})
    for row in summaries:
        if row['regime']=='sequence_context' and row['context']=='site_type_length' and row['minimum_each_sign_tokens_per_stratum']==5:
            print(row['first_candidate_M'],row['second_candidate_M'],row['matched_strata'],row['matched_first_tokens'],row['matched_second_tokens'],row['weighted_first_minus_second'])

if __name__=='__main__':
    main()
