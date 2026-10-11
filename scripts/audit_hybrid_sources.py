"""Reproduce source extraction and pin the limited comparative seal evidence."""
import json
from pypdf import PdfReader
from common import ROOT, sha256, write_json


def main():
    review_path = ROOT / 'data/processed/hybrid_source_review.json'
    review = json.loads(review_path.read_text())
    bm_path = ROOT / 'data/processed/bm120573_cuneiform_review.json'
    bm = json.loads(bm_path.read_text())
    bm2_path = ROOT / 'data/processed/bm122187_review.json'
    bm2 = json.loads(bm2_path.read_text())
    for e in (review['evidence_files'] + bm['source_fingerprints'] + bm['review_image_fingerprints']
              + bm2['source_fingerprints'] + bm2['review_image_fingerprints']
              + bm2['prior_review_fingerprints']):
        assert sha256(ROOT / e['path']) == e['sha256'], e['path']
        assert (ROOT / e['path']).stat().st_size == e['bytes'], e['path']
    prior = json.loads((ROOT / 'data/processed/m77_foreign_primary_parent_review.json').read_text())
    row = next(x for x in prior['rows'] if x['reference'] == bm2['identifiers']['mahadevan_1977_reference'])
    assert row['sequence'] == bm2['inscription']['sequence']
    assert row['metadata'] == bm2['inscription']['metadata']
    assert len(row['sequence']) == bm2['inscription']['gadd_character_count']
    pages = {}
    for stem in ['hybrid_vidale_2005', 'hybrid_frenez_cv']:
        reader = PdfReader(ROOT / f'data/raw/{stem}.pdf')
        texts = [p.extract_text() for p in reader.pages]
        pages[stem] = texts
        text = ('\n'.join('PDFPAGE '+str(i+1)+'\n'+p for i,p in enumerate(texts))
                if stem == 'hybrid_vidale_2005' else '\n'.join(texts))
        (ROOT / f'data/processed/{stem}_text.txt').write_text(text)
    assert 'Papers in preparation' in pages['hybrid_frenez_cv'][6]
    assert 'Hybrid identities' in pages['hybrid_frenez_cv'][6]
    assert 'July 10th 2024' in '\n'.join(pages['hybrid_frenez_cv'])
    assert '361, footnote' in pages['hybrid_vidale_2005'][6]
    assert 'family sequences' in pages['hybrid_vidale_2005'][10]
    write_json('results/hybrid_source_audit.json', {
        'source_review_sha256': sha256(review_path),
        'bm_review_sha256': sha256(bm_path),
        'bm_provisional_reading': bm['gadd1932']['provisional_reading'],
        'bm_reading_is_translation': bm['gadd1932']['reading_is_translation'],
        'bm122187_review_sha256': sha256(bm2_path),
        'bm122187_identifiers': bm2['identifiers'],
        'bm122187_sequence': bm2['inscription']['sequence'],
        'bm122187_context': bm2['context'],
        'bm122187_semantic_anchor': bm2['semantic_anchor'],
        'source_pdf_pages': {k: len(v) for k,v in pages.items()},
        'paris_object': review['paris_object'],
        'cv_publication_status': review['cv_publication_status'],
        'source_claims_are_not_independent_collations': True,
        'new_established_indus_sign_values': 0
    })
    print('Hybrid seal sources: Paris patronymic reading remains attributed and preliminary; no corresponding Indus text.')


if __name__ == '__main__':
    main()
