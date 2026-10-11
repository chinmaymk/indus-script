"""Reproduce bounded local locators and source-page crops; no identity repair."""
from pathlib import Path
import re,json,hashlib
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'coverage':('h1123-cisi2-6.png',(.055,.755,.895,.845)),
 'end-data':('h1123-cisi2-480.png',(.072,.294,.477,.398)),
 'corrigenda':('h1123-cisi2-482.png',(.604,.791,.976,.891)),
}
def main():
 source=ROOT/'data/raw/h843_identity_CorpusVol2_djvu.txt'
 text=source.read_text(); rows=[]
 for name,regex in [('H1123',r'H[\s\-‐–]*1123\b'),('field9015',r'\b9[\s,.]*015\b'),('raw9015360',r'\b9015360\b')]:
  hits=[{'offset':m.start(),'context':text[max(0,m.start()-70):m.end()+70]} for m in re.finditer(regex,text)]
  rows.append({'query_name':name,'regex':regex,'hits':hits})
 for name,(p,box) in CROPS.items():
  im=Image.open(ROOT/'results/primary_pages'/p); w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'h1123-cisi2-{name}.png')
 out={'source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'queries':rows,'limitation':'OCR absence is not evidence of absence; printed coverage was separately inspected','semantic_values':None}
 (ROOT/'data/processed/h1123_cisi2_locators.json').write_text(json.dumps(out,indent=2)+'\n')
 print([(x['query_name'],len(x['hits'])) for x in rows])
if __name__=='__main__':main()
