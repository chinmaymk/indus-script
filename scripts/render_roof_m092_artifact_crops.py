"""Persist unaltered excerpt/rotation coordinates for M77 8018 artifact review."""
from pathlib import Path
import hashlib
import json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
JOBS=[
 ('roof-m092-artifact-m77-836.png','roof-m092-artifact-m77-identity.png',(0.04,0.665,0.455,0.745),0),
 ('roof-m092-artifact-cisi-410.png','roof-m092-artifact-cisi-identity.png',(0.05,0.682,0.43,0.725),0),
 ('roof-m092-artifact-cisi-photo-340.png','roof-m092-artifact-cisi-K29.png',(0.045,0.05,0.70,0.29),0),
 ('roof-m092-artifact-klb-photo-161.png','roof-m092-artifact-klb-figure29.png',(0.12,0.37,0.875,0.68),-90),
]
def main():
 ledger=[]
 for source,target,box,angle in JOBS:
  src=ROOT/'results/primary_pages'/source; dest=ROOT/'results/primary_pages'/target
  im=Image.open(src); px=tuple(round(box[i]*(im.width if i%2==0 else im.height)) for i in range(4))
  crop=im.crop(px)
  if angle: crop=crop.rotate(angle,expand=True)
  crop.save(dest)
  ledger.append({'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'output':str(dest.relative_to(ROOT)),'fractional_crop':box,'pixel_crop':px,'counterclockwise_degrees':angle,'output_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
 (ROOT/'data/processed/roof_m092_artifact_crop_manifest.json').write_text(json.dumps(ledger,indent=2)+'\n')
if __name__=='__main__':main()
