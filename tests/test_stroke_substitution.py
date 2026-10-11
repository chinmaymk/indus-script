"""Prevent partial-context and multi-position changes becoming exact substitutions."""
import unittest
from itertools import combinations, product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_stroke_substitution import analyze, frame_index


class StrokeSubstitutionTests(unittest.TestCase):
    def test_common_anchor_does_not_hide_prefix_change(self):
        strings = {('M001', 'M102', 'M287', 'M342'): ['a'],
                   ('M002', 'M106', 'M287', 'M342'): ['b']}
        result = analyze(strings)
        self.assertEqual(result['shared_frame_counts']['all'], 0)
        self.assertEqual(len(result['anchor_occurrences']), 2)

    def test_exact_context_counts_once_despite_repeated_objects(self):
        result = analyze({('M001', 'M102', 'M287', 'M342'): ['a', 'b'],
                          ('M001', 'M106', 'M287', 'M342'): ['c']})
        self.assertEqual(result['shared_frame_counts']['followed_by_anchor'], 1)
        self.assertEqual(result['samples'], {'records': 3, 'unique_strings': 2})
        self.assertEqual(result['shared_full_frames'][0]['members']['M102']['references'], ['a', 'b'])

    def test_anchor_at_end_is_distinct_from_medial_anchor(self):
        strings = {('M102', 'M287', 'M342', 'M001'): ['a'],
                   ('M106', 'M287', 'M342', 'M001'): ['b']}
        row = analyze(strings)['shared_full_frames'][0]
        self.assertTrue(row['slot_followed_by_anchor'])
        self.assertFalse(row['anchor_at_end'])

    def test_mask_index_matches_exhaustive_hamming_oracle(self):
        strings = {seq: [str(i)] for i, seq in enumerate(
            seq for n in range(1, 5) for seq in product(('M102', 'M106'), repeat=n))}
        expected = {tuple(sorted((a, b))) for a, b in combinations(strings, 2)
                    if len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1}
        observed = set()
        for members in frame_index(strings).values():
            for a, b in combinations(members.values(), 2):
                observed.add(tuple(sorted((tuple(a['sequence']), tuple(b['sequence'])))))
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
