"""Join primary object metadata to the complete M328 recovery, descriptively.

No reference-range inference, semantic fitting or independent-trial p-values.
First-line direction is deliberately not copied onto other inscription lines.
"""
from collections import Counter
import json
import re
from common import ROOT, read_jsonl, sha256, write_json, write_jsonl
from analyze_m77_u_fields import simple_field, verify_fingerprints
from recover_m77_u_concordance import u_positions

LEDGERS = [f'data/processed/m77_u_types_{part}.json' for part in
           ('parent', 'structure', 'numerals', 'iconography')]
TYPES = {'1':'seal', '2':'sealing', '3':'miniature tablet', '4':'pottery graffiti',
         '5':'copper tablet', '6':'bronze implement', '7':'ivory/bone rod', '9':'miscellaneous'}
POSITIONS = ('solus', 'initial', 'medial', 'final')
PROTOCOL = 'data/processed/m77_u_type_protocol.json'
CORPUS = 'data/processed/m77_u_recovered_lines.jsonl'
CANDIDATE = 'data/processed/m77_candidate_records.jsonl'


def metadata_code(row):
    text = row['printed_metadata_code'].strip()
    # One review retained reference + metadata in the literal transcription.
    text = re.sub(r'^' + re.escape(str(row['reference'])) + r'\s+', '', text)
    code = re.sub(r'\s+', '', text)
    if not re.fullmatch(r'[1-79][0-9?]{5}', code):
        raise ValueError('Expected full six-digit first metadata code: '+text)
    if code[0] != row['object_type_code']:
        raise ValueError('Object type disagrees with literal metadata')
    if any(code[i] != str(row[key]) for i,key in ((1,'first_line_side'),(4,'first_line_line'))):
        raise ValueError('Side/line disagrees with literal metadata')
    return code


def collect_reviews(ledgers, targets):
    reviews = {}
    for path, doc in ledgers.items():
        for row in doc.get('rows', doc.get('records', [])):
            ref = str(row['reference'])
            if ref in reviews: raise ValueError('Duplicate reference '+ref)
            # An unresolved review is preserved, never filled from the candidate.
            verified = row.get('verified') is True
            code = metadata_code(row) if verified else None
            reviews[ref] = dict(row, reference=ref, review_ledger=path,
                                normalized_metadata_code=code,
                                object_type_code=code[0] if code else None)
    if set(reviews) != set(targets):
        raise ValueError('Primary review coverage differs from target reference set')
    return reviews


def join_lines(lines, reviews):
    return [dict(row, primary_object_type_code=reviews[row['reference']]['object_type_code'],
                 object_type_review_ledger=reviews[row['reference']]['review_ledger']) for row in lines]


def strict(row):
    return row['full_sequence_primary_checked'] and not any(row[k] for k in
           ('has_primary_loss','has_primary_doubt','has_reviewer_unknown'))


def summarize(lines):
    out = {}
    for code,label in TYPES.items():
        subset = [r for r in lines if r['primary_object_type_code']==code]
        positions = Counter()
        for row in subset: positions.update(u_positions(row['tokens']))
        fields = Counter(simple_field(r['tokens']) for r in subset
                         if strict(r) and simple_field(r['tokens']) is not None)
        out[code] = {'label':label, 'references':len({r['reference'] for r in subset}),
            'lines':len(subset), 'U_occurrences':sum(positions.values()),
            'U_positions':{p:positions[p] for p in POSITIONS},
            'distinct_full_strings':len({tuple(r['tokens']) for r in subset}),
            'exact_undoubted_stroke_U_lines':sum(fields.values()),
            'exact_undoubted_stroke_U_references':len({r['reference'] for r in subset
                if strict(r) and simple_field(r['tokens']) is not None}),
            'exact_undoubted_stroke_U_sides':dict(Counter(r['side'] for r in subset
                if strict(r) and simple_field(r['tokens']) is not None)),
            'exact_undoubted_stroke_U_by_graphic_count':dict(sorted(fields.items()))}
    return out


def main():
    docs = {p:json.loads((ROOT/p).read_text()) for p in LEDGERS}
    verified = {}
    for doc in docs.values(): verify_fingerprints(doc, verified)
    lines = read_jsonl(CORPUS)
    reviews = collect_reviews(docs, {r['reference'] for r in lines})
    # Every used evidence image must be tied to a recorded digest.
    for r in reviews.values():
        path = r['evidence_path']
        digest = r.get('image_sha256', r.get('evidence_sha256', verified.get(path)))
        if not digest or sha256(ROOT/path) != digest:
            raise ValueError('Missing or changed evidence digest: '+path)
        if path in verified and verified[path] != digest:
            raise ValueError('Conflicting evidence digest: '+path)
        verified[path] = digest
    joined = join_lines(lines, reviews)
    candidates = {r['source_reference']:r for r in read_jsonl(CANDIDATE)}
    comparisons = [{'reference':ref, 'primary_type':r['object_type_code'],
                    'candidate_type':candidates[ref]['source_object_code']}
                   for ref,r in sorted(reviews.items())]
    disagreements = [r for r in comparisons if r['primary_type'] is not None and
                     r['primary_type'] != r['candidate_type']]
    subsets = {'all_reviewed':joined,
               'loss_free':[r for r in joined if not r['has_primary_loss']],
               'fully_identified_undoubted_loss_free':[r for r in joined if strict(r)],
               'fully_identified_undoubted_two_sign':[r for r in joined if strict(r) and len(r['tokens'])==2]}
    length_two = subsets['fully_identified_undoubted_two_sign']
    patterns = []
    for code in TYPES:
        counts = Counter(tuple(r['tokens']) for r in length_two if r['primary_object_type_code']==code)
        for seq,n in sorted(counts.items()):
            patterns.append({'type':code,'tokens':list(seq),'line_count':n,
                'line_ids':[r['id'] for r in length_two if r['primary_object_type_code']==code and tuple(r['tokens'])==seq]})
    result = {'protocol':json.loads((ROOT/PROTOCOL).read_text()),
        'reviewed_references':len(reviews), 'verified_references':sum(r['verified'] is True for r in reviews.values()),
        'unverified_references':[ref for ref,r in reviews.items() if r['object_type_code'] is None],
        'type_reference_counts':dict(Counter(r['object_type_code'] for r in reviews.values())),
        'unclassified_line_ids':[r['id'] for r in joined if r['primary_object_type_code'] is None],
        'line_count':len(joined), 'candidate_disagreements':disagreements,
        'candidate_comparisons':comparisons,
        'summaries':{k:summarize(v) for k,v in subsets.items()},
        'strict_two_sign_patterns':patterns,
        'nonfinal_or_solitary_U_lines':[{'id':r['id'],'tokens':r['tokens'],
            'type':r['primary_object_type_code'],'positions':dict(u_positions(r['tokens']))}
            for r in joined if any(u_positions(r['tokens'])[p] for p in ('initial','medial','solus'))],
        'limitations':['Sign-selected census of the M77 M328 concordance, not the complete modern corpus.',
            'Reference counts are not proven independent objects, impressions or molds.',
            'No missing Table IV page was recovered; distribution reconstructed from Texts.',
            'No object type or sequence alone establishes words, sounds, numerical values or language.',
            'No first-line direction was propagated; all drawings remain in normalized order.'],
        'verified_evidence_files':verified,
        'inputs':{p:sha256(ROOT/p) for p in LEDGERS+[PROTOCOL,CORPUS,CANDIDATE]}}
    write_jsonl('data/processed/m77_u_typed_lines.jsonl', joined)
    write_jsonl('data/processed/m77_u_primary_types.jsonl', [reviews[k] for k in sorted(reviews)])
    write_json('results/m77_u_object_types.json', result)
    print(json.dumps({k:result[k] for k in ('reviewed_references','verified_references','type_reference_counts','candidate_disagreements')}, indent=2))
    print(json.dumps(result['summaries'],indent=2))


if __name__ == '__main__': main()
