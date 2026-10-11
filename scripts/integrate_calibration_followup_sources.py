"""Register the new-route source search; preserve all acquisition kinds."""
import json
from common import ROOT, sha256, write_json


def main():
    manifests = ['umma_original_entry_new_sources.json', 'kotada_sample_photo_new_sources.json']
    registry = json.loads((ROOT/'data/sources.json').read_text())
    groups = ('downloads', 'web_extraction_captures', 'archived_http_responses')
    existing = {r['path']: r for g in groups for r in registry[g]}
    paths = set()
    for name in manifests:
        for row in json.loads((ROOT/'data/processed'/name).read_text())['sources']:
            rows = [{k:v for k,v in row.items() if k != 'header_artifact'}]
            if 'header_artifact' in row:
                rows.append({**row['header_artifact'], 'url': row.get('url')})
            for r in rows:
                p = ROOT/r['path']
                assert r['path'].startswith('data/raw/')
                assert p.stat().st_size == r['bytes'] and sha256(p) == r['sha256'], r['path']
                paths.add(r['path'])
                if r['path'] in existing:
                    assert existing[r['path']]['sha256'] == r['sha256']
                    continue
                kind = r.get('kind','').lower()
                group = 'archived_http_responses' if 'headers' in kind else 'web_extraction_captures' if 'web_tool' in kind else 'downloads'
                r = dict(r)
                if str(r.get('status','')).startswith('pending_parent'): r.pop('status')
                r['source_registration_status'] = 'registered'
                registry[group].append(r)
                existing[r['path']] = r
    write_json('data/sources.json', registry)
    write_json('results/calibration_followup_source_integration.json', {
        'registered_paths': sorted(paths), 'phase_artifacts': len(paths),
        'input_sha256': {f'data/processed/{p}': sha256(ROOT/'data/processed'/p) for p in manifests},
    })
    print(f'{len(paths)} new-route phase artifacts verified and registered.')


if __name__ == '__main__': main()
