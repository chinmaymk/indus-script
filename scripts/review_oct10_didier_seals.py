"""Preserve native Fig10b seal views and bounded fish-family assessments."""
import hashlib
import json
from pathlib import Path
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
BOXES = {'left': (188,1202,403,1302), 'middle': (553,1191,684,1318), 'right': (879,1214,973,1320)}

def pin(p):
    b = (ROOT/p).read_bytes()
    return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    src='data/raw/oct10-chanhu-didier2017-hal.pdf'
    pdf=PdfReader(ROOT/src)
    obj=pdf.pages[22].images[0]
    native='results/primary_pages/oct10-didier-review-native-Im0.jpg'
    (ROOT/native).write_bytes(obj.data)
    im=Image.open(ROOT/native)
    assert im.size==(1235,1446)
    crops=[]
    for name,box in BOXES.items():
        crop=im.convert('RGB').crop(box)
        dest=f'results/primary_pages/oct10-didier-review-{name}-native.png'
        large=f'results/primary_pages/oct10-didier-review-{name}-5x.png'
        crop.save(ROOT/dest)
        crop.resize((crop.width*5,crop.height*5),Image.Resampling.NEAREST).save(ROOT/large)
        assert Image.open(ROOT/dest).tobytes()==crop.tobytes()
        crops.append({'name':name,'box':list(box),'native':pin(dest),'display_5x':pin(large),
            'transforms':'Pillow RGB conversion; native crop; separate nearest-neighbor5x display only'})
    descriptions={
        'left':'Lower animal-body fragment: two paired legs with hoof-like ends, curved belly, tail-like line at left, broken upper margin. Not an authenticated surviving sign band.',
        'middle':'Near-square face with bovine head/body and upper elongated and diagonal incisions. Distinction between horns, script and surface texture unresolved in portions. No secure complete fish diagnostic.',
        'right':'Trapezoidal broken fragment with crowded curved/angular incisions and large right-side loss. No independently identifiable complete fish diagnostic.',
    }
    family=json.loads((ROOT/'data/processed/chanhu_local_primary_positive_review.json').read_text())['fixed_family']
    out={'research_date':'2026-10-10','source':pin(src),'figure':'10b','pdf_page':23,'printed_page':989,
         'native_embedded':{**pin(native),'pixels':list(im.size),'mode':im.mode,'transforms':'none; embedded JPEG bytes'},
         'fixed_family':family,'family_changed':False,'crops':crops,
         'views':[{'view_label':k,'description':v,'visible_fixed_family_status':'U',
                   'original_whole_text_status':'U','artifact_identifier':None,'exact_sign_codes':[],
                   'reason':'No securely diagnostic fish; incompleteness and/or insufficient visual resolution preclude whole-text absence.'}
                  for k,v in descriptions.items()],
         'displayed_seal_views':3,'reported_seal_count':4,'count_discrepancy_resolved':False,
         'clio_comparison':{'candidate_view':'left','same_object_visual_support':'strong candidate',
              'features':'uneven upper break, relative placement of paired legs and curved belly, tail-like line at left',
              'authenticated_field_number':None,'independent_new_object_count_from_clio_join':None,
              'consequence':'Do not count left view plus Clio fragment as two independent seals; do not assign identity number.'},
         'context_limits':['Fig10 caption gives chantier2 and2016–2018, not individual field numbers or deposits.',
                           'Article body places objects among house assemblages; exact matched production-stratum join not supplied by these pages.',
                           'Three visible views cannot be assumed complete photographic coverage of four reported seals.'],
         'new_eligible_fish_observations':0,'new_semantic_values':[],
         'context_text':{str(n):pdf.pages[n-1].extract_text() for n in (20,23)},
         'comparison_pins':[pin(p) for p in ['data/processed/oct10_clio_fragment_review.json',
                   'results/primary_pages/oct10-clio-review-native-Im18.jpg',
                   'data/processed/chanhu_local_primary_positive_review.json']],
         'log':['Read PDF20 and23; extracted sole native image fromPDF23.',
                'Inspected native full panel plus three native crops enlarged5x with nearest-neighbor.',
                'Compared left fragment with retained Clio image; recorded distinctive morphology as candidate join only.',
                'Assigned no exact codes, reading direction, numeric or lexical values.']}
    (ROOT/'data/processed/oct10_didier_seal_review.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'views':3,'reported_seals':4,'fish_statuses':['U']*3,'new_eligible_observations':0}))

if __name__=='__main__':main()
