"""Preserve bounded manual table review plus reproducible text-only locator attempts."""
from pathlib import Path
import csv,hashlib,json,re
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 specs=[('296','jar156165',(530,1570,5150,1880),'156-left'),('296','jar156165',(530,3730,5150,4030),'165-left'),('297','inscribed-frame',(570,1600,5190,1820),'156-right'),('297','inscribed-frame',(570,3730,5190,3950),'165-right'),('296','jar156165',(2850,3070,3500,4040),'description-ditto-chain')]
 crops=[]
 for leaf,prefix,box,name in specs:
  src=f'data/raw/{prefix}-vats-leaf{leaf}.jpg';dst=f'results/primary_pages/jar156165-{name}.png'
  Image.open(ROOT/src).crop(box).save(ROOT/dst)
  crops.append({'source':pin(src),'box_xyxy':box,'operation':'native rectangular crop only','output':pin(dst)})
 queries={'container_number':r'(?<!\d)7737(?!\d)','row156_grid':r'Q\s*24\s*[/.,]\s*18','row165_grid':r'I\s*9\s*[/.,]\s*5','four_strokes':r'four\s+(?:vertical|upright)\s+(?:strokes|incisions)','goblet_incised_same_line':r'goblet[^\n]{0,80}(?:incis|stroke)|incis[^\n]{0,80}goblet'}
 files=[ROOT/'data/raw/vats_1940_text_18220_djvu.txt',ROOT/'results/cisi1_extracted.txt',ROOT/'results/h843-cisi2_extracted.txt',ROOT/'results/iconography-mahadevan_extracted.txt']
 files+=sorted(p for p in (ROOT/'results/primary_pages').glob('*.txt') if 'cisi' in p.name or 'm77' in p.name)
 search=[]
 for f in sorted(set(files)):
  txt=f.read_text(errors='replace');hits=[]
  for label,pat in queries.items():
   for m in re.finditer(pat,txt,re.I):
    hits.append({'query':label,'line':txt.count('\n',0,m.start())+1,'excerpt':txt[max(0,m.start()-100):m.end()+180]})
  search.append({'file':pin(f),'hits':hits})
 keys=['id','cisi','site','area-section','block-house','room-grid','excavation-idno','depth','type','preservation']
 csv_hits=[];harappa_rows=0
 for r in csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open()):
  if r['site']!='Harappa':continue
  harappa_rows+=1;reason=[]
  if re.search(queries['container_number'],r['excavation-idno']):reason.append('container-number locator only')
  if any(re.sub(r'[^a-z0-9]','',r[k].lower()) in ['q2418','i95'] for k in ['area-section','block-house','room-grid']):reason.append('grid locator only')
  if reason:csv_hits.append({'reason':reason,**{k:r[k] for k in keys}})
 rows=[{'row':156,'container_register':None,'container_register_raw':'dotted blank','mound':'AB','trench_raw':'Ex. P. I & II','square':'Q24/18','depth':'5 ft 3 in','stratum':'II','description':'Very fragmentary','measurements':None,'contained_marked_object':{'description':'Fragment of a unicorn seal','separate_register':None,'plate':None,'surviving_script_reported':None,'pictogram_count':None,'photo_authenticated':False,'cisi_alias':None,'m77_text':None},'other_contents':{'toys':'1 ram','potsherds':'Of a tumbler and of a dish','charcoal':'Some pieces of charcoal','bones_numeric_weight':None},'container_inscribed_reported':None},
 {'row':165,'container_register':'7737','mound':'F','trench_raw':'G. G. Area','square':'I9/5','depth':'3 ft 4 in','stratum':'II','description':{'raw':'Do.','antecedent_row':162,'intermediate_dittos':[163,164],'resolved':'Very fragmentary'},'measurements':None,'contained_marked_object':{'description':'One of three goblets with pointed bases','reported_vertical_strokes':4,'incised_reported':True,'ancient_numeric_value':None,'indus_sign_identity':None,'separate_register':None,'plate':None,'photo_authenticated':False,'cisi_alias':None,'m77_text':None,'marking_relative_to_firing':None,'marking_relative_to_jar_deposition':None},'other_contents':{'bones_reported_count':3,'pointed_base_goblets_reported_count':3,'ornaments':'1 small discoid paste bead'},'remarks':'One of the goblets had a series of four vertical strokes incised on it.','container_inscribed_reported':None}]
 ledger='data/processed/fetch_jar156165-vats-leaf296_jpg.json';r=json.loads((ROOT/ledger).read_text())
 sources=[{**pin(r['path']),'kind':'primary_report_printed_table_page_JPEG_not_contained_artifact_photograph','url':r['url'],'resolved_url':r['resolved_url'],'http_status':r['http_status'],'response_complete':r['response_complete']},{**pin(r['header_artifact']['path']),'kind':'locally_serialized_HTTP_response_headers','url':r['url']}]
 pending='data/processed/jar156_165_new_sources.json';(ROOT/pending).write_text(json.dumps({'status':'pending_parent_integration','sources':sources,'retrieval_ledger':pin(ledger),'all_response_bytes_retained':True},indent=2)+'\n')
 out={'scope':'bounded primary table review and locator follow-up, no complete corpus absence claim','established_semantic_values':0,'established_phonetic_values':0,'all_417_values_remain_null':True,'rows':rows,'source_pages':[270,271],'crop_manifest':crops,'search_protocol':{'queries':queries,'text_coverage':'retained partial CISI/M77 extracts and existing page OCR; Vats retained whole-volume OCR; not full visual corpus review','negative_search_limit':'OCR misses known visible table statements; no illustration absence conclusion','lipi_columns':keys,'translation_columns_read_or_used':False},'locator_results':search,'lipi_metadata_screen':{'Harappa_rows':harappa_rows,'hits':csv_hits},'rejected_locators':[{'locator':'Vats OCR I9/5 dog7071,figurine55','reason':'different object and depth3ft2in; no goblet/container link'},{'locator':'Vats OCR AreaG p195 goblet and incised ivory baluster','reason':'incised description belongs to ivory object in another context'},{'locator':'Vats OCR contents heading stamped goblets/incised inscriptions','reason':'generic topic heading, not object identity'},{'locator':'Vats OCR narrative Q24/18 copper rod2551','reason':'wrong object and depth10ft6in; row156depth5ft3in'},{'locator':'Vats p251 jar12414,PlateLXXXVII47 unicorn seal','reason':'different container and location; no explicit link to row156'},{'locator':'Vats pp286–287 general incised-pottery discussion and platesCII–CIV','reason':'no explicit row165container7737 or contained-goblet identification recovered'}],'outcome':'No explicit marked-contained-object photograph/CISI/M77 bridge authenticated; source graphic count4 on one goblet remains descriptive only.','evidence_files':[]}
 paths=[str(p.relative_to(ROOT)) for p in files]+[c['source']['path'] for c in crops]+[c['output']['path'] for c in crops]+[s['path'] for s in sources]+[ledger,pending,'data/raw/lipi_inscriptions.csv','docs/JAR156_165_CONTAINED_MARKS_REVIEW.md',str(Path(__file__).resolve().relative_to(ROOT))]
 out['evidence_files']=[pin(p) for p in sorted(set(paths))]
 dst=ROOT/'data/processed/jar156_165_contained_marks_review.json';dst.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
 assert all(pin(p['path'])==p for p in out['evidence_files'])
 print(json.dumps({'review':str(dst.relative_to(ROOT)),'pins':len(out['evidence_files']),'text_files_searched':len(search),'text_hits':sum(len(x['hits']) for x in search),'lipi_hits':len(csv_hits),'new_raw_files':len(sources)}))
if __name__=='__main__':main()
