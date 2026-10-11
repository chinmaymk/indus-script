"""Descriptive hypothesis checks and sensitivity analyses. No translations assigned."""
from collections import defaultdict,Counter
import json
from common import ROOT, read_jsonl, write_json, write_csv
from analyze_sequences import summarize, permutation_test, Model

# Stroke counts are source-asserted iconographic descriptions, NOT phonetic values.
# Tall/short series remain distinct; no canonical sign substitution is performed.
TALL={'W031':1,'W032':2,'W033':3,'W034':4,'W035':5}
SHORT={'W001':1,'W002':2,'W003':3,'W004':4,'W014':4,'W005':5,'W015':5,
       'W006':6,'W016':6,'W007':7,'W017':7,'W018':8,'W019':9,'W020':10}

def main():
    records=read_jsonl('data/processed/lipi_strict.jsonl')
    seqs=sorted({tuple(r['sequence']) for r in records})
    frames=defaultdict(set)
    for s in seqs:
        for i,x in enumerate(s):
            frames[s[:i]+('?',)+s[i+1:]].add(x)
    tally=[]
    for frame,signs in sorted(frames.items()):
        for name,family in [('tall',TALL),('short',SHORT)]:
            options=sorted(signs & family.keys())
            if len({family[x] for x in options})>=2:
                tally.append({'frame_file_order':' '.join(frame),'family':name,
                    'observed_signs':';'.join(options),'graphic_stroke_counts':';'.join(str(family[x]) for x in options),
                    'interpretation':'quantity-like alternation candidate; no units or phonetic values established'})
    write_csv('results/tally_substitution_frames.csv',tally,
              ['frame_file_order','family','observed_signs','graphic_stroke_counts','interpretation'])
    pair_frames=defaultdict(list)
    for frame, signs in frames.items():
        signs=sorted(signs)
        for i,x in enumerate(signs):
            for y in signs[i+1:]:
                pair_frames[x,y].append(' '.join(frame))
    alternatives=[{'sign_a':a,'sign_b':b,'shared_exact_frames':len(f),'example_frames':' | '.join(f[:5]),
                   'meaning':'substitution compatibility, not synonymy or allography'}
                  for (a,b),f in sorted(pair_frames.items(),key=lambda kv:(-len(kv[1]),kv[0])) if len(f)>=2]
    write_csv('results/substitution_pairs.csv',alternatives)
    freq=Counter(x for s in seqs for x in s)
    tally_stats={name:{'sign_types_present':sum(freq[x]>0 for x in family),
        'tokens_unique_texts':sum(freq[x] for x in family),'source_asserted_stroke_counts':family}
        for name,family in [('tall',TALL),('short',SHORT)]}
    sensitivity={}
    selections={
      'good_fine_only':[r for r in records if r['condition'].strip().lower() in ('good','fine')],
      'complete_preservation_only':[r for r in records if r['preservation'].strip().lower()=='complete'],
      'without_tally_like_signs':[r for r in records if not set(r['sequence']) & (TALL.keys()|SHORT.keys())],
      'Mohenjo-daro':[r for r in records if r['site']=='Mohenjo-daro'],
      'Harappa':[r for r in records if r['site']=='Harappa']}
    for name,subset in selections.items():
        ss=sorted({tuple(r['sequence']) for r in subset})
        sensitivity[name]={'summary':summarize(ss),'permutation_tests':permutation_test(ss,199)}
    # A strict universal fixed length schema is refuted by observed length variation.
    write_json('results/hypothesis_checks.json',{'tally_families':tally_stats,
      'tally_substitution_frames':len(tally),'sensitivity':sensitivity,
      'exactly_five_signs':sum(len(s)==5 for s in seqs),'not_exactly_five_signs':sum(len(s)!=5 for s in seqs),
      'interpretation':'Variable field width/optional fields could still fit; this does not refute every administrative model.'})
    # Explicit constructive counterexample: arbitrary semantic relabeling leaves
    # every probability unchanged when the statistical model is relabeled too.
    alphabet=sorted(freq)
    mapping={x:'arbitrary_label_'+str(i) for i,x in enumerate(alphabet)}
    relabeled=[[mapping[x] for x in s] for s in seqs]
    a=Model(seqs,alphabet,'bigram',20)
    b=Model(relabeled,mapping.values(),'bigram',20)
    diffs=[abs(a.loss(s)-b.loss(t)) for s,t in zip(seqs,relabeled)]
    write_json('results/relabeling_counterexample.json',{'signs':len(alphabet),'sequences':len(seqs),
      'max_absolute_sequence_log_loss_difference_bits':max(diffs),
      'sum_original_loss':sum(a.loss(s) for s in seqs),
      'sum_relabeled_loss':sum(b.loss(t) for t in relabeled),
      'conclusion':'Structural fit does not identify these labels as ancient words or sounds.'})

if __name__=='__main__':
    main()
