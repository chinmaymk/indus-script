import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_meluhha_name_pool import summarize_record


class NamePoolTests(unittest.TestCase):
    def record(self, text):
        return {'id': 1, 'designation': 'test', 'inscription': {
            'atf': '&P000001 = test\n#atf: lang sux\n' + text}}

    def test_recipient_name_is_not_seal_ownership(self):
        result = summarize_record(self.record('@obverse\n1. 1(disz) sila3 sa6-ma-ar\n@seal 1\n$ illegible'))
        self.assertEqual(len(result['literal_name_spelling_hits']), 1)
        self.assertFalse(result['name_hits_establish_seal_ownership'])
        self.assertEqual(result['seal_annotations_in_export'][0]['status'], 'illegible')
        self.assertEqual(result['numbered_seal_lines_in_export'], [])

    def test_missing_seal_field_is_not_physical_absence(self):
        result = summarize_record(self.record('@obverse\n1. na-na-sa3'))
        self.assertEqual(result['seal_annotations_in_export'], [])
        self.assertFalse(result['absence_from_export_proves_absence_on_artifact'])

    def test_exact_tokens_do_not_silently_repair_damage_or_extend_names(self):
        result = summarize_record(self.record('@obverse\n1. [na-na-sa3] sa6-ma-ar-ra\n2. na-na-za'))
        self.assertEqual([r['matched_spelling'] for r in result['literal_name_spelling_hits']], ['na-na-za'])

    def test_wrong_artifact_rejected(self):
        record = self.record('@obverse\n1. na-na-za')
        record['id'] = 2
        with self.assertRaises(ValueError):
            summarize_record(record)


if __name__ == '__main__':
    unittest.main()
