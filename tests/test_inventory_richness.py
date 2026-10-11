import itertools
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_inventory_richness import estimate,rarefaction

class InventoryRichnessTests(unittest.TestCase):
    def test_rarefaction_against_exhaustive_subsets(self):
        population=['A','A','B','C']
        for m in range(5):
            subsets=list(itertools.combinations(range(4),m))
            exact=sum(len({population[i] for i in subset}) for subset in subsets)/len(subsets)
            self.assertAlmostEqual(rarefaction([2,1,1],m),exact,places=12)
    def test_chao_branches_and_mass(self):
        r=estimate([1,1,2,5]);self.assertEqual(r['chao1_total_types'],6)
        self.assertAlmostEqual(r['good_turing_unseen_token_mass'],2/9)
        self.assertEqual(estimate([1,1,1,5])['chao1_total_types'],7)
    def test_duplication_is_not_new_independent_evidence(self):
        a=estimate([1,1,2,5]);b=estimate([2,2,4,10])
        self.assertEqual(a['observed_types'],b['observed_types'])
        self.assertEqual(b['good_turing_unseen_token_mass'],0)
        self.assertEqual(b['chao1_total_types'],4)
    def test_boundaries_and_rejection_of_extrapolation(self):
        self.assertEqual(rarefaction([1,2,3],0),0)
        self.assertEqual(rarefaction([1,2,3],6),3)
        for m in [-1,7,1.5]:
            with self.assertRaises(ValueError):rarefaction([1,2,3],m)
        for counts in [[],[0,0],[1,-1],[1,2.5],[True,1]]:
            with self.assertRaises(ValueError):estimate(counts)
    def test_label_invariance_and_monotonic_curve(self):
        self.assertEqual(estimate([1,2,3]),estimate([3,1,2]))
        points=[rarefaction([1,2,3],m) for m in range(7)]
        self.assertEqual(sorted(points),points)
    def test_terminal_increment_equals_singleton_mass(self):
        import csv
        source=Path(__file__).resolve().parents[1]/'data/processed/mahadevan_1977_table_i.csv'
        with source.open() as stream:
            values=[int(row['total']) for row in csv.DictReader(stream)]
        n=sum(values)
        self.assertAlmostEqual(rarefaction(values,n)-rarefaction(values,n-1),112/13372,places=11)

if __name__=='__main__':unittest.main()
