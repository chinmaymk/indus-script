"""Unretouched review crops; no restoration, sharpening, rotation or reflection."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    ('data/raw/h133_vats_leaf79.jpg', 'h133-vats-metadata-detail.png', (.16, .687, .845, .748)),
    ('results/primary_pages/h133-vats-192.png', 'h133-vats-261-detail.png', (.12, .125, .35, .212)),
    ('results/primary_pages/h133-m77-115.png', 'h133-m77-4261-detail.png', (.21, .591, .855, .624)),
    ('results/primary_pages/h133-m77-45.png', 'h133-m77-M226-detail.png', (.588, .085, .665, .157)),
    ('results/primary_pages/h133-m77-830.png', 'h133-m77-EH-rule-detail.png', (.047, .774, .486, .92)),
]

for source, name, box in SPECS:
    im = Image.open(ROOT / source)
    coords = tuple(round(v * (im.width if i % 2 == 0 else im.height)) for i, v in enumerate(box))
    im.crop(coords).save(ROOT / 'results/primary_pages' / name)
