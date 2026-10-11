import sys
from pathlib import Path
import random
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_roof_modifier import frames, comparable, distinct_witnesses, shuffle_masks, signed_score, analyze


def row(ref, seq, **changes):
    r = {'source_reference': ref, 'tokens': [{'sign': s, 'doubtful': False, 'unknown_span': False} for s in seq],
         'strict_candidate': True, 'site_label_unverified': 'A', 'source_object_code': '1'}
    r.update(changes)
    return r


class RoofTests(unittest.TestCase):
    def test_injective_witness_not_union_size(self):
        self.assertIsNone(distinct_witnesses([{'a'}, {'a'}, {'b', 'c'}, {'d'}]))
        found = distinct_witnesses([{'a', 'b'}, {'a'}, {'c'}, {'d'}])
        self.assertEqual(found, ['b', 'a', 'c', 'd'])

    def test_damage_is_excluded_not_deleted_to_join(self):
        pairs = [{'base': 'M059', 'roof': 'M065', 'root': 'fish'}]
        bad = row('2', ['M001', 'M059', 'M002'])
        bad['tokens'][0]['unknown_span'] = True
        indexed, counts = frames([row('1', ['M059']), bad,
                                  row('3', ['M001', 'M065', 'M002'])], pairs, True, True)
        self.assertEqual(len(indexed[0]), 1)
        f = next(iter(indexed[0]))
        self.assertEqual(f[4:], (('M001',), ('M002',)))
        self.assertEqual(indexed[0][f][2], {'3'})
        self.assertEqual(counts['excluded']['any_doubt_or_loss'], 1)

    def test_root_exclusion_and_mixed_zero(self):
        pairs = [{'root': 'fish'}, {'root': 'fish'}, {'root': 'cross'}]
        self.assertEqual(comparable(pairs), [(0, 2), (1, 2)])
        f = ('A', '1', 2, 0, (), ('M001',))
        self.assertEqual(signed_score([{f: 3}, {f: 1}, {f: 2}], comparable(pairs)), -1)

    def test_shuffle_preserves_strata_and_coverage(self):
        f = ('A', '1', 2, 0, (), ('M001',)); g = f[:5] + (('M002',),)
        h = ('B', '1', 2, 0, (), ('M001',))
        before = [{f: 1, g: 2, h: 3}]
        after = shuffle_masks(before, random.Random(5))
        self.assertEqual(set(after[0]), {f, g, h})
        self.assertEqual(sorted(after[0][x] for x in (f, g)), [1, 2])
        self.assertEqual(after[0][h], 3)

    def test_rectangle_requires_both_states_and_same_metadata(self):
        pairs = [{'base': 'M059', 'roof': 'M065', 'root': 'fish'},
                 {'base': 'M162', 'roof': 'M163', 'root': 'trident'}]
        rows = [row('a', ['M059', 'M001']), row('b', ['M162', 'M001']),
                row('c', ['M065', 'M002']), row('d', ['M163', 'M002'])]
        self.assertEqual(analyze(rows, pairs, True, True)['summary']['rectangles_with_four_distinct_references'], 1)
        rows[2]['source_object_code'] = rows[3]['source_object_code'] = '2'
        self.assertEqual(analyze(rows, pairs, True, True)['summary']['candidate_rectangles'], 0)
        self.assertEqual(analyze(rows, pairs, True, False)['summary']['rectangles_with_four_distinct_references'], 1)


if __name__ == '__main__':
    unittest.main()
