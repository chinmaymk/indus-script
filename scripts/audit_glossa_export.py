"""Audit local Glossa export provenance without downloading or merging namespaces."""
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
import tarfile

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def encoded_mayig(sequence):
    # Namespace stays Parpola; only formatting changes, no sign-ID crosswalk.
    assert all(re.fullmatch(r'P\d{3}', token) for token in sequence)
    return '+' + '-'.join(token[1:] for token in sequence) + '+'


def summarize(rows):
    texts = Counter(r['icit_text'] for r in rows)
    ids = defaultdict(list)
    for row in rows:
        ids[row['icit_text']].append(row['glossa_id'])
    return {
        'rows': len(rows), 'unique_exact_texts': len(texts),
        'duplicate_excess': len(rows) - len(texts),
        'rows_in_repeated_text_groups': sum(n for n in texts.values() if n > 1),
        'declared_sign_count_sum': sum(r['sign_count'] for r in rows),
        'unique_glossa_ids': len({r['glossa_id'] for r in rows}),
        'site_labels': dict(Counter(str(r['site_name']) for r in rows)),
        'artifact_type_labels': dict(Counter(r['artifact_type'] for r in rows)),
        'rights_labels_as_claimed': dict(Counter(r['rights_status'] for r in rows)),
        'rows_containing_000': sum('000' in r['icit_text'].split('-') or
                                   bool(re.search(r'(?<!\d)000(?!\d)', r['icit_text'])) for r in rows),
        'rows_containing_asterisk': sum('*' in r['icit_text'] for r in rows),
        'rows_containing_double_plus': sum('++' in r['icit_text'] for r in rows),
        'rows_not_simple_three_digit_single_line': sum(not re.fullmatch(r'\+\d{3}(?:-\d{3})*\+', r['icit_text']) for r in rows),
        'duplicate_groups': [{'icit_text': text, 'count': count, 'glossa_ids': ids[text]}
                             for text, count in sorted(texts.items()) if count > 1],
    }


def main():
    export_path = 'data/raw/glossa_icit_export.json'
    data = json.loads((ROOT / export_path).read_text())
    rows = data['sequences']
    groups = defaultdict(list)
    for row in rows:
        groups[(row['source_system'], row['sign_id_scheme'])].append(row)
    mayig_raw = []
    with tarfile.open(ROOT / 'data/raw/mayig_corpus.tar.gz') as archive:
        for member in sorted(archive.getmembers(), key=lambda m: m.name):
            if member.isfile() and '/corpus/' in member.name and member.name.endswith('.json'):
                for obj in json.load(archive.extractfile(member)):
                    mayig_raw.append({'id': obj['id'], 'source_path': member.name,
                                      'text': encoded_mayig([g['id'] for g in obj['graphemes']])})
    mayig_strict = [json.loads(line) for line in (ROOT / 'data/processed/mayig_strict.jsonl').read_text().splitlines()]
    raw_counts = Counter(r['text'] for r in mayig_raw)
    strict_counts = Counter(encoded_mayig(r['sequence']) for r in mayig_strict)
    exported_mayig = groups[('mayig-cisi', 'Parpola1982')]
    export_counts = Counter(r['icit_text'] for r in exported_mayig)
    witnesses = []
    for row in exported_mayig:
        witnesses.append({'glossa_id': row['glossa_id'], 'icit_text': row['icit_text'],
                          'same_namespace_raw_text_matches': [r for r in mayig_raw if r['text'] == row['icit_text']]})
    tree = json.loads((ROOT / 'data/raw/glossa_lab_tree.json').read_text())
    selected_paths = [r for r in tree['tree'] if r['path'] in {
        'glossa-corpus/indus/README.md', 'glossa-corpus/indus/exports/indus_icit_format.json',
        'data/import/mahadevan_m77_raw.txt', 'scripts/build_corpus_pipeline.py',
        'glossa-corpus/indus/sources/batch_mayig_2026-05-14.json',
        'glossa-corpus/indus/canonical/objects.jsonl'}]
    sources = [fingerprint(p) for p in [export_path, 'data/raw/glossa_README.md',
               'data/raw/glossa_lab_tree.json', 'data/raw/glossa_lab_main_commit.json',
               'data/raw/mayig_corpus.tar.gz', 'data/processed/mayig_strict.jsonl']]
    export_tree = next(r for r in selected_paths if r['path'].endswith('/indus_icit_format.json'))
    table_path = 'data/processed/mahadevan_1977_table_i.csv'
    primary = list(csv.DictReader((ROOT / table_path).open()))
    primary_counts = {r['sign'][1:]: int(r['total']) for r in primary}
    m77_rows = groups[('indusscript-m77', 'Mahadevan1977')]
    literal_tokens = Counter(token for row in m77_rows for token in row['icit_text'][1:-1].split('-'))
    # Asterisk removal is ONLY an explicit sensitivity tally, not a clean transcription.
    numeric_tokens = Counter()
    for token, count in literal_tokens.items():
        if re.fullmatch(r'\*?\d{3}', token):
            numeric_tokens[token.lstrip('*')] += count
    frequency_rows = [{'sign': 'M' + token, 'primary_table_total': count,
                       'export_unstarred': literal_tokens[token],
                       'export_starred': literal_tokens['*' + token],
                       'export_combined_sensitivity': numeric_tokens[token],
                       'combined_minus_primary': numeric_tokens[token] - count}
                      for token, count in sorted(primary_counts.items())]
    invalid_tokens = {token: count for token, count in literal_tokens.items()
                      if not re.fullmatch(r'\*?\d{3}', token)}
    out_of_range = {token: count for token, count in numeric_tokens.items()
                    if token != '000' and token not in primary_counts}
    count_mismatches = [row['glossa_id'] for row in m77_rows
                       if sum(token.lstrip('*') != '000' for token in row['icit_text'][1:-1].split('-')) != row['sign_count']]
    sources.append(fingerprint(table_path))
    result = {
        'protocol': {'new_downloads': False, 'comparison': 'Exact encoded text within declared namespace; keep asterisks, damage, and boundaries unchanged',
                     'mayig_formatting': 'Remove P prefix from exactly Pddd tokens and wrap with +/hyphens; no numeric crosswalk, reversal, or sorting',
                     'duplicates_mean': 'Repeated encoded sequences, not demonstrated duplicate artifacts',
                     'independence_limit': 'Same underlying artifacts may overlap across corpora; distinct rows and source labels do not establish independent observations'},
        'input_fingerprints': sources,
        'export_metadata': {k: v for k, v in data.items() if k != 'sequences'},
        'counts': {'declared_sequences': data['total_sequences'], 'observed_rows': len(rows),
                   'declared_sign_count_sum': sum(r['sign_count'] for r in rows),
                   'namespace_qualified_unique_texts': len({(r['sign_id_scheme'], r['icit_text']) for r in rows})},
        'source_groups': [{'source_system': source, 'sign_id_scheme': scheme, **summarize(group)}
                          for (source, scheme), group in sorted(groups.items())],
        'mayig_comparison': {'raw_rows': len(mayig_raw), 'raw_unique_texts': len(raw_counts),
                            'export_text_multiset_equals_raw': export_counts == raw_counts,
                            'strict_rows': len(mayig_strict), 'strict_unique_texts': len(strict_counts),
                            'strict_rows_accounted_for_with_multiplicity': sum((strict_counts & export_counts).values()),
                            'raw_export_rows_beyond_strict_multiset': sum((export_counts - strict_counts).values()),
                            'witnesses': witnesses},
        'readme_claim': {'source': 'data/raw/glossa_README.md', 'section': 'Corpus Note',
                         'name': 'Holdat LLC Indus Corpus v3 (Miller 2025)',
                         'objects': 1670, 'tokens': 7002, 'distinct_signs': 390, 'sites': 9,
                         'publicly_available_claim': False},
        'm77_frequency_diagnostic': {
            'primary_source': table_path, 'primary_table_signs': len(primary_counts),
            'primary_table_total_tokens': sum(primary_counts.values()),
            'all_literal_token_slots': sum(literal_tokens.values()),
            'unknown_000_slots': numeric_tokens['000'],
            'named_sign_slots_including_starred_sensitivity': sum(n for token, n in numeric_tokens.items() if token != '000'),
            'starred_slots': sum(n for token, n in literal_tokens.items() if token.startswith('*')),
            'distinct_named_codes_including_starred': sum(token != '000' for token in numeric_tokens),
            'invalid_literal_token_shapes': invalid_tokens,
            'nonzero_codes_outside_primary_table_inventory': out_of_range,
            'declared_sign_count_mismatch_glossa_ids': count_mismatches,
            'signs_absent_in_export': [row['sign'] for row in frequency_rows if row['export_combined_sensitivity'] == 0],
            'sign_counts_equal_primary_with_starred_sensitivity': sum(row['combined_minus_primary'] == 0 for row in frequency_rows),
            'signs_exceeding_primary_count_even_unstarred': [row for row in frequency_rows if row['export_unstarred'] > row['primary_table_total']],
            'signs_exceeding_primary_count_with_starred_sensitivity': [row for row in frequency_rows if row['combined_minus_primary'] > 0],
            'frequencies': frequency_rows,
            'interpretation': 'Diagnostic within the source-claimed M77 namespace, not a crosswalk or authentication. Asterisk meanings and damage conventions are not established here. Subset selection can reduce totals; counts above the primary table flag a nonliteral-subset relationship or differences in convention, counting, or transcription. No exact-match expectation.'},
        'm77_object_identity': {
            'row_keys': sorted({key for row in m77_rows for key in row}),
            'unique_glossa_ids': len({row['glossa_id'] for row in m77_rows}),
            'id_examples': [m77_rows[0]['glossa_id'], m77_rows[-1]['glossa_id']],
            'original_artifact_or_excavation_id_fields': [],
            'assessment': 'Export has unique Glossa row identifiers, some embedding an M77-like numeric reference, but no explicit original reference, excavation number, artifact/side link, image, or per-row citation. Stability across releases and original-source identity cannot be established from this snapshot.'},
        'upstream_tree': {'sha': tree['sha'], 'truncated': tree.get('truncated'),
                          'selected_entries': selected_paths,
                          'export_git_blob_hash_matches_tree': sources[0]['git_blob_sha1'] == export_tree['sha'],
                          'limitation': 'Tree records file paths and hashes, not un-downloaded file contents; no ingest code or canonical object-level lineage has been inspected here'},
        'conclusion': 'Public export is labelled a mixed mayig/Mahadevan reconstruction, not identified as the private 1670-object Holdat corpus. Its 179 mayig text rows reproduce the existing raw mayig multiset exactly. M77 extraction lineage and artifact overlaps remain unauthenticated; retain this component as a provisional avenue for primary transcription checks, not an adopted corpus. ICIT-format syntax does not make these Wells/ICIT sign numbers or an official ICIT corpus.'
    }
    (ROOT / 'data/processed/glossa_export_review.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k in ('counts', 'conclusion')}, indent=2))
    for g in result['source_groups']:
        print(json.dumps({k: v for k, v in g.items() if k != 'duplicate_groups'}))
    print('Mayig multiset equality:', export_counts == raw_counts)
    print('Strict subset:', len(mayig_strict), sum((strict_counts & export_counts).values()))
    print('Git blob match:', result['upstream_tree']['export_git_blob_hash_matches_tree'])


if __name__ == '__main__':
    main()
