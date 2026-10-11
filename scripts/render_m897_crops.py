"""Unaltered source crops for FEM545 / DK9111; fractional coordinates are reproducible."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'fem545':('data/raw/ending_fem_plates_leaf207.jpg',(.76,.126,.89,.214)),
 'table545':('data/raw/m897_mackay_leaf408.jpg',(.231,.440,.900,.468)),
}
if __name__=='__main__':
 for name,(source,box) in CROPS.items():
  im=Image.open(ROOT/source);w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'm897-{name}.png')
