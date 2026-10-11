"""Crop the four complete M77 reference entries without joining their fields."""
from pathlib import Path
from PIL import Image
import json
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 '4407':(122,(.17,.348,.845,.408)),
 '4493':(127,(.21,.536,.852,.595)),
 '5444':(153,(.21,.405,.852,.461)),
 '5477':(155,(.21,.330,.849,.385)),
 'eh-rule':(830,(.065,.758,.465,.863)),
 '5444-source':(833,(.09,.801,.482,.833)),
 '5477-source':(833,(.54,.509,.884,.54)),
}
def main():
 rows=[]
 for name,(page,box) in CROPS.items():
  src=f'results/primary_pages/roof-m176-{page}.png';im=Image.open(ROOT/src);w,h=im.size
  out=f'results/primary_pages/roof-m176-{name}-detail.png'
  im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/out)
  rows.append({'name':name,'source':src,'fractional_box':box,'crop':out})
 (ROOT/'data/processed/roof_m176_crop_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
