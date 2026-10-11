"""Register the completed October10 primary-source acquisition without changing readings."""
import json
from common import ROOT,sha256,write_json

def main():
 rows=[]
 for name in ['oct10_h1923_new_sources.json','oct10_route_new_sources.json','comparative_numerals_oct10_new_sources.json']:
  rows+=json.loads((ROOT/'data/processed'/name).read_text())['sources']
 for p in sorted((ROOT/'data/processed').glob('fetch_oct10-chanhu-*.json')):
  r=json.loads(p.read_text())
  if 'path' in r:
   rows.append({k:r[k] for k in ('path','bytes','sha256','url','kind','http_status','response_complete') if k in r})
  if 'header_artifact' in r:rows.append({**r['header_artifact'],'url':r['url']})
 for name in ['oct10-chanhu-web-capture.json','oct10-chanhu-web-followup.json']:
  p=ROOT/'data/raw'/name
  rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p),'url':None,'kind':'web_tool_capture_not_original_document','refetchable':False})
 for name in ['claude-opus-oct10-method-review.json','claude-opus-oct10-method-review-retry.json']:
  p=ROOT/'data/raw'/name
  if p.exists():
   rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p),'url':None,'kind':'external_AI_CLI_response_not_historical_evidence','refetchable':False,'original_document_bytes':False})
 registry=json.loads((ROOT/'data/sources.json').read_text());groups=('downloads','web_extraction_captures','archived_http_responses')
 known={r['path']:r for g in groups for r in registry[g]}
 for r in rows:
  p=ROOT/r['path'];assert p.stat().st_size==r['bytes'] and sha256(p)==r['sha256'],r['path']
  if r['path'] in known:
   assert known[r['path']]['sha256']==r['sha256'];continue
  kind=r['kind'].lower();group='archived_http_responses' if 'headers' in kind else 'web_extraction_captures' if 'web_tool' in kind else 'downloads'
  registry[group].append({**r,'research_date':'2026-10-10','source_registration_status':'registered'})
 write_json('data/sources.json',registry)
 write_json('results/oct10_source_integration.json',{'phase_sources':len(rows),'sources':rows,'semantic_values_assigned':0})
 print(f'{len(rows)} October10 source artifacts registered and verified.')
if __name__=='__main__':main()
