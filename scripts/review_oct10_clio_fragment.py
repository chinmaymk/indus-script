"""Extract native Clio2017 Figure4 images and pin the cautious visual review."""
import hashlib
import json
from pathlib import Path
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def pin(p):
    b = (ROOT / p).read_bytes()
    return {'path': p, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def main():
    src = 'data/raw/oct10-chanhu-clio2017-public.pdf'
    r = PdfReader(ROOT / src)
    base = ROOT / 'results/primary_pages'
    embedded = []
    for i in (3, 4):
        obj = r.pages[5].images[i]
        dest = base / ('oct10-clio-review-native-' + obj.name)
        dest.write_bytes(obj.data)
        embedded.append({**pin(str(dest.relative_to(ROOT))), 'pdf_page': 6,
                         'image_index_zero_based': i, 'image_name': obj.name,
                         'pixels': list(obj.image.size), 'mode': obj.image.mode,
                         'transforms': 'none; extracted embedded bytes'})
    im = Image.open(base / 'oct10-clio-review-native-Im18.jpg')
    assert im.size == (655, 926) and im.mode == 'CMYK'
    box = (432, 155, 523, 200)
    c = im.convert('RGB').crop(box)
    native = base / 'oct10-clio-review-seal-native.png'
    enlarged = base / 'oct10-clio-review-seal-nearest8x.png'
    c.save(native)
    c.resize((728, 360), Image.Resampling.NEAREST).save(enlarged)
    assert Image.open(native).tobytes() == c.tobytes()
    prior = json.loads((ROOT / 'data/processed/chanhu_local_primary_positive_review.json').read_text())
    result = {
        'research_date': '2026-10-10', 'source': pin(src),
        'pdf_pages': len(r.pages), 'figure': 4, 'figure_pdf_and_printed_page': 6,
        'fixed_family': prior['fixed_family'], 'family_changed': False,
        'observations': {
            'displayed_object': 'light rectangular fragment in upper portion of right-hand 2017 assemblage panel',
            'visible_marks': 'curved roughly parallel grooves at left; two near-vertical/oblique grooves middle-right; broken uneven upper margin',
            'complete_diagnostic_fish_identified': False,
            'visible_fixed_family_status': 'U', 'original_whole_text_fixed_family_status': 'U',
            'reason': 'tiny fragment and insufficient diagnostic graphic structure; cannot authenticate intact sign band or exclude missing fish',
            'script_versus_iconography': 'unresolved; residual pictorial lines remain possible',
            'artifact_identifier': None, 'precise_locus': None, 'deposit_event': None,
            'same_as_either_reported_fragment': 'caption/context-compatible only; no individual inventory join',
            'two_fragments_two_objects': None,
        },
        'context': {
            'reported_production_complex': True,
            'reports_two_steatite_seal_fragments': True,
            'discovery_sample_independence': 'modern campaign is distinct from old selected seals, but this source provides no authenticated analyzable fish occurrence',
            'matched_nonproduction_sample': False,
            'new_eligible_fish_production_observations': 0,
            'reason_not_added': 'unknown fish status, no object-specific event/stratum, and no comparable reporting frame',
            'source_date_wording_discrepancy': 'Figure4 caption gives first Indus period2600/2500-1900; page7 heading gives2600/2500-2300. Neither is an individual fragment date.',
        },
        'embedded_images': embedded,
        'crop': {**pin(str(native.relative_to(ROOT))), 'source_image': embedded[1]['path'],
                 'box': list(box), 'pixels': list(c.size), 'transforms': 'CMYK-to-RGB conversion then native-resolution crop; no geometry or contrast change'},
        'display_enlargement': {**pin(str(enlarged.relative_to(ROOT))), 'scale': 8,
                               'resampling': 'nearest neighbor; no new detail or reconstruction'},
        'adjacent_page_text': {str(n): r.pages[n-1].extract_text() for n in (5, 6, 7)},
        'input_pins': [pin(p) for p in ['docs/CHANHU_LOCAL_GRAPHICS_AND_SPECIFICITY.md',
                    'data/processed/chanhu_local_primary_positive_review.json']],
        'attempt_log': ['Read adjacent pages5-7 and extracted native embedded images Im17/Im18.',
                        'Initial PNG crop failed because embedded JPEG is CMYK; no PNG was produced.',
                        'Explicit RGB conversion allowed PNG preservation; inspected native panel and nearest-neighbor crop.',
                        'No mirrored, enhanced or reconstructed marks; no values assigned.'],
    }
    (ROOT / 'data/processed/oct10_clio_fragment_review.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'fish_status': 'U', 'native_panel': list(im.size), 'crop': list(c.size), 'eligible_observations': 0}))

if __name__ == '__main__':
    main()
