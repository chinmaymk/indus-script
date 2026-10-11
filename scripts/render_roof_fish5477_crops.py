"""Unretouched source excerpts for M77 5477 / CISI H-889 review."""
from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
JOBS=[
('roof-m176-833.png','roof-fish5477-m77-appendix.png',(.55,.495,.94,.552)),
('roof-fish5477-cisi2-479.png','roof-fish5477-cisi2-metadata.png',(.07,.576,.41,.625)),
('roof-fish5477-cisi2-372.png','roof-fish5477-cisi2-H889.png',(.53,.16,.94,.249)),
('roof-fish5477-cisi2-372.png','roof-fish5477-cisi2-H889A.png',(.535,.169,.711,.228)),
]
def main():
 rows=[]
 for source,target,box in JOBS:
  src=ROOT/'results/primary_pages'/source; dst=ROOT/'results/primary_pages'/target
  im=Image.open(src); px=tuple(round(box[i]*(im.width if i%2==0 else im.height)) for i in range(4))
  im.crop(px).save(dst)
  rows.append({'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'output':str(dst.relative_to(ROOT)),'fractional_box':box,'pixel_box':px,'output_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'enhancement':'none'})
 (ROOT/'data/processed/roof_fish5477_crop_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
