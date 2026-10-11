"""Candidate context alignment, never artifact identification or decipherment."""
import json
from collections import Counter, defaultdict
from common import ROOT, read_jsonl, sha256, write_json

TARGETS = {'W550': {'M216', 'M222'}, 'W555': {'M216', 'M222'}}


def feature_map(features):
    support = defaultdict(lambda: defaultdict(set))
    for feature in features:
        for w in feature['wells_graphemes']:
            for m in feature['mahadevan_graphemes']:
                support[w][m].add(feature['id'])
    return {w: {m: sorted(ids) for m, ids in ms.items()} for w, ms in support.items()}


def compatible_positions(w_file_sequence, m_sequence, support):
    if len(w_file_sequence) != len(m_sequence):
        return None
    positions = []
    for i, (w, m) in enumerate(zip(reversed(w_file_sequence), m_sequence)):
        if w in TARGETS:
            if m not in TARGETS[w]:
                return None
            positions.append({'aligned_position_zero_based': i, 'w': w, 'm': m,
                              'basis': 'source_exposed_target_hypothesis'})
        else:
            candidates = support.get(w, {})
            if m not in candidates:
                return None
            positions.append({'aligned_position_zero_based': i, 'w': w, 'm': m,
                              'basis': 'catalogue_feature_membership',
                              'feature_ids': candidates[m],
                              'all_feature_M_candidates': sorted(candidates)})
    return positions


def main():
    paths = ['data/processed/pincer_context_protocol.json',
             'data/processed/lipi_strict.jsonl',
             'data/processed/m77_candidate_strict.jsonl',
             'data/processed/catalogue_features.json']
    protocol = json.loads((ROOT / paths[0]).read_text())
    features = json.loads((ROOT / paths[3]).read_text())
    support = feature_map(features)
    lipi = read_jsonl(paths[1])
    m77 = read_jsonl(paths[2])
    by_length = defaultdict(list)
    for row in m77:
        by_length[len(row['sequence'])].append(row)
    selected = [row for row in lipi if set(row['sequence']) & TARGETS.keys()]
    rows, pairs = [], []
    mapping_tables = {w: {m: [] for m in sorted(ms)} for w, ms in TARGETS.items()}
    for row in selected:
        hits = []
        for other in by_length[len(row['sequence'])]:
            positions = compatible_positions(row['sequence'], other['sequence'], support)
            if positions is None:
                continue
            pair_id = row['id'] + '__' + other['id']
            assignments = [p for p in positions if p['w'] in TARGETS]
            pair = {'pair_id': pair_id, 'lipi_row': row, 'm77_candidate_row': other,
                    'positionwise_support': positions,
                    'target_assignments': assignments,
                    'context_has_multicandidate_feature_membership': any(
                        len(p.get('all_feature_M_candidates', [])) > 1 for p in positions),
                    'archaeological_identity': None}
            pairs.append(pair)
            hits.append(pair)
            for w, m in sorted({(p['w'], p['m']) for p in assignments}):
                mapping_tables[w][m].append(pair_id)
        possible = {w: sorted({a['m'] for hit in hits for a in hit['target_assignments']
                               if a['w'] == w})
                    for w in sorted(set(row['sequence']) & TARGETS.keys())}
        unmapped = sorted({w for w in row['sequence'] if w not in TARGETS and not support.get(w)})
        rows.append({'lipi_row': row, 'reversed_lipi_sequence': row['sequence'][::-1],
                     'equal_length_M77_rows_screened': len(by_length[len(row['sequence'])]),
                     'unmapped_non_target_W_tokens': unmapped,
                     'candidate_pair_ids': [h['pair_id'] for h in hits],
                     'compatible_candidate_rows': len(hits),
                     'compatible_distinct_M77_sequences': len({tuple(h['m77_candidate_row']['sequence']) for h in hits}),
                     'status': 'unmatched' if not hits else 'single_candidate_row' if len(hits) == 1 else 'multiple_candidate_rows',
                     'target_M_candidates_from_matches': possible,
                     'target_mapping_ambiguous': any(len(ms) > 1 for ms in possible.values())})
    summary = {'strict_lipi_rows': len(lipi), 'strict_M77_candidate_rows': len(m77),
               'selected_lipi_rows': len(rows), 'status_counts': dict(Counter(r['status'] for r in rows)),
               'rows_with_unmapped_context': sum(bool(r['unmapped_non_target_W_tokens']) for r in rows),
               'rows_with_target_mapping_ambiguity': sum(r['target_mapping_ambiguous'] for r in rows),
               'compatible_candidate_pairs': len(pairs),
               'pairs_with_multicandidate_context_membership': sum(p['context_has_multicandidate_feature_membership'] for p in pairs)}
    result = {'protocol': protocol, 'summary': summary,
              'original_feature_target_memberships': {w: support.get(w, {}) for w in TARGETS},
              'selected_rows': rows, 'candidate_pairs': pairs,
              'separate_target_mapping_tables': mapping_tables,
              'input_sha256': {p: sha256(ROOT / p) for p in paths},
              'established_semantic_values': 0, 'established_phonetic_values': 0,
              'promoted_artifact_identifications': 0}
    write_json('results/pincer_context_screen.json', result)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
