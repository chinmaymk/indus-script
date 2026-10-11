"""Check duplicated embedded image streams in the downloaded CISI scan.

Optional source audit requiring pypdf; separate from the statistical pipeline.
Does not count repeated scan pages as independent archaeological observations.
"""
from hashlib import sha256 as digest
from pypdf import PdfReader
from common import ROOT, sha256, write_json


def image_stream_fingerprints(page):
    objects = page['/Resources'].get('/XObject', {})
    return sorted(digest(obj.get_object().get_data()).hexdigest()
                  for obj in objects.values() if obj.get_object().get('/Subtype') == '/Image')


def main():
    source = ROOT/'data/raw/cisi_76884.pdf'
    reader = PdfReader(source)
    assert len(reader.pages) == 862, 'Review changed source pagination before proceeding'
    fingerprints = [image_stream_fingerprints(page) for page in reader.pages]
    pairs = [{'first_pdf_page': i+1, 'second_pdf_page': i+432,
              'first_image_count': len(fingerprints[i]),
              'second_image_count': len(fingerprints[i+431]),
              'image_streams_equal': bool(fingerprints[i]) and fingerprints[i] == fingerprints[i+431]}
             for i in range(431)]
    write_json('results/cisi_page_duplicate_audit.json', {
        'source': str(source.relative_to(ROOT)), 'source_sha256': sha256(source),
        'pdf_pages': len(reader.pages),
        'method': 'Compare sorted SHA256 fingerprints of pypdf get_data() image XObject streams; require nonempty images',
        'scope': 'Embedded images, not PDF object identity, text layers, or archaeological independence',
        'pairs': pairs, 'matching_pairs': sum(p['image_streams_equal'] for p in pairs)})
    print(f"{sum(p['image_streams_equal'] for p in pairs)}/431 paired pages have identical nonempty image streams")


if __name__ == '__main__':
    main()
