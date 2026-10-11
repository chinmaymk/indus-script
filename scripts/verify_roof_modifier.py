"""Independent finite verification of roof frames and exact conditional score support.

Uses standard library only; never imports audit_roof_modifier or its helpers.
Exact null calculation marginalizes unused frame slots by multinomial weights.
This verifies computation and fingerprints, not ancient identities or sign shapes.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text())

def pin(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def pack(key):
    return dict(zip(('site_label_unverified', 'object_code', 'length', 'position', 'prefix', 'suffix'),
                    (*key[:4], list(key[4]), list(key[5]))))

def multinomial(counts):
    answer = math.factorial(sum(counts))
    divisor = math.prod(math.factorial(n) for n in counts)
    return answer // divisor

def reconstruct(records, pairs, strict, stratified):
    # Each pair is scanned independently; no producer sign-owner lookup is used.
    kept = []
    excluded = Counter()
    for row in records:
        tokens = row['tokens']
        actual_strict = (row['source_doc_count'] == 1 and row['source_direction_code'] == '1'
                         and len(tokens) >= 2 and not any(t['doubtful'] or t['unknown_span'] for t in tokens))
        require(actual_strict == row['strict_candidate'], 'strict flag inconsistent with source fields')
        if any(t['doubtful'] or t['unknown_span'] for t in tokens):
            excluded['any_doubt_or_loss'] += 1
        elif strict and not actual_strict:
            excluded['not_strict_candidate'] += 1
        elif not tokens:
            excluded['empty'] += 1
        else:
            kept.append(row)
            if len(tokens) == 1:
                excluded['no_outside_context_in_retained_record'] += 1
    frequencies = Counter(t['sign'] for row in kept for t in row['tokens'])
    eligible_tokens = Counter()
    tables = []
    serialized = []
    for pair in pairs:
        table = defaultdict(lambda: [set(), set()])
        for row in kept:
            sequence = tuple(t['sign'] for t in row['tokens'])
            if len(sequence) < 2:
                continue
            for position, sign in enumerate(sequence):
                if sign not in (pair['base'], pair['roof']):
                    continue
                state = 0 if sign == pair['base'] else 1
                metadata = ((row['site_label_unverified'] or '<unknown>', row['source_object_code'] or '<unknown>')
                            if stratified else ('*', '*'))
                key = (*metadata, len(sequence), position, sequence[:position], sequence[position+1:])
                table[key][state].add(row['source_reference'])
                eligible_tokens[sign] += 1
        tables.append(table)
        serialized.append([dict(pack(key), state_mask=(1 if refs[0] else 0) + (2 if refs[1] else 0),
                                base_references=sorted(refs[0]), roof_references=sorted(refs[1]))
                           for key, refs in sorted(table.items())])
    comparisons = []
    totals = Counter()
    all_rectangles = []
    edges = []
    masks = [{key: (1 if refs[0] else 0) + (2 if refs[1] else 0) for key, refs in table.items()}
             for table in tables]
    signed = {1: -1, 2: 1, 3: 0}
    for first, second in combinations(range(len(pairs)), 2):
        if pairs[first]['root'] == pairs[second]['root']:
            continue
        shared = []
        categories = Counter()
        plain, roof = [], []
        for key in sorted(set(tables[first]).intersection(tables[second])):
            x, y = masks[first][key], masks[second][key]
            category = ('ambiguous' if x == 3 or y == 3 else
                        'plain_concordant' if x == y == 1 else
                        'roof_concordant' if x == y == 2 else 'discordant')
            categories[category] += 1
            shared.append(dict(pack(key), states=[x, y], category=category))
            edges.append(((first, key), (second, key)))
            if category == 'plain_concordant': plain.append(key)
            if category == 'roof_concordant': roof.append(key)
        rectangles = []
        for plain_key in plain:
            for roof_key in roof:
                if plain_key[:4] != roof_key[:4]:
                    continue
                options = [sorted(tables[first][plain_key][0]), sorted(tables[second][plain_key][0]),
                           sorted(tables[first][roof_key][1]), sorted(tables[second][roof_key][1])]
                # Direct Cartesian enumeration instead of producer recursive matching.
                witness = next((list(choice) for choice in product(*options) if len(set(choice)) == 4), None)
                rectangles.append({'pair_indices': [first, second], 'plain_frame': pack(plain_key),
                                   'roof_frame': pack(roof_key), 'all_reference_options': options,
                                   'four_distinct_reference_witness': witness,
                                   'physical_object_and_die_independence_verified': False})
        comparisons.append({'pair_indices': [first, second], 'states': dict(categories),
                            'shared_frames': shared, 'candidate_rectangles': rectangles})
        totals.update(categories)
        all_rectangles.extend(rectangles)
    score = sum(signed[masks[a][key]] * signed[masks[b][key]] for (a, key), (b, _) in edges)
    summary = {'pair_count': len(pairs), 'cross_root_pair_comparisons': len(comparisons),
               'shared_frame_incidences': len(edges), 'states': dict(totals), 'signed_score': score,
               'candidate_rectangles': len(all_rectangles),
               'rectangles_with_four_distinct_references': sum(r['four_distinct_reference_witness'] is not None for r in all_rectangles)}
    coverage = {'included_records': len(kept), 'excluded': dict(excluded), 'token_counts': dict(frequencies),
                'tokens_with_outside_context': dict(eligible_tokens)}
    return {'coverage': coverage, 'pair_frames': serialized, 'comparisons': comparisons, 'summary': summary}, masks, edges

def exact_null(masks, edges):
    """Enumerate only edge-incident slots; weight all other slots analytically."""
    nodes = {node for edge in edges for node in edge}
    buckets = defaultdict(dict)
    for i, table in enumerate(masks):
        for frame, mask in table.items():
            buckets[(i, frame[:4])][(i, frame)] = mask
    all_allocations = 1
    irrelevant_factor = 1
    movable = 0
    active_movable = 0
    active_buckets = []
    bucket_details = []
    for bucket, slots in sorted(buckets.items()):
        counts = Counter(slots.values())
        total = multinomial(list(counts.values()))
        all_allocations *= total
        movable += len(slots) if len(counts) > 1 else 0
        active = sorted(set(slots).intersection(nodes))
        active_movable += len(active) if len(counts) > 1 else 0
        if not active:
            irrelevant_factor *= total
            continue
        options = []
        for assignment in product(sorted(counts), repeat=len(active)):
            used = Counter(assignment)
            if any(used[state] > count for state, count in counts.items()):
                continue
            remaining = [count - used[state] for state, count in counts.items()]
            options.append((dict(zip(active, assignment)), multinomial(remaining)))
        active_buckets.append(options)
        bucket_details.append({'pair_index': bucket[0], 'stratum': list(bucket[1]), 'frame_slots': len(slots),
                               'mask_counts': dict(counts), 'shared_edge_slots': len(active),
                               'feasible_projected_assignments': len(options), 'full_stratum_allocations': str(total)})
    projected_count = math.prod(len(options) for options in active_buckets)
    require(projected_count <= 1000000, 'Exact projection unexpectedly large; do not silently approximate')
    distribution = Counter()
    signs = {1: -1, 2: 1, 3: 0}
    for choices in product(*active_buckets):
        assignment = {}
        weight = irrelevant_factor
        for selected, completions in choices:
            assignment.update(selected)
            weight *= completions
        score = sum(signs[assignment[a]] * signs[assignment[b]] for a, b in edges)
        distribution[score] += weight
    require(sum(distribution.values()) == all_allocations, 'Exact null weights do not sum to global allocations')
    return {'method': 'Exhaustive edge-slot assignments with capacity checks; unused slots marginalized by exact multinomial counts',
            'distinct_global_allocations': str(all_allocations), 'movable_frame_slots': movable,
            'movable_shared_edge_slots': active_movable, 'shared_edge_nodes': len(nodes),
            'projected_assignments_enumerated': projected_count, 'active_strata': bucket_details,
            'attainable_scores': sorted(distribution), 'minimum_score': min(distribution), 'maximum_score': max(distribution),
            'exact_score_allocation_counts': {str(k): str(v) for k, v in sorted(distribution.items())},
            'proved_score_invariant': len(distribution) == 1}

def check_exact_null_oracle():
    """Tiny exhaustive permutation oracle checks dependence and unused-slot weights."""
    keys = [('<unknown>', '1', 3, 1, ('M001',), (f'M{n:03d}',)) for n in (2, 3, 4)]
    masks = [dict(zip(keys, (1, 2, 3))), dict(zip(keys, (1, 1, 2)))]
    signs = {1: -1, 2: 1, 3: 0}
    for edge_count in (0, 1, 2, 3):
        edges = [((0, key), (1, key)) for key in keys[:edge_count]]
        brute = Counter()
        for left, right in product(set(permutations((1, 2, 3))), set(permutations((1, 1, 2)))):
            brute[sum(signs[left[i]] * signs[right[i]] for i in range(edge_count))] += 1
        projected = exact_null(masks, edges)
        require(projected['exact_score_allocation_counts'] == {str(k): str(v) for k, v in sorted(brute.items())},
                'synthetic exact-null permutation oracle differs')
    return {'tiny_exhaustive_permutation_oracle_cases': 4, 'checks': 'Capacity coupling, mixed masks, repeated masks, unused slots and empty graph'}

def main():
    oracle = check_exact_null_oracle()
    paths = ['scripts/verify_roof_modifier.py', 'scripts/audit_roof_modifier.py',
             'results/roof_modifier_audit.json', 'data/processed/roof_modifier_protocol.json',
             'data/processed/roof_modifier_shape_review.json', 'data/processed/m77_candidate_records.jsonl',
             'results/m77_candidate_audit.json']
    observed = read(paths[2]); protocol = read(paths[3]); shape = read(paths[4])
    require(observed['protocol'] == protocol and observed['shape_review'] == shape, 'embedded protocol/shape differ')
    evidence = {}
    for path, digest in observed['input_sha256'].items():
        entry = pin(path); require(entry['sha256'] == digest, f'input hash {path}'); evidence[path] = entry
    for entry in shape['evidence_files']:
        actual = pin(entry['path']); require(actual == entry, f'shape pin {entry["path"]}'); evidence[entry['path']] = actual
    source_audit = read(paths[6])
    for path, digest in source_audit['source_sha256'].items():
        entry = pin(path); require(entry['sha256'] == digest, f'candidate upstream pin {path}'); evidence[path] = entry
    pairs = protocol['pairs']
    require({(p['base'], p['roof']) for p in pairs} == {(p['base'], p['modified']) for p in shape['core_pairs']}, 'visual selection differs')
    endpoints = [p[k] for p in pairs for k in ('base', 'roof')]
    require(len(set(endpoints)) == len(endpoints), 'overlapping endpoints')
    records = [json.loads(line) for line in (ROOT / paths[5]).read_text().splitlines()]
    output = {}
    rebuilt = {}
    configurations = [('strict_stratified_primary', True, True), ('strict_unstratified_diagnostic', True, False),
                      ('complete_stratified_sensitivity', False, True), ('complete_unstratified_diagnostic', False, False)]
    require(set(observed['results']) == {x[0] for x in configurations}, 'unexpected analyses')
    for name, strict, stratified in configurations:
        calculated, masks, edges = reconstruct(records, pairs, strict, stratified)
        actual = observed['results'][name]
        for field, value in calculated.items():
            require(value == actual[field], f'{name}: {field} differs')
        require(actual['strict_candidate_filter'] == strict and actual['metadata_stratified'] == stratified, 'selection labels differ')
        null = exact_null(masks, edges)
        sampled = actual['conditional_null']
        require(str(null['distinct_global_allocations']) == sampled['distinct_mask_allocations'], 'allocation count differs')
        require(null['movable_frame_slots'] == sampled['movable_frame_slots'], 'movable slot count differs')
        scores = sampled['scores']
        require(len(scores) == sampled['replicates'] == 499 and sampled['seed'] == 20260927, 'simulation metadata differs')
        require(set(scores) <= set(null['attainable_scores']), 'sample contains impossible score')
        mean = sum(scores) / len(scores)
        variance = sum((value - mean)**2 for value in scores) / len(scores)
        require(variance == sampled['score_variance'], 'reported sample variance differs')
        expected_p = (1 + sum(x >= calculated['summary']['signed_score'] for x in scores))/500 if variance > 0 else None
        require(sampled['upper_tail_p_plus_one'] == expected_p, 'conditional empirical p differs')
        output[name] = {'all_frames_masks_reference_sets_comparisons_and_summaries_match': True,
                        'summary': calculated['summary'], 'exact_conditional_null': null,
                        'shared_frame_witnesses': [r for r in calculated['comparisons'] if r['shared_frames']]}
        rebuilt[name] = calculated
    membership = {p[k]: {'pair_index': i, 'role': k, 'root': p['root']} for i, p in enumerate(pairs) for k in ('base', 'roof')}
    require(len(observed['signs']) == 417, 'all-sign table size')
    for number, row in enumerate(observed['signs'], 1):
        sign = f'M{number:03d}'
        require(row['sign'] == sign and row['selected_visual_pair'] == membership.get(sign), f'membership {sign}')
        for label, key in [('strict_stratified_primary', 'strict_tokens'), ('complete_stratified_sensitivity', 'complete_undoubted_tokens')]:
            require(row[key] == rebuilt[label]['coverage']['token_counts'].get(sign, 0), f'coverage {sign}')
        require(row['semantic_value'] is None and row['phonetic_value'] is None, 'non-null value')
    require(observed['established_semantic_values'] == observed['established_phonetic_values'] == 0, 'established values')
    for path in paths:
        evidence[path] = pin(path)
    result = {'status': 'all checks passed', 'scope': 'Independent computational verification; no new primary authentication or archaeological independence claim',
              'production_helpers_imported': False, 'exact_null_self_checks': oracle,
              'results': output, 'evidence_files': list(evidence.values()),
              'verified_all_417_coverage_rows': True, 'established_semantic_values': 0, 'established_phonetic_values': 0,
              'limits': 'Exact null support belongs only to the specified conditional mask allocation scheme. Unknown-site matches are not verified shared sites. Distinct references are not independently authenticated objects/dies. Seeded random draws are checked for attainable support and reported arithmetic, not independently regenerated.'}
    target = ROOT / 'results/roof_modifier_independent.json'
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({name: {'summary': item['summary'], 'exact_score_range': [item['exact_conditional_null']['minimum_score'], item['exact_conditional_null']['maximum_score']], 'projected_assignments': item['exact_conditional_null']['projected_assignments_enumerated']} for name, item in output.items()}, indent=2))

if __name__ == '__main__':
    main()
