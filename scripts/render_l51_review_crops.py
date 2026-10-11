"""Reproduce evidence crops for L-51; no image reconstruction or enhancement."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = [
    ('l51-cisi-285.png', 'l51-review-original.png', (0.04, .77, .29, .95)),
    ('l51-cisi-285.png', 'l51-review-impression.png', (.69, .765, .94, .95)),
    ('l51-bulletin-25.png', 'l51-review-claim.png', (.1, .85, .9, .93)),
    ('l51-bulletin-25.png', 'l51-review-comparison.png', (.54, .46, .82, .77)),
    ('l51-cisi-metadata-408.png', 'l51-review-metadata.png', (.55, .425, .88, .445)),
]

if __name__ == '__main__':
    for source, output, fractions in CROPS:
        im = Image.open(ROOT / 'results/primary_pages' / source)
        w, h = im.size
        box = tuple(int(v * d) for v, d in zip(fractions, (w, h, w, h)))
        im.crop(box).save(ROOT / 'results/primary_pages' / output)
        print(output, box)
