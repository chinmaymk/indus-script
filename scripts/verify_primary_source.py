"""Check primary downloads against the Internet Archive metadata snapshot."""
import hashlib
import json
from urllib.parse import unquote
from common import ROOT,write_json

def main():
    meta=json.loads((ROOT/'data/raw/mahadevan_archive_metadata.json').read_text())
    files={f['name']:f for f in meta['files']}
    sources=json.loads((ROOT/'data/sources.json').read_text())
    checks=[]
    for entry in sources['downloads']:
        # Retained local derivatives have parent-file provenance and no network URL.
        url=entry.get('url')
        if not isinstance(url,str) or '/download/TheIndusScript.' not in url:
            continue
        name=unquote(url.rsplit('/',1)[1]);record=files[name];path=ROOT/entry['path']
        actual=hashlib.md5(path.read_bytes()).hexdigest()
        checks.append({'path':entry['path'],'archive_name':name,'archive_md5':record.get('md5'),
            'actual_md5':actual,'md5_matches':actual==record.get('md5'),
            'archive_bytes':int(record['size']),'actual_bytes':path.stat().st_size,
            'size_matches':int(record['size'])==path.stat().st_size})
    write_json('results/primary_archive_integrity.json',{'checks':checks,
        'scope':'Integrity against archived metadata; does not establish editorial accuracy or ownership.'})
    if len(checks)!=4 or not all(c['md5_matches'] and c['size_matches'] for c in checks):
        raise SystemExit('Primary archive integrity check failed')
    print('Four primary downloads match archive sizes and MD5 checksums.')

if __name__=='__main__':
    main()
