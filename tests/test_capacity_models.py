import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_capacity_models import fit, leave_one_out


class CapacityModelTests(unittest.TestCase):
    def test_exact_proportionality_and_scale_nonidentifiability(self):
        counts,values=[3,6,7],[120,240,280]
        self.assertEqual(fit(counts,values)['sse'],0)
        self.assertEqual(fit([n*10 for n in counts],values)['litres_per_stroke'],4)
        self.assertTrue(all(r['relative_prediction_error']==0 for r in leave_one_out(counts,values)))

    def test_held_out_value_cannot_change_its_prediction(self):
        a=leave_one_out([3,6,7],[120,240,280])
        b=leave_one_out([3,6,7],[999,240,280])
        self.assertEqual(a[0]['prediction_litres'],b[0]['prediction_litres'])
        self.assertNotEqual(a[1]['prediction_litres'],b[1]['prediction_litres'])

    def test_invalid_values(self):
        for n,v in [([],[]),([1],[2,3]),([0],[2]),([1],[float('nan')])]:
            with self.assertRaises(ValueError): fit(n,v)


if __name__=='__main__': unittest.main()
