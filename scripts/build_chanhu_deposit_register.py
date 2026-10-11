#!/usr/bin/env python3
"""Persist manually image-checked provenance only; no sign transcription or classifications."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pin(p):
 b=(ROOT/p).read_bytes();return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
# plate|item|excavation raw|material raw|square|trench|mound|cutting|locus|level
DATA='''LI|1|3198|Yell. steat.|7/E||||121|+8.8
LI|2|3052|Gr. steat.|7/E||||121|+7.8
LI|3|594|Br. steat.||B(5)|||56|-5.7
LI|4|518|Gr. steat.||B(5)|||56|+0.8
LI|5|4770|Gr. steat.|9/F|||Cut.|410|-1.1
LI|6|3737|Gr. steat.|7/C||||459|+7.0
LI|7|3200|Wh. steat.|8/F||||344|+6.9
LI|8|3159|Gr. steat.|7/E||||121|+7.8
LI|9|2000|Gr. st.|8/D||||223|+12.2
LI|10|4767|Wh. steat.|12/K||I||47|+13.1
LI|11|3485, b|Wh. steat.|8/C||||231|+7.2
LI|12|3493|Gr. steat.|7/C||||240|+7.0
LI|13|3148|Wh. steat.|8/E||||113|+6.8
LI|14|3215|Wh. steat.|9/B||||283|+6.9
LI|15|2285|Wh. steat.|9/D||||215|+10.4
LI|16|3049|Wh. steat.|8/F||||115|+6.5
LI|17|3495|Wh. steat.|7/C||||98|+7.5
LI|18|926|Wh. steat.||E(1)|||34|-7.1
LI|19|2845|Wh. steat.|9/F||||405|+8.0
LI|20|2594, h|Wh. steat.|9/C||||228|+9.9
LI|21|1269|Wh. steat.||F(2)|||65|-4.1
LI|22|3207|Wh. steat.|9/B||||442|+7.7
LI|23|2532|Wh. steat.|7/E||||122|+9.4
LI|24|3051|Wh. steat.|9/D||||211|+8.1
LI|25|3817|Bl. steat.|12/K||I||26|+14.1
LI|26|3043|Wh. steat.|8/E||||430|+7.3
LI|27|3045|Wh. steat.|8/E||||177|+7.6
LI|28|2293|Wh. steat.|10/E||||261|+9.3
LI|29|2297|Wh. steat.|9/D||||174|+10.0
LI|30|3485, a|Yell. steat.|8/C||||231|+7.2
LI|31|1293|Bl. steat.|7/E||||97|+14.9
LI|32|2361|Wh. steat.|9/C||||227|+10.9
LI|33|2462|Wh. steat.|8/D||||82|+9.5
LII|1|2597|Wh. steat.|9/D||||192|+8.9
LII|2|2848|Wh. steat.|8/E||||425|+8.0
LII|3|3359|Wh. steat.|7/F||||110|+7.1
LII|4|3168|Wh. steat.|9/D||||211|+8.1
LII|5|4852|Wh. steat.|9/F|||Cut.|469|-2.8
LII|6|2390|Wh. steat.|8/B||||235|+9.9
LII|7|4327|Wh. steat.|12/K||I||20|+14.8
LII|8|3886|Gr. steat.|13/J||I||6|+16.8
LII|9|950|Wh. steat.||J(1)|||73|-0.1
LII|10|3326|Wh. steat.|10/C||||385|+6.9
LII|11|3206|Wh. steat.|9/D||||204|+6.9
LII|12|2558|Wh. steat.|9/D||||106|+8.8
LII|13|2603|Wh. steat.|10/D||||362|+6.8
LII|14|2426|Wh. steat.|9/E||||199|+9.0
LII|15|2531|Wh. steat.|8/D||||178|+9.6
LII|16|1393|Bl. steat.|8/F||||83|+15.4
LII|17|4960|Gr. steat.|13/J||I||9|+13.5
LII|18|3154|Wh. steat.|9/C||||395|+7.7
LII|19|2428|Br. steat.|9/D||||286|+9.7
LII|20|2559|Wh. steat.|9/C||||296|+9.5
LII|21|2358|Wh. steat.|8/C||||152|+11.1
LII|22|2595|Br. steat.|7/E||||164|+9.3
LII|23|2529, CC|Wh. steat.|8/C||||297|+10.4
LII|24|2605|Wh. steat.|6/F||||159|+8.4
LII|25|4596|Wh. steat.|13/J||I||2|+14.4
LII|26|2467|Wh. steat.|8/C||||151|+10.5
LII|27|2468|Wh. steat.|7/F||||189|+9.8
LII|28|3318|Wh. steat.|10/F||||423|+6.7
LII|29|3811|Gr. steat.|9/F|||Cut.|468|+3.8
LII|30|2389|Gr. steat.|7/C||||240|+9.2
LII|31|2530|Wh. steat.|7/E||||300|+9.5
LII|32|3492|Gr. steat.|8/C||||289|+8.6'''
rows=[]
for line in DATA.splitlines():
 plate,item,ex,mat,sq,tr,mo,cut,loc,level=line.split('|');item=int(item)
 page=292 if plate=='LI' or item<=3 else 293
 rows.append(dict(row_id=f'{plate}.{item}',plate=plate,item=item,excavation_number_raw=ex,material_raw=mat,square_raw=sq or None,trench_raw=tr or None,mound_raw=mo or None,cutting_raw=cut or None,locus_raw=loc,elevation_ft_raw=level,elevation_ft=float(level),source_page=page,source_leaf=page+20,source_image=f'data/raw/chanhu_context_leaf{page+20}.jpg',fragment_status='not_stated_in_catalogue',missing_requested_fields=[] if sq else ['square_raw'],uncertain_requested_fields=[],notes=[]))
byid={r['row_id']:r for r in rows}
byid['LI.9']['notes'].append("Printed material is 'Gr. st.'; not silently expanded to steatite.")
for rid in ('LI.6','LI.19','LI.24'):
 byid[rid]['notes'].append('Printed dimensions contain question mark(s); not evidence of an unbroken object or a sufficient fragment criterion. Dimensions outside requested extraction.')
byid['LI.23']['notes'].append('Only two dimensions printed; does not itself establish fragmentation.')
byid['LI.14']['notes'].append('Image reads3215 and9/B; OCR3115 and secondary9/D not substituted; prior workshop review discusses square boundary inconsistency.')
byid['LI.29']['notes'].append('Catalogue+10.0 preserved; prior workshop review reports narrative p46 bead/seal elevation conflict; not resolved here.')
byid['LI.26']['notes'].append('Image reads3043; parent reports duplicate3817 at this plate/item in secondary data. No identity correction made in source export.')
byid['LII.12']['fragment_status']='not_stated_in_catalogue; fragment_reported_in_prior_physical_review'
byid['LII.12']['notes'].append('Prior docs/CHANHU_WORKSHOP_CONTEXT_REVIEW.md physically assessed broken lower fragment; no new seal photograph or glyph assessment in this task.')
# The six preceding rows physically present on292 belong to the earlier Jhukar section, not the core Harappa section.
extra=[]
for item,ex,mat,sq,loc,lev in [(11,'2928','Dr. pot.','10/E','252','+7.1'),(12,'1815','Gr. pot.','9/E','124','+14.9'),(13,'2488','Lt. rd. pot.','8/D','82','+14.9'),(14,'3840','Lt. red. pot.','10/F','465','+2.3'),(15,'2289','Lt. rd. pot.','10/E','225',None),(16,'1594','Dk. gr. st.','8/C','109','+16.5')]:
 extra.append(dict(row_id=f'L.{item}',plate='L',item=item,excavation_number_raw=ex,material_raw=mat,square_raw=sq,trench_raw=None,mound_raw=None,cutting_raw=None,locus_raw=loc,elevation_ft_raw=lev if lev else 'cross-shaped mark before10.3',elevation_ft=float(lev) if lev else None,source_page=292,source_leaf=312,source_image='data/raw/chanhu_context_leaf312.jpg',fragment_status='not_stated_in_catalogue',uncertain_requested_fields=['elevation_ft_raw'] if lev is None else [],exclusion_reason='Continuation of Plate L Jhukar seal-amulet/impression section, outside LI/LII Harappa frame'))
paths=['data/raw/chanhu-register-primary-leaf165.jpg','data/raw/chanhu_context_leaf312.jpg','data/raw/chanhu_context_leaf313.jpg','data/raw/c40_mackay1943_djvu.txt','data/raw/c40_mackay1943_page_numbers.json','data/raw/c40_mackay1943_metadata.json','docs/CHANHU_WORKSHOP_CONTEXT_REVIEW.md']
crops=[]
for leaf in (312,313):
 for k,(y0,y1) in enumerate(((500,2600),(2400,4400),(4200,6200))):
  path=f'results/primary_pages/chanhu-register-{leaf}-{k}.png'
  crops.append(dict(**pin(path),parent_image=f'data/raw/chanhu_context_leaf{leaf}.jpg',crop_box_xyxy=[450,y0,4900,y1],resize_output=[2225,(y1-y0)//2],operations='rectangular crop then Pillow resize; no content edits'))
result=dict(schema_version=1,scope='Complete LI1–33 and LII1–32 Harappa illustrated seal-amulet provenance rows on printed292–293; not a census of every excavated seal or of inscribed seals.',method='Manual reading of original whole-page images and enlarged text crops; OCR only locator. No sign transcription, fish coding, meaning assignment or context-sign outcome counts.',rows=rows,adjacent_excluded_rows=extra,source_pins=[pin(p) for p in paths],crop_pins=crops,coverage=dict(core_rows=len(rows),plates={'LI':33,'LII':32},excavation_numbers_present=65,materials_present=65,loci_present=65,elevations_present=65,squares_present=sum(r['square_raw'] is not None for r in rows),trench_instead_of_square=sum(r['trench_raw'] is not None for r in rows),mound_explicit=sum(r['mound_raw'] is not None for r in rows),cutting_explicit=sum(r['cutting_raw'] is not None for r in rows),requested_field_digit_uncertainties=0),page_mapping=[{'leaf':312,'printed':292,'verified':'page_numbers JSON and visible image header'},{'leaf':313,'printed':293,'verified':'page_numbers JSON and visible image header'}],limitations=['Blanks in mound/cutting do not establish a mound or excavation-unit identity.','Same square/locus is not automatically the same deposit or level.','No phase/room-function/closed-deposit status supplied by these rows.','No explicit fragment word in the65 catalogue entries; unflagged rows are not certified whole.','Colour/material abbreviations preserved; st. not expanded beyond source.','All sign surfaces, preservation and inscription denominators require separate assessments.'],attempts=['Located LI/LII and preceding/following headings in retained OCR.','Visually checked complete source pages292293 and all provenance fields in overlapping crops.','Resolved OCR/preliminary low-resolution errors including3215,3043,LII2+8.0,LII3Wh. and7/F.','No corpus/sign outcome counts inspected.'])
assert len(rows)==65 and len(byid)==65
assert [(r['plate'],r['item']) for r in rows]==[('LI',i) for i in range(1,34)]+[('LII',i) for i in range(1,33)]
result['catalogue_boundaries']={'preceding':{'printed_page':291,'heading':'Plate L. Seal-amulets and Impressions of the Jhukar Period. Chapter IX','evidence':'retained original OCR heading; no291 image inspected','continues_on292':'L11–16, image checked; excluded adjacent rows preserved'},'core':'LI1–33 and LII1–32; both visible headings assign Harappa period','following':{'printed_page':293,'heading':'Plate LIII. Figurines. Chapter X','evidence':'original image; OCR294 continues figurines'},'full_excavation_census_status':'not established; chapter is Catalogue of Illustrated Objects;65 only finite illustrated frame'}
result['production_and_image_metadata']={'source_page':145,'source_leaf':165,'source_image':'data/raw/chanhu-register-primary-leaf165.jpg','verification':'original image reviewed for physical-production and photographic-method statements only','author_reports_unfinished_specimens':['LI.'+str(i) for i in range(1,11)],'author_additional_back_completion_discussion':['LI.12','LI.18','LI.21'],'author_reports_direct_photographs':['LII.'+str(i) for i in [1,2,3,4,5,6,11]],'remaining_LI_LII':'Author says photographs of plasticine impressions; not independently checked here.','limits':'Unfinished is not equivalent to uninscribed, broken, or missing text. This is publication-level coverage/method information, not a sign reading or outcome.'}
result['crop_pins'].append(dict(**pin('results/primary_pages/chanhu-register-p145-production.png'),parent_image='data/raw/chanhu-register-primary-leaf165.jpg',crop_box_xyxy=[650,1750,4700,5100],resize_output=[1620,1340],operations='rectangular crop then Pillow resize; no content edits'))
for leaf,name,box in [(312,'LI12',[1000,2950,4300,3300]),(312,'LI26',[1000,4310,4300,4610]),(312,'LI31',[1000,4700,4300,5050]),(313,'LII15',[700,1600,4100,2050])]:
 result['crop_pins'].append(dict(**pin(f'results/primary_pages/chanhu-register-confirm-{name}.png'),parent_image=f'data/raw/chanhu_context_leaf{leaf}.jpg',crop_box_xyxy=box,operations='native-resolution rectangular crop; no other edit'))
for rid,note in [('LII.15','Native follow-up reconfirms2531,8/D,178,+9.6; parent reports secondary2431.'),('LI.12','Native follow-up reconfirms+7.0; parent reports secondary+7.2.'),('LI.31','Native follow-up reconfirms+14.9; parent reports secondary+14.1.')]:
 byid[rid]['notes'].append(note)
result['attempts'].append('After parent metadata-only join reported discrepancies, independently rechecked LII15, LI26, LI12, LI31 in native crops; all retained original readings confirmed; no signs inspected.')
result['source_pins'].append(pin('scripts/build_chanhu_deposit_register.py'))
result['attempts'].extend(['Original p145 acquired after a sandbox DNS failure; error metadata retained without response body. Successful acquisition has independent basename, headers and typed pending manifest.','Visually checked p145 production/photographic-method discussion; no sign values, fish counts or sequence transcription.'])
(ROOT/'data/processed/chanhu_deposit_seal_register.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['coverage'])
