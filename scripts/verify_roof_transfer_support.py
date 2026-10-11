"""Independent BFS/occurrence-pair reconstruction; imports no producer helpers."""
import json
import hashlib
import re
from pathlib import Path
from collections import defaultdict
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
def label(x):
    s = '' if x is None else str(x).strip()
    return '<unknown>' if s.lower() in {'','<unknown>','unknown','null','none','?'} else s


def main():
    path = 'results/roof_transfer_support.json'
    result = json.loads((ROOT / path).read_text())
    protocol = result['protocol']; pairs = protocol['pairs']
    owner = {p[k]: (i, p['root'], state) for i,p in enumerate(pairs)
             for k,state in [('base',0),('roof',1)]}
    source = [json.loads(s) for s in (ROOT / 'data/processed/m77_candidate_records.jsonl').read_text().splitlines()]
    for r in source:
        assert isinstance(r['source_reference'], str) and r['source_reference'].strip()
        strict = (int(r['source_doc_count']) == 1 and str(r['source_direction_code']) == '1'
                  and len(r['tokens']) >= 2 and not any(t['doubtful'] or t['unknown_span'] for t in r['tokens']))
        assert strict == r['strict_candidate']
    for p,h in result['input_sha256'].items(): assert digest(p) == h, p
    review_paths = ['docs/ROOF_TRANSFER_SUPPORT_DESIGN.md', 'docs/ROOF_TRANSFER_SUPPORT_CODE_REVIEW.md']
    review_pins = 0
    for p in review_paths:
        matches = re.findall(r'`([^`]+)`: SHA256 `([0-9a-f]{64})`', (ROOT / p).read_text())
        assert matches
        for source_path,h in matches:
            assert digest(source_path) == h, source_path
            review_pins += 1
    checks = 0
    for name, branch in result['results'].items():
        raw = [r for r in source if len(r['tokens']) >= 2
               and not any(t['doubtful'] or t['unknown_span'] for t in r['tokens'])
               and (not branch['strict_filter'] or r['strict_candidate'])]
        by_id = {r['id']: r for r in raw}; assert len(by_id) == len(raw)
        keys = defaultdict(set); adjacency = defaultdict(set)
        for r in raw:
            keys[('ref', r['source_reference'])].add(r['id'])
            keys[('seq', tuple('TARGET' if t['sign'] in owner else t['sign'] for t in r['tokens']))].add(r['id'])
        for bucket in keys.values():
            first = min(bucket)
            for rid in bucket: adjacency[first].add(rid); adjacency[rid].add(first)
        remaining = set(by_id); expected_groups = set()
        while remaining:
            todo = [min(remaining)]; seen = set()
            while todo:
                v = todo.pop()
                if v in seen: continue
                seen.add(v); todo.extend(adjacency[v] - seen)
            expected_groups.add(frozenset(seen)); remaining -= seen
        assert {frozenset(c['record_ids']) for c in branch['components']} == expected_groups
        component_of = {rid:c['id'] for c in branch['components'] for rid in c['record_ids']}
        occurrences = {}
        for r in raw:
            for pos,t in enumerate(r['tokens']):
                if t['sign'] not in owner: continue
                pi,root,state = owner[t['sign']]
                oid = f"{r['id']}:{pos}"
                occurrences[oid] = {'component': component_of[r['id']], 'root':root, 'state':state,
                    'stratum': (pi,label(r['site_label_unverified']),label(r['source_object_code']),len(r['tokens']),pos)}
        assert set(occurrences) == {o['id'] for o in branch['occurrences']}
        for o in branch['occurrences']:
            e = occurrences[o['id']]
            assert (o['component'],o['root'],o['state']) == (e['component'],e['root'],e['state'])
            assert (o['pair_index'],o['site_label_unverified'],o['object_code'],o['length'],o['position']) == e['stratum']
        def verify_support(support, root, banned=set()):
            nonlocal checks
            eligible = {k:v for k,v in occurrences.items() if v['root']==root and v['component'] not in banned
                        and (not branch['known_secondary_labels_only'] or '<unknown>' not in v['stratum'][1:3])}
            expected_edges = set()
            for a,b in combinations(eligible.values(),2):
                if a['state'] != b['state'] and a['stratum']==b['stratum'] and a['component']!=b['component']:
                    expected_edges.add(tuple(sorted((a['component'],b['component']))))
            edges = {tuple(e['components']) for e in support['distinct_component_edges']}
            assert edges == expected_edges
            possible = any(len(set(a+b))==4 for a,b in combinations(sorted(edges),2))
            assert possible == support['threshold_pass']
            for edge in support['distinct_component_edges']:
                a,b = eligible[edge['plain_occurrence']],eligible[edge['roof_occurrence']]
                assert a['state']==0 and b['state']==1 and a['stratum']==b['stratum']==tuple(edge['stratum'])
                assert {a['component'],b['component']}==set(edge['components'])
            if possible:
                witness = support['two_disjoint_edges_witness']
                assert len(witness)==2 and len({v for e in witness for v in e['components']})==4
                assert all(tuple(e['components']) in edges for e in witness)
            else: assert support['two_disjoint_edges_witness'] is None
            assert support['occurrences']==len(eligible)
            for state,prefix in [(0,'plain'),(1,'roof')]:
                pool=[v for v in eligible.values() if v['state']==state]
                assert support[prefix+'_occurrences']==len(pool)
                assert support[prefix+'_components']==len({v['component'] for v in pool})
            checks += 1
        marginal = branch['marginal_root_support']
        for root,s in marginal.items(): verify_support(s,root)
        for fold in branch['folds']:
            root=fold['held_out_root']
            banned={o['component'] for o in occurrences.values() if o['root']==root}
            assert set(fold['purged_components'])==banned
            assert fold['held_out_support']==marginal[root]
            for r,s in fold['remaining_training_roots'].items(): verify_support(s,r,banned)
            trained=sorted(r for r,s in fold['remaining_training_roots'].items() if s['threshold_pass'])
            assert fold['training_roots_passing']==trained
            assert fold['proxy_support_gate_pass']==(marginal[root]['threshold_pass'] and len(trained)>=2)
        passing = [r for r,s in marginal.items() if s['threshold_pass']]
        assert branch['summary']['marginal_roots_passing']==sorted(passing)
        # Deleting occurrences only removes possible edges; it cannot create a threshold witness.
        if len(passing)<3: assert not any(f['proxy_support_gate_pass'] for f in branch['folds'])
    assert len(result['signs'])==417 and {s['sign'] for s in result['signs']}=={f'M{i:03d}' for i in range(1,418)}
    assert all(s['semantic_value'] is None and s['phonetic_value'] is None for s in result['signs'])
    out={'verified_root_support_pools':checks,'review_revision_pins_verified':review_pins,
         'strict_flags_independently_reconstructed':len(source), 'independent_grouping':'BFS over reference/formula adjacency',
         'independent_edges':'All opposite-state occurrence pairs', 'all_417_null_values_verified':True,
         'monotonicity_lemma':'Purge removes vertices/edges. A root failing the two-disjoint-edge gate cannot pass after purge. Fewer than three marginally passing roots implies every declared fold fails.',
         'semantic_claim':None,'input_sha256':{p:digest(p) for p in [path,'scripts/verify_roof_transfer_support.py']+review_paths}}
    (ROOT/'results/roof_transfer_support_independent.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'Independent roof support verification: {checks} root pools, four BFS component reconstructions, all417 null values.')


if __name__=='__main__': main()
