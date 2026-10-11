"""Independent pairwise-Hamming audit of M102/M106 substitution claims.

Deliberately does not import the parent mask-index implementation. Filtering is
spelled out here and cross-checked against the established selection helpers.
No sign meanings or sounds are inferred.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    from analyze_m77_foreign import eligible, sequence, DOMESTIC_RANGES, NAMED_OTHER
    path = 'data/processed/m77_candidate_records.jsonl'
    rows = [json.loads(line) for line in (ROOT/path).read_text().splitlines()]
    strings = defaultdict(list)
    for row in rows:
        named = row['source_reference'] in NAMED_OTHER or any(
            lo <= int(row['source_reference']) <= hi for lo, hi in DOMESTIC_RANGES)
        selected = (row['source_object_code'] == '1'
                    and row['source_doc_count'] == 1
                    and row['source_direction_code'] in ['1', '2']
                    and len(row['tokens']) >= 2
                    and all(not token['doubtful'] and not token['unknown_span']
                            for token in row['tokens']))
        assert selected == (not eligible(row))
        if named and selected:
            seq = tuple(token['sign'] for token in row['tokens'])
            assert seq == sequence(row)
            strings[seq].append(row['source_reference'])
    all_pairs, target_pairs = [], []
    length_counts = Counter(map(len, strings))
    # Exhaustively compare unordered same-length complete strings. The change
    # index is discovered by Hamming distance, not by masking lookup keys.
    for left, right in combinations(sorted(strings), 2):
        if len(left) != len(right):
            continue
        changed = [i for i, (a, b) in enumerate(zip(left, right)) if a != b]
        if len(changed) != 1:
            continue
        i = changed[0]
        pair = {'left': list(left), 'left_references': sorted(strings[left]),
                'right': list(right), 'right_references': sorted(strings[right]),
                'changed_index': i, 'substitution': sorted([left[i], right[i]])}
        all_pairs.append(pair)
        if pair['substitution'] == ['M102', 'M106']:
            target_pairs.append(pair)
    frames = []
    for pair in target_pairs:
        seq = tuple(pair['left'])
        index = pair['changed_index']
        occupants = []
        for candidate, refs in sorted(strings.items()):
            if (len(candidate) == len(seq)
                and all(candidate[j] == seq[j] for j in range(len(seq)) if j != index)):
                occupants.append({'sign': candidate[index], 'sequence': list(candidate),
                                  'references': sorted(refs)})
        frame = list(seq)
        frame[index] = '?'
        frames.append({'frame': frame, 'changed_index': index, 'occupants': occupants})
    partial = []
    for seq, refs in sorted(strings.items()):
        for i, sign in enumerate(seq):
            if sign in ['M102', 'M106'] and seq[i+1:i+3] == ('M287', 'M342'):
                partial.append({'sequence': list(seq), 'references': sorted(refs),
                                'changed_sign': sign, 'index': i,
                                'left_complete_context': list(seq[:i]),
                                'right_complete_context': list(seq[i+1:]),
                                'at_end': i+3 == len(seq)})
    excluded_apparent_solus = []
    for row in rows:
        candidate = tuple(t['sign'] for t in row['tokens'])
        if candidate in [('M102', 'M287', 'M342'), ('M106', 'M287', 'M342')] and eligible(row):
            excluded_apparent_solus.append({'reference': row['source_reference'],
                                           'diplomatic': row['diplomatic'],
                                           'exclusion_reasons': eligible(row)})
    target_with_curve_terminal = [pair for pair in target_pairs
        if tuple(pair['left'][pair['changed_index']+1:pair['changed_index']+3])
           == ('M287', 'M342')]
    output = {
        'method': 'Exhaustive unordered same-length complete-string Hamming-distance-one pairs',
        'sample': {'records': sum(map(len, strings.values())), 'unique_strings': len(strings),
                   'same_length_unordered_pairs_examined': sum(n*(n-1)//2 for n in length_counts.values()),
                   'hamming_one_pairs_all_substitutions': len(all_pairs)},
        'target_pair_count': len(target_pairs), 'target_pairs': target_pairs,
        'target_exact_frames_with_all_occupants': frames,
        'target_pairs_followed_by_M287_M342': target_with_curve_terminal,
        'excluded_apparent_solus_counterpart_records': excluded_apparent_solus,
        'partial_M102_or_M106_M287_M342_matches': partial,
        'all_substitution_pair_counts': [{'signs': list(signs), 'count': count}
            for signs, count in sorted(Counter(tuple(p['substitution']) for p in all_pairs).items())],
        'new_semantic_values': 0, 'new_phonetic_values': 0,
        'input_sha256': {p: digest(p) for p in [path, 'scripts/analyze_m77_foreign.py',
                                                   'scripts/verify_stroke_substitutions_independent.py']},
        'limits': ['Exploratory same-corpus analysis, not a held-out test.',
                   'Transcription-based; this script does not inspect glyph images.',
                   'Complete strings are deduplicated; independence of objects or producers is not established.',
                   'Distributional substitution cannot distinguish quantities, phonetic alternatives, lexical alternatives, allographs, or other sign functions.'],
    }
    (ROOT/'results/stroke_substitution_independent_review.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k not in ['all_substitution_pair_counts']}, indent=2))


if __name__ == '__main__':
    main()
