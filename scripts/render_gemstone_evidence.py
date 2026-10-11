"""Recreate the retained gemstone-audit page images and unretouched crops."""
import argparse
import json
import subprocess
from PIL import Image
from common import ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdftoppm', required=True)
    args = parser.parse_args()
    dest = ROOT/'results/primary_pages'
    for source, pages, prefix in [
        ('vats_1940_plates_9842.pdf', [190,194,198,200,202,204,208,210], 'gemstone-vats-plate-'),
        ('irc_2025_fish_bulletin.pdf', [17], 'gemstone-bulletin-p11')]:
        for n in pages:
            output = dest/(prefix+str(n) if prefix.endswith('-') else prefix)
            subprocess.run([args.pdftoppm, '-f', str(n), '-l', str(n), '-scale-to', '2000',
                            '-png', '-singlefile', str(ROOT/'data/raw'/source), str(output)], check=True)
    thumbnails = []
    for n, leaf in [(58,84),(59,85),(60,86),(435,463)]:
        thumbnails.append((f'vats_1940_text_p{n}_leaf{leaf}.jpg', f'gemstone-vats-p{n}.png', (1900,2100)))
    thumbnails.extend([
        ('vats_1940_text_p346_leaf374.jpg', 'gemstone-vats-leaf374.png', (2000,2400)),
        ('vats_1940_text_p348_leaf376.jpg', 'gemstone-vats-table-376.png', (2200,2600)),
        ('vats_1940_holdout_leaf373.jpg', 'gemstone-vats-table-373.png', (2200,2600)),
        ('vats_1940_holdout_leaf377.jpg', 'gemstone-vats-table-377.png', (2200,2600))])
    for source, output, size in thumbnails:
        im = Image.open(ROOT/'data/raw'/source)
        im.thumbnail(size)
        im.save(dest/output)
    for spec in json.loads((ROOT/'data/processed/gemstone_crop_boxes.json').read_text()):
        im = Image.open(ROOT/spec['source']).crop(spec['box'])
        factor = spec['resize_factor']
        if factor != 1:
            im = im.resize((im.width*factor, im.height*factor))
        im.save(ROOT/spec['destination'])
    im = Image.open(dest/'gemstone-vats-plate-200.png')
    im.crop((0,1650,1524,1850)).resize((2286,300)).save(dest/'gemstone-plate-bottom-navigation.png')


if __name__ == '__main__':
    main()
