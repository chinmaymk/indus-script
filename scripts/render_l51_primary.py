"""Recreate Rao L-51 evidence pages from retained original PDF. No inference."""
import argparse, subprocess, sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pdftoppm', required=True); ap.add_argument('--tesseract', required=True); a=ap.parse_args()
    for prefix,pages,scale in [('l51-rao',[60,61,67,68],2700),('l51-nav',[440,450,460,470],1200),('l51-plate',[488,489,490],3000)]:
        subprocess.run([sys.executable,str(ROOT/'scripts/inspect_research_pdf.py'),'l51_rao1985_volume2.pdf','--prefix',prefix,'--render-only','--pages',*map(str,pages),'--pdftoppm',a.pdftoppm,'--tesseract',a.tesseract,'--scale',str(scale)],check=True)
    im=Image.open(ROOT/'results/primary_pages/l51-plate-489.png')
    im.rotate(-90,expand=True).save(ROOT/'results/primary_pages/l51-plate-clix-upright.png')
if __name__=='__main__': main()
