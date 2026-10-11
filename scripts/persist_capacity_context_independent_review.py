"""Persist independent manual table cells, exact unit checks and documentary crops."""
from pathlib import Path
from fractions import Fraction
from PIL import Image
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 specs=[
 ('280',(650,1500,5170,2530),'table-left-rows1to4'),
 ('281',(530,1560,5050,2560),'table-right-rows1to4'),
 ('280',(650,5100,5150,5710),'table-left-row18'),
 ('281',(530,5430,5050,5900),'table-right-row18'),
 ('280',(3550,1960,4100,2500),'bones-rows2and3'),
 ('281',(4200,5400,5100,5920),'row18-remarks'),
 ('281',(2100,2100,2700,2320),'row2-bead'),
 ('117',(600,2480,4370,3790),'context1033AB'),
 ('280',(3550,3550,4100,3740),'fraction-comparator')]
 crops=[]
 for leaf,box,name in specs:
  s=ROOT/f'data/raw/capacity-context-vats-leaf{leaf}.jpg'
  d=ROOT/f'results/primary_pages/capacity-context-independent-{name}.png'
  Image.open(s).crop(box).save(d)
  crops.append({'source':pin(s),'output':pin(d),'box_xyxy':box,'operation':'native rectangular crop only'})
 fuls=json.loads((ROOT/'data/processed/capacity_table_followup.json').read_text())
 comparison=[]
 for register,inches in [('1033A',36),('1033B',34)]:
  r=next(r for r in fuls['table1']['rows'] if r['excavation_number'].casefold()==register.casefold())
  cm=Fraction(inches)*Fraction(254,100); f=Fraction(str(r['external_height']))
  comparison.append({'register':register,'Vats_height_inches':inches,'converted_cm_exact':str(cm),'converted_cm_decimal':float(cm),'Fuls_external_height_cm':float(f),'Fuls_minus_Vats_cm_exact':str(f-cm),'rounds_to_Fuls_at_one_decimal_cm':round(float(cm),1)==float(f),'CISI_alias_used':False})
 assert all(x['rounds_to_Fuls_at_one_decimal_cm'] for x in comparison)
 result={'scope':'independent manual review of retained primary images, not independent archaeological sample',
 'established_semantic_values':0,'established_phonetic_values':0,
 'source_pages':{'table_left':254,'table_right':255,'narrative':91},
 'rows':[
  {'row':2,'register':'1033A','mound':'F','trench':'I','square':'M11/16','depth':'5ft6in','stratum':'III','height':'3ft','height_inches':36,'description':'Large, napiform','contents':{'bones':'6[unresolved fraction]oz','bones_numeric_ounces':None,'pointed_base_goblets':{'raw':'Do.','antecedent_row':1,'resolved':'2 and 2 fragmentary'},'other_pottery':'2 medium cylindrical and2 small round vases and1 fragmentary long oval vase','toys':'Seated male','cakes':None,'potsherds':'Several, miscellaneous','ornaments':'Round faience bead No.3531f','charcoal':'Some charcoal','shell_ivory_copper':None,'miscellaneous':None}},
  {'row':3,'register':'1033B','mound':'F','trench':'I','square':'M11/16','depth':'5ft6in','stratum':'III','height':'2ft10in','height_inches':34,'description':{'raw':'Do.','antecedent_row':2,'resolved':'Large, napiform'},'contents':{'bones':'6[unresolved fraction]oz','bones_numeric_ounces':None,'pointed_base_goblets':None,'other_pottery':None,'toys':None,'cakes':'Fragments','potsherds':'Of goblets with pointed bases, vases, etc.','ornaments':'Fragments of bangles','charcoal':None,'shell_ivory_copper':None,'miscellaneous':'Charred wheat and slag'}},
  {'row':18,'register':'3822','mound':'F','trench':'I','square':'M12/6','depth':'15ft9in','stratum':'VI','height':'2ft3in','height_inches':27,'height_cm':68.58,'mouth_diameter':'11in','mouth_diameter_cm':27.94,'description':'Large, napiform, in sherds','potsherds':'2 small, one being of the neck of jar','remarks':{'reported_pictograms':3,'location':'shoulder','nearby_objects':['jar stand3823A','jar stand3823B'],'plate':'XXIII,c'},'plate_image_visually_inspected_this_review':False,'simple_stroke_count_established':False}
 ],
 'shared_rows2and3_remark':{'explicitly_names_both_rows':True,'condition':'fragmentary','setting':'against a small broken pavement','plate':'XXIII,a'},
 'narrative1033AB':{'same_square':'M11/16','paint':'pairs of black bands on deep red ground','B_location':'south under drain','A_location':'west, half buried; upper part above pavement','plate':'XXIII,a','explicit_contents_footnote_pages':[254,255],'nearby_shaft_dimensions_not_jar_dimensions':{'internal_length':'3ft4in','internal_width':'2ft5in','standing_height':'5ft7in'},'granary_interpretation':'author proposed for nearby shaft, not a measured jar capacity'},
 'blank_and_ditto_rules':['Only explicit Do. is expanded within its column.','Dots retained as unreported cell/null, not quantitative zero or transfer from preceding row.','Row2 remark explicitly names Nos2and3, so applies to both.','Charred wheat and slag row3 not transferred to row2.'],
 'dimension_comparison_only':comparison,
 'not_verified':['CISI aliases','maximum external diameters','internal heights','opening diameters of1033A/B','capacities','stroke counts or ancient numeric values','independent origin of later height measurements'],
 'crop_manifest':crops,'evidence_files':[]}
 files=[ROOT/f'data/raw/capacity-context-vats-leaf{leaf}.jpg' for leaf in ['117','280','281']]+[ROOT/'data/processed/capacity_table_followup.json',ROOT/'docs/CAPACITY_CONTEXT_INDEPENDENT_REVIEW.md',Path(__file__).resolve()]+[ROOT/x['output']['path'] for x in crops]
 result['evidence_files']=[pin(p) for p in sorted(set(files))]
 (ROOT/'data/processed/capacity_context_independent_review.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'pins':len(result['evidence_files']),'native_crops':len(crops),'height_checks':comparison}))
if __name__=='__main__':main()
