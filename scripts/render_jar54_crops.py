"""Native-pixel crops for jar54 identity, with candidate seal kept separate."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
C={
 'table-left54':('data/raw/jar54-vats-leaf284-retry.jpg',(.126,.81,.889,.839)),
 'table-right54':('data/raw/inscribed-frame-vats-leaf285.jpg',(.636,.8,.895,.838)),
 'candidate-trench-heading':('data/raw/jar54-vats-leaf214.jpg',(.177,.366,.848,.485)),
 'candidate-J630':('data/raw/jar54-vats-leaf215.jpg',(.18,.235,.924,.309)),
 'candidate-EH446':('results/primary_pages/roof-fish4493-vats-200.png',(.224,.332,.327,.435)),
 'candidate-CISI-H890':('results/primary_pages/roof-fish5477-cisi2-479.png',(.075,.602,.464,.639)),
}
a=[]
for label,(src,b) in C.items():
 out='results/primary_pages/jar54-'+label+'.png'
 with Image.open(R/src) as im:
  px=tuple(round(x*(im.width if i%2==0 else im.height)) for i,x in enumerate(b));im.crop(px).save(R/out)
 a.append({'source':src,'output':out,'pixel_box':px,'fractional_box':b,'operation':'crop only'})
(R/'data/processed/jar54_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
