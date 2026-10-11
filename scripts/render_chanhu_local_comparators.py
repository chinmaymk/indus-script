"""Reproduce unretouched source-page renders and native-pixel comparator crops."""
from pathlib import Path
import subprocess,json
from PIL import Image
R=Path(__file__).resolve().parents[1]
exe='/Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
for page,scale,prefix in [(367,4000,'hi'),(368,4000,'hi'),(410,2400,'cisi'),(411,3000,'cisi')]:
 name=f'chanhu-local-{prefix}-{page}' if prefix=='hi' else f'chanhu-local-{prefix}{page}'
 dest=R/'results/primary_pages'/name
 if not dest.with_suffix('.png').exists():subprocess.run([exe,'-f',str(page),'-l',str(page),'-scale-to',str(scale),'-png','-singlefile',str(R/'data/raw/cisi_76884.pdf'),str(dest)],check=True)
jobs=[('data/raw/chanhu_context_leaf416.jpg','LI14',(.49,.295,.60,.384)),('data/raw/chanhu_context_leaf416.jpg','LI15',(.605,.277,.734,.389)),('data/raw/chanhu_context_leaf416.jpg','LI22',(.35,.461,.464,.549)),('data/raw/chanhu_context_leaf312.jpg','catalogue14-15',(.2,.449,.89,.49)),('data/raw/chanhu_context_leaf312.jpg','catalogue22',(.2,.563,.89,.582)),('results/primary_pages/chanhu-local-hi-367.png','C17',(.47,.76,.94,.95)),('results/primary_pages/chanhu-local-hi-368.png','C22',(.03,.65,.95,.89)),('results/primary_pages/chanhu-local-cisi410.png','C17-metadata',(.55,.932,.94,.956)),('results/primary_pages/chanhu-local-cisi411.png','C22-metadata',(.05,.088,.46,.108)),('results/primary_pages/sign_list_page_32.png','M008',(.64,.082,.74,.151)),('results/primary_pages/sign_list_page_32.png','M028',(.64,.245,.74,.317))]
manifest=[]
for source,name,b in jobs:
 im=Image.open(R/source);w,h=im.size;box=tuple(round(x*(w if i%2==0 else h)) for i,x in enumerate(b));out=f'results/primary_pages/chanhu-local-{name}.png';im.crop(box).save(R/out);manifest.append(dict(source=source,source_dimensions=[w,h],box_pixels=box,output=out,processing='crop only; no rotation, mirroring, contrast or restoration'))
(R/'data/processed/chanhu_local_comparators_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
