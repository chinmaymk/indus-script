"""Persist the manual, fixed-page documentary screen and missing-data bounds.

The code does not read inscriptions or infer negative archaeological observations.
Page/row observations below were read from the retained primary images.
"""
from fractions import Fraction
from common import ROOT,sha256,write_json

# page, first/last printed serial, explicit cereal-related mention serials
PAGES=[
 (255,1,23,[3,7,8,9,12,13,14]),
 (257,24,39,[24,26,27,28,29,30,35,36,38,39]),
 (259,40,56,[44,50,52,53]),
 (261,57,78,[60,65,70,77]),
 (263,79,99,[82,84,85,86,88,89,95,99]),
 (265,100,115,[101,102,103,105,106,109,111,113]),
 (267,116,135,[116,117,118,120,126,132,135]),
 (269,136,155,[136,140,141,145,150,151]),
 (271,156,176,[158,162,164,171,172,176]),
]

MARKS={
 18:dict(container_inscription_reported=True,source='table255 remarks',description='Three pictograms on the jar shoulder.',field_number='3822'),
 35:dict(container_inscription_reported=True,source='table256 description; narrative253 and165',description='Jar explicitly described as inscribed in left-hand table and narrative; no exact transcription recovered.',field_number='5919'),
 44:dict(container_inscription_reported=False,source='table259 remarks',description='Two contained goblet sherds: one incised, another bearing a seal impression.',contained_marked_objects=2),
 54:dict(container_inscription_reported=False,source='table259 miscellaneous',description='A small rectangular steatite seal with inscriptions on both sides was among contents.',contained_marked_objects=1),
 116:dict(container_inscription_reported=True,source='table267 remarks and miscellaneous',description='Jar has seven pictograms in two lines; a separate discoid faience sealing is among contents.',field_number='10252',contained_marked_objects=1),
 156:dict(container_inscription_reported=False,source='table271 miscellaneous',description='Fragment of a unicorn seal among contents; preserved writing not explicitly specified.',contained_seal_fragment=1),
 165:dict(container_inscription_reported=False,source='table271 remarks',description='One contained goblet bears four incised upright strokes; these are not stated to mark the containing jar.',contained_marked_objects=1),
}

def path_for(page):
    leaf=page+26
    prefix='capacity-context' if page==255 else 'inscribed-contents' if page==257 else 'inscribed-frame'
    return f'data/raw/{prefix}-vats-leaf{leaf}.jpg'

def main():
    rows=[];pages=[]
    for page,first,last,grain in PAGES:
        source=path_for(page)
        pages.append(dict(printed_page=page,first_serial=first,last_serial=last,
                          source=source,sha256=sha256(ROOT/source),review='manual visual full right-hand continuation page'))
        for serial in range(first,last+1):
            cereal='reported' if serial in grain else 'not_reported_in_screened_cells'
            if serial==30:cereal='reported_as_apparent_grain_fill'
            if serial==135:cereal='reported_as_cereal_like_sesame_impressions'
            mark=MARKS.get(serial)
            known=bool(mark and mark.get('container_inscription_reported'))
            rows.append(dict(serial=serial,printed_page=page,source=source,
                cereal_related_report=cereal,cereal_related_mention=serial in grain,
                jar_inscription_status='explicitly_reported' if known else 'not_established',
                observed_uninscribed=False,plant_impressions_without_cereal_report=serial==147,
                marking_note=mark))
    assert [r['serial'] for r in rows]==list(range(1,177))
    # Exact enumeration of all completions of UNREPORTED jar-inscription status.
    # Outcome here is ONLY a documentary cereal mention, not actual ancient contents.
    known=[r for r in rows if r['jar_inscription_status']=='explicitly_reported']
    unknown=[r for r in rows if r['jar_inscription_status']=='not_established']
    a=sum(r['cereal_related_mention'] for r in known);b=len(known)-a
    c=sum(r['cereal_related_mention'] for r in unknown);d=len(unknown)-c
    extremal=[]
    for x in range(c+1):
        for y in range(d+1):
            if c+d-x-y==0:continue
            diff=Fraction(a+x,a+b+x+y)-Fraction(c-x,c+d-x-y)
            extremal.append((diff,x,y))
    lo=min(extremal);hi=max(extremal)
    def completion(v):
        diff,x,y=v
        return dict(difference_exact=str(diff),difference=float(diff),
            unknown_cereal_mention_rows_assigned_inscribed=x,
            unknown_nonmention_rows_assigned_inscribed=y,
            inscribed_group_cereal_mentions=a+x,inscribed_group_rows=a+b+x+y,
            other_group_cereal_mentions=c-x,other_group_rows=c+d-x-y)
    output=dict(scope='Reported marks and plant/cereal observations in a fixed primary table; no semantic assignment',
        design_sha256=sha256(ROOT/'docs/INSCRIBED_JAR_FRAME_DESIGN.md'),pages=pages,rows=rows,
        expected_narrative_jar_count=178,observed_printed_serial_count=176,
        unlocated_expected_serials=[177,178],final_page_says_concluded=True,
        count_discrepancy='Narrative252 reports178; complete printed table serials end176. No synthetic rows or negative observations created.',
        other_table_54_jar_group_excluded=True,
        summary=dict(cereal_related_mention_rows=a+c,qualified_cereal_rows=[30,135],
            direct_report_excluding_two_qualified_rows=a+c-2,
            plant_impressions_without_cereal_report_rows=[147],
            container_inscription_reported_rows=[r['serial'] for r in known],
            container_inscription_unestablished_rows=len(unknown),observed_uninscribed_rows=0,
            rows_with_contained_marked_object_reports=[44,54,116,165],
            rows_with_seal_fragment_but_no_explicit_preserved_text=[156]),
        documentary_association_nonidentifiability=dict(outcome='Whether this right-hand table page explicitly mentions cereal-related material',
            exposure='Actual jar inscription status, known positive for three jars and unestablished for173',
            known_inscribed_mention=a,known_inscribed_nonmention=b,unknown_mention=c,unknown_nonmention=d,
            grouped_completions_enumerated=len(extremal),minimum=completion(lo),maximum=completion(hi),
            inferential_limit='Both signs of association are possible even for the reporting outcome; no p-value or ancient commodity association is justified. Missing grain reports also are not actual absences.'),
        near_misses=[dict(serial=26,reason='Incised ivory decoration is not an authenticated inscription.'),
                     dict(serial=30,reason='A grooved discoid tablet is mentioned without a script identification.'),
                     dict(serial=87,reason='Quadrant depressions on a stone die are not reported pictograms.'),
                     dict(serial=137,reason='An oval shell tablet is mentioned without writing.'),
                     dict(serial=152,reason='A steatite tumbler is not identified as a seal.')],
        semantic_values_assigned=0,phonetic_values_assigned=0,
        input_sha256={p:sha256(ROOT/p) for p in ['scripts/build_inscribed_jar_frame.py','docs/INSCRIBED_JAR_FRAME_DESIGN.md','data/raw/capacity-context-vats-leaf279.jpg','data/raw/capacity-context-vats-leaf278.jpg','data/processed/inscribed_jar_contents_review.json']})
    write_json('results/inscribed_jar_frame.json',output)
    print(f'Inscribed-jar frame: {len(rows)} serials; {a+c} broad cereal mentions; {len(known)} reported jar inscriptions; association bounds {lo[0]} to {hi[0]}.')

if __name__=='__main__':main()
