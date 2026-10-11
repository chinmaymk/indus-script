"""Independently recompute model compatibility; no primary authentication.

Does not import either pincer audit's implementation. Candidate availability is
taken from the existing context screen, then whole-pair target compatibility is
reconstructed from the two sequence arrays, not target-assignment summaries.
"""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = {
    'both_M216': {'W550': 'M216', 'W555': 'M216'},
    'both_M222': {'W550': 'M222', 'W555': 'M222'},
    'local_split': {'W550': 'M216', 'W555': 'M222'},
    'reversed_split': {'W550': 'M222', 'W555': 'M216'},
}


def main():
    paths = ['results/pincer_context_screen.json',
             'data/raw/lipi_inscriptions.csv',
             'data/processed/pincer_preservation_protocol.json',
             'results/pincer_preservation_audit.json']
    screen = json.loads((ROOT / paths[0]).read_text())
    with (ROOT / paths[1]).open() as handle:
        raw_rows = list(csv.DictReader(handle))
    raw = {r['id']: r for r in raw_rows}
    assert len(raw) == len(raw_rows), 'Nonunique raw row IDs'
    protocol = json.loads((ROOT / paths[2]).read_text())
    audit = json.loads((ROOT / paths[3]).read_text())
    assert protocol['models'] == MODELS
    assert audit['protocol'] == protocol
    for rel, digest in audit['input_sha256'].items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest, rel
    pairs = defaultdict(list)
    for pair in screen['candidate_pairs']:
        pairs[pair['lipi_row']['id']].append(pair)
    reconstructed = []
    for selected in screen['selected_rows']:
        row_id = selected['lipi_row']['id']
        seq = selected['lipi_row']['sequence']
        candidates = pairs[row_id]
        assert [p['pair_id'] for p in candidates] == selected['candidate_pair_ids']
        witnesses = {name: [] for name in MODELS}
        for pair in candidates:
            w = pair['lipi_row']['sequence'][::-1]
            m = pair['m77_candidate_row']['sequence']
            assert len(w) == len(m) and w == seq[::-1]
            target_indices = [i for i, token in enumerate(w) if token in ('W550', 'W555')]
            assert target_indices
            for name, model in MODELS.items():
                mismatches = [i for i in target_indices if m[i] != model[w[i]]]
                if not mismatches:
                    witnesses[name].append(pair['pair_id'])
        reconstructed.append({
            'row_id': row_id, 'cisi': raw[row_id]['cisi'],
            'preservation': raw[row_id]['preservation'],
            'non_target_positions': len(seq) - seq.count('W550') - seq.count('W555'),
            'has_candidate': bool(candidates),
            'model_compatible': {name: (bool(witnesses[name]) if candidates else None) for name in MODELS},
            'compatible_whole_pair_witnesses': witnesses,
        })
    audit_by_id = {r['source']['id']: r for r in audit['rows']}
    assert len(audit_by_id) == len(audit['rows']) == len(reconstructed)
    for row in reconstructed:
        other = audit_by_id[row['row_id']]
        for key in ['non_target_positions', 'has_candidate', 'model_compatible']:
            assert other[key] == row[key], (row['row_id'], key)
        for key, value in other['source'].items():
            assert value == raw[row['row_id']][key], (row['row_id'], key)
    partitions = {}
    selectors = {
        'all': lambda r: True,
        'source_complete': lambda r: r['preservation'] == 'complete',
        'source_complete_two_context_positions': lambda r: r['preservation'] == 'complete' and r['non_target_positions'] >= 2,
    }
    outcomes = {True: 'compatible', False: 'incompatible_given_candidate_set', None: 'no_candidate_uninformative'}
    for name, choose in selectors.items():
        subset = [r for r in reconstructed if choose(r)]
        models = {}
        for model in MODELS:
            groups = {label: [] for label in outcomes.values()}
            for row in subset:
                groups[outcomes[row['model_compatible'][model]]].append(row['cisi'])
            models[model] = groups
        partitions[name] = {
            'selected_rows': len(subset), 'with_candidates': sum(r['has_candidate'] for r in subset),
            'preservation_counts': dict(Counter(r['preservation'] for r in subset)), 'models': models,
        }
    assert partitions == audit['partitions'], 'Partition counts or complete ordered lists disagree'
    assert (len(reconstructed), partitions['all']['with_candidates']) == (93, 36)
    assert partitions['all']['models']['local_split']['incompatible_given_candidate_set'] == ['M-897']
    for partition, expected in [('source_complete', (72, 27)), ('source_complete_two_context_positions', (67, 24))]:
        p = partitions[partition]
        assert (p['selected_rows'], p['with_candidates']) == expected
        assert not p['models']['local_split']['incompatible_given_candidate_set']
    result = {
        'all_checks_passed': True, 'rows_checked': len(reconstructed),
        'model_partition_combinations_checked': 12,
        'scope': 'Computational verification only, conditional on the context screen candidate pairs and raw source preservation labels; not primary authentication, physical-completeness certification, a held-out prediction, or decipherment.',
        'independence': 'No imports from audit_pincer_preservation or screen_pincer_contexts. Whole-pair compatibility reconstructed from reversed W sequence and candidate M sequence, independent of target_assignments summaries; candidate-set discovery itself is not revalidated.',
        'source_complete_caveat': 'Source preservation=complete is not physical certification. Known L9 corner damage remains in this source-labelled sensitivity branch.',
        'partitions': partitions, 'rows': reconstructed,
        'input_sha256': {rel: hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() for rel in paths},
        'established_semantic_values': 0, 'established_phonetic_values': 0,
    }
    output = ROOT / 'results/pincer_preservation_independent.json'
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'all_checks_passed': True, 'rows_checked': len(reconstructed),
                      'model_partition_combinations_checked': 12}, indent=2))


if __name__ == '__main__':
    main()
