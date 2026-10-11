"""Recover URL provenance for interrupted ending downloads, verifying image bytes remotely.
Metadata endpoint is dynamic: recover its URL from embedded identifier, marked inferred.
"""
import concurrent.futures, hashlib, json, pathlib, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
def one(p):
 if p.name=='ending_cisi2_metadata.json':
  ident=json.loads(p.read_text())['metadata']['identifier']; url=f'https://archive.org/metadata/{ident}'
  verified=False; method='URL inferred from embedded identifier; dynamic metadata not byte-reverified'
 else:
  ident='in.gov.ignca.9954' if 'fem_plates' in p.name else 'in.gov.ignca.18225'
  leaf=p.stem.split('leaf')[1]; url=f'https://archive.org/download/{ident}/page/n{leaf}.jpg'
  with urllib.request.urlopen(url,timeout=90) as r: remote=r.read()
  verified=remote==p.read_bytes(); method='Inferred from filename and retained Archive item metadata, then independently downloaded and byte-compared'
  if not verified:
   q=p.with_name(p.stem+'_reverification_response'+p.suffix);q.write_bytes(remote)
   raise ValueError(f'Byte mismatch: {p}; retained response {q}')
 return {'path':str(p.relative_to(ROOT)),'url':url,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'url_recovery_method':method,'remote_bytes_identical':verified}
if __name__=='__main__':
 paths=sorted((ROOT/'data/raw').glob('ending_*'))
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: rows=list(ex.map(one,paths))
 out=ROOT/'data/processed/ending_pakistan_new_sources.json';out.write_text(json.dumps({'recovery_date':'2026-09-25','sources':rows},indent=2)+'\n'); print(len(rows),'provenance records verified/recovered')
