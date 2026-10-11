"""Native-pixel identity and graffito crops; no restorations or fitted measurements."""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
C={
 'key-column12':('roof-m092-artifact-cisi-key-401.png',(.543,.841,.942,.95)),
 'key-column345':('capacity-h370-source-402.png',(.063,.139,.457,.258)),
 'key-abbreviations':('capacity-h370-source-402.png',(.06,.261,.46,.492)),

 'metadata':('capacity-cisi-408.png',(.055,.656,.355,.693)),
 'H370-full':('capacity-h370-source-269.png',(.05,.644,.452,.953)),
 'H370-detail':('capacity-h370-source-269.png',(.489,.642,.945,.916)),
 'H371-full':('capacity-h370-source-270.png',(.071,.059,.478,.362)),
 'H371-detail':('capacity-h370-source-270.png',(.516,.058,.954,.327)),
 'H372-full':('capacity-h370-source-270.png',(.063,.548,.353,.767)),
 'H372-detail':('capacity-h370-source-270.png',(.522,.542,.951,.781)),
}
a=[]
for label,(fn,box) in C.items():
 src='results/primary_pages/'+fn;out=f'results/primary_pages/capacity-h370-{label}.png'
 with Image.open(R/src) as im:
  px=tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box));im.crop(px).save(R/out)
 a.append({'source':src,'output':out,'fractional_box':box,'pixel_box':px,'operation':'crop only'})
(R/'data/processed/capacity_h370_crop_manifest.json').write_text(json.dumps(a,indent=2)+'\n')
