import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from recover_m77_u_concordance import merge_sightings, validate_tokens, u_positions, export_comparisons


class URecoveryTests(unittest.TestCase):
    def row(self,index=0,tokens=None,side='2'):
        return {'reference':'4653','side':side,'line':'0',
                'tokens':tokens or ['M328','M328','M328'],
                'indexed_M328_token_index_zero_based':index,
                'pdf_page':594,'printed_page':583,
                'full_sequence_primary_checked':True,'ledger':'manual-test'}

    def test_three_indexed_sightings_are_one_three_token_line(self):
        lines=merge_sightings([self.row(i) for i in (2,1,0)])
        self.assertEqual(len(lines),1)
        self.assertEqual(sum(u_positions(lines[0]['tokens']).values()),3)
        with self.assertRaises(ValueError):merge_sightings([self.row(0),self.row(0)])

    def test_same_string_on_different_sides_remains_two_lines(self):
        lines=merge_sightings([self.row(0,side='1'),self.row(0,side='2')])
        self.assertEqual(len(lines),2)

    def test_conflicting_transcriptions_require_review(self):
        with self.assertRaises(ValueError):
            merge_sightings([self.row(0),self.row(1,['M328','M328','M059'])])

    def test_doubt_unknown_and_loss_are_not_interchangeable(self):
        row=self.row(1,['*UNKNOWN','M328'])
        line=merge_sightings([row])[0]
        self.assertTrue(line['has_reviewer_unknown'])
        self.assertTrue(line['has_primary_doubt'])
        self.assertFalse(line['has_primary_loss'])
        self.assertEqual(u_positions(['LOSS','M328']),{'final':1})
        for invalid in ['*LOSS','**M328','M418']:
            with self.assertRaises(ValueError):validate_tokens([invalid])

    def test_export_string_does_not_identify_which_side(self):
        lines=merge_sightings([self.row(0,['M328'],side='1'),self.row(0,['M328'],side='2')])
        candidate={'4653':{'tokens':[{'sign':'M328','doubtful':False,'unknown_span':False}]}}
        result=export_comparisons(lines,candidate)[0]
        self.assertEqual(len(result['exact_sequence_match_line_ids']),2)
        self.assertEqual(result['conditional_missing_U_count_lower_bound'],1)
        self.assertFalse(result['line_identity_established_by_sequence_match'])


if __name__=='__main__':unittest.main()
