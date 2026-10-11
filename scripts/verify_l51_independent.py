"""Independently reconstruct L51 counts; enumerate 512 stratum outcomes exactly.

Does not import audit_l51 or its helpers. Production output is loaded only after
all independent calculations, for comparison. This is a consistency check, not
independent corpus transcription or validation of a proposed semantic value.
"""
import csv
import hashlib
import itertools
import json
import re
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text())

def h(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def main():
    protocol = load('data/processed/l51_protocol.json')
    catalogue = load('data/processed/catalogue_features.json')
    fish = set()
    for family in catalogue:
        if family['id'] in protocol['fish_family_ids']:
            fish.update(family['wells_graphemes'])
    targets = {'fish': fish, 'plain_fish': {'W220'},
               'U': set(protocol['U_candidates'])}
    targets['fish_or_U'] = fish | targets['U']
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open() as f:
        # Do not import translation or Sanskrit fields.
        fields = ('id','cisi','site','type','text','complete','preservation','dir.')
        raw = [{k:r[k] for k in fields} for r in csv.DictReader(f)]
    strict = {json.loads(line)['id'] for line in
              (ROOT/'data/processed/lipi_strict.jsonl').read_text().splitlines()}
    groups = Counter(r['id'].split('.')[0] for r in raw)
    universe = []
    for row in raw:
        if (row['id'] in strict and groups[row['id'].split('.')[0]] == 1
                and row['complete'] == 'Y' and row['preservation'] == 'complete'
                and row['type'].startswith('SEAL')):
            assert re.fullmatch(r'\+\d{3}(?:-\d{3})*\+', row['text'])
            seq = tuple('W'+t for t in row['text'][1:-1].split('-'))
            assert not {'W000','W999'} & set(seq)
            if len(seq) >= 2:
                universe.append(dict(row, seq=seq))
    dedup = {}
    for row in universe:
        dedup.setdefault((row['site'],row['type'],row['seq']), row)
    branches = {'objects':universe, 'text_types':list(dedup.values()),
                'same_W527_terminal_objects':[r for r in universe if r['seq'][0]=='W527']}
    computed = {}
    for target, codes in targets.items():
        computed[target] = {}
        for branch, rows in branches.items():
            strata = defaultdict(list)
            for r in rows:
                strata[(r['site'],r['type'],len(r['seq']))].append(r)
            active=[]
            for key, members in sorted(strata.items()):
                exposed=[r for r in members if r['seq'][:2]==('W527','W555')]
                if not exposed:
                    continue
                assert len(exposed)==1
                K=sum(bool(codes & set(r['seq'])) for r in members)
                active.append({'key':key, 'N':len(members), 'K':K,
                               'observed':int(bool(codes & set(exposed[0]['seq']))),
                               'exposed':exposed[0]['cisi'],
                               'controls':[r['cisi'] for r in members if r not in exposed]})
            assert len(active)==9
            observed=sum(s['observed'] for s in active)
            expected=sum((Fraction(s['K'],s['N']) for s in active), Fraction())
            total=Fraction(); tail=Fraction()
            for bits in itertools.product((0,1), repeat=len(active)):
                p=Fraction(1)
                for bit,s in zip(bits,active):
                    p *= Fraction(s['K'] if bit else s['N']-s['K'],s['N'])
                total += p
                if sum(bits)>=observed:
                    tail += p
            assert total == 1
            computed[target][branch]={'universe_rows':len(rows),'ending_rows':len(active),
                'observed_both':observed,'expected_exact':str(expected),
                'conditional_expected':float(expected),'exact_fraction':str(tail),
                'upper_tail_descriptive_only':float(tail),'active_strata':active,
                'binary_patterns_enumerated':2**len(active)}
    raw_rows = [r for r in raw if r['type'].startswith('SEAL')
                and re.match(r'^\+527-555(?:-|\+|\[)',r['text'])]
    raw_counts={}
    raw_statuses={}
    for target,codes in targets.items():
        statuses={}
        for r in raw_rows:
            codes_here={'W'+x for x in re.findall(r'(?<![\d?*/])(\d{3})(?![\d?*/])',r['text'])}
            intact_text=(r['complete']=='Y' and
                re.fullmatch(r'\+\d{3}(?:-\d{3})*\+',r['text']) and
                not ({'W000','W999'} & codes_here))
            statuses[r['cisi']]='positive' if codes_here & codes else 'negative' if intact_text else 'unknown'
        raw_counts[target]={k:list(statuses.values()).count(k) for k in ['positive','negative','unknown']}
        raw_statuses[target]=statuses
    # Compare independently calculated objects with saved production output.
    production=load('results/l51_audit.json')
    assert sorted(fish)==production['fish_codes']
    for target,branches_result in computed.items():
        for branch,calc in branches_result.items():
            actual=production['matched'][target][branch]
            for key in ['universe_rows','ending_rows','observed_both','exact_fraction']:
                assert calc[key]==actual[key],(target,branch,key,calc[key],actual[key])
            assert abs(calc['conditional_expected']-actual['conditional_expected'])<1e-12
        for key in ['positive','negative','unknown']:
            assert raw_counts[target][key]==production['raw_summaries'][target][key]
    assert {r['cisi'] for r in raw_rows}=={r['cisi'] for r in production['raw_ending_rows']}
    conservative = dict(raw_statuses['fish_or_U'])
    for row in raw_rows:
        if conservative[row['cisi']] == 'negative' and row['preservation'] != 'complete':
            conservative[row['cisi']] = 'unknown'
    conservative_counts = {k:list(conservative.values()).count(k) for k in ['positive','negative','unknown']}
    result={'method':'Independent CSV reconstruction and exact enumeration of512 binary stratum outcomes; no production imports',
        'comparison_passed':True,'matched':computed,'raw_counts':raw_counts,'raw_statuses':raw_statuses,
        'conservative_preservation_sensitivity':{'counts':conservative_counts,'known_only_fraction':str(Fraction(conservative_counts['positive'],conservative_counts['positive']+conservative_counts['negative']))},
        'raw_union_known_only_fraction':str(Fraction(raw_counts['fish_or_U']['positive'],raw_counts['fish_or_U']['positive']+raw_counts['fish_or_U']['negative'])),
        'cautions':['Production text-completeness rule counts M821 as negative despite fragmentary object preservation; original-text completeness requires primary inspection.',
                    '11/13 excludes one unknown; denominator is not specified by published claim. All14 gives observed11/14.',
                    'Exact enumeration verifies arithmetic and operationalization, not semantic specificity.'],
        'inputs':{p:h(p) for p in ['data/raw/lipi_inscriptions.csv','data/processed/lipi_strict.jsonl','data/processed/catalogue_features.json','data/processed/l51_protocol.json','results/l51_audit.json','scripts/verify_l51_independent.py']}}
    (ROOT/'results/l51_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'comparison_passed':True,'raw_counts':raw_counts,'matched_checks':12},indent=2))

if __name__=='__main__':
    main()
