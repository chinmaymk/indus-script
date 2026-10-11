"""Local-only H1923 locator audit and unretouched coverage crops; no value inference.

Run with bundled Python (Pillow, pypdf). Pass --render to regenerate source pages.
This writes only the uniquely prefixed audit/crop files, not the review or corpus.
"""
import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
POPPLER = Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'

def pin(path):
    b=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--render',action='store_true')
    a=p.parse_args()
    specs=[
      ('data/raw/cisi_76884.pdf',5,1200,'h1923-numeral-cisi1-title-5'),
      ('data/raw/cisi_76884.pdf',7,1200,'h1923-numeral-cisi1-title-7'),
      ('data/raw/h843_identity_CorpusVol2.pdf',4,1800,'h1923-numeral-cisi2-4'),
      ('data/raw/h843_identity_CorpusVol2.pdf',6,1800,'h1923-numeral-cisi2-contents-6')]
    if a.render:
        for src,page,scale,name in specs:
            subprocess.run([str(POPPLER),'-f',str(page),'-l',str(page),'-singlefile',
                '-scale-to',str(scale),'-png',str(ROOT/src),str(ROOT/'results/primary_pages'/name)],check=True)
    crops=[]
    for name,box,out in [
      ('h1923-numeral-cisi1-title-7',(35,985,800,1072),'h1923-numeral-cisi1-harappa-coverage'),
      ('h1923-numeral-cisi2-contents-6',(75,1425,1145,1515),'h1923-numeral-cisi2-harappa-coverage')]:
        src=f'results/primary_pages/{name}.png'; dst=f'results/primary_pages/{out}.png'
        im=Image.open(ROOT/src); im.crop(box).save(ROOT/dst)
        crops.append({'source':pin(src),'source_dimensions':list(im.size),'box_xyxy':list(box),
          'output':pin(dst),'operations':['native pixel crop'],'mirrored':False,'rotated':False})
    fields=['id','cisi','site','area-section','excavation-idno','material','preservation','type','sides','condition','complete','dir.','signs','text']
    rows=[{k:r[k] for k in fields} for r in csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open()) if r['cisi']=='H-1923']
    patterns=[r'H[\s-]*1923',r'H94[\s-]*2217',r'28\.01']
    searches=[]
    for path in ['data/raw/h843_identity_CorpusVol2_djvu.txt','data/raw/mahadevan_1977_ocr.txt',
                 'results/cisi1_extracted.txt','results/h843-cisi2_extracted.txt',
                 'data/raw/comb_tablet_kenoyer1997_web_capture.json',
                 'data/raw/comb_tablet_kenoyer2010_web_capture.json',
                 'data/raw/h1817_identity_web_captures.json']:
        txt=(ROOT/path).read_text(errors='replace')
        # Image PDFs can yield only the extractor's page separators. A null is not absence proof.
        stripped=re.sub(r'--- PDF PAGE \d+ ---','',txt).strip()
        searches.append({'source':pin(path),'nonseparator_characters':len(stripped),
          'patterns':[{'pattern':pat,'hits':[{'line':n,'text':line[:300]} for n,line in enumerate(txt.splitlines(),1) if re.search(pat,line,re.I)]} for pat in patterns],
          'negative_search_does_not_establish_absence':True})
    audit={'scope':'local locator only; no translation/transliteration fields selected',
      'secondary_source':pin('data/raw/lipi_inscriptions.csv'),'secondary_rows':rows,'searches':searches,
      'primary_page_renders':[{'pdf':pin(src),'pdf_page_1based':page,'scale_to':scale,'render':pin(f'results/primary_pages/{name}.png')} for src,page,scale,name in specs],
      'crops':crops,'new_downloads':[]}
    dest=ROOT/'data/processed/h1923_numeral_locator_audit.json'
    dest.write_text(json.dumps(audit,indent=2)+'\n')
    print(dest)

if __name__=='__main__': main()
