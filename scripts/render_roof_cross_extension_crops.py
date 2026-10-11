"""Retain complete M77 fields and both CISI photographs per object, unretouched."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
CROPS={
 '3319-fields':('roof-cross-extension-m77-104.png',(.14,.14,.82,.198)),
 '3320-fields':('roof-cross-extension-m77-104.png',(.14,.195,.82,.249)),
 'appendix':('roof-cross-extension-m77-829.png',(.541,.708,.891,.756)),
 'cisi-metadata':('roof-cross-extension-cisi-405.png',(.035,.885,.406,.912)),
 'M509A':('roof-cross-extension-photo-164.png',(.202,.051,.48,.25)),
 'M509B':('roof-cross-extension-photo-164.png',(.546,.052,.829,.265)),
 'M510A':('roof-cross-extension-photo-164.png',(.202,.284,.481,.493)),
 'M510B':('roof-cross-extension-photo-164.png',(.546,.284,.829,.495)),
 'sign287':('sign_list-045.png',(.64,.585,.712,.651)),
 'sign319':('sign_list-045.png',(.823,.826,.894,.893)),
}
def main():
 a=[]
 for name,(filename,box) in CROPS.items():
  src='results/primary_pages/'+filename;im=Image.open(R/src);w,h=im.size;out=f'results/primary_pages/roof-cross-extension-{name}-detail.png'
  im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(R/out)
  a.append({'name':name,'source':src,'fractional_box':box,'crop':out,'processing':'crop only; no mirroring, rotation, retouching or contrast adjustment'})
 (R/'data/processed/roof_cross_extension_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
if __name__=='__main__':main()
