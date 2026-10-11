"""Unretouched fractional primary-source crops for M81/C3133/MIC180/M77-1180."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
CROPS={
 'mic180':('data/raw/m934_marshall48270_leaf191.jpg',(.06,.705,.19,.818)),
 'mic180-table':('results/primary_pages/m934-marshall-54.png',(.028,.623,.458,.642)),
 'm77-1180':('results/primary_pages/double-grid-m77-55.png',(.18,.600,.825,.634)),
 'm77-mic-rule':('results/primary_pages/chain-artifact-m77-827.png',(.12,.062,.505,.169)),
 'm245-sign':('results/primary_pages/ending-signlist-045.png',(.495,.25,.565,.321)),
}
if __name__=='__main__':
 for name,(source,box) in CROPS.items():
  im=Image.open(ROOT/source); w,h=im.size
  im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'double-grid-{name}.png')
