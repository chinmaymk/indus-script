"""Register retained inventory-method downloads and external-model opinion separately by kind."""
import json
from common import ROOT,sha256,write_json

def main():
 registry=json.loads((ROOT/'data/sources.json').read_text());rows=[]
 for p in sorted((ROOT/'data/processed').glob('fetch_inventory-oct10-*.json')):
  meta=json.loads(p.read_text())
  if 'path' in meta:
   rows.append({k:meta[k] for k in ['path','bytes','sha256','url','kind','http_status','response_complete'] if k in meta})
  if 'header_artifact' in meta:rows.append({**meta['header_artifact'],'url':meta['url']})
 for name,kind in [('inventory-oct10-web-capture.json','web_tool_capture_not_original_document'),('inventory-oct10-claude-fable.json','external_AI_CLI_response_not_historical_evidence')]:
  p=ROOT/'data/raw'/name;rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p),'url':None,'kind':kind,'refetchable':False,'original_document_bytes':False})
 groups=['downloads','web_extraction_captures','archived_http_responses'];known={r['path']:r for g in groups for r in registry[g]}
 for r in rows:
  p=ROOT/r['path'];assert p.stat().st_size==r['bytes'] and sha256(p)==r['sha256'],r['path']
  if r['path'] in known:
   assert known[r['path']]['sha256']==r['sha256'];continue
  kind=r['kind'].lower();g='archived_http_responses' if 'headers' in kind else 'web_extraction_captures' if 'web_tool' in kind else 'downloads'
  registry[g].append({**r,'research_date':'2026-10-10','source_registration_status':'registered'})
 write_json('data/sources.json',registry);write_json('data/processed/inventory_oct10_sources.json',{'sources':rows,'initial_discovery_response_not_serialized':True})
 print(len(rows),'source artifacts registered')
if __name__=='__main__':main()
