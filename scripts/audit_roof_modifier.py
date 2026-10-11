"""Cross-root full-frame roof contrasts, with explicit missing/mixed states.

The finite candidates are visual operations, never semantic equations. Distinct
catalogue references are a necessary screening condition, not independent dies.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import json
import math
import random
from common import ROOT, read_jsonl, sha256, write_json


def distinct_witnesses(groups):
    """Return one injective reference assignment, or None (not a count product)."""
    def visit(i, chosen):
        if i == len(groups):
            return chosen
        for ref in sorted(set(groups[i]) - set(chosen)):
            found = visit(i + 1, chosen + [ref])
            if found is not None:
                return found
        return None
    return visit(0, [])


def frames(records, pairs, strict, stratified):
    owner = {p[k]: (i, state) for i, p in enumerate(pairs)
             for k, state in [('base', 1), ('roof', 2)]}
    assert len(owner) == 2 * len(pairs), 'Pair endpoints must not overlap'
    indexed = [defaultdict(lambda: {1: set(), 2: set()}) for _ in pairs]
    excluded = Counter(); counts = Counter(); selected = Counter(); included = 0
    for r in records:
        if any(t['doubtful'] or t['unknown_span'] for t in r['tokens']):
            excluded['any_doubt_or_loss'] += 1; continue
        if strict and not r['strict_candidate']:
            excluded['not_strict_candidate'] += 1; continue
        seq = tuple(t['sign'] for t in r['tokens'])
        if not seq:
            excluded['empty'] += 1; continue
        included += 1; counts.update(seq)
        if len(seq) == 1:
            excluded['no_outside_context_in_retained_record'] += 1; continue
        site = (r['site_label_unverified'] or '<unknown>') if stratified else '*'
        obj = (r['source_object_code'] or '<unknown>') if stratified else '*'
        for pos, sign in enumerate(seq):
            if sign not in owner:
                continue
            i, state = owner[sign]
            frame = (site, obj, len(seq), pos, seq[:pos], seq[pos+1:])
            indexed[i][frame][state].add(r['source_reference'])
            selected[sign] += 1
    return indexed, {'included_records': included, 'excluded': dict(excluded),
                     'token_counts': counts, 'tokens_with_outside_context': selected}


def state_mask(refs):
    return int(bool(refs[1])) + 2 * int(bool(refs[2]))


def frame_json(key):
    return {'site_label_unverified': key[0], 'object_code': key[1],
            'length': key[2], 'position': key[3],
            'prefix': list(key[4]), 'suffix': list(key[5])}


def comparable(pairs):
    return [(a, b) for a, b in combinations(range(len(pairs)), 2)
            if pairs[a]['root'] != pairs[b]['root']]


def signed_score(masks, comparisons):
    code = {1: -1, 2: 1, 3: 0}
    return sum(code[masks[a][f]] * code[masks[b][f]]
               for a, b in comparisons for f in masks[a].keys() & masks[b].keys())


def shuffle_masks(masks, rng):
    out = []
    for by_frame in masks:
        strata = defaultdict(list)
        for f in sorted(by_frame):
            strata[f[:4]].append(f)
        shuffled = {}
        for fs in strata.values():
            values = [by_frame[f] for f in fs]; rng.shuffle(values)
            shuffled.update(zip(fs, values))
        out.append(shuffled)
    return out


def analyze(records, pairs, strict, stratified):
    indexed, coverage = frames(records, pairs, strict, stratified)
    masks = [{f: state_mask(refs) for f, refs in by_frame.items()} for by_frame in indexed]
    comparisons = comparable(pairs)
    details = []; all_rectangles = []
    total = Counter()
    for a, b in comparisons:
        states = Counter(); shared = []; plain = []; roof = []
        for f in sorted(masks[a].keys() & masks[b].keys()):
            x, y = masks[a][f], masks[b][f]
            label = ('ambiguous' if 3 in (x, y) else 'plain_concordant' if x == y == 1
                     else 'roof_concordant' if x == y == 2 else 'discordant')
            states[label] += 1
            shared.append(dict(frame_json(f), states=[x, y], category=label))
            if label == 'plain_concordant': plain.append(f)
            if label == 'roof_concordant': roof.append(f)
        rectangles = []
        for f0, f1 in product(plain, roof):
            if f0[:4] != f1[:4]:
                continue
            groups = [indexed[a][f0][1], indexed[b][f0][1], indexed[a][f1][2], indexed[b][f1][2]]
            witness = distinct_witnesses(groups)
            row = {'pair_indices': [a, b], 'plain_frame': frame_json(f0),
                   'roof_frame': frame_json(f1), 'all_reference_options': [sorted(x) for x in groups],
                   'four_distinct_reference_witness': witness,
                   'physical_object_and_die_independence_verified': False}
            rectangles.append(row)
        total.update(states); all_rectangles.extend(rectangles)
        details.append({'pair_indices': [a, b], 'states': dict(states),
                        'shared_frames': shared, 'candidate_rectangles': rectangles})
    all_frames = [[dict(frame_json(f), state_mask=masks[i][f],
                       base_references=sorted(refs[1]), roof_references=sorted(refs[2]))
                   for f, refs in sorted(by_frame.items())] for i, by_frame in enumerate(indexed)]
    score = signed_score(masks, comparisons)
    movable = 0; allocations = 1
    for by_frame in masks:
        strata = defaultdict(list)
        for f, mask in by_frame.items(): strata[f[:4]].append(mask)
        movable += sum(len(ms) for ms in strata.values() if len(set(ms)) > 1)
        for ms in strata.values():
            possibilities = math.factorial(len(ms))
            for n in Counter(ms).values(): possibilities //= math.factorial(n)
            allocations *= possibilities
    rng = random.Random(20260927)
    null = [signed_score(shuffle_masks(masks, rng), comparisons) for _ in range(499)]
    variance = sum((x - sum(null)/len(null))**2 for x in null)/len(null)
    return {'coverage': coverage, 'pair_frames': all_frames, 'comparisons': details,
            'summary': {'pair_count': len(pairs), 'cross_root_pair_comparisons': len(comparisons),
                        'shared_frame_incidences': sum(total.values()), 'states': dict(total),
                        'signed_score': score, 'candidate_rectangles': len(all_rectangles),
                        'rectangles_with_four_distinct_references': sum(x['four_distinct_reference_witness'] is not None for x in all_rectangles)},
            'conditional_null': {'seed': 20260927, 'replicates': 499, 'movable_frame_slots': movable,
                                 'distinct_mask_allocations': str(allocations),
                                 'preserved': 'Only per-pair/stratum frame-mask counts and coverage graph; not token/reference multiplicities, physical-object or formula dependencies',
                                 'score_variance': variance, 'scores': null,
                                 'upper_tail_p_plus_one': (1 + sum(x >= score for x in null))/500 if variance > 0 else None,
                                 'status': 'nondegenerate specified conditional shuffle' if variance > 0 else 'degenerate; no informative p-value'},
            'strict_candidate_filter': strict, 'metadata_stratified': stratified}


def main():
    paths = ['data/processed/roof_modifier_protocol.json', 'data/processed/roof_modifier_shape_review.json',
             'data/processed/m77_candidate_records.jsonl']
    protocol = json.loads((ROOT / paths[0]).read_text())
    shape = json.loads((ROOT / paths[1]).read_text())
    for pin in shape['evidence_files']:
        assert sha256(ROOT / pin['path']) == pin['sha256'], pin['path']
        assert (ROOT / pin['path']).stat().st_size == pin['bytes'], pin['path']
    records = read_jsonl(paths[2]); pairs = protocol['pairs']
    assert {(p['base'], p['roof']) for p in pairs} == {(p['base'], p['modified']) for p in shape['core_pairs']}
    results = {label: analyze(records, pairs, strict, stratified) for label, strict, stratified in [
        ('strict_stratified_primary', True, True), ('strict_unstratified_diagnostic', True, False),
        ('complete_stratified_sensitivity', False, True), ('complete_unstratified_diagnostic', False, False)]}
    membership = {p[k]: {'pair_index': i, 'role': k, 'root': p['root']}
                  for i, p in enumerate(pairs) for k in ('base', 'roof')}
    signs = []
    for number in range(1, 418):
        sign = f'M{number:03d}'
        signs.append({'sign': sign, 'selected_visual_pair': membership.get(sign),
                      'complete_undoubted_tokens': results['complete_stratified_sensitivity']['coverage']['token_counts'].get(sign, 0),
                      'strict_tokens': results['strict_stratified_primary']['coverage']['token_counts'].get(sign, 0),
                      'scope': 'Unselected signs are not tested for this graphic operation',
                      'semantic_value': None, 'phonetic_value': None})
    write_json('results/roof_modifier_audit.json', {'protocol': protocol, 'results': results, 'signs': signs,
               'shape_review': shape, 'input_sha256': {p: sha256(ROOT / p) for p in paths},
               'established_semantic_values': 0, 'established_phonetic_values': 0,
               'limits': 'Exclusive-state absence in this selected export is not ancient absence. A rectangle is a screening candidate, not equivalence or a semantic operator. Source-labelled sites and references are not an archaeological holdout.'})
    for label, result in results.items():
        print(label, json.dumps(result['summary']))


if __name__ == '__main__':
    main()
