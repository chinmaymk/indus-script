from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_kober_alternations import rectangle_summary
from ending_support_certificate import support_certificate


def brute_support(sequences, k):
    """Enumerate ALL distinct block permutations, independently of the criterion."""
    strata = defaultdict(list)
    for s in sequences:
        if len(s) > k:
            strata[len(s)].append(tuple(s))
    choices = []
    for seqs in strata.values():
        choices.append([tuple(s[:-k]+e for s, e in zip(seqs, blocks))
                        for blocks in set(permutations(s[-k:] for s in seqs))])
    scores = {rectangle_summary([s for stratum in option for s in stratum], k)['four_cycles']
              for option in product(*choices)}
    return max(scores) > 0


class EndingSupportTests(unittest.TestCase):
    def assert_support_matches(self, seqs, k):
        cert = support_certificate(seqs, k)
        self.assertEqual(cert['any_rectangle_in_permutation_support'], brute_support(seqs, k), (seqs, k))

    def test_exhaustive_small_same_and_different_length_marginals(self):
        # All 3^4 or 3^5 assignments for each fixed stem-slot arrangement,
        # then every distinct within-length block permutation for each assignment.
        arrangements = [ [('A',), ('A',), ('B',), ('B',)],
                         [('A',), ('A',), ('B', 'C'), ('B', 'C')],
                         [('A',), ('A',), ('A',), ('B',), ('B',)],
                         [('A',), ('A',), ('B',), ('C',)],
                         [('A',), ('A',), ('B', 'C'), ('B', 'C'), ('D',)] ]
        for stems in arrangements:
            for ends in product('XYZ', repeat=len(stems)):
                for k in (1, 2):
                    seqs = [s+((e,) if k == 1 else (e, 'Q')) for s, e in zip(stems, ends)]
                    self.assert_support_matches(seqs, k)

    def test_distinct_ending_threshold_and_copies(self):
        no = [('A', 'X')]*2+[('B', 'X')]*2
        yes = [('A', 'X')]*2+[('B', 'Y')]*2
        scarce = [('A', 'X')]*2+[('B', 'X'), ('B', 'Y')]
        self.assertFalse(support_certificate(no, 1)['any_rectangle_in_permutation_support'])
        self.assertTrue(support_certificate(yes, 1)['any_rectangle_in_permutation_support'])
        self.assertFalse(support_certificate(scarce, 1)['any_rectangle_in_permutation_support'])
        self.assertEqual(rectangle_summary(yes, 1)['four_cycles'], 0)

    def test_cross_length_intersection_requires_two_endings(self):
        one = [('A', 'X'), ('A', 'Y'), ('B', 'C', 'X'), ('B', 'C', 'Z')]
        two = one[:-1]+[('B', 'C', 'Y')]
        self.assertFalse(support_certificate(one, 1)['any_rectangle_in_permutation_support'])
        self.assertTrue(support_certificate(two, 1)['any_rectangle_in_permutation_support'])

    def test_dedup_before_shuffle_differs_from_collision_prohibition(self):
        seqs = [('A', 'X')]*2+[('B', 'Y')]*2
        self.assertTrue(support_certificate(seqs, 1)['any_rectangle_in_permutation_support'])
        self.assertFalse(support_certificate(sorted(set(seqs)), 1)['any_rectangle_in_permutation_support'])
        # Unique starting slots can collide; the original observed rectangle
        # proves feasibility, even though another permutation merges edges.
        unique = [('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')]
        self.assert_support_matches(unique, 1)

    def test_empty_singleton_and_atomic_two_sign_endings(self):
        for seqs in ([], [('X',)], [('A', 'X')], [('A', 'X'), ('B', 'Y')]):
            self.assert_support_matches(seqs, 1)
        seqs = [('A', 'X', 'Q'), ('A', 'Y', 'R'), ('B', 'X', 'Q'), ('B', 'Y', 'R')]
        self.assertTrue(support_certificate(seqs, 2)['any_rectangle_in_permutation_support'])
        self.assertFalse(support_certificate(seqs, 1)['any_rectangle_in_permutation_support'])
        for k in (0, 3, -1):
            with self.assertRaises(ValueError):
                support_certificate(seqs, k)


if __name__ == '__main__':
    unittest.main()
