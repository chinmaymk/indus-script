"""Losslessly package the large frozen support ledger; never rerun the analysis."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil


def stream_hash(stream):
    digest = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b''):
        digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    root = args.directory
    original = root / 'analysis.json'
    compressed = root / 'analysis.json.gz'
    record = root / 'storage_manifest.json'
    if compressed.exists() or record.exists():
        raise FileExistsError('Storage package already exists')
    expected = json.loads((root / 'output_manifest.json').read_text())['analysis.json']
    with original.open('rb') as stream:
        if stream_hash(stream) != expected:
            raise ValueError('Frozen original hash differs')
    size = original.stat().st_size
    with original.open('rb') as source, compressed.open('xb') as target:
        with gzip.GzipFile(filename='', mode='wb', fileobj=target, mtime=0) as archive:
            shutil.copyfileobj(source, archive)
    with gzip.open(compressed, 'rb') as stream:
        if stream_hash(stream) != expected:
            raise ValueError('Lossless decompression verification failed')
    with compressed.open('rb') as stream:
        compressed_hash = stream_hash(stream)
    record.write_text(json.dumps({
        'logical_file': 'analysis.json', 'stored_file': 'analysis.json.gz',
        'original_bytes': size, 'original_sha256': expected,
        'stored_bytes': compressed.stat().st_size, 'stored_sha256': compressed_hash,
        'verified_decompressed_sha256': expected,
        'original_output_manifest_preserved': True,
        'note': 'Read with gzip.open; original manifest describes logical uncompressed bytes. No analysis rerun or content change.'
    }, indent=2) + '\n')
    original.unlink()  # Verified, lossless alternate representation is retained.
    print(record.read_text())


if __name__ == '__main__':
    main()
