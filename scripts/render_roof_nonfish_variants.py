"""Reproduce native-pixel excerpts from the frozen non-fish variant ledger."""
import json
from PIL import Image
from common import ROOT


def main():
    review = json.loads((ROOT / 'data/processed/roof_nonfish_variant_review.json').read_text())
    for record in review['crop_records']:
        with Image.open(ROOT / record['source']) as source:
            assert list(source.size) == record['source_dimensions']
            source.crop(record['box_xyxy']).save(ROOT / record['crop'])


if __name__ == '__main__':
    main()
