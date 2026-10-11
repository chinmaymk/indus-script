import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_evidence_index import build_index, attach_substitution_evidence, attach_candidate_m77_profiles


def inputs():
    dossiers, families = [], []
    for n in range(1, 418):
        sign = f'M{n:03d}'
        dossiers.append(dict(sign=sign, image=f'{n}.png', sha256='test',
            m77_solus='0', m77_initial='1', m77_medial='2', m77_final='3',
            m77_total='6', m77_primary_pdf_page='728', m77_distributional_description='test',
            mapping_status='ambiguous_or_multiple', candidate_wells_ids=''))
        families.append(dict(sign=sign, coverage='test', supported_families=''))
    copper = {'all_conditions': {'singleton_to_source_labels': {'W777':['Anth','Goat:8'], 'W780':['Anth']}},
              'good_fair_only': {'singleton_to_source_labels': {'W777':['Anth']}}}
    features = [dict(id='P118', mahadevan_graphemes=['M362','M363','M364'],
                     wells_graphemes=['W777','W782'], source_path='features/P118.json')]
    return dossiers, families, features, copper


class EvidenceIndex(unittest.TestCase):
    def test_candidate_transcription_stays_separate_from_primary_and_readings(self):
        rows,_=build_index(*inputs())
        profiles=[{'sign':r['sign'], 'primary_table_total':6,
                   'all_export_occurrences_including_doubtful':4,
                   'strict_candidate_occurrences':2,
                   'strict_candidate_positions':{'initial':1,'final':1},
                   'accepted_semantic_value':'must not promote this'} for r in rows]
        attach_candidate_m77_profiles(rows,profiles)
        self.assertTrue(all(r['primary_M77']['total']==6 and r['semantic_value'] is None for r in rows))
        self.assertEqual(rows[0]['candidate_M77_sequence_profile']['strict_candidate_occurrences'],2)
        with self.assertRaises(ValueError): attach_candidate_m77_profiles(rows,profiles[:-1])
        profiles[0]['primary_table_total']=7
        with self.assertRaises(ValueError): attach_candidate_m77_profiles(rows,profiles)

    def test_ambiguous_link_retains_full_membership_and_unmapped_candidate(self):
        rows, missing = build_index(*inputs())
        self.assertEqual(missing, ['W780'])
        self.assertEqual(sum(bool(r['conditional_copper_links']) for r in rows), 3)
        link = rows[361]['conditional_copper_links'][0]
        self.assertEqual(link['M_candidates_in_source_entry'], ['M362','M363','M364'])
        self.assertEqual(link['motif_labels_good_fair_only'], ['Anth'])
        self.assertTrue(all(r['semantic_value'] is None and r['phonetic_value'] is None for r in rows))

    def test_duplicate_or_missing_sign_rejected(self):
        d, f, features, copper = inputs()
        with self.assertRaises(ValueError): build_index(d[:-1], f, features, copper)
        with self.assertRaises(ValueError): build_index(d, f[:-1]+[f[0]], features, copper)

    def test_substitution_join_preserves_missing_and_ambiguous_members(self):
        d,f,features,copper=inputs()
        rows,_=build_index(d,f,features,copper)
        missing=attach_substitution_evidence(rows,features,{'W777':{'substitution_partner_count':2},
                                                         'W780':{'substitution_partner_count':0}})
        self.assertEqual(missing,['W780'])
        self.assertEqual(len(rows[361]['conditional_substitution_links']),1)
        self.assertEqual(rows[361]['conditional_substitution_links'][0]['M_candidates_in_source_entry'],
                         ['M362','M363','M364'])
        self.assertFalse(rows[0]['conditional_substitution_links'])
        self.assertTrue(all(r['semantic_value'] is None for r in rows))


if __name__ == '__main__':
    unittest.main()
