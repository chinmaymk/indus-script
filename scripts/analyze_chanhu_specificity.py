"""Background-frequency controls for a fixed local contrast, not a semantic test."""
import json
import re
from collections import Counter
from fractions import Fraction
from common import ROOT, sha256, write_json
from audit_chanhu_fish import fish_status


def count_status(statuses):
    c = Counter(statuses)
    return {k: c[k] for k in ('positive', 'negative', 'unknown')}


def interval(statuses):
    a, b = count_status(statuses[:3]), count_status(statuses[3:])
    low = Fraction(a['positive'], 3)-Fraction(b['positive']+b['unknown'], 2)
    high = Fraction(a['positive']+a['unknown'], 3)-Fraction(b['positive'], 2)
    return [str(low), str(high)]


def main():
    paths = ['results/chanhu_deposit_metadata_joins.json',
             'results/chanhu_fish_audit.json', 'results/chanhu_local_contrast.json',
             'data/processed/catalogue_features.json',
             'docs/CHANHU_LOCAL_SPECIFICITY_PROTOCOL.md']
    joins, fish, local, features = [json.loads((ROOT/p).read_text()) for p in paths[:4]]
    source = {r['secondary_object_id']: r['rows'] for r in fish['secondary_objects']}
    local_ids = [r['primary_row'] for r in local['objects']]
    assert local_ids == ['LI.15', 'LII.19', 'LII.23', 'LI.14', 'LI.22']
    frame = {}
    for row in joins['rows']:
        meta = row['selected_secondary_metadata']
        frame[row['primary']['row_id']] = source[meta['secondary_object_id']] if meta else None
    background = {k: v for k, v in frame.items() if k not in local_ids}
    assert len(frame) == 65 and len(background) == 60
    exclusions = {code for f in features if re.fullmatch(r'P\d{3}', f['id']) and 50 <= int(f['id'][1:]) <= 65 for code in f['wells_graphemes']}
    exclusions |= {'W000', 'W999', 'W221'}
    universe = set()
    for rows in background.values():
        for row in rows or []:
            for pre, code, post in re.findall(r'(?<!\d)([*?]?)(\d{3})([?]?)(?!\d)', row['text']):
                if not pre and not post:
                    universe.add('W'+code)
    controls = sorted(universe-exclusions)

    # Freeze frequency sets before calculating any control's local status vector.
    background_profiles = {}
    for code in ['W220'] + controls:
        statuses = {key: fish_status(rows, {code}) if rows else 'unknown' for key, rows in background.items()}
        background_profiles[code] = {'counts': count_status(statuses.values()), 'object_status': statuses}
    target_count = background_profiles['W220']['counts']
    sets = {
        'all_background_observed_controls': controls,
        'same_observed_positive_count': [c for c in controls if background_profiles[c]['counts']['positive'] == target_count['positive']],
        'same_positive_and_unknown_counts': [c for c in controls if background_profiles[c]['counts']['positive'] == target_count['positive'] and background_profiles[c]['counts']['unknown'] == target_count['unknown']],
        'half_to_twice_observed_positive_count': [c for c in controls if target_count['positive'] and target_count['positive'] <= 2*background_profiles[c]['counts']['positive'] <= 4*target_count['positive']],
    }
    result_rows = []
    for code in ['W220'] + controls:
        statuses = [fish_status(frame[k], {code}) if frame[k] else 'unknown' for k in local_ids]
        bounds = interval(statuses)
        result_rows.append({'code': code, 'background': background_profiles[code],
                            'local_status_vector': statuses, 'difference_bounds': bounds,
                            'interval_width': str(Fraction(bounds[1])-Fraction(bounds[0]))})
    target = result_rows[0]
    assert target['difference_bounds'] == local['fixed_five_object_contrasts']['plain_fish']['difference_bounds']
    lookup = {r['code']: r for r in result_rows}
    summaries = {}
    for label, codes in sets.items():
        selected = [lookup[c] for c in codes]
        summaries[label] = {
            'control_codes': codes, 'n_codes': len(codes),
            'distinct_local_profiles': len({tuple(r['local_status_vector']) for r in selected}),
            'equal_target_status_profile': [r['code'] for r in selected if r['local_status_vector'] == target['local_status_vector']],
            'equal_target_interval': [r['code'] for r in selected if r['difference_bounds'] == target['difference_bounds']],
            'at_least_target_lower_bound': [r['code'] for r in selected if Fraction(r['difference_bounds'][0]) >= Fraction(target['difference_bounds'][0])],
            'strictly_greater_lower_bound': [r['code'] for r in selected if Fraction(r['difference_bounds'][0]) > Fraction(target['difference_bounds'][0])],
        }
    profile_groups = {}
    for row in result_rows[1:]:
        profile_groups.setdefault('|'.join(row['local_status_vector']), []).append(row['code'])
    write_json('results/chanhu_local_specificity.json', {
        'scope': 'Retrospective local contrast; observed-frequency controls are not independent archaeological or semantic validation.',
        'primary_frame_size': 65, 'background_size': 60,
        'unjoined_background_objects': sum(v is None for v in background.values()),
        'local_primary_order': local_ids, 'excluded_codes': sorted(exclusions),
        'target': target, 'control_set_summaries': summaries,
        'all_code_results': result_rows, 'distinct_profile_groups': profile_groups,
        'zero_background_target_frequency': target_count['positive'] == 0,
        'p_value': None, 'semantic_values_assigned': 0, 'phonetic_values_assigned': 0,
        'input_sha256': {p: sha256(ROOT/p) for p in paths},
    })
    print(json.dumps({'target_background': target_count, 'summaries': summaries}, indent=2))


if __name__ == '__main__':
    main()
