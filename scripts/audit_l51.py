"""L51's depicted ending and its source-selected fish/U association."""
import csv
import json
import re
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb
from common import ROOT,sha256,read_jsonl,write_json
from audit_pipe_chain import certain_tokens,FIELDS


def is_ending(sequence):
    return sequence[:2] == ['W527','W555']


def conditioned(rows, codes):
    strata=defaultdict(list)
    for r in rows:
        strata[(r['site'],r['type'],len(r['sequence']))].append(r)
    dist={0:Fraction(1)}; details=[]; observed=0; expected=Fraction(0)
    for key,members in sorted(strata.items()):
        n=sum(is_ending(r['sequence']) for r in members)
        if not n:continue
        N=len(members); K=sum(bool(set(r['sequence']) & codes) for r in members)
        a=sum(is_ending(r['sequence']) and bool(set(r['sequence'])&codes) for r in members)
        observed+=a;expected+=Fraction(n*K,N)
        probs={j:Fraction(comb(K,j)*comb(N-K,n-j),comb(N,n))
               for j in range(max(0,n-N+K),min(n,K)+1)}
        new=defaultdict(Fraction)
        for i,p in dist.items():
            for j,q in probs.items():new[i+j]+=p*q
        dist=dict(new)
        details.append({'site':key[0],'type':key[1],'length':key[2],'N':N,
                        'ending':n,'target':K,'both':a,
                        'ending_ids':[r['cisi'] for r in members if is_ending(r['sequence'])]})
    assert sum(dist.values())==1
    tail=sum((p for j,p in dist.items() if j>=observed),Fraction())
    return {'universe_rows':len(rows),'ending_rows':sum(s['ending'] for s in details),
            'observed_both':observed,'conditional_expected':float(expected),
            'upper_tail_descriptive_only':float(tail),'exact_fraction':str(tail),'strata':details}


def summarize(rows,target):
    counts=Counter('positive' if r[target] is True else 'negative' if r[target] is False else 'unknown' for r in rows)
    n=len(rows)
    return {'rows':n,'objects':len({r['id'].split('.')[0] for r in rows}),
            **{k:counts[k] for k in ('positive','negative','unknown')},
            'observed_positive_fraction':counts['positive']/n if n else None,
            'possible_positive_fraction_bounds':[counts['positive']/n,(counts['positive']+counts['unknown'])/n] if n else None}


def main():
    inputs=['data/processed/l51_protocol.json','data/raw/lipi_inscriptions.csv',
            'data/processed/lipi_strict.jsonl','data/processed/catalogue_features.json']
    protocol=json.loads((ROOT/inputs[0]).read_text())
    with (ROOT/inputs[1]).open() as f:raw=[{k:r.get(k,'') for k in FIELDS} for r in csv.DictReader(f)]
    byid={r['id']:r for r in raw};counts=Counter(r['id'].split('.')[0] for r in raw)
    fish={c for f in json.loads((ROOT/inputs[3]).read_text()) if f['id'] in protocol['fish_family_ids'] for c in f['wells_graphemes']}
    U=set(protocol['U_candidates']);targets={'fish':fish,'plain_fish':{'W220'},'U':U,'fish_or_U':fish|U}
    hitrows=[];elsewhere=[]
    for r in raw:
        if not r['type'].startswith('SEAL'):continue
        if not re.search(r'(?<![\d*?/])527-555(?![\d?*/])',r['text']):continue
        seq=certain_tokens(r['text'])
        readable=(r['complete']=='Y' and bool(re.fullmatch(r'\+\d{3}(?:-\d{3})*\+',r['text']))
                  and not re.search(r'(?<!\d)(000|999)(?!\d)',r['text']))
        row=dict(r,reading_ending_certified_by_direction=r['dir.']=='R/L',
                 **{t:True if set(seq)&cs else False if readable else None for t,cs in targets.items()})
        if re.match(r'^\+527-555(?:[-+\[])',r['text']):hitrows.append(row)
        else:elsewhere.append(row)
    universe=[]
    for r in read_jsonl(inputs[2]):
        rawrow=byid[r['id']]
        if (counts[r['id'].split('.')[0]]==1 and rawrow['complete']=='Y'
            and rawrow['preservation']=='complete' and rawrow['type'].startswith('SEAL')
            and len(r['sequence'])>=2):universe.append(dict(rawrow,sequence=r['sequence']))
    dedup={}
    for r in universe:dedup.setdefault((r['site'],r['type'],tuple(r['sequence'])),r)
    branches={'objects':universe,'text_types':list(dedup.values()),
              'same_W527_terminal_objects':[r for r in universe if r['sequence'][0]=='W527']}
    result={'protocol':protocol,'fish_codes':sorted(fish),'raw_ending_rows':hitrows,'pair_elsewhere':elsewhere,
            'raw_summaries':{t:summarize(hitrows,t) for t in targets},
            'conservative_preservation_summaries':{
                t:summarize([dict(r,**{t:None if r[t] is False and r['preservation']!='complete' else r[t]})
                             for r in hitrows],t) for t in targets},
            'matched':{t:{b:conditioned(rows,codes) for b,rows in branches.items()} for t,codes in targets.items()},
            'eligible_ending_rows':[r for r in universe if is_ending(r['sequence'])],
            'input_sha256':{p:sha256(ROOT/p) for p in inputs},
            'established_semantic_values':0,'established_phonetic_values':0}
    result['primary_reviews']={}
    for label in ('context','visual'):
        p=f'data/processed/l51_{label}_review.json'
        review=json.loads((ROOT/p).read_text())
        for pin in review['evidence_files']:
            f=ROOT/pin['path'];assert f.stat().st_size==pin['bytes'] and sha256(f)==pin['sha256'],pin['path']
        result['primary_reviews'][label]=review
        result['input_sha256'][p]=sha256(ROOT/p)
    write_json('results/l51_audit.json',result)
    print(json.dumps(result['raw_summaries'],indent=2))
    print('Pair elsewhere',[(r['cisi'],r['text']) for r in elsewhere])
    for t,branches in result['matched'].items():
        print(t,{b:{k:v for k,v in v.items() if k!='strata'} for b,v in branches.items()})


if __name__=='__main__':main()
