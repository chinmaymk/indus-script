"""Preserve a source-labeled M77 corpus and select a conservative candidate subset.

No source code executed, no dubious tokens removed within a line, no M/P/W joins.
Selection is not wholesale authentication of the secondary transcription.
"""
from collections import Counter, defaultdict
import csv
import json
import re
from common import ROOT, sha256, write_json

OBJECT_CODES = {'1': 'seal', '2': 'sealing', '3': 'miniature tablet',
                '4': 'pottery graffito', '5': 'copper tablet', '6': 'bronze implement',
                '7': 'ivory or bone rod', '9': 'miscellaneous'}
DIRECTION_CODES = {'0': 'no line', '1': 'right to left', '2': 'left to right',
                   '3': 'single sign', '4': 'top to bottom',
                   '5': 'symmetrical arrangement', '9': 'doubtful'}


def parse_token(raw):
    """Keep a doubtful reading distinct; 000 is an unknown-span marker, not a sign."""
    if not isinstance(raw, str) or not re.fullmatch(r'\*?\d{1,3}', raw):
        raise ValueError(f'Invalid literal M77 token: {raw!r}')
    doubtful = raw.startswith('*')
    number = int(raw.lstrip('*'))
    if not 0 <= number <= 417:
        raise ValueError(f'Out-of-inventory M77 token: {raw!r}')
    return {'raw': raw, 'sign': None if number == 0 else f'M{number:03d}',
            'doubtful': doubtful, 'unknown_span': number == 0,
            'diplomatic': ('*' if doubtful else '') + f'{number:03d}'}


def parse_record(source):
    if source.get('source_system') != 'indusscript-m77' or source.get('sign_id_scheme') != 'Mahadevan1977':
        raise ValueError('Expected explicit M77 source and namespace')
    reference = str(source['source_object_id'])
    if not reference.isdigit() or int(reference) != source['_source_extra']['textnum']:
        raise ValueError('Source reference mismatch')
    if source['glossa_id'] != f'GLI-IND-M77-{int(reference):05d}':
        raise ValueError('Glossa reference mismatch')
    tokens = [parse_token(t) for t in source['raw_signs']]
    encoded = '+' + '-'.join(t['diplomatic'] for t in tokens) + '+'
    if encoded != source['text_code_diplomatic'] or encoded != source['text_code_diplomatic_normalized']:
        raise ValueError(f'Diplomatic/raw disagreement: {reference}')
    if [t['diplomatic'] for t in tokens] != source['canonical_grapheme_ids']:
        raise ValueError(f'Canonical/raw disagreement: {reference}')
    if sum(t['sign'] is not None for t in tokens) != source['sign_instance_count']:
        raise ValueError(f'Sign count disagreement: {reference}')
    dc = source['_source_extra']['doc_count']
    if not isinstance(dc, int) or dc < 1:
        raise ValueError('Invalid upstream doc_count')
    direction, object_code = source['direction'], source['inscobj']
    if direction not in DIRECTION_CODES or object_code not in OBJECT_CODES:
        raise ValueError('Unknown primary code; do not guess')
    reasons = []
    if dc != 1:
        reasons.append('multiple_source_documents_line_recovery_unverified')
    if direction != '1':
        reasons.append('direction_not_right_to_left')
    if any(t['unknown_span'] for t in tokens):
        reasons.append('unknown_span_present')
    if any(t['doubtful'] for t in tokens):
        reasons.append('doubtful_reading_present')
    if len(tokens) < 2:
        reasons.append('fewer_than_two_token_slots')
    return {
        'id': source['glossa_id'], 'source_reference': reference,
        'namespace': 'Mahadevan1977', 'diplomatic': encoded, 'tokens': tokens,
        'source_doc_count': dc, 'source_direction_code': direction,
        'primary_direction_definition': DIRECTION_CODES[direction],
        'source_object_code': object_code, 'primary_object_definition': OBJECT_CODES[object_code],
        'upstream_artifact_type': source['artifact_type'],
        'site_label_unverified': source.get('site_name'),
        'source_extra': source['_source_extra'], 'source_citation': source['_citation'],
        'strict_candidate': not reasons, 'exclusion_reasons': reasons,
        'order': 'preserved source array; agrees with reading printed normalized glyphs right to left in two checked examples',
        'authentication': 'secondary transcription, two selected complete lines checked; no population error rate or complete physical-object crosswalk',
    }


def main():
    path = 'data/raw/glossa_canonical_objects.jsonl'
    objects = [json.loads(l) for l in (ROOT/path).read_text().splitlines()]
    rows = [parse_record(r) for r in objects if r.get('source_system') == 'indusscript-m77']
    if len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Repeated canonical row IDs')
    exported = {r['glossa_id']: r for r in json.loads((ROOT/'data/raw/glossa_icit_export.json').read_text())['sequences'] if r['source_system'] == 'indusscript-m77'}
    if set(exported) != {r['id'] for r in rows}:
        raise ValueError('Export/canonical ID mismatch')
    for r in rows:
        if exported[r['id']]['icit_text'] != r['diplomatic']:
            raise ValueError('Export/canonical text mismatch')
    strict = [{'id': r['id'], 'source_reference': r['source_reference'],
               'sequence': [t['sign'] for t in r['tokens']],
               'source_object_code': r['source_object_code'],
               'source_doc_count': r['source_doc_count'],
               'source_direction_code': r['source_direction_code'],
               'status': 'conditional secondary corpus; not all lines visually authenticated'}
              for r in rows if r['strict_candidate']]
    unique = defaultdict(list)
    for r in strict:
        unique[tuple(r['sequence'])].append(r['source_reference'])
    primary = {r['sign']: int(r['total']) for r in csv.DictReader((ROOT/'data/processed/mahadevan_1977_table_i.csv').open())}
    all_freq = Counter(t['sign'] for r in rows for t in r['tokens'] if t['sign'])
    freq = Counter(t for r in strict for t in r['sequence'])
    positions = defaultdict(Counter)
    for r in strict:
        for i, sign in enumerate(r['sequence']):
            positions[sign]['initial' if i == 0 else 'final' if i == len(r['sequence'])-1 else 'medial'] += 1
    profiles = [{'sign': sign, 'primary_table_total': primary[sign],
                 'all_export_occurrences_including_doubtful': all_freq[sign],
                 'strict_candidate_occurrences': freq[sign],
                 'strict_candidate_positions': dict(positions[sign]),
                 'accepted_semantic_value': None, 'accepted_phonetic_value': None}
                for sign in sorted(primary)]
    for out, values in [('data/processed/m77_candidate_records.jsonl', rows),
                        ('data/processed/m77_candidate_strict.jsonl', strict)]:
        (ROOT/out).write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in values))
    write_json('results/m77_candidate_profiles_417.json', profiles)
    counts = {'source_records': len(rows), 'strict_candidate_rows': len(strict),
              'strict_tokens': sum(freq.values()), 'strict_sign_types': len(freq),
              'strict_unique_texts': len(unique),
              'strict_duplicate_excess': len(strict)-len(unique),
              'strict_unique_text_tokens': sum(map(len, unique)),
              'primary_inventory_size': len(profiles),
              'exclusion_reason_counts_overlapping': dict(Counter(x for r in rows for x in r['exclusion_reasons'])),
              'strict_object_code_counts': dict(Counter(r['source_object_code'] for r in strict)),
              'source_doc_count_histogram': dict(Counter(r['source_doc_count'] for r in rows))}
    write_json('results/m77_candidate_audit.json', {
        'source_sha256': {p: sha256(ROOT/p) for p in [path, 'data/raw/glossa_icit_export.json', 'data/processed/mahadevan_1977_table_i.csv']},
        'counts': counts,
        'exact_export_canonical_join': True,
        'duplicate_text_groups': [{'sequence': list(s), 'source_references': refs} for s, refs in sorted(unique.items()) if len(refs)>1],
        'rules': ['Entire doubtful/unknown-span records excluded; no gap bridging.',
                  'doc_count!=1 excluded because multiline recovery is unverified; source2405 demonstrably collapses seven printed lines to one sequence.',
                  'Actual source direction1 selected; no array reversal based on direction metadata.',
                  'Primary object-code meaning kept apart from upstream blanket seal label.',
                  'No semantic values imported; no M/P/W identity inferred from equal numbers.',
                  'Different transcripts can share physical objects; this is not an independent sample from the W corpus.'],
        'scope': 'Conditional corpus preparation. Two targeted line checks do not authenticate every record. No transcription is silently repaired; excluded data remain in the record ledger.'})
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
