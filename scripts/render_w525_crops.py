"""Retain unretouched, fractional-coordinate crops for W525 primary review."""
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'fem-cii-15': ('data/raw/w525_fem_leaf217.jpg', (.74,.713,.91,.941)),
    'fem-ciii-15': ('data/raw/w525_fem_leaf219.jpg', (.73,.555,.915,.81)),
    'mackay-dk8489': ('data/raw/w525_mackay_leaf385.jpg', (.118,.304,.825,.451)),
    'm77-2868': ('results/primary_pages/w525-m77-95.png', (.23,.058,.869,.111)),
    'm77-cii-rule': ('results/primary_pages/chain-artifact-m77-827.png', (.555,.286,.845,.478)),
    'm254-sign': ('results/primary_pages/ending-signlist-045.png', (.399,.336,.456,.403)),
    'vats-356': ('results/primary_pages/w525-vats-xciv-196.png', (.235,.724,.32,.818)),
    'vats-360': ('results/primary_pages/w525-vats-xciv-196.png', (.662,.722,.759,.816)),
    'vats-9015-metadata': ('data/raw/w525_vats_leaf59.jpg', (.18,.676,.82,.733)),
    'vats-ab473-metadata': ('data/raw/w525_vats_leaf49.jpg', (.127,.616,.8,.722)),
    'vats-672': ('results/primary_pages/w525-vats-c-208.png', (.438,.518,.527,.614)),
    'm77-4672': ('results/primary_pages/w525-m77-h-137.png', (.2,.311,.817,.371)),
    'm77-4360': ('results/primary_pages/w525-m77-h-120.png', (.146,.425,.81,.483)),
    'm77-eh-rule': ('results/primary_pages/w525-m77-h-830.png', (.05,.758,.467,.863)),
}
if __name__ == '__main__':
    for name,(source,box) in CROPS.items():
        im=Image.open(ROOT/source); w,h=im.size
        im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(ROOT/'results/primary_pages'/f'w525-{name}.png')
