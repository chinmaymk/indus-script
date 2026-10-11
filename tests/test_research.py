"""Tests protect scientific validity: parsing, grouping, nulls, normalization."""
import sys
import unittest
import random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from prepare_corpora import parse_lipi
from analyze_sequences import Model, entropy, mutual_information, endpoint_js, shuffle_sequences, grouped_records

class ResearchTests(unittest.TestCase):
    def row(self,text,**kw):
        r={'text':text,'complete':'Y','dir.':'R/L','class':'SS','signs':'2'}
        r.update(kw)
        return r

    def test_literal_signs_and_order(self):
        seq,reasons=parse_lipi(self.row('+740-033+'))
        self.assertEqual(seq,['W740','W033'])
        self.assertEqual(reasons,[])

    def test_damage_not_silently_removed(self):
        for s in [']740-033+','+740-000+','+740/033+','+740-999+','+740-*033+']:
            self.assertTrue(parse_lipi(self.row(s))[1])

    def test_metadata_constraints(self):
        for extra in [{'complete':'N'},{'dir.':'L/R'},{'class':'2L'},{'signs':'3'}]:
            self.assertTrue(parse_lipi(self.row('+740-033+',**extra))[1])

    def test_entropy_known_values(self):
        self.assertEqual(entropy({'a':1}),0)
        self.assertAlmostEqual(entropy({'a':1,'b':1}),1)
        self.assertAlmostEqual(mutual_information([['a','x'],['b','y']]),1)
        self.assertAlmostEqual(endpoint_js([['a','x'],['b','y']]),1)

    def test_reversal_invariance(self):
        s=[list('abbc'),list('cad'),list('a')]
        self.assertAlmostEqual(mutual_information(s),mutual_information([x[::-1] for x in s]))
        self.assertAlmostEqual(endpoint_js(s),endpoint_js([x[::-1] for x in s]))

    def test_relabeling_invariance(self):
        s=[list('abbc'),list('cad'),list('a')]
        mapping={'a':'grain','b':'king','c':'river','d':'fish'}
        renamed=[[mapping[x] for x in row] for row in s]
        self.assertAlmostEqual(mutual_information(s),mutual_information(renamed))
        self.assertAlmostEqual(endpoint_js(s),endpoint_js(renamed))

    def test_within_null_preserves_each_bag(self):
        seq=[list('abc'),list('abb'),list('ca')]
        out=shuffle_sequences(seq,random.Random(4),'within_text')
        self.assertEqual([sorted(s) for s in seq],[sorted(s) for s in out])

    def test_position_null_preserves_length_and_slot_counts(self):
        seq=[list('abc'),list('abb'),list('ccc'),list('ca'),list('bb')]
        out=shuffle_sequences(seq,random.Random(4),'length_position')
        self.assertEqual(list(map(len,seq)),list(map(len,out)))
        for length in {len(s) for s in seq}:
            for i in range(length):
                self.assertEqual(sorted(s[i] for s in seq if len(s)==length), sorted(s[i] for s in out if len(s)==length))

    def test_connected_groups_and_deduplication(self):
        recs=[{'id':'1','artifact':'A','site':'X','sequence':['a']},
              {'id':'2','artifact':'B','site':'X','sequence':['a']},
              {'id':'3','artifact':'B','site':'Y','sequence':['b']},
              {'id':'4','artifact':'C','site':'Y','sequence':['c']}]
        out=grouped_records(recs)
        self.assertEqual(len(out),3)
        d={r['sequence']:r['group'] for r in out}
        self.assertEqual(d[('a',)],d[('b',)])
        self.assertNotEqual(d[('a',)],d[('c',)])

    def test_probability_normalization_unseen_contexts(self):
        for mode in ['unigram','position','bigram','bigram_position']:
            model=Model([list('abb'),list('ca')],list('abcd'),mode,5)
            for prev in ['a','<BOS>','unseen']:
                for p in ['start','middle','end','single']:
                    probs=[model.prob(x,prev,p) for x in 'abcd']
                    self.assertAlmostEqual(sum(probs),1)
                    self.assertTrue(all(x>0 for x in probs))

    def test_renamed_models_have_same_likelihood(self):
        seq=[list('abb'),list('ca')]
        transform=lambda s:[{'a':'x','b':'y','c':'z','d':'w'}[x] for x in s]
        for mode in ['unigram','position','bigram','bigram_position']:
            a=Model(seq,list('abcd'),mode)
            b=Model([transform(s) for s in seq],list('xyzw'),mode)
            self.assertAlmostEqual(a.loss(list('dab')),b.loss(transform('dab')))

if __name__=='__main__':
    unittest.main()
