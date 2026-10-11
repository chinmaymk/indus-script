"""Unaltered fractional crops from retained Mackay page JPEGs."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 '60':('ending_fem_plates_leaf181.jpg',(0.79,0.06,0.90,0.147)),
 '129':('ending_fem_plates_leaf183.jpg',(0.073,0.50,0.244,0.63)),
 '142':('ending_fem_plates_leaf183.jpg',(0.38,0.66,0.56,0.731)),
 '583':('ending_fem_plates_leaf207.jpg',(0.75,0.63,0.903,0.756)),
}
if __name__=='__main__':
 for key,(file,box) in CROPS.items():
  im=Image.open(ROOT/'data/raw'/file); w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'ending-pakistan-fem-{key}.png')
