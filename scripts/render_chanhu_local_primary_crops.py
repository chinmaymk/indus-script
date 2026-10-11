"""Reproduce unretouched original-photo and identity crops for two Chanhudaro objects."""
from pathlib import Path
import json,hashlib
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
SPECS=[
 ('data/raw/chanhu_context_leaf417.jpg',(3000,2120,3650,2920),'LII19'),
 ('data/raw/chanhu_context_leaf417.jpg',(980,2870,1520,3490),'LII23'),
 ('data/raw/chanhu_context_leaf417.jpg',(3060,2180,3600,2400),'LII19-text'),
 ('data/raw/chanhu_context_leaf417.jpg',(1005,2930,1490,3130),'LII23-text'),
 ('data/raw/chanhu_context_leaf313.jpg',(650,2020,4600,2820),'catalogue19-23'),
]
def pin(p):
 b=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 out=[]
 for src,box,name in SPECS:
  parent=ROOT/src;im=Image.open(parent);dst=ROOT/'results/primary_pages'/f'chanhu-local-primary-{name}.png';im.crop(box).save(dst)
  out.append({'source':pin(parent),'source_dimensions':list(im.size),'crop_box_xyxy':list(box),'output':pin(dst),'operation':'native-resolution rectangular crop only; no reflection, rotation, enhancement or reconstructed detail'})
 (ROOT/'data/processed/chanhu_local_primary_crop_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
 print('Saved',len(out),'native crops')
if __name__=='__main__':main()
