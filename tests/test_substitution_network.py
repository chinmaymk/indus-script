import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_substitution_network import audit,masked


def records(strings):
    return [dict(id=str(i),artifact='a'+str(i),sequence=s.split()) for i,s in enumerate(strings)]


class SubstitutionNetworkTests(unittest.TestCase):
    def test_duplicates_do_not_inflate_frames_and_sources_survive(self):
        summary,texts,frames,pairs=audit(records(['A X','B X','A X']))
        self.assertEqual(summary['unique_complete_texts'],2)
        self.assertEqual(summary['shared_frames'],1)
        self.assertEqual(pairs[0]['shared_frame_count'],1)
        a=next(t for t in texts if t['sequence']==['A','X'])
        self.assertEqual(len(a['source_records']),2)
        self.assertEqual(summary['signs']['A']['token_count'],1)

    def test_exact_single_position_required_and_lengths_preserved(self):
        summary,_,_,_=audit(records(['A X','B Y','A X Z']))
        self.assertEqual(summary['pair_edges'],0)
        self.assertEqual(masked(('A','A'),0),('?','A'))
        self.assertNotEqual(masked(('A','A'),0),masked(('A','A'),1))

    def test_real_open_wedge_logic_does_not_add_transitive_edge(self):
        summary,_,_,pairs=audit(records(['A X','B X','B Y','C Y']))
        self.assertFalse(any({p['a'],p['b']}=={'A','C'} for p in pairs))
        wedge=summary['open_wedge_witness']
        self.assertEqual((wedge['a'],wedge['b'],wedge['c']),('A','B','C'))
        self.assertFalse(wedge['ac_edge_observed'])

    def test_cooccurrence_and_same_sign_repetition_count_texts(self):
        summary,texts,_,pairs=audit(records(['A X','B X','A B A X','A B A X']))
        ab=next(p for p in pairs if (p['a'],p['b'])==('A','B'))
        self.assertEqual(ab['cooccurring_complete_text_count'],1)
        self.assertEqual(ab['cooccurring_text_witnesses'][0]['a_positions'],[0,2])
        self.assertEqual(summary['signs']['A']['repeated_sign_text_count'],1)
        self.assertEqual(summary['signs']['A']['token_count'],3)

    def test_every_sign_including_isolates_and_length_sensitivity(self):
        summary,_,_,_=audit(records(['A X','B X','C Q R S']))
        self.assertEqual(summary['observed_signs'],7)
        self.assertEqual(summary['signs']['Q']['substitution_partner_count'],0)
        self.assertEqual(summary['length_minimum_sensitivities'][3]['pair_edges'],0)
        self.assertEqual(summary['length_minimum_sensitivities'][2]['pair_edges'],1)

    def test_reordering_rows_keeps_complete_outputs_stable(self):
        rows=records(['A X','B X','A X','C Z'])
        self.assertEqual(audit(rows),audit(list(reversed(rows))))


if __name__=='__main__':
    unittest.main()
