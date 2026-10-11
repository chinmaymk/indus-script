"""Retain bounded roof-X identity-source downloads with pending provenance."""
import sys,urllib.request,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1];name,url=sys.argv[1:3]
assert Path(name).name==name
with urllib.request.urlopen(url,timeout=60) as r:
 data=r.read();resolved=r.url
p=root/'data/raw'/name;p.write_bytes(data)
out=root/'data/processed/roof_x_identity_new_sources.json'
j=json.loads(out.read_text()) if out.exists() else {'downloads':[],'web_extraction_captures':[]}
j['downloads']=[x for x in j['downloads'] if x['path']!=str(p.relative_to(root))]
j['downloads'].append({'kind':'original_download','path':str(p.relative_to(root)),'url':url,'resolved_url':resolved,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
out.write_text(json.dumps(j,indent=2)+'\n');print(name,len(data))
