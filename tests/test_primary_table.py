"""Primary-source checks: uncertainty, coverage, printed invariants, stale artifacts."""
import copy
import csv
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from common import ROOT
from extract_primary_table import parse_cell, validate_rows
from audit_primary_pilot import strict_sequence

class PrimaryTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT/'data/processed/mahadevan_1977_table_i.csv').open() as f:
            cls.rows=list(csv.DictReader(f))

    def test_ocr_uncertainty_is_explicit(self):
        self.assertEqual(parse_cell('1395'),(1395,'literal_numeric_OCR'))
        self.assertEqual(parse_cell('O'),(0,'normalized_OCR_requires_review'))
        for raw in ['', '1 2', '2?', 'S', '−1', '١']:
            self.assertEqual(parse_cell(raw),(None,'unresolved_OCR'))

    def test_printed_constraints(self):
        validate_rows(self.rows)

    def test_primary_anchor_readings(self):
        bysign={r['sign']:r for r in self.rows}
        # Visually read from Table I, printed p. 722.
        fields=['solus','initial','medial','final','total']
        self.assertEqual([int(bysign['M342'][f]) for f in fields],[3,1,420,971,1395])
        self.assertEqual([int(bysign['M343'][f]) for f in fields],[0,20,152,5,177])

    def test_pilot_does_not_splice_across_damage_or_doubt(self):
        sign={'kind':'sign','sign':'M342','source_doubtful':False}
        self.assertIsNone(strict_sequence([sign,{'kind':'damage','minimum_lost_signs':1}]))
        self.assertIsNone(strict_sequence([dict(sign,source_doubtful=True),sign]))

    def test_pilot_printed_order_is_reversed_once(self):
        tokens=[{'kind':'sign','sign':s,'source_doubtful':False} for s in ['M342','M099','M267']]
        self.assertEqual(strict_sequence(tokens),['M267','M099','M342'])

    def test_missing_duplicate_or_edited_rows_rejected(self):
        cases=[self.rows[:-1],self.rows[:-1]+[self.rows[0]]]
        changed=copy.deepcopy(self.rows)
        changed[0]['total']=str(int(changed[0]['total'])+1)
        cases.append(changed)
        changed=copy.deepcopy(self.rows)
        changed[0]['medial']=''
        cases.append(changed)
        for rows in cases:
            with self.assertRaises(ValueError):
                validate_rows(rows)

if __name__=='__main__':
    unittest.main()
