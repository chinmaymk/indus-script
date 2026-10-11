import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import importlib.util
spec=importlib.util.spec_from_file_location('structure_theory_model',Path(__file__).resolve().parents[1]/'scripts/analyze_structure_theory.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ContextModel,context_keys,grouped_with_metadata,synthetic_records=(module.ContextModel,module.context_keys,module.grouped_with_metadata,module.synthetic_records)

class StructureTheoryTests(unittest.TestCase):
    def test_no_target_or_future_in_features(self):
        a=list('ABCDEFG')
        b=list('ABCXXXX')
        self.assertEqual(context_keys(a,3),context_keys(b,3))
        self.assertIsNone(context_keys(a,2)[3])
        self.assertEqual(context_keys(a,3)[3][1:],(a[0],tuple(a[1:3])))

    def test_probabilities_normalized_in_unseen_context(self):
        rows=[dict(sequence=list('ABACA'),metadata=(('site','type'),))]
        for metadata in [False,True]:
            model=ContextModel(rows,list('ABCD'),20,metadata)
            for seq in [list('ABACA'),list('DDDDD')]:
                probs=[model.probabilities(x,seq,4,(('site','type'),)) for x in 'ABCD']
                controls=[model.refinement_controls(x,seq,4,(('site','type'),)) for x in 'ABCD']
                for k in range(2):
                    self.assertAlmostEqual(sum(p[k] for p in controls),1)
                    self.assertTrue(all(p[k]>0 for p in controls))
                for k in range(4):
                    self.assertAlmostEqual(sum(p[k] for p in probs),1)
                    self.assertTrue(all(p[k]>0 for p in probs))

    def test_groups_keep_artifacts_and_duplicate_text_together(self):
        rows=[dict(id=str(i),artifact=a,sequence=list(s),site='site',type='type')
              for i,(a,s) in enumerate([('A','ABCD'),('B','ABCD'),('B','EFGH'),('C','EFGH')])]
        grouped=grouped_with_metadata(rows)
        self.assertEqual(len(grouped),2)
        self.assertEqual(len({r['group'] for r in grouped}),1)
        self.assertEqual(len({r['fold'] for r in grouped}),1)

    def test_unseen_higher_context_backs_off_exactly(self):
        model=ContextModel([dict(sequence=list('ABACA'))],list('ABCD'))
        p=model.probabilities('A',list('DABCA'),4)
        self.assertEqual(p[2],p[3])

    def test_controls_reproducible_and_distinct(self):
        a,v=synthetic_records('order_one',10)
        self.assertEqual((a,v),synthetic_records('order_one',10))
        self.assertNotEqual(a,synthetic_records('remote_memory',10)[0])

if __name__=='__main__':
    unittest.main()
