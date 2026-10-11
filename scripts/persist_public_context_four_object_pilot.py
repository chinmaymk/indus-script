"""Preserve the bounded manual four-object review; never overwrite its result."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/public_context_four_object_pilot_v1.json'


def pin(path):
    p = ROOT / path
    return dict(path=path, bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def main():
    if OUT.exists():
        raise FileExistsError('Frozen result already exists')
    protocol = 'data/processed/public_context_four_object_pilot_v1.json'
    fixed = json.loads((ROOT / protocol).read_text())
    records = []
    for target in fixed['targets']:
        cisi = target['cisi']
        available = cisi in ('M-1178', 'M-1190')
        records.append(dict(
            target=target,
            identity_status='documented_catalogue_to_table_chain' if available
                else 'unresolved_primary_evidence_unavailable',
            catalogue_observation=dict(volume=2, printed_page=438, pdf_page=473,
                field_no=target['field_no'],
                fc='1559' if cisi == 'M-1178' else '2558') if available else None,
            table_observation=dict(printed_page=386, archive_leaf=408,
                source='data/raw/m897_mackay_leaf408.jpg',
                no=target['mackay_no'], field_no=target['field_no'],
                block='2', house='IV', room='20', level_ft='-16.5', type='B')
                if available else None,
            unavailable=[] if available else [
                'CISI I covers M-1–620; II covers M-595 and M-621–1659',
                'Mackay printed379/Archive leaf401 pixels are not retained; OCR field numbers are corrupt'],
            object_marking_newly_inspected=False,
            shared_deposition_evidence='No explicit common deposition event established',
            represented_quantity_or_known_referent=None))
    sources = [protocol, fixed['input_pin']['path'],
        'data/raw/cisi_76884.pdf', 'data/raw/h843_identity_CorpusVol2.pdf',
        'data/raw/m897_mackay_leaf408.jpg',
        'data/raw/chain_artifact_mackay_leaf400.jpg',
        'data/raw/roof_u_mackay_leaf402.jpg',
        'data/raw/metal_original_mackay18225_djvu.txt',
        'data/raw/metal_original_mackay18225_page_numbers.json',
        'data/raw/public-context-oct11-mackay-seal-table.csv',
        'results/primary_pages/context-join-cisi2-473.png',
        'results/primary_pages/context-pilot-cisi2-M1178-M1190.png',
        'scripts/persist_public_context_four_object_pilot.py']
    result = dict(date='2026-10-11', protocol=protocol, status='closed_at_finite_stop',
        records=records,
        coverage_inspection=['CISI I contents III/PDF7: M-1–620',
            'CISI II contents III/PDF6: M-595, M-621–1659',
            'CISI II basic data441/PDF476 ends M-1659 then Harappa',
            'Retained Mackay leaf400 ends row305; leaf402 starts row339'],
        contextual_leads=[dict(status='OCR-only; no primary pixels authenticated',
            location='Mackay printed61–62, DK block2 houseIV',
            observation='Fragmented plan; room20/21 paving at -16.5ft reported; no DK7447/7448 deposition statement located'),
            dict(status='OCR-only; no primary pixels authenticated',
            location='Mackay printed82–83, DK block7 houseII',
            observation='Badly wrecked house, walls nearly to foundation; no DK3692/3693 shared-event statement'),
            dict(status='OCR-only contextual warning; not a new numerical datum',
            location='Mackay introduction',
            observation='DK and SD use different benchmarks; phase depths overlap amid rebuilding')],
        outcome='Two specific chains authenticated; two unavailable; zero secured shared deposits or known referents',
        limits=['Frozen targets not replaced; no acquisition during pilot',
            'Exact room/depth equality does not establish contemporaneity or original use',
            'Catalogue entries are distinct, but original object markings were not newly verified',
            'Four cases do not validate the general provisional locator rule',
            'No sign outcomes, significance tests, corpus amendments or new meanings'],
        review='Independent read-only agent authenticated later-pair coverage failure; parent inspected first pair pixels',
        evidence_pins=[pin(p) for p in sources])
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(result['outcome'])


if __name__ == '__main__':
    main()
