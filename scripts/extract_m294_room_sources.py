#!/usr/bin/env python3
"""Extract page-linked original room evidence; raw downloads are immutable inputs."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from pypdf import PdfReader
ROOT = Path(__file__).resolve().parents[1]

def main():
    xml_source = 'data/raw/m294_marshall722_djvu.xml'
    objects = ET.parse(ROOT / xml_source).findall('.//OBJECT')
    pages = []
    for leaf, printed in [(229,187),(231,189),(235,193),(236,194),(237,195)]:
        text = ' '.join(' '.join(objects[leaf].itertext()).split())
        pages.append({'source':xml_source,'archive_leaf':leaf,'printed_page':printed,'text':text,'warning':'Archive OCR; manually checked image supersedes text'})
    source = 'data/raw/stone1471_marshall1931_volume2_text.pdf'
    reader = PdfReader(ROOT / source)
    for pdf_page, printed in [(27,376),(144,493),(173,522)]:
        pages.append({'source':source,'pdf_page':pdf_page,'printed_page':printed,'text':reader.pages[pdf_page-1].extract_text(),'warning':'Embedded OCR; manually checked rendered image supersedes text'})
    out = ROOT / 'results/m294_room_source_extracts.json'
    out.write_text(json.dumps({'pages':pages},indent=2)+'\n')
    print(f'Wrote {len(pages)} page extracts to {out.relative_to(ROOT)}')

if __name__ == '__main__':
    main()
