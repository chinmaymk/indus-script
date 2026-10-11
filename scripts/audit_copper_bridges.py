"""Find literal text bridges between copper-tablet motifs and singleton reverses.

This is an exploratory source audit, not a translation or independence test.
Only named input columns are imported; no proposed language readings are used.
"""
from collections import Counter, defaultdict
import csv
import json
from common import ROOT, sha256, write_json, write_csv
from prepare_corpora import parse_lipi

ABSENT = {'', '-', '--', '?', 'None', 'Unknown'}


def select_rows(rows, quality=None):
    selected, excluded = [], []
    for row in rows:
        if row['type'].strip() != 'TAB:C':
            continue
        copy = dict(row)
        # A singleton has no order to reverse; NR is allowed only for that case.
        if row['dir.'].strip() == 'NR' and len(row['text']) == 5:
            copy['dir.'] = 'R/L'
        seq, reasons = parse_lipi(copy)
        if row['site'].strip() != 'Mohenjo-daro':
            reasons.append('site_not_Mohenjo-daro')
        if quality is not None and row['condition'].strip() not in quality:
            reasons.append('quality_filter')
        artifact = row['cisi'].strip()
        if artifact in ABSENT:
            artifact = 'lipi_id:' + row['id'].split('.')[0]
        record = {k: row[k].strip() for k in
                  ['id', 'cisi', 'text', 'symbol', 'cult', 'condition', 'dir.']}
        record.update(artifact=artifact, sequence=seq)
        if reasons:
            excluded.append(dict(record, reasons=reasons))
        else:
            selected.append(record)
    return selected, excluded


def find_bridges(rows):
    """Require two distinct source sides; retain every witness, deduplicate counts."""
    artifacts = defaultdict(list)
    by_text = defaultdict(list)
    for row in rows:
        artifacts[row['artifact']].append(row)
        if len(row['sequence']) > 1 and row['symbol'] not in ABSENT:
            by_text[tuple(row['sequence'])].append(row)
    groups = {}
    for artifact, sides in sorted(artifacts.items()):
        # No motif-bearing side may act as a text-only donor.
        if any(side['symbol'] not in ABSENT for side in sides):
            continue
        singletons = [s for s in sides if len(s['sequence']) == 1]
        texts = [s for s in sides if len(s['sequence']) > 1]
        if len(singletons) != 1 or len(texts) != 1:
            continue
        singleton, text = singletons[0], texts[0]
        if singleton['id'] == text['id']:
            continue
        for target in by_text[tuple(text['sequence'])]:
            if target['artifact'] == artifact:
                continue
            key = (singleton['sequence'][0], tuple(text['sequence']), target['symbol'])
            entry = groups.setdefault(key, {
                'singleton': key[0], 'shared_sequence': list(key[1]),
                'motif_label': key[2], 'donors': {}, 'motif_rows': {}})
            entry['donors'][artifact] = {'artifact': artifact,
                'singleton_id': singleton['id'], 'text_id': text['id'],
                'condition': [singleton['condition'], text['condition']]}
            entry['motif_rows'][target['id']] = target
    result = []
    for key in sorted(groups):
        entry = groups[key]
        entry['donors'] = list(entry['donors'].values())
        entry['motif_rows'] = list(entry['motif_rows'].values())
        entry['donor_artifact_count'] = len(entry['donors'])
        entry['motif_artifact_count'] = len({r['artifact'] for r in entry['motif_rows']})
        result.append(entry)
    return result


def main():
    source = ROOT / 'data/raw/lipi_inscriptions.csv'
    fields = ['id', 'cisi', 'type', 'site', 'condition', 'dir.', 'class',
              'signs', 'complete', 'text', 'symbol', 'cult']
    with source.open() as f:
        rows = [{k: r[k] for k in fields} for r in csv.DictReader(f)]
    outputs = {}
    for name, quality in [('all_conditions', None), ('good_fair_only', {'Good', 'Fair'})]:
        kept, excluded = select_rows(rows, quality)
        bridges = find_bridges(kept)
        labels = defaultdict(set)
        for bridge in bridges:
            labels[bridge['singleton']].add(bridge['motif_label'])
        outputs[name] = {'selected_rows': len(kept), 'excluded_rows': excluded,
            'bridge_count': len(bridges), 'bridges': bridges,
            'singleton_to_source_labels': {s: sorted(v) for s, v in sorted(labels.items())}}
    ledger = json.loads((ROOT / 'data/processed/copper_types_2008.json').read_text())
    if sha256(ROOT / ledger['source']) != ledger['sha256']:
        raise ValueError('Type ledger source hash mismatch')
    totals = Counter()
    for row in ledger['types']:
        totals[row['type'][0]] += row['count']
    outputs['type_ledger_audit'] = {'subtype_rows': len(ledger['types']),
        'count_totals': dict(totals), 'sum': sum(totals.values()),
        'matches_reported_shape_totals': dict(totals) == ledger['reported_shape_totals']}
    outputs['source_sha256'] = sha256(source)
    outputs['scope'] = ('Exact source-code and file-order matches only. Catalogued TAB:C '
        'need not equal the author’s incised-tablet definition. Shared texts connect '
        'objects; they do not establish synonymous reverses, phonetic values, '
        'independence of source readings, or the ancient meaning of a motif label.')
    write_json('results/copper_bridge_audit.json', outputs)
    flat = []
    for name in ['all_conditions', 'good_fair_only']:
        for b in outputs[name]['bridges']:
            flat.append({'filter': name, 'singleton': b['singleton'],
                'shared_sequence': ' '.join(b['shared_sequence']),
                'motif_label': b['motif_label'],
                'donor_artifacts': ';'.join(x['artifact'] for x in b['donors']),
                'motif_artifacts': ';'.join(sorted({x['artifact'] for x in b['motif_rows']}))})
    write_csv('results/copper_bridges.csv', flat,
              ['filter','singleton','shared_sequence','motif_label','donor_artifacts','motif_artifacts'])
    print(json.dumps({k: {'selected_rows': v['selected_rows'],
                         'bridge_count': v['bridge_count'],
                         'singleton_labels': v['singleton_to_source_labels']}
                      for k, v in outputs.items() if 'selected_rows' in v}, indent=2))


if __name__ == '__main__':
    main()
