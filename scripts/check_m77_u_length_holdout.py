"""Evaluate frozen length predictions against manually reviewed Vats table rows.

No fitting, sample selection, image recognition or automatic transcription occurs.
The primary ledger deliberately retains damage, doubtful signs and source conflicts.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    protocol_path = 'data/processed/m77_u_length_prediction_protocol.json'
    protocol = json.loads((ROOT / protocol_path).read_text())
    preread = json.loads((ROOT / 'data/processed/m77_u_length_4476_preread.json').read_text())
    assert fingerprint(protocol_path)['sha256'] == preread['protocol_sha256']
    # Explicit plate-item rows, never a 'similar to' row in the dimension table.
    rows = [
        dict(reference='4403', eh_item='403', count=3, table_length='0.55', table_width='0.3',
             table_page=347, leaf=373, material='white steatite', find_number='8102', area='F',
             depth='5ft3in', type_code='h', plate='XCV', plate_pdf_page=198,
             condition='Narrative explicitly fragmentary; photographed fragment retained.',
             narrative_length='11/20', narrative_width=None, narrative_page=72, narrative_leaf=98,
             narrative_join='Explicit EH403 and excavation8102', eligibility='damage-sensitive'),
        dict(reference='4405', eh_item='405', count=3, table_length='0.6', table_width='0.3',
             table_page=347, leaf=373, material='white steatite', find_number='2355', area='F',
             depth='15ft3in', type_code='j', plate='XCV', plate_pdf_page=198,
             condition='Both oval faces pictured; no fragmentary condition specified in joined narrative.',
             narrative_length='5/8', narrative_width='5/16', narrative_page=109, narrative_leaf=135,
             narrative_join='Table EH405 identifies find2355; narrative item6 explicitly find2355, similar to item2. Not joined merely by similar-to description.', eligibility='decisive'),
        dict(reference='4476', eh_item='476', count=4, table_length='0.4', table_width='0.3',
             table_page=349, leaf=377, material='white steatite', find_number=None, area=None,
             depth=None, type_code='h', plate='XCVI', plate_pdf_page=200,
             condition='Primary *M095 doubtful; plate shows missing upper/left portions. Four-stroke interpretation conditional.',
             narrative_length=None, narrative_width=None, narrative_page=None, narrative_leaf=None,
             narrative_join=None, eligibility='doubt-and-damage-sensitive'),
        dict(reference='4516', eh_item='516', count=4, table_length='0.55', table_width='0.3',
             table_page=349, leaf=377, material='white steatite', find_number='262', area='G',
             depth='10ft0in', type_code='h', plate='XCVII', plate_pdf_page=202,
             condition='Both rectangular faces pictured; no autopsy or completeness guarantee.',
             narrative_length=None, narrative_width=None, narrative_page=None, narrative_leaf=None,
             narrative_join='OCR lead G262 and EH516 consistent with table; narrative not visually authenticated, not used for dimensions. OCR also misreads unrelated unfinished one-face item as516; excluded.', eligibility='table-supported'),
        dict(reference='4543', eh_item='543', count=3, table_length='0.4', table_width='0.3',
             table_page=350, leaf=378, material='white steatite (table); burnt steatite (narrative)', find_number='1261', area='F',
             depth='11ft4in', type_code='i', plate='XCVII', plate_pdf_page=202,
             condition='Both oval faces pictured; no fragmentary condition specified in joined narrative.',
             narrative_length='7/16', narrative_width='5/16', narrative_page=93, narrative_leaf=119,
             narrative_join='Table EH543 identifies find1261; narrative StratumV item2 gives1261 but says similar to543. Identity rests on find number, and source wording discrepancy is retained.', eligibility='table-supported-with-narrative-wording-caveat'),
    ]
    assert [r['reference'] for r in rows] == protocol['heldout_reference_candidates']
    for row in rows:
        ref = row['reference']
        expected = (Fraction(row['count']) + 3) / 16
        if ref in protocol['predicted_lengths_before_targeted_dimension_lookup']:
            assert expected == Fraction(protocol['predicted_lengths_before_targeted_dimension_lookup'][ref])
        else:
            assert ref == '4476' and row['count'] == preread['visually_observed_long_strokes']
        row['prediction_inches'] = str(expected)
        row['table_residual_inches_exact'] = str(Fraction(row['table_length']) - expected)
        row['table_exact_match'] = Fraction(row['table_length']) == expected
        if row['narrative_length']:
            row['narrative_residual_inches_exact'] = str(Fraction(row['narrative_length']) - expected)
            row['narrative_exact_match'] = Fraction(row['narrative_length']) == expected
        row['table_image'] = f"data/raw/vats_1940_holdout_leaf{row['leaf']}.jpg"
    downloads = json.loads((ROOT / 'data/processed/m77_u_length_holdout_downloads.json').read_text())
    for entry in downloads:
        assert fingerprint(entry['path'])['sha256'] == entry['sha256']
    images = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'results/primary_pages').glob('m77-u-holdout*.png'))
    result = {
        'status': 'Frozen exact nominal length rule falsified; no represented quantity inferred',
        'protocol': fingerprint(protocol_path), '4476_preread': preread,
        'lookup_order': '4476 primary glyph observation and prediction saved before first Vats dimension search; other counts supplied in frozen protocol',
        'join': 'M77 AppendixV printed821/PDF830 explicitly maps4001–4713 to EHII items1–713. Exact numbered plates and VatsI dimension-table rows visually inspected.',
        'rows': rows,
        'summary': {'fixed_candidates': 5, 'table_dimensions_recovered': 5, 'table_exact_matches': sum(r['table_exact_match'] for r in rows),
                    'decisive_counterexample': '4405/EH405: expected3/8; table0.6 and narrative5/8, linked by exact find2355. No damage exclusion or refit rescues the frozen exact rule.'},
        'source_discrepancies': ['Vats narrative fractional and tabular decimal dimensions are not interchangeable.',
            'Training508 table0.45x0.28 vs narrative7/16x1/4;509 table0.4x0.25 vs narrative3/8x1/4;548 tableDiameter0.3 vs narrative5/16x1/4.',
            'Archive page-number metadata is locally unreliable: leaf374 is printed346, leaf373 printed347, leaf376 printed348; verify printed pages visually.',
            'Narrative similar-to543 find1261 is associated via exact table find number, not similarity alone.'],
        'limitations': ['No posthoc tolerance or revised formula tested. A decimal table mismatch alone may reflect rounding; decisive405 differs substantially in both source representations.',
            '4476 is doubtful and broken;403 is fragmentary. Neither is needed for the robust counterexample.',
            'Photographs are low-resolution halftones, not fresh measurements or autopsies.',
            'No inference about mass, vessel capacity, goods, arithmetic denominations or semantic numeric values follows.',
            'Prospective relative to targeted lookup, not externally registered or blind; training was selected posthoc.',
            'All five fixed candidates retained. Repeated inscriptions need not be independent production events.'],
        'downloads': downloads, 'images': [fingerprint(p) for p in images],
        'prior_source_fingerprints': [fingerprint(p) for p in ['data/raw/mahadevan_1977_text.pdf','data/raw/vats_1940_plates_9842.pdf','data/raw/vats_1940_text_18220_djvu.txt']],
    }
    (ROOT / 'data/processed/m77_u_length_holdout.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
