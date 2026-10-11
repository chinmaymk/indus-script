"""Describe competing segmentations of a selected chain in the existing corpus.

Exploratory recurrence only: overlapping chunks are not authenticated words.
The selected example was found using this same corpus; removing it is not an
independent held-out validation experiment.
"""
from collections import Counter, defaultdict
import json
from common import ROOT, sha256, write_json
from analyze_m77_foreign import eligible, sequence, DOMESTIC_RANGES, NAMED_OTHER


PATTERNS = {
    'shared_three': ('M391', 'M099', 'M387'),
    'shared_two': ('M102', 'M287'),
    'overlapping_left_pair': ('M391', 'M099'),
    'overlapping_right_pair': ('M099', 'M387'),
    'longer_four_sign_prefix': ('M102', 'M287', 'M329', 'M343'),
    'three_strokes_curve_terminal': ('M102', 'M287', 'M342'),
    'five_strokes_curve_terminal': ('M106', 'M287', 'M342'),
}
SELECTED = {'2463', '2302', '4084'}


def positions(seq, pattern):
    return [i for i in range(len(seq)-len(pattern)+1)
            if tuple(seq[i:i+len(pattern)]) == tuple(pattern)]


def domestic(row):
    return row['source_reference'] in NAMED_OTHER or any(
        lo <= int(row['source_reference']) <= hi for lo, hi in DOMESTIC_RANGES)


def profile(strings, pattern):
    occurrences, before, after = [], Counter(), Counter()
    for seq, refs in sorted(strings.items()):
        for i in positions(seq, pattern):
            left = seq[i-1] if i else 'BOS'
            right = seq[i+len(pattern)] if i+len(pattern)<len(seq) else 'EOS'
            before[left] += 1
            after[right] += 1
            occurrences.append({'sequence': list(seq), 'references': sorted(refs),
                                'start_index': i, 'left_neighbor': left, 'right_neighbor': right})
    seqs = {tuple(o['sequence']) for o in occurrences}
    refs = {ref for o in occurrences for ref in o['references']}
    return {'pattern': list(pattern), 'unique_strings': len(seqs),
            'distinct_references': len(refs), 'occurrences_in_unique_strings': len(occurrences),
            'initial_occurrences': before['BOS'], 'final_occurrences': after['EOS'],
            'all_417_neighbor_counts': [
                {'sign': f'M{i:03d}', 'before': before[f'M{i:03d}'], 'after': after[f'M{i:03d}']}
                for i in range(1, 418)],
            'occurrences': occurrences}


def main():
    input_path = 'data/processed/m77_candidate_records.jsonl'
    rows = [json.loads(line) for line in (ROOT / input_path).read_text().splitlines()]
    primary_path = 'data/processed/chain_segment_primary_review.json'
    primary = json.loads((ROOT / primary_path).read_text())
    for item in primary['evidence_files']:
        p = ROOT / item['path']
        assert p.stat().st_size == item['bytes'] and sha256(p) == item['sha256'], item['path']
    for checked in primary['rows']:
        found = [r for r in rows if r['source_reference'] == checked['reference']]
        assert len(found) == 1 and list(sequence(found[0])) == checked['tokens']
    artifact_path = 'data/processed/chain_artifact_identity_review.json'
    artifacts = json.loads((ROOT / artifact_path).read_text())
    for item in artifacts['evidence_files']:
        p = ROOT / item['path']
        assert p.stat().st_size == item['bytes'] and sha256(p) == item['sha256'], item['path']
    assert {r['m77_reference'] for r in artifacts['rows']} == SELECTED
    strings = defaultdict(list)
    for row in rows:
        if domestic(row) and not eligible(row):
            strings[sequence(row)].append(row['source_reference'])
    selected_strings = {s for s, refs in strings.items() if SELECTED.intersection(refs)}
    assert len(selected_strings) == 3
    remaining = {s: refs for s, refs in strings.items() if s not in selected_strings}
    profiles = {name: {'all': profile(strings, p),
                      'excluding_selected_complete_strings': profile(remaining, p)}
                for name, p in PATTERNS.items()}
    excluded = []
    for row in rows:
        matching = [name for name in ['shared_three', 'shared_two']
                    if positions(sequence(row), PATTERNS[name])]
        reasons = eligible(row) + ([] if domestic(row) else ['not_named_domestic'])
        if matching and reasons:
            excluded.append({'reference': row['source_reference'], 'patterns': matching,
                             'diplomatic': row['diplomatic'], 'exclusions': reasons})
    frames = []
    for seq, refs in sorted(strings.items()):
        for i in range(len(seq)-2):
            if seq[i]=='M391' and seq[i+2]=='M387':
                frames.append({'sequence': list(seq), 'references': sorted(refs),
                               'start_index': i, 'middle_sign': seq[i+1]})
    predecessor_counts = Counter()
    predecessor_rows = []
    for seq, refs in sorted(strings.items()):
        for i in positions(seq, ('M287',)):
            prev = seq[i-1] if i else 'BOS'
            predecessor_counts[prev] += 1
            predecessor_rows.append({'sequence': list(seq), 'references': sorted(refs),
                                     'curve_index': i, 'predecessor': prev})
    result = {
        'status': 'Exploratory recurrence and boundary alternatives; no semantic identification',
        'samples': {'records': sum(map(len, strings.values())), 'unique_strings': len(strings),
                    'selected_complete_strings': len(selected_strings),
                    'remaining_unique_strings': len(remaining)},
        'profiles': profiles,
        'excluded_whole_records_with_exact_target_occurrence': excluded,
        'M391_any_M387': frames,
        'M287_predecessors': {'counts_in_unique_strings': dict(sorted(predecessor_counts.items())),
                             'occurrences': predecessor_rows},
        'scope': [
            'Same exploratory corpus used to select the example; exclusion is sensitivity, not held-out validation',
            'Counts use complete-string deduplication; different strings are not proven independent artifacts',
            'Overlapping patterns are dependent and can cross unknown word boundaries',
            'No frequency threshold or significance level identifies a name or numerical expression',
            'Stroke descriptors concern the catalogue shapes; no number values or units assigned',
        ],
        'new_semantic_values': 0, 'new_phonetic_values': 0,
        'primary_recurrence_review': {'path': primary_path,
                                      'references': [r['reference'] for r in primary['rows']],
                                      'pinned_evidence_files': len(primary['evidence_files'])},
        'artifact_identity_review': {'path': artifact_path,
                                     'rows': artifacts['rows'],
                                     'pinned_evidence_files': len(artifacts['evidence_files']),
                                     'interpretation': 'Object identities and contexts only; no dated personal relationships'},
        'input_sha256': {p: sha256(ROOT / p) for p in [input_path,
            primary_path, artifact_path,
            'results/consistent_chain_audit.json', 'data/processed/consistent_chain_primary_review.json',
            'scripts/analyze_m77_foreign.py']},
    }
    write_json('results/chain_segment_audit.json', result)
    print(json.dumps({'samples': result['samples'], 'patterns': {
        name: {scope: {k: profile[k] for k in ['unique_strings', 'distinct_references',
                                             'initial_occurrences', 'final_occurrences']}
               for scope, profile in value.items()}
        for name, value in profiles.items()}}, indent=2))


if __name__ == '__main__':
    main()
