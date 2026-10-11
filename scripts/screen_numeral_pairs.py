"""Exhaustive denominator for a narrow, exploratory two-marker numeral rule.

Keep exclusions, duplicate patterns, residual signs, and sensitivity failures.
No semantic or phonetic columns are imported. See docs/NUMERAL_SCREEN.md.
"""
from collections import Counter, defaultdict
import csv
import json
import re
from fractions import Fraction
from common import ROOT, sha256, write_json, write_csv
from prepare_corpora import parse_lipi

FIELDS = ('id', 'cisi', 'excavation-idno', 'type', 'dir.', 'complete', 'class', 'signs', 'text')
MARKERS = ('W700', 'W840')
LONG = {f'W{i:03}': i-30 for i in range(31, 40)}
SHORT = {f'W{i:03}': i for i in range(1, 8)}
STACKED = {f'W{i:03}': i-10 for i in range(12, 20)}
NUMERIC = set(LONG) | set(SHORT) | set(STACKED) | {'W900'}


def literal_tokens(text):
    """Find literal codes even in damaged text; never repair that text."""
    return ['W'+x for x in re.findall(r'(?<!\d)\d{3}(?!\d)', text)]


def adjacent_runs(sequence, marker):
    if sequence.count(marker) != 1:
        raise ValueError('Require one marker occurrence')
    i = sequence.index(marker)
    left, right = i, i+1
    while left and sequence[left-1] in NUMERIC:
        left -= 1
    while right < len(sequence) and sequence[right] in NUMERIC:
        right += 1
    return {'left': sequence[left:i], 'right': sequence[i+1:right],
            'residual_before': sequence[:left], 'residual_after': sequence[right:]}


def coefficients(tokens, stacked_as_units=False):
    result = dict(L=0, S=0, v=0, constant=0)
    for token in tokens:
        if token in LONG:
            result['L'] += LONG[token]
        elif token in SHORT:
            result['S'] += SHORT[token]
        elif token in STACKED:
            result['constant' if stacked_as_units else 'L'] += STACKED[token]
        elif token == 'W900':
            result['v'] += 1
        else:
            raise ValueError(f'Unrecognized candidate numeral: {token}')
    return result


def value(coef, candidate):
    return coef['constant'] + sum(coef[k]*candidate[k] for k in ('L', 'S', 'v'))


def inspect_group(group_id, rows, candidates, allow_lr=False):
    record = {'group_id': group_id, 'cisi': sorted({r['cisi'] for r in rows}),
              'rows': rows, 'eligible': False, 'exclusion_reasons': []}
    reasons = record['exclusion_reasons']
    if len(record['cisi']) != 1 or record['cisi'][0].strip() in ('', '-', '--', '?'):
        reasons.append('inconsistent_or_missing_artifact_identifier')
    occurrences = {m: [i for i, r in enumerate(rows) for t in literal_tokens(r['text']) if t == m]
                   for m in MARKERS}
    if any(len(occurrences[m]) != 1 for m in MARKERS):
        reasons.append('marker_occurrence_not_unique')
        return record
    if occurrences['W700'][0] == occurrences['W840'][0]:
        reasons.append('markers_on_same_face')
        return record
    faces = {}
    for marker in MARKERS:
        row = rows[occurrences[marker][0]]
        sequence, failures = parse_lipi(row)
        if allow_lr and row['dir.'].strip().upper() == 'L/R':
            failures = [f for f in failures if f != 'direction_not_R/L']
        if failures:
            reasons.extend(f'{marker}:{f}' for f in failures)
            continue
        runs = adjacent_runs(sequence, marker)
        numeric = runs['left'] + runs['right']
        faces[marker] = {'row_id': row['id'], **runs,
                         'coefficients': coefficients(numeric),
                         'stacked_unit_coefficients': coefficients(numeric, True)}
        if not numeric:
            reasons.append(f'{marker}:no_recognized_adjacent_numeric_run')
    record['faces'] = faces
    if reasons:
        return record
    record['eligible'] = True
    record['literal_pair_signature'] = [rows[occurrences[m][0]]['text'] for m in MARKERS]
    record['numeric_pair_signature'] = [[faces[m]['left'], faces[m]['right']] for m in MARKERS]
    record['equation_difference'] = {k: faces['W700']['coefficients'][k]-faces['W840']['coefficients'][k]
                                     for k in ('L', 'S', 'v', 'constant')}
    record['evaluations'] = []
    for candidate in candidates:
        for name, key in [('stacked_as_L', 'coefficients'), ('stacked_as_one', 'stacked_unit_coefficients')]:
            totals = {m: value(faces[m][key], candidate) for m in MARKERS}
            record['evaluations'].append({'candidate': candidate, 'model': name,
                'values': totals, 'residual': totals['W700']-totals['W840'],
                'balances': totals['W700'] == totals['W840']})
    return record


def aggregate(records):
    eligible = [r for r in records if r['eligible']]
    return {'candidate_groups': len(records), 'eligible_groups': len(eligible),
            'excluded_groups': len(records)-len(eligible),
            'distinct_literal_pairs': len({json.dumps(r['literal_pair_signature']) for r in eligible}),
            'distinct_numeric_pairs': len({json.dumps(r['numeric_pair_signature']) for r in eligible}),
            'exclusion_reasons_overlap': dict(Counter(reason for r in records for reason in r['exclusion_reasons'])),
            'evaluations': [dict(candidate=e['candidate'], model=e['model'],
                  balanced=sum(r['evaluations'][i]['balances'] for r in eligible), total=len(eligible))
                  for i,e in enumerate(eligible[0]['evaluations'])] if eligible else []}


def constant_long_stroke_ratio_audit(records):
    """Allow different positive stroke values in the two marker contexts.

    Each pure-long pair requires n700*a=n840*b, hence b/a=n700/n840.
    Different required ratios cannot hold with a,b positive and constant.
    """
    constraints = []
    for record in records:
        if not record['eligible']:
            continue
        runs = {m: record['faces'][m]['left'] + record['faces'][m]['right'] for m in MARKERS}
        if not all(runs[m] and all(t in LONG for t in runs[m]) for m in MARKERS):
            continue
        counts = {m: sum(LONG[t] for t in runs[m]) for m in MARKERS}
        ratio = Fraction(counts['W700'], counts['W840'])
        constraints.append({'cisi': record['cisi'], 'group_id': record['group_id'],
            'stroke_counts': counts, 'required_b_over_a': str(ratio)})
    ratios = sorted({c['required_b_over_a'] for c in constraints}, key=Fraction)
    return {'a': 'Constant positive value per long stroke in W700 context',
            'b': 'Constant positive value per long stroke in W840 context',
            'constraints': constraints, 'distinct_required_b_over_a': ratios,
            'incompatible_with_any_positive_constant_pair': len(ratios) > 1,
            'scope': 'Conditional on equal quantities across faces; source transcriptions retained'}


def main():
    protocol_path = ROOT/'data/processed/numeral_screen_protocol.json'
    protocol = json.loads(protocol_path.read_text())
    candidates = protocol['fixed_candidates']
    source = ROOT/'data/raw/lipi_inscriptions.csv'
    groups = defaultdict(list)
    with source.open() as f:
        for row in csv.DictReader(f):
            groups[row['id'].split('.')[0]].append({k: row[k] for k in FIELDS})
    selected = {g: rows for g,rows in groups.items()
                if set(MARKERS) <= {t for r in rows for t in literal_tokens(r['text'])}}
    results = {}
    for name, allow_lr in [('strict', False), ('allow_LR_sensitivity', True)]:
        records = [inspect_group(g, selected[g], candidates, allow_lr) for g in sorted(selected, key=int)]
        results[name] = {'summary': aggregate(records), 'records': records,
                         'constant_long_stroke_unit_ratio': constant_long_stroke_ratio_audit(records)}
    write_csv('results/numeral_pair_source_rows.csv', [r for rows in selected.values() for r in rows], FIELDS)
    write_json('results/numeral_pair_screen.json', {
        'source_sha256': sha256(source), 'protocol_sha256': sha256(protocol_path),
        'all_local_groups': len(groups), 'all_source_rows': sum(map(len,groups.values())),
        'candidate_source_rows': sum(map(len,selected.values())),
        'status': protocol['status'], 'screens': results,
        'new_established_sign_values': 0,
        'proposed_crosswalk': {'local_id': '1786', 'cisi': 'H-904', 'article_id': '3786',
            'status': 'Matching numerical pattern only; artifact image and article figure not authenticated'}})
    for name, result in results.items():
        print(name, json.dumps(result['summary'], sort_keys=True))


if __name__ == '__main__':
    main()
