"""Independent masked-target/adjacent-deletion computation verification."""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slot_alignment(w_sequence, m_sequence, hidden, memberships, extend):
    allowed, kinds, ownership = [], [], []
    for w in w_sequence[::-1]:
        start = len(allowed)
        if w == hidden:
            values, kind = [{f'M{i:03d}' for i in range(1, 418)}], 'masked_target'
        elif w == 'W617':
            values, kind = [{'M245'}, {'M245'}], 'declared_double_grid_span'
        elif w == 'W525' and extend:
            values, kind = [{'M254'}], 'experimental_extension_from_two_local_anchors'
        elif w in ('W550', 'W555'):
            values, kind = [{'M216', 'M222'}], 'prior_pincer_candidates'
        else:
            values, kind = [memberships.get(w, set())], 'catalogue_membership'
        allowed.extend(values)
        kinds.extend([kind] * len(values))
        ownership.append((w, list(range(start, len(allowed)))))
    if len(allowed) != len(m_sequence) or any(m not in options for m, options in zip(m_sequence, allowed)):
        return None
    masked = {m for m, kind in zip(m_sequence, kinds) if kind == 'masked_target'}
    if len(masked) != 1:
        return None
    return {'masked_M_candidate': next(iter(masked)),
            'segments': [{'W': w, 'reversed_W_position': i, 'M': [m_sequence[j] for j in indices],
                          'M_positions': indices, 'basis': kinds[indices[0]]}
                         for i, (w, indices) in enumerate(ownership)]}


def main():
    paths = ['data/processed/comb_tablet_protocol.json', 'data/processed/lipi_strict.jsonl',
             'data/processed/catalogue_features.json', 'data/processed/m77_candidate_strict.jsonl',
             'data/processed/m77_candidate_records.jsonl', 'results/comb_tablet_screen.json']
    protocol = json.loads((ROOT / paths[0]).read_text())
    features = json.loads((ROOT / paths[2]).read_text())
    corpus, strict, records = [[json.loads(line) for line in (ROOT / p).read_text().splitlines() if line.strip()]
                               for p in (paths[1], paths[3], paths[4])]
    reported = json.loads((ROOT / paths[5]).read_text())
    assert reported['protocol'] == protocol
    for p, digest in reported['input_sha256'].items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == digest, p
    memberships = defaultdict(set)
    for feature in features:
        for w in feature['wells_graphemes']:
            memberships[w].update(feature['mahadevan_graphemes'])
    diagnostics = []
    for record in records:
        if record['source_doc_count'] <= 1 or str(record['source_direction_code']) != '1':
            continue
        tokens = record['tokens']
        if tokens and all(t['sign'] is not None and not t['doubtful'] and not t['unknown_span'] for t in tokens):
            diagnostics.append(record)
    pool_records = {'strict': strict, 'multi_document_locator_only': diagnostics}
    recomputed, compact = [], []
    for hidden in ('W195', 'W554'):
        selected = [r for r in corpus if hidden in r['sequence']]
        for extend in (False, True):
            for pool, candidates in pool_records.items():
                pairs, unique_context_pairs = [], set()
                for row in selected:
                    for candidate in candidates:
                        seq = candidate['sequence'] if pool == 'strict' else [t['sign'] for t in candidate['tokens']]
                        alignment = slot_alignment(row['sequence'], seq, hidden, memberships, extend)
                        if alignment is None:
                            continue
                        pairs.append({'lipi_row': row, 'M_record': candidate, **alignment, 'artifact_identity': None})
                        unique_context_pairs.add((tuple(row['sequence']), tuple(seq), alignment['masked_M_candidate']))
                summary = {'selected_rows': len(selected),
                           'selected_distinct_strings': len({tuple(r['sequence']) for r in selected}),
                           'matched_rows': len({p['lipi_row']['id'] for p in pairs}), 'pairs': len(pairs),
                           'candidate_M_pair_incidences': dict(Counter(p['masked_M_candidate'] for p in pairs))}
                recomputed.append({'target': hidden, 'experimental_W525_M254_extension': extend,
                    'pool': pool, 'pool_record_count': len(candidates), 'selected_rows': selected,
                    'pairs': pairs, 'summary': summary, 'source_memberships_hidden_for_target': sorted(memberships.get(hidden, set()))})
                compact.append({'target': hidden, 'experimental_W525_M254_extension': extend,
                    'pool': pool, 'summary': summary,
                    'distinct_W_sequence_M_sequence_candidate_triples': len(unique_context_pairs),
                    'deduplicated_context_candidate_incidences': dict(Counter(p[2] for p in unique_context_pairs))})
    assert recomputed == reported['experiments'], 'Experiments, ordered full pairs, metadata, segments or counts disagree'
    index = defaultdict(list)
    for row in corpus:
        index[tuple(row['sequence'])].append(row)
    adjacent = []
    for sequence in sorted(index):
        for i, w in enumerate(sequence):
            if w != 'W400' or i + 1 >= len(sequence) or sequence[i + 1] not in ('W525', 'W526', 'W527'):
                continue
            shorter = tuple(w for j, w in enumerate(sequence) if j != i)
            # Find equality against entire other strings, not only neighbors.
            matches = [r for r in corpus if tuple(r['sequence']) == shorter]
            adjacent.append({'sequence': list(sequence), 'rows': index[sequence], 'comb': sequence[i + 1],
                             'W400_file_position': i, 'deleted_sequence': list(shorter),
                             'exact_deletion_counterpart_rows': matches})
    assert adjacent == reported['W400_comb_adjacent_contexts']
    adjacency_summary = {comb: {'distinct_strings': sum(a['comb'] == comb for a in adjacent),
                               'rows': sum(len(a['rows']) for a in adjacent if a['comb'] == comb),
                               'strings_with_exact_W400_deletion': sum(bool(a['exact_deletion_counterpart_rows']) for a in adjacent if a['comb'] == comb)}
                         for comb in ('W525', 'W526', 'W527')}
    assert adjacency_summary == reported['adjacency_summary']
    for key in ['established_semantic_values', 'established_phonetic_values', 'global_mapping_promotions']:
        assert reported[key] == 0
    # Boundary checks independently exercise masked consistency and extension.
    assert slot_alignment(['W195', 'W195'], ['M054', 'M054'], 'W195', {}, False)
    assert slot_alignment(['W195', 'W195'], ['M054', 'M216'], 'W195', {}, False) is None
    assert slot_alignment(['W525', 'W554'], ['M054', 'M254'], 'W554', {}, False) is None
    assert slot_alignment(['W525', 'W554'], ['M054', 'M254'], 'W554', {}, True)
    result = {'all_checks_passed': True, 'experiment_count': len(recomputed),
        'pair_incidences_checked_across_experiments': sum(len(e['pairs']) for e in recomputed),
        'segment_incidences_checked_across_experiments': sum(len(p['segments']) for e in recomputed for p in e['pairs']),
        'experiments': compact, 'adjacency_summary': adjacency_summary,
        'input_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        'method': 'No production helper imports. Independently builds expanded Cartesian slot constraints, checks all candidate records, enforces consistent repeated masked tokens, and compares full ordered experiment and adjacency records.',
        'scope': 'Computational verification only. Strict candidates and multi-document diagnostic locators remain separate. Pair incidences include duplicate contexts and duplicated extension branches; distinct sequence triples are also reported, but neither measure is a count of independent artifacts. No primary identity or global sign mapping is authenticated.',
        'established_semantic_values': 0, 'established_phonetic_values': 0, 'global_mapping_promotions': 0}
    (ROOT / 'results/comb_tablet_independent.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: result[k] for k in ('all_checks_passed', 'experiment_count', 'pair_incidences_checked_across_experiments', 'segment_incidences_checked_across_experiments', 'adjacency_summary')}, indent=2))


if __name__ == '__main__':
    main()
