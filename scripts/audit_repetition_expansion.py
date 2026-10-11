"""Screen A^n versus stroke-group(n),A with exact surrounding strings.

An observed substitution is not an equation or established equivalence. Enumerate
every alternative X,A and A,X too, so a selected stroke match is not privileged.
Use complete undoubted candidate strings without filling gaps or merging lines.
"""
from collections import Counter, defaultdict
import json
from common import ROOT, read_jsonl, sha256, write_json

# Graphic multiplicities, not assigned numerical values. Distinct forms retained.
MARKERS = {2: {'M087':'long','M099':'short_high','M100':'short_low'},
           3: {'M089':'long','M102':'short'},
           4: {'M095':'long','M104':'short'}}


def maximal_runs(seq):
    i=0
    while i<len(seq):
        j=i+1
        while j<len(seq) and seq[j]==seq[i]:
            j+=1
        if j-i>=2:
            yield i,j,seq[i]
        i=j


def rewrite_matches(sequences, markers=MARKERS, alphabet=None):
    """Sequences maps tuples to reference lists. No observed count weighting."""
    if alphabet is None:
        alphabet=sorted({s for seq in sequences for s in seq})
    runs=[]; matches=[]
    for seq in sorted(sequences):
        for i,j,sign in maximal_runs(seq):
            n=j-i
            run={'expanded_sequence':list(seq),'expanded_references':sorted(sequences[seq]),
                 'target':sign,'run_start':i,'run_length':n,
                 'prefix':list(seq[:i]),'suffix':list(seq[j:]),
                 'outside_context_length':len(seq)-n}
            runs.append(run)
            if n not in markers:
                continue
            for order in ['before','after']:
                for marker in alphabet:
                    replacement=(marker,sign) if order=='before' else (sign,marker)
                    alternative=seq[:i]+replacement+seq[j:]
                    if alternative==seq or alternative not in sequences:
                        continue
                    matches.append(dict(run, replacement_sign=marker,replacement_order=order,
                                        alternative_sequence=list(alternative),
                                        alternative_references=sorted(sequences[alternative]),
                                        graphic_count_match=marker in markers[n],
                                        marker_form=markers[n].get(marker)))
    return runs,matches


def corpus(records, strict=False):
    out=defaultdict(list);excluded=Counter();included=0
    for r in records:
        if any(t['doubtful'] or t['unknown_span'] for t in r['tokens']):
            excluded['any_doubt_or_loss']+=1
            continue
        if strict and not r['strict_candidate']:
            excluded['not_strict_candidate']+=1
            continue
        seq=tuple(t['sign'] for t in r['tokens'])
        if not seq:
            excluded['empty']+=1
            continue
        out[seq].append(r['source_reference']);included+=1
    return dict(out),included,dict(excluded)


def summarize(records, strict):
    seqs,n,excluded=corpus(records,strict)
    runs,matches=rewrite_matches(seqs)
    selected=[m for m in matches if m['graphic_count_match']]
    per_sign=[]
    for i in range(1,418):
        sign=f'M{i:03d}'
        sign_runs=[r for r in runs if r['target']==sign]
        sign_matches=[m for m in selected if m['target']==sign]
        per_sign.append({'sign':sign,'observed_maximal_runs_in_distinct_strings':len(sign_runs),
                         'run_lengths':dict(sorted(Counter(r['run_length'] for r in sign_runs).items())),
                         'selected_matches':sign_matches,'established_meaning':None})
    return {'included_records':n,'distinct_strings':len(seqs),'excluded':excluded,
            'maximal_runs':len(runs),'run_length_counts':dict(sorted(Counter(r['run_length'] for r in runs).items())),
            'target_signs_with_runs':len({r['target'] for r in runs}),
            'all_alternative_matches':len(matches),'selected_matches_count':len(selected),
            'selected_matches_with_nonempty_context':sum(m['outside_context_length']>0 for m in selected),
            'selected_matches':selected,'alternative_matches':matches,'runs':runs,'signs':per_sign}


def main():
    path='data/processed/m77_candidate_records.jsonl'
    observations='data/processed/m77_repetition_primary_review.json'
    records=read_jsonl(path)
    review=json.loads((ROOT/observations).read_text())
    for source in review['sources']:
        if sha256(ROOT/source['path'])!=source['sha256']:
            raise ValueError('Changed primary evidence: '+source['path'])
    byref={r['source_reference']:r for r in records}
    for r in review['primary_lines']:
        candidate=byref[r['reference']]
        if [t['sign'] for t in candidate['tokens']]!=r['sequence']:
            raise ValueError('Primary/candidate sequence mismatch: '+r['reference'])
        if candidate['source_direction_code']!=r['direction_code']:
            raise ValueError('Primary/candidate direction mismatch: '+r['reference'])
    results={'complete_undoubted_export':summarize(records,False),
             'strict_candidate_sensitivity':summarize(records,True)}
    write_json('results/repetition_expansion_audit.json',{
        'inputs_sha256':{p:sha256(ROOT/p) for p in [path,observations]},
        'graphic_marker_map':MARKERS,'selection':'Maximal runs; n=2,3,4; both marker orders; exact whole remaining string; unique string weighting.',
        'results':results,'primary_review':observations,
        'limits':['No semantic equality follows from occupying the same frame.',
                  'Markers are grouped only by visible stroke number for this hypothesis, not merged as allographs or assigned values.',
                  'The exported strings are a selected, partly authenticated subset with known omitted lines.',
                  'All417 target codes are indexed; zero observations are not evidence of no meaning.',
                  'Discovery is exploratory, with many tested signs/frames. No null significance or decipherment coverage is asserted.',
                  'Empty frames and different object types or directions weaken an equivalence claim.',
                  'The primary fish pair has different site headings and field-symbol codes.'],
        'established_semantic_or_phonetic_values':0})
    for label,result in results.items():
        print(label,json.dumps({k:v for k,v in result.items() if k not in ['selected_matches','alternative_matches','runs','signs']}))


if __name__=='__main__':
    main()
