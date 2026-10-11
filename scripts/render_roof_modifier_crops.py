"""Unretouched primary sign-list crops; visual selection is independent of context counts."""
from pathlib import Path
from PIL import Image
import json
ROOT=Path(__file__).resolve().parents[1]
PAGES={43:'comb-tablet-m77-detail-43.png',44:'sign_list-044.png',45:'sign_list-045.png',46:'sign_list-046.png'}
# Fractional crop geometry records the original representative glyph AND its number.
LAYOUT={43:(.086,.0847,.113,.0795),44:(.096,.0858,.120,.0803),46:(.079,.0867,.124,.0805)}
SIGNS={43:[59,60,65,66,75,89,92],44:[134,137,138,141,158,159,162,163,195,196,202,203],46:[333,334,410,411]}
def main():
 records=[]
 for page,signs in SIGNS.items():
  source='results/primary_pages/'+PAGES[page];im=Image.open(ROOT/source);w,h=im.size
  x0,dx,y0,dy=LAYOUT[page]
  start={43:1,44:111,46:330}[page]
  for sign in signs:
   row,col=divmod(sign-start,10);cx=x0+col*dx;cy=y0+row*dy
   box=(cx-.035,cy-.032,cx+.04,cy+.046) if page==43 else (cx-.035,cy-.034,cx+.04,cy+.041)
   dest=f'results/primary_pages/roof-modifier-M{sign:03d}.png'
   im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/dest)
   records.append({'sign':f'M{sign:03d}','source':source,'pdf_page':page,'printed_page':page-11,'fractional_box':box,'crop':dest})
 (ROOT/'data/processed/roof_modifier_crop_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__':main()
