"""Constrained second-sign discovery and exact adjacent-comb deletion contexts."""
import json
from collections import defaultdict, Counter
from common import ROOT, read_jsonl, sha256, write_json
from screen_pincer_contexts import feature_map, TARGETS

DOMAIN = {f'M{i:03d}' for i in range(1, 418)}


def align(sequence, mseq, target, support, extend_w525=False):
    cursor, masked, segments = 0, None, []
    for i, w in enumerate(reversed(sequence)):
        size = 2 if w == 'W617' else 1
        observed = mseq[cursor:cursor+size]
        if len(observed) != size:
            return None
        if w == target:
            m = observed[0]
            if m not in DOMAIN or (masked is not None and masked != m):
                return None
            masked, basis = m, 'masked_target'
        elif w == 'W617':
            if observed != ['M245', 'M245']:
                return None
            basis = 'declared_double_grid_span'
        elif w == 'W525' and extend_w525:
            if observed != ['M254']:
                return None
            basis = 'experimental_extension_from_two_local_anchors'
        else:
            choices = TARGETS[w] if w in TARGETS else support.get(w, {})
            if observed[0] not in choices:
                return None
            basis = 'prior_pincer_candidates' if w in TARGETS else 'catalogue_membership'
        segments.append({'W': w, 'reversed_W_position': i, 'M': observed,
                         'M_positions': list(range(cursor, cursor+size)), 'basis': basis})
        cursor += size
    return {'masked_M_candidate': masked, 'segments': segments} if cursor == len(mseq) and masked else None


def main():
    paths = ['data/processed/comb_tablet_protocol.json', 'data/processed/lipi_strict.jsonl',
             'data/processed/catalogue_features.json', 'data/processed/m77_candidate_strict.jsonl',
             'data/processed/m77_candidate_records.jsonl']
    support = feature_map(json.loads((ROOT / paths[2]).read_text()))
    corpus = read_jsonl(paths[1])
    strict = read_jsonl(paths[3])
    diagnostic = [r for r in read_jsonl(paths[4]) if r['source_doc_count'] > 1 and str(r['source_direction_code']) == '1'
                  and r['tokens'] and all(t['sign'] is not None and not t['doubtful'] and not t['unknown_span'] for t in r['tokens'])]
    pools = {'strict': [(r, r['sequence']) for r in strict],
             'multi_document_locator_only': [(r, [t['sign'] for t in r['tokens']]) for r in diagnostic]}
    experiments = []
    for target in ('W195', 'W554'):
        selected = [r for r in corpus if target in r['sequence']]
        for extension in (False, True):
            for pool, candidates in pools.items():
                pairs = []
                for row in selected:
                    for m, mseq in candidates:
                        hit = align(row['sequence'], mseq, target, support, extension)
                        if hit:
                            pairs.append({'lipi_row': row, 'M_record': m, **hit, 'artifact_identity': None})
                experiments.append({'target': target, 'experimental_W525_M254_extension': extension,
                    'pool': pool, 'pool_record_count': len(candidates), 'selected_rows': selected,
                    'pairs': pairs, 'summary': {'selected_rows': len(selected),
                    'selected_distinct_strings': len({tuple(r['sequence']) for r in selected}),
                    'matched_rows': len({p['lipi_row']['id'] for p in pairs}), 'pairs': len(pairs),
                    'candidate_M_pair_incidences': dict(Counter(p['masked_M_candidate'] for p in pairs))},
                    'source_memberships_hidden_for_target': sorted(support.get(target, {}))})
    strings = defaultdict(list)
    for row in corpus:
        strings[tuple(row['sequence'])].append(row)
    adjacent = []
    for seq, rows in sorted(strings.items()):
        for i in range(len(seq)-1):
            if seq[i] != 'W400' or seq[i+1] not in ('W525', 'W526', 'W527'):
                continue
            shorter = seq[:i] + seq[i+1:]
            adjacent.append({'sequence': list(seq), 'rows': rows, 'comb': seq[i+1],
                             'W400_file_position': i, 'deleted_sequence': list(shorter),
                             'exact_deletion_counterpart_rows': strings.get(shorter, [])})
    result = {'protocol': json.loads((ROOT / paths[0]).read_text()), 'experiments': experiments,
              'W400_comb_adjacent_contexts': adjacent,
              'adjacency_summary': {c: {'distinct_strings': sum(a['comb'] == c for a in adjacent),
                  'rows': sum(len(a['rows']) for a in adjacent if a['comb'] == c),
                  'strings_with_exact_W400_deletion': sum(bool(a['exact_deletion_counterpart_rows']) for a in adjacent if a['comb'] == c)}
                  for c in ('W525', 'W526', 'W527')},
              'input_sha256': {p: sha256(ROOT / p) for p in paths},
              'established_semantic_values': 0, 'established_phonetic_values': 0, 'global_mapping_promotions': 0}
    write_json('results/comb_tablet_screen.json', result)
    for e in experiments:
        print(e['target'], e['experimental_W525_M254_extension'], e['pool'], e['summary'])
    print('ADJACENCY', result['adjacency_summary'])


if __name__ == '__main__':
    main()
