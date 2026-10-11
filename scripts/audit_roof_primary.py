"""Validate the recorded roof-field source checks without joining object sides."""
import json
from common import ROOT, read_jsonl, sha256, write_json


def main():
    paths = ['data/processed/roof_m176_primary_review.json', 'data/processed/roof_m092_primary_review.json']
    m176, m092 = reviews = [json.loads((ROOT / p).read_text()) for p in paths]
    pins = 0
    for review in reviews:
        for pin in review['evidence_files']:
            assert sha256(ROOT / pin['path']) == pin['sha256'], pin['path']
            assert (ROOT / pin['path']).stat().st_size == pin['bytes'], pin['path']
            pins += 1
        assert review['semantic_values'] is None and review['phonetic_values'] is None
    fields = {f['field_id']: f for f in m176['fields']}
    assert len(fields) == len(m176['fields']) == 8
    assert sum(f['field_kind'] == 'script_line' for f in fields.values()) == 7
    by_ref = {r['source_reference']: r for r in read_jsonl('data/processed/m77_candidate_records.jsonl')}
    for ref in ('4407', '4493', '5444', '5477'):
        field = fields[f'{ref}:1:0']; source = by_ref[ref]
        assert [t['sign'] for t in source['tokens']] == field['normalized_tokens']
        assert field['full_printed_field_verified']
    for ref in ('4407', '5444'):
        assert fields[f'{ref}:2:0']['normalized_tokens'] == ['M087', 'M328']
    assert fields['4493:2:0']['normalized_tokens'] == ['M095', 'M328']
    assert fields['5477:1:0']['original_direction_code'] == 2
    assert fields['5477:2:9']['field_kind'] == 'symbol_only'
    assert not fields['5477:2:9']['normalized_tokens']
    assert m092['whole_field_excluded_for_loss'] and m092['primary_table_M092_total'] == 1
    assert m092['normalized_reading_order'] == ['M092', 'M099', 'LOSS']
    assert any(t['unknown_span'] for t in by_ref['8018']['tokens'])
    write_json('results/roof_primary_audit.json', {
        'm176_fields': m176, 'm092_coverage': m092, 'evidence_pin_checks': pins,
        'fields_verified': 8, 'script_lines': 7, 'symbol_only_entries': 1,
        'source_direction_discrepancies': [
            {'reference': ref, 'secondary': by_ref[ref]['source_direction_code'],
             'primary': fields[f'{ref}:1:0']['original_direction_code']}
            for ref in ('4407', '4493', '5444', '5477')
            if int(by_ref[ref]['source_direction_code']) != fields[f'{ref}:1:0']['original_direction_code']],
        'new_semantic_values': 0, 'new_phonetic_values': 0,
        'limits': 'Primary normalized fields, not original artifact readings or independent die counts. Additional sides remain separate. Corpus screen is unchanged.',
        'input_sha256': {p: sha256(ROOT / p) for p in paths + ['data/processed/m77_candidate_records.jsonl']}})
    print(f'Roof primary evidence verified: {pins} pins; eight separate M176-object entries; M092 loss retained.')


if __name__ == '__main__':
    main()
