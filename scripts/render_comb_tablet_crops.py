"""Unretouched candidate-source crops; no asserted H843 artifact identity."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'm77-5326-text':('results/primary_pages/comb-tablet-m77-149.png',(.195,.719,.819,.772)),
 'm77-5326-metadata':('results/primary_pages/chain-artifact-m77-832.png',(.47,.714,.835,.787)),
 'm77-5326-reverse':('results/primary_pages/comb-tablet-m77-822.png',(.757,.501,.905,.605)),
 'm054-sign':('results/primary_pages/comb-tablet-m77-detail-43.png',(.3,.48,.363,.547)),
}
if __name__=='__main__':
 for name,(source,box) in CROPS.items():
  im=Image.open(ROOT/source);w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'comb-tablet-{name}.png')
