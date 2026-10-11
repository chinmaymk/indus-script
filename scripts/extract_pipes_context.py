"""Extract the bounded primary Kalibangan pipe passages (requires pypdf).

Original downloaded PDFs remain in data/raw. PDF pages are one-based, not
printed page numbers. Rendering can be repeated with inspect_research_pdf.py.
"""
from pathlib import Path
import json
import hashlib
from pypdf import PdfReader
ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('data/raw/pipes_kalibangan_excavation_2015_part1.pdf', [96, 98, 99]),
    ('data/raw/pipes_asi_download61.pdf', [247, 248, 249, 250]),
    ('data/raw/metal_kalibangan_excavation_2020_part2.pdf', [362, 363, 364, 365]),
]

def main():
    entries = []
    parts = []
    for rel, pages in SOURCES:
        path = ROOT / rel
        r = PdfReader(path)
        entries.append({'path': rel, 'bytes': path.stat().st_size,
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'pdf_pages_one_based': pages, 'page_count': len(r.pages)})
        for page in pages:
            parts.append(f'\n--- {rel}: PDF PAGE {page} ---\n' + (r.pages[page-1].extract_text() or ''))
    (ROOT/'results/pipes_primary_context_extracted.txt').write_text(''.join(parts))
    (ROOT/'results/pipes_primary_context_extraction.json').write_text(json.dumps({
        'extractor': 'pypdf', 'sources': entries,
        'warning': 'Extraction is not a substitute for visual verification; images and human evidence pins are separate.'
    }, indent=2) + '\n')
    print(f'Extracted {sum(len(p) for _,p in SOURCES)} selected PDF pages.')

if __name__ == '__main__':
    main()
