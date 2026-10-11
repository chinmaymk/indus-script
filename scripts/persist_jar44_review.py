"""Preserve primary descriptions and distinct identifier/containment relations."""
import csv,json
from PIL import Image
from common import ROOT,sha256,write_json

def pin(path):return dict(path=path,bytes=(ROOT/path).stat().st_size,sha256=sha256(ROOT/path))

def main():
    crops=[]
    for source,label,box in [
        ('data/raw/jar54-vats-leaf284-retry.jpg','table-left',(650,3330,5200,3790)),
        ('data/raw/capacity-context-vats-leaf117.jpg','narrative91',(650,650,4650,2000))]:
        output=f'results/primary_pages/jar44-{label}.png'
        with Image.open(ROOT/source) as im:im.crop(box).save(ROOT/output)
        crops.append(dict(source=pin(source),output=pin(output),box_xyxy=box,operation='crop only'))
    with (ROOT/'data/raw/lipi_inscriptions.csv').open() as f:
        candidates=[{k:r[k] for k in ('id','cisi','excavation-idno','site','type','text')} for r in csv.DictReader(f) if '7856' in r.get('excavation-idno','')]
    files=['data/raw/jar54-vats-leaf284-retry.jpg','data/raw/capacity-context-vats-leaf117.jpg',
           'data/raw/inscribed-frame-vats-leaf285.jpg','data/raw/vats_1940_text_18220_djvu.txt',
           'data/raw/lipi_inscriptions.csv','results/primary_pages/inscribed-frame-independent-p259-row44.png',
           'docs/JAR44_CONTAINED_GOBLETS_REVIEW.md','scripts/persist_jar44_review.py']
    result=dict(scope='Exact primary records and typed candidate relations; no jar or goblet transcription established',
        table=dict(serial=44,register='7856',mound='F',trench='I',square='M12/7 and8',depth='6ft',stratum='III',
            description='Large, round, cracked',measurement=None,locator='Vats1940 I printed258–259',
            goblet_count=None,other_pottery=['one small tumbler','two miniature lids'],
            contained_marked_items=[dict(item='goblet sherd',mark='incision',own_identifier=None),
                                   dict(item='another goblet sherd',mark='seal impression',own_identifier=None)],
            cereal_report='Decayed cereal in lower portion; greenish porous earth',
            container_inscription_established=False),
        narrative=dict(locator='Vats1940 I printed91',register='7856',square='M12/7',
            described_object='fragment of an inscribed goblet',comparison='similar to No73 in PlateCIV',
            own_photograph_identified=False,comparison_is_identity=False),
        co_reference=dict(shared_literal_register=True,overlapping_grid=True,object_descriptions_differ=True,
            possible_explanations=['register covers an assemblage or is reused for an associated item','loose narrative reference','catalogue or printing error'],
            explanation_selected=None,exact_contained_item_identified=False,
            rule='Do not collapse the containing jar, its contained sherds and the illustrated comparison into one artifact.'),
        secondary_candidate_search=dict(field='excavation-idno',literal_substring='7856',rows=candidates,
            accepted_rows=[],exclusion='DK7856 belongs to Mohenjo-daro implements, not Harappa jar/goblet7856.',
            limit='No matched row in this secondary field search; not proof of absence from every catalogue.'),
        source_text_search=dict(literal_7856_hit_in_retained_Vats_OCR=False,
            OCR_location='printed91 located through goblet/stamped terms; original image clearly reads7856 despite damaged OCRnumerals',
            negative_OCR_is_not_absence=True),
        reported_numerical_value=None,semantic_values_assigned=0,phonetic_values_assigned=0,
        crop_manifest=crops,evidence_files=[pin(p) for p in files])
    write_json('data/processed/jar44_contained_goblets_review.json',result)
    print(f'Jar44: {len(files)} evidence pins and {len(crops)} crops; no exact contained-text join.')

if __name__=='__main__':main()
