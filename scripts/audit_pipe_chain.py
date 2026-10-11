"""Literal chain-sign contexts and matched descriptive calibration, without readings."""
import csv
import json
import re
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb
from common import ROOT, sha256, read_jsonl, write_json

FIELDS = ('id','cisi','site','excavation-idno','type','preservation','complete',
          'condition','dir.','text','symbol','room-grid','depth')


def certain_tokens(text):
    return ['W'+m[1] for m in re.finditer(r'(?<![\d*?/])(\d{3})(?![\d?*/])',text)
            if m[1] not in ('000','999')]


def matched_tail(rows, target, chain):
    """Exact upper-tail convolution; no asymptotic sparse-cell approximation."""
    groups = defaultdict(list)
    for r in rows:
        groups[(r['site'],r['type'],len(r['sequence']))].append(r)
    dist = {0:Fraction(1)}
    strata = []
    observed = 0
    expected = Fraction(0)
    for key, group in sorted(groups.items()):
        N = len(group)
        n = sum(bool(set(r['sequence']) & chain) for r in group)
        if not n:
            continue
        K = sum(bool(set(r['sequence']) & target) for r in group)
        a = sum(bool(set(r['sequence']) & chain) and bool(set(r['sequence']) & target) for r in group)
        observed += a
        expected += Fraction(n*K,N)
        pmf = {j:Fraction(comb(K,j)*comb(N-K,n-j),comb(N,n))
               for j in range(max(0,n-(N-K)),min(n,K)+1)}
        new = defaultdict(Fraction)
        for old,p in dist.items():
            for j,q in pmf.items():
                new[old+j] += p*q
        dist = dict(new)
        strata.append({'site':key[0],'type':key[1],'length':key[2],
                       'N':N,'chain':n,'target':K,'both':a,
                       'chain_ids':[r['cisi'] for r in group if set(r['sequence']) & chain]})
    assert sum(dist.values()) == 1
    p = sum((q for j,q in dist.items() if j >= observed), Fraction(0))
    return {'universe_rows':len(rows),'chain_rows':sum(s['chain'] for s in strata),
            'observed_both':observed,'conditional_expected':float(expected),
            'upper_tail_descriptive_only':float(p),'exact_fraction':str(p),
            'strata':strata,'null_distribution':{str(k):float(v) for k,v in sorted(dist.items())}}


def main():
    inputs = ['data/processed/pipes_protocol.json','data/raw/lipi_inscriptions.csv',
              'data/processed/lipi_strict.jsonl','data/processed/catalogue_features.json']
    protocol = json.loads((ROOT/inputs[0]).read_text())
    with (ROOT/inputs[1]).open() as f:
        rows = [{k:r.get(k,'') for k in FIELDS} for r in csv.DictReader(f)]
    byid = {r['id']:r for r in rows}
    object_counts = Counter(r['id'].split('.')[0] for r in rows)
    strict = read_jsonl(inputs[2])
    strictids = {r['id'] for r in strict}
    features = json.loads((ROOT/inputs[3]).read_text())
    fish = {c for f in features if f['id'] in protocol['fish_families'] for c in f['wells_graphemes']}
    gold = set(protocol['gold_candidate_codes'])
    chain = set(protocol['chain_codes'])
    targets = {'fish_family':fish,'plain_fish':{'W220'},'attributed_gold_candidate':gold,
               'fish_or_attributed_gold_candidate':fish|gold}
    hits = []
    for r in rows:
        seq = certain_tokens(r['text'])
        if not set(seq)&chain:
            continue
        readable = (r['complete']=='Y' and bool(re.fullmatch(r'\+\d{3}(?:-\d{3})*\+',r['text']))
                    and not re.search(r'(?<!\d)(000|999)(?!\d)',r['text']))
        hits.append(dict(r, certain_sequence=seq, strict=r['id'] in strictids,
                         row_fully_readable=bool(readable),
                         **{name:True if set(seq)&codes else (False if readable else None)
                            for name,codes in targets.items()}))
    universe = []
    for r in strict:
        raw = byid[r['id']]
        if (object_counts[r['id'].split('.')[0]] == 1 and raw['complete']=='Y'
            and raw['preservation']=='complete' and raw['type'].startswith('SEAL')
            and len(r['sequence'])>2):
            universe.append(dict(raw,sequence=r['sequence']))
    seen = set(); dedup = []
    for r in universe:
        key = r['site'],r['type'],tuple(r['sequence'])
        if key not in seen:
            dedup.append(r); seen.add(key)
    seals = [r for r in hits if r['type'].startswith('SEAL')]
    longseals = [r for r in seals if len(r['certain_sequence'])>2]
    result = {'protocol':protocol,'chain_codes':sorted(chain),
              'fish_codes':sorted(fish),'raw_hits':hits,
              'raw_summary':{'rows':len(hits),'objects':len({r['id'].split('.')[0] for r in hits}),
                             'seal_rows':len(seals),'seal_objects':len({r['id'].split('.')[0] for r in seals}),
                             'seal_rows_with_more_than2_certain_tokens':len(longseals),
                             'short_surviving_seal_texts_with_unknown_original_length':
                                 [r['cisi'] for r in seals if len(r['certain_sequence'])<=2 and not r['row_fully_readable']],
                             'long_seal_positive_by_target':{name:sum(r[name] is True for r in longseals) for name in targets},
                             'long_seal_unknown_by_target':{name:sum(r[name] is None for r in longseals) for name in targets}},
              'matched_comparisons':{name:{'objects':matched_tail(universe,codes,chain),
                                          'deduplicated_texts':matched_tail(dedup,codes,chain)}
                                     for name,codes in targets.items()},
              'input_sha256':{p:sha256(ROOT/p) for p in inputs},
              'established_semantic_values':0,'established_phonetic_values':0}
    result['primary_reviews'] = {}
    for name in ('context','figure'):
        p = f'data/processed/pipes_{name}_review.json'
        review = json.loads((ROOT/p).read_text())
        for pin in review['evidence_files']:
            f = ROOT/pin['path']
            assert f.stat().st_size == pin['bytes'] and sha256(f) == pin['sha256'],pin['path']
        result['primary_reviews'][name] = review
        result['input_sha256'][p] = sha256(ROOT/p)
    write_json('results/pipe_chain_audit.json',result)
    print(json.dumps(result['raw_summary'],indent=2))
    for name,branches in result['matched_comparisons'].items():
        print(name,{b:{k:v for k,v in val.items() if k not in ('strata','null_distribution')} for b,val in branches.items()})


if __name__=='__main__':
    main()
