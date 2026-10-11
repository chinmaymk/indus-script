"""Exact, unretouched excerpts for the two M334 artifact identifications."""
from pathlib import Path
from PIL import Image
import hashlib, json
ROOT=Path(__file__).resolve().parents[1]
PAGE='results/primary_pages/'
JOBS=[
('data/raw/roof_u_marshall_leaf199.jpg','marshall-403',(.60,.805,.847,.869)),
(PAGE+'roof-u-extension-m77-827.png','appendix-mic',(.10,.055,.53,.165)),
(PAGE+'roof-u-extension-m77-827.png','appendix-fem',(.10,.35,.53,.411)),
(PAGE+'roof-u-extension-m77-62.png','1403',(.13,.385,.80,.426)),
(PAGE+'roof-u-extension-m77-80.png','2364',(.12,.073,.80,.108)),
('data/raw/roof_u_mackay_leaf402.jpg','mackay-header',(.195,.09,.89,.235)),
('data/raw/roof_u_mackay_leaf402.jpg','mackay-364',(.20,.675,.89,.705)),
(PAGE+'roof-u-extension-mic-table-55.png','mic-header',(.50,.08,.93,.168)),
(PAGE+'roof-u-extension-mic-table-55.png','mic-403',(.505,.752,.935,.773)),
(PAGE+'crab-cisi-target-404.png','M354-metadata',(.075,.932,.49,.966)),
(PAGE+'roof-u-extension-cisi1-124.png','M354-views',(.06,.347,.95,.619)),
(PAGE+'roof-u-extension-cisi-471.png','M810-metadata',(.092,.299,.401,.314)),
(PAGE+'roof-u-extension-cisi-105.png','M810-views',(.35,.06,.65,.513)),
]
def main():
 rows=[]
 for source,name,box in JOBS:
  src=ROOT/source; dst=ROOT/PAGE/f'roof-u-extension-{name}-crop.png'
  with Image.open(src) as im:
   px=tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box))
   im.crop(px).save(dst)
  rows.append({'source':source,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'output':str(dst.relative_to(ROOT)),'fractional_box':box,'pixel_box':px,'output_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'enhancement':'none'})
 (ROOT/'data/processed/roof_u_extension_crop_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
