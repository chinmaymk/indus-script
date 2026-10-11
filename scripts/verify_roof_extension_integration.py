"""Verify registered bytes, final all-sign coverage, audit inputs and local Markdown links."""
import json,re
from urllib.parse import unquote,urlsplit
from common import ROOT,sha256,write_json

def main():
 registry=json.loads((ROOT/'data/sources.json').read_text())
 groups=('downloads','web_extraction_captures','archived_http_responses')
 seen=set()
 for key in groups:
  for row in registry[key]:
   assert row['path'] not in seen,row['path'];seen.add(row['path'])
   p=ROOT/row['path']
   assert p.stat().st_size==row['bytes'] and sha256(p)==row['sha256'],row['path']
 unregistered=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'data/raw').rglob('*') if p.is_file() and str(p.relative_to(ROOT)) not in seen)
 # Local explanatory/license files predate this phase and are not separate downloads.
 assert set(unregistered)<={'data/raw/README.md','data/raw/mayig_LICENSE'},unregistered
 idx=json.loads((ROOT/'results/sign_evidence_417.json').read_text())
 rows=idx['signs']
 assert len(rows)==417 and {r['sign'] for r in rows}=={f'M{i:03d}' for i in range(1,418)}
 assert all(r['semantic_value'] is None and r['phonetic_value'] is None for r in rows)
 for row in idx['summary']['sources'].values():assert sha256(ROOT/row['path'])==row['sha256'],row['path']
 result=json.loads((ROOT/'results/roof_coverage_extension.json').read_text())
 for path,digest in result['input_sha256'].items():assert sha256(ROOT/path)==digest,path
 checked=0;missing=[]
 for doc in [ROOT/'README.md',*sorted((ROOT/'docs').glob('*.md'))]:
  for match in re.finditer(r'!?\[[^\]]*\]\(([^\n]+?)\)',doc.read_text()):
   target=match.group(1).strip().split(' "',1)[0].strip('<>')
   if urlsplit(target).scheme or target.startswith('#'):continue
   target=unquote(target.split('#',1)[0]);target=re.sub(r':\d+$','',target)
   if not target:continue
   path=(doc.parent/target).resolve();checked+=1
   if not path.exists():missing.append([str(doc.relative_to(ROOT)),target])
 assert not missing,missing
 output={'source_records':sum(len(registry[k]) for k in groups),'source_record_groups':{k:len(registry[k]) for k in groups},'unregistered_raw_local_files':unregistered,'all_sign_rows':417,'semantic_and_phonetic_values_all_null':True,'index_source_hashes_verified':len(idx['summary']['sources']),'conditional_context_sign_rows':idx['summary']['M_rows_with_conditional_context_audits'],'new_audit_input_hashes_verified':len(result['input_sha256']),'local_markdown_links_checked':checked,'missing_local_links':[],'evidence_pin_checks':result['evidence_pin_checks'],'independent_review_revision_pin_checks':result['independent_review_revision_pin_checks'],'exact_pixel_crop_checks':result['exact_pixel_crop_checks'],'scope':'Integrity and coverage only; semantic claims remain undetermined.'}
 write_json('results/roof_extension_integration_checks.json',output)
 print(json.dumps(output,indent=2))

if __name__=='__main__':main()
