"""Validate the mathematical claims without assuming the historical conclusion."""
import csv
from fractions import Fraction as F
from itertools import combinations,product
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from common import ROOT
from analyze_context_bounds import probability,total_variation,intersection_bounds,validate_context

class ContextBoundsTests(unittest.TestCase):
    def test_total_variation_is_maximum_binary_mixture_gap(self):
        # A linear mixture reaches its extreme at binary per-context rates.
        for p,q in [([F(1,2),F(1,3),F(1,6)],[F(1,3)]*3),
                    ([F(1),F(0)],[F(0),F(1)]),
                    ([F(1,2)]*2,[F(1,2)]*2)]:
            maxgap=max(abs(sum((a-b)*r for a,b,r in zip(p,q,rates)))
                       for rates in product([0,1],repeat=len(p)))
            self.assertEqual(total_variation(p,q),maxgap)

    def test_intersection_bounds_are_attainable(self):
        # Exhaust all pairs of event/context subsets in a five-token population.
        universe=range(5)
        for event_n in range(6):
            for context_n in range(6):
                sizes=[len(set(e)&set(c)) for e in combinations(universe,event_n)
                       for c in combinations(universe,context_n)]
                self.assertEqual(intersection_bounds(5,event_n,context_n),(min(sizes),max(sizes)))

    def test_joint_confounding_not_excluded_by_separate_marginals(self):
        # A occupies 00 and 11, B occupies 01 and 10. Each one-variable marginal
        # is identical, but the common event rule X==Y separates A/B perfectly.
        a=[(0,0),(1,1)];b=[(0,1),(1,0)]
        for i in [0,1]:
            self.assertEqual(sorted(x[i] for x in a),sorted(x[i] for x in b))
        self.assertTrue(all(x==y for x,y in a))
        self.assertTrue(all(x!=y for x,y in b))

    def test_selected_source_rows_agree_with_position_totals(self):
        data=json.loads((ROOT/'data/processed/primary_context_subset.json').read_text())
        with (ROOT/'data/processed/mahadevan_1977_table_i.csv').open() as f:
            positions={r['sign']:{'total':int(r['total'])} for r in csv.DictReader(f)}
        validate_context(data,positions)
        data['rows'][0]['counts'][0]+=1
        with self.assertRaises(ValueError):
            validate_context(data,positions)

    def test_jar_mohenjodaro_bound_from_source_marginals(self):
        self.assertEqual(intersection_bounds(1395,971,766),(342,766))
        self.assertEqual(intersection_bounds(177,5,101),(0,5))
        self.assertEqual(F(342,766)-F(5,101),F(15356,38683))

if __name__=='__main__':
    unittest.main()
