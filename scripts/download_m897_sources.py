"""Retain public primary M897 sources and pending provenance records."""
import sys,urllib.request,pathlib,json,hashlib,datetime
root=pathlib.Path(__file__).resolve().parents[1]
name,url=sys.argv[1:3];assert pathlib.Path(name).name==name
with urllib.request.urlopen(url,timeout=90) as response:data=response.read()
p=root/'data/raw'/name;p.write_bytes(data)
out=root/'data/processed/m897_new_sources.json';doc=json.loads(out.read_text()) if out.exists() else {'sources':[]}
doc['sources']=[r for r in doc['sources'] if r['path']!=str(p.relative_to(root))]
doc['sources'].append(dict(path=str(p.relative_to(root)),url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),retrieved_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
out.write_text(json.dumps(doc,indent=2)+'\n');print(name,len(data))
