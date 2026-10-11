import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_sign_families import family_inventory, grouped_units, tokens_from_units, VariantModel, descriptive_evidence


OWNER = {'W001': 'P001', 'W002': 'P001'}
FAMILIES = {'P001': ['W001', 'W002'], 'P002': ['W010', 'W011', 'W012']}


def row(identifier, artifact, sequence):
    return dict(id=identifier, artifact=artifact, sequence=sequence, site='synthetic', type='synthetic')


class SignFamilyTests(unittest.TestCase):
    def test_collapsed_text_and_artifact_links_are_transitive(self):
        rs = [row('a1', 'a', ['W001', 'W090']), row('b1', 'b', ['W002', 'W090']),
              row('b2', 'b', ['W050', 'W001']), row('c1', 'c', ['W050', 'W002']),
              row('d1', 'd', ['W040', 'W001'])]
        units = grouped_units(rs, OWNER)
        by_artifact = {r['artifact']:r for r in units}
        self.assertEqual(len({by_artifact[x]['group'] for x in 'abc'}), 1)
        self.assertNotEqual(by_artifact['a']['group'], by_artifact['d']['group'])
        self.assertEqual(grouped_units(list(reversed(rs)), OWNER), units)

    def test_dedup_retains_ids_and_target_is_not_a_feature(self):
        rs = [row('a1', 'a', ['W050', 'W001']), row('a2', 'a', ['W050', 'W001']),
              row('b1', 'b', ['W050', 'W002'])]
        units = grouped_units(rs, OWNER)
        self.assertEqual(len(units), 2)
        self.assertEqual(units[0]['source_ids'], ['a1', 'a2'])
        ts = tokens_from_units(units, OWNER)
        self.assertEqual(ts[0]['neighbors'], ts[1]['neighbors'])
        self.assertEqual(ts[0]['metadata'], ts[1]['metadata'])
        self.assertNotIn('W001', ts[0]['neighbors'])

    def test_probability_normalization_with_unseen_classes_and_contexts(self):
        train = tokens_from_units(grouped_units([row('a', 'a', ['W050', 'W001'])], OWNER), OWNER)
        for strength in [5, 20, 100]:
            model = VariantModel(train, FAMILIES, strength)
            for f in FAMILIES:
                for neighbors in [('W050', '<EOS>'), ('unseen', 'unseen')]:
                    probabilities = [model.probabilities(dict(family=f, sign=s,
                        metadata=('unseen', 'unseen', 9, 'middle'), neighbors=neighbors)) for s in FAMILIES[f]]
                    for mode in range(3):
                        self.assertAlmostEqual(sum(p[mode] for p in probabilities), 1)
                        self.assertTrue(all(p[mode] > 0 for p in probabilities))

    def test_duplicate_inscriptions_do_not_multiply_exact_frames(self):
        rs = [row('a', 'a', ['W050', 'W001']), row('b', 'b', ['W050', 'W002']),
              row('c', 'c', ['W050', 'W001']), row('d', 'd', ['W001', 'W002'])]
        result = descriptive_evidence(grouped_units(rs, OWNER), OWNER)['P001']
        self.assertEqual(result['exact_substitution_frames'], [{'frame':'W050 ?', 'variants':['W001','W002']}])
        self.assertEqual(len(result['texts_with_distinct_members']), 1)

    def test_ambiguous_catalogue_family_fails_closed(self):
        with self.assertRaises(ValueError):
            family_inventory([{'id':'P001','wells_graphemes':['W001','W002']},
                              {'id':'P002','wells_graphemes':['W002','W003']}])


if __name__ == '__main__':
    unittest.main()
