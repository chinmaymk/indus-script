"""Persist reviewer A's manual page-50 reading; this is not an OCR decoder."""
from pathlib import Path
from common import ROOT,sha256,write_json
# Read from primary page and sign-list images before seeing reviewer B's token strings.
# The secondary candidate strings were seen first; A is explicitly nonblind.
READINGS='''1001 103511 LOSS 067 072 008 342
1001 23 393
1002 100101 *373 244 LOSS
1003 100101 *086 055 267 099 121 072 336 089 211
1004 100101 059 127 245 343 075 245 245
1005 100101 296 342
1006 100101 233 081 099 389 065 336 089 087 155 124 169
1007 100101 *109 162
1008 100101 076 402 087 059 067 336 089 211
1010 100101 391 099 048 171 008 342
1011 100101 267 099 067 296 009 342 017 407 169
1012 100111 150 123 051 130 149 342 150 123 387 342
1012 21 028 400 404
1013 100101 051 130 149 342
1014 100101 267 099 087 059 067 194 342
1015 100101 197 028 054
1016 100111 245 245 345 065 158 *169
1016 23 393
1017 100101 221 127 345 053 171 059 *397 LOSS
1018 110003 336
1018 20101 017 336 189 252
1019 100101 267 099 104 059 211
1020 100101 175 230 343 336 LOSS 194 048 342
1021 100101 293 123 345 065 067 051 130 149 342
1022 100101 267 099 204 367 342
1023 100101 *267 *099 053 087 059 048 294 342
1024 100101 293 123 343 072 065 008 342
1025 100101 112 169
1026 100101 087 197 087 099 336 347 342
1027 100101 LOSS *216 *123 051 130 342 048 342
1028 100101 086 381 099 048 008 342
1029 100101 293 123 344 102 402
1030 100101 336 089 211 097 086 015'''
CENTERS=[206,271,335,400,465,529,594,660,724,789,853,918,983,1047,1112,1177,1242,1307,1372,1437,1500,1564,1629,1694,1758,1823,1887,1952,2017,2081,2146,2210,2274]
def main():
 rows=[]
 for i,(literal,y) in enumerate(zip(READINGS.splitlines(),CENTERS),1):
  ref,raw,*tokens=literal.split(); expanded=raw if len(raw)==6 else rows[-1]['expanded_metadata_code'][:-len(raw)]+raw
  seq=['LOSS' if s=='LOSS' else ('*' if s.startswith('*') else '')+'M'+s.lstrip('*') for s in tokens]
  segments=[{'position_from_right':j,'kind':'unknown_length_loss' if s=='LOSS' else 'identified_sign','sign':None if s=='LOSS' else s.lstrip('*'),'source_doubt':s.startswith('*'),'minimum_signs':1,'maximum_signs':None if s=='LOSS' else 1} for j,s in enumerate(seq,1)]
  rows.append({'printed_row_index':i,'reference':ref,'side':expanded[1],'line':expanded[4],'object_type_code':expanded[0],'field_symbol_code':expanded[2:4],'direction_code':expanded[5],'printed_metadata_literal':raw,'expanded_metadata_code':expanded,'inherited_from_row':None if len(raw)==6 else i-1,'normalized_order':'right_to_left','tokens':seq,'segments':segments,'line_bbox_render_pixels':[260,y-32,1450,y+32],'record_kind':'text_line','notes':[]})
 pins=['data/raw/mahadevan_1977_text.pdf','results/primary_pages/texts-050.png','results/primary_pages/sign_list_page_32.png','results/primary_pages/sign_list-044.png','results/primary_pages/sign_list-045.png','results/primary_pages/sign_list-046.png','data/processed/m77_codebook_review.json']
 crops=[f'results/primary_pages/m77-v1-reviewerA-part{i}.png' for i in (1,2,3)]
 doc={'schema_version':'m77-review-submission-1','reviewer':'A: /root','status':'frozen_unadjudicated_candidate','frozen_date':'2026-10-10','source_pdf_page':50,'source_printed_page':39,'page_render':'results/primary_pages/texts-050.png','page_render_dimensions':[1865,2400],'coordinate_convention':'integer native render pixels; top-left origin; whole-row bbox x1,y1,x2,y2','review_basis':'Manual comparison with primary page and all four primary sign-list images. Secondary candidate strings seen before reading; no B token strings seen before freeze. Three visual crops include every line. Unmodified independent freeze; adjudication must be separate.','prior_exposure':{'fully_blind':False,'secondary_candidate_refs':'all 29 references on this page','reviewer_b_exposure':'Schema, metadata of first row, aggregate counts, and crop filenames only; no B token strings.'},'source_pins':[{'path':p,'sha256':sha256(ROOT/p)} for p in pins],'auxiliary_visual_crops':[{'path':p,'sha256':sha256(ROOT/p)} for p in crops],'coverage':{'references':29,'printed_rows':33,'references_absent_within_1001_1030':['1009'],'physical_objects_independent':None},'rows':rows,'limitations':['Nonblind to secondary candidate strings.','Whole-row boxes, not glyph segmentation.','Normalized source does not preserve allographs.','No phonetic or semantic assignments.']}
 out='data/processed/m77_verified/reviewer_a_page050.json'
 if (ROOT/out).exists():raise SystemExit('Refusing to overwrite frozen review')
 write_json(out,doc); print(out,sha256(ROOT/out))
if __name__=='__main__':main()
