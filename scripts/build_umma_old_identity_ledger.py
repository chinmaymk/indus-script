#!/usr/bin/env python3
"""Fingerprint the bounded older Umma object audit; does not infer sign readings."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-09-24'


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    urls = {
        'umma_old_archive_search.json': ('https://archive.org/advancedsearch.php?q=title%3A%28Revue+assyriologie%29+AND+year%3A1925&output=json', 'download'),
        'umma_old_archive_search_broad.json': ('https://archive.org/advancedsearch.php?q=title%3A%28%22Revue+d%27assyriologie%22%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=100&output=json', 'download'),
        'umma_old_archive_collection_search.json': ('https://archive.org/advancedsearch.php?q=collection%3Apub_revue-dassyriologie-et-darcheologie-orientale+AND+year%3A1925&fl%5B%5D=identifier&fl%5B%5D=title&rows=50&output=json', 'download'),
        'umma_old_archive_wildcard_search.json': ('https://archive.org/advancedsearch.php?q=identifier%3A%2Arevue%2A+AND+year%3A1925&fl%5B%5D=identifier&fl%5B%5D=title&rows=250&output=json', 'download'),
        'umma_old_parpola_1994.pdf': ('https://www.sindhilanguagelibrary.com/assets/documents/pdf/647f088f1fff3.pdf', 'download'),
        'umma_old_scheil_jstor_response.bin': ('https://www.jstor.org/stable/pdf/23290782.pdf', 'archived_http_response'),
        'umma_old_tosi_harappa.html': ('https://www.harappa.com/blog/indus-seal-impression-umma-mesopotamia', 'archived_http_response'),
        'umma_old_tosi_web_capture.json': ('https://www.harappa.com/blog/indus-seal-impression-umma-mesopotamia', 'web_extraction_capture'),
        'umma_old_scheil_bibliography_web_capture.json': ('https://www.jstor.org/stable/i23283221', 'web_extraction_capture'),
    }
    sources = []
    for filename, (url, kind) in urls.items():
        row = fingerprint('data/raw/' + filename)
        row.update(url=url, kind=kind, retrieved_date=DATE)
        if kind == 'archived_http_response':
            row['status'] = 'Challenge/error HTML; requested research content not retrieved; HTTP status not captured.'
        sources.append(row)
    (ROOT / 'data/processed/umma_old_downloads.json').write_text(json.dumps({'sources': sources}, indent=2) + '\n')
    review = {
        'review_date': DATE,
        'status': 'Bounded identity audit; no decipherment; official accession record and full Scheil article not recovered',
        'older_object': {
            'm77_reference': '9811',
            'm77_site_label': 'Djoka (Umma)',
            'object_type': 'clay sealing / clay tag',
            'accession_literal': '1931.120',
            'institution': 'Ashmolean Museum, Oxford',
            'accession_evidence': 'Parpola1994 printed113/PDF131 Fig7.16 caption, visually verified',
            'official_museum_record_recovered': False,
            'scheil_citation': 'V. Scheil, Revue d\u2019Assyriologie22(2),1925,55–56; JSTOR23290782',
            'scheil_full_article_recovered': False,
            'reported_acquisition': 'Tosi account quoted on Harappa: dealer delivery to Louvre before WWI; transfer to Ashmolean1931',
            'findspot_status': 'dealer-attributed Jhoka, explicitly unconfirmed in Tosi account',
            'excavation_context_authenticated': False,
            'reverse_observation': 'Published photo and caption support cloth impression',
            'reverse_interpretation': 'Tosi reconstructs cloth-covered jar mouth, string and knot cavity',
            'cotton_fiber_authenticated': False,
            'container_contents': None,
            'quantity': None,
            'cuneiform_on_same_object_authenticated': False,
            'cuneiform_absence_scope': 'No cuneiform identified in reviewed descriptions or two published views; not complete surface autopsy',
            'glyph_count_discrepancy': {'m77_candidate_code_count': 5, 'tosi_reported_count': 6, 'resolved': False},
            'semantic_value': None,
            'phonetic_value': None,
        },
        'excluded_identity_matches': [
            {'identifier': 'TJ17-PRO-S56', 'reason': '2017 case handled separately; not joined to older published object'},
            {'identifier': 'EAMd.13', 'reason': 'Museum search result is unrelated Mohenjo-daro triangular prism'},
        ],
        'manual_visual_review': [{'path': 'results/primary_pages/umma-old-parpola-p113.png', 'pdf_page': 131, 'printed_page':113, 'result': 'Accession and clay/cloth caption legible; patterned reverse; Indus obverse'}],
        'unresolved': ['Official Ashmolean accession register', 'Original Scheil article full text', 'Louvre inventory and acquisition record', 'Exact excavated provenance', 'Five versus six sign segmentation'],
        'evidence_files': sources + [fingerprint('results/primary_pages/umma-old-parpola-p113.png'), fingerprint('data/processed/m77_foreign_selection_review.json')],
    }
    review['glyph_count_followup'] = {
        'status': 'Five M77 catalogue units verified; Tosi six-report cause unresolved',
        'm77_primary_row': {'printed_page':160, 'pdf_page':171, 'reference':'9811', 'normalized_right_to_left':['M029','M336','M099','M104','M162']},
        'export_matches_primary_row': True,
        'primary_sign_list_checked': {'M029':32,'M336':35,'M099':32,'M104':32,'M162':33},
        'grouping_observation': 'M029 complex figure and M336 internally marked U are each single numbered signs; stroke groups M099 and M104 are single units too.',
        'tosi_six_specific_explanation_authenticated': False,
        'photograph_limit': 'Halftone and shadow limit remaining-field reading; no securely separate or damaged sixth glyph established. Enlargement adds no original detail.',
        'orientation_caution': 'Apparent spatial arrangement in Parpola photograph opposite normalized M77 row. No source reversal or original photographic-orientation decision.',
        'authority_edited': False,
        'viewed_images': [
            'results/primary_pages/umma-old-m77-p160.png',
            'results/primary_pages/umma-old-m77-9811-crop.png',
            'results/primary_pages/umma-old-obverse-crop.png',
            'results/primary_pages/sign_list_page_32.png',
            'results/primary_pages/sign_list-044.png',
            'results/primary_pages/sign_list-045.png',
            'results/primary_pages/sign_list-046.png',
        ] + ['IM_417_150_PNG/' + str(n) + '.png' for n in (29,336,99,104,162)],
        'render_and_crop': {
            'parpola_detail': {'pdf_page':131, 'scale_to':4800, 'render_path':'results/primary_pages/umma-old-parpola-p113-detail.png', 'crop_fraction_ltrb':[.47,.08,.79,.29]},
            'm77_row': {'pdf_page':171, 'scale_to':2800, 'render_path':'results/primary_pages/umma-old-m77-p160.png', 'crop_fraction_ltrb':[.235,.448,.87,.48]},
            'crop_note': 'PIL.Image.crop with int(width*fraction) and int(height*fraction); no sharpening, contrast adjustment, rotation or mirroring.'
        },
    }
    review['evidence_files'] += [fingerprint(p) for p in review['glyph_count_followup']['viewed_images']]
    review['evidence_files'] += [fingerprint('results/primary_pages/umma-old-parpola-p113-detail.png'),fingerprint('data/processed/m77_candidate_records.jsonl')]
    (ROOT / 'data/processed/umma_older_identity.json').write_text(json.dumps(review, indent=2) + '\n')
    print(json.dumps({'source_records':len(sources), 'source_bytes':sum(x['bytes'] for x in sources), 'museum_record_recovered': False, 'same_object_bilingual_authenticated': False}))


if __name__ == '__main__':
    main()
