"""Package manual primary-page observations; no OCR, crosswalk or decoding inference.

Edit observations only after viewing the cited primary images. M-prefix is Mahadevan.
UNKNOWN is reviewer uncertainty; LOSS is the primary hatched uncountable passage.
A leading * records the primary doubtful-reading mark, not reviewer uncertainty.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
rows=[]

def add(page, ref, tokens, main, count=None, *, side='2', group=None, notes=None, contexts=None):
    ordinal=1+sum(r['pdf_page']==page for r in rows)
    indices=[i for i,t in enumerate(tokens) if t=='M328']
    key=indices[0]
    complete='LOSS' not in tokens
    doubt=any(t.startswith('*') for t in tokens)
    unknown=any(t.lstrip('*')=='UNKNOWN' for t in tokens)
    reasons=[]
    if not complete:reasons.append('indexed line includes loss')
    if doubt:reasons.append('indexed line includes primary doubt')
    if unknown:reasons.append('indexed line includes reviewer-unidentified glyph')
    if not main:reasons.append('other-side transcription unavailable')
    if 'LOSS' in main:reasons.append('other-side line includes loss')
    if any(t.lstrip('*')=='UNKNOWN' for t in main):reasons.append('other-side line includes reviewer-unidentified glyph')
    if any(t.startswith('*') for t in main):reasons.append('other-side line includes primary doubt')
    instances=[]
    for i in indices:
        previous=tokens[i-1] if i else None
        stroke={'M086':1,'M087':2,'M089':3,'M095':4}.get(previous.lstrip('*') if previous else None)
        instances.append({'token_index_zero_based':i,'is_R_column_reference_occurrence':i==key,
                          'immediately_preceding_token':previous,
                          'immediate_preceding_stroke_count':stroke,
                          'preceding_stroke_primary_doubt':bool(previous and previous.startswith('*')),
                          'is_final_in_this_line':i==len(tokens)-1})
    assert instances[0]['immediate_preceding_stroke_count']==count
    rows.append({'pdf_page':page,'printed_page':page-11,'reference':str(ref),'side':side,'line':'0',
                 'page_group_ordinal':ordinal,'row_locator':f'PDF{page}, indexed group{ordinal}, reference{ref}, side{side}, line0',
                 'tokens':tokens,'order':'normalized reading RTL; sequence listed first-read to last-read',
                 'M328_instances':instances,'indexed_M328_token_index_zero_based':key,
                 'immediate_preceding_stroke_count':count,
                 'preceding_stroke_form':'long vertical stroke group' if count is not None else None,
                 'observed_nonadjacent_stroke_group':group,
                 'complete_line':complete,'complete_line_definition':'No primary hatched loss passage on this displayed line; does not mean undoubted or fully decoded',
                 'primary_doubt':doubt,'reviewer_unidentified_glyph':unknown,
                 'damage_marker':'hatched loss passage, one or more unknown signs' if not complete else None,
                 'other_side_lines':[{'side':'1' if side!='1' else '2','line':'0','tokens':main,
                                      'complete_line':'LOSS' not in main,
                                      'primary_doubt':any(t.startswith('*') for t in main),
                                      'reviewer_unidentified_glyph':any(t.lstrip('*')=='UNKNOWN' for t in main),
                                      'scope':'context only; not a new indexed occurrence'}]+(contexts or []),
                 'paired_other_side_eligibility':not reasons,'paired_other_side_ineligibility_reasons':reasons,
                 'eligibility_definition':'Both displayed strings entirely identified, loss-free and free of primary doubt; artifact association itself comes from shared primary reference',
                 'notes':notes or []})

# Printed565/PDF576. Fifteen R-column groups, top to bottom.
add(576,4494,['LOSS','M328'],['UNKNOWN','UNKNOWN'],notes=['Other-side shapes not assigned numerical IDs.'])
add(576,5428,['LOSS','M328'],['LOSS','M342'])
add(576,4546,['LOSS','M328'],['LOSS','*UNKNOWN','M342'],notes=['Human-shaped other-side sign has primary doubt; not confidently identified.'])
add(576,5281,['LOSS','M328'],['LOSS','M375'])
for ref in [1623,2847]:
    add(576,ref,['M386','M053','M048','M342','UNKNOWN','M328','M328','M328','M162'],
        ['M137','M155','M343','M010','UNKNOWN','M403','M087'],side='1',
        contexts=[{'side':'3','line':'0','tokens':['M343','M294','M328','M391','M087','M112','M294','M171','M008','M342'],'scope':'context only; not the R-column reference occurrence on this page'}],
        notes=['R-column reference is first of three adjacent U signs in RTL order; other two occurrences recorded separately.',
               'Human carrying loads and bracketed complex glyph left UNKNOWN rather than choosing similar catalogue forms.',
               'Three displayed side-lines; other_side_lines are context, not separate pilot indexed rows.'])
for ref in [4487,5481]:
    add(576,ref,['UNKNOWN','M328'],['M067','M244','M342','M176'],notes=['Preceding glyph is a human/bow-like composite; unassigned exact M ID. No stroke group immediately precedes U.'])
add(576,4452,['M095','M059','M328'],['M172','M059','M347','M342','M176'],
    group={'token_index_zero_based':0,'code':'M095','observed_strokes':4,'form':'four parallel long vertical strokes','separated_from_U_by':'M059'},
    notes=['Four strokes are authenticated as M095, not M104. Fish-shaped M059 intervenes before U.'])
add(576,4552,['*M086','M328'],['M267','*M097','LOSS'],1)
add(576,4491,['M086','M328'],['*M053','M114','LOSS'],1)
add(576,4354,['*M086','M328'],['M053','M067','M059','M182','LOSS'],1)
add(576,4667,['*M086','M328'],['M387','M065','M059','M336','LOSS'],1)
for ref in [4566,5414]:add(576,ref,['*M086','M328'],['LOSS','M342','M176'],1)

# Printed566/PDF577. Sixteen indexed groups.
add(577,4661,['*M086','M328'],['M059','M182','M293','M342','M176'],1)
for ref in [4459,4515]:add(577,ref,['M087','M328'],['LOSS'],2)
add(577,5429,['*M087','M328'],['LOSS'],2)
add(577,5483,['M087','M328'],['LOSS'],2)
add(577,4381,['M087','M328'],['M048','*M047','LOSS'],2)
add(577,4700,['M087','M328'],['M112','M197','LOSS'],2)
add(577,4420,['M087','M328'],['M103','M403','M087','M244','LOSS'],2)
for ref in [5415,5420,5443]:add(577,ref,['M087','M328'],['M048','M342','LOSS'],2)
add(577,4364,['M087','M328'],['UNKNOWN'],2,notes=['Other-side human-shaped sign not assigned exact ID.'])
add(577,4479,['M087','M328'],['M067','UNKNOWN'],2,notes=['Other-side load-bearing human sign unidentified.'])
add(577,4404,['M087','M328'],['M293','M123','M343','M048','UNKNOWN'],2,notes=['Other-side load-bearing human sign unidentified.'])
add(577,5472,['M087','M328'],['M286','M087','UNKNOWN'],2,notes=['Other-side load-bearing human sign unidentified.'])
add(577,4649,['M087','M328'],['M051','M130','UNKNOWN'],2,notes=['Other-side load-bearing human sign unidentified.'])

# Printed567/PDF578. Sixteen indexed groups.
add(578,4665,['M087','M328'],['M391','M099','UNKNOWN'],2,notes=['Other-side human-shaped sign with lower appendage unidentified.'])
add(578,5303,['M167','M087','M328'],['M391','M099','UNKNOWN'],2,
    notes=['Indexed line includes extra branching M167 before the two long strokes; not reduced to stroke+U.','Other-side human-shaped sign with lower appendage unidentified.'])
add(578,4378,['M087','M328'],['UNKNOWN','M176'],2)
add(578,4357,['M087','M328'],['M042','UNKNOWN','M176'],2)
add(578,4461,['M087','M328'],['M250','UNKNOWN','M176'],2)
add(578,4475,['*M087','M328'],['M250','UNKNOWN','M176'],2)
add(578,4556,['M087','M328'],['M087','M060','M176'],2)
add(578,5323,['M087','M328'],['M065','M060','M176'],2)
for ref in [4407,5444]:add(578,ref,['M087','M328'],['M138','M176'],2)
add(578,5270,['M087','M328'],['M175','M176','M211','M176'],2)
for ref in [4610,4682,5285]:add(578,ref,['M087','M328'],['M379','M307','M176'],2)
add(578,4342,['M087','M328'],['M065','M008','M342','M176'],2)
add(578,4548,['M087','M328'],['M048','M342','M176'],2)


def main():
    assert len(rows)==47
    assert len({(r['reference'],r['side'],r['line']) for r in rows})==47
    assert Counter(r['pdf_page'] for r in rows)=={576:15,577:16,578:16}
    source=ROOT/'data/raw/mahadevan_1977_text.pdf'
    image_paths=[f'results/primary_pages/numeral-u-pilot-{p}.png' for p in [576,577,578]]
    image_paths+=['results/primary_pages/sign_list_page_32.png','results/primary_pages/sign_list-044.png','results/primary_pages/sign_list-045.png','results/primary_pages/sign_list-046.png']
    summary={'indexed_groups':len(rows),'groups_by_pdf_page':dict(Counter(r['pdf_page'] for r in rows)),
             'M328_occurrences_in_indexed_lines':sum(len(r['M328_instances']) for r in rows),
             'R_column_occurrences':len(rows),
             'immediate_preceding_stroke_count_groups':dict(Counter(str(r['immediate_preceding_stroke_count']) for r in rows)),
             'primary_doubt_groups':sum(r['primary_doubt'] for r in rows),
             'loss_marked_indexed_lines':sum(not r['complete_line'] for r in rows),
             'indexed_lines_with_reviewer_unidentified_glyph':sum(r['reviewer_unidentified_glyph'] for r in rows),
             'paired_other_side_eligible_groups':sum(r['paired_other_side_eligibility'] for r in rows)}
    result={'status':'Manual bounded primary concordance pilot; no translation or numeric values assigned',
            'source':{'path':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()},
            'protocol':{'selection':'Every R-column indexed M328 group on PDF576–578, not every contextual U occurrence; page groups enumerated top to bottom',
                        'order':'Primary normalized RTL reading order; no claims about raw object orientation',
                        'code_namespace':'Mahadevan1977 only',
                        'notation':{'*Mddd':'Primary doubtful reading','UNKNOWN':'Reviewer cannot safely identify this visible glyph; not a primary damage marker','LOSS':'Primary hatched passage of unknown positive sign extent; not a fixed sign count'},
                        'R_column':'Column aligns the indexed occurrence. All M328 in each indexed line are also inventoried, but are not extra independent indexed groups.',
                        'selection_bias':'Concordance ordering clusters similar contexts. Counts describe these selected pages, not corpus prevalence or independent artifacts.',
                        'other_sides':'Manual context transcription only. No assumption that canonical export preserves first side; no missing-line verdict or automatic join applied.',
                        'sign_authentication':{'M086':'Printed32/PDF43: one long vertical stroke','M087':'Printed32/PDF43: two long vertical strokes','M089':'Printed32/PDF43: three long vertical strokes; not used for these two-stroke lines','M095':'Printed32/PDF43: four long vertical strokes','M104':'Printed32/PDF43: four short vertical strokes; corrected from erroneous five-long-stroke label after independent review; not used in pilot rows','M167':'Printed33/PDF44: branching vertical form','M328':'Printed34/PDF45: plain U'}},
            'images':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),'visually_reviewed':True} for p in image_paths],
            'summary':summary,'rows':rows,'downloads':[]}
    (ROOT/'data/processed/m77_u_pilot_numerals.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
