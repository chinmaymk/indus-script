"""Source-exposed context descriptions for W525/W526/W527; no allography claim."""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from common import ROOT, read_jsonl, sha256, write_json

CODES = ('W525', 'W526', 'W527')


def positions(sequence, code):
    reading = sequence[::-1]
    n = len(reading)
    return [{'reading_index_zero_based': i, 'offset_from_reading_end': n - 1 - i,
             'relative_position': 'singleton' if n == 1 else str(Fraction(i, n - 1)),
             'category': 'singleton' if n == 1 else 'initial' if i == 0 else 'final' if i == n - 1 else 'medial'}
            for i, token in enumerate(reading) if token == code]


def exact_counterparts(sequence_index):
    output = []
    for sequence in sorted(sequence_index):
        for i, token in enumerate(sequence):
            if token != 'W525':
                continue
            for alternate in ('W526', 'W527'):
                changed = sequence[:i] + (alternate,) + sequence[i + 1:]
                if changed not in sequence_index:
                    continue
                output.append({'alternative_code': alternate,
                               'source_file_position_zero_based': i,
                               'reading_position_zero_based': len(sequence) - 1 - i,
                               'W525_sequence': list(sequence), 'alternative_sequence': list(changed),
                               'W525_rows': sequence_index[sequence], 'alternative_rows': sequence_index[changed]})
    return output


def describe_position_records(records):
    return {field: dict(sorted(Counter(str(p[field]) for p in records).items()))
            for field in ('reading_index_zero_based', 'offset_from_reading_end', 'relative_position', 'category')}


def shared_strata(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row['site'], row['type'], len(row['sequence']))].append(row)
    strata = []
    for (site, kind, length), group in sorted(grouped.items()):
        sides = {}
        for name, codes in [('W525', ('W525',)), ('W526_or_W527', ('W526', 'W527'))]:
            members = [r for r in group if set(codes).intersection(r['sequence'])]
            sides[name] = {'row_count': len(members), 'distinct_strings': len({tuple(r['sequence']) for r in members}),
                           'rows': members,
                           'form_counts': {c: sum(c in r['sequence'] for r in members) for c in codes},
                           'position_categories': dict(Counter(p['category'] for r in members for c in codes
                                                              for p in positions(r['sequence'], c)))}
        strata.append({'site': site, 'type': kind, 'token_length': length, **sides,
                       'shared': all(side['row_count'] > 0 for side in sides.values())})
    shared = [s for s in strata if s['shared']]
    return {'strata': strata, 'observed_strata': len(strata), 'shared_strata': len(shared),
            'coverage': {side: {'all_rows': sum(s[side]['row_count'] for s in strata),
                               'rows_in_shared_strata': sum(s[side]['row_count'] for s in shared),
                               'distinct_strings_within_shared_strata': sum(s[side]['distinct_strings'] for s in shared)}
                         for side in ('W525', 'W526_or_W527')}}


def main():
    paths = ['data/processed/comb_family_context_protocol.json', 'data/processed/lipi_strict.jsonl']
    protocol = json.loads((ROOT / paths[0]).read_text())
    corpus = read_jsonl(paths[1])
    index = defaultdict(list)
    for row in corpus:
        index[tuple(row['sequence'])].append(row)
    summaries = {}
    for code in CODES:
        rows = [row for row in corpus if code in row['sequence']]
        groups = [seq for seq in index if code in seq]
        metadata = {field: dict(sorted(Counter(row.get(field, '') for row in rows).items()))
                    for field in ('site', 'type', 'preservation')}
        label_sets = {field: dict(sorted(Counter(
            json.dumps(sorted({row.get(field, '') for row in index[seq]})) for seq in groups).items()))
            for field in ('site', 'type', 'preservation')}
        row_positions = [p for row in rows for p in positions(row['sequence'], code)]
        string_positions = [p for seq in groups for p in positions(seq, code)]
        summaries[code] = {'row_count': len(rows), 'occurrences': len(row_positions),
                           'distinct_whole_strings': len(groups),
                           'all_rows': {'metadata_row_counts': metadata,
                                        'occurrence_position_counts': describe_position_records(row_positions)},
                           'one_per_distinct_whole_string': {
                               'occurrences': len(string_positions),
                               'metadata_label_set_counts': label_sets,
                               'occurrence_position_counts': describe_position_records(string_positions)}}
    selected = [row for row in corpus if set(CODES).intersection(row['sequence'])]
    distinct_groups = [{'sequence': list(seq), 'rows': index[seq],
                        'observed_metadata_label_sets': {field: sorted({r.get(field, '') for r in index[seq]})
                                                        for field in ('site', 'type', 'preservation')},
                        'positions_by_code': {c: positions(seq, c) for c in CODES if c in seq}}
                       for seq in sorted(index) if set(CODES).intersection(seq)]
    pairs = exact_counterparts(index)
    mixed = [r for r in selected if len(set(CODES).intersection(r['sequence'])) > 1]
    repeated = [r for r in selected if any(r['sequence'].count(c) > 1 for c in CODES)]
    w525_without_h1123 = [r for r in selected if 'W525' in r['sequence'] and r['cisi_original'] != 'H-1123']
    w525_without_h1123_strings = {tuple(r['sequence']) for r in w525_without_h1123}
    result = {'protocol': protocol, 'strict_corpus_rows': len(corpus),
              'summary_by_code': summaries,
              'selected_rows': selected, 'distinct_sequence_groups': distinct_groups,
              'exact_counterpart_sequence_pairs': pairs,
              'counterpart_summary': {alt: {'distinct_sequence_pairs': sum(p['alternative_code'] == alt for p in pairs),
                  'W525_row_ids': sorted({r['id'] for p in pairs if p['alternative_code'] == alt for r in p['W525_rows']}),
                  'alternative_row_ids': sorted({r['id'] for p in pairs if p['alternative_code'] == alt for r in p['alternative_rows']})}
                  for alt in ('W526', 'W527')},
              'multiple_distinct_form_rows': mixed,
              'multiple_distinct_form_sequence_groups': [g for g in distinct_groups if len(set(CODES).intersection(g['sequence'])) > 1],
              'repeated_same_form_rows': repeated,
              'repeated_same_form_sequence_groups': [g for g in distinct_groups if any(g['sequence'].count(c) > 1 for c in CODES)],
              'shared_site_type_length_strata': shared_strata(selected),
              'retrospective_H1123_exclusion_strata': shared_strata([r for r in selected if r['cisi_original'] != 'H-1123']),
              'retrospective_H1123_exclusion_W525_distribution': {
                  'rows': w525_without_h1123, 'row_count': len(w525_without_h1123),
                  'distinct_whole_strings': len(w525_without_h1123_strings),
                  'all_row_positions': describe_position_records([p for r in w525_without_h1123 for p in positions(r['sequence'], 'W525')]),
                  'distinct_string_positions': describe_position_records([p for seq in w525_without_h1123_strings for p in positions(seq, 'W525')]),
                  'metadata_row_counts': {field: dict(sorted(Counter(r[field] for r in w525_without_h1123).items()))
                                          for field in ('site', 'type', 'preservation')}},
              'source_label_cautions': [{'id': '313.1', 'cisi_original': 'H-1123',
                  'scope': 'Retained in main source-labelled analysis; unresolved excavation/plate identity conflict documented in docs/W525_PRIMARY_REVIEW.md. Source preservation is not corrected. Exclusion only in explicitly retrospective stratum sensitivity.'}],
              'input_sha256': {p: sha256(ROOT / p) for p in paths},
              'established_semantic_values': 0, 'established_phonetic_values': 0,
              'global_allography_promotions': 0}
    write_json('results/comb_family_contexts.json', result)
    print(json.dumps({'signs': {c: {k: summaries[c][k] for k in ('row_count', 'occurrences', 'distinct_whole_strings')} for c in CODES},
                      'counterparts': result['counterpart_summary'],
                      'mixed_rows': len(mixed), 'repeated_form_rows': len(repeated)}, indent=2))


if __name__ == '__main__':
    main()
