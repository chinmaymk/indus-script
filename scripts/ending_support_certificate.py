"""Exact existence certificate for rectangles in the within-length ending shuffle."""
import argparse
from collections import Counter, defaultdict
import hashlib
from itertools import combinations
import json
from pathlib import Path

from analyze_kober_alternations import clean_rows, rectangle_summary

ROOT = Path(__file__).resolve().parents[1]


def support_certificate(sequences, ending_length):
    """Decide whether ANY allowed ending permutation can contain a four-cycle.

    Input slots are retained, including repetitions; permutations may collide.
    A fixed stem belongs to exactly one total-length stratum for fixed k.
    """
    if ending_length not in (1, 2):
        raise ValueError('Ending length must be 1 or 2')
    slots = [tuple(s) for s in sequences if len(s) > ending_length]
    stems = Counter(s[:-ending_length] for s in slots)
    endings = defaultdict(Counter)
    for seq in slots:
        endings[len(seq)][seq[-ending_length:]] += 1
    repeated = sorted(s for s, count in stems.items() if count >= 2)
    pairs = []
    possible_rectangles = 0
    for a, b in combinations(repeated, 2):
        la, lb = len(a)+ending_length, len(b)+ending_length
        if la == lb:
            available = sorted(e for e, count in endings[la].items() if count >= 2)
            threshold = 'Each of two distinct endings needs two copies in the common stratum.'
        else:
            available = sorted(set(endings[la]) & set(endings[lb]))
            threshold = 'Each of two distinct endings needs one copy in each stratum.'
        count = len(available)*(len(available)-1)//2
        possible_rectangles += count
        pairs.append({'stems': [list(a), list(b)], 'total_lengths': [la, lb],
                      'stem_slot_counts': [stems[a], stems[b]],
                      'eligible_endings': [list(e) for e in available],
                      'feasible_ending_pair_count': count, 'criterion': threshold,
                      'witness_ending_pair': [list(e) for e in available[:2]] if count else None})
    feasible = possible_rectangles > 0
    observed = rectangle_summary(slots, ending_length)['four_cycles']
    if observed > 0 and not feasible:
        raise AssertionError('Observed rectangle must belong to permutation support')
    return {'ending_length': ending_length, 'eligible_slots': len(slots),
            'unique_starting_sequences': len(set(slots)),
            'observed_four_cycles': observed,
            'repeated_stems': [{'stem': list(s), 'slot_count': stems[s],
                                'total_length': len(s)+ending_length} for s in repeated],
            'length_strata': [{'total_length': length, 'slots': sum(counts.values()),
                               'ending_multiplicities': [{'ending': list(e), 'count': n}
                                                        for e, n in sorted(counts.items())]}
                              for length, counts in sorted(endings.items())],
            'candidate_stem_pair_count': len(pairs), 'stem_pair_certificates': pairs,
            'individually_feasible_rectangle_count': possible_rectangles,
            'any_rectangle_in_permutation_support': feasible,
            'all_permutations_have_zero_four_cycles': not feasible,
            'conclusion': ('At least one allowed permutation has a rectangle; this does not establish a nonconstant statistic or useful power.'
                           if feasible else
                           'Every allowed permutation has zero rectangles: exact support degeneracy, not a Monte Carlo sampling accident.'),
            'count_caveat': 'Individually feasible rectangles need not be simultaneously realizable; this count is neither a maximum score nor a number of permutations.'}


def analyze(corpus):
    rows, excluded = clean_rows(corpus)
    seqs = [r['sequence'] for r in rows]
    return {'schema_version': 'ending-support-certificate-1',
            'coverage': {'corpus_rows': len(corpus['rows']), 'clean_rows': len(rows),
                         'clean_unique_sequences': len(set(seqs)), 'excluded_rows': len(excluded)},
            'terminal_lengths': {str(k): {
                'row_slot': support_certificate(seqs, k),
                'unique_sequence_slot': support_certificate(sorted(set(seqs)), k)} for k in (1, 2)},
            'assumptions': ['Uses exactly the clean-row filter and rectangle statistic of analyze_kober_alternations.py.',
                            'Nonempty exact stems remain fixed; atomic ending blocks permute within total length.',
                            'Both bases allow collisions after shuffling; unique-sequence input is deduplicated only before shuffling.',
                            'No archaeological, sign-family, or semantic constraints are imposed on permutations.'],
            'limitations': ['Only an exact support calculation for this specified statistic and conditional null.',
                            'Zero support is not evidence against language, inflection, or administrative labels.',
                            'This does not test historical generation, phonetic values, or translations.']}


def pin(path):
    return {'path': str(path.resolve().relative_to(ROOT)) if path.resolve().is_relative_to(ROOT) else str(path.resolve()),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, default=ROOT/'data/processed/m77_verified/corpus_v3.json')
    parser.add_argument('--output', type=Path, default=ROOT/'results/ending_support_v3.json')
    args = parser.parse_args()
    result = analyze(json.loads(args.corpus.read_bytes()))
    result['source_pins'] = [pin(args.corpus), pin(Path(__file__)),
                             pin(ROOT/'scripts/analyze_kober_alternations.py')]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'coverage': result['coverage'],
                      'any_rectangle_in_permutation_support': {
                          k: {basis: cert['any_rectangle_in_permutation_support'] for basis, cert in values.items()}
                          for k, values in result['terminal_lengths'].items()}}))


if __name__ == '__main__':
    main()
