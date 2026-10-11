"""Fetch one public source into data/raw, retaining interrupted/error bodies.

Example: python scripts/fetch_preserved_source.py URL unique-name.jpg
No central registry mutation: inspect the body and merge the emitted typed record.
Refuses existing targets. Partial responses are never claimed as complete sources.
"""
import argparse,hashlib,json,urllib.request,urllib.error
from datetime import datetime,timezone
from pathlib import Path
from common import ROOT

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('url');parser.add_argument('filename')
 parser.add_argument('--timeout',type=int,default=45)
 args=parser.parse_args()
 if Path(args.filename).name!=args.filename or args.filename in ('','.','..'):
  raise SystemExit('filename must be a single nonempty data/raw basename')
 if not args.url.startswith(('https://','http://')):raise SystemExit('HTTP(S) URL required')
 dest=ROOT/'data/raw'/args.filename
 partial=dest.with_name(dest.name+'.partial')
 header_path=dest.with_name(dest.name+'.headers.json')
 metadata=ROOT/'data/processed'/('fetch_'+args.filename.replace('.','_')+'.json')
 if dest.exists() or partial.exists() or metadata.exists() or header_path.exists():raise SystemExit('Refusing overwrite of retained fetch')
 record={'url':args.url,'retrieval_started_utc':datetime.now(timezone.utc).isoformat(),'response_complete':False,'http_status':None,'response_body_received':False}
 response=None;failure=None
 try:
  try:
   response=urllib.request.urlopen(urllib.request.Request(args.url,headers={'User-Agent':'IndusResearch/1.0 (public-source provenance)'}),timeout=args.timeout)
  except urllib.error.HTTPError as error:
   response=error
  record.update(http_status=response.status,resolved_url=response.geturl())
  header_path.write_text(json.dumps(dict(response.headers.items()),indent=2)+'\n')
  record['header_artifact']={'path':str(header_path.relative_to(ROOT)),'bytes':header_path.stat().st_size,'sha256':hashlib.sha256(header_path.read_bytes()).hexdigest(),'kind':'locally_serialized_HTTP_response_headers'}
  with partial.open('xb') as stream:
   while True:
    chunk=response.read1(65536)
    if not chunk:break
    stream.write(chunk);stream.flush()
   record['response_complete']=True
  if 200<=response.status<300:
   partial.rename(dest);record['kind']='complete_http_body_pending_content_review'
  else:record['kind']='complete_error_response_body_not_requested_research_content'
 except BaseException as error:
  failure=error;record['error']=type(error).__name__+': '+str(error)
  record['kind']='incomplete_response_or_connection_failure'
 finally:
  if response is not None:response.close()
  body=dest if dest.exists() else partial if partial.exists() else None
  if body is not None:
   record.update(path=str(body.relative_to(ROOT)),bytes=body.stat().st_size,sha256=hashlib.sha256(body.read_bytes()).hexdigest(),response_body_received=body.stat().st_size>0)
  record['retrieval_ended_utc']=datetime.now(timezone.utc).isoformat()
  metadata.write_text(json.dumps(record,indent=2)+'\n')
  print(json.dumps(record,indent=2))
 if failure is not None:raise SystemExit(130 if isinstance(failure,KeyboardInterrupt) else 1)
 if not 200<=record['http_status']<300:raise SystemExit(1)

if __name__=='__main__':main()
