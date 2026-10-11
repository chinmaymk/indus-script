"""Enumerate bounded roof-extension candidates without translating or joining them.

Exact existing W rows and native M endpoint records are independent sections.
Source pins are fixed from the preceding candidate audit; source changes fail
rather than silently extending this frozen enumeration.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'data/raw/lipi_inscriptions.csv': {
        'bytes': 1204921,
        'sha256': 'b8dcb325a2e2cd3cde12ac12e7a418b0348e45713c9ee28aad81b645d2ac5ee4'},
    'data/processed/m77_candidate_records.jsonl': {
        'bytes': 4109921,
        'sha256': 'b29a176da86b125115256a8966c377c3fd9fe39ecaab17bf576b770b83b41bab'},
}
W_TARGETS = ['W678', 'W391', 'W731', 'W044']
M_ENDPOINTS = ['M138', 'M163', 'M334', 'M092']
EXCLUDED_COLUMNS = {'sanskrit', 'translation', 'notes'}
NATIVE_FIELDS = ['id', 'source_reference', 'namespace', 'diplomatic', 'tokens',
                 'source_doc_count', 'source_direction_code', 'primary_direction_definition',
                 'source_object_code', 'primary_object_definition', 'upstream_artifact_type',
                 'site_label_unverified', 'source_extra', 'source_citation', 'strict_candidate',
                 'exclusion_reasons', 'order', 'authentication']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source_checks = []
    for name, pin in SOURCES.items():
        path = ROOT / name
        check = {'path': name, **pin, 'sha256_matches': sha(path) == pin['sha256'],
                 'bytes_match': path.stat().st_size == pin['bytes']}
        source_checks.append(check)
        assert check['sha256_matches'] and check['bytes_match'], name
    raw_rows, supplemental = [], []
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open(newline='') as handle:
        reader = csv.DictReader(handle)
        retained_columns = [k for k in reader.fieldnames if k not in EXCLUDED_COLUMNS]
        for line_number, row in enumerate(reader, 2):
            # Digit boundaries retain alternatives, breaks and punctuation literally.
            # Neither language/translation columns nor free-form notes select a row.
            hits = [{'code': 'W' + m.group(), 'raw_digits': m.group(),
                     'text_character_span_zero_based': [m.start(), m.end()]}
                    for m in re.finditer(r'(?<!\d)\d{3}(?!\d)', row['text'])]
            wanted = [h for h in hits if h['code'] in W_TARGETS]
            extra = row['cisi'] == 'M-354' and any(h['code'] == 'W729' for h in hits)
            if not wanted and not extra:
                continue
            entry = {'csv_row_number_including_header': line_number,
                     'raw': {key: row[key] for key in retained_columns},
                     'queried_code_hits': wanted if wanted else [h for h in hits if h['code'] == 'W729'],
                     'scope': 'Raw source row; no physical identity, token equivalence or completeness adjudication'}
            if wanted:
                raw_rows.append(entry)
            if extra:
                supplemental.append(entry)
    assert len(raw_rows) == 15
    assert len(supplemental) == 1 and supplemental[0]['raw']['id'] == '2850.1'
    assert len({r['raw']['id'] for r in raw_rows}) == 15
    assert supplemental[0]['raw']['id'] not in {r['raw']['id'] for r in raw_rows}
    by_w = {code: [r['raw']['id'] for r in raw_rows if any(h['code'] == code for h in r['queried_code_hits'])]
            for code in W_TARGETS}
    native_rows = []
    with (ROOT / 'data/processed/m77_candidate_records.jsonl').open() as handle:
        for line in handle:
            record = json.loads(line)
            hits = [{'code': token['sign'], 'token_index_zero_based': index,
                     'doubtful': token['doubtful'], 'unknown_span': token['unknown_span']}
                    for index, token in enumerate(record['tokens']) if token['sign'] in M_ENDPOINTS]
            if hits:
                native_rows.append({'native_record': {key: record[key] for key in NATIVE_FIELDS},
                                    'endpoint_hits': hits,
                                    'scope': 'Existing native candidate record; source flags retained, not a new primary re-reading'})
    by_m = {code: [{'record_id': r['native_record']['id'],
                   'source_reference': r['native_record']['source_reference'],
                   'target_positions_zero_based': [h['token_index_zero_based'] for h in r['endpoint_hits'] if h['code'] == code]}
                  for r in native_rows if any(h['code'] == code for h in r['endpoint_hits'])]
            for code in M_ENDPOINTS}
    review_paths = ['docs/ROOF_CROSS_COVERAGE_EXTENSION.md', 'docs/ROOF_X_IDENTITY_REVIEW.md',
                    'docs/ROOF_TRIDENT_CANDIDATE_AUDIT.md', 'docs/ROOF_NONFISH_VARIANT_REVIEW.md',
                    'docs/ROOF_M092_ARTIFACT_REVIEW.md']
    result = {'schema_version': 1,
              'scope': 'Bounded source enumeration for integration; no inferred W-to-M joins or new attestations.',
              'selection': {'raw_W_targets': W_TARGETS, 'supplement': 'W729 on source CISI label M-354 only',
                            'native_M_endpoints': M_ENDPOINTS,
                            'raw_selection_column': 'text', 'raw_supplement_label_column': 'cisi',
                            'translation_columns_used': False, 'excluded_raw_columns': sorted(EXCLUDED_COLUMNS),
                            'retained_raw_columns': retained_columns},
              'raw_W_rows': raw_rows, 'raw_W_row_ids_by_target': by_w,
              'supplemental_W729_M354_rows': supplemental,
              'native_endpoint_records': native_rows, 'native_endpoints': by_m,
              'summary': {'raw_target_rows': len(raw_rows), 'raw_target_rows_by_code': {k: len(v) for k, v in by_w.items()},
                          'supplemental_rows': len(supplemental), 'total_distinct_raw_rows': len(raw_rows) + len(supplemental),
                          'native_records': len(native_rows), 'native_records_by_endpoint': {k: len(v) for k, v in by_m.items()}},
              'join_policy': 'The W and M sections are enumerated independently. No sequence resemblance, number suffix, feature-family label or shared target code creates an identity join. Consult cited review documents for their individually scoped findings.',
              'review_references_only': [{'path': p, 'sha256': sha(ROOT / p)} for p in review_paths],
              'source_integrity_checks': source_checks,
              'enumerator_sha256': sha(Path(__file__)),
              'limits': ['Raw preservation, complete and condition values can disagree; no flag is repaired.',
                         'Numeric catalogue namespaces remain separate, including W391 versus M391.',
                         'Native endpoint records can contain other doubtful signs or lost spans; all flags remain literal.',
                         'Source rows and references are not independently counted physical artifacts or dies.',
                         'This enumeration neither adds candidates to a frozen test nor assigns eligibility or newness.'],
              'new_downloads': [], 'corpus_edits': [], 'established_semantic_values': 0, 'established_phonetic_values': 0}
    destination = ROOT / 'results/roof_extension_candidates.json'
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
