"""Pin a bounded synthesis snapshot; no downloads, production imports or readings."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
FILES='''
docs/REPORT.md
docs/ALL_SIGN_EVIDENCE.md
docs/PARALLEL_THEORIES.md
docs/CONTEXT_BOUNDS.md
docs/COPPER_BRIDGES.md
docs/IDENTIFIABILITY.md
docs/NUMERAL_EQUATIONS.md
docs/ROOF_TRANSFER_SUPPORT_RESULTS.md
docs/M77_U_ALTERNATIVES.md
docs/SIGN_FAMILIES.md
docs/STRUCTURE_THEORY.md
docs/CATALOGUE_CONSTRAINT_MODELS.md
docs/TOOL_SIGN_MASS_RESULTS.md
docs/M77_U_LENGTH_HOLDOUT.md
docs/CHANHU_FISH_CONTEXT_AUDIT.md
docs/CAPACITY_MODELS.md
docs/H95_PROFILE_CAPACITY.md
docs/DECIPHERMENT_EVIDENCE_GAP_REVIEW.md
results/sign_evidence_417.json
results/primary_inventory_findings.json
results/predictive_tests.json
results/permutation_tests.json
results/relabeling_counterexample.json
results/primary_context_audit.json
results/sign_family_audit.json
results/structure_theory.json
results/numeral_theory_audit.json
results/iconography_theory_audit.json
results/numeral_equation_audit.json
results/capacity_model_audit.json
results/metal_numeral_conventions.json
results/m77_u_recovery_audit.json
results/m77_u_counterparts.json
results/roof_modifier_audit.json
results/roof_modifier_independent.json
results/roof_transfer_support.json
results/catalogue_constraint_audit.json
results/chanhu_fish_audit.json
scripts/pin_decipherment_evidence_gap_review.py
'''.split()

def main():
 index=json.loads((ROOT/'results/sign_evidence_417.json').read_text())
 primary=json.loads((ROOT/'results/primary_inventory_findings.json').read_text())
 rows=index['signs']
 assert len(rows)==417
 assert {r['sign'] for r in rows}=={f'M{i:03d}' for i in range(1,418)}
 assert all(r['semantic_value'] is None and r['phonetic_value'] is None for r in rows)
 assert primary['signs']==417 and primary['tokens']==13372
 assert index['summary']['primary_token_total']==primary['tokens']
 assert sum(primary['description_counts'].values())==417
 pins=[]
 for name in FILES:
  p=ROOT/name
  pins.append({'path':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 result={
  'scope':'bounded synthesis snapshot; not independent rerun of underlying analyses',
  'established_semantic_values':0,'established_phonetic_values':0,
  'checks':{'unique_M001_M417_rows':417,'all_semantic_and_phonetic_fields_null':True,'primary_occurrences':13372,'primary_hapax_signs':primary['hapax_signs'],'primary_signs_below_10_occurrences':primary['signs_with_fewer_than_10_occurrences'],'primary_occurrences_top67':primary['tokens_top_67'],'strict_candidate_observed_M_types':index['summary']['M_rows_observed_in_candidate_M77_strict'],'strict_candidate_unobserved_M_types':417-index['summary']['M_rows_observed_in_candidate_M77_strict']},
  'scope_warning':'Primary M counts, deduplicated W counts, candidate mappings and overlapping reviewed contexts are separate denominators.',
  'recommended_discriminating_tests':[{'id':'within_class_capacity_transfer','status':'design_not_executed','predicted_external_attribute':'independently reconstructed usable vessel capacity','primary_rival':'class/production effects without a proportional count-capacity relation','source_exposed_discovery_objects':['H-370','H-371','H-372'],'promotion_limit':'restricted quantity-like use, not universal unit, content or phonetic value'}, {'id':'deposit_level_fish_craft_transfer','status':'design_not_executed','predicted_external_attribute':'independently classified bead-production deposit','primary_rivals':['generic workshop/deposit richness','shellworking or metalworking','selected-square artifact'],'source_exposed_discovery_contexts':['Chanhudaro9/D','Chanhudaro8/E'],'promotion_limit':'restricted activity/domain association, not commodity name or rebus'}],
  'reviewed_files':pins,
  'limitations':['Source snapshots may later be updated by the central pipeline.','No new translations, sounds, global sign mergers or catalogue conversions.','Finite support failures and null results are not treated as semantic refutations.','Pin checks do not authenticate source-reading judgments.']
 }
 out=ROOT/'data/processed/decipherment_evidence_gap_review.json'
 out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'pins':len(pins),'inventory_checks':'passed','new_values':0}))

if __name__=='__main__':main()
