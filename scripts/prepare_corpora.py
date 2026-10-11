"""Strict parsing, exclusion ledger, explicit numbering, and independent corpora.

The lipi export is a secondary transcription, not a validated official ICIT release.
Its proposed phonetic values, translations, and canonicalization are NOT imported.
File order is retained. Directional labels below mean FILE start/end only.
"""
from collections import Counter
import csv
import json
import re
import tarfile
import zipfile
import xml.etree.ElementTree as ET
from common import ROOT, write_json, write_jsonl, write_csv

def parse_lipi(row):
    reasons = []
    raw = row['text']
    if not re.fullmatch(r'\+\d{3}(?:-\d{3})*\+', raw):
        reasons.append('not_complete_simple_single_line')
    tokens = raw[1:-1].split('-') if not reasons else []
    if any(x in ('000', '999') for x in tokens):
        reasons.append('unknown_or_separator_token')
    if row['complete'].strip() != 'Y':
        reasons.append('not_marked_complete')
    if row['dir.'].strip().upper() != 'R/L':
        reasons.append('direction_not_R/L')
    if row['class'].strip() in ('2L', '3L'):
        reasons.append('multiline_class')
    if tokens and row['signs'].isdigit() and len(tokens) != int(row['signs']):
        reasons.append('sign_count_mismatch')
    return ['W' + t for t in tokens], reasons

def main():
    rows = list(csv.DictReader((ROOT / 'data/raw/lipi_inscriptions.csv').open()))
    kept, ledger = [], []
    for i, r in enumerate(rows):
        seq, reasons = parse_lipi(r)
        ledger.append({'row': i + 2, 'id': r['id'], 'cisi': r['cisi'], 'text': r['text'],
                       'retained': not reasons, 'reasons': ';'.join(reasons)})
        if not reasons:
            artifact = r['cisi'].strip()
            if artifact in ('', '-', '--', '?'):
                artifact = 'lipi_id:' + r['id'].split('.')[0]
            kept.append({'id': r['id'], 'artifact': artifact, 'cisi_original': r['cisi'], 'site': r['site'],
                         'type': r['type'], 'condition': r['condition'],
                         'preservation': r['preservation'], 'sequence': seq,
                         'order': 'source_file_order', 'namespace': 'Wells_ICIT_as_exported'})
    write_csv('results/exclusions_lipi.csv', ledger)
    write_jsonl('data/processed/lipi_strict.jsonl', kept)
    features, independent, excluded = [], [], []
    with tarfile.open(ROOT / 'data/raw/mayig_corpus.tar.gz') as archive:
        for member in sorted(archive.getmembers(), key=lambda x: x.name):
            if not member.isfile():
                continue
            name = '/'.join(member.name.split('/')[1:])
            if name == 'LICENSE':
                (ROOT / 'data/raw/mayig_LICENSE').write_bytes(archive.extractfile(member).read())
            if name.startswith('features/') and name.endswith('.json'):
                feat = json.load(archive.extractfile(member))
                feat['source_path'] = name
                features.append(feat)
            if name.startswith('corpus/') and name.endswith('.json'):
                for obj in json.load(archive.extractfile(member)):
                    glyphs = obj['graphemes']
                    # Reject an entire side if line order or readings are uncertain.
                    clean = (glyphs and all(re.fullmatch(r'P\d{3}', g['id'])
                             and len(g['features']) >= 3 and g['features'][0] == 0
                             and g['features'][2] == 0 for g in glyphs)
                             and len({g['features'][1] for g in glyphs}) == 1)
                    record = {'id': obj['id'], 'artifact': name, 'site': 'Mohenjo-daro',
                              'type': obj['description'], 'sequence': [g['id'] for g in glyphs],
                              'namespace': 'Parpola', 'order': 'left_to_right_display_order'}
                    (independent if clean else excluded).append(record)
    write_json('data/processed/catalogue_features.json', features)
    write_jsonl('data/processed/mayig_strict.jsonl', independent)
    write_jsonl('results/exclusions_mayig.jsonl', excluded)
    controls = {}
    with zipfile.ZipFile(ROOT / 'data/raw/sproat_corpora.zip') as z:
        for name in z.namelist():
            if not name.endswith('.xml'):
                continue
            label = name.split('/')[-1][:-4]
            corpus = []
            tree = ET.fromstring(z.read(name))
            for i, doc in enumerate(tree.findall('.//document')):
                text = doc.find('docText')
                if text is None:
                    continue
                lines = text.findall('line') or [text]
                for j, line in enumerate(lines):
                    seq = [x.findtext('title', '').strip() for x in line.findall('symbol')]
                    if seq and all(seq):
                        corpus.append({'id': f'{label}:{i}:{j}', 'artifact': f'{label}:{i}',
                                       'site': label, 'sequence': seq, 'namespace': label,
                                       'order': 'source_file_order'})
            write_jsonl(f'data/processed/sproat_{label}.jsonl', corpus)
            controls[label] = len(corpus)
    write_json('results/corpus_audit.json', {
        'lipi_raw_rows': len(rows), 'lipi_strict_rows': len(kept),
        'lipi_unique_sequences': len({tuple(r['sequence']) for r in kept}),
        'lipi_exclusion_reasons_overlap': dict(Counter(reason for r in ledger for reason in r['reasons'].split(';') if reason)),
        'lipi_sites': dict(Counter(r['site'] for r in kept)),
        'mayig_strict_sides': len(independent), 'mayig_excluded_sides': len(excluded),
        'catalogue_features': len(features), 'sproat_rows': controls,
        'warning': 'Strict filtering cannot repair transcription mistakes. Independent corpora overlap archaeologically; never pool their counts.'})

if __name__ == '__main__':
    main()
