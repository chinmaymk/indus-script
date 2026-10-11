import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_evidence_index import attach_context_audits


class ContextAuditLinkTest(unittest.TestCase):
    def test_primary_conflict_retains_both_signs_without_merging(self):
        rows=[dict(sign=m,semantic_value=None,phonetic_value=None) for m in ('M216','M222','M254')]
        feature=dict(id='P230',wells_graphemes=['W550','W555'],mahadevan_graphemes=['M216'])
        audit=dict(id='ending',result='result',report='report',W_candidates=['W555'],
                   M_review_candidates=['M216','M222','M254'],conclusion='mapping conflict')
        attach_context_audits(rows,[feature],[audit])
        self.assertEqual([len(r['conditional_context_audit_links']) for r in rows],[2,1,1])
        self.assertIsNone(rows[1]['conditional_context_audit_links'][0]['via_P'])
        self.assertEqual(rows[0]['conditional_context_audit_links'][1]['via_P'],'P230')
        self.assertTrue(all(r['semantic_value'] is None and r['phonetic_value'] is None for r in rows))

    def test_many_way_bridge_preserves_uncertainty(self):
        rows=[dict(sign=m,semantic_value=None,phonetic_value=None) for m in ('M415','M417','M001')]
        feature=dict(id='P353',wells_graphemes=['W215','W216'],mahadevan_graphemes=['M415','M417'])
        audit=dict(id='pipe',result='result',report='report',W_candidates=['W215'],conclusion='unresolved')
        attach_context_audits(rows,[feature],[audit])
        self.assertEqual([len(r['conditional_context_audit_links']) for r in rows],[1,1,0])
        for r in rows[:2]:
            link=r['conditional_context_audit_links'][0]
            self.assertEqual(link['M_candidates_in_source_entry'],['M415','M417'])
            self.assertEqual(link['W_members_in_source_entry'],['W215','W216'])
            self.assertIsNone(r['semantic_value']);self.assertIsNone(r['phonetic_value'])


if __name__=='__main__':unittest.main()
