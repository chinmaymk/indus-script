"""Crop retained primary pages without altering orientation or sign strokes."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/primary_pages'
CROPS={
 'm63-original':('pincer-m63-64.png',(0.06,0.69,0.41,0.95)),
 'm63-impression':('pincer-m63-64.png',(0.46,0.69,0.82,0.95)),
 'm63-cisi-identity':('pincer-cisi-402.png',(0.545,0.562,0.94,0.579)),
 'm63-m77-identity':('pincer-m77-828.png',(0.475,0.24,0.85,0.27)),
 'm63-m77-text':('pincer-m77-098.png',(0.12,0.80,0.80,0.845)),
}
def main():
 for name,(source,box) in CROPS.items():
  im=Image.open(OUT/source);w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(OUT/f'pincer-{name}.png')
if __name__=='__main__':main()
