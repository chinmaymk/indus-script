"""Guard narrow whole-flank match and the invalid endpoint-permutation null."""
import unittest
from audit_patronymic_chains import split_edges, exact_chains, marginal_walk_count


class PatronymicChainTests(unittest.TestCase):
    def test_literal_whole_flanks_and_no_self_match(self):
        strings = {("A", "D", "B", "C"): ["1"],
                   ("B", "D", "E"): ["2"],
                   ("B", "C", "D", "F"): ["3"],
                   ("X", "D", "X"): ["4"]}
        chains = exact_chains(split_edges(strings, "D"))
        self.assertEqual(len(chains), 1)
        self.assertEqual(chains[0]["shared_bundle"], ["B", "C"])

    def test_no_endpoint_empty_or_repeated_delimiter_parse(self):
        strings = {("D", "A"): ["1"], ("A", "D"): ["2"],
                   ("A", "D", "B", "D", "C"): ["3"]}
        self.assertEqual(split_edges(strings, "D"), [])

    def test_right_endpoint_shuffle_keeps_marginal_walk_count(self):
        edges = [{"left": [a], "right": [b]} for a, b in
                 [("A", "B"), ("B", "C"), ("C", "A")]]
        shuffled = [{"left": [a], "right": [b]} for a, b in
                    [("A", "A"), ("B", "B"), ("C", "C")]]
        self.assertEqual(marginal_walk_count(edges), 3)
        self.assertEqual(marginal_walk_count(edges), marginal_walk_count(shuffled))
        self.assertEqual(len(exact_chains(edges)), 3)
        self.assertEqual(len(exact_chains(shuffled)), 0)


if __name__ == "__main__":
    unittest.main()
