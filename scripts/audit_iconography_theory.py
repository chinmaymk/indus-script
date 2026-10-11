"""Challenge motif-label transfer outside the copper-tablet discovery domain.

Operational model: a bridge singleton, or the complete shared text, always
identifies a motif label observed in its copper bridges. This is deliberately
stronger than 'the sign can mean an animal noun'. No semantic or phonetic values
are imported. This is an exploratory counterexample search, not a held-out
statistical evaluation: the protocol was fixed after seeing the two witnesses.
"""
from collections import Counter, defaultdict
import csv
import json
from common import ROOT, sha256, write_json, write_csv
from prepare_corpora import parse_lipi
from audit_copper_bridges import ABSENT, select_rows, find_bridges

FIELDS = ['id', 'cisi', 'type', 'site', 'condition', 'dir.', 'class', 'signs',
          'complete', 'text', 'symbol', 'cult', 'excavation-idno']


def parse_record(row):
    copy = dict(row)
    if copy['dir.'] == 'NR' and len(copy['text']) == 5:
        copy['dir.'] = 'R/L'
    seq, reasons = parse_lipi(copy)
    artifact = row['cisi'] if row['cisi'] not in ABSENT else 'lipi_id:' + row['id'].split('.')[0]
    return dict(row, artifact=artifact, sequence=seq), reasons


def transfer_scan(rows, bridges):
    sign_labels, text_labels = defaultdict(set), defaultdict(set)
    discovery_artifacts = set()
    for b in bridges:
        sign_labels[b['singleton']].add(b['motif_label'])
        text_labels[tuple(b['shared_sequence'])].add(b['motif_label'])
        discovery_artifacts.update(d['artifact'] for d in b['donors'])
        discovery_artifacts.update(r['artifact'] for r in b['motif_rows'])
    counts, rejected = Counter(), Counter()
    occurrences, witnesses, seen = [], [], set()
    for row in rows:
        record, reasons = parse_record(row)
        if reasons:
            rejected.update(reasons)
            continue
        counts['strict_rows'] += 1
        key = (record['artifact'], tuple(record['sequence']), record['symbol'], record['type'])
        if key in seen:
            counts['duplicate_rows_removed'] += 1
            continue
        seen.add(key)
        counts['unique_artifact_text_label_type_rows'] += 1
        outside = record['type'] != 'TAB:C' and record['artifact'] not in discovery_artifacts
        labelled = record['symbol'] not in ABSENT
        if outside:
            counts['outside_copper_rows'] += 1
            if labelled:
                counts['outside_copper_labelled_rows'] += 1
        matches = [('singleton_presence', s, sign_labels[s])
                   for s in sorted(set(record['sequence']) & set(sign_labels))]
        if tuple(record['sequence']) in text_labels:
            matches.append(('whole_text_equality', ' '.join(record['sequence']),
                            text_labels[tuple(record['sequence'])]))
        for mode, candidate, labels in matches:
            evidence = dict(record, mode=mode, candidate=candidate,
                discovery_labels=sorted(labels), outside_copper=outside,
                motif_label_available=labelled,
                observed_label_in_discovery_set=record['symbol'] in labels if labelled else None)
            occurrences.append(evidence)
            if outside and labelled:
                witnesses.append(evidence)
    coverage = []
    for mode, mapping in [('singleton_presence', sign_labels), ('whole_text_equality', text_labels)]:
        for key, labels in sorted(mapping.items()):
            candidate = ' '.join(key) if isinstance(key, tuple) else key
            matches = [r for r in occurrences if r['mode'] == mode and r['candidate'] == candidate]
            targets = [r for r in matches if r['outside_copper'] and r['motif_label_available']]
            coverage.append({'mode': mode, 'candidate': candidate, 'discovery_labels': sorted(labels),
                'strict_occurrence_artifacts': len({r['artifact'] for r in matches}),
                'outside_copper_occurrence_artifacts': len({r['artifact'] for r in matches if r['outside_copper']}),
                'outside_copper_labelled_artifacts': len({r['artifact'] for r in targets}),
                'outside_labels': sorted({r['symbol'] for r in targets}),
                'new_label_artifacts': len({r['artifact'] for r in targets if not r['observed_label_in_discovery_set']})})
    return {'denominators': dict(counts), 'exclusion_reason_counts_not_disjoint': dict(rejected),
            'candidate_coverage': coverage, 'all_candidate_occurrences': occurrences,
            'transfer_witnesses': witnesses}


def main():
    source = ROOT / 'data/raw/lipi_inscriptions.csv'
    with source.open() as f:
        rows = [{k: r[k].strip() for k in FIELDS} for r in csv.DictReader(f)]
    result = {'source_sha256': sha256(source), 'raw_rows': len(rows),
              'status': 'exploratory counterexample search; no p-values or semantic identification',
              'source_fields': FIELDS, 'analyses': {}}
    for name, quality in [('all_conditions', None), ('good_fair_only', {'Good', 'Fair'})]:
        scope = [r for r in rows if quality is None or r['condition'] in quality]
        selected, _ = select_rows(scope)
        bridges = find_bridges(selected)
        result['analyses'][name] = transfer_scan(scope, bridges)
        result['analyses'][name]['discovery_bridges'] = bridges
    write_json('results/iconography_theory_audit.json', result)
    flat = []
    for name, analysis in result['analyses'].items():
        for row in analysis['candidate_coverage']:
            flat.append(dict(row, quality_filter=name,
                discovery_labels=';'.join(row['discovery_labels']), outside_labels=';'.join(row['outside_labels'])))
    write_csv('results/iconography_theory_coverage.csv', flat)
    print(json.dumps({k: {'denominators': v['denominators'],
                          'witnesses': [(r['candidate'], r['artifact'], r['symbol']) for r in v['transfer_witnesses']]}
                      for k, v in result['analyses'].items()}, indent=2))


if __name__ == '__main__':
    main()
