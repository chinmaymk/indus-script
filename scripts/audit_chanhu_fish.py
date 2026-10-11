"""Source-qualified Chanhudaro fish incidence; no inferred sign meanings."""
import csv
import json
import re
from collections import Counter, defaultdict
from math import comb
from common import ROOT, sha256, write_json

FIELDS = ('id','cisi','site','excavation-idno','room-grid','type','preservation',
          'complete','condition','depth','phase','text','symbol')


def square(label):
    m = re.search(r'(?<![A-Za-z])sq\s*[.;]?\s*(\d+)\s*/\s*([A-Z])\b', label, re.I)
    return f'{int(m[1])}/{m[2].upper()}' if m else None


def fish_status(rows, codes, include_symbol=False):
    """Positive survives damage elsewhere; unobserved damaged text is unknown."""
    uncertain = False
    for row in rows:
        text = row['text']
        tokens = re.findall(r'(?<!\d)([*?]?)(\d{3})([?]?)(?!\d)', text)
        if any('W'+code in codes and not pre and not post for pre,code,post in tokens):
            return 'positive'
        if include_symbol and re.search(r'\bfish\b', row.get('symbol',''), re.I):
            return 'positive'
        if (row.get('complete') != 'Y' or row.get('preservation') != 'complete'
            or not tokens or any(code == '000' or pre or post for pre,code,post in tokens)
            or any(c in text for c in '[]?*')):
            uncertain = True
    return 'unknown' if uncertain else 'negative'


def summarize(objects, status_key):
    c = Counter(o[status_key] for o in objects)
    n = len(objects)
    return {'n': n, 'positive': c['positive'], 'negative': c['negative'],
            'unknown': c['unknown'],
            'presence_fraction_bounds': [c['positive']/n, (c['positive']+c['unknown'])/n] if n else None,
            'cisi_ids': sorted({x for o in objects for x in o['cisi']})}


def exact_tail(a, b, c, d):
    """One-sided fixed-margin tail: source-exposed descriptive statistic only."""
    if any(not isinstance(x,int) or x < 0 for x in (a,b,c,d)):
        raise ValueError('Nonnegative integer cells required')
    N = a+b+c+d; K = a+c; n = a+b
    if not N or not n or not c+d:
        return None
    return sum(comb(K,j)*comb(N-K,n-j) for j in range(a,min(n,K)+1)
               if 0 <= n-j <= N-K)/comb(N,n)


def comparison(objects, key):
    target = [o for o in objects if o['square'] == '9/D']
    other = [o for o in objects if o['square'] is not None and o['square'] != '9/D']
    t = summarize(target,key); c = summarize(other,key)
    # Complete-status subset only; unknowns and all-object bounds remain visible.
    return {'target':t, 'other_known_squares':c,
            'known_status_only_fixed_margin_tail_NOT_confirmatory':exact_tail(
                t['positive'],t['negative'],c['positive'],c['negative']),
            'unknown_square':summarize([o for o in objects if o['square'] is None],key)}


def main():
    paths = ['data/raw/lipi_inscriptions.csv','data/processed/catalogue_features.json',
             'data/processed/chanhu_fish_protocol.json','data/processed/chanhu_figure5_inventory.json',
             'data/processed/chanhu_primary_review.json']
    protocol = json.loads((ROOT/paths[2]).read_text())
    figure = json.loads((ROOT/paths[3]).read_text())
    primary = json.loads((ROOT/paths[4]).read_text())
    for p in primary['evidence_files']:
        file = ROOT/p['path']
        assert file.stat().st_size == p['bytes'] and sha256(file)==p['sha256'],p['path']
    features = json.loads((ROOT/paths[1]).read_text())
    family = set(protocol['fish_family']['primary'])
    codes = {c for r in features if r['id'] in family for c in r['wells_graphemes']}
    groups = defaultdict(list)
    with (ROOT/paths[0]).open() as f:
        for row in csv.DictReader(f):
            if row['site'] == protocol['site']:
                groups[row['id'].split('.')[0]].append({k:row.get(k,'') for k in FIELDS})
    objects = []
    for identity,rows in sorted(groups.items()):
        squares = {square(r['room-grid']) for r in rows}
        assert len(squares)==1,identity
        objects.append({'secondary_object_id':identity, 'cisi':sorted({r['cisi'] for r in rows}),
                        'rows':rows,'square':next(iter(squares)),
                        'seal_only':all(r['type'].startswith('SEAL:') for r in rows),
                        'fish':fish_status(rows,codes),'plain_fish':fish_status(rows,{'W220'}),
                        'text_or_fish_symbol':fish_status(rows,codes,True),
                        'raw_text_signature':sorted(r['text'] for r in rows)})
    # Separate, reversible overlay: raw source and uncorrected analysis retained.
    overlays = {o['cisi']:o for o in primary['selected_catalogue_location_overlays']}
    revised = json.loads(json.dumps(objects))
    for obj in revised:
        matches=[overlays[c] for c in obj['cisi'] if c in overlays]
        if matches:
            assert len(matches)==1
            obj['original_secondary_square']=obj['square']
            obj['square']=matches[0]['catalogue_square']
            obj['location_overlay']=matches[0]
    results={}
    for label,cohort in [('secondary_raw',objects),('selected_primary_location_overlay',revised)]:
        result={}
        for kind,selected in [('all_types',cohort),('seal_prefix_only',[o for o in cohort if o['seal_only']])]:
            result[kind]={key:comparison(selected,key) for key in ['fish','plain_fish','text_or_fish_symbol']}
            restricted=[o for o in selected if o['square'] and 7<=int(o['square'].split('/')[0])<=10
                        and o['square'].split('/')[1] in 'BCDEF']
            result[kind]['restricted_grid_fish']=comparison(restricted,'fish')
            result[kind]['by_square']={sq:summarize([o for o in selected if o['square']==sq],'fish')
                                      for sq in sorted({o['square'] for o in selected if o['square']})}
            documented = set(primary['craft_controls']['explicit_beadworking_squares'])
            result[kind]['retrospective_documented_square_sensitivity'] = {
                'status':'Exploratory coarse square labels; complement is unclassified, not non-beadworking.',
                'explicitly_named_beadworking_squares':summarize(
                    [o for o in selected if o['square'] in documented],'fish'),
                'other_named_beadworking_squares_excluding_9D':summarize(
                    [o for o in selected if o['square'] in documented-{'9/D'}],'fish'),
                'other_known_squares_NOT_negative_controls':summarize(
                    [o for o in selected if o['square'] and o['square'] not in documented],'fish')}
        results[label]=result
    figure_squares=defaultdict(lambda:{'ids':[],'orange_ids':[]})
    for panel in figure['panels']:
        figure_squares[panel['square']]['ids'].extend(panel['cisi_ids'])
        if panel['orange_fish_border']:
            figure_squares[panel['square']]['orange_ids'].extend(panel['cisi_ids'])
    for s in figure_squares.values():
        s['n_ids']=len(set(s['ids']));s['n_orange']=len(set(s['orange_ids']))
    discrepancies=[]
    byc={c:o for o in objects for c in o['cisi']}
    for sq,group in figure_squares.items():
        for cid in group['ids']:
            if cid not in byc:discrepancies.append({'cisi':cid,'reason':'absent from exact secondarysite export'})
            elif byc[cid]['square']!=sq:
                discrepancies.append({'cisi':cid,'figure_square':sq,'secondary_square':byc[cid]['square']})
    output={'protocol':protocol,'summary':{'secondary_objects':len(objects),
              'secondary_rows':sum(len(o['rows']) for o in objects),'fish_codes':sorted(codes),
              'figure9D':figure_squares['9/D'],'established_semantic_values':0,'established_phonetic_values':0},
            'results':results,'secondary_objects':objects,'selected_primary_overlay_objects':revised,
            'figure_by_square':dict(figure_squares),'figure_secondary_discrepancies':discrepancies,
            'primary_review':primary,'input_sha256':{p:sha256(ROOT/p) for p in paths},
            'limits':['Rawmetadata and glyphs incompletely authenticated; selective overlays do not validate remaining controls.',
                      'Other squares contain beadworking; comparison is spatial incidence, not craft specificity.',
                      'Source-exposed examples and boundaries; tails are conditional descriptive summaries, not confirmatory significance.',
                      'Missing primary fragment CH2558 has unknown text and is not silently added to secondarytranscription.']}
    write_json('results/chanhu_fish_audit.json',output)
    print(json.dumps({'summary':output['summary'],'raw_seals':results['secondary_raw']['seal_prefix_only']['fish'],
                      'overlay_seals':results['selected_primary_location_overlay']['seal_prefix_only']['fish']},indent=2))


if __name__ == '__main__':main()
