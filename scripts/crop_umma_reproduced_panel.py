"""Crop reproduced panel D without resampling, mirroring or enhancement."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
source='data/raw/umma-anchor-renewed-figure.webp'
out='results/primary_pages/umma-reproduced-panel-D.png'
box=(537,20,699,171)
im=Image.open(R/source)
assert im.size==(1000,924), 'Source changed; recheck panel geometry'
im.crop(box).save(R/out)
(R/'data/processed/umma_reproduced_crop_manifest.json').write_text(json.dumps({'source':source,'source_dimensions':[1000,924],'panel':'D','crop_box_pixels':box,'output':out,'output_dimensions':[162,151],'operations':['lossless PNG serialization of native decoded pixels','crop only'],'no_rotation':True,'no_mirroring':True,'no_upscaling':True,'no_restoration':True},indent=2)+'\n')
