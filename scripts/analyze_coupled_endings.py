"""Frozen coupled-endings-v2; native source order, no inferred word boundaries.

Imports never read data. All real-data execution requires the explicit CLI.
Atomic endings are shuffled over fixed slots, rejecting duplicate resulting edges.
The null maximum includes every pair formed in that arrangement, not only the
original pairs. Calibration assumes joint exchangeability, not partial-null FWER.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
from itertools import combinations
import json
import platform
from pathlib import Path

import numpy as np

from common import ROOT
from prepare_corpora import parse_lipi

DEFAULT_PROTOCOL = ROOT / 'data/processed/coupled_endings_protocol_v2.json'
PROTOCOL_SHA256 = '6715ace6c35f320279dd869998aa9425d9d8a58216b3ff1b3e7e642e1356cfbd'
COLUMNS = ('id', 'cisi', 'site', 'type', 'condition', 'complete', 'dir.',
           'class', 'signs', 'text')
ABSENT = {'', '-', '--', '?', 'None', 'Unknown'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_allowed_rows(path):
    """Decode only the whitelist; optional omitted suffix fields are inert."""
    with Path(path).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.reader(stream)
        header = next(reader)
        if any(header.count(c) != 1 for c in COLUMNS):
            raise ValueError('Missing or duplicate required column')
        positions = [header.index(c) for c in COLUMNS]
        for number, values in enumerate(reader, 2):
            if len(values) <= max(positions) or len(values) > len(header):
                raise ValueError(f'CSV required-column count mismatch at row {number}')
            yield {c: values[i] for c, i in zip(COLUMNS, positions)}


def prepare_artifacts(rows):
    """Validate all in-scope artifact rows across sites before selecting MD."""
    groups, row_ledger = defaultdict(list), []
    for number, original in enumerate(rows, 2):
        row = {c: original[c] for c in COLUMNS}
        scoped = row['type'] == 'SEAL:S'
        cisi = row['cisi'].strip()
        key = cisi if cisi not in ABSENT else 'lipi_id:' + row['id'].split('.')[0]
        sequence, invalid = parse_lipi(row) if scoped else ([], [])
        entry = {'source_row': number, 'fields': row, 'artifact': key,
                 'in_scope': scoped, 'sequence': sequence, 'parser_reasons': invalid}
        row_ledger.append(entry)
        if scoped:
            groups[key].append(entry)
    artifacts, ledger = [], []
    for key, members in sorted(groups.items()):
        reasons = {r for m in members for r in m['parser_reasons']}
        sequences = {tuple(m['sequence']) for m in members}
        sites = {m['fields']['site'] for m in members}
        if len(sequences) != 1:
            reasons.add('inconsistent_complete_sequence')
        if len(sites) != 1:
            reasons.add('inconsistent_site')
        entry = {'artifact': key, 'source_rows': [m['source_row'] for m in members],
                 'reasons': sorted(reasons), 'valid_artifact': not reasons,
                 'selected': False}
        if not reasons:
            sequence, site = next(iter(sequences)), next(iter(sites))
            entry.update(sequence=sequence, site=site)
            if site != 'Mohenjo-daro':
                entry['selection_reason'] = 'site_not_Mohenjo-daro'
            elif len(sequence) < 3:
                entry['selection_reason'] = 'sequence_shorter_than_3'
            else:
                entry['selected'] = True
                artifacts.append({'artifact': key, 'sequence': sequence,
                                  'source_rows': entry['source_rows']})
        ledger.append(entry)
    return artifacts, ledger, row_ledger


def sequence_families(artifacts):
    grouped = defaultdict(list)
    for artifact in artifacts:
        grouped[tuple(artifact['sequence'])].append(artifact)
    return [{'sequence': sequence, 'length': len(sequence),
             'stem': sequence[:-2], 'ending': sequence[-2:],
             'witnesses': sorted(members, key=lambda a: a['artifact'])}
            for sequence, members in sorted(grouped.items())]


def coupled(a, b):
    return a[0] != b[0] and a[1] != b[1]


def pair_support(stems, endings):
    """Return support and every distinct supporting stem, collapsing collisions."""
    if len(stems) != len(endings):
        raise ValueError('Stem and ending slot counts differ')
    groups = defaultdict(set)
    for stem, ending in zip(stems, endings):
        if not stem or len(ending) != 2:
            raise ValueError('Require nonempty stem and atomic two-sign ending')
        groups[tuple(stem)].add(tuple(ending))
    witnesses = defaultdict(list)
    for stem, labels in sorted(groups.items()):
        for a, b in combinations(sorted(labels), 2):
            if coupled(a, b):
                witnesses[(a, b)].append(stem)
    return {pair: len(stems) for pair, stems in witnesses.items()}, dict(witnesses)


def support_upper_bounds(stems, endings):
    """Collision-relaxed upper bound on simple-edge support, NOT attainability.

At length l, each supported stem consumes one A slot and one B slot and must
have >=2 slots. The bound is exact if collisions are allowed. Requiring simple
edges can strictly reduce the maximum: residual labels must also fit uniquely.
A bound below two proves insufficient support; a larger bound proves no power.
"""
    if len(stems) != len(endings):
        raise ValueError('Stem and ending slot counts differ')
    stem_counts, ending_counts = defaultdict(Counter), defaultdict(Counter)
    for stem, ending in zip(stems, endings):
        if not stem or len(ending) != 2:
            raise ValueError('Require nonempty stem and atomic two-sign ending')
        length = len(stem) + 2
        stem_counts[length][tuple(stem)] += 1
        ending_counts[length][tuple(ending)] += 1
    repeatable = {length: sum(c >= 2 for c in counts.values())
                  for length, counts in stem_counts.items()}
    labels = sorted({tuple(e) for e in endings})
    result = []
    for a, b in combinations(labels, 2):
        if not coupled(a, b):
            continue
        by_length = [{'length': length, 'stems_with_two_slots': repeatable[length],
                      'ending_a_slots': counts[a], 'ending_b_slots': counts[b],
                      'upper_bound': min(repeatable[length], counts[a], counts[b])}
                     for length, counts in sorted(ending_counts.items())]
        result.append({'endings': [a, b], 'upper_bound': sum(r['upper_bound'] for r in by_length),
                       'by_length': by_length})
    return result


def length_strata(stems):
    groups = defaultdict(list)
    for i, stem in enumerate(stems):
        groups[len(stem) + 2].append(i)
    return [np.asarray(indices, dtype=int) for _, indices in sorted(groups.items())]


def shuffle_endings(endings, strata, rng):
    result = list(endings)
    for indices in strata:
        order = rng.permutation(indices)
        for target, source in zip(indices, order):
            result[int(target)] = endings[int(source)]
    return result


def is_simple(stems, endings):
    return len(set(zip(map(tuple, stems), map(tuple, endings)))) == len(stems)


def sample_simple_stratum(stems, endings, replicates, rng, proposal_cap):
    """Independent rejection draws, uniform conditional on the simple graph.

Each accepted simple graph has product(stem_degree!) labeled-slot realizations,
constant for fixed degrees. Uniform slot permutations therefore induce uniform
simple graphs with the observed degrees and ending frequencies. The original
simple graph witnesses nonempty support, but acceptance may still be very low.
"""
    if replicates < 1 or proposal_cap < 1:
        raise ValueError('Replicate and proposal caps must be positive')
    if len(stems) != len(endings) or not is_simple(stems, endings):
        raise ValueError('Conditional-null input must have unique stem-ending edges')
    labels = sorted(set(map(tuple, endings)))
    label_ids = {label: i for i, label in enumerate(labels)}
    encoded = np.asarray([label_ids[tuple(e)] for e in endings], dtype=np.int32)
    groups = defaultdict(list)
    for i, stem in enumerate(stems):
        groups[tuple(stem)].append(i)
    # Singleton stems cannot collide. Vectorize all potential repeated-edge
    # equalities once; each proposal then needs a single array comparison.
    comparisons = [pair for indices in groups.values() for pair in combinations(indices, 2)]
    left = np.asarray([p[0] for p in comparisons], dtype=int)
    right = np.asarray([p[1] for p in comparisons], dtype=int)
    accepted = np.empty((replicates, len(stems)), dtype=np.int32)
    proposals = count = 0
    while count < replicates and proposals < proposal_cap:
        proposed = rng.permutation(encoded)
        proposals += 1
        if len(left) and np.any(proposed[left] == proposed[right]):
            continue
        accepted[count] = proposed
        count += 1
    diagnostics = {'length': len(stems[0]) + 2 if stems else None,
                   'slots': len(stems), 'proposals': proposals, 'accepted': count,
                   'rejected': proposals - count, 'proposal_cap': proposal_cap,
                   'acceptance_rate': count / proposals,
                   'complete': count == replicates}
    return accepted[:count], labels, diagnostics


def permutation_maxima(stems, endings, replicates, seed, proposal_cap=1000000):
    if len(stems) != len(endings) or not is_simple(stems, endings):
        raise ValueError('Conditional-null input must have unique stem-ending edges')
    strata, rng = length_strata(stems), np.random.default_rng(seed)
    draws, diagnostics = [], []
    for indices in strata:
        accepted, labels, info = sample_simple_stratum(
            [stems[i] for i in indices], [endings[i] for i in indices],
            replicates, rng, proposal_cap)
        diagnostics.append(info)
        if not info['complete']:
            return {'status': 'computationally_unavailable', 'maxima': [],
                    'strata': diagnostics}
        draws.append((indices, accepted, labels))
    maxima = []
    for draw in range(replicates):
        shuffled = list(endings)
        for indices, accepted, labels in draws:
            for slot, code in zip(indices, accepted[draw]):
                shuffled[int(slot)] = labels[int(code)]
        counts, _ = pair_support(stems, shuffled)
        maxima.append(max(counts.values(), default=0))
    return {'status': 'completed', 'maxima': maxima, 'strata': diagnostics}


def analyze_families(families, replicates=9999, seed=20261011, proposal_cap=1000000):
    stems = [tuple(f['stem']) for f in families]
    endings = [tuple(f['ending']) for f in families]
    if not is_simple(stems, endings):
        raise ValueError('Analysis families must be unique complete sequences')
    support, witnesses = pair_support(stems, endings)
    bounds = support_upper_bounds(stems, endings)
    observed = [{'endings': pair, 'support': count, 'supporting_stems': witnesses[pair],
                 'maxT_p': None}
                for pair, count in sorted(support.items(), key=lambda p: (-p[1], p[0]))]
    result = {'status': None, 'families': len(families), 'seed': seed,
              'configured_replicates': replicates, 'completed_replicates': 0,
              'observed_maximum': max(support.values(), default=0), 'global_p': None,
              'sampled_constant_null': None, 'observed_pairs': observed,
              'collision_relaxed_support_upper_bounds': bounds,
              'proposal_cap_per_stratum': proposal_cap, 'sampling_diagnostics': [],
              'null_maxima': [], 'candidates': [],
              'caution': 'Joint-exchangeability global calibration only. A sampled constant null is not proof of a constant population null or a power conclusion.',
              'interpretation_limit': 'Intact-ending shuffling conditions on the association between the last two signs. It tests shared attachment of those ending blocks across stems, not independent change versus coupling, word endings, inflection, or a syllabic grid.'}
    if max((r['upper_bound'] for r in bounds), default=0) < 2:
        result['status'] = 'insufficient_support'
        return result
    if result['observed_maximum'] < 2:
        result['status'] = 'no_observed_support_at_least_2'
        return result
    sampled = permutation_maxima(stems, endings, replicates, seed, proposal_cap)
    result['sampling_diagnostics'] = sampled['strata']
    if sampled['status'] != 'completed':
        result['status'] = 'computationally_unavailable'
        return result
    maxima = sampled['maxima']
    result.update(status='completed', completed_replicates=replicates, null_maxima=maxima,
                  sampled_constant_null=len(set(maxima)) == 1,
                  global_p=(1 + sum(v >= result['observed_maximum'] for v in maxima)) / (replicates + 1))
    for record in observed:
        record['maxT_p'] = (1 + sum(v >= record['support'] for v in maxima)) / (replicates + 1)
    result['candidates'] = [r for r in observed if r['support'] >= 2 and r['maxT_p'] <= .01][:5]
    return result


def write_new(path, value):
    with Path(path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, sort_keys=True, ensure_ascii=False)
        stream.write('\n')


def run(protocol_path, output_dir):
    protocol_path, output_dir = Path(protocol_path), Path(output_dir)
    if digest(protocol_path) != PROTOCOL_SHA256:
        raise ValueError('Frozen protocol hash mismatch')
    protocol = json.loads(protocol_path.read_text())
    if tuple(protocol['allowed_columns']) != COLUMNS:
        raise ValueError('Whitelist mismatch')
    source = ROOT / protocol['source']['path']
    if digest(source) != protocol['source']['sha256']:
        raise ValueError('Source hash mismatch')
    if output_dir.exists():
        raise FileExistsError('Refuse to overwrite an existing output directory')
    artifacts, ledger, row_ledger = prepare_artifacts(read_allowed_rows(source))
    families = sequence_families(artifacts)
    result = analyze_families(families, protocol['replicates'], protocol['seed'],
                              protocol['proposal_cap_per_stratum'])
    pins = {'protocol': {'path': str(protocol_path), 'sha256': digest(protocol_path)},
            'source': protocol['source'],
            'implementation': {'path': 'scripts/analyze_coupled_endings.py', 'sha256': digest(__file__)},
            'parser': {'path': 'scripts/prepare_corpora.py', 'sha256': digest(ROOT / 'scripts/prepare_corpora.py')},
            'runtime': {'numpy': np.__version__, 'python': platform.python_version()}}
    output_dir.mkdir(parents=True, exist_ok=False)
    outputs = {'pins.json': pins, 'row_ledger.json': row_ledger,
               'artifact_ledger.json': ledger, 'sequence_families.json': families,
               'analysis.json': result, 'candidates.json': result['candidates'],
               'stop.json': {'status': result['status'], 'selected': len(result['candidates']),
                             'next_action': ('primary_check_fixed_candidates' if result['candidates'] else 'stop_no_primary_followup')}}
    for name, value in outputs.items():
        write_new(output_dir / name, value)
    write_new(output_dir / 'output_manifest.json', {name: digest(output_dir / name) for name in outputs})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--protocol', type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.protocol, args.output_dir)
    print(json.dumps({'status': result['status'], 'selected': len(result['candidates']),
                      'families': result['families'], 'global_p': result['global_p']}))


if __name__ == '__main__':
    main()
