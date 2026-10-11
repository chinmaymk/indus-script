"""Source-exposed ending follow-up: named-example exclusion and exact counterparts."""
import csv
import json
from collections import Counter,defaultdict
from common import ROOT,sha256,read_jsonl,write_json
from audit_pipe_chain import FIELDS
from audit_l51 import conditioned,is_ending


def without_second(seq):
    if not is_ending(seq):
        return None
    return seq[:1]+seq[2:]


def main():
    paths=['data/processed/ending_validation_protocol.json','results/l51_audit.json',
           'data/raw/lipi_inscriptions.csv','data/processed/lipi_strict.jsonl',
           'data/processed/ending_india_review.json',
           'data/processed/ending_mapping_review.json',
           'data/processed/m77_candidate_strict.jsonl',
           'data/processed/ending_pakistan_review.json']
    protocol=json.loads((ROOT/paths[0]).read_text())
    prior=json.loads((ROOT/paths[1]).read_text())
    with (ROOT/paths[2]).open() as f:raw=[{k:r.get(k,'') for k in FIELDS} for r in csv.DictReader(f)]
    byid={r['id']:r for r in raw};counts=Counter(r['id'].split('.')[0] for r in raw)
    universe=[]
    for r in read_jsonl(paths[3]):
        source=byid[r['id']]
        if (counts[r['id'].split('.')[0]]==1 and source['complete']=='Y'
            and source['preservation']=='complete' and source['type'].startswith('SEAL')
            and len(r['sequence'])>=2):universe.append(dict(source,sequence=r['sequence']))
    index=defaultdict(list)
    for r in universe:index[tuple(r['sequence'])].append(r)
    pair_rows=[]
    for r in universe:
        reduced=without_second(r['sequence'])
        if reduced is not None:
            matches=index[tuple(reduced)]
            pair_rows.append({'with_W555':r,'exact_reduced_sequence':reduced,
                              'without_W555_matches':matches,
                              'same_site_matches':sum(m['site']==r['site'] for m in matches),
                              'same_site_and_type_matches':sum(m['site']==r['site'] and m['type']==r['type'] for m in matches)})
    excluded=set(protocol['known_named_examples'])
    leave=[r for r in universe if r['cisi'] not in excluded]
    fish=set(prior['fish_codes']);U={'W705','W706'}
    targets={'fish':fish,'plain_fish':{'W220'},'U':U,'fish_or_U':fish|U}
    other=[r for r in universe if len(r['sequence'])>1 and r['sequence'][1]=='W555' and r['sequence'][0]!='W527']
    alternate_matches=[{'other_first_token':r,'W527_full_context_matches':index[tuple(['W527']+r['sequence'][1:])]}
                       for r in other]
    india=json.loads((ROOT/paths[4]).read_text())
    mapping=json.loads((ROOT/paths[5]).read_text())
    pakistan=json.loads((ROOT/paths[7]).read_text())
    for review in [india,mapping,pakistan]:
        for pin in review['evidence_files']:
            assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
            assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
    damaged={r['cisi'].replace('-','') for r in india['objects']
             if r.get('gross_text_bearing_corner_loss')}
    screened=[r for r in alternate_matches if r['other_first_token']['cisi'].replace('-','') not in damaged]
    m77=[r for r in read_jsonl(paths[6]) if r['sequence'][-2:]==['M222','M254']]
    output={'protocol':protocol,'universe_rows':len(universe),
            'excluded_rows':[r for r in universe if r['cisi'] in excluded],
            'retrospective_leave_named_out':{t:conditioned(leave,cs) for t,cs in targets.items()},
            'exact_counterparts':pair_rows,
            'other_first_tokens_before_W555':other,
            'alternate_first_token_full_context_matches':alternate_matches,
            'alternate_pairs_after_reviewed_damage_exclusion':screened,
            'damage_screen_scope':'Retrospective exclusion of visually flagged L9; remaining M934 is not thereby primary-authenticated',
            'primary_mapping_review':mapping,
            'M77_candidate_ending_rows':m77,
            'M77_census_scope':'Source-exposed candidate transcription census; overlapping artifacts and selected examples, not an independent replication',
            'summary':{'ending_cases':len(pair_rows),
                       'cases_with_exact_counterpart':sum(bool(r['without_W555_matches']) for r in pair_rows),
                       'distinct_reduced_strings_with_counterpart':len({tuple(r['exact_reduced_sequence']) for r in pair_rows if r['without_W555_matches']}),
                       'alternate_ending_rows':len(other),'alternate_first_token_counts':dict(Counter(r['sequence'][0] for r in other))},
            'input_sha256':{p:sha256(ROOT/p) for p in paths},
            'established_semantic_values':0,'established_phonetic_values':0}
    write_json('results/ending_validation_audit.json',output)
    print(json.dumps(output['summary'],indent=2))
    for t,r in output['retrospective_leave_named_out'].items():print(t,{k:v for k,v in r.items() if k!='strata'})
    for r in pair_rows:
        if r['without_W555_matches']:print('COUNTERPART',r['with_W555']['cisi'],[(m['cisi'],m['text']) for m in r['without_W555_matches']])


if __name__=='__main__':main()
