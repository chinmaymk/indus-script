import json,sys,hashlib
from pathlib import Path
root=Path('/Users/chinmaymk/github/indus-script');sys.path.insert(0,str(root/'scripts'))
from common import sha256,write_json
# Preserve the exact historical log reviewed by the route agent before appending.
audit=json.loads((root/'data/processed/research_route_audit.json').read_text())
pin=next(p for p in audit['source_pins'] if p['path']=='docs/RESEARCH_LOG.md')
snapshot='results/research_route_audit_log_input.md'
if not (root/snapshot).exists():
    assert sha256(root/pin['path'])==pin['sha256']
    (root/snapshot).write_bytes((root/pin['path']).read_bytes())
assert sha256(root/snapshot)==pin['sha256']
registry=json.loads((root/'data/sources.json').read_text())
rows=json.loads((root/'data/processed/h1923_report_new_sources.json').read_text())['sources']
existing={r['path']:r for g in ('downloads','web_extraction_captures','archived_http_responses') for r in registry[g]}
for row in rows:
    assert sha256(root/row['path'])==row['sha256'] and (root/row['path']).stat().st_size==row['bytes']
    if row['path'] not in existing: registry['web_extraction_captures'].append({**row,'source_registration_status':'registered'})
write_json('data/sources.json',registry)
p=root/'scripts/run_all.py';s=p.read_text();needle="      ['scripts/write_manifest.py']]"
if "['scripts/audit_convergence.py']" not in s:
    s=s.replace(needle,"      ['scripts/analyze_numeral_class_constraints.py'],\n      ['scripts/audit_convergence.py'],\n"+needle)
p.write_text(s)
p=root/'README.md';s=p.read_text();line='- [Compact verdict: strongest theories and remaining evidence gap](docs/CONVERGENCE.md)\n'
if line not in s:s=s.replace('- [Research conclusions and evidence]',line+'- [Research conclusions and evidence]')
p.write_text(s)
