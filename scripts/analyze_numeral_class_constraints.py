"""Exact graph of pure stroke-class equalities; no numerical reading inferred."""
import json
from fractions import Fraction as F
from collections import defaultdict, deque
from common import ROOT, sha256, write_json


def classify(tokens):
    parts=[]
    for token in tokens:
        n=int(token[1:])
        if 31<=n<=39: parts.append(('long',n-30))
        elif 1<=n<=7: parts.append(('short',n))
        elif 12<=n<=19: parts.append(('stacked',n-10))
        else: return None
    if not parts or len({p[0] for p in parts})!=1: return None
    return parts[0][0],sum(p[1] for p in parts)


def solve(edges):
    graph=defaultdict(list)
    for i,e in enumerate(edges):
        u,v=e['nodes'];r=F(*e['counts'])
        graph[u].append((v,r,i));graph[v].append((u,1/r,i))
    values={};components=[];conflicts=[]
    for root in sorted(graph):
        if root in values: continue
        values[root]=F(1);queue=deque([root]);members=[]
        while queue:
            u=queue.popleft();members.append(u)
            for v,r,i in graph[u]:
                expected=values[u]*r
                if v not in values:
                    values[v]=expected;queue.append(v)
                elif values[v]!=expected:
                    conflicts.append({'edge_index':i,'cisi':edges[i]['cisi'],
                                      'from':u,'to':v,'existing':str(values[v]),'required':str(expected)})
        components.append(sorted(members))
    return {'positive_solution_exists':not conflicts,
            'normalized_component_values':{k:str(v) for k,v in sorted(values.items())} if not conflicts else None,
            'connected_components':components,
            'free_positive_scales_if_consistent':len(components) if not conflicts else None,
            'conflicts':conflicts}


def main():
    path='results/numeral_pair_screen.json'
    screen=json.loads((ROOT/path).read_text())['screens']['allow_LR_sensitivity']
    edges=[];excluded=[]
    for row in screen['records']:
        if not row['eligible']:
            excluded.append({'cisi':row['cisi'],'reason':'outside_frozen_screen_eligibility','details':row['exclusion_reasons']})
            continue
        fields=[classify(row['faces'][m]['left']+row['faces'][m]['right']) for m in ('W700','W840')]
        if any(f is None for f in fields):
            excluded.append({'cisi':row['cisi'],'reason':'mixed_or_nonstroke_expression_not_a_single_ratio_edge'})
            continue
        edges.append({'cisi':row['cisi'],'group_id':row['group_id'],
                      'nodes':[m+':'+f[0] for m,f in zip(('W700','W840'),fields)],
                      'counts':[f[1] for f in fields],
                      'numeric_pair_signature':row['numeric_pair_signature']})
    all_result=solve(edges)
    without_h1923=[e for e in edges if e['cisi']!=['H-1923']]
    limited=solve(without_h1923)
    assert len(edges)==5 and not all_result['positive_solution_exists']
    assert len(without_h1923)==4 and limited['positive_solution_exists']
    v=limited['normalized_component_values']
    assert F(v['W700:long'])==1 and F(v['W840:long'])==F(3,2) and F(v['W840:stacked'])==1
    # Artificially identifying stacked and long recreates the stronger failure.
    collapsed=[{**e,'nodes':[n.replace(':stacked',':long') for n in e['nodes']]} for e in without_h1923]
    collapsed_result=solve(collapsed)
    assert not collapsed_result['positive_solution_exists']
    write_json('results/numeral_class_constraints.json',{
        'scope':'Conditional equality graph from the frozen parser; values are effective class-and-marker contributions, not decoded numerals.',
        'node_definition':'Positive value per stroke conditional on graphic class and marker context.',
        'all_candidate_groups':len(screen['records']), 'eligible_frozen_groups':sum(r['eligible'] for r in screen['records']),
        'pure_class_edges':edges,'excluded_from_ratio_graph':excluded,
        'all_source_records':all_result,
        'without_unverified_H1923':{'edges':without_h1923,**limited},
        'without_H1923_but_equating_long_and_stacked':collapsed_result,
        'implied_W840_stacked_over_long_without_H1923':str(F(v['W840:stacked'])/F(v['W840:long'])),
        'limitations':[
            'This does not establish equal represented quantities across faces or the meanings of either marker.',
            'Dropping H1923 is an explicit source-sensitivity calculation, not deletion or evidence that its transcription is wrong.',
            'H326,H924,H925 repeat the same numeric pattern and do not supply three independent ratio constraints.',
            'Compatibility of a more flexible class-context model is not positive evidence for it.',
            'H904 is mixed and not expressible as one graph edge; its existing conditional equation is retained elsewhere.',
            'Graph consistency is not a fit to all417 signs or to excluded corpus records.',
        ],
        'semantic_values_assigned':0,
        'input_sha256':{p:sha256(ROOT/p) for p in [path,'scripts/screen_numeral_pairs.py','docs/NUMERAL_IMAGES.md']},
    })
    print('Class-context graph: 5 edges; contradiction with H1923, compatible without it; imposed class merger restores contradiction.')


if __name__=='__main__':main()
