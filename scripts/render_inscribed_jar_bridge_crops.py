"""Reproduce unretouched crops for the bounded jar/sealing identity review."""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    ('data/raw/capacity-context-vats-leaf279.jpg', (0.14, 0.245, 0.82, 0.365), 'vats253-target-paragraph'),
    ('data/raw/inscribed-bridge-vats-leaf191.jpg', (0.145, 0.315, 0.83, 0.51), 'vats165-5919'),
    ('data/raw/inscribed-frame-vats-leaf293.jpg', (0.46, 0.205, 0.89, 0.27), 'vats267-row116'),
    ('data/raw/inscribed-bridge-vats-plate208.png', (0.245, 0.515, 0.365, 0.615), 'vats-plateC-671'),
    ('data/raw/inscribed-bridge-m77-rule830.png', (0.045, 0.755, 0.935, 0.938), 'm77-EH-rule'),
    ('results/primary_pages/m77-u-types-numerals-137.jpg', (0.19, 0.26, 0.835, 0.318), 'm77-4671'),
]


def pin(path):
    return {'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    manifest = []
    for source, bounds, name in SPECS:
        parent = ROOT / source
        im = Image.open(parent)
        box = tuple(round(v * im.size[i % 2]) for i, v in enumerate(bounds))
        destination = ROOT / 'data/raw' / ('inscribed-bridge-' + name + '.png')
        im.crop(box).save(destination)
        manifest.append({'source': pin(parent), 'source_dimensions': list(im.size),
                         'fractional_bounds': list(bounds), 'crop_box_xyxy': list(box),
                         'output': pin(destination), 'operation': 'pixel crop only; no rotation, enhancement or reconstruction'})
    (ROOT / 'data/processed/inscribed_jar_bridge_crop_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Saved', len(manifest), 'unretouched crops')


if __name__ == '__main__':
    main()
