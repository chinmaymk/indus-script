"""Extract local research PDFs and optionally render selected pages for review.

Optional dependencies: pypdf and Poppler. Does not download anything or establish
OCR/transcription correctness. Not required by the offline statistical pipeline.
"""
import argparse
import subprocess
from pathlib import Path
from common import ROOT, sha256, write_json


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', help='Filename within data/raw/')
    p.add_argument('--prefix',required=True)
    p.add_argument('--pages',nargs='*',type=int,default=[])
    p.add_argument('--pdftoppm')
    p.add_argument('--tesseract',help='Optionally OCR rendered pages with this executable')
    p.add_argument('--scale',type=int,default=2200)
    p.add_argument('--render-only',action='store_true',
                   help='Skip whole-document text extraction when only page images are needed')
    args=p.parse_args()
    if any(Path(s).name != s for s in [args.source,args.prefix]):
        p.error('Source and prefix must be plain filenames')
    from pypdf import PdfReader
    source=ROOT/'data/raw'/args.source
    reader=PdfReader(source)
    if any(not 1<=n<=len(reader.pages) for n in args.pages):
        p.error('Requested page outside PDF')
    if args.pages and not args.pdftoppm:
        p.error('Rendering requires --pdftoppm')
    dest=ROOT/'results'
    dest.mkdir(exist_ok=True)
    if not args.render_only:
        (dest/f'{args.prefix}_extracted.txt').write_text(''.join(
            f'\n--- PDF PAGE {i} ---\n'+(page.extract_text() or '')
            for i,page in enumerate(reader.pages,1)))
    for page in args.pages:
        out=dest/'primary_pages'/f'{args.prefix}-{page}'
        out.parent.mkdir(exist_ok=True)
        subprocess.run([args.pdftoppm,'-f',str(page),'-l',str(page),'-singlefile',
            '-scale-to',str(args.scale),'-png',str(source),str(out)],check=True)
        if args.tesseract:
            subprocess.run([args.tesseract,str(out)+'.png',str(out),'-l','eng'],check=True,
                           stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    write_json(f'results/{args.prefix}_extraction.json',{
        'source':str(source.relative_to(ROOT)), 'sha256':sha256(source),
        'page_count':len(reader.pages), 'rendered_pages':args.pages,
        'rendered_pages_are_not_automatically_visually_verified':True,
        'ocr_pages':args.pages if args.tesseract else [],
        'whole_document_text_extracted_this_invocation':not args.render_only,
        'extractor':'pypdf', 'scale':args.scale if args.pages else None})
    print(f'{"Rendered requested pages" if args.render_only else "Extracted " + str(len(reader.pages)) + " pages"} from {args.source}')


if __name__=='__main__':
    main()
