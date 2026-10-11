"""Verify retained Bahrain evidence and reproduce primary-page text extraction.

This audits provenance and scope, not ancient readings or semantic correctness.
It deliberately keeps the old name list, Gulf seals and 2026 tokens separate.
"""
import json
from pypdf import PdfReader
from common import ROOT, sha256, write_json
from audit_dated_document_bridge import pinned_files


REVIEWS = [
    'data/processed/bahrain_parent_review.json',
    'data/processed/bahrain_tablet_context_review.json',
    'data/processed/bahrain_2026_review.json',
]


def main():
    evidence, counts, reviews = {}, {}, {}
    for name in REVIEWS:
        review = json.loads((ROOT / name).read_text())
        reviews[name] = review
        pins = list(pinned_files(review))
        assert pins, name
        for item in pins:
            path = ROOT / item['path']
            assert path.stat().st_size == item['bytes'], item['path']
            assert sha256(path) == item['sha256'], item['path']
            assert item['path'] not in evidence or evidence[item['path']] == item['sha256']
            evidence[item['path']] = item['sha256']
        counts[name] = len(pins)

    parpola = PdfReader(ROOT / 'data/raw/umma_old_parpola_1994.pdf')
    (ROOT / 'data/processed/bahrain_parent_parpola_text.txt').write_text('\n\n'.join(
        f'PDFPAGE {n}\n{parpola.pages[n-1].extract_text()}' for n in [29, 148]))
    gelb = PdfReader(ROOT / 'data/raw/bahrain_gelb_1980_as21.pdf')
    text = gelb.pages[17].extract_text()
    assert 'rough copy' in text and 'third being the son of the first' in ' '.join(text.split())
    # Keep a machine-produced navigation extract separate from the reviewed one.
    (ROOT / 'data/processed/bahrain_gelb_reproduced_extract.txt').write_text(text)
    old = reviews[REVIEWS[1]]
    new = reviews[REVIEWS[2]]
    write_json('results/bahrain_anchor_audit.json', {
        'status': 'No independently authenticated cuneiform-to-Indus alignment',
        'old_tablet': {
            'published_reading': old['primary_transliteration'],
            'source_basis': old['primary_source_basis'],
            'relationship': old['relationship_attributed_to_gelb'],
            'excavation_id': old['tablet_excavation_id'],
            'associated_seal_id': old['associated_seal_id'],
            'distance': old['relative_distance'],
        },
        'gulf_seal_catalogue_crosswalk': reviews[REVIEWS[0]]['crosswalk'],
        'crosswalk_scope': 'Web-extracted catalogue references; illustrations not inspected',
        'tokens_2026': {
            'full_article_recovered': new['primary_full_article_recovered'],
            'epigraphy_from_abstract': new['evidence']['author_repository_abstract'],
            'indus_anchor': new['indus_anchor'],
        },
        'new_semantic_values': 0,
        'new_phonetic_values': 0,
        'review_fingerprint_counts': counts,
        'unique_evidence_files': len(evidence),
        'evidence_sha256': evidence,
        'review_sha256': {name: sha256(ROOT / name) for name in REVIEWS},
        'verification_scope': 'Exact file integrity and reproducible extraction; not cuneiform collation or proof of an interpretation',
    })
    print(f'Bahrain: {len(evidence)} unique evidence files; old name list and new tokens remain distinct.')


if __name__ == '__main__':
    main()
