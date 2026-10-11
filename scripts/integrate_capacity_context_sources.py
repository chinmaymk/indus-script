"""Register the capacity follow-up's retained bytes without promoting error content."""
import json
from common import ROOT, sha256, write_json

def main():
    registry=json.loads((ROOT/'data/sources.json').read_text())
    entries=[]
    for leaf in (117,277,278,279,280,281):
        metadata=f'data/processed/fetch_capacity-context-vats-leaf{leaf}_jpg.json'
        row=json.loads((ROOT/metadata).read_text())
        assert row['response_complete'] and row['http_status']==200
        entries.append(('downloads',{k:row[k] for k in ('path','url','resolved_url','bytes','sha256','retrieval_started_utc','retrieval_ended_utc')}))
        entries[-1][1].update(kind='primary_Vats1940_volume1_page_JPEG_visually_reviewed',source_fetch_metadata=metadata)
        entries.append(('archived_http_responses',{**row['header_artifact'],'url':row['url'],'source_fetch_metadata':metadata}))
    for row in json.loads((ROOT/'data/processed/capacity_table_primary_downloads.json').read_text())['records']:
        kind=row['kind']
        group='archived_http_responses' if 'headers' in kind or 'error_body' in kind else 'web_extraction_captures' if 'web_tool' in kind else 'downloads'
        entries.append((group,row))
    for row in json.loads((ROOT/'data/processed/capacity_md1374_cisi2_new_sources.json').read_text())['sources']:
        entries.append(('web_extraction_captures',row))
    existing={r['path']:r for group in ('downloads','archived_http_responses','web_extraction_captures') for r in registry[group]}
    added=0
    for group,row in entries:
        p=ROOT/row['path']
        assert row['path'].startswith('data/raw/')
        assert p.stat().st_size==row['bytes'] and sha256(p)==row['sha256'],row['path']
        if row['path'] in existing:
            assert existing[row['path']]['sha256']==row['sha256']
            continue
        copied={k:v for k,v in row.items() if k!='pending_registration'}
        copied['registered_research_date']='2026-09-27'
        registry[group].append(copied);existing[row['path']]=copied;added+=1
    write_json('data/sources.json',registry)
    print(f'Registered {added} capacity follow-up artifacts.')

if __name__=='__main__':main()
