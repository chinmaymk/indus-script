import sys
from pathlib import Path
import unittest
import importlib.util
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
spec = importlib.util.spec_from_file_location('iconography_workflow', Path(__file__).resolve().parents[1] / 'scripts/audit_iconography_theory.py')
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)
parse_record, transfer_scan = workflow.parse_record, workflow.transfer_scan


def row(artifact='H-1', text='+753+', symbol='Hare', **kwargs):
    return dict(id='1.1', cisi=artifact, type='SEAL:S', site='Harappa',
                condition='Good', **{'dir.': 'R/L', 'class': 'SS', 'signs': str(text.count('-')+1),
                'complete': 'Y', 'text': text, 'symbol': symbol, 'cult': 'None'}, **kwargs)


BRIDGE = {'singleton': 'W753', 'shared_sequence': ['W740', 'W615'], 'motif_label': 'Hare',
          'donors': [{'artifact': 'M-1'}], 'motif_rows': [{'artifact': 'M-2'}]}


class IconographyTheoryTests(unittest.TestCase):
    def test_nonmatching_label_is_operational_counterexample_not_missing(self):
        result = transfer_scan([row(symbol='Bull1:I'), row(artifact='H-2', symbol='None')], [BRIDGE])
        self.assertEqual(len(result['transfer_witnesses']), 1)
        self.assertFalse(result['transfer_witnesses'][0]['observed_label_in_discovery_set'])

    def test_full_text_requires_exact_order_and_length(self):
        result = transfer_scan([row(text='+740-615+'), row(artifact='H-2', text='+615-740+'),
                                row(artifact='H-3', text='+740-615-001+')], [BRIDGE])
        self.assertEqual(len(result['transfer_witnesses']), 1)
        self.assertEqual(result['transfer_witnesses'][0]['mode'], 'whole_text_equality')

    def test_discovery_artifact_and_duplicate_are_not_extra_targets(self):
        result = transfer_scan([row(artifact='M-1'), row(), row()], [BRIDGE])
        self.assertEqual(len(result['transfer_witnesses']), 1)
        self.assertEqual(result['denominators']['duplicate_rows_removed'], 1)

    def test_nr_exception_is_only_singleton(self):
        single = row(); single['dir.'] = 'NR'
        multi = row(text='+740-615+'); multi['dir.'] = 'NR'
        self.assertEqual(parse_record(single)[1], [])
        self.assertIn('direction_not_R/L', parse_record(multi)[1])


if __name__ == '__main__':
    unittest.main()
