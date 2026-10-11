import sys
from pathlib import Path
import unittest
from itertools import combinations

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_roof_transfer_support import two_disjoint_edges, grouped_occurrences, root_support, analyze, metadata_label

PAIRS = [{'base': 'A', 'roof': 'B', 'root': 'fish'},
         {'base': 'C', 'roof': 'D', 'root': 'fish'},
         {'base': 'E', 'roof': 'F', 'root': 'cross'}]


def record(id, seq, ref=None, site='Site', strict=True):
    return {'id': id, 'source_reference': ref or id, 'site_label_unverified': site,
            'source_object_code': '1', 'strict_candidate': strict,
            'tokens': [{'sign': s, 'doubtful': False, 'unknown_span': False} for s in seq]}


def occurrence(id, component, state, pair=0, position=0):
    return {'id': id, 'component': component, 'state': state, 'pair_index': pair,
            'root': 'fish', 'site_label_unverified': 'Site', 'object_code': '1',
            'length': 3, 'position': position}


class RoofTransferSupportTests(unittest.TestCase):
    def test_exhaustive_threshold_against_four_vertex_partition_oracle(self):
        # Independent oracle: every two-edge matching partitions four vertices
        # into one of three possible pairings. Check all 1,024 five-vertex graphs.
        vertices = tuple('abcde')
        possible = list(combinations(vertices, 2))
        for mask in range(1 << len(possible)):
            edges = {edge for i, edge in enumerate(possible) if mask >> i & 1}
            expected = False
            for a, b, c, d in combinations(vertices, 4):
                pairings = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
                if any(first in edges and second in edges for first, second in pairings):
                    expected = True
            found = two_disjoint_edges(edges)
            self.assertEqual(bool(found), expected, msg=f'graph mask {mask}')
            if found:
                self.assertEqual(len(set(found[0] + found[1])), 4)
                self.assertTrue(all(tuple(edge) in edges for edge in found))

    def test_missing_metadata_normalization(self):
        for value in (None, '', '  ', ' Unknown ', '<UNKNOWN>', 'null', 'None', '?'):
            self.assertEqual(metadata_label(value), '<unknown>')
        self.assertEqual(metadata_label(' Harappa '), 'Harappa')

    def test_threshold_general_graph_not_bipartite_copy(self):
        self.assertIsNone(two_disjoint_edges([('a','b'),('b','c'),('c','a')]))
        self.assertIsNone(two_disjoint_edges([('a','b'),('a','c'),('a','d')]))
        self.assertEqual(two_disjoint_edges([('a','b'),('b','c'),('c','d')]), [['a','b'],['c','d']])
        self.assertIsNone(two_disjoint_edges([('a','a'),('a','b'),('b','a')]))

    def test_mixed_component_cannot_pair_with_itself_or_twice(self):
        rows = [occurrence('a0','a',0), occurrence('a1','a',1),
                occurrence('b0','b',0), occurrence('c1','c',1)]
        support = root_support(rows, 'fish', True)
        self.assertFalse(support['threshold_pass'])
        self.assertEqual(support['mixed_components'], 1)
        rows.append(occurrence('d0','d',0))
        self.assertTrue(root_support(rows, 'fish', True)['threshold_pass'])

    def test_pair_and_position_strata_cannot_be_crossed(self):
        rows = [occurrence('a','a',0,0), occurrence('b','b',1,1),
                occurrence('c','c',0,0,0), occurrence('d','d',1,0,1)]
        self.assertEqual(root_support(rows, 'fish', True)['distinct_component_edges'], [])

    def test_same_component_across_strata_used_once(self):
        rows = [occurrence('a0','a',0,0), occurrence('b1','b',1,0),
                occurrence('a2','a',0,1), occurrence('c3','c',1,1)]
        support = root_support(rows, 'fish', True)
        self.assertEqual(len(support['distinct_component_edges']), 2)
        self.assertFalse(support['threshold_pass'])

    def test_transitive_reference_and_all_root_formula_grouping(self):
        records = [record('a',['A','X'],ref='r'), record('b',['E','Y'],ref='r',site=None),
                   record('c',['B','Y']), record('d',['F','Z'])]
        occ, groups, _ = grouped_occurrences(records, PAIRS, True)
        by_id = {o['record_id']: o['component'] for o in occ}
        self.assertEqual(by_id['a'],by_id['b'])
        self.assertEqual(by_id['b'],by_id['c'])
        self.assertNotEqual(by_id['c'],by_id['d'])
        self.assertEqual(len(groups), 2)
        result = analyze(records, PAIRS, True, True)
        held = next(f for f in result['folds'] if f['held_out_root']=='cross')
        self.assertEqual(held['remaining_training_roots']['fish']['occurrences'], 0)

    def test_damage_and_strict_eligibility(self):
        records = [record('a',['A','X']),record('b',['B','Y'],strict=False),
                   record('c',['A']),record('d',['B','Z'])]
        records[-1]['tokens'][1]['unknown_span'] = True
        self.assertEqual(len(grouped_occurrences(records, PAIRS, True)[0]), 1)
        self.assertEqual(len(grouped_occurrences(records, PAIRS, False)[0]), 2)

    def test_post_purge_training_gate_not_marginal_gate(self):
        # Every root has marginal matching support, but all its groups leak into other roots.
        pairs=[{'base':a,'roof':b,'root':r} for a,b,r in [('A','B','a'),('C','D','b'),('E','F','c')]]
        records=[]
        for root,(base,roof) in enumerate([('A','B'),('C','D'),('E','F')]):
            for i,(sign,context) in enumerate([(base,'W'),(base,'X'),(roof,'Y'),(roof,'Z')]):
                records.append(record(f'{root}-{i}',[sign,context]))
        result=analyze(records,pairs,True,True)
        self.assertEqual(len(result['summary']['marginal_roots_passing']),3)
        self.assertEqual(result['summary']['held_out_roots_passing_proxy_gate'],[])


if __name__ == '__main__':
    unittest.main()
