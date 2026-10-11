"""Check graphic-review and synthesis snapshots without upgrading their conclusions."""
import json
from common import ROOT,sha256,write_json
from audit_roof_variant_artifacts import check_crop

def main():
 gp='data/processed/dhr24475_graphic_review.json';sp='data/processed/decipherment_evidence_gap_review.json'
 graphic=json.loads((ROOT/gp).read_text());synthesis=json.loads((ROOT/sp).read_text())
 checked=0
 for pins in (graphic['evidence_files'],synthesis['reviewed_files']):
  for p in pins:
   assert (ROOT/p['path']).stat().st_size==p['bytes'],p['path']
   assert sha256(ROOT/p['path'])==p['sha256'],p['path']
   checked+=1
 assert graphic['ordered_M_transcription'] is None
 assert not graphic['secure_exact_M_assignments'] and not graphic['token_boundaries_certified']
 assert not graphic['context_match_outcomes_inspected'] and not graphic['translation_fields_inspected']
 assert graphic['semantic_values'] is None and graphic['phonetic_values'] is None
 cp='data/processed/dhr24475_graphic_crop_manifest.json';crops=json.loads((ROOT/cp).read_text())
 for c in crops:check_crop(c['source'],c['output'],c['box_xyxy'])
 assert len(crops)==4
 assert synthesis['checks']['unique_M001_M417_rows']==417 and synthesis['checks']['primary_occurrences']==13372
 assert synthesis['checks']['all_semantic_and_phonetic_fields_null']
 paths=[gp,sp,cp,'results/dhr24475_context_screen.json','results/dhr24475_context_independent.json','docs/DHR24475_CONTEXT_RESULTS.md','scripts/audit_dhr24475_review.py']
 write_json('results/dhr24475_review_audit.json',{'source_and_snapshot_pin_checks':checked,'exact_pixel_crop_checks':len(crops),'ordered_M_transcription':None,'secure_M_assignments':0,'semantic_values_established':0,'phonetic_values_established':0,'scope':'Context retrieval, qualified graphic review and broad evidence synthesis; no corpus promotion or decipherment.','input_sha256':{p:sha256(ROOT/p) for p in paths}})
 print(f'DHR graphic/synthesis audit: {checked} pins and {len(crops)} exact crops; no ordered transcription.')

if __name__=='__main__':main()
