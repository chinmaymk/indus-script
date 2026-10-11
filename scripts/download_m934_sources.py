"""Download a named public M934 research source into data/raw and record provenance."""
import sys,urllib.request,pathlib,json,hashlib,datetime
root=pathlib.Path(__file__).resolve().parents[1]
name,url=sys.argv[1:3]
assert pathlib.Path(name).name==name
p=root/'data/raw'/name
with urllib.request.urlopen(url,timeout=90) as r: data=r.read()
p.write_bytes(data)
out=root/'data/processed/m934_new_sources.json'
d=json.loads(out.read_text()) if out.exists() else {'sources':[]}
d['sources']=[r for r in d['sources'] if r['path']!=str(p.relative_to(root))]
d['sources'].append({'path':str(p.relative_to(root)),'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
out.write_text(json.dumps(d,indent=2)+'\n');print(name,len(data))
