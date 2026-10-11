"""Exploratory exact-stem/ending rectangles; no morphological interpretation."""
import argparse
from collections import Counter, defaultdict
import hashlib
from itertools import combinations
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261010


def clean_rows(corpus):
    if corpus.get('schema_version') != 'verified-m77-1':
        raise ValueError('Requires verified-m77-1 corpus')
    if corpus.get('coverage_complete_for_manifest') is not True or corpus.get('unresolved_rows') != 0:
        raise ValueError('Requires complete manifest coverage and zero unresolved rows')
    if corpus.get('normalized_order') != 'right_to_left':
        raise ValueError('Requires already normalized right_to_left; never reverse')
    selected, excluded, seen = [], [], set()
    for row in corpus['rows']:
        key = tuple(row[k] for k in ('reference', 'side', 'line'))
        if key in seen:
            raise ValueError(f'Duplicate row key: {key}')
        seen.add(key)
        if row.get('normalized_order') != 'right_to_left':
            raise ValueError(f'Unexpected row order: {key}')
        tokens, segments = row['tokens'], row['segments']
        if not tokens or len(tokens) != len(segments):
            raise ValueError(f'Malformed tokens/segments: {key}')
        reasons = set()
        for token, segment in zip(tokens, segments):
            if not isinstance(token, str) or type(segment.get('source_doubt')) is not bool:
                raise ValueError(f'Malformed token/source_doubt: {key}')
            kind, doubt = segment.get('kind'), segment['source_doubt']
            if 'reviewer_uncertainty' in segment and type(segment['reviewer_uncertainty']) is not bool:
                raise ValueError(f'Malformed reviewer uncertainty: {key}')
            if kind == 'identified_sign':
                sign = segment.get('sign')
                if (not isinstance(sign, str) or not re.fullmatch(r'M\d{3}', sign)
                        or not 1 <= int(sign[1:]) <= 417
                        or token != ('*' if doubt else '')+sign
                        or segment.get('minimum_signs', 1) != 1
                        or segment.get('maximum_signs', 1) != 1):
                    raise ValueError(f'Inconsistent identified token/segment: {key}')
            elif kind == 'unknown_length_loss':
                if (token != 'LOSS' or segment.get('sign') is not None or doubt
                        or segment.get('minimum_signs') != 1
                        or 'maximum_signs' not in segment or segment['maximum_signs'] is not None):
                    raise ValueError(f'Inconsistent LOSS token/segment: {key}')
            elif kind in ('unidentified_visible_sign', 'visible_unidentified_glyph'):
                if (token not in ('UNKNOWN', ('*' if doubt else '')+'UNKNOWN')
                        or segment.get('sign') is not None
                        or segment.get('minimum_signs') != 1 or segment.get('maximum_signs') != 1):
                    raise ValueError(f'Inconsistent UNKNOWN token/segment: {key}')
            else:
                raise ValueError(f'Unsupported segment kind: {kind}')
            if token.startswith('*') or segment.get('source_doubt'):
                reasons.add('source_doubt')
            if token.lstrip('*') == 'UNKNOWN' or segment.get('kind') in ('unidentified_visible_sign', 'visible_unidentified_glyph'):
                reasons.add('UNKNOWN')
            if token == 'LOSS' or segment.get('kind') == 'unknown_length_loss':
                reasons.add('LOSS')
            if segment.get('reviewer_uncertainty'):
                reasons.add('reviewer_uncertainty')
        if reasons:
            excluded.append({'row_key': list(key), 'reasons': sorted(reasons)})
        else:
            selected.append({'row_key': list(key), 'sequence': tuple(tokens),
                             'source_pdf_page': row.get('source_pdf_page'),
                             'direction_code': row.get('direction_code')})
    return selected, excluded


def rectangle_summary(sequences, ending_length, witnesses=None):
    """Each pair of endings shared by s stems contributes choose(s, 2) cycles."""
    if ending_length not in (1, 2):
        raise ValueError('Ending length must be 1 or 2')
    edges = Counter((tuple(s[:-ending_length]), tuple(s[-ending_length:]))
                    for s in sequences if len(s) > ending_length)
    by_stem = defaultdict(set)
    for stem, ending in edges:
        by_stem[stem].add(ending)
    shared = defaultdict(list)
    for stem, endings in sorted(by_stem.items()):
        for pair in combinations(sorted(endings), 2):
            shared[pair].append(stem)
    pairs, cycles, row_witnesses = [], 0, 0
    for (a, b), stems in sorted(shared.items()):
        if len(stems) < 2:
            continue
        count = len(stems) * (len(stems)-1) // 2
        weighted = sum(edges[s, a]*edges[s, b]*edges[t, a]*edges[t, b]
                       for s, t in combinations(stems, 2))
        cycles += count
        row_witnesses += weighted
        pairs.append({'ending_pair': [list(a), list(b)],
                      'shared_stems': [list(s) for s in stems],
                      'four_cycles': count, 'row_witness_combinations': weighted})
    edge_output = []
    for (stem, ending), count in sorted(edges.items()):
        entry = {'stem': list(stem), 'ending': list(ending), 'row_count': count,
                 'unique_sequence_count': 1}
        if witnesses is not None:
            entry['row_keys'] = witnesses.get(stem+ending, [])
        edge_output.append(entry)
    return {'ending_length': ending_length, 'eligible_rows': sum(edges.values()),
            'unique_sequences': len(edges), 'stems': len(by_stem),
            'endings': len({e for _, e in edges}),
            'stems_with_multiple_endings': sum(len(e) >= 2 for e in by_stem.values()),
            'shared_ending_pairs': len(pairs), 'four_cycles': cycles,
            'row_witness_combinations': row_witnesses, 'pairs': pairs, 'edges': edge_output}


def shuffle_endings(sequences, ending_length, rng):
    """Keep each nonempty stem/slot; permute atomic endings within total length."""
    slots = [tuple(s) for s in sequences if len(s) > ending_length]
    strata = defaultdict(list)
    for i, seq in enumerate(slots):
        strata[len(seq)].append(i)
    output = slots.copy()
    for length in sorted(strata):
        indices = strata[length]
        blocks = [slots[i][-ending_length:] for i in indices]
        rng.shuffle(blocks)
        for i, block in zip(indices, blocks):
            output[i] = slots[i][:-ending_length]+block
    return output


def permutation_screen(sequences, ending_length, replicates, seed):
    if replicates < 1:
        raise ValueError('At least one replicate required')
    slots = sorted(tuple(s) for s in sequences if len(s) > ending_length)
    observed = rectangle_summary(slots, ending_length)['four_cycles']
    rng = random.Random(seed)
    scores = [rectangle_summary(shuffle_endings(slots, ending_length, rng), ending_length)['four_cycles']
              for _ in range(replicates)]
    strata = defaultdict(list)
    for seq in slots:
        strata[len(seq)].append(seq[-ending_length:])
    return {'seed': seed, 'replicates': replicates, 'observed_four_cycles': observed,
            'slots': len(slots),
            'slots_in_strata_with_multiple_endings': sum(len(x) for x in strata.values() if len(set(x)) > 1),
            'null_scores': scores, 'null_min': min(scores), 'null_max': max(scores),
            'null_mean': sum(scores)/replicates, 'sampled_score_is_constant': len(set(scores)) == 1,
            'raw_greater_or_equal_count': sum(x >= observed for x in scores),
            'raw_greater_or_equal_fraction': sum(x >= observed for x in scores)/replicates,
            'raw_strictly_greater_count': sum(x > observed for x in scores),
            'interpretation': 'Exploratory conditional exceedance; not a calibrated morphology test or multiple-testing-adjusted significance claim.'}


def illustrative_examples():
    grammar = [('ROOT_A', 'CASE_X'), ('ROOT_A', 'CASE_Y'),
               ('ROOT_B', 'CASE_X'), ('ROOT_B', 'CASE_Y')]
    labels = [('OFFICE_A', 'PRODUCT_X'), ('OFFICE_A', 'PRODUCT_Y'),
              ('OFFICE_B', 'PRODUCT_X'), ('OFFICE_B', 'PRODUCT_Y')]
    return {'invented_grammar': rectangle_summary(grammar, 1),
            'invented_fixed_labels': rectangle_summary(labels, 1),
            'interpretation': 'Both invented generative stories give the same rectangle. Tokens do not identify which story generated the data.'}


def analyze(corpus, replicates=999, seed=SEED):
    rows, excluded = clean_rows(corpus)
    sequences = [r['sequence'] for r in rows]
    witnesses = defaultdict(list)
    for row in rows:
        witnesses[row['sequence']].append(row['row_key'])
    lengths = {}
    for k in (1, 2):
        lengths[str(k)] = {
            'observed': rectangle_summary(sequences, k, witnesses),
            'row_slot_permutation': permutation_screen(sequences, k, replicates, seed+k),
            'unique_sequence_slot_permutation': permutation_screen(sorted(set(sequences)), k, replicates, seed+k)}
    return {'schema_version': 'kober-alternation-screen-1',
            'coverage': {'corpus_rows': len(corpus['rows']), 'clean_rows': len(rows),
                         'clean_unique_sequences': len(set(sequences)), 'excluded_rows': len(excluded),
                         'exclusion_reasons_overlapping': dict(Counter(reason for row in excluded for reason in row['reasons'])),
                         'source_pdf_pages': sorted({r['source_pdf_page'] for r in rows if r['source_pdf_page'] is not None}),
                         'clean_direction_codes': dict(sorted(Counter(r['direction_code'] for r in rows).items()))},
            'excluded': excluded, 'terminal_lengths': lengths, 'examples': illustrative_examples(),
            'assumptions': ['Sequences are preserved exactly in stored normalized RTL order; no extra reversal or concatenation of lines.',
                            'Terminal means last stored token(s), not an independently established linguistic suffix.',
                            'Units are whole printed lines without established word boundaries; this narrow screen does not implement linked penultimate/final alternations or infer syllabic grids.',
                            'Each fixed ending length leaves a nonempty exact stem; no sign-family pooling, internal deletions, or flexible boundaries.',
                            'Permutations preserve stem slots, full lengths and within-length ending-block multiplicities. They do not preserve stem-ending association, unique output count, archaeological dependencies or metadata strata.',
                            'The unique-sequence baseline starts with one slot per distinct input sequence; shuffled collisions may reduce distinct output count.',
                            'Row-witness combinations are combinatorial counts, not independent artifacts.'],
            'limitations': ['Small consecutive printed-page sample, not representative corpus evidence.',
                            'Doubt, UNKNOWN, LOSS and reviewer uncertainty are excluded, potentially selecting easier or shorter records.',
                            'A four-cycle is compatible with morphology, administrative label combinations, and other formulaic systems.',
                            'Two ending lengths and two permutation bases are exploratory comparisons; no corrected significance claim.',
                            'No observed rectangle is not evidence against language or morphology in this sparse exact-match sample.',
                            'Exact whole-line prefixes can miss changing stem forms and alternations within internal word boundaries.',
                            'Verification concerns M77 printed-transcription fidelity, not object-photograph identification or decipherment.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, default=ROOT/'data/processed/m77_verified/corpus_v3.json')
    parser.add_argument('--output', type=Path, default=ROOT/'results/kober_alternations_v3.json')
    parser.add_argument('--replicates', type=int, default=999)
    parser.add_argument('--seed', type=int, default=SEED)
    args = parser.parse_args()
    raw = args.corpus.read_bytes()
    result = analyze(json.loads(raw), args.replicates, args.seed)
    result['source'] = {'path': str(args.corpus.resolve().relative_to(ROOT)) if args.corpus.resolve().is_relative_to(ROOT) else str(args.corpus.resolve()),
                        'sha256': hashlib.sha256(raw).hexdigest()}
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'coverage': result['coverage'],
                      'four_cycles': {k: v['observed']['four_cycles'] for k, v in result['terminal_lengths'].items()}}))


if __name__ == '__main__':
    main()
