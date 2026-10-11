"""Unretouched crops of EH493 and exact primary-source entries."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
CROPS={
'493-table':('data/raw/vats_1940_holdout_leaf377.jpg',(.17,.513,.809,.543)),
 'table-heading':('data/raw/vats_1940_holdout_leaf377.jpg',(.165,.10,.82,.197)),
 'group-rows':('data/raw/vats_1940_holdout_leaf377.jpg',(.17,.41,.809,.543)),
'493-photo':('results/primary_pages/roof-fish4493-vats-200.png',(.632,.832,.693,.923))}
def main():
 a=[]
 for name,(src,box) in CROPS.items():
  im=Image.open(R/src);w,h=im.size;out=f'results/primary_pages/roof-fish4493-{name}-detail.png'
  im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(R/out)
  a.append({'name':name,'source':src,'fractional_box':box,'crop':out,'processing':'crop only'})
 (R/'data/processed/roof_fish4493_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
if __name__=='__main__':main()
