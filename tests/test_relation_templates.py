"""Prevent invented word boundaries from becoming independent observations."""
import unittest
from itertools import product
from collections import Counter
from audit_relation_templates import parse_strings, chain_witnesses, summarize


class RelationTemplateTests(unittest.TestCase):
    def test_parse_witnesses_are_not_distinct_string_pairs(self):
        strings = {('A','A','A','D'): ['1'], ('A','A','A','A','D'): ['2']}
        out = summarize(strings, 'D', 'suffix')
        self.assertEqual(out['parse_witnesses'], 4)
        self.assertEqual(out['distinct_ordered_string_pairs'], 2)

    def test_endpoint_parser_matches_independent_overlap_oracle(self):
        bodies = [s for n in range(2, 5) for s in product(('A','B'), repeat=n)]
        expected = Counter((u, v, k) for u in bodies for v in bodies if u != v
                           for k in range(1, min(len(u), len(v))) if u[-k:] == v[:k])
        for template in ('prefix', 'suffix'):
            strings = {(('D',)+s if template == 'prefix' else s+('D',)): [str(i)]
                       for i, s in enumerate(bodies)}
            witnesses = chain_witnesses(parse_strings(strings, 'D', template))
            body_slice = slice(1, None) if template == 'prefix' else slice(None, -1)
            actual = Counter((tuple(w['first']['sequence'][body_slice]),
                              tuple(w['second']['sequence'][body_slice]),
                              len(w['shared_bundle'])) for w in witnesses)
            self.assertEqual(actual, expected)

    def test_whole_bundle_not_partial_match(self):
        strings = {('D','A','B','C'): ['1'], ('D','B','E'): ['2']}
        self.assertEqual(chain_witnesses(parse_strings(strings, 'D', 'prefix')), [])

    def test_alternative_boundaries_never_chain_to_same_string(self):
        strings = {('A','A','A','D'): ['1', '2']}
        out = summarize(strings, 'D', 'suffix')
        self.assertEqual(out['eligible_unique_strings'], 1)
        self.assertEqual(out['alternative_parses'], 2)
        self.assertEqual(out['parse_witnesses'], 0)

    def test_reversal_swaps_endpoint_templates_and_chain_order(self):
        strings = {('D','A','B','C'): ['1'], ('D','B','C','E'): ['2']}
        forward = chain_witnesses(parse_strings(strings, 'D', 'prefix'))
        reversed_strings = {tuple(reversed(s)): refs for s, refs in strings.items()}
        backward = chain_witnesses(parse_strings(reversed_strings, 'D', 'suffix'))
        self.assertEqual(len(forward), 1)
        self.assertEqual(len(backward), 1)
        self.assertEqual(forward[0]['first']['references'], backward[0]['second']['references'])
        self.assertEqual(forward[0]['shared_bundle'], list(reversed(backward[0]['shared_bundle'])))

    def test_marker_uniqueness_minimum_length_and_fixed_internal_boundary(self):
        strings = {('A','D'): ['1'], ('D','A','D','B'): ['2'], ('A','D','B','C'): ['3']}
        self.assertEqual(parse_strings(strings, 'D', 'prefix'), [])
        self.assertEqual(parse_strings(strings, 'D', 'suffix'), [])
        internal = parse_strings(strings, 'D', 'internal')
        self.assertEqual(len(internal), 1)
        self.assertEqual(internal[0]['right'], ['B', 'C'])


if __name__ == '__main__':
    unittest.main()
