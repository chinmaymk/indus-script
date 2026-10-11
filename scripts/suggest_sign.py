"""Rank a single missing Wells/ICIT sign by structural compatibility, not translation.

Example: python3 scripts/suggest_sign.py 'W740 ? W033'
Order must match the source CSV (apparently left-to-right display order).
Excludes all training texts matching the observed mask, plus their artifact groups.
"""
import argparse
import json
import re
from common import read_jsonl
from analyze_sequences import Model,grouped_records

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sequence',help='Space-separated W codes and exactly one ?')
    parser.add_argument('--top',type=int,default=10)
    args=parser.parse_args()
    seq=args.sequence.split()
    if seq.count('?')!=1 or any(x!='?' and not re.fullmatch(r'W\d{3}',x) for x in seq):
        parser.error('Use exactly one ? and Wells identifiers such as W740.')
    vocab=[f'W{i:03d}' for i in range(1,999)]
    if any(x!='?' and x not in vocab for x in seq):
        parser.error('W000 and W999 are not treated as signs.')
    grouped=grouped_records(read_jsonl('data/processed/lipi_strict.jsonl'))
    excluded={r['group'] for r in grouped if len(r['sequence'])==len(seq)
              and all(x=='?' or x==y for x,y in zip(seq,r['sequence']))}
    train=[r['sequence'] for r in grouped if r['group'] not in excluded]
    model=Model(train,vocab,'bigram',20)
    idx=seq.index('?');scores=[]
    for x in vocab:
        candidate=seq.copy();candidate[idx]=x
        scores.append((model.loss(candidate),x))
    scores.sort()
    floor=scores[0][0]
    weights=[2**(floor-loss) for loss,x in scores]
    total=sum(weights)
    print(json.dumps({'warning':'Statistical suggestions only. Conditional weights are not calibrated epigraphic probabilities.',
      'source_file_order':seq,'excluded_groups':len(excluded),'training_unique_texts':len(train),
      'ranked_candidates':[{'sign':x,'relative_model_weight':w/total} for (loss,x),w in zip(scores[:args.top],weights[:args.top])]},indent=2))

if __name__=='__main__':
    main()
