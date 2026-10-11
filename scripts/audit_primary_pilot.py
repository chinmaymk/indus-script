"""Persist a small source-linked manual transcription, preserving uncertainty.

This is not OCR evaluation data: records were selected for legibility and specific
features. Never splice across damage or silently accept source-doubtful readings.
"""
import html
import json
from PIL import Image
from common import ROOT,sha256,write_json,write_jsonl

def strict_sequence(tokens):
    if any(t['kind']!='sign' or t.get('source_doubtful',True) for t in tokens):
        return None
    return [t['sign'] for t in reversed(tokens)]

def main():
    data=json.loads((ROOT/'data/processed/primary_text_pilot.json').read_text())
    if sha256(ROOT/data['source_pdf'])!=data['source_pdf_sha256']:
        raise ValueError('Pilot source PDF changed')
    src=Image.open(ROOT/data['source_page_render'])
    sx=src.width/data['ocr_coordinate_dimensions'][0]
    sy=src.height/data['ocr_coordinate_dimensions'][1]
    records=[];sections=[];counterexamples=[]
    for line in data['lines']:
        ident=line['text_id'];tokens=line['tokens_printed_left_to_right']
        for t in tokens:
            if t['kind']=='sign' and t['sign'] not in {f'M{i:03d}' for i in range(1,418)}:
                raise ValueError(f'Invalid sign {t}')
        x1,y1,x2,y2=line['crop_box_ocr']
        dest=ROOT/f'results/primary_pages/pilot_{ident}.png'
        src.crop((int(x1*sx),int(y1*sy),int(x2*sx),int(y2*sy))).save(dest)
        sequence=strict_sequence(tokens)
        records.append({'id':'M77:'+ident,'source_pdf_page':data['pdf_page'],
            'sequence_reading_order':sequence,'tokens_printed_left_to_right':tokens,
            'strict_eligible_as_printed':sequence is not None,
            'status':'manual pilot; not independent double-entry or representative sample'})
        if sequence:
            counterexamples.extend({'text_id':ident,'reading_order_index_1_based':i+1,
                'line_sign_count':len(sequence),'claim_falsified':'M342 occurs only at line end'}
                for i,s in enumerate(sequence) if s=='M342' and i<len(sequence)-1)
        glyphs=[]
        for token in tokens:
            if token['kind']=='damage':
                glyphs.append('<span class="glyph">[damage:<br>1+ signs]</span>')
            else:
                sign=token['sign'];mark=' ? (source)' if token['source_doubtful'] else ''
                glyphs.append(f'<span class="glyph"><img src="../IM_417_150_PNG/{int(sign[1:])}.png">{sign}{mark}</span>')
        reading=' → '.join(sequence) if sequence else 'Excluded from strict sequences: damage / source-doubtful reading.'
        sections.append(f'<section><h2>Text {ident}</h2><img class="strip" src="primary_pages/pilot_{ident}.png">'
            f'<p>Transcription in printed left-to-right order:</p><div>{"".join(glyphs)}</div>'
            f'<p>Reading order (right to left on the page): {reading}</p><p>{html.escape(line["note"])}</p></section>')
    write_jsonl('results/primary_text_pilot.jsonl',records)
    write_json('results/primary_text_pilot_audit.json',{'lines':len(records),
        'strict_eligible_lines':sum(r['strict_eligible_as_printed'] for r in records),
        'strict_sign_tokens':sum(len(r['sequence_reading_order'] or []) for r in records),
        'internal_jar_witnesses':counterexamples,'selection':data['selection'],
        'limitation':'One transcription pass; witness report, not a decipherment or classifier accuracy evaluation.'})
    (ROOT/'results/primary_text_pilot.html').write_text('<!doctype html><meta charset="utf-8">'
        '<title>Primary text transcription pilot</title><style>body{font:17px system-ui;max-width:1250px;margin:2rem auto;padding:1rem}'
        'section{border-top:1px solid #aaa;margin-top:2rem;padding-top:1rem}.strip{width:100%}'
        '.glyph{display:inline-flex;vertical-align:top;flex-direction:column;align-items:center;width:125px;font-size:14px}'
        '.glyph img{width:90px;filter:invert(1)}</style><h1>Four primary-source transcription witnesses</h1>'
        '<p>Mahadevan 1977, printed p. 39, PDF p. 50. Single visual pass; purposely selected sample. '
        'Printed lines are normalized right to left by the editor; glyph orientation and original variants are also normalized. '
        'No meanings or sounds are assigned. Source damage and doubtful readings remain explicit.</p>'
        '<p><a href="../data/raw/mahadevan_1977_text.pdf#page=50">Source PDF</a> · '
        '<a href="../data/processed/primary_text_pilot.json">Editable transcription and provenance</a></p>'+''.join(sections))
    print(f'Primary pilot: {len(records)} lines; {len(counterexamples)} internal-jar witness.')

if __name__=='__main__':
    main()
