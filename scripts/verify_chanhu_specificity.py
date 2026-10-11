"""Independent raw-CSV singleton-status and exact-bound reconstruction."""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction as F
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 x=ROOT/p
 return {'path':p,'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()}
def parse(s):
 # Digit spans with immediate source qualifier characters, independently scanned.
 found=[]
 for m in re.finditer(r'\d+',s):
  if len(m[0])!=3:continue
  pre=s[m.start()-1] if m.start() else '';post=s[m.end()] if m.end()<len(s) else ''
  doubtful=pre in ('*','?') or post=='?'
  found.append(('W'+m[0],doubtful))
 return found
def status(rows,code):
 if rows is None:return 'unknown'
 seen=[];all_complete=True
 for r in rows:
  tok=parse(r['text']);seen.extend(x for x,doubt in tok if not doubt)
  all_complete &= r['complete']=='Y' and r['preservation']=='complete' and bool(tok) and not any(x=='W000' or doubt for x,doubt in tok) and not any(x in r['text'] for x in '[]?*')
 if code in seen:return 'positive'
 return 'negative' if all_complete else 'unknown'
def counts(xs):
 return {k:sum(x==k for x in xs) for k in ['positive','negative','unknown']}
def bounds(xs):
 a=xs[:3];b=xs[3:];amin=sum(s=='positive' for s in a);amax=sum(s!='negative' for s in a);bmin=sum(s=='positive' for s in b);bmax=sum(s!='negative' for s in b)
 return [str(F(amin,len(a))-F(bmax,len(b))),str(F(amax,len(a))-F(bmin,len(b)))]
def main():
 path='results/chanhu_local_specificity.json';actual=json.loads((ROOT/path).read_text());joins=json.loads((ROOT/'results/chanhu_deposit_metadata_joins.json').read_text());local=json.loads((ROOT/'results/chanhu_local_contrast.json').read_text());features=json.loads((ROOT/'data/processed/catalogue_features.json').read_text())
 failures=[]
 def eq(label,x,y):
  if x!=y:failures.append({'check':label,'expected':x,'actual':y})
 for p,h in actual['input_sha256'].items():eq('input hash '+p,pin(p)['sha256'],h)
 groups=defaultdict(list)
 for r in csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open()):
  if r['site']=='Chanhu-daro':groups[r['id'].split('.')[0]].append({k:r[k] for k in ['id','text','complete','preservation']})
 prior=json.loads((ROOT/'results/chanhu_fish_audit.json').read_text())
 for r in prior['secondary_objects']:
  eq('raw source rows '+r['secondary_object_id'],groups[r['secondary_object_id']],[{k:q[k] for k in ['id','text','complete','preservation']} for q in r['rows']])
 ids=[r['primary_row'] for r in local['objects']];eq('fixed order',ids,['LI.15','LII.19','LII.23','LI.14','LI.22'])
 frame={x['primary']['row_id']:groups[x['selected_secondary_metadata']['secondary_object_id']] if x['selected_secondary_metadata'] else None for x in joins['rows']}
 background={k:v for k,v in frame.items() if k not in ids}
 eq('frame size',len(frame),65);eq('background size',len(background),60);eq('selected join count',sum(v is not None for v in frame.values()),55);eq('unjoined background',sum(v is None for v in background.values()),10)
 exclusions={'W000','W999','W221'}
 for f in features:
  name=f['id']
  if len(name)==4 and name[0]=='P' and name[1:].isdigit() and 50<=int(name[1:])<=65:exclusions.update(f['wells_graphemes'])
 observed={c for rows in background.values() for r in rows or [] for c,doubt in parse(r['text']) if not doubt}
 controls=sorted(observed-exclusions);eq('exclusions',sorted(exclusions),actual['excluded_codes'])
 results=[]
 for code in ['W220']+controls:
  stat={key:status(rows,code) for key,rows in background.items()};localstat=[status(frame[key],code) for key in ids];b=bounds(localstat)
  results.append({'code':code,'background':{'counts':counts(list(stat.values())),'object_status':stat},'local_status_vector':localstat,'difference_bounds':b,'interval_width':str(F(b[1])-F(b[0]))})
 eq('all complete code rows',results,actual['all_code_results']);target=results[0];eq('target',target,actual['target']);eq('local baseline reproduces',target['difference_bounds'],local['fixed_five_object_contrasts']['plain_fish']['difference_bounds'])
 lookup={r['code']:r for r in results};f=target['background']['counts']['positive'];u=target['background']['counts']['unknown']
 sets={'all_background_observed_controls':controls,'same_observed_positive_count':[],'same_positive_and_unknown_counts':[],'half_to_twice_observed_positive_count':[]}
 for c in controls:
  cc=lookup[c]['background']['counts'];n=cc['positive']
  if n==f:sets['same_observed_positive_count'].append(c)
  if n==f and cc['unknown']==u:sets['same_positive_and_unknown_counts'].append(c)
  if f>0 and F(f,2)<=n<=2*f:sets['half_to_twice_observed_positive_count'].append(c)
 summaries={}
 for label,codes in sets.items():
  rs=[lookup[c] for c in codes]
  summaries[label]={'control_codes':codes,'n_codes':len(codes),'distinct_local_profiles':len({tuple(x['local_status_vector']) for x in rs}),'equal_target_status_profile':[x['code'] for x in rs if x['local_status_vector']==target['local_status_vector']],'equal_target_interval':[x['code'] for x in rs if x['difference_bounds']==target['difference_bounds']],'at_least_target_lower_bound':[x['code'] for x in rs if F(x['difference_bounds'][0])>=F(target['difference_bounds'][0])],'strictly_greater_lower_bound':[x['code'] for x in rs if F(x['difference_bounds'][0])>F(target['difference_bounds'][0])]}
 eq('all control sets and summaries',summaries,actual['control_set_summaries'])
 profiles=defaultdict(list)
 for x in results[1:]:profiles['|'.join(x['local_status_vector'])].append(x['code'])
 eq('profile equivalence classes',dict(profiles),actual['distinct_profile_groups'])
 for key,v in [('primary_frame_size',65),('background_size',60),('unjoined_background_objects',10),('local_primary_order',ids),('zero_background_target_frequency',f==0),('p_value',None),('semantic_values_assigned',0),('phonetic_values_assigned',0)]:eq(key,v,actual[key])
 # Additional finite diagnostics, explicitly after protocol and production output.
 diagnostic=[]
 for code in ['W220']+summaries['all_background_observed_controls']['at_least_target_lower_bound']:
  x=lookup[code];vec=x['local_status_vector'];a=[vec[i] for i in [0,2]];b=vec[3:]
  drop=[str(F(sum(t=='positive' for t in a),2)-F(sum(t!='negative' for t in b),2)),str(F(sum(t!='negative' for t in a),2)-F(sum(t=='positive' for t in b),2))]
  diagnostic.append({'code':code,'local_status_vector':vec,'background_counts':x['background']['counts'],'difference_bounds':x['difference_bounds'],'after_omitting2428_bounds':drop,'certain_positive_primary_rows':[k for k,s in zip(ids,vec) if s=='positive']})
 overlap_rows=[]
 for x in results[1:]:
  c=x['background']['counts'];low=c['positive'];high=low+c['unknown'];a=max(f,low);b=min(f+u,high)
  overlap_rows.append({'code':x['code'],'marginal_possible_count_interval':[low,high],'intersection_with_target':[a,b] if a<=b else None,'marginal_overlap':a<=b})
 overlap={'status':'posthoc requested after control outcomes; not a replacement matched set','target_marginal_interval':[f,f+u],'controls_with_overlap':sum(x['marginal_overlap'] for x in overlap_rows),'controls_total':len(overlap_rows),'interpretation':'Necessary compatibility from marginal intervals only; no probability or guaranteed common joint completion.','rows':overlap_rows}
 files=[path,'results/chanhu_deposit_metadata_joins.json','results/chanhu_fish_audit.json','results/chanhu_local_contrast.json','data/raw/lipi_inscriptions.csv','data/processed/catalogue_features.json','docs/CHANHU_LOCAL_SPECIFICITY_PROTOCOL.md','scripts/analyze_chanhu_specificity.py','scripts/audit_chanhu_fish.py','scripts/verify_chanhu_specificity.py','docs/CHANHU_LOCAL_SPECIFICITY_INDEPENDENT.md']
 report={'scope':'independent reconstruction after protocol saved; no production helpers imported','all_checks_passed':not failures,'mismatches':failures,'full_code_rows_compared':len(results),'background_statuses_compared':len(results)*len(background),'local_statuses_compared':len(results)*len(ids),'control_set_summaries':summaries,'target_background':target['background']['counts'],'target_local_vector':target['local_status_vector'],'distinct_control_profile_count':len(profiles),'post_protocol_omission_diagnostics':diagnostic,'design_protocol_difference':'Actual frozen protocol uses primary65 frame/background60 and certain-background code inventory excludingP050–P065/W221; pre-count independent design advice discussed broader export/all-code inventory. Verification follows actual frozen protocol.','established_semantic_values':0,'established_phonetic_values':0,'evidence_files':[pin(p) for p in files]}
 report['posthoc_background_marginal_compatibility']=overlap
 (ROOT/'results/chanhu_local_specificity_independent.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':not failures,'mismatches':len(failures),'code_rows':len(results),'target_background':target['background']['counts'],'posthoc_marginal_overlaps':overlap['controls_with_overlap'],'diagnostics':diagnostic}))
 if failures:raise SystemExit(1)
if __name__=='__main__':main()
