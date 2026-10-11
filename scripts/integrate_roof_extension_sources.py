"""Idempotently register the retained roof-extension downloads and failed-response artifacts."""
import json
from common import ROOT,sha256,write_json

def main():
 registry=json.loads((ROOT/'data/sources.json').read_text())
 entries=[('downloads',r) for r in json.loads((ROOT/'data/processed/roof_u_new_sources.json').read_text())['downloads']]
 for row in json.loads((ROOT/'data/processed/roof_trident_new_new_sources.json').read_text())['sources']:
  kind=row['kind']
  group='web_extraction_captures' if kind.startswith('web_tool') else 'archived_http_responses' if kind=='http_response_headers' or kind.startswith('http404') else 'downloads'
  entries.append((group,row))
 existing={r['path']:r for group in ('downloads','archived_http_responses','web_extraction_captures') for r in registry[group]}
 added=0
 for group,row in entries:
  p=ROOT/row['path']
  assert row['path'].startswith('data/raw/')
  assert p.stat().st_size==row['bytes'] and sha256(p)==row['sha256'],row['path']
  if row['path'] in existing:
   assert existing[row['path']]['sha256']==row['sha256']
   continue
  copied={**row,'registered_research_date':'2026-09-27'}
  if row['bytes']==0:
   copied['notes']='Empty local header placeholder from timed-out request; no server response bytes or research content received.'
  registry[group].append(copied);existing[row['path']]=copied;added+=1
 write_json('data/sources.json',registry)
 print(f'Registered {added} new retained raw artifacts; classified bodies, captures and headers separately.')

if __name__=='__main__':main()
