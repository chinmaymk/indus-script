"""Pin two primary tablet reviews and independently verify class equations."""
from pathlib import Path
from fractions import Fraction as F
from PIL import Image
import argparse,csv,hashlib,json,subprocess

ROOT=Path(__file__).resolve().parents[1]
POPPLER='/Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
RENDERS=[('data/raw/cisi_76884.pdf',[262,408],'balanced-tablet-cisi1'),
 ('data/raw/h843_identity_CorpusVol2.pdf',[375,479],'balanced-tablet-cisi2'),
 ('data/raw/h843_identity_CorpusVol2.pdf',[374],'balanced-tablet-cisi2-target')]
CROPS=[('balanced-tablet-cisi1-262.png','balanced-tablet-h326-faces.png',(224,3504,895,4584)),
 ('balanced-tablet-cisi1-408.png','balanced-tablet-h326-metadata.png',(187,432,1379,701)),
 ('balanced-tablet-cisi2-target-374.png','balanced-tablet-h924-faces.png',(1839,2976,3043,3350)),
 ('balanced-tablet-cisi2-479.png','balanced-tablet-h924-metadata.png',(1984,408,3283,672))]

def pin(p):
 f=ROOT/p;return {'path':p,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}

def rref(rows,n):
 m=[[F(x) for x in r] for r in rows];i=0;pivots=[]
 for j in range(n):
  k=next((k for k in range(i,len(m)) if m[k][j]),None)
  if k is None:continue
  m[i],m[k]=m[k],m[i];d=m[i][j];m[i]=[x/d for x in m[i]]
  for k in range(len(m)):
   if k!=i:
    d=m[k][j];m[k]=[x-d*y for x,y in zip(m[k],m[i])]
  pivots.append(j);i+=1
  if i==len(m):break
 inconsistent=any(not any(r[:n]) and r[n] for r in m)
 return {'inconsistent':inconsistent,'coefficient_rank':len(pivots),
         'rref':[[str(x) for x in r] for r in m]}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--render',action='store_true');args=ap.parse_args()
 base=ROOT/'results/primary_pages'
 if args.render:
  for src,pgs,prefix in RENDERS:
   for pg in pgs:
    subprocess.run([POPPLER,'-f',str(pg),'-l',str(pg),'-singlefile','-scale-to','4800','-png',str(ROOT/src),str(base/f'{prefix}-{pg}')],check=True)
 crop_records=[]
 for src,out,box in CROPS:
  im=Image.open(base/src);assert max(im.size)==4800
  im.crop(box).save(base/out)
  crop_records.append({'source':'results/primary_pages/'+src,'output':'results/primary_pages/'+out,'box':list(box),'source_pixels':list(im.size),'operation':'native crop only'})
 raw=[]
 with (ROOT/'results/numeral_pair_source_rows.csv').open() as stream:
  raw=[r for r in csv.DictReader(stream) if r['cisi'] in ['H-326','H-924']]
 assert len(raw)==4
 assert {r['text'] for r in raw}=={'+740-840-013+','+700-033+'}
 # Independently reconstruct pure-class coefficients from frozen eligible
 # token flanks, then use linear elimination rather than graph traversal.
 screen=json.loads((ROOT/'results/numeral_pair_screen.json').read_text())['screens']['allow_LR_sensitivity']['records']
 lookup={**{f'W{i:03}':('long',i-30) for i in range(31,40)},
         **{f'W{i:03}':('stacked',i-10) for i in range(12,20)},
         **{f'W{i:03}':('short',i) for i in range(1,8)}}
 edges=[];mixed=[]
 for rec in screen:
  if not rec['eligible']:continue
  fields=[]
  for marker in ['W700','W840']:
   tokens=rec['faces'][marker]['left']+rec['faces'][marker]['right']
   vals=[lookup.get(t) for t in tokens]
   if not vals or None in vals or len({v[0] for v in vals})!=1:fields.append(None)
   else:fields.append((marker+':'+vals[0][0],sum(v[1] for v in vals)))
  if None in fields:mixed.extend(rec['cisi']);continue
  edges.append({'cisi':rec['cisi'],'nodes':[f[0] for f in fields],'counts':[f[1] for f in fields]})
 producer=json.loads((ROOT/'results/numeral_class_constraints.json').read_text())
 assert len(screen)==20 and sum(r['eligible'] for r in screen)==6 and len(edges)==5 and mixed==['H-904']
 assert edges==[{k:r[k] for k in ['cisi','nodes','counts']} for r in producer['pure_class_edges']]
 names=['W700:long','W840:long','W840:stacked']
 def matrix(es):
  out=[]
  for e in es:
   row=[0,0,0,0];row[names.index(e['nodes'][0])]+=e['counts'][0];row[names.index(e['nodes'][1])]-=e['counts'][1];out.append(row)
  return out+[[1,0,0,1]] # a=1; positive homogeneous solutions permit this scale.
 all_check=rref(matrix(edges),3)
 remaining=[e for e in edges if e['cisi']!=['H-1923']]
 limited=rref(matrix(remaining),3)
 collapsed=rref(matrix(remaining)+[[0,1,-1,0]],3)
 assert all_check['inconsistent'] and not limited['inconsistent'] and collapsed['inconsistent']
 candidate=[F(1),F(3,2),F(1)]
 assert all(sum(F(x)*y for x,y in zip(row[:3],candidate))==row[3] for row in matrix(remaining))
 assert limited['coefficient_rank']==3
 assert producer['without_unverified_H1923']['normalized_component_values']==dict(zip(names,map(str,candidate)))
 assert producer['implied_W840_stacked_over_long_without_H1923']==str(candidate[2]/candidate[1])=='2/3'
 assert not producer['all_source_records']['positive_solution_exists']
 assert producer['without_unverified_H1923']['positive_solution_exists']
 assert not producer['without_H1923_but_equating_long_and_stacked']['positive_solution_exists']
 hash_checks={p:pin(p)['sha256']==h for p,h in producer['input_sha256'].items()};assert all(hash_checks.values())
 out={
  'date':'2026-09-28','scope':'Two selected primary examples, not three independent equalities or a numerical reading',
  'reviewed_physical_examples':['H-326','H-924'],'H925_primary_reviewed':False,
  'identities':[
   {'cisi':'H-326','photo':{'volume':1,'printed':226,'pdf':262},'metadata':{'printed':372,'pdf':408},
    'finnish':'3564','excavation':'1171','museum':'ASI 63.11.79','photograph_reference':'HU 564',
    'secondary_excavation_raw':'1171564','raw_field_not_silently_rewritten':True},
   {'cisi':'H-924','photo':{'volume':2,'printed':339,'pdf':374},'metadata':{'printed':444,'pdf':479},
    'finnish':'4096','excavation':'???','museum':'HM 296','photograph_reference':'P 1104',
    'secondary_excavation_raw':'3286','excavation_join_authenticated':False,
    'conflict':'3286 is printed on following H925(1) row, not H924.'}],
  'local_rows':raw,
  'graphic_observations':[
   {'cisi':'H-326','A':{'count_candidate':3,'class':'staggered/stacked','context_marker_code':'W840','residual_codes':['W740'],
     'confidence':'compatible three-mark pattern; endpoints and left B marker less clear; central notch/loss'},
    'B':{'count':3,'class':'long side-by-side','context_marker_code':'W700','residual_codes':[]},'physical_completeness_certified':False},
   {'cisi':'H-924','A':{'count':3,'class':'stacked two upper plus one lower','context_marker_code':'W840','residual_codes':['W740']},
    'B':{'count':3,'class':'long side-by-side','context_marker_code':'W700','residual_codes':[]},
    'physical_completeness_certified':False,'pattern_confidence':'clear visible groups; no whole-surface certification'}],
  'same_graphic_class_on_both_faces':False,'stacked_equals_long_globally_established':False,
  'equal_represented_quantities_established':False,
  'independent_graph_check':{'producer_imported':False,'eligibility_reconstructed':False,'frozen_eligibility_input':True,
    'candidate_groups':20,'eligible_groups':6,'pure_class_edges':edges,'mixed_excluded':mixed,
    'all_with_a_normalized_to_one':all_check,'without_H1923':limited,'without_H1923_plus_b_equals_c':collapsed,
    'conditional_normalized_values':dict(zip(names,map(str,candidate))),
    'conditional_stacked_over_long_at_W840':'2/3','distinct_equation_patterns_without_H1923':2,
    'input_hash_checks':hash_checks,'mismatches':0,
    'limits':'Frozen selection not independently revalidated; H925 unreviewed; repeated equations are not independent constraints; no positive interpretation inferred.'},
  'attempts':[{'source':'CISI1 PDF263','outcome':'H329–334, wrong target page; previous PDF262 found H326'},
              {'source':'CISI2 PDF375','outcome':'H927–942, wrong target page; previous PDF374 found H924'},
              {'source':'H924 metadata OCR crop','outcome':'unreliable OCR; primary row read visually'}],
  'crop_records':crop_records,'downloads':0,'established_semantic_values':0,'established_phonetic_values':0,
 }
 paths=[s for s,_,_ in RENDERS]+['results/primary_pages/'+f'{prefix}-{pg}.png' for _,pgs,prefix in RENDERS for pg in pgs]+[r['output'] for r in crop_records]+[
  'docs/BALANCED_TABLET_PRIMARY_REVIEW.md','docs/NUMERAL_IMAGES.md','docs/NUMERAL_SCREEN.md',
  'results/numeral_pair_screen.json','results/numeral_pair_source_rows.csv','results/numeral_class_constraints.json',
  'scripts/analyze_numeral_class_constraints.py','scripts/screen_numeral_pairs.py',
  'results/primary_pages/cisi1-28.png','results/primary_pages/h843-cisi2-key-28.png','results/primary_pages/h843-cisi2-key-469.png',
  'results/balanced-tablet-cisi1_extraction.json','results/balanced-tablet-cisi2_extraction.json','results/balanced-tablet-cisi2-target_extraction.json',
  str(Path(__file__).resolve().relative_to(ROOT))]
 out['evidence_files']=[pin(p) for p in sorted(set(paths))]
 target=ROOT/'data/processed/balanced_tablet_primary_review.json';target.write_text(json.dumps(out,indent=2)+'\n')
 assert all(pin(p['path'])==p for p in out['evidence_files'])
 print(json.dumps({'output':str(target.relative_to(ROOT)),'primary_examples':2,'pins':len(out['evidence_files']),'graph_mismatches':0}))

if __name__=='__main__':main()
