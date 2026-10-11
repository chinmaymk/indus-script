"""Persist manual primary-table observations; no automatic readings or corpus edits."""
from pathlib import Path
import hashlib,json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def pin(path):
 p=ROOT/path if isinstance(path,str) else path
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 specs=[
 ('data/raw/inscribed-contents-vats-leaf282.jpg',(620,5120,5200,5500),'row35-left'),
 ('data/raw/inscribed-contents-vats-leaf283.jpg',(530,5080,5070,5500),'row35-right'),
 ('data/raw/inscribed-contents-vats-leaf292.jpg',(670,1190,5220,1980),'row116-left'),
 ('data/raw/inscribed-contents-vats-leaf293.jpg',(500,1160,5100,2010),'row116-right'),
 ('data/raw/inscribed-contents-vats-leaf293.jpg',(4180,1590,4890,2010),'row116-remarks'),
 ('data/raw/inscribed-contents-vats-leaf191.jpg',(820,2410,4540,3800),'narrative5919'),
 ('data/raw/capacity-context-vats-leaf279.jpg',(760,1850,4510,2790),'narrative-inscribed'),
 ('data/raw/capacity-context-vats-leaf281.jpg',(4200,5400,5100,5920),'row18-correction'),
 ('results/primary_pages/capacity-context-vats-plate-correct-58.png',(80,3020,1570,4170),'plateXXIIIe-correction'),
 ('results/primary_pages/capacity-context-vats-plate-correct-58.png',(210,2720,1300,3040),'plateXXIIIc-comparator')]
 crops=[]
 for source,box,name in specs:
  target=f'results/primary_pages/inscribed-contents-{name}.png'
  Image.open(ROOT/source).crop(box).save(ROOT/target)
  crops.append({'source':source,'box_xyxy':box,'operation':'native rectangular crop only','output':pin(target)})
 rows=[
 {'row':35,'register':'5919','table_pages':[256,257],'mound':'AB','trench_raw':'Ex. P. I & II','square_table':'P23/10','depth':'10 ft','stratum':'IV','measurements':None,'measurements_raw':'dotted blank','description':'Large, inscribed napiform','inscribed_reported':True,'inscription_lines':None,'inscription_pictograms':None,
 'contents':{'bones':'Several, including a few charred pieces of large bones','pointed_base_goblets':None,'other_pottery':None,'toys':"1 bull's head and fragment of a wheel",'cakes':'Fragments of 7 or 8','potsherds':"Of an offerings’ dish, perforated vase, cylindrical, round and oval vases",'ornaments':'Fragments of bangles','charcoal':'Tiny pieces of charcoal','shell':'1 river shell was found inside a fragmentary oval vase','miscellaneous':'One chert scraper and some slag'},
 'remarks':'The lower 4/5th of this jar contained porous, greenish earth mixed with some decayed cereal and bore leafy impressions.',
 'narrative_page165':{'condition':'crushed','depth':'10 ft','square':'P23/5','earth_extent':'up to four-fifths of its height','earth_contents':'porous earth mixed with some decayed cereal on which were impressions of leaves'},'square_conflict_unresolved':True},
 {'row':116,'register':'10252','table_pages':[266,267],'mound':'F','trench_raw':'IV','square_table':'I12/4','depth':'9 ft','stratum':'IV','measurements':None,'measurements_raw':'dotted blank','description':'Round, in pieces','inscribed_reported':True,'inscription_lines':2,'inscription_pictograms':7,
 'contents':{'bones':'Several','pointed_base_goblets':None,'other_pottery':'1 oval vase with long neck and 1 small squat vase','toys':'1 wheel','cakes':'Several fragments','potsherds':'Of a basin, of goblets with pointed bases, tumblers, perforated vases, jars, dishes, etc.','ornaments':'2 pieces of bangles','charcoal':'Bits of charcoal','shell':'2 small pieces of river shell','miscellaneous':'Traces of decayed cereal and some slag. A discoid faience sealing lentoid in section (Pl. C, 671).'},
 'remarks':'The earth in the jar was porous and contained traces of decayed cereal. Chaff, straw, melon seeds and leaf impressions. The jar is inscribed in 2 lines with 7 pictograms.',
 'contained_sealing':{'plate':'C','figure':671,'distinct_from_jar_inscription':True,'temporal_link_to_inscription_established':False},'jar_inscription_illustration_reference_in_row':None}]
 registry=[]; attempts=[]
 for leaf in [191,282,283,290,292,293]:
  ledger=f'data/processed/fetch_inscribed-contents-vats-leaf{leaf}_jpg.json'
  r=json.loads((ROOT/ledger).read_text()); attempts.append({'ledger':pin(ledger),'url':r['url'],'response_complete':r['response_complete'],'http_status':r['http_status'],'purpose':'navigation only' if leaf==290 else 'primary narrative/table inspection','duplicate_parallel_capture':leaf in [191,293]})
  for key,kind in [(None,'primary_report_printed_page_JPEG_not_artifact_photograph'),('header_artifact','locally_serialized_HTTP_response_headers')]:
   item=r if key is None else r[key]
   registry.append({**pin(item['path']),'kind':kind,'url':r['url'],'resolved_url':r['resolved_url'],'response_complete':r['response_complete'],'http_status':r['http_status'],'duplicate_parallel_capture':leaf in [191,293]})
 pending='data/processed/inscribed_jar_contents_new_sources.json'
 (ROOT/pending).write_text(json.dumps({'status':'pending_parent_integration','sources':registry,'attempts':attempts,'all_response_bodies_and_headers_preserved':True,'duplicate_captures_not_independent_evidence':True},indent=2)+'\n')
 result={'scope':'selected primary-source contents/inscription co-report review, not exhaustive or statistical inventory','established_semantic_values':0,'established_phonetic_values':0,'all_417_values_remain_null':True,'rows':rows,
 'rules':['Dotted blank is null, not zero or ditto.','No neighboring dimensions or contents are transferred.','The separately contained sealing is not the jar inscription.','No temporal link between inscription and deposition is established.','No capacity or original commodity is inferred.'],
 'new_correction_layer':{'prior_review':'data/processed/capacity_context_independent_review.json','prior_files_unchanged':True,'row':18,'register':'3822','field':'remarks.plate','prior':'XXIII,c','corrected':'XXIII,e','basis':'Small printed letter reinspected; panel e caption is inscribed jar and stands, Stratum VI, M12/6; panel c is hearths/mangers M12/19.','glyph_transcription_established':False},
 'crop_manifest':crops,'retrieval_attempts':attempts,'evidence_files':[]}
 files=[x['path'] for x in registry]+[x['ledger']['path'] for x in attempts]+[x['source'] for x in crops]+[x['output']['path'] for x in crops]+[pending,'data/raw/vats_1940_text_18220_djvu.txt','data/raw/vats_1940_plates_9842.pdf','data/processed/capacity_context_independent_review.json','docs/CAPACITY_CONTEXT_INDEPENDENT_REVIEW.md','docs/INSCRIBED_JAR_CONTENTS_REVIEW.md',str(Path(__file__).resolve().relative_to(ROOT))]
 result['evidence_files']=[pin(p) for p in sorted(set(files))]
 out=ROOT/'data/processed/inscribed_jar_contents_review.json';out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 assert all(pin(p['path'])==p for p in result['evidence_files'])
 print(json.dumps({'review':str(out.relative_to(ROOT)),'pins':len(result['evidence_files']),'new_source_artifacts':len(registry),'crops':len(crops)}))
if __name__=='__main__':main()
