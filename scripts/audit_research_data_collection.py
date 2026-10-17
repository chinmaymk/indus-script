#!/usr/bin/env python3
"""Measure retained registered external downloads without counting local renders."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse


def file_format(prefix):
    if b'%PDF-' in prefix:
        return 'pdf'
    if (prefix.startswith((b'\xff\xd8\xff', b'\x89PNG\r\n\x1a\n', b'GIF87a', b'GIF89a'))
            or (prefix[:4] == b'RIFF' and prefix[8:12] == b'WEBP')):
        return 'image'
    return 'other'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    assert not args.report.exists(), 'Use a new report path.'
    repo = Path(__file__).resolve().parents[1]
    registry_path = repo / 'data/sources.json'
    registry_bytes = registry_path.read_bytes()
    registry = json.loads(registry_bytes)
    records, excluded, seen = [], [], set()
    for row in registry['downloads']:
        if (urlparse(row.get('url') or '').scheme not in ('http', 'https')
                or (row.get('kind') or '').startswith('local_')):
            excluded.append({'path': row['path'], 'kind': row.get('kind'),
                             'reason': 'No direct HTTP source URL or explicitly local render/crop.'})
            continue
        assert row['path'] not in seen, ('duplicate path', row['path'])
        seen.add(row['path'])
        path = repo / row['path']
        digest = hashlib.sha256()
        prefix, size = b'', 0
        with path.open('rb') as stream:
            while chunk := stream.read(1024 * 1024):
                if not prefix:
                    prefix = chunk[:1024]
                digest.update(chunk)
                size += len(chunk)
        assert size == row['bytes'], ('source size differs', row['path'])
        assert digest.hexdigest() == row['sha256'], ('source hash differs', row['path'])
        records.append({'path': row['path'], 'bytes': size, 'sha256': digest.hexdigest(),
                        'format': file_format(prefix), 'url': row['url'],
                        'kind': row.get('kind'), 'http_status': row.get('http_status')})
    grouped = defaultdict(list)
    for row in records:
        grouped[row['sha256']].append(row)
    unique = [rows[0] for rows in grouped.values()]

    def tally(rows):
        return {'files': len(rows), 'bytes': sum(r['bytes'] for r in rows),
                'formats': dict(Counter(r['format'] for r in rows)),
                'bytes_by_format': {f: sum(r['bytes'] for r in rows if r['format'] == f)
                                    for f in sorted({r['format'] for r in rows})}}

    report = {
        'scope': 'Registered downloads with HTTP(S) URLs, excluding explicitly local renders/crops. Retained bytes, not network traffic or independent publications.',
        'registry_sha256': hashlib.sha256(registry_bytes).hexdigest(),
        'registered_download_files': tally(records),
        'byte_distinct_downloads': tally(unique),
        'duplicates': [{'sha256': digest, 'bytes_each': rows[0]['bytes'],
                        'paths': [r['path'] for r in rows]}
                       for digest, rows in grouped.items() if len(rows) > 1],
        'separately_registered': {
            key: {'files': len(registry[key]), 'bytes': sum(r['bytes'] for r in registry[key])}
            for key in ('web_extraction_captures', 'archived_http_responses')},
        'excluded_download_entries': excluded,
        'excluded_scope': 'User-supplied starting data, local crops/renders, AI CLI responses, token/accounting captures, derived experiments and extracted archive contents. Search captures and archived HTTP responses are reported separately.',
        'format_note': 'Formats detected by file headers. PDF files can be complete works, excerpts or frontmatter. Downloads may include landing/error responses; no complete-publication claim is made.',
        'all_selected_sizes_and_sha256_verified': True,
        'records': records,
    }
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('registered_download_files', 'byte_distinct_downloads',
                                           'separately_registered', 'all_selected_sizes_and_sha256_verified')}, indent=2))


if __name__ == '__main__':
    main()
