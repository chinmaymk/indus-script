"""Unretouched Appendix I crops for roof-candidate base variants."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'M059': ('roof-variants-locate-801.png', (.535, .166, .93, .229)),
    'M060': ('roof-variants-locate-795.png', (.14, .344, .54, .409)),
    'M089': ('roof-variants-locate-795.png', (.542, .403, .947, .474)),
}

def main():
    for name, (source, box) in CROPS.items():
        im = Image.open(ROOT / 'results/primary_pages' / source)
        im.crop(tuple(round(v * (im.width if i % 2 == 0 else im.height)) for i, v in enumerate(box))).save(
            ROOT / 'results/primary_pages' / f'roof-variants-{name}.png')

if __name__ == '__main__':
    main()
