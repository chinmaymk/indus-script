"""Exploratory variant-context prediction for every source-asserted sign family.

No family is promoted to an allograph set, and no semantic values are assigned.
Connected artifact/collapsed-text grouping prevents a close variant of a training
inscription from being scored as a new held-out example.
"""
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
import random
from common import ROOT, read_jsonl, sha256, write_csv, write_json
from analyze_sequences import slot

SEED = 20260922


def family_inventory(features):
    families = {r['id']: sorted(set(r['wells_graphemes'])) for r in features
                if len(set(r['wells_graphemes'])) >= 2}
    owner = {}
    for family, signs in families.items():
        for sign in signs:
            if sign in owner:
                raise ValueError(f'Ambiguous family membership: {sign}')
            owner[sign] = family
    return families, owner


def canonical(sequence, owner):
    return tuple('F:'+owner[x] if x in owner else x for x in sequence)


def grouped_units(records, owner):
    dedup = {}
    for r in records:
        key = (r['artifact'], tuple(r['sequence']), r['site'], r['type'])
        if key not in dedup:
            dedup[key] = {'artifact': r['artifact'], 'sequence': tuple(r['sequence']),
                          'site': r['site'], 'type': r['type'], 'source_ids': []}
        dedup[key]['source_ids'].append(r['id'])
    units = [dict(r, source_ids=sorted(set(r['source_ids']))) for _,r in sorted(dedup.items())]
    parent = list(range(len(units)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    seen = {}
    for i, r in enumerate(units):
        for key in [('artifact', r['artifact']), ('collapsed_text', canonical(r['sequence'], owner))]:
            if key in seen:
                parent[find(i)] = find(seen[key])
            seen[key] = i
    components = defaultdict(list)
    for i in range(len(units)):
        components[find(i)].append(i)
    for indices in components.values():
        texts = sorted({canonical(units[i]['sequence'], owner) for i in indices})
        group = hashlib.sha256(json.dumps(texts).encode()).hexdigest()
        for i in indices:
            units[i]['group'] = group
            units[i]['fold'] = int(group[:12], 16) % 5
    return units


def tokens_from_units(units, owner):
    tokens = []
    for r in units:
        sequence = r['sequence']
        normalized = canonical(sequence, owner)
        for i, sign in enumerate(sequence):
            if sign not in owner:
                continue
            tokens.append({'family': owner[sign], 'sign': sign, 'group': r['group'], 'fold': r['fold'],
                'artifact': r['artifact'], 'ids': ';'.join(r['source_ids']), 'position': i,
                'sequence': ' '.join(sequence),
                'metadata': (r['site'], r['type'], len(sequence), slot(i, len(sequence))),
                'neighbors': (normalized[i-1] if i else '<BOS>',
                              normalized[i+1] if i+1 < len(sequence) else '<EOS>')})
    return tokens


class VariantModel:
    def __init__(self, train, families, strength):
        self.families, self.strength = families, strength
        self.frequency = defaultdict(Counter)
        self.metadata = defaultdict(Counter)
        self.neighbors = defaultdict(Counter)
        for t in train:
            self.frequency[t['family']][t['sign']] += 1
            self.metadata[t['family'], t['metadata']][t['sign']] += 1
            self.neighbors[t['family'], t['neighbors']][t['sign']] += 1

    def probabilities(self, token):
        f, x = token['family'], token['sign']
        c = self.frequency[f]
        p0 = (c[x]+.5)/(sum(c.values())+.5*len(self.families[f]))
        m = self.metadata.get((f, token['metadata']), {})
        p1 = (m.get(x, 0)+self.strength*p0)/(sum(m.values())+self.strength)
        n = self.neighbors.get((f, token['neighbors']), {})
        p2 = (n.get(x, 0)+self.strength*p1)/(sum(n.values())+self.strength)
        return p0, p1, p2


def descriptive_evidence(units, owner):
    frames = defaultdict(lambda: defaultdict(set))
    cooccurrences = defaultdict(list)
    for sequence in sorted({r['sequence'] for r in units}):
        present = defaultdict(set)
        for i, sign in enumerate(sequence):
            if sign in owner:
                f = owner[sign]
                present[f].add(sign)
                frame = sequence[:i] + ('?',) + sequence[i+1:]
                frames[f][frame].add(sign)
        for f, signs in present.items():
            if len(signs) >= 2:
                cooccurrences[f].append({'sequence': ' '.join(sequence), 'variants': sorted(signs)})
    result = {}
    for f in set(owner.values()):
        shared = [{'frame': ' '.join(frame), 'variants': sorted(signs)}
                  for frame,signs in sorted(frames[f].items()) if len(signs) >= 2]
        result[f] = {'exact_substitution_frames': shared,
                     'texts_with_distinct_members': cooccurrences[f]}
    return result


def aggregate_bootstrap(scored, supported, strength):
    selected = [r for r in scored if r['family'] in supported and r['strength'] == strength]
    groups = defaultdict(lambda: [0, 0.0])
    for r in selected:
        g = groups[r['group']]
        g[0] += 1
        g[1] += r['metadata_bits']-r['neighbor_bits']
    values = list(groups.values())
    rng = random.Random(SEED)
    draws = []
    for _ in range(1000):
        sampled = rng.choices(values, k=len(values))
        draws.append(sum(x[1] for x in sampled)/sum(x[0] for x in sampled))
    draws.sort()
    n = len(selected)
    largest_group = max(groups, key=lambda k: groups[k][0])
    rest = [v for k,v in groups.items() if k != largest_group]
    return {'tokens': n, 'connected_groups': len(groups),
            'frequency_bits_per_token': sum(r['frequency_bits'] for r in selected)/n,
            'metadata_bits_per_token': sum(r['metadata_bits'] for r in selected)/n,
            'neighbor_bits_per_token': sum(r['neighbor_bits'] for r in selected)/n,
            'neighbor_improvement_over_metadata_bits': sum(r['metadata_bits']-r['neighbor_bits'] for r in selected)/n,
            'component_bootstrap_95_percentile_interval': [draws[25], draws[974]],
            'group_size_sensitivity': {
                'status': 'Added after inspecting group sizes; fixed predictions, no refitting',
                'largest_selected_group': largest_group,
                'largest_selected_group_tokens': groups[largest_group][0],
                'equal_component_weight_improvement_bits': sum(v[1]/v[0] for v in values)/len(values),
                'excluding_largest_component_improvement_bits': sum(v[1] for v in rest)/sum(v[0] for v in rest)},
            'bootstrap_scope': 'Fixed out-of-fold predictions and fixed supported families; not selection-adjusted or causal'}


def main():
    features_path = ROOT/'data/processed/catalogue_features.json'
    protocol_path = ROOT/'data/processed/sign_family_protocol.json'
    features = json.loads(features_path.read_text())
    protocol = json.loads(protocol_path.read_text())
    families, owner = family_inventory(features)
    raw = read_jsonl('data/processed/lipi_strict.jsonl')
    units = grouped_units(raw, owner)
    artifact_folds, normalized_folds = defaultdict(set), defaultdict(set)
    for r in units:
        artifact_folds[r['artifact']].add(r['fold'])
        normalized_folds[canonical(r['sequence'], owner)].add(r['fold'])
    assert all(len(v) == 1 for v in artifact_folds.values())
    assert all(len(v) == 1 for v in normalized_folds.values())
    tokens = tokens_from_units(units, owner)
    counts = defaultdict(Counter)
    for t in tokens:
        counts[t['family']][t['sign']] += 1
    gate = protocol['support_gate']
    supported = {f for f in families if sum(counts[f].values()) >= gate['minimum_tokens']
                 and sum(n >= 5 for n in counts[f].values()) >= gate['minimum_variants_with_five_tokens']}
    scored = []
    for fold in range(5):
        train = [t for t in tokens if t['fold'] != fold]
        test = [t for t in tokens if t['fold'] == fold]
        assert {t['group'] for t in train}.isdisjoint(t['group'] for t in test)
        for strength in protocol['smoothing_strengths']:
            model = VariantModel(train, families, strength)
            for t in test:
                p0, p1, p2 = model.probabilities(t)
                scored.append({k:v for k,v in t.items() if k not in ('metadata', 'neighbors')} | {
                    'metadata': json.dumps(t['metadata']), 'neighbors': json.dumps(t['neighbors']),
                    'strength': strength, 'frequency_bits': -math.log2(p0),
                    'metadata_bits': -math.log2(p1), 'neighbor_bits': -math.log2(p2),
                    'variant_absent_in_training': model.frequency[t['family']][t['sign']] == 0,
                    'neighbor_training_support': sum(model.neighbors.get((t['family'], t['neighbors']), {}).values())})
    write_csv('results/family_token_predictions.csv', scored)
    write_csv('results/family_group_folds.csv', [{'artifact': r['artifact'], 'ids': ';'.join(r['source_ids']),
        'sequence': ' '.join(r['sequence']), 'family_normalized_sequence': ' '.join(canonical(r['sequence'], owner)),
        'group': r['group'], 'fold': r['fold'], 'site': r['site'], 'type': r['type']} for r in units])
    descriptions = descriptive_evidence(units, owner)
    by_family = {}
    for f in sorted(families):
        evaluations = []
        for strength in protocol['smoothing_strengths']:
            rs = [r for r in scored if r['family'] == f and r['strength'] == strength]
            if not rs:
                continue
            gains = [r['metadata_bits']-r['neighbor_bits'] for r in rs]
            evaluations.append({'strength': strength, 'tokens': len(rs),
                'neighbor_improvement_over_metadata_bits': sum(gains)/len(rs),
                'tokens_with_seen_neighbor_context': sum(r['neighbor_training_support'] > 0 for r in rs),
                'tokens_with_variant_absent_in_training': sum(r['variant_absent_in_training'] for r in rs),
                'fold_improvements': {str(k): sum(r['metadata_bits']-r['neighbor_bits'] for r in rs if r['fold']==k)/sum(r['fold']==k for r in rs)
                                      for k in range(5) if any(r['fold']==k for r in rs)}})
        by_family[f] = {'members': families[f], 'observed_variant_counts': dict(counts[f]),
                        'meets_support_gate': f in supported, 'evaluations': evaluations,
                        **descriptions[f], 'allograph_status': 'not established'}
    source_entries = {r['id']:r for r in features}
    summary_rows = []
    for f,r in by_family.items():
        e20 = next((e for e in r['evaluations'] if e['strength'] == 20), None)
        summary_rows.append({'source_P_entry': f,
            'candidate_M_ids': ';'.join(source_entries[f]['mahadevan_graphemes']),
            'candidate_W_ids': ';'.join(r['members']),
            'observed_variant_counts': json.dumps(r['observed_variant_counts'], sort_keys=True),
            'tokens': sum(r['observed_variant_counts'].values()),
            'meets_support_gate': r['meets_support_gate'],
            'exact_substitution_frames': len(r['exact_substitution_frames']),
            'texts_with_distinct_members': len(r['texts_with_distinct_members']),
            **{f'neighbor_gain_strength_{s}': next((e['neighbor_improvement_over_metadata_bits']
                for e in r['evaluations'] if e['strength']==s), '') for s in protocol['smoothing_strengths']},
            'seen_neighbor_context_tokens_strength_20': e20['tokens_with_seen_neighbor_context'] if e20 else 0,
            'allograph_status': 'not established'})
    write_csv('results/sign_family_summary.csv', summary_rows)
    primary = {r['sign']:r for r in csv.DictReader((ROOT/'results/primary_sign_profiles_417.csv').open())}
    index = []
    for m in sorted(primary):
        entries = [r for r in features if m in r['mahadevan_graphemes']]
        candidate = sorted({r['id'] for r in entries} & set(families))
        tested = sorted(set(candidate) & supported)
        index.append({'sign': m, 'primary_occurrences': primary[m]['total'],
            'primary_positional_description': primary[m]['distributional_description'],
            'source_P_entries': ';'.join(sorted(r['id'] for r in entries)),
            'candidate_W_ids': ';'.join(sorted({w for r in entries for w in r['wells_graphemes']})),
            'multi_W_families': ';'.join(candidate), 'supported_families': ';'.join(tested),
            'coverage': 'mapped_family_meets_support_gate' if tested else 'mapped_family_too_sparse' if candidate else 'no_multi_W_family_asserted',
            'semantic_value': 'undetermined', 'phonetic_value': 'undetermined',
            'caveat': 'Many-to-many source correspondence; family results cannot be assigned uniquely to each M variant.'})
    assert len(index) == 417
    write_csv('results/sign_family_index_417.csv', index)
    group_sizes = Counter(r['group'] for r in units)
    result = {'protocol_sha256': sha256(protocol_path), 'features_sha256': sha256(features_path),
        'source_rows': len(raw), 'deduplicated_artifact_sequence_context_units': len(units),
        'connected_groups': len(group_sizes), 'largest_group_units': max(group_sizes.values()),
        'leakage_checks': {'artifacts_crossing_folds': sum(len(v)>1 for v in artifact_folds.values()),
                           'family_normalized_texts_crossing_folds': sum(len(v)>1 for v in normalized_folds.values())},
        'fold_unit_counts': dict(Counter(r['fold'] for r in units)),
        'families': by_family, 'candidate_families': len(families),
        'supported_families': sorted(supported), 'family_tokens': len(tokens),
        'aggregate_by_strength': {str(s): aggregate_bootstrap(scored, supported, s) for s in protocol['smoothing_strengths']},
        'all_M_coverage': dict(Counter(r['coverage'] for r in index)), 'new_established_sign_values': 0,
        'interpretation': 'Variant-context predictability conditional on family. Neither positive nor absent gain identifies allography or meaning.'}
    write_json('results/sign_family_audit.json', result)
    print(f"{len(families)} candidate families; {len(supported)} meet support gate; {len(index)} M-index rows")
    print(json.dumps(result['aggregate_by_strength'], sort_keys=True))


if __name__ == '__main__':
    main()
