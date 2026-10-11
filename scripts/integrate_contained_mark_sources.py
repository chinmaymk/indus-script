"""Register all successful bodies and header artifacts, preserving no-body failures."""
import json
from common import ROOT,sha256,write_json

def main():
    registry=json.loads((ROOT/'data/sources.json').read_text());entries=[];failures=[]
    for row in json.loads((ROOT/'data/processed/jar54_new_sources.json').read_text())['sources']:
        if 'path' in row:entries.append({k:v for k,v in row.items() if k!='header_artifact'})
        else:failures.append(row)
        if 'header_artifact' in row:entries.append({**row['header_artifact'],'url':row['url']})
    for filename,key in [('jar156_165_new_sources.json','sources'),('vats_pottery_text_downloads.json','records')]:
        entries+=json.loads((ROOT/'data/processed'/filename).read_text())[key]
    groups=('downloads','web_extraction_captures','archived_http_responses')
    existing={r['path']:r for group in groups for r in registry[group]};added=0
    for row in entries:
        path=ROOT/row['path'];assert row['path'].startswith('data/raw/')
        assert path.stat().st_size==row['bytes'] and sha256(path)==row['sha256'],row['path']
        if row['path'] in existing:
            assert existing[row['path']]['sha256']==row['sha256'];continue
        group='archived_http_responses' if 'headers' in row['kind'] else 'downloads'
        clean={k:v for k,v in row.items() if k!='pending_registration'}
        registry[group].append(clean);existing[row['path']]=clean;added+=1
    write_json('data/sources.json',registry)
    write_json('results/contained_mark_source_integration.json',dict(retained_artifacts=len(entries),
        registered_paths=sorted(r['path'] for r in entries),no_body_failures=failures,
        scope='Network responses and local derivatives retain distinct kinds; no-body failures are attempts, not downloaded evidence.'))
    print(f'Registered {added} source artifacts; preserved {len(failures)} no-body failure records.')

if __name__=='__main__':main()
