import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_copper_bridges import find_bridges, select_rows


def row(id, cisi, text, symbol='None', direction='R/L', condition='Good'):
    return dict(id=id, cisi=cisi, text=text, symbol=symbol, cult='None',
                **{'type':'TAB:C', 'site':'Mohenjo-daro', 'condition':condition,
                   'dir.':direction, 'class':'PN', 'signs':str(text.count('-')+1),
                   'complete':'Y'})


class CopperBridges(unittest.TestCase):
    def test_nr_only_for_singleton_and_unknowns_rejected(self):
        kept, excluded = select_rows([row('1.1','M-1','+777+',direction='NR'),
            row('2.1','M-2','+740-001+',direction='NR'),
            row('3.1','M-3','+000+',direction='NR')])
        self.assertEqual([r['id'] for r in kept], ['1.1'])
        self.assertEqual(len(excluded), 2)

    def test_same_text_bridge_is_not_sign_merger(self):
        raw = [row('1.1','M-1','+777+',direction='NR'), row('1.2','M-1','+740-001+'),
               row('2.1','M-2','+740-001+','Hare'),
               row('3.1','M-3','+740-002+','Elep')]
        bridges = find_bridges(select_rows(raw)[0])
        self.assertEqual(len(bridges),1)
        self.assertEqual(bridges[0]['motif_label'],'Hare')
        self.assertEqual(bridges[0]['donor_artifact_count'],1)

    def test_poor_donor_removed_and_duplicate_motif_artifact_counted_once(self):
        raw = [row('1.1','M-1','+777+',direction='NR',condition='Poor'),
               row('1.2','M-1','+740-001+',condition='Poor'),
               row('2.1','M-2','+740-001+','Hare'), row('2.2','M-2','+740-001+','Hare')]
        self.assertEqual(find_bridges(select_rows(raw)[0])[0]['motif_artifact_count'],1)
        self.assertEqual(find_bridges(select_rows(raw, {'Good','Fair'})[0]),[])

    def test_ambiguous_donor_and_motif_bearing_donor_rejected(self):
        base = [row('1.1','M-1','+777+',direction='NR'), row('1.2','M-1','+740-001+'),
                row('2.1','M-2','+740-001+','Hare')]
        self.assertEqual(find_bridges(select_rows(base+[row('1.3','M-1','+781+',direction='NR')])[0]),[])
        base[0]['symbol']='Hare'
        self.assertEqual(find_bridges(select_rows(base)[0]),[])


if __name__ == '__main__':
    unittest.main()
