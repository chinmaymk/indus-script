"""Reproduce unretouched CISI2 H843 source crops (fractional page coordinates)."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'h843-a':('h843-cisi2-target-366.png',(.09,.06,.415,.176)),
 'h843-all':('h843-cisi2-target-366.png',(.079,.059,.413,.505)),
 'h843-metadata':('h843-cisi2-target-479.png',(.065,.06,.421,.122)),
}
if __name__=='__main__':
 for name,(source,box) in CROPS.items():
  im=Image.open(ROOT/'results/primary_pages'/source);w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'h843-identity-{name}.png')
