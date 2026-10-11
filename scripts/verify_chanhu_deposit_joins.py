"""Independent metadata-only reconstruction; does not import producer/helpers."""
import csv,hashlib,json,re
from collections import defaultdict,Counter
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','cisi','site','excavation-idno','room-grid','type','depth','phase']
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def identity(s):
 before=re.split(r'pl\s*\.',s,flags=re.I)[0].strip()
 if before.upper().startswith('CH'):before=before[2:].strip()
 m=re.fullmatch(r'(\d+)\s*[,.-]?\s*\(?([a-zA-Z]*)\)?',before)
 return [str(int(m[1])),m[2].upper()] if m else None
def plate(s):
 pieces=re.split(r'pl\s*\.',s,flags=re.I)
 if len(pieces)<2:return None
 m=re.match(r'\s*([IVXL]+)\s*:+\s*(\d+)\b',pieces[1],re.I)
 return f'{m[1].upper()}.{int(m[2])}' if m and m[1].upper() in ['LI','LII'] else None
def metadata_context(r):
 t=r['room-grid'];square=re.search(r'sq\s*[.;]?\s*(\d+)\s*/\s*([A-Za-z])\b',t,re.I);locus=re.search(r'loc\s*\.?\s*(\d+)',t,re.I)
 depth=r['depth'].strip().lower().removesuffix('ft.').removesuffix('ft').strip()
 try:elev=float(depth)
 except ValueError:elev=None
 return {'square':f'{int(square[1])}/{square[2].upper()}' if square else None,'locus':str(int(locus[1])) if locus else None,'elevation_ft':elev}
def main():
 regpath='data/processed/chanhu_deposit_seal_register.json';outpath='results/chanhu_deposit_metadata_joins.json';rawpath='data/raw/lipi_inscriptions.csv'
 reg=json.loads((ROOT/regpath).read_text());actual=json.loads((ROOT/outpath).read_text());mismatches=[]
 def same(label,x,y):
  if x!=y:mismatches.append({'check':label,'independent':x,'producer':y})
 for p,h in actual['input_sha256'].items():same('producer input hash '+p,pin(p)['sha256'],h)
 expected_ids=[f'LI.{n}' for n in range(1,34)]+[f'LII.{n}' for n in range(1,33)]
 same('complete ordered primary frame',[p['row_id'] for p in reg['rows']],expected_ids)
 same('output frame',[p['primary']['row_id'] for p in actual['rows']],expected_ids)
 groups=defaultdict(list)
 for raw in csv.DictReader((ROOT/rawpath).open()):
  if raw['site']=='Chanhu-daro':groups[raw['id'].split('.')[0]].append({k:raw.get(k,'') for k in FIELDS})
 sec=[]
 for obj,rows in sorted(groups.items()):
  ids=[identity(r['excavation-idno']) for r in rows]
  sec.append({'secondary_object_id':obj,'rows':rows,'excavation_key':ids[0] if all(x==ids[0] for x in ids) else None,'seal_type':all(r['type'].split(':')[0]=='SEAL' and ':' in r['type'] for r in rows)})
 rebuilt=[]
 for p in reg['rows']:
  k=identity(p['excavation_number_raw']);numbers=[];seals=[];plates=[];joint=[]
  for s in sec:
   ps=[plate(r['excavation-idno']) for r in s['rows']]
   if p['row_id'] in ps:plates.append(s)
   if s['excavation_key']==k:
    numbers.append(s)
    if s['seal_type']:
     seals.append(s)
     if set(ps)=={p['row_id']}:joint.append(s)
  selected=joint[0] if len(joint)==1 else None
  if len(joint)==1:status='unique_number_and_plate_metadata_match'
  elif len(joint)>1:status='ambiguous'
  elif seals:status='number_match_plate_conflict'
  elif numbers:status='number_match_secondary_class_conflict'
  elif plates:status='plate_match_number_conflict'
  else:status='no_metadata_candidate'
  disagreements=[]
  if selected:
   expected={'square':p['square_raw'],'locus':p['locus_raw'],'elevation_ft':p['elevation_ft']}
   for r in selected['rows']:
    for field,value in metadata_context(r).items():
     if value is not None and expected[field] is not None and str(value)!=str(expected[field]):
      disagreements.append({'secondary_row':r['id'],'field':field,'primary':expected[field],'secondary':value})
  rebuilt.append({'primary':p,'normalized_excavation_key':k,'join_status':status,'candidate_secondary_object_ids':[s['secondary_object_id'] for s in seals],'number_candidates_all_classes':numbers,'plate_candidates_NOT_identity_proof':plates,'selected_secondary_metadata':selected,'provenance_disagreements':disagreements,'text_status':'not_assessed_in_this_metadata_only_phase'})
 same('all full join rows',rebuilt,actual['rows'])
 summary={'primary_catalogue_rows':len(rebuilt),'secondary_site_objects':len(sec),'secondary_site_rows':sum(len(s['rows']) for s in sec),'join_status_counts':dict(Counter(x['join_status'] for x in rebuilt)),'matched_rows_with_provenance_disagreements':sum(bool(x['provenance_disagreements']) for x in rebuilt),'provenance_field_disagreements':sum(len(x['provenance_disagreements']) for x in rebuilt),'secondary_phase_fields':dict(Counter(r['phase'] for s in sec for r in s['rows'])),'new_sign_outcomes_examined':0,'semantic_values_assigned':0}
 same('all summary fields',summary,actual['summary'])
 selectedids=[r['selected_secondary_metadata']['secondary_object_id'] for r in rebuilt if r['selected_secondary_metadata']]
 same('no selected secondary object reused',len(selectedids),len(set(selectedids)))
 visual=[{'row':'LI.4','excavation_number':'518','elevation_ft':0.8,'class_heading':'Seal-amulets of the Harappa Period','secondary_conflict':'MISC; rejected, not silently coerced'}, {'row':'LI.12','excavation_number':'3493','elevation_ft':7.0,'secondary_conflict':'+7.2; retained disagreement'}, {'row':'LI.26','excavation_number':'3043','elevation_ft':7.3,'secondary_conflict':'3817; plate-only candidate rejected;3817 is printed atLI.25'}, {'row':'LI.31','excavation_number':'1293','elevation_ft':14.9,'secondary_conflict':'+14.1; retained disagreement'}, {'row':'LII.15','excavation_number':'2531','elevation_ft':9.6,'secondary_conflict':'2431; plate-only candidate rejected'}]
 for v in visual:
  p=next(p for p in reg['rows'] if p['row_id']==v['row']);same(v['row']+' visual number',v['excavation_number'],p['excavation_number_raw']);same(v['row']+' visual elevation',v['elevation_ft'],p['elevation_ft'])
 crops=[]
 for leaf,box,name in [(312,(1130,2250,4550,2400),'LI4'),(312,(1110,3050,4550,3190),'LI12'),(312,(1110,4240,4650,4500),'LI25and26'),(312,(1110,4800,4550,4960),'LI31'),(313,(800,1730,4260,1900),'LII15')]:
  src=f'data/raw/chanhu_context_leaf{leaf}.jpg';dst=f'results/primary_pages/chanhu-join-independent-{name}.png';Image.open(ROOT/src).crop(box).save(ROOT/dst);crops.append({'source':src,'output':pin(dst),'box_xyxy':box,'operation':'native rectangular crop only'})
 inputs=[regpath,outpath,rawpath,'scripts/build_chanhu_deposit_joins.py','docs/CHANHU_DEPOSIT_PROTOCOL.md','data/raw/chanhu_context_leaf312.jpg','data/raw/chanhu_context_leaf313.jpg','docs/CHANHU_DEPOSIT_JOIN_INDEPENDENT.md','data/processed/chanhu_deposit_join_verification_attempts.json',str(Path(__file__).resolve().relative_to(ROOT))]+[c['output']['path'] for c in crops]
 result={'scope':'independent full metadata reconstruction plus targeted original-page review; no new sign outcome inspection','producer_helpers_imported':False,'all_full_rows_equal':rebuilt==actual['rows'],'all_summary_fields_equal':summary==actual['summary'],'summary':summary,'mismatches':mismatches,'visual_checks':visual,'crop_manifest':crops,'limitations':['65 is completeness of declared LI1–33/LII1–32 illustrated frame, not all excavated seals.','Metadata matches do not authenticate inscription transcriptions.','Only targeted row readings and section boundaries were independently visually checked.','Artifact-number/class conflicts remain unjoined; a source-only MISC label may be an editorial problem, not historical uncertainty about primary section heading.','Implementation compares known square/locus/elevation; missing values and trench/mound/cutting fields are not silently verified by empty disagreement list.'],'established_semantic_values':0,'established_phonetic_values':0,'evidence_files':[pin(p) for p in inputs]}
 (ROOT/'results/chanhu_deposit_join_independent.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':not mismatches,'mismatch_count':len(mismatches),'pins':len(inputs),'summary':summary}))
 if mismatches:raise SystemExit(1)
if __name__=='__main__':main()
