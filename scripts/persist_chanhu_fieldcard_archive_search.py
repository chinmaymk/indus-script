"""Pin official archive-discovery evidence; do not infer unseen fieldcard contents."""
from pathlib import Path
from html.parser import HTMLParser
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
class Page(HTMLParser):
 def __init__(self):super().__init__();self.words=[];self.links=[]
 def handle_data(self,s):self.words.append(s)
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.links.append(dict(attrs).get('href',''))
def main():
 specs=[('chanhu-fieldcards-penn1064.html','official_archival_finding_aid_HTML_not_fieldcard_images'),('chanhu-fieldcards-brown-findingaid.html','official_related_archival_finding_aid_HTML_not_field_reports'),('chanhu-fieldcards-mfa-access.html','official_current_archive_access_notice_HTML')]
 entries=[];ledgers=[]
 for filename,kind in specs:
  ledger=f'data/processed/fetch_{filename.replace(".","_")}.json';r=json.loads((ROOT/ledger).read_text());ledgers.append(pin(ledger))
  for obj,k in [(r,kind),(r['header_artifact'],'locally_serialized_HTTP_response_headers')]:
   entries.append({**pin(obj['path']),'kind':k,'url':r['url'],'resolved_url':r['resolved_url'],'http_status':r['http_status'],'response_complete':r['response_complete']})
 capture='data/raw/chanhu-fieldcards-web-capture.json';entries.append({**pin(capture),'kind':'web_tool_search_open_error_capture_with_partial_initial_batch_log_not_original_field_records','refetchable':False})
 pending='data/processed/chanhu_fieldcard_archive_new_sources.json';(ROOT/pending).write_text(json.dumps({'status':'pending_parent_integration','sources':entries,'retrieval_ledgers':ledgers},indent=2)+'\n')
 page=Page();page.feed((ROOT/'data/raw/chanhu-fieldcards-penn1064.html').read_text());text=' '.join(' '.join(page.words).split())
 ranges=[(5,1,575),(6,576,1157),(7,1158,1730),(8,1731,2288),(9,2289,2726),(10,2727,3280),(11,3281,3810),(12,3811,4361),(13,4362,4904),(14,4905,5457)]
 checks={f'box{b}range':f'Object card catalog {lo}-{hi}. Box {b}' in text for b,lo,hi in ranges}
 for s in ['Field Notebooks 1935-1936. Box 2','Original Register 1935-1936 (1 of 3). Box 2','Original Register 1935-1936 (2 of 3). Box 2','Original Register 1935-1936 (3 of 3). Box 2','Register Copy 1935-1936 (1 of 2). Box 2','Register Copy 1935-1936 (2 of 2). Box 2']:checks[s]=s in text
 assert all(checks.values()),checks
 candidates=[]
 for s in ['2285','2297','2428','2529cc','2558','3215','3811','4852']:
  num=int(''.join(x for x in s if x.isdigit()));box=next(b for b,lo,hi in ranges if lo<=num<=hi)
  candidates.append({'excavation_label':s,'candidate_box_from_numeric_range':box,'individual_card_presence_verified':False,'suffix_handling_verified':False if any(c.isalpha() for c in s) else None})
 r={'scope':'five-query bounded official archive discovery, no outreach or card inspection','date':'2026-09-28','search_queries_total':5,'archive_located':True,'catalogued_holding':{'repository':'Penn Museum Archives','title':'Chanhu-daro Pakistan records','call_number':'1064','url':'https://findingaids.library.upenn.edu/records/UPENN_MUSEUM_PU-MU.1064','field_notebooks_and_site_levels':'Box2; scope describes site-level notebooks','original_register_parts':{'box':2,'parts':3},'register_copy_parts':{'box':2,'parts':2},'card_catalogue_ranges':[{'box':b,'lower':lo,'upper':hi} for b,lo,hi in ranges],'range_endpoint_is_not_verified_card_count':True},'candidate_locators':candidates,'access':{'finding_aid_public':True,'underlying_records_default':'physically available in reading room, not digitally available through web unless otherwise noted','public_card_image_link_located':False,'direct_penn_access_web_error':'403','repository_index_web_error':'400 Timeout fetching','current_penn_appointment_rules_verified':False,'mfa_notice':'libraries and archives temporarily unavailable for appointments and research requests','no_outreach':True},'related_Brown_papers':{'collection':'UPT50B879','field_reports':'box6 folders10–12','url':'https://archives.upenn.edu/collections/finding-aid/upt50b879/'},'known_limits':['Individual cards not inspected.','No completeness claim or exact equality with preface card inventory.','Access errors not evidence of destruction or closure.','Supersedes historical archive-not-located state in new layer; frozen review unchanged.'],'parsed_catalogue_checks':checks,'finding_aid_outgoing_links':page.links,'new_raw_artifact_count':len(entries),'established_semantic_values':0,'established_phonetic_values':0,'evidence_files':[]}
 paths=[e['path'] for e in entries]+[p['path'] for p in ledgers]+[pending,'docs/CHANHU_FIELDCARD_ARCHIVE_SEARCH.md','data/processed/chanhu_recording_method_review.json','data/raw/chanhu-methods-leaf10.jpg','data/raw/chanhu-methods-leaf11.jpg',str(Path(__file__).resolve().relative_to(ROOT))]
 r['evidence_files']=[pin(p) for p in sorted(set(paths))];out=ROOT/'data/processed/chanhu_fieldcard_archive_search.json';out.write_text(json.dumps(r,indent=2)+'\n')
 assert all(pin(p['path'])==p for p in r['evidence_files'])
 print(json.dumps({'review':str(out.relative_to(ROOT)),'pins':len(r['evidence_files']),'new_raw_files':len(entries),'archive_located':True}))
if __name__=='__main__':main()
