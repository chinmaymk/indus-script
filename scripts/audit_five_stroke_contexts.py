"""Describe context overlap without equating visually five-stroke catalogue signs."""
from collections import Counter, defaultdict
from itertools import combinations
import csv
import json
from common import ROOT, sha256, write_json
from analyze_m77_foreign import eligible, sequence
from audit_chain_segments import domestic
from audit_stroke_substitution import frame_index

SIGNS = ('M096', 'M106', 'M107')


def position_counts(sequences, sign):
    counts = Counter()
    for seq in sequences:
        for i, token in enumerate(seq):
            if token == sign:
                counts['solus' if len(seq) == 1 else 'initial' if i == 0
                       else 'final' if i == len(seq)-1 else 'medial'] += 1
    return {k: counts[k] for k in ('solus', 'initial', 'medial', 'final')}


def clear_single_document(row):
    return (row['source_doc_count'] == 1 and row['source_direction_code'] in ('1', '2')
            and bool(row['tokens'])
            and not any(t['doubtful'] or t['unknown_span'] for t in row['tokens']))


def summarize(strings):
    frames = frame_index(strings)
    target_frames = [{'frame': list(f), 'members': m} for f, m in sorted(frames.items())
                     if any(s in m for s in SIGNS)]
    sign_rows = []
    for sign in SIGNS:
        found = [{'sequence': list(seq), 'references': sorted(refs),
                  'positions': [i for i, s in enumerate(seq) if s == sign]}
                 for seq, refs in sorted(strings.items()) if sign in seq]
        sign_rows.append({'sign': sign, 'unique_strings': len(found),
                          'references': sum(len(r['references']) for r in found),
                          'occurrences_in_unique_strings': sum(len(r['positions']) for r in found),
                          'rows': found})
    pairs = []
    # A pairwise oracle checks the masked index using a different enumeration.
    hamming = defaultdict(set)
    for left, right in combinations(sorted(strings), 2):
        if len(left) != len(right):
            continue
        changed = [i for i, (a, b) in enumerate(zip(left, right)) if a != b]
        if len(changed) == 1:
            i = changed[0]
            pair = tuple(sorted((left[i], right[i])))
            if all(s in SIGNS for s in pair):
                hamming[pair].add((left, right))
    for a, b in combinations(SIGNS, 2):
        shared = [{'frame': list(f), 'members': m} for f, m in sorted(frames.items())
                  if a in m and b in m]
        cooccurring = [{'sequence': list(s), 'references': sorted(refs)}
                       for s, refs in sorted(strings.items()) if a in s and b in s]
        merged = defaultdict(list)
        for seq, refs in sorted(strings.items()):
            key = tuple('MERGED' if s in (a, b) else s for s in seq)
            merged[key].append({'sequence': list(seq), 'references': sorted(refs)})
        collisions = [{'normalized': list(k), 'originals': v}
                      for k, v in sorted(merged.items()) if len(v) > 1]
        indexed_pairs = {tuple(sorted((tuple(r['members'][a]['sequence']),
                                       tuple(r['members'][b]['sequence'])))) for r in shared}
        assert indexed_pairs == hamming[a, b]
        pairs.append({'signs': [a, b], 'shared_full_frames': shared,
                      'independent_hamming_enumeration_agrees': True,
                      'cooccurring_complete_strings': cooccurring,
                      'counterfactual_merge_collisions': collisions,
                      'counterfactual_unique_string_reduction': len(strings)-len(merged)})
    controls = [{'sign': f'M{i:03d}', 'shared_frames_with': {
        t: [r['frame'] for r in target_frames if t != f'M{i:03d}'
            and t in r['members'] and f'M{i:03d}' in r['members']]
        for t in SIGNS}} for i in range(1, 418)]
    return {'records': sum(map(len, strings.values())), 'unique_strings': len(strings),
            'signs': sign_rows, 'pairs': pairs, 'target_bearing_full_frames': target_frames,
            'all_417_replacement_controls': controls}


def main():
    corpus = 'data/processed/m77_candidate_records.jsonl'
    table_path = 'data/processed/mahadevan_1977_table_i.csv'
    rows = [json.loads(line) for line in (ROOT/corpus).read_text().splitlines()]
    predicates = {'domestic_seals': lambda r: domestic(r) and not eligible(r),
                  'global_seals': lambda r: not eligible(r),
                  'all_clear_single_document_objects_including_solus': clear_single_document}
    result = {'scopes': {}}
    for name, predicate in predicates.items():
        strings = defaultdict(list)
        for row in rows:
            if predicate(row):
                strings[sequence(row)].append(row['source_reference'])
        result['scopes'][name] = summarize(strings)
    primary = {r['sign']: r for r in csv.DictReader((ROOT/table_path).open())}
    counts = Counter(s for row in rows for s in sequence(row))
    result['coverage'] = [{'sign': s,
        'primary_table_i': {k: int(primary[s][k]) for k in ['solus', 'initial', 'medial', 'final', 'total']},
        'export_occurrences_including_doubt_and_multiple_document_records': counts[s],
        'primary_total_minus_export_tokens': int(primary[s]['total'])-counts[s]}
        for s in SIGNS]
    review_paths = ['data/processed/five_stroke_primary_review.json',
                    'data/processed/five_stroke_missing_review.json',
                    'data/processed/stone1471_context_review.json']
    reviews = [json.loads((ROOT/p).read_text()) for p in review_paths]
    for review in reviews:
        for item in review['evidence_files']:
            p = ROOT/item['path']
            assert p.stat().st_size == item['bytes'] and sha256(p) == item['sha256'], item['path']
    recovered = list(reviews[1]['rows'])
    recovered += [dict(r, target_sign='M107',
                       id=f"M77:{r['reference']}:side{r['side']}:line{r['line']}")
                  for r in reviews[0]['rows'] if not r['matches_candidate_export']]
    assert len(recovered) == 6 and len({r['id'] for r in recovered}) == 6
    result['recovered_primary_lines'] = recovered
    for coverage in result['coverage']:
        sign = coverage['sign']
        added = [tuple(t.lstrip('*') for t in r['tokens']) for r in recovered]
        combined = position_counts([sequence(r) for r in rows] + added, sign)
        assert combined == {k: coverage['primary_table_i'][k] for k in combined}
        coverage['reconciled_position_counts'] = combined
        coverage['reconciled_total'] = sum(combined.values())
        occurrence_refs = Counter(r['source_reference'] for r in rows for t in sequence(r) if t == sign)
        occurrence_refs.update(r['reference'] for r in recovered for t in r['tokens'] if t.lstrip('*') == sign)
        primary_rows = reviews[0]['rows'] if sign == 'M107' else reviews[1]['concordance_occurrences'][sign]
        assert occurrence_refs == Counter(r['reference'] for r in primary_rows)
    # A labelled targeted supplement, not a newly representative or fully recovered corpus.
    supplemented = defaultdict(list)
    for row in rows:
        if clear_single_document(row):
            supplemented[sequence(row)].append(row['source_reference'])
    added_ids = []
    for row in recovered:
        if not row['has_primary_loss'] and not row['has_primary_doubt']:
            supplemented[tuple(row['tokens'])].append(row['id'])
            added_ids.append(row['id'])
    result['targeted_primary_supplement'] = {
        'scope': 'Base all-clear single-document sample plus five intact recovered fields; normalized primary lines allow direction3/4 and multiple-field objects. Target-selected, incomplete supplement, not a replacement corpus.',
        'added_ids': added_ids, 'analysis': summarize(supplemented)}
    result['primary_reviews'] = [{'path': p, 'evidence_files': len(r['evidence_files'])}
                                  for p, r in zip(review_paths, reviews)]
    result['stone1471_context'] = {k: reviews[2][k] for k in ['identity', 'accepted_claims', 'caveats']}
    result['limits'] = [
        'Three separate samples; expanded material and site scopes are descriptive sensitivity analyses',
        'The export omits primary lines; raw token deficits do not by themselves identify missing text',
        'Shared contexts cannot distinguish allographs, equal values, different values or other functions',
        'No exact counterpart is an absence in this sample, not a proof of incompatibility',
        'Counterfactual merge is not applied to the stored corpus or catalogue identities',
    ]
    result['new_semantic_values'] = result['new_phonetic_values'] = 0
    inputs = [corpus, table_path, 'data/processed/five_stroke_context_protocol.json',
              'scripts/analyze_m77_foreign.py', 'scripts/audit_stroke_substitution.py']
    inputs += review_paths
    result['input_sha256'] = {p: sha256(ROOT/p) for p in inputs}
    write_json('results/five_stroke_context_audit.json', result)
    print(json.dumps({'coverage': result['coverage'], 'scopes': {
        k: {'records': v['records'], 'unique_strings': v['unique_strings'],
            'signs': [{x: s[x] for x in ['sign','unique_strings','references']} for s in v['signs']],
            'pairs': [{'signs': p['signs'], 'shared_frames': len(p['shared_full_frames']),
                       'cooccurring_strings': len(p['cooccurring_complete_strings']),
                       'merge_reduction': p['counterfactual_unique_string_reduction']} for p in v['pairs']]}
        for k, v in result['scopes'].items()}}, indent=2))


if __name__ == '__main__':
    main()
