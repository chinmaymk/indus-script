"""Join the complete LI/LII frame to metadata, without reading sign outcomes."""
import csv
import json
import re
from collections import Counter, defaultdict
from common import ROOT, sha256, write_json

METADATA_FIELDS = ('id', 'cisi', 'site', 'excavation-idno', 'room-grid',
                   'type', 'depth', 'phase')


def excavation_key(value):
    """Only an anchored number + retained alphabetic suffix; never substring match."""
    value = re.split(r'(?<![A-Z])PL\s*\.', value.upper(), maxsplit=1)[0].strip()
    value = re.sub(r'^CH\s*', '', value)
    match = re.fullmatch(r'(\d+)\s*(?:[,.-]?\s*\(?\s*([A-Z]+)\s*\)?)?', value)
    return (str(int(match[1])), match[2] or '') if match else None


def plate_key(value):
    match = re.search(r'(?<![A-Z])PL\s*\.\s*(LI|LII)\s*:+\s*(\d+)\b', value.upper())
    return f'{match[1]}.{int(match[2])}' if match else None


def provenance(value):
    sq = re.search(r'(?<![A-Za-z])sq\s*[.;]?\s*(\d+)\s*/\s*([A-Z])\b', value, re.I)
    loc = re.search(r'\bloc\s*\.?\s*(\d+)(?!\d)', value, re.I)
    return {'square': f'{int(sq[1])}/{sq[2].upper()}' if sq else None,
            'locus': str(int(loc[1])) if loc else None}


def level(value):
    match = re.fullmatch(r'\s*([+-]?\d+(?:\.\d+)?)\s*(?:ft\.?)?\s*', value)
    return float(match[1]) if match else None


def main():
    register_path = 'data/processed/chanhu_deposit_seal_register.json'
    raw_path = 'data/raw/lipi_inscriptions.csv'
    register = json.loads((ROOT/register_path).read_text())
    groups = defaultdict(list)
    with (ROOT/raw_path).open() as stream:
        for raw in csv.DictReader(stream):
            if raw['site'] == 'Chanhu-daro':
                row = {key: raw.get(key, '') for key in METADATA_FIELDS}
                groups[row['id'].split('.')[0]].append(row)
    secondary = []
    for identity, rows in sorted(groups.items()):
        keys = {excavation_key(r['excavation-idno']) for r in rows}
        secondary.append({'secondary_object_id': identity, 'rows': rows,
                          'excavation_key': next(iter(keys)) if len(keys) == 1 else None,
                          'seal_type': all(r['type'].startswith('SEAL:') for r in rows)})
    output = []
    for primary in register['rows']:
        key = excavation_key(primary['excavation_number_raw'])
        assert key is not None, primary
        all_number_candidates = [s for s in secondary if s['excavation_key'] == key]
        candidates = [s for s in all_number_candidates if s['seal_type']]
        plate_candidates = [s for s in secondary if any(plate_key(r['excavation-idno']) == primary['row_id'] for r in s['rows'])]
        accepted = [s for s in candidates if all(plate_key(r['excavation-idno']) == primary['row_id'] for r in s['rows'])]
        if len(accepted) == 1:
            status = 'unique_number_and_plate_metadata_match'
            selected = accepted[0]
        else:
            status = ('ambiguous' if len(accepted) > 1 else
                      'number_match_plate_conflict' if candidates else
                      'number_match_secondary_class_conflict' if all_number_candidates else
                      'plate_match_number_conflict' if plate_candidates else 'no_metadata_candidate')
            selected = None
        disagreements = []
        if selected:
            for row in selected['rows']:
                parsed = provenance(row['room-grid'])
                expected = {'square': primary['square_raw'], 'locus': str(primary['locus_raw']),
                            'elevation_ft': primary['elevation_ft']}
                observed = {**parsed, 'elevation_ft': level(row['depth'])}
                for field in expected:
                    if expected[field] is not None and observed[field] is not None and expected[field] != observed[field]:
                        disagreements.append({'secondary_row': row['id'], 'field': field,
                                              'primary': expected[field], 'secondary': observed[field]})
        output.append({'primary': primary, 'normalized_excavation_key': key,
                       'join_status': status,
                       'candidate_secondary_object_ids': [s['secondary_object_id'] for s in candidates],
                       'number_candidates_all_classes': all_number_candidates,
                       'plate_candidates_NOT_identity_proof': plate_candidates,
                       'selected_secondary_metadata': selected,
                       'provenance_disagreements': disagreements,
                       'text_status': 'not_assessed_in_this_metadata_only_phase'})
    summary = {'primary_catalogue_rows': len(output),
               'secondary_site_objects': len(secondary),
               'secondary_site_rows': sum(len(s['rows']) for s in secondary),
               'join_status_counts': dict(Counter(r['join_status'] for r in output)),
               'matched_rows_with_provenance_disagreements': sum(bool(r['provenance_disagreements']) for r in output),
               'provenance_field_disagreements': sum(len(r['provenance_disagreements']) for r in output),
               'secondary_phase_fields': dict(Counter(r['phase'] for s in secondary for r in s['rows'])),
               'new_sign_outcomes_examined': 0, 'semantic_values_assigned': 0}
    write_json('results/chanhu_deposit_metadata_joins.json', {
        'summary': summary, 'rows': output,
        'scope': 'LI/LII illustrated seal catalogue; an exact metadata match is not independent authentication of the secondary transcription.',
        'rules': ['Exact excavation number, alphabetic suffix and plate/item required for unique match.',
                  'Missing secondary text rows never remove primary objects.',
                  'Metadata contradictions retained; no elevation-to-phase conversion.',
                  'No strings, symbols, preservation outcomes or fish frequencies read.'],
        'input_sha256': {p: sha256(ROOT/p) for p in [register_path, raw_path, 'docs/CHANHU_DEPOSIT_PROTOCOL.md']},
    })
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
