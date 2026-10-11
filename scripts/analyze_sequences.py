"""Reproducible structural tests, controls, grouped predictive evaluation.

No language labels, dictionaries, or proposed translations are used.
All directions are file order. Reversal does not alter adjacency mutual information.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
import random
import statistics
from common import ROOT, read_jsonl, write_json, write_csv

SEED = 20260922

def entropy(counts):
    total = sum(counts.values())
    return -sum((n / total) * math.log2(n / total) for n in counts.values() if n) if total else 0.0

def mutual_information(sequences):
    pairs = Counter((a, b) for s in sequences for a, b in zip(s, s[1:]))
    left, right = Counter(), Counter()
    for (a, b), n in pairs.items():
        left[a] += n
        right[b] += n
    total = sum(pairs.values())
    return sum(n / total * math.log2(n * total / (left[a] * right[b])) for (a, b), n in pairs.items()) if total else 0.0

def endpoint_js(sequences):
    a = Counter(s[0] for s in sequences if len(s) > 1)
    b = Counter(s[-1] for s in sequences if len(s) > 1)
    both = a + b
    return entropy(both) - (entropy(a) + entropy(b)) / 2 if both else 0.0

def summarize(sequences):
    freq = Counter(x for s in sequences for x in s)
    return {'sequences': len(sequences), 'tokens': sum(freq.values()), 'sign_types': len(freq),
            'length_mean': statistics.mean(map(len, sequences)), 'length_max': max(map(len, sequences)),
            'length_histogram': dict(sorted(Counter(map(len, sequences)).items())),
            'hapax_sign_types': sum(n == 1 for n in freq.values()), 'unigram_entropy_bits': entropy(freq),
            'adjacent_mutual_information_bits': mutual_information(sequences),
            'endpoint_js_bits': endpoint_js(sequences),
            'texts_with_repeated_sign_fraction': sum(len(set(s)) < len(s) for s in sequences) / len(sequences)}

def shuffle_sequences(sequences, rng, mode):
    out = [list(s) for s in sequences]
    if mode == 'within_text':
        for s in out:
            rng.shuffle(s)
    elif mode == 'length_position':
        slots = defaultdict(list)
        for i, s in enumerate(out):
            for j in range(len(s)):
                slots[len(s), j].append(i)
        for (_, j), indices in slots.items():
            values = [out[i][j] for i in indices]
            rng.shuffle(values)
            for i, x in zip(indices, values):
                out[i][j] = x
    else:
        raise ValueError(mode)
    return out

def permutation_test(sequences, iterations):
    observed = {'mi': mutual_information(sequences), 'endpoint_js': endpoint_js(sequences)}
    result = {'observed': observed, 'iterations': iterations, 'seed': SEED}
    for mode in ('within_text', 'length_position'):
        rng = random.Random(SEED)
        values = {'mi': [], 'endpoint_js': []}
        for _ in range(iterations):
            shuffled = shuffle_sequences(sequences, rng, mode)
            values['mi'].append(mutual_information(shuffled))
            if mode == 'within_text':
                values['endpoint_js'].append(endpoint_js(shuffled))
        result[mode] = {}
        for key, draws in values.items():
            if not draws:
                continue
            ordered = sorted(draws)
            result[mode][key] = {'null_mean': statistics.mean(draws),
                'null_95_interval': [ordered[int(.025 * len(draws))], ordered[min(len(draws)-1, int(.975 * len(draws)))]],
                'observed_minus_null_mean': observed[key] - statistics.mean(draws),
                'p_upper': (1 + sum(x >= observed[key] - 1e-12 for x in draws)) / (iterations + 1)}
    return result

def slot(index, length):
    return 'single' if length == 1 else 'start' if index == 0 else 'end' if index == length-1 else 'middle'

class Model:
    """All probabilities normalized over fixed, known symbol inventory.

    unigram add-1/2; positional and bigram contexts use hierarchical Dirichlet
    smoothing. The combined model backs (previous, slot) off to slot probability.
    Length is given to all models; no end-of-text token is scored.
    """
    def __init__(self, sequences, vocab, mode='bigram_position', strength=20):
        self.vocab = tuple(sorted(vocab))
        self.mode, self.strength = mode, strength
        self.count = Counter(x for s in sequences for x in s)
        self.total = sum(self.count.values())
        self.context = defaultdict(Counter)
        self.positions = defaultdict(Counter)
        for s in sequences:
            for i, x in enumerate(s):
                p, prev = slot(i, len(s)), s[i-1] if i else '<BOS>'
                self.positions[p][x] += 1
                self.context[prev if mode == 'bigram' else (prev, p)][x] += 1
        self.ctotal = {k: sum(v.values()) for k, v in self.context.items()}
        self.ptotal = {k: sum(v.values()) for k, v in self.positions.items()}

    def prob(self, x, prev, p):
        base = (self.count[x] + .5) / (self.total + .5 * len(self.vocab))
        if self.mode == 'unigram':
            return base
        pos = (self.positions.get(p, {}).get(x, 0) + self.strength * base) / (self.ptotal.get(p, 0) + self.strength)
        if self.mode == 'position':
            return pos
        key = prev if self.mode == 'bigram' else (prev, p)
        backoff = base if self.mode == 'bigram' else pos
        return (self.context.get(key, {}).get(x, 0) + self.strength * backoff) / (self.ctotal.get(key, 0) + self.strength)

    def loss(self, seq):
        return -sum(math.log2(self.prob(x, seq[i-1] if i else '<BOS>', slot(i, len(seq)))) for i, x in enumerate(seq))

def grouped_records(records):
    # Connected components: neither a repeated sequence nor an artifact can cross folds.
    parent = list(range(len(records)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    seen = {}
    for i, r in enumerate(records):
        for key in [('text', tuple(r['sequence'])), ('artifact', r['artifact'])]:
            if key in seen:
                parent[find(i)] = find(seen[key])
            else:
                seen[key] = i
    members = defaultdict(list)
    for i, r in enumerate(records):
        members[find(i)].append(r)
    out = []
    for rs in members.values():
        signature = '|'.join(sorted(set(' '.join(r['sequence']) for r in rs)))
        group = hashlib.sha256(signature.encode()).hexdigest()
        by_seq = defaultdict(list)
        for r in rs:
            by_seq[tuple(r['sequence'])].append(r)
        for seq, source in sorted(by_seq.items()):
            out.append({'sequence': seq, 'group': group, 'fold': int(group[:12], 16) % 5,
                        'ids': ';'.join(r['id'] for r in source),
                        'artifacts': ';'.join(sorted({r['artifact'] for r in source})),
                        'sites': sorted({r['site'] for r in source})})
    return sorted(out, key=lambda r: (r['group'], r['sequence']))

def evaluate(records, vocab, label):
    grouped = grouped_records(records)
    ledger, tuning = [], []
    modes = ['unigram', 'position', 'bigram', 'bigram_position']
    for fold in range(5):
        test = [r for r in grouped if r['fold'] == fold]
        validation = [r for r in grouped if r['fold'] == (fold + 1) % 5]
        train = [r for r in grouped if r['fold'] not in (fold, (fold + 1) % 5)]
        models = {}
        for mode in modes:
            trials = []
            for strength in ([20] if mode == 'unigram' else [1, 5, 20, 100]):
                model = Model([r['sequence'] for r in train], vocab, mode, strength)
                loss = sum(model.loss(r['sequence']) for r in validation) / sum(len(r['sequence']) for r in validation)
                trials.append((loss, strength))
                tuning.append({'fold': fold, 'mode': mode, 'strength': strength, 'validation_bits_per_sign': loss})
            strength = min(trials)[1]
            models[mode] = Model([r['sequence'] for r in train + validation], vocab, mode, strength)
        for r in test:
            result = {'fold': fold, 'group': r['group'], 'ids': r['ids'], 'artifacts': r['artifacts'],
                      'sequence': ' '.join(r['sequence']), 'length': len(r['sequence'])}
            for mode, model in models.items():
                result[mode] = model.loss(r['sequence'])
            ledger.append(result)
    write_csv(f'results/prediction_{label}.csv', ledger)
    write_csv(f'results/tuning_{label}.csv', tuning)
    total = sum(r['length'] for r in ledger)
    losses = {mode: sum(r[mode] for r in ledger) / total for mode in modes}
    groups = defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0])
    for r in ledger:
        g = groups[r['group']]
        g[0] += r['length']
        g[1] += r['unigram'] - r['bigram_position']
        g[2] += r['position'] - r['bigram_position']
        g[3] += r['unigram'] - r['bigram']
        g[4] += r['position'] - r['bigram']
    rng = random.Random(SEED)
    gs = list(groups.values())
    draws = [[], [], [], []]
    for _ in range(1000):
        sample = rng.choices(gs, k=len(gs))
        n = sum(g[0] for g in sample)
        for j in range(4):
            draws[j].append(sum(g[j+1] for g in sample) / n)
    intervals = {name: [sorted(ds)[25], sorted(ds)[974]] for name, ds in zip(
        ['combined_improvement_over_unigram', 'combined_improvement_over_position',
         'bigram_improvement_over_unigram', 'bigram_improvement_over_position'], draws)}
    return {'unique_sequences': len(grouped), 'connected_groups': len(gs), 'tokens': total,
            'bits_per_sign': losses, 'perplexity': {k: 2**v for k, v in losses.items()},
            'group_bootstrap_95_percentile_intervals': intervals,
            'fold_sequence_counts': dict(Counter(r['fold'] for r in grouped))}

def sign_profiles(records):
    seqs = sorted(set(tuple(r['sequence']) for r in records))
    counts = defaultdict(Counter)
    examples = defaultdict(list)
    for s in seqs:
        for i, x in enumerate(s):
            counts[x][slot(i, len(s))] += 1
            if len(examples[x]) < 4:
                examples[x].append(' '.join(s))
    rows = []
    for x, c in sorted(counts.items()):
        total = sum(c.values())
        edge_total = c['start'] + c['end']
        role = 'insufficient evidence' if total < 10 else 'mixed/interior'
        if total >= 10 and c['start'] / total >= .8:
            role = 'file-start concentrated'
        elif total >= 10 and c['end'] / total >= .8:
            role = 'file-end concentrated'
        rows.append({'sign': x, 'tokens_unique_texts': total, 'single': c['single'],
                     'file_start': c['start'], 'middle': c['middle'], 'file_end': c['end'],
                     'file_start_fraction': c['start']/total, 'file_end_fraction': c['end']/total,
                     'edge_occurrences': edge_total, 'provisional_distributional_role': role,
                     'examples_file_order': ' | '.join(examples[x])})
    return rows

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--permutations', type=int, default=499)
    args = parser.parse_args()
    corpus = read_jsonl('data/processed/lipi_strict.jsonl')
    rawseq = [r['sequence'] for r in corpus]
    unique = sorted(set(tuple(s) for s in rawseq))
    summary = {'lipi_rows': summarize(rawseq), 'lipi_unique': summarize(unique)}
    perms = {'lipi_unique': permutation_test(unique, args.permutations)}
    for label in ['mayig_strict', 'sproat_IndusBarSeals', 'sproat_BarnStars', 'sproat_WeatherIcons', 'sproat_TotemPoles', 'sproat_Kudurrus', 'sproat_Pictish']:
        recs = read_jsonl('data/processed/' + label + '.jsonl')
        seqs = sorted({tuple(r['sequence']) for r in recs})
        summary[label] = summarize(seqs)
        perms[label] = permutation_test(seqs, args.permutations)
    write_json('results/sequence_summary.json', summary)
    write_json('results/permutation_tests.json', perms)
    write_csv('results/sign_profiles_wells.csv', sign_profiles(corpus))
    write_csv('results/sign_profiles_parpola.csv', sign_profiles(read_jsonl('data/processed/mayig_strict.jsonl')))
    pairs = Counter((a,b) for s in unique for a,b in zip(s,s[1:]))
    write_csv('results/common_pairs.csv', [{'first': a, 'second': b, 'count_unique_texts': n}
              for (a,b),n in pairs.most_common()])
    vocab = ['W' + str(i).zfill(3) for i in range(1,999)]
    predictions = {'lipi': evaluate(corpus, vocab, 'lipi')}
    # Distributional evidence alone does not determine physical reading direction.
    predictions['reversal_invariance'] = {
        'mi_abs_difference': abs(mutual_information(unique)-mutual_information([s[::-1] for s in unique])),
        'js_abs_difference': abs(endpoint_js(unique)-endpoint_js([s[::-1] for s in unique]))}
    # Cross-site test removes every test sequence from the training pool.
    site_results = {}
    for site in ['Harappa', 'Mohenjo-daro']:
        test = sorted({tuple(r['sequence']) for r in corpus if r['site'] == site})
        train = sorted({tuple(r['sequence']) for r in corpus if r['site'] != site} - set(test))
        losses = {}
        for mode in ['unigram','position','bigram_position']:
            model = Model(train,vocab,mode,20)
            losses[mode] = sum(model.loss(s) for s in test)/sum(map(len,test))
        site_results[site] = {'train_unique': len(train), 'test_unique': len(test), 'bits_per_sign': losses}
    predictions['cross_site_fixed_strength_20'] = site_results
    write_json('results/predictive_tests.json', predictions)
    print(json.dumps({'summary': summary['lipi_unique'], 'prediction': predictions['lipi']}, indent=2))

if __name__ == '__main__':
    main()
