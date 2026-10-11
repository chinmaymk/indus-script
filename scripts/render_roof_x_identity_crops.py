"""Unretouched crops: fractional coordinates measured on retained primary pages."""
from pathlib import Path
from PIL import Image
import json
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 '407-metadata':('data/raw/roof_x_identity_vats_leaf193.jpg',(.197,.792,.823,.850)),
 '558-metadata':('data/raw/roof_x_identity_vats_leaf134.jpg',(.238,.465,.846,.536)),
 'shield-class':('data/raw/roof_x_identity_vats_leaf353.jpg',(.153,.793,.813,.895)),
 'm77-suffix-rule':('results/primary_pages/roof-x-identity-m77-826.png',(.17,.372,.826,.426)),
 '407-photo':('results/primary_pages/roof-x-identity-vats-198.png',(.617,.575,.711,.683)),
 '558-photo':('results/primary_pages/roof-x-identity-vats-202.png',(.592,.613,.646,.694)),
}
def main():
 rows=[]
 for name,(src,box) in CROPS.items():
  im=Image.open(ROOT/src);w,h=im.size;out=f'results/primary_pages/roof-x-identity-{name}-detail.png'
  im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/out)
  rows.append({'name':name,'source':src,'fractional_box':box,'crop':out,'processing':'crop only; no retouching, rotation, mirroring or contrast changes'})
 (ROOT/'data/processed/roof_x_identity_crop_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
