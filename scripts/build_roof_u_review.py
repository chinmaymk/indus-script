"""Materialize the explicit manual roof-U review and its evidence pins; do not silently refresh a frozen review."""
from pathlib import Path
import csv,json,hashlib
r=Path(__file__).resolve().parents[1]
raws={v['id']:v for v in csv.DictReader((r/'data/raw/lipi_inscriptions.csv').open())}
native={v['source_reference']:v for v in map(json.loads,(r/'data/processed/m77_candidate_records.jsonl').read_text().splitlines())}
records=[]
for ref,ident,pub,field,raw_id,w,code,shape in [('1403','M354','MIC403','D262','2850.1','W729','100001','long basal extension oblique/curved'),('2364','M810','FEM364','DK5890','3223.1','W731','100101','long basal extension approximately vertical')]:
 n=native[ref]; raw=raws[raw_id]
 records.append({'m77_reference':ref,'cisi_alias':ident,'publication_item':pub,'excavation':field,'literal_metadata':code,'normalized_tokens':[t['sign'] for t in n['tokens']],'existing_native_record':True,'strict_flag_unchanged':n['strict_candidate'],'secondary_row':{k:raw[k] for k in ['id','cisi','excavation-idno','site','type','preservation','condition','complete','text','dir.']},'local_position_correspondence':{'W':w,'M':'M334','scope':'this artifact and target position only'},'photographic_observation':shape,'roof_body_basal_arrangement_visible':True,'every_neighbouring_sign_certified':False,'catalogued_physical_objects':1})
records[0]['metadata']={'source':'Marshall II printed404/PDF55; CISI1 printed368/PDF404','material':'white steatite','size_inches':[2.25,.6],'type':'F','depth':None,'museum':'NMI15','photo':'HU912','photo_page':'CISI1 printed88/PDF124; Marshall III plateCXII item403'}
records[0]['preservation']='Broadly preserved text field; uneven edges and surface marks; fine completeness not certified.'
records[1]['metadata']={'source':'Mackay printed380 row364; CISI2 printed436/PDF471','material':'steatite','size_inches':[1.02,1.02,.26],'type':'B','locus_literal':'Bet. Bls. 1 (V) & 10','level_ft':-11.7,'museum_secure_literal':'MD195','following_accession_tentative':'50.14','following_accession_used_for_join':False,'photos':['JL311','P231'],'photo_page':'CISI2 printed70/PDF105'}
records[1]['preservation']='Large missing lower corner lies in animal field; upper two-sign field broadly preserved; artifact not intact.'
paths=['data/raw/mahadevan_1977_text.pdf','data/raw/cisi_76884.pdf','data/raw/h843_identity_CorpusVol2.pdf','data/raw/stone1471_marshall1931_volume2_text.pdf','data/raw/lipi_inscriptions.csv','data/raw/roof_u_mackay_leaf402.jpg','data/raw/roof_u_marshall_leaf199.jpg','data/processed/m77_candidate_records.jsonl','data/processed/catalogue_features.json','data/processed/roof_u_extension_crop_manifest.json','scripts/render_roof_u_extension_crops.py','scripts/download_roof_u_sources.py','docs/ROOF_U_ARTIFACT_EXTENSION.md','results/primary_pages/crab-cisi-target-404.png']
paths += [str(p.relative_to(r)) for p in sorted((r/'results').glob('roof-u-extension*_extraction.json'))]
paths += [str(p.relative_to(r)) for p in sorted((r/'results/primary_pages').glob('roof-u-extension*.png'))]
obj={'date':'2026-09-27','scope':'Two already exported M334 objects independently identified and photographed; no new native occurrence.','records':records,'correspondence_rule_source':'M77 AppendixV printed818/PDF827, MIC1001–1560=items1–560 and FEM2002–2704=items2–704','new_native_occurrences':0,'catalogued_objects_reviewed':2,'global_crosswalk_established':False,'corpus_recoded':False,'semantic_values':None,'phonetic_values':None,'evidence_files':[{'path':p,'bytes':(r/p).stat().st_size,'sha256':hashlib.sha256((r/p).read_bytes()).hexdigest()} for p in dict.fromkeys(paths)]}
(r/'data/processed/roof_u_artifact_extension.json').write_text(json.dumps(obj,indent=2)+'\n')
print(len(obj['evidence_files']))
