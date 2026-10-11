"""A frozen, source-exposed five-object area contrast; no semantic test."""
import itertools
import json
from collections import Counter
from fractions import Fraction
from common import ROOT, sha256, write_json
from build_chanhu_deposit_joins import excavation_key

GROUPS = {'associated_complex': ['2285', '2428', '2529, CC'],
          'bath_vicinity': ['3215', '3207']}


def counts(rows, field):
    c = Counter(r[field] for r in rows)
    n = len(rows)
    return {'n': n, 'positive': c['positive'], 'negative': c['negative'], 'unknown': c['unknown'],
            'bounds': [str(Fraction(c['positive'], n)), str(Fraction(c['positive']+c['unknown'], n))] if n else None}


def contrast(rows, field):
    groups = {key: counts([r for r in rows if r['group'] == key], field) for key in GROUPS}
    a, b = [groups[key]['bounds'] for key in GROUPS]
    delta = [str(Fraction(a[0])-Fraction(b[1])), str(Fraction(a[1])-Fraction(b[0]))] if a and b else None
    return {'groups': groups, 'difference_bounds': delta,
            'available': delta is not None,
            'direction_identified_positive': bool(delta and Fraction(delta[0]) > 0),
            'direction_identified_negative': bool(delta and Fraction(delta[1]) < 0)}


def main():
    paths = ['results/chanhu_deposit_metadata_joins.json', 'results/chanhu_fish_audit.json',
             'docs/CHANHU_LOCAL_CONTRAST_ASSUMPTIONS.md', 'results/chanhu_deposit_support.json']
    joins, old = [json.loads((ROOT/p).read_text()) for p in paths[:2]]
    old_objects = {r['secondary_object_id']: r for r in old['secondary_objects']}
    rows = []
    for group, labels in GROUPS.items():
        for label in labels:
            candidates = [r for r in joins['rows'] if tuple(r['normalized_excavation_key']) == excavation_key(label)]
            assert len(candidates) == 1
            row = candidates[0]
            assert row['join_status'] == 'unique_number_and_plate_metadata_match'
            identity = row['selected_secondary_metadata']['secondary_object_id']
            prior = old_objects[identity]
            rows.append({'excavation_number': label, 'primary_row': row['primary']['row_id'],
                         'secondary_object_id': identity, 'group': group,
                         'fish': prior['fish'], 'plain_fish': prior['plain_fish'],
                         'signature_key': json.dumps(prior['raw_text_signature'])})
    output = {'scope': 'Conditional retrospective contrast of two described areas; not a matched deposit or craft-specific test.',
              'independent_area_blocks_per_category': 1,
              'assumptions_verified': False, 'strict_test_repaired': False,
              'fixed_five_object_contrasts': {f: contrast(rows, f) for f in ['fish', 'plain_fish']}}
    scenarios = []
    for mask in itertools.product([False, True], repeat=len(rows)):
        kept = [r for r, present in zip(rows, mask) if present]
        scenarios.append({'retained_primary_rows': [r['primary_row'] for r in kept],
                          'family': contrast(kept, 'fish'), 'plain': contrast(kept, 'plain_fish')})
    output['omission_sensitivity'] = {'scenarios': scenarios,
        'total': len(scenarios), 'available': sum(s['family']['available'] for s in scenarios),
        'unavailable': sum(not s['family']['available'] for s in scenarios),
        'interpretation': 'All subsets of five unsecured exact-deposit associations; not probabilities or newly inferred locations.'}
    signatures = Counter(r['signature_key'] for r in rows)
    output['selected_text_signature_group_sizes'] = sorted(signatures.values())
    output['objects'] = [{k: v for k, v in r.items() if k != 'signature_key'} for r in rows]
    output['new_semantic_values'] = output['new_phonetic_values'] = 0
    output['input_sha256'] = {p: sha256(ROOT/p) for p in paths}
    write_json('results/chanhu_local_contrast.json', output)
    print(json.dumps(output['fixed_five_object_contrasts'], indent=2))


if __name__ == '__main__':
    main()
