"""Pin visually checked primary recording-method evidence; no sign inference."""
import json
from common import ROOT, sha256, write_json


def main():
    paths = ['data/raw/chanhu-methods-leaf10.jpg',
             'data/raw/chanhu-methods-leaf11.jpg',
             'data/raw/c40_mackay1943_djvu.txt',
             'docs/CHANHU_RECORDING_METHOD_REVIEW.md',
             'docs/CHANHU_DEPOSIT_PROTOCOL.md']
    write_json('data/processed/chanhu_recording_method_review.json', {
        'review_date': '2026-09-28',
        'printed_pages': ['vi', 'vii'],
        'method': 'Parent visual inspection of complete original page images.',
        'locus_number_alone_identifies_deposit': False,
        'locus_positions_carried_across_excavation_levels': True,
        'field_cards_reported_approximately': 5000,
        'field_card_archive_located': False,
        'card_count_is_seal_count': False,
        'working_datum_ft_above_reported_sea_level': 100.45,
        'grid_square_side_ft': 50,
        'semantic_values_assigned': 0,
        'phonetic_values_assigned': 0,
        'evidence_files': [{'path': p, 'bytes': (ROOT/p).stat().st_size,
                            'sha256': sha256(ROOT/p)} for p in paths],
    })
    records = []
    for n in (10, 11):
        m = json.loads((ROOT/f'data/processed/fetch_chanhu-methods-leaf{n}_jpg.json').read_text())
        assert m['response_complete'] and m['http_status'] == 200
        records.append({k: v for k, v in m.items() if k != 'header_artifact'})
        records[-1]['kind'] = 'downloaded_original_page_scan_JPEG'
        records.append({**m['header_artifact'], 'url': m['url']})
    write_json('data/processed/chanhu_methods_new_sources.json', {'sources': records})


if __name__ == '__main__':
    main()
