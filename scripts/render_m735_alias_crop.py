"""Crop the observed CISI2 M735 basic-data row without enhancement."""
from PIL import Image
from common import ROOT

if __name__ == '__main__':
    with Image.open(ROOT / 'results/primary_pages/h843-cisi2-key-470.png') as im:
        box = (.56, .39, .935, .415)
        pixels = tuple(round(v * (im.width if i % 2 == 0 else im.height)) for i, v in enumerate(box))
        im.crop(pixels).save(ROOT / 'results/primary_pages/m735-cisi2-alias-detail.png')
