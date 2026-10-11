"""Pin an independent, outcome-uninspected design review; no corpus computation."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pin(path):
 p=ROOT/path
 return {'path':path,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 paths=['docs/DECIPHERMENT_EVIDENCE_GAP_REVIEW.md','docs/CHANHU_WORKSHOP_CONTEXT_REVIEW.md','docs/CHANHU_FISH_CONTEXT_AUDIT.md','data/processed/chanhu_fish_protocol.json','data/processed/chanhu_primary_review.json','docs/CHANHU_DEPOSIT_TEST_DESIGN_REVIEW.md','scripts/pin_chanhu_deposit_design_review.py']
 result={'scope':'independent design audit before new sign outcomes; previously published outcomes remain discovery data','new_sign_counts_computed':False,'family_changed':False,'new_downloads':0,'primary_estimand':'fixed-stratum equally weighted difference of mean deposit family-bearing physical-seal proportions, D+ versus comparably reported D0','exposure_target':'documented diagnostic bead-production evidence, not verified true activity absence/presence','outcome_unknown_bounds':'a/n to (a+u)/n per fixed deposit; exact linear contrast bounds, then admissible-world union for phase/location/exposure uncertainty','comparison_absence_requirement':'perfect archaeological negatives are not required; reporting silence alone is insufficient','next_action':'Freeze context-only feasibility ledger for all seal entries in retained primary catalogue pp292–293 and direct narrative pointers; show sign-free support by phase/deposit/reporting strata and independent complexes, then stop or freeze matched test.','established_semantic_values':0,'established_phonetic_values':0,'all_417_values_remain_null':True,'evidence_files':[pin(p) for p in paths]}
 target=ROOT/'data/processed/chanhu_deposit_test_design_review.json';target.write_text(json.dumps(result,indent=2)+'\n')
 assert all(pin(p['path'])==p for p in result['evidence_files'])
 print(json.dumps({'review':str(target.relative_to(ROOT)),'pins':len(paths)}))
if __name__=='__main__':main()
