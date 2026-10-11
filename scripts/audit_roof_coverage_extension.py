"""Integrity and scope checks for expanded roof-source coverage; no visual proof or corpus edits."""
import csv,json,re
from PIL import Image
from common import ROOT,sha256,write_json
from audit_roof_variant_artifacts import check_crop

REVIEW_PATHS=['data/processed/roof_cross_coverage_extension.json','data/processed/roof_u_artifact_extension.json','data/processed/roof_trident_candidate_audit.json','data/processed/roof_trident_new_attestations.json']

def main():
 reviews=[json.loads((ROOT/p).read_text()) for p in REVIEW_PATHS]
 pins=0
 for review in reviews:
  for pin in review.get('evidence_files',review.get('pins',[])):
   assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
   assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
   pins+=1
 cross,u,trident,new=reviews
 for review in (cross,u):
  assert review['semantic_values'] is None and review['phonetic_values'] is None
 for review in (trident,new):
  assert review['established_semantic_values']==review['established_phonetic_values']==0
 by_ref={r['reference']:r for r in cross['records']}
 assert set(by_ref)=={'3319','3320'}
 assert by_ref['3319']['exact_secondary_export_diplomatic']=='+000-342-067-138+'
 for record in cross['records']:
  assert record['catalogued_physical_objects']==1 and record['photo_views']==2
  assert not record['M138_exact_photo_strokes_independently_certified']
  assert record['fields'][0]['tokens']==['M287','M319'] and record['fields'][0]['omitted_from_flat_export']
 assert by_ref['3319']['fields'][1]['unknown_span']
 assert not by_ref['3320']['fields'][1]['unknown_span']
 assert u['new_native_occurrences']==0 and not u['corpus_recoded'] and not u['global_crosswalk_established']
 assert [(r['m77_reference'],r['cisi_alias'],r['excavation'],r['local_position_correspondence']['W']) for r in u['records']]==[('1403','M354','D262','W729'),('2364','M810','DK5890','W731')]
 raw={r['id']:r for r in csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open())}
 native={r['source_reference']:r for r in map(json.loads,(ROOT/'data/processed/m77_candidate_records.jsonl').read_text().splitlines())}
 for r in u['records']:
  assert all(raw[r['secondary_row']['id']][k]==v for k,v in r['secondary_row'].items())
  assert [t['sign'] for t in native[r['m77_reference']]['tokens']]==r['normalized_tokens']
 assert len(trident['candidate_ledger'])==10
 assert {r['raw']['id'] for r in trident['candidate_ledger']}=={i for i,r in raw.items() if '391' in r['text'].replace('/','-').replace('+','-').replace('[','-').replace(']','-').split('-')}
 for r in trident['candidate_ledger']:
  assert all(raw[r['raw']['id']][k]==v for k,v in r['raw'].items())
 dhr=new['DHR24475']; ns=new['NausharoNs53']
 assert dhr['exact_primary_accession']=='24475' and dhr['primary_exact_identity_authenticated']
 assert dhr['roof_over_forked_stem_visible'] and not dhr['all_secondary_token_ids_authenticated']
 assert not dhr['whole_field_completeness_certified'] and not dhr['M163_global_mapping_established']
 assert dhr['stage_table']['stage'] is None and dhr['stage_table']['motif']=='Goat'
 assert not ns['photograph_recovered'] and ns['roof_over_forked_stem_visible'] is None
 for r in new['secondary_candidate_rows']:
  assert all(raw[r['id']][k]==v for k,v in r.items())
 crops=0
 manifests=['data/processed/roof_cross_extension_crop_manifest.json','data/processed/roof_u_extension_crop_manifest.json']
 for path in manifests:
  for c in json.loads((ROOT/path).read_text()):
   with Image.open(ROOT/c['source']) as im:
    box=[round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(c['fractional_box'])]
   target=c.get('crop',c.get('output'))
   check_crop(c['source'],target,box)
   if 'source_sha256' in c:assert sha256(ROOT/c['source'])==c['source_sha256']
   if 'output_sha256' in c:assert sha256(ROOT/target)==c['output_sha256']
   crops+=1
 path='data/processed/roof_trident_new_crop_manifest.json';manifests.append(path)
 manifest=json.loads((ROOT/path).read_text());assert sha256(ROOT/manifest['source'])==manifest['source_sha256']
 for c in manifest['outputs']:
  check_crop(manifest['source'],c['path'],c['box_xyxy'])
  assert sha256(ROOT/c['path'])==c['sha256'];crops+=1
 registry=json.loads((ROOT/'data/sources.json').read_text())
 registered={r['path']:r for k in ('downloads','web_extraction_captures','archived_http_responses') for r in registry[k]}
 for pending,key in [('data/processed/roof_u_new_sources.json','downloads'),('data/processed/roof_trident_new_new_sources.json','sources')]:
  for r in json.loads((ROOT/pending).read_text())[key]:
   assert registered[r['path']]['sha256']==r['sha256'] and sha256(ROOT/r['path'])==r['sha256']
 independent_path='docs/ROOF_U_EXTENSION_INDEPENDENT_REVIEW.md'
 independent_pins=re.findall(r'\|`([^`]+)`\|(\d+)\|`([0-9a-f]{64})`\|',(ROOT/independent_path).read_text())
 assert len(independent_pins)==23
 for p,size,digest in independent_pins:
  assert (ROOT/p).stat().st_size==int(size) and sha256(ROOT/p)==digest,p
 enumerated=json.loads((ROOT/'results/roof_extension_candidates.json').read_text())
 paths=REVIEW_PATHS+manifests+[independent_path]+['results/roof_extension_candidates.json','scripts/audit_roof_coverage_extension.py','scripts/enumerate_roof_extension_candidates.py']
 write_json('results/roof_coverage_extension.json',{'scope':'Source coverage and explicit local comparisons; integrity checks do not independently establish visual readings.','evidence_pin_checks':pins,'independent_review_revision_pin_checks':len(independent_pins),'exact_pixel_crop_checks':crops,'cross_catalogued_objects':2,'cross_script_fields':4,'U_existing_native_objects':2,'Dholavira_exact_photo_recovered':True,'Dholavira_native_M_transcription_promoted':False,'Nausharo_exact_photo_recovered':False,'raw_W391_rows_accounted_for':10,'established_semantic_values':0,'established_phonetic_values':0,'corpus_recoded':False,'prior_frozen_roof_screens_changed':False,'reviews':reviews,'input_sha256':{p:sha256(ROOT/p) for p in paths}})
 print(f'Roof coverage extension: {pins} evidence pins, {crops} exact crops; one additional exact Dholavira photograph, no corpus promotion.')

if __name__=='__main__':main()
