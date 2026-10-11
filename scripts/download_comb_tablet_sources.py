"""Download public source candidates, retaining all bytes under data/raw."""
import sys, urllib.request, pathlib, json, hashlib
root=pathlib.Path(__file__).resolve().parents[1]
name,url=sys.argv[1:3]
assert pathlib.Path(name).name==name
with urllib.request.urlopen(url,timeout=90) as response:
    data=response.read(); final_url=response.url
p=root/'data/raw'/name;p.write_bytes(data)
out=root/'data/processed/comb_tablet_new_sources.json'
doc=json.loads(out.read_text()) if out.exists() else {'sources':[]}
doc['sources']=[r for r in doc['sources'] if r['path']!=str(p.relative_to(root))]
doc['sources'].append(dict(path=str(p.relative_to(root)),url=url,final_url=final_url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
out.write_text(json.dumps(doc,indent=2)+'\n')
print(name,len(data))
