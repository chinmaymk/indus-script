"""Register this external-anchor phase's source artifacts without altering bytes."""
import json
from common import ROOT, sha256, write_json


def main():
    manifests = [
        'chanhu_public_records_new_sources.json',
        'new_external_anchor_downloads.json',
        'inscribed_weight_anchor_new_sources.json',
        'umma_renewed_new_sources.json',
        'kotada_anchor_followup_new_sources.json',
    ]
    registry = json.loads((ROOT/'data/sources.json').read_text())
    groups = ('downloads', 'web_extraction_captures', 'archived_http_responses')
    existing = {r['path']: r for g in groups for r in registry[g]}
    entries = []
    for name in manifests:
        for row in json.loads((ROOT/'data/processed'/name).read_text())['sources']:
            entries.append({k: v for k, v in row.items() if k != 'header_artifact'})
            if 'header_artifact' in row:
                entries.append({**row['header_artifact'], 'url': row.get('url')})
    added = 0
    for row in entries:
        path = ROOT/row['path']
        assert row['path'].startswith('data/raw/')
        assert path.stat().st_size == row['bytes'] and sha256(path) == row['sha256'], row['path']
        if row['path'] in existing:
            assert existing[row['path']]['sha256'] == row['sha256']
            continue
        kind = row.get('kind', '').lower()
        group = ('archived_http_responses' if 'headers' in kind else
                 'web_extraction_captures' if 'web_tool' in kind else 'downloads')
        clean = dict(row)
        if str(clean.get('status', '')).startswith('pending_parent'):
            clean.pop('status')
        clean['source_registration_status'] = 'registered'
        registry[group].append(clean)
        existing[row['path']] = clean
        added += 1
    write_json('data/sources.json', registry)
    write_json('results/external_anchor_source_integration.json', {
        'registered_paths': sorted({r['path'] for r in entries}),
        'phase_artifacts': len({r['path'] for r in entries}),
        'scope': 'Public sources, serialized headers and web-tool captures; no outreach or new semantic assignments.',
        'input_sha256': {f'data/processed/{p}': sha256(ROOT/'data/processed'/p) for p in manifests},
    })
    print(f'Registered {added} new artifacts; {len(entries)} phase records verified.')


if __name__ == '__main__':
    main()
