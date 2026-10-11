"""Pin the independently reviewed Yale document/seal evidence and text extracts.

Hash verification authenticates retained files, not the ancient interpretation.
The human reviews preserve where ownership, provenance, and readings are inferred.
"""
import json
from pypdf import PdfReader
from common import ROOT, sha256, write_json


REVIEWS = [
    'data/processed/yale_anchor_parent_review.json',
    'data/processed/yale_dated_seal_review.json',
    'data/processed/gungunum_tablet_review.json',
]


def pinned_files(value):
    if isinstance(value, dict):
        if {'path', 'bytes', 'sha256'} <= value.keys():
            yield value
        for child in value.values():
            yield from pinned_files(child)
    elif isinstance(value, list):
        for child in value:
            yield from pinned_files(child)


def main():
    counts, review_hashes, unique_files = {}, {}, {}
    for name in REVIEWS:
        path = ROOT / name
        review = json.loads(path.read_text())
        items = list(pinned_files(review))
        assert items, f'No pinned evidence in {name}'
        for item in items:
            p = ROOT / item['path']
            assert p.stat().st_size == item['bytes'], item['path']
            assert sha256(p) == item['sha256'], item['path']
            if item['path'] in unique_files:
                assert unique_files[item['path']] == item['sha256'], item['path']
            unique_files[item['path']] = item['sha256']
        counts[name] = len(items)
        review_hashes[name] = sha256(path)

    extracts = {}
    for stem, pages in [('umma_old_parpola_1994', [148, 291, 292]),
                        ('yale_ricetti_2020', list(range(1, 21))),
                        ('gungunum_as16_1965', [220, 222])]:
        reader = PdfReader(ROOT / f'data/raw/{stem}.pdf')
        extracts[stem] = [(n, reader.pages[n-1].extract_text()) for n in pages]
    assert '5447' in dict(extracts['umma_old_parpola_1994'])[292]
    assert '5447' in dict(extracts['yale_ricetti_2020'])[4]
    assert 'debtor' in dict(extracts['gungunum_as16_1965'])[222]
    # Retain the full Ricetti navigation extract in its existing format.
    (ROOT / 'data/processed/yale_ricetti_2020_text.txt').write_text('\n'.join(
        f'PDFPAGE {n}\n{t}' for n, t in extracts['yale_ricetti_2020']))
    (ROOT / 'data/processed/yale_parent_selected_text.txt').write_text('\n\n'.join(
        f'SOURCE {stem}\nPDFPAGE {n}\n{text}'
        for stem, entries in extracts.items() if stem != 'yale_ricetti_2020'
        for n, text in entries))
    tablet = json.loads((ROOT / REVIEWS[2]).read_text())
    write_json('results/dated_document_bridge_audit.json', {
        'status': 'Reviewed documentary context; no authenticated Indus text alignment',
        'tablet': 'YBC 5447',
        'yale_catalogue_entry': 1090,
        'regnal_year_as_published': 'Gungunum 10',
        'proposed_sealer_in_primary_edition': 'Hatin-Ibanum, son of Apkallum',
        'sealer_attribution_status': 'Inference from contractual role; not read from the seal',
        'catalogue_identity': tablet['identity'],
        'date_evidence': tablet['date_evidence'],
        'goods_in_readable_contract': tablet['goods'],
        'catalogue_seal_epigraphy': tablet['seal_epigraphy'],
        'indus_sequence_authenticated': False,
        'indus_sign_ids_assigned': [],
        'new_semantic_values': 0,
        'new_phonetic_values': 0,
        'review_fingerprint_counts': counts,
        'review_sha256': review_hashes,
        'unique_evidence_files': len(unique_files),
        'evidence_sha256': unique_files,
        'verification_scope': 'Exact retained bytes and reproducible source extraction; not independent cuneiform collation or proof of sign meaning'
    })
    print(f'YBC5447: {len(unique_files)} unique pinned evidence files; no Indus reading established.')


if __name__ == '__main__':
    main()
