"""Exact support gates for cross-root roof prediction; no classifier or readings."""
from collections import defaultdict, Counter
from itertools import combinations
import json
from common import ROOT, read_jsonl, sha256, write_json


def metadata_label(value):
    label = str(value).strip() if value is not None else ''
    return '<unknown>' if label.lower() in ('', '<unknown>', 'unknown', 'null', 'none', '?') else label


def two_disjoint_edges(edges):
    """Exact threshold witness, including graphs with mixed-state vertices."""
    unique = sorted({tuple(sorted(e)) for e in edges if len(set(e)) == 2})
    for first, second in combinations(unique, 2):
        if set(first).isdisjoint(second):
            return [list(first), list(second)]
    return None


def grouped_occurrences(records, pairs, strict):
    owner = {p[k]: (i, p['root'], state) for i, p in enumerate(pairs)
             for k, state in [('base', 0), ('roof', 1)]}
    assert len(owner) == 2 * len(pairs)
    eligible = []
    excluded = Counter()
    for record in records:
        if any(t['doubtful'] or t['unknown_span'] for t in record['tokens']):
            excluded['doubt_or_loss'] += 1; continue
        if strict and not record['strict_candidate']:
            excluded['not_strict'] += 1; continue
        if len(record['tokens']) < 2:
            excluded['no_outside_context'] += 1; continue
        eligible.append(record)
    parent = list(range(len(eligible)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    def join(a, b):
        a, b = find(a), find(b)
        if a != b: parent[max(a, b)] = min(a, b)
    references, formulas = {}, {}
    sequences, collapsed = [], []
    for i, record in enumerate(eligible):
        seq = tuple(t['sign'] for t in record['tokens'])
        formula = tuple('TARGET' if t in owner else t for t in seq)
        sequences.append(seq); collapsed.append(formula)
        for mapping, key in ((references, record['source_reference']), (formulas, formula)):
            if key in mapping: join(i, mapping[key])
            else: mapping[key] = i
    members = defaultdict(list)
    for i in range(len(eligible)): members[find(i)].append(i)
    ordered = sorted(members.values(), key=lambda ids: sorted(eligible[i]['id'] for i in ids))
    component_ids = {i: f'C{j:05d}' for j, ids in enumerate(ordered) for i in ids}
    occurrences = []
    for i, record in enumerate(eligible):
        seq = sequences[i]
        for pos, sign in enumerate(seq):
            if sign not in owner: continue
            pair, root, state = owner[sign]
            occurrences.append({'id': f"{record['id']}:{pos}",
                'record_id': record['id'], 'reference': record['source_reference'],
                'component': component_ids[i], 'sign': sign, 'pair_index': pair,
                'root': root, 'state': state, 'sequence': list(seq),
                'site_label_unverified': metadata_label(record['site_label_unverified']),
                'object_code': metadata_label(record['source_object_code']),
                'length': len(seq), 'position': pos})
    components = [{'id': component_ids[ids[0]],
                   'record_ids': sorted(eligible[i]['id'] for i in ids),
                   'references': sorted({eligible[i]['source_reference'] for i in ids}),
                   'collapsed_formulas': [list(s) for s in sorted({collapsed[i] for i in ids})]}
                  for ids in ordered]
    return occurrences, components, {'eligible_records': len(eligible), 'excluded': dict(excluded)}


def root_support(occurrences, root, known_labels, banned=frozenset()):
    strata = defaultdict(lambda: {0: defaultdict(list), 1: defaultdict(list)})
    selected = []
    for o in occurrences:
        if o['root'] != root or o['component'] in banned: continue
        if known_labels and '<unknown>' in (o['site_label_unverified'], o['object_code']): continue
        selected.append(o)
        key = (o['pair_index'], o['site_label_unverified'], o['object_code'], o['length'], o['position'])
        strata[key][o['state']][o['component']].append(o['id'])
    edges = {}
    shared_strata = []
    for key, states in sorted(strata.items()):
        if not states[0] or not states[1]: continue
        shared_strata.append({'stratum': list(key),
            'plain_components': sorted(states[0]), 'roof_components': sorted(states[1]),
            'mixed_components': sorted(states[0].keys() & states[1].keys())})
        for a in sorted(states[0]):
            for b in sorted(states[1]):
                if a == b: continue
                edge = tuple(sorted((a, b)))
                edges.setdefault(edge, {'components': list(edge), 'stratum': list(key),
                    'plain_occurrence': min(states[0][a]), 'roof_occurrence': min(states[1][b])})
    witness = two_disjoint_edges(edges)
    by_state = {s: {o['component'] for o in selected if o['state'] == s} for s in (0, 1)}
    return {'root': root, 'occurrences': len(selected),
        'plain_occurrences': sum(o['state'] == 0 for o in selected),
        'roof_occurrences': sum(o['state'] == 1 for o in selected),
        'plain_components': len(by_state[0]), 'roof_components': len(by_state[1]),
        'mixed_components': len(by_state[0] & by_state[1]),
        'strata_with_both_states': shared_strata,
        'distinct_component_edges': [edges[e] for e in sorted(edges)],
        'two_disjoint_edges_witness': [edges[tuple(e)] for e in witness] if witness else None,
        'threshold_pass': witness is not None,
        'scope': 'Exact existence of two component-disjoint matched pairs, not maximum matching or verified independent objects'}


def analyze(records, pairs, strict, known_labels):
    occurrences, components, coverage = grouped_occurrences(records, pairs, strict)
    roots = sorted({p['root'] for p in pairs})
    marginal = {r: root_support(occurrences, r, known_labels) for r in roots}
    folds = []
    for held in roots:
        banned = {o['component'] for o in occurrences if o['root'] == held}
        train = {r: root_support(occurrences, r, known_labels, banned) for r in roots if r != held}
        trained_roots = [r for r, result in train.items() if result['threshold_pass']]
        folds.append({'held_out_root': held, 'purged_components': sorted(banned),
            'other_root_occurrences_purged': sum(o['component'] in banned and o['root'] != held for o in occurrences),
            'held_out_support': marginal[held], 'remaining_training_roots': train,
            'training_roots_passing': trained_roots,
            'proxy_support_gate_pass': marginal[held]['threshold_pass'] and len(trained_roots) >= 2})
    return {'strict_filter': strict, 'known_secondary_labels_only': known_labels,
        'coverage': coverage, 'components': components, 'occurrences': occurrences,
        'marginal_root_support': marginal, 'folds': folds,
        'summary': {'selected_occurrences': len(occurrences), 'total_components': len(components),
            'target_bearing_components': len({o['component'] for o in occurrences}),
            'marginal_roots_passing': [r for r in roots if marginal[r]['threshold_pass']],
            'held_out_roots_passing_proxy_gate': [f['held_out_root'] for f in folds if f['proxy_support_gate_pass']],
            'complete_artifact_die_keys_available': False,
            'prediction_test_status': 'not run; this is a support audit, with archaeological independence unauthenticated'}}


def main():
    paths = ['data/processed/roof_transfer_support_protocol.json',
             'data/processed/m77_candidate_records.jsonl',
             'docs/ROOF_TRANSFER_SUPPORT_DESIGN.md', 'scripts/audit_roof_transfer_support.py']
    protocol = json.loads((ROOT / paths[0]).read_text())
    records = read_jsonl(paths[1]); pairs = protocol['pairs']
    results = {f'{corpus}_{metadata}': analyze(records, pairs, strict, known)
               for corpus, strict in [('strict', True), ('complete', False)]
               for metadata, known in [('known_labels', True), ('unknown_allowed', False)]}
    owner = {p[k]: p['root'] for p in pairs for k in ('base', 'roof')}
    signs = [{'sign': f'M{i:03d}', 'selected_root': owner.get(f'M{i:03d}'),
              'semantic_value': None, 'phonetic_value': None} for i in range(1, 418)]
    write_json('results/roof_transfer_support.json', {'protocol': protocol, 'results': results,
        'signs': signs, 'established_semantic_values': 0, 'established_phonetic_values': 0,
        'input_sha256': {p: sha256(ROOT / p) for p in paths}})
    for branch, result in results.items(): print(branch, json.dumps(result['summary']))


if __name__ == '__main__':
    main()
