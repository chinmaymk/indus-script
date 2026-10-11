"""Package manual observations of M328 concordance PDF591–595.

Only edit the literal observations after inspecting the cited pages. This script
does not recognize glyphs or import candidate-export spellings.
"""
from collections import Counter
from common import ROOT, sha256, write_json


def observations():
    rows = []
    def add(page, ref, tokens, side=2, line=0, index=None, note=None):
        if index is None:
            positions = [i for i,t in enumerate(tokens) if t.lstrip('*') == 'M328']
            if len(positions) != 1:
                raise ValueError('Specify indexed occurrence for repeated U')
            index = positions[0]
        rows.append({'reference': str(ref), 'side': str(side), 'line': str(line),
            'pdf_page': page, 'printed_page': page-11,
            'group_on_page': 1+sum(r['pdf_page']==page for r in rows),
            'tokens': tokens, 'indexed_M328_token_index_zero_based': index,
            'full_sequence_primary_checked': True, 'actual_direction_code': None,
            'notes': [note] if note else []})
    for ref in [4516,5405,5426,5427,5430,5432,5433,5440,5447,5277,4591,4581,4522,4451,4582]:
        add(591,ref,['M095','M328'],side=3 if ref in [4591,4581] else 2)
    for ref in [4587,4448,5461,5460,4458,4544,5450,5302,4428,5471,4498,5455,4681,4683,4576]:
        add(592,ref,['M095','M328']+(['M059'] if ref in [4448,5461,5460] else []),
            side=3 if ref in [5471,4576] else 2)
    for ref in [4361,4469,4346,4406,4574,4553,4555,5418]:
        add(593,ref,['M095','M328'])
    add(593,2188,['LOSS','M123','M328','*UNKNOWN'],side=0,
        note='Load-bearing human-shaped glyph carries primary doubt; exact M code left unassigned.')
    add(593,4309,['M087','M141','M328','M328'],side=2,line=2,index=2,
        note='Corrected initial M149 guess after independent primary review: vertical inner strokes identify M141.')
    add(593,5473,['M328','UNKNOWN'],note='Human/bow-shaped composite; exact M code left unassigned.')
    add(593,1206,['M329','M212','M328'],side=0)
    add(593,7280,['LOSS','M249','M328','M086','M217','M342'],side=0)
    add(593,5325,['M280','M328','M342'])
    side3=['M343','M294','M328','M391','M087','M112','M294','M171','M008','M342']
    for ref in [1623,2847]: add(593,ref,side3.copy(),side=3,index=2)
    add(594,3234,['UNKNOWN','M326','M328','M280'],side=1,
        note='Human/bow-shaped first glyph is visible but exact M code remains unresolved.')
    add(594,2035,['M328','M328','M176','M176'],side=0,index=1)
    add(594,1477,['M328','M328','M267','M099'],side=0,index=1)
    add(594,1475,['M328','M328','M267','M099'],side=1,index=1)
    side1=['M386','M053','M048','M342','UNKNOWN','M328','M328','M328','M162']
    for ref in [1623,2847]: add(594,ref,side1.copy(),side=1,index=6,
        note='Same line as PDF576 first-U sighting; load-bearing glyph remains UNKNOWN. This sighting indexes middle U.')
    add(594,4309,['M087','M141','M328','M328'],side=2,line=2,index=3,
        note='Independent primary review confirms M141, replacing initial M149 guess.')
    for ref in [1623,2847]: add(594,ref,side1.copy(),side=1,index=7,
        note='Repeated line, now leftmost/last-read U indexed. Do not count this as another line.')
    for index in [2,1,0]: add(594,4653,['M328','M328','M328'],index=index)
    for ref in [4363,5250]: add(594,ref,['M328','M059'])
    add(594,5257,['M345','M328'],note='Independent crosscheck confirms three internal neck ticks, M345; M344 has two.')
    for ref in [5334,5311,4321,5252,5289]:
        add(595,ref,['M345','M328'],note='Three internal neck ticks checked in independent row-specific montage; M345.')
    add(595,7001,['M126','M087','M373','*M328','M162'],side=0)
    return rows


def main():
    rows=observations()
    assert Counter(r['pdf_page'] for r in rows)=={591:15,592:15,593:16,594:15,595:6}
    paths=['data/raw/mahadevan_1977_text.pdf',
           'results/primary_pages/m77-position-final-592.png']
    paths += [f'results/primary_pages/m77-u-extension-parent-{n}.png' for n in [591,593,594,595]]
    paths += [f'results/primary_pages/m77-u-extension-parent-{n}-neck.png' for n in [594,595]]
    paths += ['results/primary_pages/sign_list_page_32.png']
    paths += [f'results/primary_pages/sign_list-{n:03d}.png' for n in [44,45,46]]
    write_json('data/processed/m77_u_extension_parent.json', {
        'schema_version':1, 'review_date':'2026-09-23',
        'scope':'Every R-column indexed M328 occurrence on PDF591–595; stop after7001 before M329 block begins',
        'notation':{'UNKNOWN':'One visible glyph with unassigned M code',
                    '*UNKNOWN':'Primary-doubt marker on a visible glyph whose M code is unassigned',
                    'LOSS':'Primary hatched positive span, unknown extent; not a single sign'},
        'order':'Primary printed normalization, right to left; no actual-direction inference',
        'full_sequence_primary_checked_definition':'All displayed token slots checked in primary image; UNKNOWN retains unresolved glyph identity. No candidate-only prefix.',
        'sources':[{'path':p,'sha256':sha256(ROOT/p)} for p in paths],
        'rows':rows, 'indexed_sightings':len(rows),
        'limits':['Repeated concordance sighting is not another physical line.',
                  'No unprinted side/line concatenation; no sound or meaning assigned.',
                  'M code uncertainty remains distinct from primary damage and primary reading doubt.']})
    print('Packaged',len(rows),'manual parent sightings')


if __name__=='__main__':main()
