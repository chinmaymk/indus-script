"""Build a hash-pinned, double-reviewed native M77 corpus without reversing rows.

Manifest pages contain source_pdf_page, source_printed_page, ordered expected_rows
({reference,side,line}), and review_a/review_b ({path,sha256}). The root source_pdf
is also pinned. Reviews follow m77-review-submission-1. Run --help for output paths.
Unresolved differences always appear in comparison output; publication normally
requires their adjudication. --agreements-only explicitly permits a partial corpus.
"""
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = ('reference', 'side', 'line')
FIELDS = ('printed_row_index', *KEY, 'object_type_code', 'field_symbol_code',
          'direction_code', 'printed_metadata_literal', 'expanded_metadata_code',
          'inherited_from_row', 'normalized_order', 'tokens', 'segments', 'record_kind')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def row_key(row):
    require(all(isinstance(row.get(k), str) and row[k].isdigit() for k in KEY), 'row key must contain digit strings')
    return tuple(row[k] for k in KEY)

def validate_row(row, dimensions):
    key = row_key(row)
    require(all(f in row for f in FIELDS), f'{key}: missing required fields')
    require(row['normalized_order'] == 'right_to_left', f'{key}: tokens must already be normalized right_to_left')
    require(row['record_kind'] == 'text_line', f'{key}: unexpected record kind')
    for field, length in [('object_type_code',1),('field_symbol_code',2),('direction_code',1)]:
        require(isinstance(row[field],str) and row[field].isdigit() and len(row[field])==length, f'{key}: invalid {field}')
    expanded = row['object_type_code']+row['side']+row['field_symbol_code']+row['line']+row['direction_code']
    require(row['expanded_metadata_code']==expanded, f'{key}: expanded metadata conflicts with fields')
    require(isinstance(row['printed_metadata_literal'],str) and row['printed_metadata_literal'], f'{key}: missing printed metadata')
    bbox=row.get('line_bbox_render_pixels')
    require(isinstance(bbox,list) and len(bbox)==4 and all(type(v) is int for v in bbox), f'{key}: invalid bbox')
    require(0<=bbox[0]<bbox[2]<=dimensions[0] and 0<=bbox[1]<bbox[3]<=dimensions[1], f'{key}: bbox out of render')
    require(isinstance(row['tokens'],list) and row['tokens'] and isinstance(row['segments'],list) and len(row['tokens'])==len(row['segments']), f'{key}: tokens/segments mismatch')
    for pos,(token,seg) in enumerate(zip(row['tokens'],row['segments']),1):
        require(seg.get('position_from_right')==pos, f'{key}: segment position mismatch')
        require(type(seg.get('source_doubt')) is bool, f'{key}: missing source doubt')
        kind=seg.get('kind')
        if kind=='identified_sign':
            sign=seg.get('sign')
            require(isinstance(sign,str) and re.fullmatch(r'M\d{3}',sign) and 1<=int(sign[1:])<=417, f'{key}: invalid native M77 sign')
            require(token==('*' if seg['source_doubt'] else '')+sign, f'{key}: token and source doubt disagree')
            require(seg.get('minimum_signs',1)==1 and seg.get('maximum_signs',1)==1, f'{key}: identified sign occupies exactly one sign')
            require('reviewer_uncertainty' not in seg or type(seg['reviewer_uncertainty']) is bool, f'{key}: invalid reviewer uncertainty')
            require('candidate_signs' not in seg or isinstance(seg['candidate_signs'],list), f'{key}: invalid candidate signs')
        elif kind=='unknown_length_loss':
            require(token=='LOSS' and seg.get('sign') is None and not seg['source_doubt'], f'{key}: loss is not a doubtful sign')
            require(type(seg.get('minimum_signs')) is int and seg['minimum_signs']==1 and 'maximum_signs' in seg and seg['maximum_signs'] is None, f'{key}: LOSS must have minimum1 and unbounded maximum')
        elif kind in ('visible_unidentified_glyph','unidentified_visible_sign'):
            require(token in ('UNKNOWN',('*' if seg['source_doubt'] else '')+'UNKNOWN') and seg.get('sign') is None, f'{key}: unknown glyph token invalid')
            require(seg.get('minimum_signs')==1 and seg.get('maximum_signs')==1, f'{key}: visible unknown glyph occupies exactly one sign')
        else:
            raise ValueError(f'{key}: unsupported segment kind {kind!r}')
    return key

def validate_review(review, page):
    require(review.get('schema_version')=='m77-review-submission-1', 'unsupported review schema')
    require(review.get('source_pdf_page')==page['source_pdf_page'] and review.get('source_printed_page')==page['source_printed_page'], 'review page identity mismatch')
    require(isinstance(review.get('reviewer'),str) and review['reviewer'], 'missing reviewer')
    dimensions=review.get('page_render_dimensions')
    require(isinstance(dimensions,list) and len(dimensions)==2 and all(type(x) is int and x>0 for x in dimensions), 'invalid render dimensions')
    expected=[row_key(r) for r in page['expected_rows']]
    require(expected and len(set(expected))==len(expected), 'duplicate/empty expected row keys')
    keys=[]; by_index={}
    for index,row in enumerate(review['rows'],1):
        key=validate_row(row,dimensions); keys.append(key)
        require(row['printed_row_index']==index, 'printed row indices must be contiguous and ordered')
        inherited=row['inherited_from_row']
        if inherited is not None:
            require(type(inherited) is int and inherited in by_index, f'{key}: invalid inherited metadata row')
            prior=by_index[inherited]
            require(prior['reference']==row['reference'], f'{key}: cannot inherit metadata across objects')
            # Pointer records the printed continuation; individual lines/faces
            # may retain different explicit metadata, especially direction.
        literal=row['printed_metadata_literal']
        require(literal.isdigit() and 1<=len(literal)<=6, f'{key}: printed metadata must be one to six digits')
        if inherited is None:
            require(len(literal)==6, f'{key}: abbreviated metadata requires an inheritance pointer')
            reconstructed=literal
        else:
            reconstructed=by_index[inherited]['expanded_metadata_code'][:6-len(literal)]+literal
        require(reconstructed==row['expanded_metadata_code'], f'{key}: printed metadata/inheritance conflicts with expanded metadata')
        by_index[index]=row
    require(len(keys)==len(set(keys)), 'duplicate row keys in review')
    require(keys==expected, f'full page row coverage mismatch: missing={sorted(set(expected)-set(keys))}, extra={sorted(set(keys)-set(expected))}, order_match={keys==expected}')
    return {row_key(r):r for r in review['rows']}

def compare_page(page, a, b, decisions=None):
    left=validate_review(a,page); right=validate_review(b,page)
    require(a['reviewer']!=b['reviewer'], 'A and B must be distinct reviewer identities')
    decisions=decisions or {}; records=[]; differences=[]; used=set()
    for expected in page['expected_rows']:
        key=row_key(expected); x=left[key]; y=right[key]
        def content(field, value):
            # Optional reviewer annotations are retained separately, not equated
            # with printed source doubt or silently promoted to transcription.
            if field!='segments':return value
            projected=[]
            for seg in value:
                item={k:v for k,v in seg.items() if k not in ('reviewer_uncertainty','candidate_signs')}
                if item['kind']=='identified_sign':
                    item.setdefault('minimum_signs',1);item.setdefault('maximum_signs',1)
                projected.append(item)
            return projected
        changed={f:{'A':x[f],'B':y[f]} for f in FIELDS if content(f,x[f])!=content(f,y[f])}
        if any(s.get('reviewer_uncertainty') or s.get('candidate_signs') for r in (x,y) for s in r['segments']):
            changed['reviewer_uncertainty']={'A':x['segments'],'B':y['segments']}
        chosen=None; resolution='exact_agreement'
        if changed:
            difference={'source_pdf_page':page['source_pdf_page'],'key':list(key),'fields':changed,'adjudicated':False}
            decision=decisions.get(key)
            if decision:
                require(isinstance(decision.get('reason'),str) and decision['reason'].strip(), f'{key}: adjudication needs reason')
                require(decision.get('source_pins'), f'{key}: adjudication needs primary evidence pins')
                resolution=decision.get('resolution')
                require(resolution in ('A','B','custom'), f'{key}: invalid resolution')
                chosen=x if resolution=='A' else y if resolution=='B' else decision['row']
                dims=a['page_render_dimensions'] if resolution!='B' else b['page_render_dimensions']
                require(validate_row(chosen,dims)==key and chosen['printed_row_index']==x['printed_row_index'], f'{key}: adjudication changed row identity')
                difference.update(adjudicated=True,decision=decision);used.add(key)
            differences.append(difference)
        else:
            chosen=x
        if chosen is not None:
            record={f:copy.deepcopy(chosen[f]) for f in FIELDS}
            record.update(source_pdf_page=page['source_pdf_page'],source_printed_page=page['source_printed_page'],verification=resolution,reviewer_bboxes={'A':x['line_bbox_render_pixels'],'B':y['line_bbox_render_pixels']},reviewer_segments={'A':x['segments'],'B':y['segments']},length_bounds=length_bounds(chosen))
            records.append(record)
    require(set(decisions)==used, 'adjudication targets an absent or already-agreed row')
    return records,differences

def length_bounds(row):
    minimum=sum(s.get('minimum_signs',1) for s in row['segments'])
    maximum=None if any(s['kind']=='unknown_length_loss' for s in row['segments']) else len(row['segments'])
    return {'minimum_signs':minimum,'maximum_signs':maximum,'unknown_length_loss_spans':sum(s['kind']=='unknown_length_loss' for s in row['segments']),'visible_unidentified_glyphs':sum(s['kind'] in ('visible_unidentified_glyph','unidentified_visible_sign') for s in row['segments'])}

def verify_pin(pin, root=ROOT):
    path=Path(pin['path'])
    require(not path.is_absolute() and '..' not in path.parts, 'pinned paths must be repository relative')
    actual=hashlib.sha256((root/path).read_bytes()).hexdigest()
    require(actual==pin['sha256'], f'hash mismatch: {path}')

def load_pinned(pin, root=ROOT):
    verify_pin(pin,root);return json.loads((root/pin['path']).read_text())

def candidate_comparison(records, candidates):
    grouped={}
    for row in records:grouped.setdefault(row['reference'],[]).append(row)
    indexed={}
    for row in candidates:indexed.setdefault(str(row['source_reference']),[]).append(row)
    out=[]
    for reference,rows in grouped.items():
        old=indexed.get(reference,[])
        normalized=[];errors=[]
        for candidate in old:
            try:normalized.append(normalize_candidate_tokens(candidate['tokens']))
            except (ValueError,KeyError,TypeError) as error:
                normalized.append(None);errors.append(str(error))
        status='not_in_candidate_export' if not old else 'candidate_schema_error' if errors else 'not_comparable_multiple_lines_or_export_records' if len(rows)!=1 or len(old)!=1 else 'exact_tokens' if rows[0]['tokens']==normalized[0] else 'token_mismatch'
        out.append({'reference':reference,'status':status,'verified_row_keys':[list(row_key(r)) for r in rows],'candidate_ids':[r.get('id') for r in old],'candidate_tokens':[r.get('tokens') for r in old],'candidate_normalized_tokens':normalized,'candidate_schema_errors':errors,'verified_tokens':[r['tokens'] for r in rows]})
    return out

def normalize_candidate_tokens(tokens):
    """Normalize the documented secondary-export token schema for reporting only."""
    require(isinstance(tokens,list),'candidate tokens must be a list')
    normalized=[]
    for token in tokens:
        if isinstance(token,str):
            require(token in ('LOSS','UNKNOWN') or re.fullmatch(r'\*?M\d{3}',token),'invalid candidate token string')
            normalized.append(token);continue
        require(isinstance(token,dict),'invalid candidate token object')
        require(type(token.get('unknown_span')) is bool and type(token.get('doubtful')) is bool,'candidate uncertainty flags must be booleans')
        if token['unknown_span']:
            require(token.get('sign') is None,'candidate loss cannot also identify a sign')
            normalized.append('LOSS')
        else:
            sign=token.get('sign')
            require(isinstance(sign,str) and re.fullmatch(r'M\d{3}',sign),'candidate identified sign is invalid')
            normalized.append(('*' if token['doubtful'] else '')+sign)
    return normalized

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['manifest','comparison','output']:parser.add_argument('--'+name,required=True,type=Path)
    parser.add_argument('--adjudications',type=Path);parser.add_argument('--candidate-export',type=Path)
    parser.add_argument('--agreements-only',action='store_true')
    args=parser.parse_args(); manifest=json.loads(args.manifest.read_text())
    require(manifest.get('schema_version')=='m77-page-manifest-1','unsupported manifest schema')
    verify_pin(manifest['source_pdf'])
    page_ids=[p['source_pdf_page'] for p in manifest['pages']]
    require(page_ids and len(set(page_ids))==len(page_ids),'duplicate/empty manifest pages')
    adjudication=json.loads(args.adjudications.read_text()) if args.adjudications else {'decisions':[]}
    review_pins=[p[k] for p in manifest['pages'] for k in ['review_a','review_b']]
    if args.adjudications:
        require(adjudication.get('review_pins')==review_pins,'adjudication must pin the exact ordered A/B input files')
    decisions={};records=[];differences=[]
    for d in adjudication['decisions']:
        key=(d['source_pdf_page'],tuple(d['key']))
        require(key not in decisions,'duplicate adjudication key');decisions[key]=d
        require(key[0] in page_ids,'adjudication page absent')
        for pin in d.get('source_pins',[]):verify_pin(pin)
    for page in manifest['pages']:
        reviews=[load_pinned(page[k]) for k in ['review_a','review_b']]
        for review in reviews:
            require(manifest['source_pdf'] in review.get('source_pins',[]),'review does not pin the manifest source PDF')
            for pin in review['source_pins']+review.get('auxiliary_visual_crops',[]):verify_pin(pin)
            require(any(p['path']==review['page_render'] for p in review['source_pins']),'review page render must be pinned')
        ds={key[1]:value for key,value in decisions.items() if key[0]==page['source_pdf_page']}
        rows,diffs=compare_page(page,*reviews,ds);records+=rows;differences+=diffs
    keys=[row_key(r) for r in records];require(len(keys)==len(set(keys)),'duplicate row key across pages')
    unresolved=sum(not d['adjudicated'] for d in differences)
    report={'schema_version':'m77-comparison-1','review_pins':review_pins,'expected_rows':sum(len(p['expected_rows']) for p in manifest['pages']),'accepted_rows':len(records),'unresolved_differences':unresolved,'differences':differences}
    if args.candidate_export:
        candidates=[json.loads(s) for s in args.candidate_export.read_text().splitlines() if s.strip()]
        report['candidate_export']={'path':str(args.candidate_export),'sha256':hashlib.sha256(args.candidate_export.read_bytes()).hexdigest(),'comparison':candidate_comparison(records,candidates),'used_to_resolve_primary_reviews':False}
    args.comparison.parent.mkdir(parents=True,exist_ok=True);args.comparison.write_text(json.dumps(report,indent=2)+'\n')
    if unresolved and not args.agreements_only:
        raise SystemExit(f'{unresolved} unresolved rows; comparison written, corpus NOT written (any prior output remains historical).')
    provenance={'manifest':{'path':str(args.manifest),'sha256':hashlib.sha256(args.manifest.read_bytes()).hexdigest()},'review_pins':review_pins,'source_pdf':manifest['source_pdf']}
    if args.adjudications:provenance['adjudications']={'path':str(args.adjudications),'sha256':hashlib.sha256(args.adjudications.read_bytes()).hexdigest()}
    output={'schema_version':'verified-m77-1','coverage_complete_for_manifest':not unresolved,'unresolved_rows':unresolved,'normalized_order':'right_to_left','automatic_reversals':0,'provenance':provenance,'rows':records,'limitations':['M77 printed-transcription fidelity only; not object-photograph verification.','Complete row coverage may include explicitly unidentified visible signs and unknown-length losses; it does not establish every sign identity.','Review agreement does not establish ancient readings or statistically independent artifacts.']}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'published_rows':len(records),'unresolved_rows':unresolved,'full_page_coverage':not unresolved}))

if __name__=='__main__':main()
