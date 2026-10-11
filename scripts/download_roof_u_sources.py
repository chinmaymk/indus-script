"""Download two publicly archived primary pages into the shared raw-data folder."""
from pathlib import Path
import json, hashlib, urllib.request, datetime
ROOT = Path(__file__).resolve().parents[1]
JOBS = [
 ('roof_u_mackay_leaf402.jpg', 'https://archive.org/download/in.gov.ignca.18225/page/n402.jpg'),
 ('roof_u_marshall_leaf199.jpg', 'https://archive.org/download/in.gov.ignca.48270/page/n199.jpg'),
]

def main():
    ledger = ROOT / 'data/processed/roof_u_new_sources.json'
    records = json.loads(ledger.read_text()) if ledger.exists() else {'downloads': []}
    for name, url in JOBS:
        path = ROOT / 'data/raw' / name
        previous = next((r for r in records['downloads'] if r['path'] == str(path.relative_to(ROOT))), None)
        if previous:
            assert hashlib.sha256(path.read_bytes()).hexdigest() == previous['sha256']
            continue
        assert not path.exists(), 'Refusing to overwrite unregistered source'
        with urllib.request.urlopen(url, timeout=120) as response:
            data = response.read(); resolved = response.url
        path.write_bytes(data)
        records['downloads'].append({'path':str(path.relative_to(ROOT)), 'url':url,
            'resolved_url':resolved, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        ledger.write_text(json.dumps(records,indent=2)+'\n')
        print(name,len(data))

if __name__ == '__main__': main()
