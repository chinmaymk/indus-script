"""Guard the evidential separation that an external reading proposal requires."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_glossa_key import audit_key, compare_417


class ExternalKeyAuditTests(unittest.TestCase):
    def test_out_of_namespace_sign_cannot_inflate_m77_coverage(self):
        d = {'anchors': {'M001': {'confidence': 'HIGH'}, 'W001': {'confidence': 'HIGH'}, 'H003': {'confidence': 'LOW'}}}
        a = audit_key(d, {'M001': 5, 'M002': 7})
        self.assertEqual(a['entry_count'], 3)
        self.assertEqual(a['m77_present_count'], 1)
        self.assertEqual(a['nominal_high_medium_id_coverage_tokens'], 5)
        self.assertEqual(a['m77_table_i_token_denominator'], 12)
        self.assertEqual(a['outside_m77_inventory'], ['H003', 'W001'])

    def test_reported_counts_never_override_computed_counts(self):
        d = {'anchors': {'M001': {'confidence': 'LOW'}}, 'by_confidence': {'HIGH': 100}, 'total': 100}
        a = audit_key(d, {'M001': 10})
        self.assertEqual(a['recomputed_confidence_counts'], {'LOW': 1})
        self.assertEqual(a['nominal_high_medium_id_coverage_tokens'], 0)

    def test_proposed_reading_does_not_become_an_established_reading(self):
        a = {'anchors': {'M001': {'confidence': 'HIGH', 'reading': 'test'}}}
        rows = compare_417(a, a, {'reviewed_anchors': []})
        self.assertEqual(len(rows), 417)
        self.assertTrue(all(r['established_phonetic_value'] is None and r['established_semantic_value'] is None for r in rows))
        self.assertEqual(rows[0]['release_candidate']['reading'], 'test')
        self.assertIsNone(rows[1]['release_candidate'])


if __name__ == '__main__':
    unittest.main()
