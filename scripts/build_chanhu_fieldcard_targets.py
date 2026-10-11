"""Turn published conflicts into archive navigation targets, never card evidence."""
import json
from common import ROOT, sha256, write_json


def main():
    paths = ['results/chanhu_deposit_metadata_joins.json',
             'data/processed/chanhu_fieldcard_archive_search.json']
    joins, archive = [json.loads((ROOT/p).read_text()) for p in paths]
    ranges = archive['catalogued_holding']['card_catalogue_ranges']
    context = {
        '2285': 'Room 215 +10.4-ft seal versus unfinished-bead floor +9.3 ft; seek stratigraphic association.',
        '2428': 'Passage 286 floor; check relation to room 215 production horizon.',
        '2529': 'Courtyard 297 spread; preserve CC suffix and distinguish buried pan 2596.',
        '2297': 'Narrative slightly below +6.8-ft beads versus catalogue +10.0 ft.',
        '2558': 'Archaeological fragment absent from secondary export; establish surviving text only from evidence.',
        '3207': 'Catalogue +7.7 ft versus narrative near +6.7-ft bath floor; assess event association.',
        '2390': 'Locus 235 +9.9-ft seal near, not identical to, buried metal hoard 284 +9.5 ft.',
    }
    targets = []
    for row in joins['rows']:
        number, suffix = row['normalized_excavation_key']
        reasons = []
        if number in context:
            reasons.append(context[number])
        if row['provenance_disagreements']:
            reasons.append('Resolve primary/secondary location or signed-level discrepancies: ' +
                           json.dumps(row['provenance_disagreements'], sort_keys=True))
        if row['join_status'] in ('plate_match_number_conflict', 'number_match_secondary_class_conflict'):
            reasons.append(row['join_status'] + '; candidate metadata preserved separately, not merged.')
        if not reasons:
            continue
        boxes = [r['box'] for r in ranges if r['lower'] <= int(number) <= r['upper']]
        assert len(boxes) == 1
        targets.append({'primary_row': row['primary']['row_id'],
                        'excavation_number': number, 'suffix': suffix,
                        'candidate_card_box': boxes[0], 'reasons': reasons,
                        'register_and_site_level_notebooks_box': 2,
                        'individual_card_presence_verified': False,
                        'card_contents_acquired': False,
                        'suffix_filing_verified': False if suffix else None})
    write_json('results/chanhu_fieldcard_targets.json', {
        'repository': archive['catalogued_holding'],
        'targets': targets, 'target_count': len(targets),
        'scope': 'Numeric-range navigation for published conflicts and test-critical associations; no contact or archival images acquired.',
        'selection_independent_of_new_sign_counts': True,
        'input_sha256': {p: sha256(ROOT/p) for p in paths},
    })
    print(f'{len(targets)} archive navigation targets; zero card contents acquired.')


if __name__ == '__main__':
    main()
