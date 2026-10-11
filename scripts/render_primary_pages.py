"""Reproduce source-page images for visual review; requires Poppler pdftoppm.

Example: python scripts/render_primary_pages.py --pages 50 51 --prefix texts
Default renders Table I (728--734), at the resolution used for its visual review.
"""
import argparse
import shutil
import subprocess
from common import ROOT

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdftoppm',default=shutil.which('pdftoppm'))
    p.add_argument('--pages',nargs='+',type=int,default=list(range(728,735)))
    p.add_argument('--prefix',default='table_i_highres')
    p.add_argument('--scale',type=int,default=2400)
    args=p.parse_args()
    if not args.pdftoppm:
        p.error('Poppler pdftoppm is required; provide --pdftoppm /path/to/pdftoppm')
    if any(not 1<=page<=842 for page in args.pages):
        p.error('Page numbers must be between 1 and 842')
    if '/' in args.prefix or '\\' in args.prefix:
        p.error('Prefix must be a filename, not a path')
    dest=ROOT/'results/primary_pages'
    dest.mkdir(parents=True,exist_ok=True)
    for page in args.pages:
        subprocess.run([args.pdftoppm,'-f',str(page),'-l',str(page),
            '-scale-to',str(args.scale),'-png',str(ROOT/'data/raw/mahadevan_1977_text.pdf'),
            str(dest/args.prefix)],check=True)

if __name__=='__main__':
    main()
