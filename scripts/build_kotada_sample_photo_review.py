"""Bounded extraction of retained 2020 Kotada SI and visually reviewed images.

No network; raw files are immutable inputs. XML table indices are one-based.
"""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
def pin(path):
    p = ROOT / path
    return {'path': path, 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}

def main():
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    docx = 'data/raw/kotada-sample-photo-2020-si.docx'
    with ZipFile(ROOT / docx) as z:
        xml = z.read('word/document.xml')
        media = [name for name in z.namelist() if '/media/' in name]
    root = ET.fromstring(xml)
    tables = []
    for ti, table in enumerate(root.findall('.//w:tbl', ns), 1):
        rows = []
        for ri, row in enumerate(table.findall('w:tr', ns), 1):
            cells = []
            for cell in row.findall('w:tc', ns):
                paragraphs = [''.join(node.text or '' for node in p.findall('.//w:t', ns))
                              for p in cell.findall('w:p', ns)]
                cells.append('\n'.join(paragraphs))
            rows.append({'xml_row_1based': ri, 'cells': cells})
        tables.append({'xml_table_1based': ti, 'row_count': len(rows), 'rows': rows})
    target = [48, 61, 69, 106, 136, 154, 156, 167, 171, 215, 225]
    def key(label):
        return label.strip().replace('KB-', '').replace('KB', '')
    selected = []
    for t in tables:
        for row in t['rows']:
            if row['cells'] and key(row['cells'][0]) in {str(x) for x in target + [60]}:
                selected.append({'xml_table_1based': t['xml_table_1based'], **row})
    profiles = {69, 106, 156, 167, 171, 215}
    samples = []
    for k in target:
        matches = [r for r in selected if key(r['cells'][0]) == str(k)]
        samples.append({'id_2024': 'KB' + str(k), 'matches_2020': matches,
                        'figure4_visual_type': 'photographic_views_plus_profile' if k == 225 else 'reconstructed_profile' if k in profiles else 'not_depicted',
                        'identity_status': 'same_published_sample_label_in_explicitly_cited_predecessor_cohort' if matches else 'no_exact_label_match_in_2020_S1_or_S2',
                        'physical_field_register_crosswalk': None,
                        'authenticated_inscription_sequence': None})
    crops = []
    source = 'data/raw/kotada-sample-photo-2020-fig4.png'
    with Image.open(ROOT / source) as im:
        dims = list(im.size)
        for name, box in [('kb225', (407, 309, 580, 410)), ('kb173', (414, 244, 577, 311))]:
            p = 'results/primary_pages/kotada-sample-photo-' + name + '.png'
            im.crop(box).save(ROOT / p)
            crops.append({**pin(p), 'source': source, 'source_dimensions': dims,
                          'rectangle_xyxy': list(box), 'operation': 'native_pixel_crop_no_enlargement'})
    fetches = []
    sources = []
    for f in sorted((ROOT / 'data/processed').glob('fetch_kotada-sample-photo-*.json')):
        record = json.loads(f.read_text())
        fetches.append({'metadata': pin(str(f.relative_to(ROOT))), 'record': record})
        if record.get('path'):
            kind = 'original_publisher_HTTP_body' if record.get('http_status') == 200 else record['kind']
            sources.append({**pin(record['path']), 'kind': kind, 'url': record['url'], 'http_status': record.get('http_status')})
        if record.get('header_artifact'):
            sources.append({**record['header_artifact'], 'url': record['url']})
    for name in ['search', 'primary-captures']:
        p = 'data/raw/kotada-sample-photo-' + name + '.json'
        sources.append({**pin(p), 'kind': 'web_tool_result_serialization_not_HTTP_body', 'url': None})
    review = {
        'schema_version': 1, 'scope': 'Four targeted queries; public exposed 2020 article links; no further queries or blocked-source retry.',
        'conclusion': 'No authenticated inscription-content anchor recovered. Actual KB225 photo views inspected; no definite script identifiable at supplied resolution. This does not establish an uninscribed artifact.',
        '2024_figure2_pixels_inspected': False,
        '2020_publication_date': '2020-09-30',
        'cohort_scope': '2024 explicitly cites 2019/2020 earlier lipid screening; 2020 describes 2011-12 and 2012-13 sample collection. Publication sample labels do not supply excavation-register identity or independence.',
        'docx': pin(docx), 'document_xml_sha256': hashlib.sha256(xml).hexdigest(),
        'extraction': 'Original DOCX ZIP word/document.xml, direct w:tbl/w:tr/w:tc, concatenated text runs within paragraphs; one-based XML addresses; no rendered-page assumptions.',
        'table_row_counts_including_headers': [t['row_count'] for t in tables], 'embedded_media': media,
        'samples': samples, 'control_rows_KB60': [r for r in selected if key(r['cells'][0]) == '60'],
        'conflicts': [
            {'id': 'KB61_vs_KB60', 'finding': '2024 Table1 and Figure2 caption say KB61. No KB61 in 2020 S1/S2; KB60 exists. No correction or identity merge authorized.'},
            {'id': 'KB106', 'finding': 'S1: Aquatic fat; isotope cells all dashes. S2: -19.1,-24.9,-5.8; Ruminant dairy. Main article Figure3b calls KB106 possible aquatic fat, and discussion says the one aquatic sample was excluded from isotopic analysis. Preserve disagreement; no preferred values or inferred corrected label.'}
        ],
        'visual_observations': [
            {'source': source, 'locator': 'Figure4', 'dimensions': dims, 'finding': 'Mostly reconstructed profile drawings keyed by ware legend, not surface photographs. Six 2024 target IDs have profiles; KB225 has two small photographic views and profile. KB173 photo views are outside the eleven target IDs. No definite script identifiable in KB225 or KB173 shown views; small scale, limited surfaces, and no epigraphic recording make this inconclusive.'},
            {'source': 'data/raw/kotada-sample-photo-2020-fig3.png', 'locator': 'Figure3', 'finding': 'Two chromatograms only; no vessel surface photographs.'},
            {'source': 'data/raw/kotada-sample-photo-2020-si2.jpg', 'locator': 'Supplement2', 'finding': 'Isotope scatterplot, not sample photographs; not an independent resolution of S1/S2 conflicts.'}
        ],
        'crops': crops, 'fetch_attempts': fetches, 'raw_sources': sources,
        'prior_review_pins': [pin('docs/KOTADA_BHADLI_ANCHOR_FOLLOWUP.md'), pin('data/processed/kotada_anchor_followup.json')],
        'script_pin': pin('scripts/build_kotada_sample_photo_review.py'),
        'limitations': ['2024 Figure2 and its supplementary source remain unseen; earlier author/publisher blocks not retried.', 'No 2019 thesis file recovered from four searches.', 'No marks transcribed or values assigned.', 'Ten matching sample labels are not eleven confirmed physical-object joins.', 'Reconstructed drawings cannot certify absence of surface inscription.']
    }
    out = ROOT / 'data/processed/kotada_sample_photo_review.json'
    out.write_text(json.dumps(review, indent=2, ensure_ascii=False) + '\n')
    (ROOT / 'data/processed/kotada_sample_photo_new_sources.json').write_text(json.dumps({'sources': sources}, indent=2) + '\n')
    print(json.dumps({'samples': len(samples), 'S1_matches': sum(any(r['xml_table_1based'] == 1 for r in x['matches_2020']) for x in samples), 'sources': len(sources), 'crops': len(crops), 'all_pins_verified': all(pin(s['path'])['sha256'] == s['sha256'] for s in sources + crops)}))

if __name__ == '__main__':
    main()
