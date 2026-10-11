"""Reproduce the bounded Umma provenance audit from pinned source records.

No source is joined on site name. Missing same-object/parallel-text evidence
means no authenticated anchor in this review, not demonstrated absence.
"""
import json
from html.parser import HTMLParser
from common import ROOT, sha256, write_json


class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current = None
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == 'p' and self.current is not None:
            self.rows.append(' '.join(''.join(self.current).split()))
            self.current = None


def main():
    path = ROOT / 'data/processed/umma_anchor_review.json'
    review = json.loads(path.read_text())
    old_path = ROOT / 'data/processed/umma_older_identity.json'
    old = json.loads(old_path.read_text())
    for e in review['evidence_files'] + old['evidence_files']:
        assert sha256(ROOT / e['path']) == e['sha256'], e['path']
        if 'bytes' in e:
            assert (ROOT / e['path']).stat().st_size == e['bytes'], e['path']
    parser = Paragraphs()
    parser.feed((ROOT / 'data/raw/jokha_iaa_project.html').read_text())
    survey = [p for p in parser.rows if 'Harappan' in p]
    tablet = [p for p in parser.rows if 'TJ19-2A-K54-T1' in p]
    assert len(survey) == len(tablet) == 1
    assert 'topographic survey' in survey[0]
    assert 'TJ17-PRO-S56' not in '\n'.join(parser.rows)
    identifiers = [o['review_id'] for o in review['objects']]
    assert len(identifiers) == len(set(identifiers))
    for candidate in review['candidate_joins']:
        assert candidate['left'] in identifiers and candidate['right'] in identifiers
        assert candidate['left'] != candidate['right']
        assert candidate['relationship'] == 'shared_site_label_only'
        assert candidate['same_object_authenticated'] is False
    assert old['older_object']['accession_literal'] == '1931.120'
    write_json('results/umma_anchor_audit.json', {
        'review_sha256': sha256(path),
        'older_identity_review_sha256': sha256(old_path),
        'reviewed_object_records': len(identifiers),
        'candidate_joins': review['candidate_joins'],
        'iaa_survey_paragraph': survey[0],
        'iaa_tablet_paragraph': tablet[0],
        'exact_modern_inventory_id_in_iaa_body': False,
        'primary_2017_object_page_examined': False,
        'authenticated_bilingual_anchors_in_review': 0,
        'authenticated_contents_anchors_in_review': 0,
        'new_established_sign_values': 0,
        'scope': 'Bounded provenance audit, not proof of absence across all Umma material.'
    })
    print('Umma: separate objects; survey report authenticated, exact modern ID remains a lead; no authenticated reading anchor.')


if __name__ == '__main__':
    main()
