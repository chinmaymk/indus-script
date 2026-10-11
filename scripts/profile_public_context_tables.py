"""Metadata-only feasibility profile; never imports sign/translation columns.

External scripts are evidence to inspect, not code to execute. Joins normalize only
case and whitespace and are provisional catalogue-key agreements, not identities.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'data/raw/public-context-oct11-'
LIPI_COLUMNS = ('id', 'cisi', 'site', 'excavation-idno')
MISSING = {'', '-', '--', '?', 'NONE', 'UNKNOWN'}


def normalized(value):
    return ''.join(str(value).upper().split())


def present(value):
    return normalized(value) not in MISSING


def numeric(value):
    try:
        return math.isfinite(float(value))
    except (ValueError, TypeError):
        return False


def read_rows(path, columns=None):
    with path.open(newline='') as handle:
        reader = csv.DictReader(handle)
        if columns and not set(columns).issubset(reader.fieldnames or []):
            raise ValueError('Missing required whitelisted metadata column')
        # Discard non-whitelisted fields immediately; never retain or process them.
        return [{key: row[key] for key in columns} if columns else row
                for row in reader]


def artifact_key(row):
    if present(row['cisi']):
        return row['cisi'].strip()
    if not present(row['id']):
        return None
    return 'lipi_id:' + row['id'].split('.')[0].strip()


def profile(rows, identifier):
    grouped = defaultdict(list)
    for row in rows:
        if present(row[identifier]):
            grouped[normalized(row[identifier])].append(row)
    return {
        'rows': len(rows), 'nonmissing_unique_identifier_keys': len(grouped),
        'missing_identifier_rows': [r for r in rows if not present(r[identifier])],
        'duplicate_identifier_keys': {k: v for k, v in sorted(grouped.items()) if len(v) > 1},
        'column_nonmissing_counts': {key: sum(present(r[key]) for r in rows)
                                     for key in (rows[0] if rows else [])},
    }


def join_mackay(mackay, lipi):
    md = [dict(r) for r in lipi if r['site'] == 'Mohenjo-daro']
    tables, fields = defaultdict(list), defaultdict(list)
    artifact_fields = defaultdict(set)
    for row in mackay:
        if present(row['field_no']):
            tables[normalized(row['field_no'])].append(row)
    for row in md:
        if present(row['excavation-idno']):
            key = normalized(row['excavation-idno'])
            fields[key].append(row)
            if artifact_key(row):
                artifact_fields[artifact_key(row)].add(key)
    artifact_conflicts = {k: sorted(v) for k, v in sorted(artifact_fields.items()) if len(v) > 1}
    joined, rejected = [], []
    for key, table_rows in sorted(tables.items()):
        witnesses = fields.get(key, [])
        artifacts = {artifact_key(r) for r in witnesses}
        reasons = []
        if len(table_rows) != 1:
            reasons.append('nonunique_mackay_field_key')
        if not witnesses:
            reasons.append('no_exact_lipi_field_match')
        elif None in artifacts or len(artifacts) != 1:
            reasons.append('missing_or_multiple_lipi_artifact_keys')
        elif next(iter(artifacts)) in artifact_conflicts:
            reasons.append('lipi_artifact_has_multiple_field_keys')
        record = {'normalized_field_key': key, 'mackay_rows': table_rows,
                  'lipi_rows': witnesses}
        if reasons:
            rejected.append({**record, 'reasons': reasons})
        else:
            row = table_rows[0]
            joined.append({**record, 'artifact_key': next(iter(artifacts)),
                'has_locus': any(present(row[k]) for k in ('block', 'house', 'room', 'street')),
                'has_raw_numeric_depth': numeric(row['level_ft'])})
    return {
        'lipi_mohenjo_daro_rows': len(md),
        'lipi_nonmissing_field_keys': len(fields),
        'mackay_nonmissing_field_keys': len(tables),
        'mackay_duplicate_field_key_count': sum(len(v) > 1 for v in tables.values()),
        'exact_field_key_overlap': len(set(fields) & set(tables)),
        'raw_field_examples_separate_not_identity_pairs': {
            'mackay': [r['field_no'] for r in mackay[:15]],
            'lipi_mohenjo_daro': [r['excavation-idno'] for r in md[:15]],
        },
        'eligible_join_count': len(joined),
        'eligible_locus_and_raw_numeric_depth_count': sum(r['has_locus'] and r['has_raw_numeric_depth'] for r in joined),
        'eligible_join_areas_from_raw_field_prefix': dict(sorted(Counter(
            r['mackay_rows'][0]['field_no'].split()[0] for r in joined).items())),
        'eligible_locus_depth_areas_from_raw_field_prefix': dict(sorted(Counter(
            r['mackay_rows'][0]['field_no'].split()[0] for r in joined
            if r['has_locus'] and r['has_raw_numeric_depth']).items())),
        'eligible_joins': joined, 'rejected_table_keys': rejected,
        'mackay_missing_field_rows': [r for r in mackay if not present(r['field_no'])],
        'lipi_missing_field_rows': [r for r in md if not present(r['excavation-idno'])],
        'lipi_field_keys_absent_from_mackay': {k: v for k, v in sorted(fields.items()) if k not in tables},
        'lipi_field_keys_multiple_artifacts': {k: v for k, v in sorted(fields.items())
            if len({artifact_key(r) for r in v}) > 1 or any(artifact_key(r) is None for r in v)},
        'lipi_artifact_keys_multiple_fields': artifact_conflicts,
    }


def main():
    names = {'mackay': PREFIX + 'mackay-seal-table.csv',
             'marshall': PREFIX + 'marshall-seal-table.csv',
             'findspots': PREFIX + 'findspots-mackay.csv',
             'lipi': 'data/raw/lipi_inscriptions.csv'}
    tables = {key: read_rows(ROOT / path, LIPI_COLUMNS if key == 'lipi' else None)
              for key, path in names.items()}
    sources = list(names.values()) + [PREFIX + suffix for suffix in
        ('datasets.md', 'build-mackay-table.py', 'license-data.txt', 'commit.json')]
    pins = {path: {'bytes': (ROOT / path).stat().st_size,
                  'sha256': hashlib.sha256((ROOT / path).read_bytes()).hexdigest()}
            for path in sources + ['scripts/profile_public_context_tables.py']}
    result = {
        'scope': 'Provisional metadata feasibility only; no sign data, semantic test, source authentication or independence claim.',
        'normalization': 'Uppercase and remove whitespace only; preserve punctuation, prefixes, suffixes and leading zeroes.',
        'additional_conservative_exclusion': 'Exclude a Lipi artifact reported under multiple nonmissing normalized field keys.',
        'source_pins': pins,
        'mackay_profile': profile(tables['mackay'], 'no'),
        'mackay_raw_context_coverage': {
            'some_locus_rows': sum(any(present(r[k]) for k in ('block', 'house', 'room', 'street')) for r in tables['mackay']),
            'numeric_raw_depth_rows': sum(numeric(r['level_ft']) for r in tables['mackay']),
            'some_locus_and_numeric_raw_depth_rows': sum(numeric(r['level_ft']) and any(present(r[k]) for k in ('block', 'house', 'room', 'street')) for r in tables['mackay']),
        },
        'marshall_profile': profile(tables['marshall'], 'plate_no'),
        'findspots_profile': profile(tables['findspots'], 'mackay_no'),
        'mackay_join': join_mackay(tables['mackay'], tables['lipi']),
        'limits': [
            'Public table is AI-assisted secondary transcription. Repository validation did not independently verify field numbers or depths.',
            'Mackay phase_estimate is inferred from numeric depth thresholds, including an SD +2.2 feet adjustment; not independently excavated phases or Early/Late Harappan periods.',
            'Raw Mackay depths have area-specific datum conventions; this profile never pools or recalibrates them.',
            'Marshall depth is below modern surface and must not be pooled with Mackay fixed-datum depth.',
            'Findspots are narrative-derived and not an independent replication of the Mackay table.',
            'Exact normalized key agreement proposes a linkage for primary verification; it does not prove identity, context integrity, contemporaneity or independent artifacts.',
        ],
    }
    target = ROOT / 'results/public_context_feasibility.json'
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    summary = {k: result['mackay_join'][k] for k in ('eligible_join_count',
        'eligible_locus_and_raw_numeric_depth_count', 'eligible_join_areas_from_raw_field_prefix',
        'eligible_locus_depth_areas_from_raw_field_prefix')}
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
