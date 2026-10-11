"""Independent raw-text reconstruction of ending follow-up counts and exact tails.

No production-analysis imports; this validates computation, not readings/meanings.
"""
import csv
import hashlib
import itertools
import json
import re
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    paths=['data/raw/lipi_inscriptions.csv','data/processed/catalogue_features.json',
           'data/processed/ending_validation_protocol.json','results/ending_validation_audit.json']
    with (ROOT/paths[0]).open() as f:
        fields=['id','cisi','text','site','type','complete','preservation','dir.','class','signs']
        raw=[{k:r[k] for k in fields} for r in csv.DictReader(f)]
    counts=Counter(r['id'].split('.')[0] for r in raw)
    universe=[]
    for r in raw:
        if not re.fullmatch(r'\+\d{3}(?:-\d{3})*\+',r['text']):continue
        seq=tuple('W'+v for v in r['text'][1:-1].split('-'))
        if ({'W000','W999'} & set(seq) or r['complete'].strip()!='Y'
                or r['dir.'].strip().upper()!='R/L' or r['class'].strip() in ('2L','3L')
                or (r['signs'].isdigit() and len(seq)!=int(r['signs']))):continue
        if (counts[r['id'].split('.')[0]]==1 and r['complete']=='Y'
                and r['preservation']=='complete' and r['type'].startswith('SEAL') and len(seq)>=2):
            universe.append(dict(r,seq=seq))
    counterparts={r['id']:sorted(s['id'] for s in universe if s['seq']==r['seq'][:1]+r['seq'][2:])
                  for r in universe if r['seq'][:2]==('W527','W555')}
    alternate={r['id']:sorted(s['id'] for s in universe if s['seq']==('W527',)+r['seq'][1:])
               for r in universe if r['seq'][1]=='W555' and r['seq'][0]!='W527'}
    catalogue=json.loads((ROOT/paths[1]).read_text())
    fish={w for f in catalogue if f['id'] in ['P050','P051']+['P%03d'%i for i in range(56,65)]
          for w in f['wells_graphemes']}
    protocol=json.loads((ROOT/paths[2]).read_text())
    rows=[r for r in universe if r['cisi'] not in protocol['known_named_examples']]
    strata=defaultdict(list)
    for r in rows:strata[r['site'],r['type'],len(r['seq'])].append(r)
    tails={}
    for target,codes in {'fish':fish,'plain_fish':{'W220'},'U':{'W705','W706'},'fish_or_U':fish|{'W705','W706'}}.items():
        active=[]
        for members in strata.values():
            exposed=[r for r in members if r['seq'][:2]==('W527','W555')]
            if not exposed:continue
            assert len(exposed)==1
            active.append((len(members),sum(bool(codes & set(r['seq'])) for r in members),
                           int(bool(codes & set(exposed[0]['seq'])))))
        observed=sum(s[2] for s in active)
        expectation=sum((Fraction(k,n) for n,k,_ in active),Fraction())
        tail=Fraction();total=Fraction()
        for bits in itertools.product((0,1),repeat=len(active)):
            p=Fraction(1)
            for bit,(n,k,_) in zip(bits,active):p*=Fraction(k if bit else n-k,n)
            total+=p
            if sum(bits)>=observed:tail+=p
        assert total==1
        tails[target]={'observed':observed,'expectation':str(expectation),'tail':str(tail),
                       'patterns':2**len(active),'active_strata':len(active)}
    actual=json.loads((ROOT/paths[3]).read_text())
    assert len(universe)==actual['universe_rows']
    assert counterparts=={r['with_W555']['id']:sorted(s['id'] for s in r['without_W555_matches']) for r in actual['exact_counterparts']}
    assert alternate=={r['other_first_token']['id']:sorted(s['id'] for s in r['W527_full_context_matches']) for r in actual['alternate_first_token_full_context_matches']}
    for target,r in tails.items():
        a=actual['retrospective_leave_named_out'][target]
        assert a['observed_both']==r['observed'] and a['exact_fraction']==r['tail']
        assert abs(a['conditional_expected']-float(Fraction(r['expectation'])))<1e-12
        assert a['ending_rows']==r['active_strata'] and a['universe_rows']==len(rows)
    out={'universe_rows':len(universe),'counterparts':counterparts,'alternate_pairs':alternate,
         'leave_named_out_exact_checks':tails,'all_comparisons_agree':True,
         'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/ending_independent_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Ending follow-up verified from raw CSV; all exact counterpart and four tail comparisons agree.')

if __name__=='__main__':main()
