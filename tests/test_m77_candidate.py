"""Prevent invented adjacency, false certainty, and namespace errors in M77 import."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_m77_candidate import parse_record, parse_token


def record(tokens=('86', '99'), documents=1, direction='1', object_code='1'):
    diplomatic_tokens = [('*' if t.startswith('*') else '') + f'{int(t.lstrip("*")):03d}' for t in tokens]
    text = '+' + '-'.join(diplomatic_tokens) + '+'
    return {'source_system': 'indusscript-m77', 'sign_id_scheme': 'Mahadevan1977',
            'glossa_id': 'GLI-IND-M77-01066', 'source_object_id': '1066',
            '_source_extra': {'textnum': 1066, 'doc_count': documents},
            'raw_signs': list(tokens), 'canonical_grapheme_ids': diplomatic_tokens,
            'text_code_diplomatic': text, 'text_code_diplomatic_normalized': text,
            'sign_instance_count': sum(int(t.lstrip('*')) != 0 for t in tokens),
            'direction': direction, 'inscobj': object_code, 'artifact_type': 'seal',
            '_citation': {'derivation': 'synthetic fixture'}}


class M77CandidateTests(unittest.TestCase):
    def test_doubtful_reading_is_not_silently_made_certain(self):
        t = parse_token('*402')
        self.assertEqual(t['sign'], 'M402')
        self.assertTrue(t['doubtful'])
        r = parse_record(record(('86', '*402', '99')))
        self.assertFalse(r['strict_candidate'])
        self.assertEqual([t['raw'] for t in r['tokens']], ['86', '*402', '99'])

    def test_zero_gap_is_preserved_and_excludes_whole_line(self):
        r = parse_record(record(('86', '0', '99')))
        self.assertFalse(r['strict_candidate'])
        self.assertEqual(len(r['tokens']), 3)
        self.assertIsNone(r['tokens'][1]['sign'])
        self.assertEqual(r['diplomatic'], '+086-000-099+')

    def test_multidocument_record_not_treated_as_complete_line_recovery(self):
        self.assertFalse(parse_record(record(documents=7))['strict_candidate'])
        self.assertTrue(parse_record(record())['strict_candidate'])

    def test_non_rtl_record_excluded_without_reversing_or_destroying_it(self):
        r = parse_record(record(direction='2'))
        self.assertFalse(r['strict_candidate'])
        self.assertEqual([t['sign'] for t in r['tokens']], ['M086', 'M099'])

    def test_primary_object_code_is_not_overridden_by_generic_seal_label(self):
        r = parse_record(record(object_code='5'))
        self.assertEqual(r['primary_object_definition'], 'copper tablet')
        self.assertEqual(r['upstream_artifact_type'], 'seal')

    def test_corruption_or_wrong_namespace_fails_closed(self):
        for field, value in [('sign_id_scheme', 'Wells2015'), ('source_object_id', '1067'),
                             ('text_code_diplomatic', '+099-086+'), ('inscobj', '8')]:
            with self.subTest(field=field):
                r = copy.deepcopy(record()); r[field] = value
                with self.assertRaises(ValueError):
                    parse_record(r)
        for token in ('418', 'W086', '-1', '86.0'):
            with self.assertRaises(ValueError):
                parse_token(token)


if __name__ == '__main__':
    unittest.main()
