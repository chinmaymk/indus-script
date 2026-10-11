"""Exploratory grouped predictive test of context beyond adjacent signs.

All quantities are file-order predictions, not readings or semantic labels.
"""
from collections import Counter, defaultdict
import math
import random
from analyze_sequences import grouped_records
from common import ROOT, read_jsonl, write_csv, write_json, sha256

SEED = 20260923
STRENGTHS = (5, 20, 100)
MODES = ('slot', 'previous_one', 'previous_two', 'first_plus_previous_two')
CONTROL_MODES = ('two_parent_refinement', 'first_parent_refinement')


def context_keys(sequence, i, metadata=()):
    """Each key uses only earlier signs, known length/index, and optional metadata."""
    base = (len(sequence), i, metadata)
    one = (base, sequence[i-1]) if i >= 1 else None
    two = (base, tuple(sequence[i-2:i])) if i >= 2 else None
    remote = (base, sequence[0], tuple(sequence[i-2:i])) if i >= 3 else None
    return base, one, two, remote


class ContextModel:
    def __init__(self, records, vocab, strength=20, use_metadata=False):
        self.vocab, self.strength = tuple(vocab), strength
        self.use_metadata = use_metadata
        self.unigram = Counter()
        self.counts = [defaultdict(Counter) for _ in MODES]
        for row in records:
            seq = row['sequence']
            self.unigram.update(seq)
            metadata = row.get('metadata', ()) if use_metadata else ()
            for i, x in enumerate(seq):
                for table, key in zip(self.counts, context_keys(seq, i, metadata)):
                    if key is not None:
                        table[key][x] += 1
        self.total = sum(self.unigram.values())
        self.totals = [{key:sum(c.values()) for key,c in table.items()} for table in self.counts]

    def probabilities(self, x, seq, i, metadata=()):
        if x not in self.vocab:
            raise ValueError('Target outside declared inventory')
        p = (self.unigram[x]+.5)/(self.total+.5*len(self.vocab))
        result = []
        for table, totals, key in zip(self.counts, self.totals,
                context_keys(seq, i, metadata if self.use_metadata else ())):
            if key is not None:
                p = (table.get(key, {}).get(x, 0)+self.strength*p)/(totals.get(key, 0)+self.strength)
            result.append(p)
        return result


    def refinement_controls(self, x, seq, i, metadata=()):
        """Post-result diagnostic: sharpen parent with child-sized pseudo-counts.

        Same child support/alpha, but its empirical composition is replaced by
        parent composition. The child identity still selects its support count,
        but not a distinct target composition.
        """
        probabilities = self.probabilities(x, seq, i, metadata)
        keys = context_keys(seq, i, metadata if self.use_metadata else ())
        output = []
        for child in (2,3):
            parent = child-1
            parent_n = self.totals[parent].get(keys[parent],0)
            child_n = self.totals[child].get(keys[child],0)
            empirical = self.counts[parent].get(keys[parent],{}).get(x,0)/parent_n if parent_n else probabilities[parent]
            output.append((child_n*empirical+self.strength*probabilities[parent])/(child_n+self.strength))
        return output


def grouped_with_metadata(records):
    grouped = grouped_records(records)
    by_sequence = defaultdict(set)
    for row in records:
        by_sequence[tuple(row['sequence'])].add((row.get('site','unknown'), row.get('type','unknown')))
    for row in grouped:
        row['metadata'] = tuple(sorted(by_sequence[tuple(row['sequence'])]))
    return grouped


def evaluate(records, vocab, strength, use_metadata=False):
    grouped = grouped_with_metadata(records)
    ledger = []
    for fold in range(5):
        model = ContextModel([r for r in grouped if r['fold'] != fold], vocab, strength, use_metadata)
        for row in grouped:
            if row['fold'] != fold:
                continue
            seq = row['sequence']
            for i in range(2, len(seq)):
                probs = model.probabilities(seq[i], seq, i, row['metadata'])
                entry = dict(group=row['group'], fold=fold, ids=row['ids'], artifacts=row['artifacts'],
                    sequence=' '.join(seq), index=i, target=seq[i], length=len(seq),
                    metadata=repr(row['metadata']))
                entry.update({mode:-math.log2(p) for mode,p in zip(MODES,probs)})
                entry.update({mode:-math.log2(p) for mode,p in zip(CONTROL_MODES,model.refinement_controls(seq[i],seq,i,row['metadata']))})
                ledger.append(entry)
    return ledger, grouped


def summarize(ledger):
    common = [r for r in ledger if r['index'] >= 3]
    output = {'tokens_common_index_ge_3':len(common), 'tokens_two_context_index_ge_2':len(ledger)}
    output['loss_common_bits_per_token'] = {m:sum(r[m] for r in common)/len(common) for m in MODES+CONTROL_MODES}
    comparisons = [('two_over_one_common',common,'previous_one','previous_two'),
                   ('first_over_two_common',common,'previous_two','first_plus_previous_two'),
                   ('two_over_one_all_eligible',ledger,'previous_one','previous_two'),
                   ('two_over_parent_refinement',common,'two_parent_refinement','previous_two'),
                   ('first_over_parent_refinement',common,'first_parent_refinement','first_plus_previous_two')]
    for name, rows, baseline, candidate in comparisons:
        groups = defaultdict(lambda:[0,0.])
        folds = defaultdict(lambda:[0,0.])
        for r in rows:
            gain = r[baseline]-r[candidate]
            for bucket in (groups[r['group']],folds[r['fold']]):
                bucket[0] += 1
                bucket[1] += gain
        gs = list(groups.values())
        rng = random.Random(SEED)
        draws = []
        for _ in range(1000):
            sample = rng.choices(gs,k=len(gs))
            draws.append(sum(g[1] for g in sample)/sum(g[0] for g in sample))
        draws.sort()
        largest = max(gs,key=lambda g:g[0])
        output[name] = {'gain_bits_per_token':sum(g[1] for g in gs)/sum(g[0] for g in gs),
            'group_bootstrap_95_interval':[draws[25],draws[974]],
            'equal_group_gain':sum(g[1]/g[0] for g in gs)/len(gs),
            'excluding_largest_group_gain':(sum(g[1] for g in gs)-largest[1])/(sum(g[0] for g in gs)-largest[0]),
            'groups':len(gs), 'largest_group_tokens':largest[0],
            'fold_gains':{k:v[1]/v[0] for k,v in folds.items()}}
    return output


def synthetic_records(mode, n=6000):
    rng = random.Random(SEED)
    alphabet = tuple('ABCDEFGH')
    rows = []
    for j in range(n):
        seq = [rng.choice(alphabet),rng.choice(alphabet)]
        for i in range(2,8):
            if mode == 'order_one':
                value = (alphabet.index(seq[-1])+1)%8
            else:
                value = (alphabet.index(seq[-1])+alphabet.index(seq[-2]))%8
                if mode == 'remote_memory' and i >= 3:
                    value = (value+alphabet.index(seq[0]))%8
            seq.append(alphabet[value] if rng.random() < .8 else rng.choice(alphabet))
        rows.append(dict(id=f'synthetic:{j}',artifact=f'synthetic:{j}',site='synthetic',type='synthetic',sequence=seq))
    return rows, alphabet


def main():
    result = {'protocol_sha256':sha256(ROOT/'data/processed/structure_theory_protocol.json'),
        'seed':SEED, 'headline_strength':20, 'results':{}}
    indus = read_jsonl('data/processed/lipi_strict.jsonl')
    weather = read_jsonl('data/processed/sproat_WeatherIcons.jsonl')
    datasets = [('indus',indus,tuple(f'W{i:03}' for i in range(1,999)),False,STRENGTHS),
                ('indus_metadata',indus,tuple(f'W{i:03}' for i in range(1,999)),True,STRENGTHS),
                ('weather',weather,tuple(sorted({x for r in weather for x in r['sequence']})),False,STRENGTHS)]
    for mode in ('order_one','order_two','remote_memory'):
        rows,vocab = synthetic_records(mode)
        datasets.append(('synthetic_'+mode,rows,vocab,False,(20,)))
    for label, rows, vocab, metadata, strengths in datasets:
        result['results'][label] = {}
        for strength in strengths:
            ledger,grouped = evaluate(rows,vocab,strength,metadata)
            summary = summarize(ledger)
            summary.update(unique_texts=len(grouped),connected_groups=len({r['group'] for r in grouped}),
                fold_text_counts=dict(Counter(r['fold'] for r in grouped)))
            result['results'][label][strength] = summary
            write_csv(f'results/structure_theory_{label}_{strength}.csv',ledger)
            print(label,strength,summary['two_over_one_common']['gain_bits_per_token'],
                summary['first_over_two_common']['gain_bits_per_token'],flush=True)
    write_json('results/structure_theory.json',result)


if __name__ == '__main__':
    main()
