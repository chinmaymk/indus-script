"""Preserve unretouched text-region crops from Vats original pages286–287."""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPECS = [(312, 286, (0.15, 0.611, 0.85, 0.886)),
         (313, 287, (0.15, 0.128, 0.86, 0.458))]


def pin(path):
    return {'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    out = []
    for leaf, page, fractions in SPECS:
        source = ROOT / 'data/raw' / f'pottery-text-vats-leaf{leaf}.jpg'
        image = Image.open(source)
        box = tuple(round(value * image.size[i % 2]) for i, value in enumerate(fractions))
        target = ROOT / 'data/raw' / f'pottery-text-vats-p{page}-discussion.png'
        image.crop(box).save(target)
        out.append({'parent': pin(source), 'output': pin(target),
                    'printed_page': page, 'archive_leaf': leaf,
                    'source_dimensions': list(image.size), 'crop_box_xyxy': list(box),
                    'fractional_bounds': list(fractions),
                    'operation': 'pixel crop only; no rotation, contrast change or reconstruction'})
    (ROOT / 'data/processed/vats_pottery_text_crop_manifest.json').write_text(json.dumps(out, indent=2) + '\n')


if __name__ == '__main__':
    main()
