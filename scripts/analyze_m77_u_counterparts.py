"""Test exact counterpart-to-stroke-state constraints on a primary-reviewed census.

Catalogue references are counting units, not proven independent transactions.
This code tests deterministic relations; it assigns no numerical or lexical value.
"""
from collections import Counter, defaultdict
import csv
import json
from common import ROOT, read_jsonl, sha256, write_json, write_jsonl
from analyze_m77_u_fields import simple_field, verify_fingerprints, PILOTS, REVIEW, normalize
from analyze_m77_u_object_types import strict
from recover_m77_u_concordance import validate_tokens

PROTOCOL = 'data/processed/m77_u_counterpart_protocol.json'
FIELDS = 'data/processed/m77_u_typed_lines.jsonl'
CANDIDATE = 'data/processed/m77_candidate_records.jsonl'
CROSSCHECK = 'data/processed/m77_u_counterpart_parent_crosscheck.json'
CORRECTIONS = 'data/processed/m77_u_3234_primary_review.json'
REVIEWS = [f'data/processed/m77_u_counterpart_correction_crosscheck_{part}.json' for part in ('structure','iconography')] + ['data/processed/m77_u_counterpart_promotion_crosscheck_numerals.json']
LEDGERS = [f'data/processed/m77_u_counterparts_{part}.json' for part in
           ('structure','numerals','iconography')]


def key(reference, side, line):
    return f'M77:{reference}:side{side}:line{line}'


def collect(ledgers, field_lines):
    selected = {r['id'] for r in field_lines}
    refs = {r['reference'] for r in field_lines}
    reviews = {}
    for path,doc in ledgers.items():
        for row in doc.get('rows',doc.get('records',[])):
            ref = str(row['reference'])
            if ref in reviews: raise ValueError('Duplicate reference review '+ref)
            seen = set()
            counterparts = []
            for r in row['counterpart_lines']:
                ident = key(ref,str(r['side']),str(r['line']))
                if ident in selected: raise ValueError('Selected field reused as counterpart '+ident)
                if ident in seen: raise ValueError('Duplicate counterpart line '+ident)
                seen.add(ident)
                validate_tokens(r['tokens'])
                if str(r['line'])=='9': raise ValueError('Symbol-only entry treated as text '+ident)
                counterparts.append(dict(r,id=ident,reference=ref,side=str(r['side']),line=str(r['line']),
                    has_primary_loss='LOSS' in r['tokens'],
                    has_primary_doubt=any(t.startswith('*') for t in r['tokens']),
                    has_reviewer_unknown=any(t.lstrip('*')=='UNKNOWN' for t in r['tokens']),
                    normalized_reading_order='right_to_left',
                    actual_direction_code=r.get('actual_direction_code')))
            reviews[ref] = dict(row, reference=ref, review_ledger=path,
                counterpart_lines=sorted(counterparts,key=lambda r:(r['side'],r['line'])))
    if set(reviews) != refs: raise ValueError('Counterpart reference coverage differs from field census')
    return reviews


def bundle(row):
    """Tuple of separate positioned lines, not concatenated sign sequences."""
    return tuple((r['side'],r['line'],tuple(r['tokens'])) for r in row['counterpart_lines'])


def exclusion_reasons(row):
    reasons = []
    if row.get('all_counterpart_lines_accounted_for') is not True:
        reasons.append('not_all_other_lines_accounted_for')
    if not row['counterpart_lines']: reasons.append('no_textual_counterpart')
    for r in row['counterpart_lines']:
        if not r.get('full_sequence_primary_checked'): reasons.append('not_fully_primary_checked')
        for name in ('has_primary_loss','has_primary_doubt','has_reviewer_unknown'):
            if r[name]: reasons.append(name)
    return sorted(set(reasons))


def eligible(row):
    # An empty or partial transcription is not a fully identified counterpart.
    return not exclusion_reasons(row)


def paired_states(fields, reviews):
    byref = defaultdict(list)
    for r in fields: byref[r['reference']].append(r)
    rows = []
    for ref,fs in sorted(byref.items()):
        types = {r['primary_object_type_code'] for r in fs}
        if len(types)!=1 or None in types: raise ValueError('Unverified or inconsistent primary object type')
        field_state = tuple((r['side'],r['line'],simple_field(r['tokens']))
                            for r in sorted(fs,key=lambda r:(r['side'],r['line'])))
        if any(c is None for _,_,c in field_state): raise ValueError('Nonexact field in selected set')
        rows.append({'reference':ref,'primary_object_type_code':next(iter(types)),
            'field_line_ids':[r['id'] for r in fs],
            'field_state':field_state, 'counterpart_bundle':bundle(reviews[ref]),
            'eligible':eligible(reviews[ref]),'exclusion_reasons':exclusion_reasons(reviews[ref]),'review_ledger':reviews[ref]['review_ledger']})
    return rows


def relation_groups(rows, include_type=True, include_field_layout=True):
    """Group equal inputs to a deterministic map; count contradictory outputs.

    Including field layout prevents differing side counts from being mistaken for
    a same-layout count contrast. Each reference contributes one tuple of states.
    """
    groups = defaultdict(list)
    for row in rows:
        if not row['eligible']: continue
        groupkey = (row['primary_object_type_code'] if include_type else None,
                    row['counterpart_bundle'],
                    tuple((s,l) for s,l,c in row['field_state']) if include_field_layout else None)
        groups[groupkey].append(row)
    result = []
    for (typ,context,layout),members in sorted(groups.items(),key=lambda p:repr(p[0])):
        states = Counter(tuple(c for s,l,c in r['field_state']) for r in members)
        result.append({'object_type':typ,'counterpart_bundle':context,'field_layout':layout,
            'reference_count':len(members),'references':[r['reference'] for r in members],
            'distinct_stroke_states':len(states),
            'states':[{'graphic_counts':state,'reference_count':n,
                'references':[r['reference'] for r in members if tuple(c for s,l,c in r['field_state'])==state]}
                for state,n in sorted(states.items())],
            'minimum_reference_exceptions_to_single_valued_map':len(members)-max(states.values())})
    return result


def apply_context_corrections(lines, corrections):
    corrected = {r['id']:dict(r) for r in lines}
    if len(corrected)!=len(lines): raise ValueError('Duplicate context IDs')
    for fix in corrections['rows']:
        ident = fix['id']
        if ident not in corrected or corrected[ident]['tokens']!=fix['old_tokens']:
            raise ValueError('Correction target differs from preserved historical reading: '+ident)
        validate_tokens(fix['new_tokens'])
        row = corrected[ident]
        row['tokens'] = fix['new_tokens'].copy()
        row['transcription_correction'] = dict(fix,ledger=CORRECTIONS)
        row['has_primary_loss'] = 'LOSS' in row['tokens']
        row['has_primary_doubt'] = any(t.startswith('*') for t in row['tokens'])
        row['has_reviewer_unknown'] = any(t.lstrip('*')=='UNKNOWN' for t in row['tokens'])
    return [corrected[r['id']] for r in lines]


def main():
    protocol = json.loads((ROOT/PROTOCOL).read_text())
    historical_lines = read_jsonl(FIELDS)
    corrections = json.loads((ROOT/CORRECTIONS).read_text())
    all_lines = apply_context_corrections(historical_lines,corrections)
    fields = [r for r in all_lines if strict(r) and simple_field(r['tokens']) is not None]
    if set(protocol['field_line_ids']) != {r['id'] for r in fields}:
        raise ValueError('Field selection changed after protocol')
    if len(fields)!=len(protocol['field_line_ids']): raise ValueError('Duplicated field selection')
    docs = {p:json.loads((ROOT/p).read_text()) for p in LEDGERS}
    verified = {}
    verify_fingerprints(protocol,verified)
    verify_fingerprints(corrections,verified)
    for path in REVIEWS: verify_fingerprints(json.loads((ROOT/path).read_text()),verified)
    for d in docs.values(): verify_fingerprints(d,verified)
    crosscheck = json.loads((ROOT/CROSSCHECK).read_text())
    verify_fingerprints(crosscheck,verified)
    reviews = collect(docs,fields)
    for row in reviews.values():
        for r in row['counterpart_lines']:
            path = r['evidence_path']
            digest = r.get('image_sha256',r.get('evidence_sha256',verified.get(path)))
            if not digest or sha256(ROOT/path)!=digest:
                raise ValueError('No valid evidence-image fingerprint: '+path)
            if path in verified and verified[path]!=digest:
                raise ValueError('Conflicting image fingerprint: '+path)
            verified[path]=digest
    pairs = paired_states(fields,reviews)
    groups = relation_groups(pairs)
    pooled = relation_groups(pairs,include_type=False)
    counterpart_lines = [r for row in reviews.values() for r in row['counterpart_lines']]
    existing = {r['id']:r for r in all_lines}
    overlap = []
    for r in counterpart_lines:
        if any(t.lstrip('*')=='M328' for t in r['tokens']) and r['id'] not in existing:
            raise ValueError('New U-bearing counterpart absent from complete U recovery: '+r['id'])
        if r['id'] in existing:
            overlap.append({'id':r['id'],'prior_tokens':existing[r['id']]['tokens'],
                            'counterpart_tokens':r['tokens'],
                            'exact_match':existing[r['id']]['tokens']==r['tokens']})
    crosscheck_results = []
    line_by_id = {r['id']:r for r in counterpart_lines}
    for r in crosscheck['rows']:
        ident = key(r['reference'],r['side'],r['line'])
        crosscheck_results.append({'id':ident,'independent_tokens':r['tokens'],
            'recovered_tokens':line_by_id.get(ident,{}).get('tokens'),
            'exact_match':line_by_id.get(ident,{}).get('tokens')==r['tokens']})
    prior_contexts = []
    for path in PILOTS:
        for old in normalize(json.loads((ROOT/path).read_text()),path):
            for c in old['contexts']:
                prior_contexts.append(dict(c,reference=old['reference'],prior_ledger=path))
    for c in json.loads((ROOT/REVIEW).read_text())['contexts']:
        prior_contexts.append(dict(c,prior_ledger=REVIEW))
    prior_comparisons = []
    for c in prior_contexts:
        ident = key(c['reference'],str(c['side']),str(c['line']))
        if ident in line_by_id:
            prior_comparisons.append({'id':ident,'prior_ledger':c['prior_ledger'],
                'prior_tokens':c['tokens'],'new_tokens':line_by_id[ident]['tokens'],
                'exact_match':c['tokens']==line_by_id[ident]['tokens']})
    unique_lines = {r['id']:r for r in counterpart_lines+fields}
    if len(unique_lines)!=len(counterpart_lines)+len(fields):
        raise ValueError('Overlap between selected fields and counterpart lines')
    known = Counter(t.lstrip('*') for r in unique_lines.values() for t in r['tokens']
                    if t.lstrip('*') not in ('LOSS','UNKNOWN'))
    primary = {r['sign']:int(r['total']) for r in csv.DictReader((ROOT/'data/processed/mahadevan_1977_table_i.csv').open())}
    conflicts = {s:[n,primary[s]] for s,n in known.items() if n>primary[s]}
    if conflicts: raise ValueError('Recovered known tokens exceed primary total: '+str(conflicts))
    candidate = {r['source_reference']:r for r in read_jsonl(CANDIDATE)}
    byref = defaultdict(list)
    for r in unique_lines.values(): byref[r['reference']].append(r)
    export_comparisons = []
    for ref,lines in sorted(byref.items()):
        tokens = ['LOSS' if t['unknown_span'] else ('*' if t['doubtful'] else '')+t['sign']
                  for t in candidate[ref]['tokens']]
        export_comparisons.append({'reference':ref,'export_tokens':tokens,
            'exact_matching_line_ids':[r['id'] for r in lines if r['tokens']==tokens],
            'comparison_all_counterparts_accounted_for':reviews[ref]['all_counterpart_lines_accounted_for'],
            'all_recovered_lines_fully_identified':all(not r['has_reviewer_unknown'] for r in lines),
            'sequence_match_alone_establishes_export_line_identity':False})
    union_lines = {r['id']:dict(r,primary_review_scope='M328 concordance recovery') for r in all_lines}
    for r in counterpart_lines:
        if r['id'] in union_lines and r['tokens']!=union_lines[r['id']]['tokens']:
            raise ValueError('Conflicting transcription in combined primary context corpus: '+r['id'])
        union_lines[r['id']] = dict(r,primary_review_scope='counterpart of exact stroke+M328 field',
            primary_object_type_code=next(p['primary_object_type_code'] for p in pairs if p['reference']==r['reference']))
    union_counts = Counter(t.lstrip('*') for r in union_lines.values() for t in r['tokens']
                          if t.lstrip('*') not in ('LOSS','UNKNOWN'))
    union_conflicts = {s:[n,primary[s]] for s,n in union_counts.items() if n>primary[s]}
    if union_conflicts: raise ValueError('Combined primary contexts exceed Table I totals: '+str(union_conflicts))
    counts = Counter(t.lstrip('*') for r in counterpart_lines for t in r['tokens']
                     if t.lstrip('*') not in ('LOSS','UNKNOWN'))
    result = {'protocol':protocol,'references':len(reviews),'selected_field_lines':len(fields),
        'counterpart_lines':len(counterpart_lines),
        'references_accounted_for':sum(r.get('all_counterpart_lines_accounted_for') is True for r in reviews.values()),
        'eligible_references':sum(r['eligible'] for r in pairs),
        'eligible_field_lines':sum(len(r['field_line_ids']) for r in pairs if r['eligible']),
        'eligibility_by_type':{typ:{
            'references':sum(r['primary_object_type_code']==typ for r in pairs),
            'eligible_references':sum(r['primary_object_type_code']==typ and r['eligible'] for r in pairs),
            'eligible_field_lines':sum(len(r['field_line_ids']) for r in pairs if r['primary_object_type_code']==typ and r['eligible'])}
            for typ in sorted({r['primary_object_type_code'] for r in pairs})},
        'excluded_references':[r['reference'] for r in pairs if not r['eligible']],
        'adopted_historical_context_corrections':corrections['rows'],
        'corrected_U_context_sign_counts':dict(sorted(Counter(t.lstrip('*') for r in all_lines for t in r['tokens'] if t.lstrip('*') not in ('LOSS','UNKNOWN')).items())),
        'existing_U_line_crosschecks':overlap,
        'independent_parent_crosschecks':crosscheck_results,
        'prior_context_comparisons':prior_comparisons,
        'candidate_sequence_comparisons':export_comparisons,
        'known_counterpart_sign_counts':dict(sorted(counts.items())),
        'known_signs_in_fields_and_counterparts':len(known),
        'combined_primary_context_lines':len(union_lines),
        'combined_primary_context_known_tokens':sum(union_counts.values()),
        'combined_primary_context_known_sign_counts':dict(sorted(union_counts.items())),
        'combined_primary_context_known_types':len(union_counts),
        'counterpart_lines_with_loss':sum(r['has_primary_loss'] for r in counterpart_lines),
        'counterpart_lines_with_doubt':sum(r['has_primary_doubt'] for r in counterpart_lines),
        'counterpart_lines_with_unknown':sum(r['has_reviewer_unknown'] for r in counterpart_lines),
        'type_stratified_groups':groups,'type_pooled_groups':pooled,
        'type_stratified_variable_groups':sum(g['distinct_stroke_states']>1 for g in groups),
        'type_stratified_minimum_reference_exceptions':sum(g['minimum_reference_exceptions_to_single_valued_map'] for g in groups),
        'distinct_type_context_layout_stroke_combinations':sum(g['distinct_stroke_states'] for g in groups),
        'interpretation':'Variable exact context groups contradict only a single-valued map from their included inputs to graphic stroke states. Quantity and arbitrary category labels remain observationally interchangeable without external anchors.',
        'verified_evidence_files':verified,
        'inputs':{p:sha256(ROOT/p) for p in LEDGERS+PILOTS+REVIEWS+[PROTOCOL,FIELDS,CANDIDATE,CROSSCHECK,REVIEW,CORRECTIONS]}}
    write_jsonl('data/processed/m77_u_counterpart_lines.jsonl',counterpart_lines)
    write_jsonl('data/processed/m77_u_counterpart_pairs.jsonl',pairs)
    write_jsonl('data/processed/m77_primary_reviewed_contexts.jsonl',[union_lines[k] for k in sorted(union_lines)])
    write_json('results/m77_u_counterparts.json',result)
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(list,dict))},indent=2))


if __name__=='__main__':main()
