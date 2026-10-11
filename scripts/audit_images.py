"""Audit all 417 supplied images; compare CSV row pixels and create a sign atlas.

Nearest visual neighbors are retrieval suggestions, not allograph or reading claims.
The external catalogue's M/P/W crosswalk is attributed and provisional.
"""
from collections import defaultdict, Counter
import csv
import html
import json
import numpy as np
from PIL import Image, ImageDraw, ImageOps
from common import ROOT, sha256, write_json, write_csv

def normalized(arr):
    ys, xs = np.where(arr > 127)
    if not len(xs):
        return np.zeros(64 * 64, dtype=np.float32), [0,0,0,0]
    box = [int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)]
    img = Image.fromarray(arr).crop(box)
    img.thumbnail((56,56), Image.Resampling.LANCZOS)
    canvas = Image.new('L',(64,64),0)
    canvas.paste(img,((64-img.width)//2,(64-img.height)//2))
    vector = np.asarray(canvas,dtype=np.float32).reshape(-1)/255
    vector /= max(float(np.linalg.norm(vector)),1e-9)
    return vector, box

def main():
    features = json.loads((ROOT/'data/processed/catalogue_features.json').read_text())
    m_features, w_to_m, m_to_w = defaultdict(list), defaultdict(set), defaultdict(set)
    crosswalk = []
    for f in features:
        for m in f.get('mahadevan_graphemes',[]):
            m_features[m].append(f)
            for w in f.get('wells_graphemes',[]):
                m_to_w[m].add(w)
                w_to_m[w].add(m)
                crosswalk.append({'mahadevan':m,'parpola':f['id'],'wells':w,
                                  'source_path':f['source_path'], 'status':'source_asserted_not_independently_validated'})
    write_csv('data/processed/candidate_crosswalk.csv',crosswalk)
    profiles_path = ROOT/'results/sign_profiles_wells.csv'
    profiles = {r['sign']:r for r in csv.DictReader(profiles_path.open())} if profiles_path.exists() else {}
    primary_path=ROOT/'results/primary_sign_profiles_417.csv'
    primary={r['sign']:r for r in csv.DictReader(primary_path.open())} if primary_path.exists() else {}
    paths = sorted((ROOT/'IM_417_150_PNG').glob('*.png'),key=lambda p:int(p.stem))
    if [int(p.stem) for p in paths] != list(range(1,418)):
        raise ValueError('Image IDs must be exactly 1..417')
    arrays, vectors, boxes = [], [], []
    for p in paths:
        arr=np.asarray(Image.open(p).convert('L'))
        arrays.append(arr)
        v,b=normalized(arr);vectors.append(v);boxes.append(b)
    matrix=np.stack(vectors)
    sim=matrix@matrix.T
    np.fill_diagonal(sim,-1)
    rows=[]
    with (ROOT/'im_417_150.csv').open() as handle:
        for i,row in enumerate(csv.reader(handle)):
            vals=np.array(row,dtype=np.int16)
            if i>=len(arrays) or vals.size != arrays[i].size:
                raise ValueError('CSV/image dimensions differ')
            rows.append({'csv_row_1based':i+1,'image':paths[i].name,
                         'exact_pixel_match':bool(np.array_equal(vals,arrays[i].reshape(-1))),
                         'mean_absolute_pixel_difference':float(np.abs(vals-arrays[i].reshape(-1).astype(np.int16)).mean())})
    if len(rows)!=len(paths):
        raise ValueError('CSV row count does not match images')
    write_csv('results/csv_image_alignment.csv',rows)
    dossiers=[]
    for i,p in enumerate(paths):
        m=f'M{i+1:03d}'
        links=m_features[m]
        ws=sorted(m_to_w[m])
        reciprocal=[w for w in ws if w_to_m[w]=={m}]
        safe=ws[0] if len(ws)==1 and reciprocal==ws else None
        prof=profiles.get(safe,{})
        native=primary.get(m,{})
        nearest=sorted(range(len(paths)),key=lambda j:(-sim[i,j],j))[:5]
        dossiers.append({'sign':m, 'image':str(p.relative_to(ROOT)), 'sha256':sha256(p),
          'width':arrays[i].shape[1], 'height':arrays[i].shape[0],
          'foreground_fraction':float((arrays[i]>127).mean()), 'bounding_box':','.join(map(str,boxes[i])),
          'catalogue_descriptions':' | '.join(sorted(set(f['description'] for f in links))),
          'candidate_parpola_ids':';'.join(sorted(set(f['id'] for f in links))),
          'candidate_wells_ids':';'.join(ws),
          'mapping_status':'reciprocal_one_to_one_source_assertion' if safe else 'ambiguous_or_multiple' if ws else 'unmapped',
          'conditional_wells_profile':safe or '',
          'tokens_unique_texts':prof.get('tokens_unique_texts',''),
          'conditional_file_order_role':prof.get('provisional_distributional_role','unresolved'),
          'm77_solus':native.get('solus',''),'m77_initial':native.get('initial',''),
          'm77_medial':native.get('medial',''),'m77_final':native.get('final',''),
          'm77_total':native.get('total',''),
          'm77_distributional_description':native.get('distributional_description','not transcribed'),
          'm77_primary_pdf_page':native.get('primary_pdf_page',''),
          'visual_neighbors':';'.join(f'M{j+1:03d}:{sim[i,j]:.4f}' for j in nearest),
          'phonetic_reading':'undetermined','semantic_reading':'undetermined',
          'evidence_status':'visual inventory audited; direct M77 position counts where present; W/P crosswalk provisional; no established decipherment'})
    write_csv('results/sign_dossiers_417.csv',dossiers)
    write_json('results/sign_dossiers_417.json',dossiers)
    dup=defaultdict(list)
    for p,arr in zip(paths,arrays):
        dup[arr.tobytes()].append(p.stem)
    write_json('results/image_audit.json',{'images':len(paths),'csv_rows':len(rows),
        'csv_columns':len(arrays[0].reshape(-1)), 'exact_aligned_rows':sum(r['exact_pixel_match'] for r in rows),
        'pixel_identical_groups':[v for v in dup.values() if len(v)>1],
        'image_dimension_counts':dict(Counter(str(a.shape) for a in arrays)),
        'mapping_status_counts':dict(Counter(d['mapping_status'] for d in dossiers)),
        'direct_m77_profile_count':sum(bool(d['m77_total']) for d in dossiers),
        'csv_sha256':sha256(ROOT/'im_417_150.csv'),
        'note':'Catalogue numbering is presumed from input naming and external attribution. Crosswalk assertions are not validated by pixel similarity.'})
    # Contact sheets invert display only, preserving source files.
    for page in range(5):
        subset=dossiers[page*90:(page+1)*90]
        canvas=Image.new('RGB',(1200,((len(subset)+9)//10)*132),'white')
        draw=ImageDraw.Draw(canvas)
        for j,d in enumerate(subset):
            img=ImageOps.invert(Image.open(ROOT/d['image']).convert('L'))
            img.thumbnail((106,106))
            x,y=(j%10)*120,(j//10)*132
            canvas.paste(img,(x+7,y+3))
            draw.text((x+37,y+112),d['sign'],fill='black')
        canvas.save(ROOT/f'results/contact_sheet_{page+1}.png')
    cards=[]
    for d in dossiers:
        desc=d['catalogue_descriptions'] or 'No description in the external crosswalk.'
        native_html=(f'''<p><b>Mahadevan 1977:</b> {d['m77_total']} occurrences · alone {d['m77_solus']} · initial {d['m77_initial']} · medial {d['m77_medial']} · final {d['m77_final']}.
          <a href="../data/raw/mahadevan_1977_text.pdf#page={d['m77_primary_pdf_page']}">Printed source</a></p>
          <p class="meta">{d['m77_distributional_description']}. Positions refer to a line in reading order, not the secondary CSV's file order.</p>''' if d['m77_total'] else '')
        cards.append(f'''<article data-search="{html.escape(' '.join(map(str,d.values())),quote=True)}">
          <img loading="lazy" src="../{d['image']}" alt="{d['sign']}">
          <div><h2>{d['sign']}</h2><p>{html.escape(desc)}</p>
          {native_html}
          <p class="meta">Source-asserted links: {html.escape(d['candidate_parpola_ids']) or '—'} · {html.escape(d['candidate_wells_ids']) or '—'}</p>
          <p class="meta">Mapping: {d['mapping_status']}. Conditional distribution: {d['conditional_file_order_role']}.</p>
          <p>Sound and meaning: <b>undetermined</b></p></div></article>''')
    content='''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Indus sign evidence atlas · 417 signs</title><style>
    body{font:16px/1.5 system-ui;margin:40px auto;padding:0 24px;max-width:1100px;background:#faf8f1;color:#242b2b}
    h1{font:42px Georgia}h2{margin:0;font-size:20px}p{margin:8px 0}.meta{color:#5b6565;font-size:13px}
    input{font:18px system-ui;padding:14px;width:95%;margin:20px 0;border:1px solid #c5c9be;border-radius:8px}
    article{display:flex;gap:24px;padding:24px;background:white;border:1px solid #deded2;margin:12px 0;border-radius:10px}
    img{width:120px;height:120px;object-fit:contain;filter:invert(1)} article[hidden]{display:none}
    .notice{border-left:4px solid #a77d27;padding:12px 20px;background:#f3ecda}a{color:#195956}
    </style><h1>Indus sign evidence atlas</h1><p>All 417 supplied signs · reproducible inventory · 22 September 2026</p>
    <p class="notice">This is an evidence catalogue, not a translation key. Object-like descriptions name shapes.
    They do not identify ancient meanings. M77 counts come directly from the printed frequency table.
    Crosswalks are attributed to the mayig catalogue and remain provisional.
    A conditional role applies only if that crosswalk and the secondary transcription are correct.</p>
    <p><a href="../docs/REPORT.md">Research report</a> · <a href="sign_dossiers_417.csv">Download all sign dossiers</a> · <a href="../docs/ALL_SIGN_EVIDENCE.md">Consolidated evidence and association limits</a></p>
    <input id="search" type="search" placeholder="Search sign ID, shape, or candidate correspondence" aria-label="Search sign evidence">
    <p id="count">417 signs</p>'''+''.join(cards)+'''
    <script>document.querySelector('#search').addEventListener('input',e=>{let n=0;const q=e.target.value.toLowerCase();
    document.querySelectorAll('article').forEach(a=>{a.hidden=!a.dataset.search.toLowerCase().includes(q);if(!a.hidden)n++});
    document.querySelector('#count').textContent=n+' signs'});</script>'''
    (ROOT/'results/sign_atlas.html').write_text(content)

if __name__=='__main__':
    main()
