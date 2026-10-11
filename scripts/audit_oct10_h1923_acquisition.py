"""Reproduce the bounded H1923 acquisition record from preserved source bytes."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://www.arslibri.com/collections/PossehlLibrary1.pdf'

def pin(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def main():
    source = 'data/raw/oct10-h1923-possehl-library-authorized.pdf'
    pdf = PdfReader(ROOT / source)
    pages = {str(n): pdf.pages[n-1].extract_text() for n in (35, 76, 90, 94)}
    assert len(pdf.pages) == 145
    assert '1212 MEADOW' in pages['90'] and '(238)pp.' in pages['90']
    assert '34pp., 4 tables, 22 plates' in pages['76']
    assert '40pp., 23 plates' in pages['76']
    assert '1276 MOORCROFT' in pages['94']
    all_text = '\n'.join(page.extract_text() for page in pdf.pages)
    capture_path = 'data/raw/oct10-h1923-web-capture.json'
    capture = json.loads((ROOT / capture_path).read_text())
    queries = [q['q'] for batch in capture['batches'] for q in batch['request'].get('search_query', [])]
    assert len(queries) == 8
    sources = []
    for path, kind, url in [
        (source, 'original_public_bookseller_catalogue_pdf_not_excavation_report', URL),
        (source + '.headers.json', 'locally_serialized_HTTP_response_headers', URL),
        (capture_path, 'web_tool_capture_not_original_source_document', URL),
    ]:
        sources.append({**pin(path), 'kind': kind, 'url': url, 'research_date': '2026-10-10',
                        'refetchable': kind.startswith('original_public')})
    review = {
        'research_date': '2026-10-10',
        'outcome': 'No authenticated H1923 photograph or Figure28.01 acquired; new original catalogue locator only.',
        'source_pdf_pages': len(pdf.pages), 'selected_page_text': pages,
        'queries': queries,
        'exact_text_target_searches': {term: term in all_text for term in ('H94-2217', 'H-1923', '28.01')},
        'catalogue_version_difference': {'new_original': '13 April 2012: entry1212, printed/PDF90',
                                         'prior_scribd_capture': 'entry1276, printed94; retained unchanged'},
        'primary_image_acquired': False, 'original_report_acquired': False,
        'object_identity_authenticated': False, 'meaning_assignments': [],
        'limitations': ['Catalogue entries do not prove figure contents, current custody, report identity or availability.',
                        'Two 1994 components may reflect different versions or cataloguing error; unresolved.',
                        'No denied source URL was retried; initial DNS failure followed by authorized same public catalogue download.',
                        'No outreach, purchase or restricted download.'],
        'evidence_pins': [pin(p) for p in [source, capture_path, 'docs/H1923_REPORT_SEARCH.md',
                    'docs/H1923_PRIMARY_NUMERAL_REVIEW.md', 'docs/H1817_IDENTITY_FOLLOWUP.md',
                    'data/processed/fetch_oct10-h1923-possehl-library_pdf.json',
                    'data/processed/fetch_oct10-h1923-possehl-library-authorized_pdf.json']],
    }
    (ROOT / 'data/processed/oct10_h1923_acquisition.json').write_text(json.dumps(review, indent=2) + '\n')
    (ROOT / 'data/processed/oct10_h1923_new_sources.json').write_text(json.dumps({'sources': sources}, indent=2) + '\n')
    print(json.dumps({'sources': len(sources), 'queries': len(queries), 'pdf_pages': len(pdf.pages), 'primary_image_acquired': False}))

if __name__ == '__main__':
    main()
