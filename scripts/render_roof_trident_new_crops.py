"""Reproduce documentary crops; no restoration, tracing or sign reconstruction."""
from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'data/raw/roof_trident_new_report_leaf302_response.bin'
im=Image.open(source)
assert im.size==(5100,6601)
boxes={
 'roof-trident-new-dhr24475-photo.png':(3270,1660,4540,2940),
 'roof-trident-new-dhr24475-entry.png':(400,1640,4590,2940),
 'roof-trident-new-dhr24475-field.png':(3290,1680,4540,2390),
}
out=[]
for name,box in boxes.items():
 p=ROOT/'results/primary_pages'/name
 im.crop(box).save(p)
 out.append({'path':str(p.relative_to(ROOT)),'box_xyxy':box,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'data/processed/roof_trident_new_crop_manifest.json').write_text(json.dumps({'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'operation':'native-resolution rectangular crop only','outputs':out},indent=2)+'\n')
