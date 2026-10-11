"""Re-fetch version-pinned public research data; verify checksums before replacing files.

Uses curl for system TLS certificates. Never executes downloaded code.
"""
import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
from common import ROOT

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'data/sources.json').read_text())
    for item in manifest.get('archived_http_responses', []):
        path = ROOT / item['path']
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise SystemExit('Missing or changed archived response (not retried): ' + item['path'])
        print('verified archived response', item['path'])
    for item in manifest.get('web_extraction_captures', []):
        path = ROOT / item['path']
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise SystemExit('Missing or changed archived web extraction (not automatically re-fetched): ' + item['path'])
        print('verified archived web extraction', item['path'])
    for item in manifest['downloads']:
        dest = ROOT / item['path']
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest() == item['sha256']:
            print('verified', item['path'])
            continue
        if args.verify_only:
            raise SystemExit('Missing or changed: ' + item['path'])
        if item.get('refetchable') is False:
            raise SystemExit('Missing or changed session-dependent snapshot; restore retained bytes or repeat its documented public search: ' + item['path'])
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / 'download'
            subprocess.run(['curl', '-fsSL', '--max-time', str(item.get('timeout_seconds', 120)),
                            item['url'], '-o', str(tmp)], check=True)
            if hashlib.sha256(tmp.read_bytes()).hexdigest() != item['sha256']:
                raise SystemExit('Upstream checksum changed; refusing replacement: ' + item['url'])
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(tmp.read_bytes())
            print('downloaded and verified', item['path'])

if __name__ == '__main__':
    main()
