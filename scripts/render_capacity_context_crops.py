"""Retain exact pixel crops of Vats's context and split table; no enhancement."""
from PIL import Image
from common import ROOT, sha256, write_json

BOXES = [
    ('data/raw/capacity-context-vats-leaf280.jpg', 'table-rows1-3-left', (670,1460,5190,2570)),
    ('data/raw/capacity-context-vats-leaf281.jpg', 'table-rows1-3-right', (530,1470,5080,2530)),
    ('data/raw/capacity-context-vats-leaf280.jpg', 'table-row18-left', (670,5280,5190,5760)),
    ('data/raw/capacity-context-vats-leaf281.jpg', 'table-row18-right', (530,5440,5080,5790)),
]

def main():
    records=[]
    for source,label,box in BOXES:
        output=f'results/primary_pages/capacity-context-{label}.png'
        with Image.open(ROOT/source) as im:
            im.crop(box).save(ROOT/output)
        records.append(dict(source=source, source_sha256=sha256(ROOT/source),
                            box_xyxy=box, output=output, output_sha256=sha256(ROOT/output),
                            operation='crop only; neighboring rows may be included'))
    write_json('data/processed/capacity_context_crop_manifest.json',records)

if __name__=='__main__': main()
