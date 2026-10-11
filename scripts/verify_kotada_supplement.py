"""Independently preserve exact DOCX rows; no correction of sample IDs or claims."""
import json
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from common import ROOT, sha256, write_json


def main():
    source = 'data/raw/kotada-sample-photo-2020-si.docx'
    ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with ZipFile(ROOT/source) as archive:
        xml = ET.fromstring(archive.read('word/document.xml'))
    tables = []
    for table in xml.findall('.//w:tbl', ns):
        tables.append([[''.join(t.text or '' for t in cell.findall('.//w:t', ns))
                        for cell in row.findall('w:tc', ns)]
                       for row in table.findall('w:tr', ns)])
    assert len(tables) == 2
    target_path = 'data/processed/kotada_anchor_followup.json'
    targets = {r['sample_id'] for r in json.loads((ROOT/target_path).read_text())['samples']}
    assert len(targets) == 11
    keyed = [{row[0].strip(): row for row in table if row and row[0].strip().startswith('KB-')}
             for table in tables]
    common = sorted(targets & keyed[0].keys())
    assert len(common) == 10
    assert targets - keyed[0].keys() == {'KB-61'}
    assert 'KB-60' in keyed[0] and 'KB-61' not in keyed[1]
    first, second = keyed[0]['KB-106'], keyed[1]['KB-106']
    assert 'Aquatic fat' in [c.strip() for c in first] and first[-4:] == ['-']*4
    assert second[2:] == ['-19.1', '-24.9', '-5.8', 'Ruminant dairy']
    write_json('results/kotada_supplement_independent.json', {
        'source_table_row_counts_including_headers': [len(t) for t in tables],
        'target_sample_count': len(targets),
        'exact_sample_labels_in_first_table': common,
        'unmatched_target_labels': sorted(targets-keyed[0].keys()),
        'KB60_not_merged_into_KB61': True,
        'literal_selected_rows': [{key: rows[key] for key in sorted(set(common+['KB-60']) & rows.keys())}
                                  for rows in keyed],
        'KB106_conflict': {'table1': first, 'table2': second,
                          'resolution': 'unresolved source discrepancy; no isotope assignment selected'},
        'limits': [
            'DOCX table extraction preserves individual XML cells; merged header cells are not expanded to a rectangular schema.',
            'Exact laboratory label overlap is not independently authenticated physical-object identity.',
            'No inscription photograph or quantity represented by signs is supplied by these tables.',
        ],
        'input_sha256': {p: sha256(ROOT/p) for p in [source, target_path]},
    })
    print('Kotada independent DOCX check: 10/11 labels, KB61 unmatched, KB106 discrepancy retained.')


if __name__ == '__main__': main()
