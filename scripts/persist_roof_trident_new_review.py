"""Persist the bounded manual review, source attempts and content hashes; no network."""
from pathlib import Path
import json,hashlib,csv,re
R=Path(__file__).resolve().parents[1]
def pin(p):
 p=R/p if not isinstance(p,Path) else p
 return {'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
ledger=R/'data/processed/roof_trident_new_download_attempts.json'
a=json.loads(ledger.read_text())
for x in a:
 if 'error' in x and 'path' not in x:x['response_body_retained']=False;x['preservation_note']='Initial downloader recorded HTTP exception without reading response body.'
base='https://ia801906.us.archive.org/19/items/dholavirareportpreliminaryjan2015_860_K/'
name='Dholavira%20Report%20%28preliminary%2C%20Jan%202015%29'
extra=[
 {'url':base+name+'.pdf','kind':'interrupted_full_pdf_transfer','error':'KeyboardInterrupt during response.read(); command exited130','response_body_retained':False,'preservation_note':'Slow full127352282byte response stopped at parent instruction; in-memory partial buffer not recoverable, no local PDF created.'},
 {'url':base+name+'_djvu.txt','kind':'archive_generated_ocr_text_navigation_only','path':'data/raw/roof_trident_new_dholavira_djvu.txt','headers':'data/raw/roof_trident_new_dholavira_text_headers.txt','status':200},
 {'url':base+name+'_page_numbers.json','kind':'archive_generated_page_index','path':'data/raw/roof_trident_new_dholavira_page_numbers.json','headers':'data/raw/roof_trident_new_page_numbers_headers.txt','status':200},
 {'url':'http://museumsofindia.gov.in:81/cdn/portal_record/%5Bnat_del%5D/nat_del-DHR-24475-18639/nat_del-DHR-24475-18639_01_l.jpg','kind':'official_museum_image_attempt','error':'curl28 connection timeout45002ms; zero response body','headers':'data/raw/roof_trident_new_museum_image_headers.txt','response_body_retained':False},
 {'url':'https://museumsofindia.gov.in/cdn/portal_record/%5Bnat_del%5D/nat_del-DHR-24475-18639/nat_del-DHR-24475-18639_01_l.jpg','kind':'http404_html_response_not_image','path':'data/raw/roof_trident_new_museum_https_response.bin','headers':'data/raw/roof_trident_new_museum_https_headers.txt','status':404},
 {'url':'https://archive.org/download/dholavirareportpreliminaryjan2015_860_K/page/n302.jpg','kind':'archived_primary_report_page_image_with_original_artifact_photograph','path':'data/raw/roof_trident_new_report_leaf302_response.bin','headers':'data/raw/roof_trident_new_report_leaf302_headers.txt','status':200,'printed_page':286,'entry':119},
 {'url':'https://archive.org/download/dholavirareportpreliminaryjan2015_860_K/page/n263.jpg','kind':'archived_primary_report_table_page_image','path':'data/raw/roof_trident_new_report_leaf263_response.bin','headers':'data/raw/roof_trident_new_report_leaf263_headers.txt','status':200,'printed_page':247,'entry':8},
 {'url':'https://asi.nic.in/pdf/dholavira_excavation_report_cover.pdf','kind':'official_primary_report_cover_pdf_two_pages_not_full_report','path':'data/raw/roof_trident_new_cover_response.bin','headers':'data/raw/roof_trident_new_cover_headers.txt','status':200},
]
for x in extra:
 if not any(z['url']==x['url'] for z in a):a.append(x)
for x in a:
 if x.get('path'):x.update(pin(x['path']))
ledger.write_text(json.dumps(a,indent=2)+'\n')
sources=[]
for p in sorted((R/'data/raw').glob('roof_trident_new*')):
 x=pin(p); matching=next((z for z in a if z.get('path')==x['path'] or z.get('headers')==x['path']),None)
 if matching:
  x.update(url=matching['url'],kind='http_response_headers' if matching.get('headers')==x['path'] else matching['kind'])
  x['status']=matching.get('status')
 elif 'web_captures' in p.name:
  x.update(url='https://asi.nic.in/pdf/dholavira_excavation_report_cover.pdf',kind='web_tool_search_and_open_capture_not_original_documents',refetchable=False)
 else:raise AssertionError('untyped raw file '+str(p))
 sources.append(x)
reg={'status':'pending_parent_integration','sources':sources,'failed_fetches':[x for x in a if x.get('error')],'no_restriction_bypass':True}
(R/'data/processed/roof_trident_new_new_sources.json').write_text(json.dumps(reg,indent=2)+'\n')
keys=['id','cisi','site','excavation-idno','preservation','condition','complete','type','text']
with (R/'data/raw/lipi_inscriptions.csv').open() as f:rows=[{k:x[k] for k in keys} for x in csv.DictReader(f) if x['id'] in ['4196.1','5355.1']]
with (R/'data/raw/glossa_canonical_objects.jsonl').open() as f:moi=next(x for x in map(json.loads,f) if x.get('source_object_id')=='nat_del-DHR-24475-18639')
j={'scope':'bounded source-exposed primary photograph recovery, no corpus promotion','established_semantic_values':0,'established_phonetic_values':0,'secondary_candidate_rows':rows,'DHR24475':{'exact_primary_accession':'24475','primary_reference':'Bisht2015p286entry119','image_type':'colour photograph of seal face, not drawing','primary_exact_identity_authenticated':True,'roof_over_forked_stem_visible':True,'location_in_displayed_photo':'rightmost upper inscription group','apparent_inscription_groups':4,'all_secondary_token_ids_authenticated':False,'reading_direction_independently_established':False,'whole_field_extent':'apparently retained between surviving margins; no obvious missing end segment','every_stroke_preserved':None,'whole_field_completeness_certified':False,'damage':'surface abrasion and cracks; some strokes approach upper edge; photograph insufficient for complete stroke inventory','stage_table':{'reference':'Bisht2015p247row8','accession':'24475 NM','GSQ':'25x10x4','stratum':'6','depth_3DR':'A=470cm; D=980cm','motif':'Goat','inscription':None,'area':None,'stage':None},'museum_retained_record':moi,'motif_metadata_conflict':'primary stage table Goat versus retained museum title unicorn; unresolved, not used for sign inference','M163_global_mapping_established':False,'W391_local_graphic_comparison_only':True},'NausharoNs53':{'photograph_recovered':False,'primary_exact_identity_authenticated':None,'roof_over_forked_stem_visible':None,'whole_field_completeness':None,'outcome':'unresolved after bounded primary-source routes','primary_article':'Jarrige1996CRAI140(3)821–878 doi10.3406/crai.1996.15636; directPDF403','related_catalogue':'CISI3.2(2019)includesNausharo; fullscan not recovered'},'source_attempts':a,'limitations':['source-exposed local inspection, not held-out generalization','no meaning, phonetic value, chronology or productivity inferred','source complete labels not physical certification','museum metadata is retained API-derived record, not newly authenticated live museum photograph','initial error bodies and interrupted fullPDF partial buffer not retained'],'pins':[]}
files=[R/'scripts/persist_roof_trident_new_review.py',R/'data/raw/lipi_inscriptions.csv',R/'data/raw/glossa_canonical_objects.jsonl',ledger,R/'data/processed/roof_trident_new_new_sources.json',R/'data/processed/roof_trident_new_crop_manifest.json',R/'scripts/render_roof_trident_new_crops.py',R/'scripts/download_roof_trident_new_sources.py',R/'docs/ROOF_TRIDENT_NEW_ATTESTATIONS.md']+list((R/'data/raw').glob('roof_trident_new*'))+list((R/'results/primary_pages').glob('roof-trident-new*'))+list((R/'results').glob('roof-trident-new*_extraction.json'))
j['pins']=[pin(p) for p in sorted(set(files))]
(R/'data/processed/roof_trident_new_attestations.json').write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'pins':len(j['pins']),'new_raw_files':len(sources),'attempts':len(a)}))
