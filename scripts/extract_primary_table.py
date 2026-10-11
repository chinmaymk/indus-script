"""Transcribe Mahadevan 1977 Table I from archived OCR coordinates.

Columns and row order are inspected against PDF pp. 728--734 (printed 717--723).
OCR is never accepted merely because its row sum fits. Every normalization and manual
correction is exposed in the ledger; aggregate constraints are additional checks.
"""
from collections import Counter
import json
import xml.etree.ElementTree as ET
from common import ROOT, sha256, write_csv, write_json

FIELDS=['solus','initial','medial','final','total']
PRINTED_TOTALS=[190,3010,7196,2976,13372]
FREQUENCY_BANDS=[(1000,100000,1,1395),(500,999,1,649),(100,499,31,6344),
                 (50,99,34,2381),(10,49,86,1833),(2,9,152,658),(1,1,112,112)]

def validate_rows(rows):
    """Check actual table values, without relying on a possibly stale audit file."""
    if len(rows)!=417 or {r['sign'] for r in rows}!={f'M{i:03d}' for i in range(1,418)}:
        raise ValueError('Expected exactly one row for every M001--M417 sign')
    values=[]
    for row in rows:
        try:
            counts=[int(row[f]) for f in FIELDS]
        except (ValueError,TypeError):
            raise ValueError(f"Unresolved cell in {row['sign']}") from None
        if min(counts)<0 or counts[-1]<1 or sum(counts[:-1])!=counts[-1]:
            raise ValueError(f"Invalid counts in {row['sign']}")
        values.append(counts)
    if [sum(v[i] for v in values) for i in range(5)]!=PRINTED_TOTALS:
        raise ValueError('Table disagrees with printed column totals')
    for lo,hi,n,tokens in FREQUENCY_BANDS:
        band=[v[-1] for v in values if lo<=v[-1]<=hi]
        if len(band)!=n or sum(band)!=tokens:
            raise ValueError('Table disagrees with printed frequency bands')
    if [sum(v[i]>0 for v in values) for i in range(4)]!=[88,290,286,173]:
        raise ValueError('Table disagrees with printed position type counts')
# Approximate header x centers in original OCR-image coordinates, by page/half.
LAYOUT={
 728:([[1333,1561,1783,2026,2260],[2928,3159,3381,3618,3848]],610,6100,[32,32]),
 729:([[1551,1782,2004,2238,2471],[3133,3350,3581,3828,4067]],470,6120,[32,32]),
 730:([[1235,1466,1670,1904,2126],[2753,2966,3200,3404,3617]],540,5940,[32,32]),
 731:([[1356,1584,1803,2043,2274],[2936,3156,3381,3621,3858]],470,6000,[32,32]),
 732:([[1136,1361,1583,1814,2072],[2714,2951,3170,3407,3641]],470,6000,[32,32]),
 733:([[1439,1679,1913,2143,2375],[3023,3257,3491,3720,3962]],530,6100,[32,32]),
 734:([[1213,1437,1659,1906,2142],[2799,3036,3273,3499,3732]],620,3590,[17,16])}

def parse_cell(raw):
    if raw.isascii() and raw.isdigit():
        return int(raw), 'literal_numeric_OCR'
    if raw in ['O','o']:
        return 0, 'normalized_OCR_requires_review'
    if raw in ['I','i','l','t','!','|']:
        return 1, 'normalized_OCR_requires_review'
    return None,'unresolved_OCR'

def main():
    pages=ET.parse(ROOT/'data/raw/mahadevan_1977_ocr.xml').findall('.//OBJECT')
    corrpath=ROOT/'data/processed/primary_table_corrections.json'
    corrections=json.loads(corrpath.read_text()) if corrpath.exists() else {}
    reviewpath=ROOT/'data/processed/primary_table_visual_review.json'
    review=json.loads(reviewpath.read_text()) if reviewpath.exists() else {}
    if review and sha256(ROOT/review['source_pdf'])!=review['source_pdf_sha256']:
        raise ValueError('Visual-review source has changed; review no longer applies')
    reviewed={p['pdf_page'] for p in review.get('pages',[]) if p['status']=='visually_reviewed'}
    cells=[];rows=[];sign_number=0
    for pg,(halves,ylo,yhi,counts) in LAYOUT.items():
        words=[]
        for w in pages[pg-1].findall('.//WORD'):
            a,b,c,d,*_=map(int,w.attrib['coords'].split(','))
            words.append({'x':(a+c)/2,'y':(b+d)/2,'text':w.text or '', 'box':[a,d,c,b]})
        for half,(centers,expected) in enumerate(zip(halves,counts)):
            pool=sorted((w for w in words if centers[0]-120<w['x']<centers[-1]+130 and ylo<w['y']<yhi),key=lambda w:w['y'])
            clusters=[]
            for w in pool:
                if not clusters or w['y']-sum(v['y'] for v in clusters[-1])/len(clusters[-1])>70:
                    clusters.append([w])
                else:clusters[-1].append(w)
            # Last page's right half has a totals row after its 16 sign rows.
            if pg==734 and half==1:clusters=clusters[:16]
            if len(clusters)!=expected:
                raise ValueError(f'Page {pg}, half {half}: {len(clusters)} rows, expected {expected}')
            for j,cluster in enumerate(clusters):
                sign_number+=1; sign=f'M{sign_number:03d}'
                row={'sign':sign,'pdf_page':pg,'printed_page':pg-11,'table_half':half+1,'row_in_half':j+1,
                     'source':'Mahadevan 1977 Table I',
                     'row_y_ocr':round(sum(w['y'] for w in cluster)/len(cluster),1)}
                values=[]
                for k,field in enumerate(FIELDS):
                    selected=sorted([w for w in cluster if min(range(5),key=lambda c:abs(w['x']-centers[c]))==k],key=lambda w:w['x'])
                    raw=' '.join(w['text'] for w in selected)
                    val,status=parse_cell(raw)
                    if status=='normalized_OCR_requires_review' and pg in reviewed:
                        status='normalized_OCR_page_reviewed'
                    correction=corrections.get(sign,{}).get(field)
                    note=''
                    if correction is not None:
                        val=correction['value'];status='visually_checked_correction';note=correction['reason']
                    row[field]=val;values.append(val)
                    cells.append({'sign':sign,'field':field,'raw_ocr':raw,'value':val,'status':status,
                        'pdf_page':pg,'printed_page':pg-11,'half':half+1,'row':j+1,
                        'ocr_boxes':json.dumps([w['box'] for w in selected]),'note':note})
                row['row_sum_matches']=all(v is not None for v in values) and sum(values[:4])==values[4]
                rows.append(row)
    write_csv('results/primary_table_cells.csv',cells)
    write_csv('data/processed/mahadevan_1977_table_i.csv',rows)
    unresolved=[r['sign'] for r in rows if not r['row_sum_matches']]
    totals={field:sum(r[field] or 0 for r in rows) for field in FIELDS}
    freq=Counter(r['total'] for r in rows if r['total'] is not None)
    bandchecks=[]
    for lo,hi,count,occurrences in FREQUENCY_BANDS:
        actual=[r['total'] for r in rows if r['total'] is not None and lo<=r['total']<=hi]
        bandchecks.append({'minimum':lo,'maximum':hi,'signs':len(actual),'occurrences':sum(actual),
            'printed_signs':count,'printed_occurrences':occurrences,'matches':len(actual)==count and sum(actual)==occurrences})
    audit={'rows':len(rows),'unresolved_or_sum_disagreement_signs':unresolved,
      'cell_status_counts':dict(Counter(c['status'] for c in cells)), 'column_sums':totals,
      'printed_column_sums':dict(zip(FIELDS,[190,3010,7196,2976,13372])),
      'column_sums_match':list(totals.values())==[190,3010,7196,2976,13372],
      'hapax_signs':freq[1],'printed_hapax_signs':112,
      'frequency_band_checks':bandchecks,'all_bands_match':all(b['matches'] for b in bandchecks),
      'visually_reviewed_pdf_pages':sorted(reviewed),
      'warning':'Exact aggregate agreement is necessary but not sufficient to establish every cell. Consult cell provenance and visual review notes.'}
    write_json('results/primary_table_audit.json',audit)
    print(json.dumps(audit,indent=2))

if __name__=='__main__':
    main()
