"""Declared same-length comparandum retrieval; stored W codes, never readings."""
import csv,json,re
from collections import Counter
from common import ROOT,sha256,write_json

TARGET=('391','002','365','550')

def parse_closed_slots(text):
    """Closed-plus code slots; ambiguity retained, damaged/boundary syntax rejected."""
    if not re.fullmatch(r'\+\d{3}(?:/\d{3})*(?:-\d{3}(?:/\d{3})*)*\+',text):
        return None
    slots=tuple(frozenset(t.split('/')) for t in text[1:-1].split('-'))
    if any(s & {'000','999'} for s in slots):return None
    return slots

def possible_relations(slots,target=TARGET):
    """Set-valued relations; a slash row is never a certain transcription."""
    if slots is None or len(slots)!=len(target):return []
    out=[]
    if all(t in slot for slot,t in zip(slots,target)):out.append('exact_duplicate_compatible')
    for i,slot in enumerate(slots):
        if slot-{target[i]} and all(target[j] in slots[j] for j in range(len(target)) if j!=i):
            out.append('one_position_'+str(i)+'_compatible')
    return out

def exact_relations(slots,target=TARGET):
    if slots is None or len(slots)!=len(target) or any(len(s)!=1 for s in slots):return []
    seq=tuple(next(iter(s)) for s in slots)
    diff=[i for i,(a,b) in enumerate(zip(seq,target)) if a!=b]
    if not diff:return ['exact_duplicate']
    if len(diff)==1:return ['one_position_'+str(diff[0])]
    return []

def parse_row(text):
    s=text.strip()
    if len(s)<2 or s[0] not in '+[]' or s[-1] not in '+[]':return 'other_excluded','missing_or_invalid_endpoint',None
    cells=s[1:-1].split('-')
    if len(cells)!=4:return 'other_excluded','not_four_cells',None
    if not all(re.fullmatch(r'[0-9]{3}(?:/[0-9]{3})*',c) for c in cells):return 'other_excluded','malformed_cell_or_interior_boundary',None
    slots=tuple(frozenset(c.split('/')) for c in cells)
    if any(slot & {'000','999'} for slot in slots):return 'unknown_four_cell','unknown_or_separator_token',slots
    if any('/' in c for c in cells):return 'slash_sensitivity',None,slots
    if s[0]==s[-1]=='+':return 'primary',None,slots
    return 'boundary_sensitivity',None,slots

def literal_flags(slots):
    relations=exact_relations(slots)
    flags=[]
    if 'exact_duplicate' in relations:flags.append('exact_duplicate')
    if relations and relations[0].startswith('one_position_'):
        flags.append('one_position_substitution')
        if relations==['one_position_0']:flags.append('initial_substitution_exact_tail')
    return flags

def main():
    protocol_path='data/processed/dhr24475_context_protocol.json'
    protocol=json.loads((ROOT/protocol_path).read_text())
    assert sha256(ROOT/protocol_path)=='56b5e3b0477baa90297b5397c09c95aba767b02033ad2404ac2d2f11292ab7c5'
    source=protocol['source'];assert sha256(ROOT/source['path'])==source['sha256']
    assert (ROOT/source['path']).stat().st_size==source['bytes']
    assert tuple(protocol['seed']['tokens'])==TARGET
    rows=list(csv.DictReader((ROOT/source['path']).open()))
    excluded=set(protocol['scope']['excluded_columns'])
    ledger=[];hits=[];uncertain=[]
    for number,row in enumerate(rows,2):
        branch,reason,slots=parse_row(row['text'])
        ledger.append({'csv_row':number,'id':row['id'],'text':row['text'],'branch':branch,'exclusion_reason':reason})
        record={'csv_row':number,'raw':{k:v for k,v in row.items() if k not in excluded},'branch':branch,'is_seed':row['id']==protocol['seed']['id'],'literal_seed_text_equal':row['text']==protocol['seed']['text'],'possible_row_family':row['id'].split('.')[0] if re.fullmatch(r'[0-9]+\.[0-9]+',row['id']) else None}
        if branch=='unknown_four_cell':uncertain.append(record);continue
        if branch=='other_excluded':continue
        record['slots']=[sorted(s) for s in slots]
        if branch=='slash_sensitivity':
            lo=sum(t not in s for t,s in zip(TARGET,slots));hi=sum(bool(s-{t}) for t,s in zip(TARGET,slots))
            flags=[]
            if lo==0:flags.append('possible_duplicate')
            if lo<=1<=hi:flags.append('possible_one_position')
            if all(TARGET[i] in slots[i] for i in (1,2,3)) and slots[0]-{TARGET[0]}:flags.append('possible_initial_substitution_exact_tail')
            record.update(minimum_distance=lo,maximum_distance=hi,flags=flags)
        else:
            seq=[next(iter(s)) for s in slots]
            record.update(tokens=seq,changed_positions=[i for i in range(4) if seq[i]!=TARGET[i]],flags=literal_flags(slots))
        if record['flags']:hits.append(record)
    counts={}
    for branch in ['primary','boundary_sensitivity','slash_sensitivity']:
        subset=[r for r in hits if r['branch']==branch]
        names=['possible_duplicate','possible_one_position','possible_initial_substitution_exact_tail'] if branch=='slash_sensitivity' else ['exact_duplicate','one_position_substitution','initial_substitution_exact_tail']
        counts[branch]={}
        for name in names:
            selected=[r for r in subset if name in r['flags']]
            counts[branch][name]={'rows':len(selected),'distinct_raw_strings':len({r['raw']['text'] for r in selected}),'seed_rows':sum(r['is_seed'] for r in selected),'additional_rows':sum(not r['is_seed'] for r in selected)}
            if branch!='slash_sensitivity':counts[branch][name]['distinct_token_tuples']=len({tuple(r['tokens']) for r in selected})
    stems={r['possible_row_family'] for r in hits}-{None}
    companions=[{'csv_row':i,'raw':{k:v for k,v in row.items() if k not in excluded},'is_hit':i in {r['csv_row'] for r in hits}} for i,row in enumerate(rows,2) if re.fullmatch(r'[0-9]+\.[0-9]+',row['id']) and row['id'].split('.')[0] in stems]
    paths=[protocol_path,source['path'],'docs/DHR24475_CONTEXT_DESIGN.md','docs/DHR24475_CONTEXT_IMPLEMENTATION.md','scripts/screen_dhr24475_contexts.py','scripts/prepare_corpora.py','tests/test_dhr24475_contexts.py']
    result={'scope':'Stored-string comparandum locator, not primary reading, identity or meaning.','protocol':protocol,'implementation_unknown_tokens':['000','999'],'summary':{'source_rows':len(rows),'parser_categories':dict(Counter(r['branch'] for r in ledger)),'exclusion_reasons':dict(Counter(r['exclusion_reason'] for r in ledger if r['exclusion_reason'])),'counts_by_branch_class':counts,'distinct_matching_source_rows':len(hits)},'hits':hits,'uncertainty_ledger':uncertain,'parser_ledger':ledger,'same_stem_companions_not_extra_hits':companions,'input_sha256':{p:sha256(ROOT/p) for p in paths},'established_semantic_values':0,'established_phonetic_values':0,'physical_artifact_count':None}
    write_json('results/dhr24475_context_screen.json',result)
    print(json.dumps(result['summary'],indent=2))
    for r in hits:print(r['raw']['id'],r['raw']['cisi'],r['raw']['excavation-idno'],r['raw']['text'],r['branch'],r['flags'])

if __name__=='__main__':main()
