"""Test the evidential scope of the published crab/crab-fish comparison."""
import csv
import json
from collections import Counter
from common import ROOT,read_jsonl,sha256,write_json
from audit_hind_leg_hypothesis import occurrences,FIELDS


def scan(rows,strict_ids,codes):
    hits=[]
    for row in rows:
        for h in occurrences(row['text'],codes):
            following=h['file_left'] if row['dir.']=='R/L' and h['file_left']!='W000' else None
            hits.append(dict({k:row.get(k,'') for k in FIELDS},**h,
                following_in_reported_RL=following,
                strict=row['id'] in strict_ids,
                named_in_selected_argument=row['cisi'] in ('M-57','M-387')))
    return hits


def suffix_cases(records,prefix=('W226','W032')):
    output=[]
    for r in records:
        seq=tuple(r['sequence'])
        if seq[:len(prefix)]==prefix and len(seq)>len(prefix):
            output.append(dict(r,next_one_after_file_prefix=seq[len(prefix)],
                next_two_after_file_prefix=list(seq[len(prefix):len(prefix)+2]),
                interpretation='File prefix corresponds to reading suffix only for reported R/L; no equality of preceding expressions'))
    return output


def main():
    raw='data/raw/lipi_inscriptions.csv';strictpath='data/processed/lipi_strict.jsonl'
    protocol='data/processed/crab_fish_protocol.json';featurepath='data/processed/catalogue_features.json'
    expansion='results/composite_expansion_audit.json'
    primarypath='data/processed/crab_fish_primary_review.json'
    primary=json.loads((ROOT/primarypath).read_text())
    for pin in primary['evidence_files']:
        p=ROOT/pin['path'];assert p.stat().st_size==pin['bytes'] and sha256(p)==pin['sha256']
    rows=list(csv.DictReader((ROOT/raw).open()));strict=read_jsonl(strictpath)
    strictids={r['id'] for r in strict};byid={r['id']:r for r in rows}
    mainhits=scan(rows,strictids,{'798'});related=scan(rows,strictids,{'193','797'})
    features=json.loads((ROOT/featurepath).read_text())
    fish_entries={'P050','P051'}|{f'P{i:03d}' for i in range(56,65)}
    fish_codes=sorted({c for f in features if f['id'] in fish_entries for c in f['wells_graphemes']})
    cases=suffix_cases(strict)
    for r in cases:r['reported_direction']=byid[r['id']]['dir.']
    exact_pair=[h for h in mainhits if h['following_in_reported_RL']=='W231']
    strict_pair=[h for h in exact_pair if h['strict']]
    expanded=json.loads((ROOT/expansion).read_text())
    full_matches={label:[m for m in b['matches'] if m['target']=='M053' and m['replacement'] in
                 (['M053','M070'],['M070','M053'])] for label,b in expanded['results'].items()}
    summary={'all_raw_rows':len(rows),'main_occurrences':len(mainhits),
        'main_distinct_rows':len({h['id'] for h in mainhits}),
        'strict_main_occurrences':sum(h['strict'] for h in mainhits),
        'main_RL_following_codes':dict(sorted(Counter(h['following_in_reported_RL'] for h in mainhits if h['following_in_reported_RL']).items())),
        'main_RL_W231':sum(h['following_in_reported_RL']=='W231' for h in mainhits),
        'main_RL_W231_strict_rows':len(strict_pair),
        'main_RL_W231_strict_distinct_texts':len({h['text'] for h in strict_pair}),
        'main_RL_W231_strict_distinct_texts_outside_named_pair':len({h['text'] for h in strict_pair if not h['named_in_selected_argument']}),
        'main_RL_W220':sum(h['following_in_reported_RL']=='W220' for h in mainhits),
        'main_RL_selected_fish_family':sum(h['following_in_reported_RL'] in fish_codes for h in mainhits),
        'strict_suffix_cases':len(cases),
        'strict_suffix_next_one_codes':dict(sorted(Counter(h['next_one_after_file_prefix'] for h in cases).items())),
        'strict_suffix_distinct_next_pairs':len({tuple(h['next_two_after_file_prefix']) for h in cases if len(h['next_two_after_file_prefix'])==2}),
        'strict_suffix_good_fair_fine_cases':sum(h['condition'] in ('Good','Fair','Fine') for h in cases),
        'full_M77_matches':{k:len(v) for k,v in full_matches.items()}}
    write_json('results/crab_fish_audit.json',{'protocol':json.loads((ROOT/protocol).read_text()),
        'summary':summary,'main_occurrences':mainhits,'related_not_merged':related,
        'fish_family_sensitivity_codes':fish_codes,'suffix_cases':cases,'full_M77_matches':full_matches,
        'primary_review':primary,
        'input_sha256':{p:sha256(ROOT/p) for p in (raw,strictpath,protocol,featurepath,expansion,primarypath)},
        'established_semantic_values':0,'established_phonetic_values':0,
        'limits':['Secondary-export counts, not full historical-corpus counts or accepted aliases.',
                  'Source-exposed examples are not held-out semantic predictions.',
                  'Shared suffix does not require synonymy; full-context absence is not refutation.']})
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
