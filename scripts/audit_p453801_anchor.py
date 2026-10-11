"""Audit a proposed name-anchor lead without converting missing evidence to values.

Parses these pinned CDLI exports, preserves textual differences, and excludes a
catalogue's explicitly generic seal link from object-identity evidence. This is
not an ATF transliterator or a cuneiform/Indus decipherment program.
"""
from pathlib import Path
import hashlib
import json
import re
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[1]

def parse_atf(text):
    artifact=None; section=None; language=None; lines=[]; annotations=[]
    for raw in text.splitlines():
        line=raw.strip()
        if not line: continue
        if line.startswith('&'):
            m=re.fullmatch(r'&(P\d+)\s*=\s*(.+)',line)
            if not m: raise ValueError('Unexpected ATF header')
            artifact=m.group(1)
        elif line.startswith('#atf: lang '):
            language=line.removeprefix('#atf: lang ')
        elif line.startswith('#'):
            continue  # Translation/comment lines, not text on the artifact.
        elif line.startswith('@'):
            section=line[1:]
        elif line.startswith('$'):
            annotations.append({'section':section,'status':line[1:].strip()})
        else:
            m=re.fullmatch(r"([0-9]+[a-z']*)\.\s+(.+)",line)
            if not m: raise ValueError('Unsupported ATF line: '+line)
            lines.append({'section':section,'label':m.group(1),'text':m.group(2)})
    if artifact is None: raise ValueError('Missing artifact identifier')
    return {'artifact':artifact,'top_level_language_code':language,
            'lines':lines,'annotations':annotations}

def compare_lines(a,b):
    def indexed(record):
        result={}
        for line in record['lines']:
            key=(line['section'],line['label'])
            if key in result: raise ValueError('Duplicate section/line label')
            result[key]=line['text']
        return result
    left,right=indexed(a),indexed(b)
    return [{'section':key[0],'label':key[1],'left':left.get(key),'right':right.get(key)}
            for key in sorted(set(left)|set(right)) if left.get(key)!=right.get(key)]

def classified_seals(record):
    rows=[]
    for relation in record.get('seals',[]):
        seal=relation['seal']
        placeholder=seal.get('seal_no')=='S999999' or 'dummy' in seal.get('designation','').lower()
        rows.append({'id':seal['id'],'designation':seal.get('designation'),
                     'seal_no':seal.get('seal_no'),'explicit_placeholder':placeholder})
    return rows

def usable_shared_seal_ids(a,b):
    return sorted({s['id'] for s in classified_seals(a) if not s['explicit_placeholder']} &
                  {s['id'] for s in classified_seals(b) if not s['explicit_placeholder']})

class ImageSources(HTMLParser):
    def __init__(self):
        super().__init__(); self.sources=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='img' and a.get('src'): self.sources.append(a['src'])

def main():
    paths={
      'record453801':'data/raw/cdli_p453801_artifact.json',
      'record516366':'data/raw/cdli_p516366_artifact.json',
      'old':'data/raw/cdli_p453801_historical_2249158.atf',
      'current':'data/raw/cdli_p453801_current_2289564.atf',
      'comparison':'data/raw/cdli_p516366_current_2335716.atf',
      'html':'data/raw/cdli_p453801_artifact.html'}
    records={}
    for key,expected in [('record453801',453801),('record516366',516366)]:
        raw=json.loads((ROOT/paths[key]).read_text())
        if len(raw)!=1 or raw[0]['id']!=expected: raise ValueError('Unexpected export identity')
        records[key]=raw[0]
    texts={k:parse_atf((ROOT/paths[k]).read_text()) for k in ['old','current','comparison']}
    for record_key,text_key in [('record453801','current'),('record516366','comparison')]:
        embedded=parse_atf(records[record_key]['inscription']['atf'])
        if embedded!=texts[text_key]: raise ValueError('JSON and ATF exports disagree')
    if texts['old']['artifact']!=texts['current']['artifact']: raise ValueError('Revision identity changed')
    parser=ImageSources();parser.feed((ROOT/paths['html']).read_text())
    result={
      'scope':'Pinned record comparison, not a new reading of the tablet or seal',
      'inputs_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths.values()},
      'records':{k:{'id':v['id'],'designation':v['designation'],'museum_no':v.get('museum_no'),
                    'dates_referenced':v.get('dates_referenced'),'seals':classified_seals(v)} for k,v in records.items()},
      'parsed_texts':texts,
      'historical_to_current_changes':compare_lines(texts['old'],texts['current']),
      'current_to_comparison_changes':compare_lines(texts['current'],texts['comparison']),
      'nonplaceholder_shared_seal_ids':usable_shared_seal_ids(records['record453801'],records['record516366']),
      'html_image_sources':parser.sources,
      'html_has_no_image_placeholder':'/images/no-image.jpg' in parser.sources,
      'indus_seal_transcription':None,
      'established_indus_name_pair':False,
      'limitations':[
        'Shared generic seal IDs do not establish the same physical seal or its owner.',
        'An illegible seal annotation is not a legible Indus sequence or a classification of its script.',
        'Top-level Sumerian metadata is not assigned to the unread seal separately.',
        'Spelling/version differences are preserved, not silently pooled as phonetic alternatives.',
        'Different database IDs neither prove two physical objects nor prove independent attestations.',
        'The catalogue HTML placeholder is not proof that no photograph exists elsewhere.',
        'Independent primary handcopy and BDTNS date/duplication caveats are in separate manual reviews.'
      ]}
    (ROOT/'results/p453801_anchor_audit.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:result[k] for k in ['historical_to_current_changes','current_to_comparison_changes','nonplaceholder_shared_seal_ids','html_has_no_image_placeholder','established_indus_name_pair']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
