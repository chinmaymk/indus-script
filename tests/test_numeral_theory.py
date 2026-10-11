import itertools
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_numeral_theory import maximal_runs, descents, unique_runs, select_rows, models


class NumeralTheoryTests(unittest.TestCase):
    def test_unknown_signs_are_boundaries_not_deleted(self):
        classes={'long':['W031'], 'short':['W002']}
        runs=list(maximal_runs(['W031','W999','W002','W031'],classes))
        self.assertEqual([r['tokens'] for r in runs],[['W031'],['W002','W031']])
        self.assertEqual([r['start'] for r in runs],[0,2])
        with self.assertRaises(ValueError):
            list(maximal_runs([],{'a':['W031'],'b':['W031']}))

    def test_exact_minimum_boundaries_matches_exhaustive_partitions(self):
        order=['long','short','stacked']
        for length in range(1,6):
            for seq in itertools.product(order,repeat=length):
                minimum=length-1
                for bits in itertools.product((0,1),repeat=length-1):
                    cuts=[0]+[i+1 for i,b in enumerate(bits) if b]+[length]
                    fields=[seq[a:b] for a,b in zip(cuts,cuts[1:])]
                    if all(list(f)==sorted(f,key=order.index) for f in fields):
                        minimum=min(minimum,sum(bits))
                self.assertEqual(len(descents(seq,order,{})),minimum)

    def test_return_to_first_class_refutes_both_orders(self):
        for model in models():
            self.assertTrue(descents(['long','short','long'],model['order'],model['merge']))
        self.assertFalse(descents(['long','long'],['long','short'],{}))

    def test_dedup_keeps_distinct_artifacts_but_not_duplicate_export_rows(self):
        rows=[dict(artifact='H-1',sequence=['W031','W002'],start=0,tokens=['W031','W002']),
              dict(artifact='H-1',sequence=['W031','W002'],start=0,tokens=['W031','W002']),
              dict(artifact='H-2',sequence=['W031','W002'],start=0,tokens=['W031','W002'])]
        self.assertEqual(len(unique_runs(rows,'artifact_text_runs')),2)
        self.assertEqual(len(unique_runs(rows,'text_runs')),1)

    def test_lr_sensitivity_never_accepts_damage(self):
        good=dict(id='1.1',cisi='H-1',text='+031-002+',**{'dir.':'L/R'},complete='Y',
                  **{'class':'2'},signs='2',condition='Good',preservation='complete',type='TAB',site='H')
        bad=dict(good,id='2.1',complete='N')
        self.assertEqual(len(select_rows([good,bad],False)[0]),0)
        selected,excluded=select_rows([good,bad],True)
        self.assertEqual([r['id'] for r in selected],['1.1'])
        self.assertIn('not_marked_complete',excluded[0]['reasons'])


if __name__=='__main__':
    unittest.main()
