"""Preserve pre-control-outcome design; algebra checks use no corpus sign data."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 x=ROOT/p
 return {'path':p,'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()}
def main():
 profiles=[]
 for a in range(4):
  for u in range(4-a):
   for b in range(3):
    for v in range(3-b):
     L=Fraction(a,3)-Fraction(b+v,2);U=Fraction(a+u,3)-Fraction(b,2)
     assert (L>=Fraction(1,3))==((b+v==0 and a>=1)or(b+v==1 and a==3))
     assert (L>Fraction(1,3))==((b+v==0 and a>=2)or(b+v==1 and a==3))
     profiles.append({'a':a,'u':u,'b':b,'v':v,'L':str(L),'U':str(U)})
 assert len(profiles)==60
 paths=['docs/CHANHU_DEPOSIT_RESULTS.md','results/chanhu_local_contrast.json','docs/CHANHU_LOCAL_SPECIFICITY_DESIGN_REVIEW.md','scripts/pin_chanhu_local_specificity_design.py']
 r={'scope':'design audit before new control outcomes; existing five-seal fish results known','new_control_outcomes_inspected':False,'new_frequencies_computed':False,'fish_family_changed':False,'primary_fair_comparison':'single W220 vs other single literal Wcodes','frequency_matching':'outside fixed five grouped objects, certain-positive object count; exact and factor-two sets separate; unknown-count range retained','equivalence_definition':'identical ordered five-object P/N/U vector','strength_definition':'lower endpoint compared to1/3; larger upper endpoint not by itself stronger','known_target_vector':['U','P','N','N','N'],'known_target_bounds':['1/3','2/3'],'algebra_only_profiles':profiles,'group_count_profile_maximum':60,'object_status_vector_maximum':243,'sole_positive_omitted_bounds':['0','1/2'],'p_value_planned':False,'established_semantic_values':0,'established_phonetic_values':0,'evidence_files':[pin(p) for p in paths]}
 target=ROOT/'data/processed/chanhu_local_specificity_design_review.json';target.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({'review':str(target.relative_to(ROOT)),'pins':len(paths),'pure_algebra_profiles_checked':len(profiles)}))
if __name__=='__main__':main()
