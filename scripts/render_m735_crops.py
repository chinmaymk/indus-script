"""Reproduce unretouched source crops for the M735/MIC60 local review."""
from PIL import Image
from common import ROOT
CROPS = [
 ('results/primary_pages/comb-tablet-mic-53.png','m735-mic60-table.png',(0.04,0.81,0.51,0.865)),
 ('results/primary_pages/comb-tablet-m77-51.png','m735-m77-1060.png',(0.16,0.863,0.87,0.908)),
 ('results/primary_pages/sign_list_page_32.png','m735-m054-sign.png',(0.29,0.48,0.37,0.545)),
 ('data/raw/comb_tablet_marshall_leaf185.jpg','m735-mic60-photo.png',(0.715,0.525,0.885,0.652)),
]
def main():
 for source,name,box in CROPS:
  with Image.open(ROOT/source) as im:
   pixels=tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box))
   im.crop(pixels).save(ROOT/'results/primary_pages'/name)
if __name__=='__main__':main()
