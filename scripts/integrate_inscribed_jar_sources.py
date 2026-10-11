"""Register preserved source responses from this fixed-table investigation."""
import json
from common import ROOT,sha256,write_json

def main():
    registry=json.loads((ROOT/'data/sources.json').read_text()); entries=[]
    for metadata in sorted((ROOT/'data/processed').glob('fetch_inscribed-*.json')):
        row=json.loads(metadata.read_text())
        if 'path' in row:
            group='downloads' if row.get('response_complete') and row.get('http_status')==200 else 'archived_http_responses'
            entries.append((group,{k:v for k,v in row.items() if k!='header_artifact'}))
            entries[-1][1]['source_fetch_metadata']=str(metadata.relative_to(ROOT))
            if group=='downloads':entries[-1][1]['kind']='primary_Vats1940_page_JPEG_retained_for_manual_review'
        if 'header_artifact' in row:
            entries.append(('archived_http_responses',{**row['header_artifact'],'url':row['url'],'source_fetch_metadata':str(metadata.relative_to(ROOT))}))
    for row in json.loads((ROOT/'data/processed/inscribed_jar_bridge_downloads.json').read_text())['records']:
        group='archived_http_responses' if 'headers' in row['kind'] or 'error' in row['kind'] else 'downloads'
        entries.append((group,{k:v for k,v in row.items() if k!='pending_registration'}))
    # The agent registry includes two fetch records already assembled above.
    entries=list({r['path']:(g,r) for g,r in entries}.values())
    groups=('downloads','web_extraction_captures','archived_http_responses')
    existing={r['path']:r for g in groups for r in registry[g]};added=0
    for group,row in entries:
        p=ROOT/row['path'];assert row['path'].startswith('data/raw/')
        assert sha256(p)==row['sha256'] and p.stat().st_size==row['bytes'],row['path']
        if row['path'] in existing:
            assert existing[row['path']]['sha256']==row['sha256'];continue
        registry[group].append(row);existing[row['path']]=row;added+=1
    write_json('data/sources.json',registry)
    duplicates={}
    for group,row in entries:
        if group=='downloads' and row['path'].endswith('.jpg'):duplicates.setdefault(row['sha256'],[]).append(row['path'])
    write_json('results/inscribed_jar_source_integration.json',dict(artifacts_in_phase=len(entries),
        duplicate_body_hash_groups=[v for v in duplicates.values() if len(v)>1],
        duplicate_policy='Keep each acquired response and its provenance; identical bodies are not independent evidence.',
        registered_paths=sorted(r['path'] for _,r in entries)))
    print(f'Registered {added} new source artifacts; retained repeated responses without treating them as independent observations.')

if __name__=='__main__':main()
