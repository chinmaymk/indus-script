"""Audit the counting unit in the Harappa8650 fish/gemstone argument.

Does not translate signs, infer fish membership from photographs, or estimate
enrichment without a matched reference population. All source readings excluded.
"""
import csv
import json
import math
from collections import defaultdict
from common import ROOT, sha256, write_json

FIELDS = ('id', 'cisi', 'site', 'excavation-idno', 'sides', 'preservation',
          'condition', 'dir.', 'text', 'material', 'phase', 'depth')


def exact_catalogue_join(rows, catalogue):
    """Match literal excavation+plate identifiers; never collapse by find group."""
    eligible = {r['find_number'] + str(r['eh_item']): r for r in catalogue}
    objects = defaultdict(list)
    for row in rows:
        if row['site'] == 'Harappa' and row['excavation-idno'] in eligible:
            objects[row['id'].split('.')[0]].append({k: row.get(k, '') for k in FIELDS})
    output = []
    for key, lines in sorted(objects.items()):
        identities = {r['excavation-idno'] for r in lines}
        if len(identities) != 1:
            raise ValueError('Conflicting excavation identity within secondary object group')
        source = eligible[next(iter(identities))]
        output.append({'secondary_object_id': key, 'eh_item': source['eh_item'],
                       'find_number': source['find_number'], 'lines': lines,
                       'full_raw_text_signature': sorted(r['text'] for r in lines),
                       'fish_presence_independently_verified': None,
                       'all_faces_independently_verified': False})
    return output


def binomial_tail(n, k, p):
    """Hypothetical sensitivity only; no empirical baseline supplied here."""
    if not (isinstance(n, int) and isinstance(k, int) and 0 <= k <= n and 0 <= p <= 1):
        raise ValueError('Invalid binomial arguments')
    return sum(math.comb(n, j) * p**j * (1-p)**(n-j) for j in range(k, n+1))


def main():
    paths = ['data/processed/gemstone_context_protocol.json',
             'data/processed/gemstone_primary_review.json', 'data/raw/lipi_inscriptions.csv']
    protocol = json.loads((ROOT/paths[0]).read_text())
    primary = json.loads((ROOT/paths[1]).read_text())
    for pin in primary['evidence_files']:
        path = ROOT/pin['path']
        assert path.stat().st_size == pin['bytes'] and sha256(path) == pin['sha256'], pin['path']
    with (ROOT/paths[2]).open() as f:
        rows = list(csv.DictReader(f))
    catalogue = primary['b_group_exact_catalogue_rows']
    joined = exact_catalogue_join(rows, catalogue)
    signatures = {tuple(r['full_raw_text_signature']) for r in joined}
    summary = {
        'primary_b_group_numbered_plate_entries': len(catalogue),
        'secondary_matched_object_groups': len(joined),
        'secondary_matched_rows': sum(len(o['lines']) for o in joined),
        'secondary_distinct_raw_multiline_signatures': len(signatures),
        'same_b_group_is_one_identical_inscription_supported': False,
        'corrected_complete_assemblage_fish_numerator': None,
        'corrected_complete_assemblage_type_denominator': None,
        'matched_control_probability': None,
        'empirical_enrichment_test': None,
        'established_semantic_values': 0, 'established_phonetic_values': 0}
    write_json('results/gemstone_context_audit.json', {
        'protocol': protocol, 'summary': summary, 'primary_review': primary,
        'secondary_exact_join': joined,
        'hypothetical_sensitivity_not_empirical_p_values': [
            {'assumed_independent_type_probability': p, 'P_X_ge_4_of_6': binomial_tail(6, 4, p)}
            for p in (0.2, 0.3, 0.4, 0.5)],
        'input_sha256': {p: sha256(ROOT/p) for p in paths},
        'limits': ['Exact secondary raw strings are not authenticated fine sign transcriptions.',
                   'Seven numbered illustrations are not a corrected whole-assemblage type total.',
                   'The original count of nine b objects does not imply nine independent trials.',
                   'Association alone does not choose commodity, institution, owner or phonetics.']})
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
