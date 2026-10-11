import copy
from collections import Counter
from pathlib import Path
import random
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_kober_alternations import (clean_rows, rectangle_summary, shuffle_endings,
                                        permutation_screen, illustrative_examples)


class KoberScreenTests(unittest.TestCase):
    def test_rectangles_require_two_distinct_stems_and_two_endings(self):
        three_corners = [('A', 'X'), ('A', 'Y'), ('B', 'X')]
        self.assertEqual(rectangle_summary(three_corners*10, 1)['four_cycles'], 0)
        full = three_corners+[('B', 'Y')]
        result = rectangle_summary(full+[('A', 'X')]*2, 1)
        self.assertEqual(result['four_cycles'], 1)
        self.assertEqual(result['eligible_rows'], 6)
        self.assertEqual(result['unique_sequences'], 4)
        self.assertEqual(result['row_witness_combinations'], 3)

    def test_choose_shared_stems_two_without_double_counting(self):
        seqs = [(stem, end) for stem in 'ABC' for end in 'XYZ']
        result = rectangle_summary(seqs, 1)
        self.assertEqual(result['shared_ending_pairs'], 3)
        self.assertEqual(result['four_cycles'], 9)

    def test_blocks_are_atomic_and_stems_nonempty_exact(self):
        seqs = [('A', 'X', 'Q'), ('A', 'Y', 'R'), ('B', 'X', 'Q'), ('B', 'Y', 'R')]
        self.assertEqual(rectangle_summary(seqs, 2)['four_cycles'], 1)
        self.assertEqual(rectangle_summary(seqs, 1)['four_cycles'], 0)
        self.assertEqual(rectangle_summary([('X', 'Q')]*4, 2)['eligible_rows'], 0)
        changed = seqs[:-1]+[('C', 'B', 'Y', 'R')]
        self.assertEqual(rectangle_summary(changed, 2)['four_cycles'], 0)

    def test_permutation_preserves_slots_lengths_and_block_multisets(self):
        seqs = [('A', 'X', 'Q'), ('A', 'Y', 'R'), ('B', 'X', 'Q'), ('C', 'D', 'Z', 'S')]
        result = shuffle_endings(seqs, 2, random.Random(10))
        self.assertEqual([s[:-2] for s in result], [s[:-2] for s in seqs])
        self.assertEqual(Counter((len(s), s[-2:]) for s in result), Counter((len(s), s[-2:]) for s in seqs))
        self.assertEqual(result[-1], seqs[-1])
        self.assertEqual(result, shuffle_endings(seqs, 2, random.Random(10)))

    def test_exclusions_consult_segments_as_well_as_tokens(self):
        def row(i, token='M001'):
            return dict(reference=str(i), side='0', line='0', normalized_order='right_to_left',
                        tokens=[token], segments=[dict(kind='identified_sign', sign=token, source_doubt=False)])
        rows = [row(i) for i in range(6)]
        rows[1]['tokens'] = ['*M001']
        rows[1]['segments'][0]['source_doubt'] = True
        rows[2]['tokens'] = ['*M001']
        rows[2]['segments'][0]['source_doubt'] = True
        rows[3]['tokens'] = ['UNKNOWN']
        rows[3]['segments'] = [dict(kind='unidentified_visible_sign', sign=None, source_doubt=False, minimum_signs=1, maximum_signs=1)]
        rows[4]['tokens'] = ['LOSS']
        rows[4]['segments'] = [dict(kind='unknown_length_loss', sign=None, source_doubt=False, minimum_signs=1, maximum_signs=None)]
        rows[5]['segments'][0]['reviewer_uncertainty'] = True
        corpus = dict(schema_version='verified-m77-1', normalized_order='right_to_left', rows=rows,
                      coverage_complete_for_manifest=True, unresolved_rows=0)
        selected, excluded = clean_rows(corpus)
        self.assertEqual(len(selected), 1)
        self.assertEqual(len(excluded), 5)
        corpus['rows'].append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            clean_rows(corpus)

    def test_reject_incomplete_or_malformed_even_after_excluded_token(self):
        corpus = dict(schema_version='verified-m77-1', normalized_order='right_to_left',
                      coverage_complete_for_manifest=True, unresolved_rows=0, rows=[
                          dict(reference='1', side='0', line='0', normalized_order='right_to_left',
                               tokens=['*M001', 'M002'], segments=[
                                   dict(kind='identified_sign', sign='M001', source_doubt=True),
                                   dict(kind='identified_sign', sign='M002', source_doubt=False)])])
        for field, value in [('coverage_complete_for_manifest', False), ('unresolved_rows', 1)]:
            bad = copy.deepcopy(corpus); bad[field] = value
            with self.assertRaisesRegex(ValueError, 'complete manifest'):
                clean_rows(bad)
        for field, value in [('sign', 'M003'), ('sign', 'M418'), ('kind', 'unknown_kind'), ('source_doubt', None)]:
            bad = copy.deepcopy(corpus); bad['rows'][0]['segments'][1][field] = value
            with self.assertRaises(ValueError):
                clean_rows(bad)
        bad = copy.deepcopy(corpus); bad['rows'][0]['segments'][1].pop('source_doubt')
        with self.assertRaises(ValueError):
            clean_rows(bad)

    def test_raw_exceedance_and_degenerate_sparse_case(self):
        result = permutation_screen([('A', 'X')], 1, 20, 1)
        self.assertEqual(result['raw_greater_or_equal_count'], 20)
        self.assertEqual(result['raw_strictly_greater_count'], 0)
        self.assertTrue(result['sampled_score_is_constant'])
        self.assertEqual(result, permutation_screen([('A', 'X')], 1, 20, 1))
        with self.assertRaises(ValueError):
            permutation_screen([], 1, 0, 1)

    def test_fixed_labels_and_grammar_have_identical_structure(self):
        examples = illustrative_examples()
        a, b = examples['invented_grammar'], examples['invented_fixed_labels']
        for field in ('stems', 'endings', 'unique_sequences', 'four_cycles', 'row_witness_combinations'):
            self.assertEqual(a[field], b[field])
        self.assertEqual(a['four_cycles'], 1)


if __name__ == '__main__':
    unittest.main()
