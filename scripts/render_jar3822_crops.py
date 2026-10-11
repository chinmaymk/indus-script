"""Crop retained primary evidence for jar3822 without altering image pixels."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
C={
 'row18-254':('data/raw/capacity-context-vats-leaf280.jpg',(.125,.729,.906,.765)),
 'row18-255':('data/raw/capacity-context-vats-leaf281.jpg',(.105,.729,.902,.774)),
 'plate-e':('results/primary_pages/capacity-context-vats-plate-correct-58.png',(.043,.728,.481,.99)),
 'plate-jar-shoulder':('results/primary_pages/capacity-context-vats-plate-correct-58.png',(.241,.775,.386,.843)),
 'cisi1-graffiti':('results/primary_pages/cisi1-408.png',(.059,.654,.45,.789)),
}
manifest=[]
for label,(src,box) in C.items():
 out='results/primary_pages/jar3822-'+label+'.png'
 with Image.open(R/src) as im:
  px=tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box))
  im.crop(px).save(R/out)
 manifest.append({'source':src,'output':out,'fractional_box':box,'pixel_box':px,'operation':'crop only'})
(R/'data/processed/jar3822_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
