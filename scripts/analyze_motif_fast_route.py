"""Frozen motif-fast-route-v2: discovery and hash-verified fixed transfer.

No semantic fields are imported. This module has no import-time data reads.
CLI phases require an explicit output directory and never overwrite files.
Seeds: protocol seed + 0 discovery, + 1 transfer, + 2 Good/Fair sensitivity.
Permutation batching changes memory use, not the random draw sequence.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

import numpy as np

from common import ROOT
from prepare_corpora import parse_lipi

DEFAULT_PROTOCOL = ROOT / 'data/processed/motif_fast_route_protocol_v2.json'
PROTOCOL_SHA256 = '9a339d2bd761658d2ed56465cdc6efe635efe6432f13185f063a5dde64a8f1d3'
COLUMNS = ('id', 'cisi', 'site', 'type', 'condition', 'complete', 'dir.',
           'class', 'signs', 'text', 'symbol')
PHASE_OFFSETS = {'discovery': 0, 'transfer': 1, 'good_fair': 2}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_allowed_rows(path, columns=COLUMNS):
    """Select only configured columns at ingestion; never retain other fields."""
    if tuple(columns) != COLUMNS:
        raise ValueError('Unexpected protocol columns')
    with Path(path).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.reader(stream)
        header = next(reader)
        if any(header.count(c) != 1 for c in columns):
            raise ValueError('Missing or duplicate configured column')
        indices = [header.index(c) for c in columns]
        for number, values in enumerate(reader, 2):
            if len(values) != len(header):
                raise ValueError(f'CSV column count mismatch at row {number}')
            yield {column: values[index] for column, index in zip(columns, indices)}


def parse_row(row):
    copy = {c: row[c] for c in COLUMNS}
    if (copy['dir.'].strip().upper() == 'NR'
            and re.fullmatch(r'\+\d{3}\+', copy['text'])):
        copy['dir.'] = 'R/L'
    return parse_lipi(copy)


def prepare_artifacts(rows, absent_labels):
    """Exclude entire in-scope artifact groups before any quality filtering."""
    groups = defaultdict(list)
    absent = set(absent_labels)
    for row in rows:
        if row['type'] != 'SEAL:S':
            continue
        cisi = row['cisi'].strip()
        key = cisi if cisi not in absent else 'lipi_id:' + row['id'].split('.')[0]
        groups[key].append(row)
    artifacts, ledger = [], []
    for key, members in sorted(groups.items()):
        reasons, sequences = set(), set()
        sites, motifs = set(), set()
        for row in members:
            seq, invalid = parse_row(row)
            reasons.update(invalid)
            sequences.add(tuple(seq))
            sites.add(row['site'])
            motifs.add(row['symbol'])
            if row['symbol'].strip() in absent:
                reasons.add('absent_motif')
        if len(sites) != 1:
            reasons.add('inconsistent_site')
        if len(motifs) != 1:
            reasons.add('inconsistent_raw_motif')
        if len(sequences) != 1:
            reasons.add('inconsistent_complete_sequence')
        ledger.append({'artifact': key, 'in_scope_rows': len(members),
                       'retained': not reasons, 'reasons': sorted(reasons)})
        if not reasons:
            artifacts.append({'artifact': key, 'site': next(iter(sites)),
                              'motif': next(iter(motifs)),
                              'sequence': next(iter(sequences)),
                              'good_fair': all(r['condition'] in ('Good', 'Fair')
                                               for r in members)})
    return artifacts, ledger


def sequence_families(artifacts, site, good_fair=False, excluded_sequences=()):
    excluded = {tuple(s) for s in excluded_sequences}
    grouped = defaultdict(dict)
    for artifact in artifacts:
        seq = tuple(artifact['sequence'])
        if (artifact['site'] != site or seq in excluded
                or (good_fair and not artifact['good_fair'])):
            continue
        # Each eligible artifact contributes exactly one label, regardless of
        # duplicate export rows; a family contributes total weight one.
        previous = grouped[seq].get(artifact['artifact'])
        if previous is not None and previous != artifact['motif']:
            raise ValueError('Conflicting artifact passed preparation')
        grouped[seq][artifact['artifact']] = artifact['motif']
    families = []
    for seq, members in sorted(grouped.items()):
        counts = Counter(members.values())
        families.append({'sequence': list(seq), 'length': len(seq),
                         'artifact_count': len(members),
                         'motifs': {k: v / len(members) for k, v in sorted(counts.items())}})
    return families


def make_design(families, signs=None, motifs=None):
    signs = sorted({s for r in families for s in r['sequence']}) if signs is None else list(signs)
    motifs = sorted({s for r in families for s in r['motifs']}) if motifs is None else list(motifs)
    if any(not re.fullmatch(r'W\d{3}', s) for s in signs):
        raise ValueError('Only native W sign IDs are permitted')
    f = np.array([[s in r['sequence'] for s in signs] for r in families], dtype=float)
    y = np.array([[r['motifs'].get(s, 0.) for s in motifs] for r in families], dtype=float)
    f = f.reshape(len(families), len(signs))
    y = y.reshape(len(families), len(motifs))
    lengths = np.array([r['length'] for r in families], dtype=int)
    strata = [np.flatnonzero(lengths == length) for length in sorted(set(lengths))]
    covariance, variance = moments(f, y, strata)
    return {'signs': signs, 'motifs': motifs, 'f': f, 'y': y, 'strata': strata,
            'lengths': lengths, 'covariance': covariance, 'variance': variance,
            'sign_support': f.sum(axis=0).astype(int),
            'motif_support': (y > 0).sum(axis=0).astype(int)}


def center_stratum(y):
    """Center while preserving exact zero variance of identical input values.

    A floating mean of repeated 1/3 values need not equal the input value.
    Detect constancy before centering so rounding cannot manufacture support.
    """
    if not len(y):
        return y.copy()
    constant = np.all(y == y[0], axis=0)
    centered = y - y.mean(axis=0)
    centered[:, constant] = 0.
    return centered


def moments(f, y, strata):
    """Exact conditional covariance numerator and permutation variance."""
    covariance = np.zeros((f.shape[1], y.shape[1]))
    variance = np.zeros_like(covariance)
    for indices in strata:
        n = len(indices)
        if n < 2:
            continue
        x, z = f[indices], y[indices]
        centered = center_stratum(z)
        nf = x.sum(axis=0)
        covariance += x.T @ centered
        variance += np.outer(nf * (n - nf) / (n * (n - 1)),
                             (centered ** 2).sum(axis=0))
    return covariance, variance


def eligible_pairs(design, min_support=10):
    return ((design['sign_support'][:, None] >= min_support)
            & (design['motif_support'][None, :] >= min_support)
            & (design['variance'] > 0))


def shuffle_indices(strata, n, rng):
    permutation = np.arange(n)
    for indices in strata:
        if len(indices) > 1:
            permutation[indices] = rng.permutation(indices)
    return permutation


def permutation_z(design, pairs, replicates, seed, batch_size=32):
    """Yield batches of Z for fixed pairs, shuffling whole motif vectors.

    One centered motif matrix is permuted across families within each length.
    Flattening only fixed pair columns avoids a B x signs x motifs output.
    """
    if replicates < 1 or batch_size < 1:
        raise ValueError('replicates and batch_size must be positive')
    pairs = list(pairs)
    if not pairs:
        return
    si = np.array([a for a, _ in pairs], dtype=int)
    mi = np.array([b for _, b in pairs], dtype=int)
    variance = design['variance'][si, mi]
    if np.any(variance <= 0):
        raise ValueError('Cannot permute zero-variance pair')
    active_s, local_s = np.unique(si, return_inverse=True)
    active_m, local_m = np.unique(mi, return_inverse=True)
    x = design['f'][:, active_s]
    centered = design['y'][:, active_m].copy()
    for indices in design['strata']:
        centered[indices] = center_stratum(centered[indices])
    rng = np.random.default_rng(seed)
    scale = np.sqrt(variance)
    # Matrix multiplication reuses a sign across motifs; eligible-pair slicing
    # occurs after each small batch rather than materializing all replicates.
    for start in range(0, replicates, batch_size):
        indices = np.array([shuffle_indices(design['strata'], len(centered), rng)
                            for _ in range(min(batch_size, replicates - start))])
        covariance = np.einsum('ns,bnm->bsm', x, centered[indices], optimize=True)
        yield covariance[:, local_s, local_m] / scale


def greater_equal_with_roundoff(values, observed):
    """Count mathematical ties despite float64 summation order differences.

    The frozen absolute numerical allowance is 1e-12 in Z units.
    This is a rounding tolerance, not a fitted statistical decision threshold.
    """
    return np.asarray(values) >= np.asarray(observed) - 1e-12


def holm(p_values):
    p = np.asarray(p_values, dtype=float)
    if np.any(~np.isfinite(p)) or np.any((p < 0) | (p > 1)):
        raise ValueError('Invalid p value')
    order = np.argsort(p, kind='stable')
    adjusted = np.empty(len(p))
    if len(p):
        adjusted[order] = np.minimum(1., np.maximum.accumulate(p[order] * np.arange(len(p), 0, -1)))
    return adjusted.tolist()


def run_discovery(families, replicates, seed):
    design = make_design(families)
    pairs = list(zip(*np.where(eligible_pairs(design))))
    if not pairs:
        return {'status': 'no_eligible_pairs', 'families': len(families),
                'eligible_pairs': [], 'null_max_positive_z': [],
                'global_p': None, 'candidates': []}
    si, mi = np.array(pairs).T
    observed = design['covariance'][si, mi] / np.sqrt(design['variance'][si, mi])
    maxima = np.concatenate([np.maximum(0., batch.max(axis=1))
                            for batch in permutation_z(design, pairs, replicates, seed)])
    records = []
    for k, (a, b) in enumerate(pairs):
        records.append({'sign': design['signs'][a], 'raw_motif': design['motifs'][b],
                        'z': float(observed[k]),
                        'maxT_p': float((1 + np.count_nonzero(greater_equal_with_roundoff(
                            maxima, observed[k]))) / (replicates + 1)),
                        'sign_support': int(design['sign_support'][a]),
                        'motif_positive_support': int(design['motif_support'][b]),
                        'conditional_variance': float(design['variance'][a, b])})
    candidates = sorted((r for r in records if r['z'] > 0 and r['maxT_p'] <= .01),
                        key=lambda r: (-r['z'], r['sign'], r['raw_motif']))[:5]
    observed_maximum = max(0., float(observed.max()))
    return {'status': 'candidates_frozen' if candidates else 'no_selected_candidates',
            'families': len(families), 'eligible_pairs': records,
            'observed_max_positive_z': observed_maximum,
            'null_max_positive_z': maxima.tolist(),
            'global_p': float((1 + np.count_nonzero(greater_equal_with_roundoff(
                maxima, observed_maximum))) / (replicates + 1)),
            'candidates': candidates}


def run_fixed_transfer(families, candidates, replicates, seed):
    signs = sorted({c['sign'] for c in candidates})
    motifs = sorted({c['raw_motif'] for c in candidates})
    design = make_design(families, signs, motifs)
    records, valid_pairs, record_indices = [], [], []
    for candidate in candidates:
        a, b = signs.index(candidate['sign']), motifs.index(candidate['raw_motif'])
        valid = bool(eligible_pairs(design)[a, b])
        variance = float(design['variance'][a, b])
        records.append({'sign': candidate['sign'], 'raw_motif': candidate['raw_motif'],
                        'status': 'testable' if valid else 'insufficient_configured_support',
                        'sign_support': int(design['sign_support'][a]),
                        'motif_positive_support': int(design['motif_support'][b]),
                        'conditional_variance': variance,
                        'z': float(design['covariance'][a, b] / np.sqrt(variance)) if valid else None,
                        'one_sided_p': 1., 'null_exceedances': None})
        if valid:
            valid_pairs.append((a, b)); record_indices.append(len(records) - 1)
    if valid_pairs:
        observed = np.array([records[i]['z'] for i in record_indices])
        exceedances = np.zeros(len(valid_pairs), dtype=int)
        for batch in permutation_z(design, valid_pairs, replicates, seed):
            exceedances += greater_equal_with_roundoff(batch, observed).sum(axis=0)
        for j, i in enumerate(record_indices):
            records[i]['null_exceedances'] = int(exceedances[j])
            records[i]['one_sided_p'] = float((1 + exceedances[j]) / (replicates + 1))
    for row, p in zip(records, holm([r['one_sided_p'] for r in records])):
        row['holm_p'] = p
        row['passes_positive_holm_005'] = bool(row['z'] is not None and row['z'] > 0 and p <= .05)
    return {'families': len(families), 'tested_candidates': len(valid_pairs),
            'holm_family_size': len(candidates), 'candidates': records,
            'status': ('no_selected_candidates' if not candidates else
                       'insufficient_configured_support' if not valid_pairs else 'evaluated')}


def load_protocol(path):
    if digest(path) != PROTOCOL_SHA256:
        raise ValueError('Protocol bytes differ from the frozen v2 specification')
    protocol = json.loads(Path(path).read_text())
    if (protocol['id'] != 'motif-fast-route-v2' or tuple(protocol['columns']) != COLUMNS
            or protocol['replicates'] != 9999 or protocol['seed'] != 20261011):
        raise ValueError('Unsupported frozen protocol')
    source = ROOT / protocol['source']['path']
    if digest(source) != protocol['source']['sha256']:
        raise ValueError('Source hash does not match frozen protocol')
    pins = {'protocol': {'path': str(path), 'sha256': digest(path)},
            'source': protocol['source'],
            'implementation': {'path': 'scripts/analyze_motif_fast_route.py',
                               'sha256': digest(__file__)},
            'parser': {'path': 'scripts/prepare_corpora.py',
                       'sha256': digest(ROOT / 'scripts/prepare_corpora.py')}}
    return protocol, source, pins


def write_new(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=('discovery', 'transfer'))
    parser.add_argument('--protocol', type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--candidates', type=Path)
    parser.add_argument('--candidate-sha256')
    args = parser.parse_args()
    if args.phase == 'transfer' and (not args.candidates or not args.candidate_sha256):
        parser.error('transfer requires --candidates and --candidate-sha256')
    if args.phase == 'discovery' and (args.candidates or args.candidate_sha256):
        parser.error('discovery cannot accept candidates')
    names = ['candidates.json', 'discovery.json'] if args.phase == 'discovery' else ['transfer.json']
    if any((args.output_dir / name).exists() for name in names):
        raise ValueError('Refusing to overwrite a frozen phase output')
    protocol, source, pins = load_protocol(args.protocol)
    artifacts, ledger = prepare_artifacts(read_allowed_rows(source, protocol['columns']), protocol['absent_labels'])
    discovery_families = sequence_families(artifacts, protocol['discovery_site'])
    metadata = {'protocol_id': protocol['id'], 'pins': pins,
                'replicates': protocol['replicates'], 'base_seed': protocol['seed'],
                'seed_offsets': PHASE_OFFSETS,
                'numerical_tie_allowance': 'absolute 1e-12 in Z units for >= comparisons',
                'quality_rule': 'Every in-scope row of a fully eligible artifact must be Good or Fair; regroup families afterward.',
                'group_ledger': ledger,
                'limitations': protocol['limitations'], 'success_scope': protocol['success_scope']}
    if args.phase == 'discovery':
        result = run_discovery(discovery_families, protocol['replicates'], protocol['seed'])
        frozen = {'schema_version': 'motif-fast-route-candidates-v2', 'protocol_id': protocol['id'],
                  'pins': pins, 'seed': protocol['seed'], 'replicates': protocol['replicates'],
                  'candidates': result['candidates'],
                  'discovery_sequences': [r['sequence'] for r in discovery_families]}
        args.output_dir.mkdir(parents=True, exist_ok=True)
        candidate_path = args.output_dir / 'candidates.json'
        write_new(candidate_path, frozen)
        # Freeze and hash selection before a later, explicitly separate phase.
        result['candidate_file'] = {'path': str(candidate_path), 'sha256': digest(candidate_path)}
        write_new(args.output_dir / 'discovery.json', {**metadata, **result})
        print(json.dumps({'phase': 'discovery', 'families': len(discovery_families),
                          'eligible_pairs': len(result['eligible_pairs']),
                          'selected_candidates': len(result['candidates']),
                          'candidate_file': result['candidate_file'], 'status': result['status']}))
    else:
        if digest(args.candidates) != args.candidate_sha256:
            raise ValueError('Candidate freeze hash mismatch')
        frozen = json.loads(args.candidates.read_text())
        if (frozen.get('schema_version') != 'motif-fast-route-candidates-v2'
                or frozen.get('protocol_id') != protocol['id'] or frozen.get('pins') != pins
                or frozen.get('seed') != protocol['seed'] or frozen.get('replicates') != protocol['replicates']):
            raise ValueError('Candidate provenance differs from current frozen inputs or code')
        seen = [r['sequence'] for r in discovery_families]
        if frozen['discovery_sequences'] != seen:
            raise ValueError('Discovery sequence set changed')
        candidates = frozen['candidates']
        if len(candidates) > 5 or len({(c['sign'], c['raw_motif']) for c in candidates}) != len(candidates):
            raise ValueError('Invalid fixed candidate set')
        results = {}
        for phase, quality in [('transfer', False), ('good_fair', True)]:
            families = sequence_families(artifacts, protocol['transfer_site'], quality, seen)
            results[phase] = run_fixed_transfer(families, candidates, protocol['replicates'],
                                                protocol['seed'] + PHASE_OFFSETS[phase])
            results[phase]['sequence_set_sha256'] = hashlib.sha256(json.dumps(
                [r['sequence'] for r in families], separators=(',', ':')).encode()).hexdigest()
        results['primary_supported_pairs'] = [
            {'sign': r['sign'], 'raw_motif': r['raw_motif']}
            for r in results['transfer']['candidates'] if r['passes_positive_holm_005']]
        results['decision_basis'] = 'All-condition transfer only; quality sensitivity cannot rescue failure.'
        args.output_dir.mkdir(parents=True, exist_ok=True)
        write_new(args.output_dir / 'transfer.json', {**metadata, **results,
                  'candidate_file': {'path': str(args.candidates), 'sha256': args.candidate_sha256},
                  'excluded_exact_discovery_sequences': len(seen)})
        print(json.dumps({'phase': 'transfer', 'primary_supported_pairs': results['primary_supported_pairs'],
                          **{k: {a: results[k][a] for a in ('families', 'tested_candidates', 'status')}
                             for k in ('transfer', 'good_fair')}}))


if __name__ == '__main__':
    main()
