"""Overlapping visual regions; boxes are not asserted sign boundaries."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
source='results/primary_pages/roof-trident-new-dhr24475-photo.png'
boxes={'A-left-crossed':(65,65,495,690),'B-upper-strokes':(455,55,835,355),'C-shaft-wing':(655,55,885,685),'D-roof-stem':(825,55,1250,690)}
a=[]
with Image.open(R/source) as im:
 for label,box in boxes.items():
  out=f'results/primary_pages/dhr24475-graphic-{label}.png';im.crop(box).save(R/out)
  a.append({'source':source,'box_xyxy':box,'output':out,'operation':'crop only','boundary_status':'overlapping inspection region, not certified sign boundary'})
(R/'data/processed/dhr24475_graphic_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
