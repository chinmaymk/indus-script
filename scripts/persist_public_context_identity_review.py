"""Save five manual primary catalogue observations and their metadata-only joins.

Manual observations are documentary readings, not machine-extracted discoveries.
Existing results are never overwritten. Original Lipi identifiers remain intact.
"""
from pathlib import Path
import csv
import hashlib
import json
from profile_public_context_tables import join_mackay

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/public_context_identity_five.json'
TARGETS = [
    ('180.1', 'M-584', 'DK 4807', '0779', 1, 405, 369),
    ('219.1', 'M-1140', 'DK 11340', '2188', 2, 473, 438),
    ('278.1', 'M-592', 'SD 3225', '0749', 1, 405, 369),
    ('583.1', 'M-718', 'DK 5644', '2209', 2, 470, 435),
    ('796.1', 'M-233', 'DK 10799', '2003', 1, 403, 367),
]
# Exact documentary context readings from inspected table rows, with blanks null.
CONTEXTS = {
    '3': dict(field_no='DK 10799', block=None, house=None, room=None,
              level_ft='Surface', numeric_level_ft=None, printed_page=369,
              source='data/raw/context-join-mackay-leaf391-network.jpg'),
    '188': dict(field_no='DK 11340', block='13', house='III', room='17',
                level_ft='-8.0', numeric_level_ft=-8.0, printed_page=375,
                source='data/raw/context-join-mackay-leaf397.jpg'),
    '209': dict(field_no='DK 5644', block='7', house='III', room='39',
                level_ft='-8.2', numeric_level_ft=-8.2, printed_page=376,
                source='data/raw/chain_artifact_mackay_leaf398.jpg'),
}


def pin(path):
    file = ROOT / path
    return dict(path=path, bytes=file.stat().st_size,
                sha256=hashlib.sha256(file.read_bytes()).hexdigest())


def main():
    if OUT.exists():
        raise FileExistsError('Refusing overwrite of frozen manual review')
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open(newline='') as stream:
        # Immediately project onto four metadata columns; no sign/reading fields.
        lipi = [{k: r[k] for k in ('id', 'cisi', 'site', 'excavation-idno')}
                for r in csv.DictReader(stream)]
    chosen = [r for r in lipi if r['site'] == 'Mohenjo-daro'
              and r['cisi'].strip() not in ('', '-', '--', '?', 'None', 'Unknown')
              and r['excavation-idno'].strip() not in ('', '-', '--', '?', 'None', 'Unknown')][:5]
    if [r['id'] for r in chosen] != [t[0] for t in TARGETS]:
        raise ValueError('Fixed source-order metadata targets changed')
    records, documentary_rows = [], []
    for raw, (ident, cisi, field, fc, volume, pdf, printed) in zip(chosen, TARGETS):
        if raw['id'] != ident or raw['cisi'] != cisi:
            raise ValueError('Target identity changed')
        documentary_rows.append({**raw, 'excavation-idno': field})
        records.append(dict(lipi_original_metadata=raw, cisi=cisi,
                            primary_excavation_number=field, primary_fc_number=fc,
                            primary_volume=volume, primary_pdf_page=pdf,
                            primary_printed_page=printed,
                            primary_column=3, status='documented_catalogue_field_association',
                            suffix_interpretation='No global rule inferred; original composite string retained'))
    with (ROOT / 'data/raw/public-context-oct11-mackay-seal-table.csv').open(newline='') as stream:
        table = list(csv.DictReader(stream))
    joins = join_mackay(table, documentary_rows)
    for joined in joins['eligible_joins']:
        table_row = joined['mackay_rows'][0]
        context = CONTEXTS[table_row['no']]
        for key in ('field_no', 'block', 'house', 'room'):
            if (table_row[key] or None) != context[key]:
                raise ValueError('Primary and secondary metadata differ: ' + key)
        if table_row['level_ft'].lower() != context['level_ft'].lower():
            raise ValueError('Level transcription conflict')
        joined['manual_primary_context'] = context
        joined['link_status'] = 'CISI field and Mackay row documented; original object marking not newly inspected'
    files = ['data/raw/lipi_inscriptions.csv', 'data/raw/cisi_76884.pdf',
             'data/raw/h843_identity_CorpusVol2.pdf',
             'data/raw/public-context-oct11-mackay-seal-table.csv',
             'data/raw/metal_original_mackay18225_page_numbers.json',
             'scripts/persist_public_context_identity_review.py',
             'scripts/profile_public_context_tables.py']
    files += [c['source'] for c in CONTEXTS.values()]
    files += [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'results/primary_pages').glob('context-join-*.png'))]
    result = dict(
        date='2026-10-11', scope='Five fixed catalogue associations only; no general identifier parser or corpus amendment',
        selection='First five Mohenjo-daro rows with nonmissing CISI and excavation identifiers; targets frozen in ACTIVE_STATE before primary image inspection. This file records observations afterward.',
        source_column_definitions=dict(CISI='column 1', FC='column 2 Finnish Concordance, not automatically Mahadevan', excavation='column 3',
                                       references=['CISI1 printed pp365-366 / PDF401-402', 'CISI2 printed p434 / PDF469']),
        records=records, specific_mackay_joins=joins['eligible_joins'],
        table_match_count=len(joins['eligible_joins']),
        specific_targets_without_table_match=[r for r in records if r['cisi'] in ('M-584', 'M-592')],
        supplemental_primary_context=dict(cisi='M-592', field_no='SD 3225',
            source='data/raw/context-join-mackay-leaf391-network.jpg', printed_page=369,
            form_literal='tablet; appears bronze; both sides in relief',
            area='SD', block='6', house=None, room='13', level_ft=-0.8,
            status='Explicit narrative field association; separate from seal-table sample and DK depth convention'),
        unresolved_context=[dict(cisi='M-584', reason='CISI field association verified, no primary context pixels authenticated in this bounded review')],
        outcome='Three specific seal-table associations documented, two numeric room-depth records at different loci, no replicated matched deposit comparison',
        constraints=['Original identifiers unchanged; no suffix stripping or inferred corpus-wide identities',
                     'Linked catalogue descriptions are not independent observations',
                     'CISI warns that some excavation numbers are wrong; no new object marking verification',
                     'AI-assisted public table remains unverified outside these specific rows',
                     'Room plus depth is not secure contemporaneous deposition or original use',
                     'SD narrative depth is not pooled with DK table or Marshall surface datum',
                     'No sign outcomes, translations, phonetic or semantic values used or assigned'],
        retrieval_attempts=['Sandbox DNS failures for leaves391/392 preserved; no bytes received',
                           'Successful network retrieval of leaves391/397; leaf398 already retained',
                           'Initial page-offset lead from printed363 was rejected by inspecting retained page; public chapter PDF45 corresponds to printed369'],
        evidence_pins=[pin(p) for p in dict.fromkeys(files)])
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k:result[k] for k in ('table_match_count', 'outcome')}))


if __name__ == '__main__':
    main()
