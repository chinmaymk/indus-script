"""Pin a visually verified historical statement and its narrow conditional inference."""
from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 source='data/raw/capacity-context-vats-leaf117.jpg'
 crop='results/primary_pages/repeated-goblet-p91-first-paragraph.png'
 box=(650,970,4400,1790)
 Image.open(ROOT/source).crop(box).save(ROOT/crop)
 r={'scope':'independent visual verification of historical report; conditional counterexample, not statistical test','printed_page':91,'source_statement':{'container_type':'trough','container_register':'470','square':'M12/13','goblets_reported':2,'goblet_form':'pointed bases','each_stamped_with_same_seal':True,'plate_reference':'CII,21','proposed_potter_name':'author conjecture only'},'conditional_inference':{'premise':'The report accurately describes two distinct goblets sharing a stamp design.','contradicted_claim':'That stamp design alone uniquely identifies each individual physical vessel.','formal_reason':'A != B and design(A) == design(B), so design is not injective on physical vessels.'},'not_excluded':['owner identifier','maker or workshop identifier','batch identifier','class identifier','additional distinguishing marks or information','accidental impression differences'],'individual_goblet_field_numbers':[None,None],'cisi_aliases':[None,None],'m77_texts':[None,None],'later3262_reference':'same page and same plate reference do not by themselves identify3262 as one of this pair','plate_inspected':False,'new_downloads':0,'established_semantic_values':0,'established_phonetic_values':0,'all_417_values_remain_null':True,'crop':{'source':source,'output':crop,'box_xyxy':box,'operation':'native rectangular crop only'},'evidence_files':[]}
 r['evidence_files']=[pin(p) for p in [source,crop,'docs/REPEATED_GOBLET_STAMP_REVIEW.md',str(Path(__file__).resolve().relative_to(ROOT))]]
 target=ROOT/'data/processed/repeated_goblet_stamp_review.json';target.write_text(json.dumps(r,indent=2)+'\n')
 assert all(pin(x['path'])==x for x in r['evidence_files'])
 print(json.dumps({'review':str(target.relative_to(ROOT)),'pins':len(r['evidence_files'])}))
if __name__=='__main__':main()
