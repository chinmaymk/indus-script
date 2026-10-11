"""Integrate a manually traced vessel interior; preserve scale and shape assumptions."""
import base64
import argparse
import json
import math
from common import ROOT, sha256, write_json


def profile_volume(points, cm_per_pixel, radial_shift=0, vertical_factor=1, cutoff_y=None):
    """Exact frustum integration of linearly interpolated (y,radius) pairs, litres.

    Image y grows downwards: cutoff_y removes space ABOVE the selected fill level.
    Horizontal bottom closure requires no zero-radius last point.
    """
    if len(points)<2 or cm_per_pixel<=0 or vertical_factor<=0:
        raise ValueError('At least two profile points and positive scales required')
    if any(not math.isfinite(z) for p in points for z in p):
        raise ValueError('Non-finite profile')
    total=0
    for (y0,r0),(y1,r1) in zip(points,points[1:]):
        if y1<=y0 or min(r0,r1)<0:
            raise ValueError('Heights must increase; radii must be nonnegative')
        if cutoff_y is not None:
            if y1<=cutoff_y: continue
            if y0<cutoff_y:
                r0=r0+(r1-r0)*(cutoff_y-y0)/(y1-y0)
                y0=cutoff_y
        r0=max(0,r0+radial_shift)
        r1=max(0,r1+radial_shift)
        total += math.pi*(y1-y0)*(r0*r0+r0*r1+r1*r1)/3
    return total*cm_per_pixel**3*vertical_factor/1000


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract-image',action='store_true',
                        help='Re-extract embedded figure from saved PDF; optional pypdf dependency')
    args=parser.parse_args()
    path=ROOT/'data/processed/h95_profile_trace.json'
    d=json.loads(path.read_text())
    if sha256(ROOT/d['source_pdf'])!=d['source_pdf_sha256']:
        raise ValueError('Source PDF checksum mismatch')
    if args.extract_image:
        from pypdf import PdfReader
        page=PdfReader(ROOT/d['source_pdf']).pages[d['pdf_page']-1]
        if len(page.images)!=1:
            raise ValueError('Expected one embedded Figure7 image')
        (ROOT/d['image']).write_bytes(page.images[0].data)
    for key in ['source_pdf','image']:
        if sha256(ROOT/d[key])!=d[key+'_sha256']:
            raise ValueError(f'{key} checksum mismatch')
    (ax0,ay0),(ax1,ay1)=d['axis_endpoints_px']
    def axis(y): return ax0+(ax1-ax0)*(y-ay0)/(ay1-ay0)
    points=[(y,axis(y)-x) for x,y in d['inner_left_profile_xy_px']]
    (sx0,sy0),(sx1,sy1)=d['scale_endpoints_px']
    bar=math.hypot(sx1-sx0,sy1-sy0)
    scale=d['scale_cm']/bar
    central=profile_volume(points,scale)
    a=d['sensitivity_assumptions']
    lo=profile_volume(points,d['scale_cm']/(bar+a['scale_length_error_px']),
                      -a['radial_error_px'],1-a['height_scale_relative_error'])
    hi=profile_volume(points,d['scale_cm']/(bar-a['scale_length_error_px']),
                      a['radial_error_px'],1+a['height_scale_relative_error'])
    results={'source_trace_sha256':sha256(path),'status':d['status'],
             'litres_to_traced_rim':central,'cm_per_pixel':scale,
             'traced_internal_height_cm':(points[-1][0]-points[0][0])*scale,
             'maximum_internal_diameter_cm':2*max(r for y,r in points)*scale,
             'analyst_perturbation_envelope_litres':[lo,hi],
             'perturbation_envelope_is_not_a_confidence_interval':True,
             'four_rim_strokes_provisional_litres_per_stroke':central/4,
             'three_rim_strokes_alternative_litres_per_stroke':central/3,
             'fill_level_sensitivity':[{'cm_below_traced_rim':h,
                'litres':profile_volume(points,scale,cutoff_y=points[0][0]+h/scale)}
                for h in [0,2,5,10]],'caveats':d['caveats'],
             'conditional_four_stroke_40_353_prediction_litres':4*40.3531914893617}
    write_json('results/h95_profile_volume.json',results)
    encoded=base64.b64encode((ROOT/d['image']).read_bytes()).decode()
    poly=' '.join(f'{x},{y}' for x,y in d['inner_left_profile_xy_px'])
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="696" height="873" viewBox="0 0 696 873">
<rect width="696" height="873" fill="white"/>
<image href="data:image/jpeg;base64,{encoded}" width="696" height="803"/>
<polyline points="{poly}" stroke="#e11d48" fill="none" stroke-width="1.5"/>
<line x1="{ax0}" y1="{ay0}" x2="{ax1}" y2="{ay1}" stroke="#2563eb" stroke-width="1.5"/>
<line x1="{sx0}" y1="{sy0}" x2="{sx1}" y2="{sy1}" stroke="#16a34a" stroke-width="2"/>
<g font-family="sans-serif" font-size="13"><text x="12" y="824">Red: traced inner wall. Blue: axis. Green: published 20 cm scale.</text>
<text x="12" y="845">Kenoyer, Figure 7.2, journal PDF page 21 / printed 156; analytical overlay.</text>
<text x="12" y="865">Drawing-based estimate assumes rotation symmetry; not a direct volume measurement.</text></g></svg>'''
    (ROOT/'results/h95_profile_overlay.svg').write_text(svg)
    from PIL import Image, ImageDraw
    overlay=Image.open(ROOT/d['image']).convert('RGB')
    draw=ImageDraw.Draw(overlay)
    draw.line([tuple(p) for p in d['inner_left_profile_xy_px']],fill='#e11d48',width=2)
    draw.line([(ax0,ay0),(ax1,ay1)],fill='#2563eb',width=2)
    draw.line([(sx0,sy0),(sx1,sy1)],fill='#16a34a',width=2)
    overlay.save(ROOT/'results/h95_profile_overlay.png')
    print(f'H95 traced capacity: {central:.2f} L; analyst perturbations {lo:.2f}–{hi:.2f} L')


if __name__=='__main__': main()
