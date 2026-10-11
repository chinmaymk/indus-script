"""Independent CSV/strict-corpus enumeration; does not import the production audit.
Enumerates all 64 binary target outcomes in the six one-chain strata.
"""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import product
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
raw=list(csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open()))
by_id={r['id']:r for r in raw}
row_count=Counter(r['id'].split('.')[0] for r in raw)
strict=[json.loads(l) for l in (ROOT/'data/processed/lipi_strict.jsonl').read_text().splitlines()]
selected=[]
for r in strict:
 source=by_id[r['id']]
 if row_count[r['id'].split('.')[0]]==1 and source['complete']=='Y' and source['preservation']=='complete' and source['type'].startswith('SEAL') and len(r['sequence'])>2:
  selected.append(r)
fish=set()
for f in json.loads((ROOT/'data/processed/catalogue_features.json').read_text()):
 if f['id'] in {'P050','P051'}|{f'P{x:03}' for x in range(56,65)}:
  fish.update(f['wells_graphemes'])
chain={'W215','W216'}
gold={'W705','W706'}
targets={'fish_family':fish,'plain_fish':{'W220'},'attributed_gold_candidate':gold,'fish_or_attributed_gold_candidate':fish|gold}
expected=json.loads((ROOT/'results/pipe_chain_audit.json').read_text())['matched_comparisons']
results={}
for mode in ['objects','deduplicated_texts']:
 rows=selected
 if mode=='deduplicated_texts':
  unique={}
  for r in rows:unique.setdefault((r['site'],r['type'],tuple(r['sequence'])),r)
  rows=list(unique.values())
 grouped=defaultdict(list)
 for r in rows:grouped[(r['site'],r['type'],len(r['sequence']))].append(r)
 active={k:v for k,v in grouped.items() if any(chain&set(r['sequence']) for r in v)}
 for label,codes in targets.items():
  probabilities=[];observed=0;records=[]
  for key,members in sorted(active.items()):
   exposed=[r for r in members if chain&set(r['sequence'])]
   assert len(exposed)==1, 'Only handles independently checked one-chain-per-stratum design'
   positives=sum(bool(codes&set(r['sequence'])) for r in members)
   both=int(bool(codes&set(exposed[0]['sequence'])))
   observed+=both
   probabilities.append(Fraction(positives,len(members)))
   records.append({'site':key[0],'type':key[1],'length':key[2],'N':len(members),'target':positives,'chain':1,'both':both,'chain_ids':[exposed[0]['cisi_original']]})
  distribution=defaultdict(Fraction)
  for pattern in product((0,1),repeat=len(probabilities)):
   likelihood=Fraction(1)
   for outcome,p in zip(pattern,probabilities):likelihood*=p if outcome else 1-p
   distribution[sum(pattern)]+=likelihood
  tail=sum((p for n,p in distribution.items() if n>=observed),Fraction())
  mean=sum(probabilities,Fraction())
  ref=expected[label][mode]
  assert records==ref['strata'],(label,mode,'strata discrepancy')
  assert len(rows)==ref['universe_rows']
  assert observed==ref['observed_both']
  assert str(tail)==ref['exact_fraction'],(label,mode,tail,ref['exact_fraction'])
  assert abs(float(mean)-ref['conditional_expected'])<1e-12
  for n,p in distribution.items():assert abs(float(p)-ref['null_distribution'].get(str(n),0))<1e-12
  results.setdefault(label,{})[mode]={'universe_rows':len(rows),'chain_rows':len(probabilities),'observed':observed,'expected_fraction':str(mean),'expected':float(mean),'upper_tail_fraction':str(tail),'upper_tail':float(tail),'strata':records,'binary_patterns_enumerated':2**len(probabilities)}
paths=['data/raw/lipi_inscriptions.csv','data/processed/lipi_strict.jsonl','data/processed/catalogue_features.json','results/pipe_chain_audit.json','scripts/verify_pipe_chain_independent.py']
output={'status':'All eight matched comparisons independently reproduced from source rows; all exact fractions and stratum margins agree.','method':'Separate CSV selection, source-object grouping, and enumeration of all 64 Bernoulli outcomes, using rational arithmetic. Production audit script not read or imported.','comparisons':results,'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
(ROOT/'results/pipe_chain_independent_verification.json').write_text(json.dumps(output,indent=2)+'\n')
print(output['status'])
for k,v in results.items():print(k,{m:r['upper_tail_fraction'] for m,r in v.items()})
