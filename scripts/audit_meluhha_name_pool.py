"""Compare pinned cuneiform records in the four-citation name pool.

Literal spelling hits locate evidence; they do not identify the seal owner or
translate Indus signs. Absence from a catalogue export is not artifact absence.
"""
from pathlib import Path
import hashlib
import json
import re
from audit_p453801_anchor import parse_atf, classified_seals

ROOT = Path(__file__).resolve().parents[1]
SPELLINGS = ('na-na-za', 'na-na-sa3', 'sa6-ma-ar', 'a-li-a-hi')


def spelling_hits(parsed):
    return [dict(line, matched_spelling=spelling)
            for line in parsed['lines'] for spelling in SPELLINGS
            if spelling in line['text'].split()]


def summarize_record(record):
    parsed = parse_atf(record['inscription']['atf'])
    if parsed['artifact'] != 'P' + str(record['id']).zfill(6):
        raise ValueError('Catalogue/ATF identity mismatch')
    seal_lines = [line for line in parsed['lines']
                  if re.fullmatch(r'seal\s*\d+', line['section'] or '')]
    seal_annotations = [row for row in parsed['annotations']
                        if re.fullmatch(r'seal\s*\d+', row['section'] or '')]
    return {
        'artifact': parsed['artifact'], 'designation': record['designation'],
        'museum_no': record.get('museum_no'),
        'dates_referenced': record.get('dates_referenced'),
        'top_level_language_code': parsed['top_level_language_code'],
        'literal_name_spelling_hits': spelling_hits(parsed),
        'numbered_seal_lines_in_export': seal_lines,
        'seal_annotations_in_export': seal_annotations,
        'seal_relations': classified_seals(record),
        'parsed_text': parsed,
        'absence_from_export_proves_absence_on_artifact': False,
        'name_hits_establish_seal_ownership': False,
    }


def main():
    inputs = json.loads((ROOT/'data/processed/meluhha_name_pool_records.json').read_text())
    outputs = []
    hashes = {}
    for item in inputs['records']:
        path = ROOT/item['path']
        raw = path.read_bytes()
        hashes[item['path']] = hashlib.sha256(raw).hexdigest()
        records = json.loads(raw)
        if len(records) != 1 or records[0]['id'] != item['cdli_id']:
            raise ValueError('Unexpected record at ' + item['path'])
        outputs.append(dict(citation=item['citation'], **summarize_record(records[0])))
    result = {
        'scope': inputs['scope'], 'inputs_sha256': hashes, 'records': outputs,
        'publication_count': len(inputs['citations']),
        'cdli_export_record_count': len({r['artifact'] for r in outputs}),
        'records_without_cdli_export': inputs['records_without_cdli_export'],
        'independent_physical_object_count': None,
        'possible_duplicate_groups': inputs['possible_duplicate_groups'],
        'limitations': [
            'Names are literal export matches, not fresh cuneiform readings.',
            'Spelling revisions are not validated interchangeable phonetic values.',
            'Catalogue IDs and repeated names are not independent object identities.',
            'No syllabic key is fitted: externally attributed Indus strings remain unestablished.',
            'Image and ownership reviews are manual evidence, linked in the companion report.'
        ]
    }
    (ROOT/'results/meluhha_name_pool_audit.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'records': len(outputs), 'name_hits_by_artifact': {
        r['artifact']: len(r['literal_name_spelling_hits']) for r in outputs},
        'independent_physical_object_count': None}))


if __name__ == '__main__':
    main()
