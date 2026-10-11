"""Unretouched CISI2 page crops for M897; coordinates refer to retained renders."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'original': ('m897-cisi2-photo-120.png', (.398, .607, .645, .777)),
    'impression': ('m897-cisi2-photo-120.png', (.399, .783, .645, .961)),
    'metadata': ('m897-cisi2-meta-471.png', (.593, .396, .960, .417)),
}

def main():
    for name, (source, box) in CROPS.items():
        im = Image.open(ROOT / 'results/primary_pages' / source)
        w, h = im.size
        im.crop(tuple(int(v * (w if i % 2 == 0 else h)) for i, v in enumerate(box))).save(
            ROOT / 'results/primary_pages' / f'm897-cisi2-{name}.png')

if __name__ == '__main__':
    main()
