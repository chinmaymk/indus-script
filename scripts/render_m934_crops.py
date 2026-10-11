"""Reproducible, unretouched crops for MIC158/DM50 and comparison seals."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'mic158':('data/raw/m934_marshall48270_leaf191.jpg',(0.335,0.252,0.451,0.355)),
 'mic158-table':('results/primary_pages/m934-marshall-54.png',(0.028,0.382,0.458,0.401)),
 'm63-original':('results/primary_pages/pincer-m63-64.png',(0.067,0.691,0.408,0.948)),
 'm63-impression':('results/primary_pages/pincer-m63-64.png',(0.476,0.693,0.824,0.952)),
}
if __name__=='__main__':
 for name,(src,box) in CROPS.items():
  im=Image.open(ROOT/src); w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'm934-{name}.png')
