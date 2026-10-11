"""Register the bounded Fuls figure follow-up, including retained error bodies."""
import json
from common import ROOT, sha256, write_json


def main():
    source = 'data/processed/fuls_numeral_figure_new_sources.json'
    rows = json.loads((ROOT/source).read_text())['sources']
    registry = json.loads((ROOT/'data/sources.json').read_text())
    groups = ('downloads','web_extraction_captures','archived_http_responses')
    existing = {r['path']:r for g in groups for r in registry[g]}
    for row in rows:
        p = ROOT/row['path']
        assert row['path'].startswith('data/raw/')
        assert p.stat().st_size == row['bytes'] and sha256(p) == row['sha256']
        if row['path'] in existing:
            assert existing[row['path']]['sha256'] == row['sha256']
            continue
        kind = row.get('kind','').lower()
        group = 'archived_http_responses' if 'headers' in kind else 'web_extraction_captures' if 'web_tool' in kind else 'downloads'
        registry[group].append({**row,'source_registration_status':'registered'})
    write_json('data/sources.json',registry)
    write_json('results/numeral_identity_source_integration.json',{
        'phase_artifacts':len(rows),'registered_paths':sorted(r['path'] for r in rows),
        'input_sha256':{source:sha256(ROOT/source)},
    })
    print(f'{len(rows)} Fuls follow-up source artifacts registered and verified.')


if __name__=='__main__':main()
