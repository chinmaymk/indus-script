"""Independent slot-constraint verification of the one-to-two W617 screen.

No production screen or alignment helpers are imported. This verifies the
declared computation, not physical sign identity or a semantic composition.
"""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    paths = ['data/processed/double_grid_protocol.json',
             'results/pincer_context_screen.json',
             'data/processed/catalogue_features.json',
             'data/processed/lipi_strict.jsonl',
             'data/processed/m77_candidate_strict.jsonl',
             'results/double_grid_screen.json']
    protocol, old, features = [json.loads((ROOT / p).read_text()) for p in paths[:3]]
    lipi, m77 = [[json.loads(line) for line in (ROOT / p).read_text().splitlines() if line.strip()]
                for p in paths[3:5]]
    reported = json.loads((ROOT / paths[5]).read_text())
    assert reported['protocol'] == protocol
    for rel, digest in reported['input_sha256'].items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest, rel
    links = defaultdict(set)
    evidence = defaultdict(set)
    for feature in features:
        for w in feature['wells_graphemes']:
            for m in feature['mahadevan_graphemes']:
                links[w].add(m)
                evidence[w, m].add(feature['id'])
    prior_rows = {r['lipi_row']['id'] for r in old['selected_rows']}
    # Verify the inherited selection itself, rather than assuming its label.
    assert prior_rows == {r['id'] for r in lipi if {'W550', 'W555'}.intersection(r['sequence'])}
    prior_pairs = {p['pair_id'] for p in old['candidate_pairs']}
    rows, pairs = [], []
    for row in lipi:
        reversed_w = row['sequence'][::-1]
        if row['id'] not in prior_rows and 'W617' not in reversed_w:
            continue
        # Build an expanded Cartesian constraint space independently of M rows.
        # Each slot is an allowed set; membership in their Cartesian product is
        # checked without materializing every possible M-string.
        slots, positions_for_w = [], []
        for w in reversed_w:
            start = len(slots)
            if w == 'W617':
                slots.extend([{'M245'}, {'M245'}])
            elif w in ('W550', 'W555'):
                slots.append({'M216', 'M222'})
            else:
                slots.append(set(links[w]))
            positions_for_w.append(list(range(start, len(slots))))
        hits = []
        for other in m77:
            m = other['sequence']
            if len(m) != len(slots):
                continue
            if any(token not in allowed for token, allowed in zip(m, slots)):
                continue
            pair_id = row['id'] + '__' + other['id']
            hits.append(pair_id)
            segments = []
            for i, (w, positions) in enumerate(zip(reversed_w, positions_for_w)):
                segment = {'reversed_W_position': i, 'W': w,
                           'M_positions': positions, 'M': [m[j] for j in positions]}
                if w == 'W617':
                    segment['basis'] = 'source_exposed_double_grid_tokenization'
                elif w in ('W550', 'W555'):
                    segment.update(basis='target_hypothesis', feature_ids=[])
                else:
                    segment.update(basis='feature_membership',
                                   feature_ids=sorted(evidence[w, m[positions[0]]]))
                segments.append(segment)
            pairs.append({'pair_id': pair_id, 'lipi_row': row, 'm77_candidate_row': other,
                          'segments': segments, 'previous_pincer_candidate': pair_id in prior_pairs,
                          'archaeological_identity': None})
        rows.append({'lipi_row': row, 'W_tokens': len(reversed_w),
                     'expected_M_tokens': len(slots), 'W617_occurrences': reversed_w.count('W617'),
                     'candidate_pair_ids': hits, 'in_previous_pincer_selection': row['id'] in prior_rows})
    assert rows == reported['rows'], 'Selected rows, constraints or ordered candidate lists differ'
    assert pairs == reported['candidate_pairs'], 'Full candidate pairs or segment records differ'
    summaries = {}
    groups = {'pincer': [r for r in rows if r['in_previous_pincer_selection']],
              'all_W617': [r for r in rows if r['W617_occurrences'] > 0]}
    for name, group in groups.items():
        sizes = [len(r['candidate_pair_ids']) for r in group]
        summaries[name] = {'selected_rows': len(group), 'rows_with_candidates': sum(n > 0 for n in sizes),
                           'candidate_pairs': sum(sizes), 'rows_with_multiple_candidates': sum(n > 1 for n in sizes)}
    current_pincer_pairs = {p for r in groups['pincer'] for p in r['candidate_pair_ids']}
    assert prior_pairs <= current_pincer_pairs
    summaries['prior_pincer_pairs_preserved'] = len(prior_pairs)
    summaries['new_pincer_pairs'] = len(current_pincer_pairs - prior_pairs)
    summaries['new_pincer_candidate_rows'] = [r['lipi_row']['cisi_original'] for r in groups['pincer']
        if r['candidate_pair_ids'] and set(r['candidate_pair_ids']).isdisjoint(prior_pairs)]
    assert summaries == reported['summary'], 'Summary differs'
    assert (summaries['pincer']['selected_rows'], summaries['pincer']['rows_with_candidates'],
            summaries['pincer']['candidate_pairs']) == (93, 41, 66)
    assert (summaries['all_W617']['selected_rows'], summaries['all_W617']['rows_with_candidates'],
            summaries['all_W617']['candidate_pairs']) == (59, 22, 38)
    assert len(summaries['new_pincer_candidate_rows']) == 5 and summaries['new_pincer_pairs'] == 11
    for key in ['established_semantic_values', 'established_phonetic_values', 'promoted_artifact_identifications']:
        assert reported[key] == 0
    result = {
        'all_checks_passed': True, 'summary': summaries,
        'union_selected_rows_checked': len(rows), 'union_candidate_pairs_checked': len(pairs),
        'segments_checked': sum(len(p['segments']) for p in pairs),
        'verified_fields': ['full selected-row records', 'ordered full candidate-pair records and segments',
                            'feature provenance', 'prior-candidate flags', 'all summary fields',
                            'inherited pincer selection', 'zero promotions and values', 'input hashes'],
        'method': 'Independently flatten reversed W sequences into constrained M slots (two singleton M245 slots only for W617), then test every M77 candidate row for membership in the Cartesian product of allowed slot sets. No production helper imports.',
        'scope': 'Computational verification of a source-exposed tokenization hypothesis, not primary sign authentication, artifact identity, global tokenization equivalence, independent corpus replication, or semantic composition.',
        'input_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'promoted_artifact_identifications': 0,
    }
    (ROOT / 'results/double_grid_independent.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
