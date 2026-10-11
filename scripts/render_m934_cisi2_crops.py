"""Unretouched CISI2 M934 evidence crops; preserves earlier frozen review files."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = [
    ('m934-cisi2-meta-471.png', 'm934-cisi2-meta-detail.png', (.58, .778, .93, .811)),
    ('m934-cisi2-photo-125.png', 'm934-cisi2-original.png', (.063, .594, .294, .785)),
    ('m934-cisi2-photo-125.png', 'm934-cisi2-impression.png', (.302, .60, .535, .787)),
]
for source, target, box in CROPS:
    im = Image.open(ROOT / 'results/primary_pages' / source)
    bounds = tuple(round(v * (im.width if i % 2 == 0 else im.height)) for i, v in enumerate(box))
    im.crop(bounds).save(ROOT / 'results/primary_pages' / target)
