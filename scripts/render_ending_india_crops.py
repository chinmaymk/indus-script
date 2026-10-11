"""Crop retained CISI pages by fractional coordinates; no enhancement or reconstruction."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/primary_pages'
CROPS={
 'm81-pair':('ending-india-m81-70.png',(0.34,0.05,0.96,0.49)),
 'm133-original':('ending-india-79.png',(0.63,0.50,0.96,0.71)),
 'm133-impression':('ending-india-79.png',(0.63,0.72,0.96,0.95)),
 'l89-pair':('ending-india-nav-295.png',(0.05,0.32,0.31,0.52)),
 'l9-pair':('ending-india-l9-276.png',(0.14,0.31,0.92,0.565)),
 'l9-metadata':('l51-cisi-metadata-408.png',(0.05,0.85,0.43,0.872)),
 'm81-metadata':('crab-cisi-final-402.png',(0.55,0.737,0.95,0.767)),
 'm133-metadata':('ending-india-nav-403.png',(0.05,0.377,0.38,0.395)),
 'l89-metadata':('l51-cisi-metadata-408.png',(0.55,0.86,0.87,0.88)),
}
if __name__=='__main__':
 for name,(source,box) in CROPS.items():
  image=Image.open(OUT/source); w,h=image.size
  image.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(OUT/f'ending-india-{name}.png')
