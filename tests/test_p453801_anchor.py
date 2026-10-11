import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_p453801_anchor import parse_atf,compare_lines,usable_shared_seal_ids

class AnchorAuditTests(unittest.TestCase):
    def test_language_and_unread_seal_remain_separate(self):
        text='&P1 = Test\n#atf: lang sux\n@obverse\n1. name\n#tr.en: for somebody\n@seal 1\n$ illegible\n'
        result=parse_atf(text)
        self.assertEqual(len(result['lines']),1)
        self.assertEqual(result['annotations'],[{'section':'seal 1','status':'illegible'}])
        self.assertNotIn('seal_language',result)

    def test_damage_and_spelling_changes_not_normalized_away(self):
        a=parse_atf('&P1 = Test\n@reverse\n1. en-lil2 na-na-za\n')
        b=parse_atf('&P1 = Test\n@reverse\n1. {d}en#-[lil2] na-na-sa3\n')
        diff=compare_lines(a,b)
        self.assertEqual(diff[0]['right'],'{d}en#-[lil2] na-na-sa3')

    def test_shared_placeholder_is_not_an_identity_join(self):
        def rec(i,label,number):return {'seals':[{'seal':{'id':i,'designation':label,'seal_no':number}}]}
        dummy=rec(533185,'dummy composite seal for unidentified seals','S999999')
        self.assertEqual(usable_shared_seal_ids(dummy,dummy),[])
        real=rec(123,'specific catalogue seal','S123')
        self.assertEqual(usable_shared_seal_ids(real,real),[123])

    def test_repeated_line_numbers_on_different_faces_preserved(self):
        a=parse_atf('&P1 = Test\n@obverse\n1. a\n@reverse\n1. b\n')
        b=parse_atf('&P1 = Test\n@obverse\n1. a\n@reverse\n1. c\n')
        self.assertEqual(compare_lines(a,b),[{'section':'reverse','label':'1','left':'b','right':'c'}])

if __name__=='__main__':unittest.main()
