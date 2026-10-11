"""Reproduce secondary row selection and bounded local OCR identity searches."""
from pathlib import Path
import csv,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','cisi','site','area-section','excavation-idno','material','shape','cross-section','preservation','symbol','type','sides','condition','complete','text','horizontal(mm)','vertical(mm)','thickness(mm)']
rows=[{k:r.get(k) for k in FIELDS} for r in csv.DictReader((ROOT/'data/raw/lipi_inscriptions.csv').open()) if r['id'] in {'624.1','624.2','1729.1'}]
searches=[]
for source in ['data/raw/vats_1940_text_18220_djvu.txt','results/iconography-mahadevan_extracted.txt']:
 s=(ROOT/source).read_text()
 for pattern in [r'14307',r'14[\s,.]*307']:
  searches.append(dict(source=source,pattern=pattern,matches=[dict(offset=m.start(),context=s[max(0,m.start()-120):m.end()+120]) for m in re.finditer(pattern,s)]))
out={'secondary_rows':rows,'excluded_columns':['sanskrit','translation','notes'],'local_searches':searches,'warning':'No OCR hit does not prove absence from original book; OCR and coverage can fail.'}
(ROOT/'data/processed/comb_tablet_source_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('Retained',len(rows),'secondary rows and',len(searches),'bounded searches')
