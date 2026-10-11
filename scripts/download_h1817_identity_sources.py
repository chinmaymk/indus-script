"""Bounded public Archive catalogue searches, retaining actual response bytes."""
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = []
for request in json.loads((ROOT / 'data/processed/h1817_identity_download_plan.json').read_text()):
    with urllib.request.urlopen(request['url'], timeout=45) as response:
        data = response.read()
    path = ROOT / 'data/raw' / request['filename']
    path.write_bytes(data)
    sources.append({'path': str(path.relative_to(ROOT)), 'url': request['url'],
                    'kind': 'public_archive_search_api_json_not_original_catalogue',
                    'query': request['query'], 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest()})
    parsed = json.loads(data)
    print(request['filename'], parsed.get('response', {}))
(ROOT / 'data/processed/h1817_identity_new_sources.json').write_text(json.dumps({'sources': sources}, indent=2) + '\n')
