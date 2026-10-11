"""Register the bounded deposit phase's retained sources with original byte pins."""
import json
from common import ROOT, sha256, write_json


def main():
    manifests = ['chanhu_methods_new_sources.json', 'chanhu_deposit_new_sources.json',
                 'chanhu_deposit_register_downloads.json', 'chanhu_fieldcard_archive_new_sources.json']
    registry = json.loads((ROOT/'data/sources.json').read_text())
    groups = ('downloads', 'web_extraction_captures', 'archived_http_responses')
    existing = {r['path']: r for group in groups for r in registry[group]}
    entries = []
    for name in manifests:
        data = json.loads((ROOT/'data/processed'/name).read_text())
        for row in data['sources']:
            entries.append({k: v for k, v in row.items() if k != 'header_artifact'})
            if 'header_artifact' in row:
                entries.append({**row['header_artifact'], 'url': row['url']})
    added = 0
    for row in entries:
        path = ROOT/row['path']
        assert row['path'].startswith('data/raw/')
        assert path.stat().st_size == row['bytes'] and sha256(path) == row['sha256'], row['path']
        if row['path'] in existing:
            assert existing[row['path']]['sha256'] == row['sha256']
            continue
        kind = row.get('kind', '')
        group = ('archived_http_responses' if 'headers' in kind else
                 'web_extraction_captures' if 'web_tool' in kind else 'downloads')
        clean = dict(row)
        if clean.get('status') == 'pending_parent_registration':
            clean.pop('status')
        clean['source_registration_status'] = 'registered'
        registry[group].append(clean)
        existing[row['path']] = clean
        added += 1
    write_json('data/sources.json', registry)
    write_json('results/chanhu_deposit_source_integration.json', {
        'registered_paths': sorted({r['path'] for r in entries}),
        'phase_artifacts': len({r['path'] for r in entries}),
        'scope': 'Downloaded pages and finding aids, serialized headers and web-tool captures; no original field cards.',
        'input_sha256': {f'data/processed/{p}': sha256(ROOT/'data/processed'/p) for p in manifests},
    })
    print(f'Registered {added} new source artifacts; {len(entries)} phase records verified.')


if __name__ == '__main__':
    main()
