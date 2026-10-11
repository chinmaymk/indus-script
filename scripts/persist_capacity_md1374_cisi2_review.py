"""Reproduce two documentary crops and pin the manual CISI2 review; no network."""
from pathlib import Path
import hashlib,json,csv
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 crops=[]
 for source,size,box,target in [
  ('capacity-md1374-detail-474.png',(3223,4500),(1820,1100,2900,1255),'capacity-md1374-metadata-crop.png'),
  ('capacity-md1374-detail-215.png',(3189,4500),(170,2320,1390,3000),'capacity-md1374-photos-crop.png')]:
  source=ROOT/'results/primary_pages'/source;target=ROOT/'results/primary_pages'/target
  im=Image.open(source);assert im.size==size
  im.crop(box).save(target)
  crops.append({'source':pin(source),'output':pin(target),'box_xyxy':box,'operation':'rectangular native-resolution crop only'})
 capture=pin('data/raw/capacity_md1374_cisi2_web_capture.json')
 capture.update(kind='web_tool_search_and_open_capture_not_original_documents',url='https://www.academia.edu/8808307/VOLUMENMA%C3%9FE_VON_TONGEF%C3%84%C3%9FEN_DER_INDUSKULTUR',refetchable=False)
 registry={'status':'pending_parent_integration','sources':[capture],'original_document_downloads':[],'restricted_paths_retried':False}
 reg=ROOT/'data/processed/capacity_md1374_cisi2_new_sources.json';reg.write_text(json.dumps(registry,indent=2)+'\n')
 with (ROOT/'data/raw/lipi_inscriptions.csv').open() as f:
  row=next(x for x in csv.DictReader(f) if x['id']=='3672.1')
 keys=['id','cisi','site','area-section','excavation-idno','type','material','preservation','condition','complete','dir.','text']
 result={'scope':'primary CISI artifact authentication; explicit separation from unjoined capacity-vessel citation','established_semantic_values':0,'established_phonetic_values':0,
 'primary_metadata':{'printed_page':439,'pdf_page':474,'CISI':'M-1374','Finnish_Concordance':'2893','excavation_identifier':'UPM/MD-138','holding_code':'EXB','registration':'1381','photograph_source':'JL346'},
 'primary_key':{'printed_page':434,'pdf_page':469,'EXB':'Excavation Branch, Department of Archaeology and Museums, Government of Pakistan, Karachi','JL':'CISI project photograph','column2_is_Finnish_not_automatic_M77':True,'UPM_expansion_verified_in_this_key':False},
 'primary_photographs':{'printed_page':180,'pdf_page':215,'captions':['M-1374 A (1) (50 %)','M-1374 A (2)'],'page_heading':'MOHENJO-DARO 1372–1376 SEAL IMPRESSIONS on pots','physical_form':'broken rim/neck sherd with stamped inscription','whole_vessel_view_for_M1374':False,'neighbor_whole_vessels':['M-1372','M-1373'],'internal_profile_present_for_M1374':False,'graduated_metric_scale_present_for_M1374':False,'complete_stroke_inventory_authenticated':False,'counted_numeric_value':None},
 'secondary_candidate':{k:row[k] for k in keys},
 'Fuls_comparison':{'source_locator':'Section3.3,Figure7(a),citesDalesandKenoyer1986pp240–241','reported_label':'MD-1374','reported_form':'complete vessel','reported_height_cm':73,'reported_maximum_diameter_cm':69,'reported_marks':'three vertical plus three slanted marks','primary_profile_visually_verified':False,'explicit_link_to_CISI_M1374_or_UPM_MD138_found':False,'identity_established':False,'conclusion':'Do not join from integer1374. Complete-versus-fragmentary mismatch retained, without proving no possible historical relationship or refuting the intended-object capacity calculation.'},
 'new_capacity_computed':False,'new_sign_mapping_established':False,
 'attempts':[{'method':'local retained PDF','pages':[474,475,476,195,215,235,462,463,469],'outcome':'exact metadata/photo/key recovered; irrelevant navigation pages retained'}, {'method':'public web search','queries':['"Fuls" "1374" "138"','"UPM" "MD-138" pottery','"Volumenmaße" Fuls pdf','"Dales" "Kenoyer" "1986" "240" pottery','"MD-1374" pottery','site.harappa.com "Excavations at Mohenjo Daro" pottery'],'outcome':'No new exact artifact bridge or original target page. Author-posted extracted text corroborates attributed complete-vessel description.'}, {'method':'public author-posted manuscript web extraction','url':capture['url'],'outcome':'Section3.3andFigure7(a)captiontextavailable;figure not visually recovered. Reading/commodity proposals not adopted.'}],
 'restricted_source_retry_or_bypass':False,'crop_manifest':crops,'evidence_files':[]}
 files=[ROOT/'data/raw/h843_identity_CorpusVol2.pdf',ROOT/'data/raw/lipi_inscriptions.csv',ROOT/'data/raw/capacity_md1374_cisi2_web_capture.json',ROOT/'docs/MD1374_SOURCE_FOLLOWUP.md',ROOT/'data/processed/md1374_source_followup.json',ROOT/'data/processed/capacity_table_followup.json',ROOT/'docs/CAPACITY_MD1374_CISI2_REVIEW.md',reg,Path(__file__).resolve()]+list((ROOT/'results/primary_pages').glob('capacity-md1374*'))+list((ROOT/'results').glob('capacity-md1374*_extraction.json'))
 result['evidence_files']=[pin(p) for p in sorted(set(files))]
 (ROOT/'data/processed/capacity_md1374_cisi2_review.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'pins':len(result['evidence_files']),'crops':len(crops),'new_raw_files':1,'new_capacities':0}))
if __name__=='__main__':main()
