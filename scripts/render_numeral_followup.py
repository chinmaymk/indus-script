"""Reproduce the bounded primary numeral-pattern review images.

Requires pypdf, Pillow and Poppler. Crops magnify pixels only; they do not repair
or redraw signs. Manual observations live in numeral_primary_followup.json.
"""
import argparse
import subprocess
import sys
from PIL import Image
from common import ROOT

PAGES = [52, 81, 82, 825, 827]
CROPS = {52: (950, 135, 1570, 245), 82: (1120, 650, 1570, 780)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdftoppm', required=True)
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT/'scripts/inspect_research_pdf.py'),
        'mahadevan_1977_text.pdf', '--prefix', 'numeral-followup',
        '--pages', *map(str, PAGES), '--render-only', '--scale', '2600',
        '--pdftoppm', args.pdftoppm], check=True)
    for page, box in CROPS.items():
        source = ROOT/f'results/primary_pages/numeral-followup-{page}.png'
        with Image.open(source) as im:
            crop = im.crop(box)
            crop.resize((crop.width*3, crop.height*3), Image.Resampling.BICUBIC).save(
                source.with_name(f'numeral-followup-{page}-detail.png'))


if __name__ == '__main__':
    main()
