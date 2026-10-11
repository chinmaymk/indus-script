"""Scientific-validity checks for the foreign-seal comparison."""
import math
import unittest
from analyze_m77_foreign import eligible, pair_counts, score, leave_one_out, compare

class ForeignComparisonTests(unittest.TestCase):
    def test_no_pair_crosses_string_boundary(self):
        counts=pair_counts([("M001","M002"),("M003","M004")])
        self.assertEqual(counts[("M002","M003")],0)
        self.assertEqual(sum(counts.values()),2)

    def test_complete_string_exclusion_removes_repeated_pairs(self):
        seq=("M001","M001","M001")
        counts=pair_counts([seq,("M002","M003")])
        actual=leave_one_out(seq,counts)
        self.assertEqual(actual["unseen_pair_fraction"],1)
        self.assertAlmostEqual(actual["mean_transition_surprisal_bits"],math.log2(417))
        self.assertEqual(counts[("M001","M001")],2)

    def test_shared_pairs_survive_exclusion(self):
        seq=("M001","M002")
        counts=pair_counts([seq,("M001","M002","M003")])
        actual=leave_one_out(seq,counts)
        self.assertEqual(actual["pairs"][0]["training_count"],1)
        self.assertEqual(actual["unseen_pair_fraction"],0)

    def test_doubt_loss_and_multiline_not_repaired(self):
        row={"source_object_code":"1","source_doc_count":2,"source_direction_code":"2",
             "tokens":[{"doubtful":True,"unknown_span":False},{"doubtful":False,"unknown_span":True}]}
        self.assertEqual(eligible(row),["multiple_export_documents","doubt","loss"])

    def test_add_one_probabilities_normalize_over_full_inventory(self):
        counts=pair_counts([("M001","M002"),("M001","M003")])
        probabilities=[2**(-score(("M001",f"M{i:03d}"),counts)["mean_transition_surprisal_bits"]) for i in range(1,418)]
        self.assertAlmostEqual(sum(probabilities),1)

    def test_empirical_comparison_keeps_ties_and_empty_controls(self):
        self.assertEqual(compare(0.5,[0,0.5,0.5,1])["equal"],2)
        self.assertEqual(compare(0.5,[])["count"],0)

if __name__=="__main__":
    unittest.main()

