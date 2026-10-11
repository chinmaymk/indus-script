"""Crop-only checks for independent marked-container/content screen."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
C={
 'p255-row18':('capacity-context-vats-leaf281.jpg',(.74,.732,.9,.775)),
 'p259-row44':('inscribed-frame-vats-leaf285.jpg',(.735,.46,.899,.518)),
 'p259-row54':('inscribed-frame-vats-leaf285.jpg',(.636,.8,.895,.838)),
 'p267-row116':('inscribed-frame-vats-leaf293.jpg',(.62,.207,.883,.268)),
 'p271-row156':('inscribed-frame-vats-leaf297.jpg',(.636,.211,.908,.238)),
 'p271-row165':('inscribed-frame-vats-leaf297.jpg',(.736,.496,.909,.525)),
 'p271-final':('inscribed-frame-vats-leaf297.jpg',(.63,.831,.918,.893)),
 'p271-concluded':('inscribed-frame-vats-leaf297.jpg',(.092,.119,.329,.151)),
 'p269-row152':('inscribed-frame-vats-leaf295.jpg',(.61,.762,.762,.796)),
 'p265-row104':('inscribed-frame-vats-leaf291.jpg',(.619,.346,.898,.37)),
}
a=[]
for label,(fn,b) in C.items():
 src='data/raw/'+fn;out='results/primary_pages/inscribed-frame-independent-'+label+'.png'
 with Image.open(R/src) as im:
  px=tuple(round(x*(im.width if i%2==0 else im.height)) for i,x in enumerate(b));im.crop(px).save(R/out)
 a.append({'source':src,'output':out,'pixel_box':px,'fractional_box':b,'operation':'crop only'})
(R/'data/processed/inscribed_jar_frame_independent_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
