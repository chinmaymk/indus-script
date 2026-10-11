"""Independent overlap oracle and ambiguity counterexamples for triple paths."""
import unittest
from itertools import permutations, product
from audit_relation_templates import parse_strings, chain_witnesses
from audit_consistent_chains import compose_paths


def analyze(strings, template='suffix'):
    return compose_paths(chain_witnesses(parse_strings(strings, 'D', template)))


def counts_by_triple(result):
    return {tuple(tuple(s) for s in row['strings']): (
        row['pair_witness_combinations'], row['compatible_parse_realizations'])
        for row in result['triples']}


class ConsistentChainTests(unittest.TestCase):
    def test_duplicate_witnesses_are_rejected_instead_of_inflating_counts(self):
        witnesses = chain_witnesses(parse_strings({tuple('abD'): ['1'],
                                                  tuple('bcD'): ['2']}, 'D', 'suffix'))
        self.assertEqual(len(witnesses), 1)
        with self.assertRaises(ValueError):
            compose_paths(witnesses + witnesses)

    def test_incompatible_middle_boundary_is_rejected(self):
        strings = {tuple(s): [str(i)] for i, s in enumerate(['xabD', 'abcD', 'bcyD'])}
        result = analyze(strings)
        self.assertEqual(result['naive_distinct_ordered_triples'], 1)
        self.assertEqual(result['compatible_distinct_ordered_triples'], 0)
        self.assertEqual(result['incompatible_distinct_ordered_triples'], 1)

    def test_one_compatible_realization_suffices_among_alternatives(self):
        strings = {tuple(s): [str(i)] for i, s in enumerate(['aaD', 'aaaaD', 'aaaaaD'])}
        row = counts_by_triple(analyze(strings))[
            (tuple('aaD'), tuple('aaaaD'), tuple('aaaaaD'))]
        self.assertEqual(row, (3, 1))

    def test_two_strings_cannot_make_a_three_distinct_string_path(self):
        strings = {tuple('aaaD'): ['1', '2'], tuple('aaaaD'): ['3']}
        self.assertEqual(analyze(strings)['naive_distinct_ordered_triples'], 0)

    def test_exhaustive_terminal_overlap_length_oracle(self):
        bodies = [s for n in range(2, 5) for s in product('AB', repeat=n)]
        overlap = {(u, v): [k for k in range(1, min(len(u), len(v)))
                           if u[-k:] == v[:k]]
                   for u in bodies for v in bodies if u != v}
        expected = {}
        for u, v, w in permutations(bodies, 3):
            left, right = overlap[u, v], overlap[v, w]
            if left and right:
                expected[u, v, w] = (len(left) * len(right), sum(
                    i + j == len(v) for i in left for j in right))
        for template in ['prefix', 'suffix']:
            decorate = lambda b: ('D',) + b if template == 'prefix' else b + ('D',)
            actual = counts_by_triple(analyze({decorate(b): [str(i)]
                                              for i, b in enumerate(bodies)}, template))
            oracle = {tuple(decorate(b) for b in triple): count
                      for triple, count in expected.items()}
            self.assertEqual(actual, oracle)

    def test_internal_fixed_boundary_has_no_inconsistent_triples(self):
        strings = {(a, 'D', b): [str(i)] for i, (a, b) in enumerate(product('ABC', repeat=2))}
        result = analyze(strings, 'internal')
        self.assertGreater(result['naive_distinct_ordered_triples'], 0)
        self.assertEqual(result['incompatible_distinct_ordered_triples'], 0)
        self.assertEqual(result['naive_distinct_ordered_triples'],
                         result['compatible_parse_realizations'])

    def test_reversal_maps_all_triples_and_their_realization_counts(self):
        bodies = [s for n in range(2, 5) for s in product('AB', repeat=n)]
        strings = {('D',)+b: [str(i)] for i, b in enumerate(bodies)}
        forward = counts_by_triple(analyze(strings, 'prefix'))
        backward = counts_by_triple(analyze({s[::-1]: refs for s, refs in strings.items()}, 'suffix'))
        mapped = {tuple(s[::-1] for s in triple[::-1]): counts
                  for triple, counts in forward.items()}
        self.assertEqual(mapped, backward)

    def test_nonkinship_category_model_has_many_consistent_paths(self):
        for q in [2, 3, 4]:
            signs = tuple(str(i) for i in range(q))
            strings = {(a, b, 'D'): [str(i)] for i, (a, b) in enumerate(product(signs, repeat=2))}
            result = analyze(strings)
            self.assertEqual(result['compatible_distinct_ordered_triples'], q**4 - 3*q*q + 2*q)
            self.assertEqual(result['incompatible_distinct_ordered_triples'], 0)


if __name__ == '__main__':
    unittest.main()
