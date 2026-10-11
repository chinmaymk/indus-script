"""Audit selected primary U contexts and exact main/auxiliary contrasts.

Graphic counts are observations, never assigned numerical values. Concordance
pages are sorted and selected: these outputs are not population estimates.
"""
from collections import Counter, defaultdict
import json
import re
from common import ROOT, sha256, write_json, write_jsonl, read_jsonl

STROKES = {'M086': 1, 'M087': 2, 'M089': 3, 'M095': 4}
PILOTS = ['data/processed/m77_u_pilot_numerals.json',
          'data/processed/m77_u_pilot_structure.json',
          'data/processed/m77_u_pilot_parent.json']
REVIEW = 'data/processed/m77_u_paired_context_review.json'
COUNTEREXAMPLES = 'data/processed/m77_u_counterexamples.json'


def clean(sequence):
    return bool(sequence) and all(re.fullmatch(r'M\d{3}', t) and 1 <= int(t[1:]) <= 417
                                  for t in sequence)


def simple_field(sequence):
    """Return the observed count only for an exact, undoubted two-sign line."""
    if len(sequence) == 2 and sequence[0] in STROKES and sequence[1] == 'M328':
        return STROKES[sequence[0]]
    return None


def group_contexts(pairs):
    """Group exact contexts, excluding uncertainty and repeated same-line input.

    Multiple observations of one reference/side/line cannot inflate support.
    Conflicting observations are an error rather than new evidence.
    """
    unique = {}
    for p in pairs:
        if not clean(p['main']) or simple_field(p['field']) is None:
            continue
        key = (str(p['reference']), str(p['field_side']), str(p['field_line']),
               str(p['main_side']), str(p['main_line']))
        if key in unique and (unique[key]['main'], unique[key]['field']) != (p['main'], p['field']):
            raise ValueError('Conflicting transcription for the same paired lines')
        unique[key] = p
    groups = defaultdict(list)
    for p in unique.values():
        groups[tuple(p['main'])].append(p)
    return [{'main': list(main), 'observed_stroke_counts': sorted({simple_field(p['field']) for p in ps}),
             'reference_count': len({p['reference'] for p in ps}),
             'references_are_not_proved_independent_objects': True,
             'witnesses': sorted(ps, key=lambda p: (p['reference'], str(p['field_side'])))}
            for main, ps in sorted(groups.items())]


def verify_fingerprints(node, verified):
    if isinstance(node, dict):
        if 'path' in node and 'sha256' in node:
            path = node['path']
            if path in verified and verified[path] != node['sha256']:
                raise ValueError('Inconsistent fingerprint: '+path)
            if path not in verified and sha256(ROOT/path) != node['sha256']:
                raise ValueError('Source changed: '+path)
            verified[path] = node['sha256']
        for v in node.values():
            verify_fingerprints(v, verified)
    elif isinstance(node, list):
        for v in node:
            verify_fingerprints(v, verified)


def normalize(ledger, path):
    rows = []
    for r in ledger.get('rows', ledger.get('records', [])):
        if 'tokens' in r:
            tokens = r['tokens']
            contexts = r.get('other_side_lines', [])
        else:
            tokens = [('LOSS' if t['unknown_span'] else
                       ('*' if t['doubtful'] else '')+t['sign']) for t in r['sequence']]
            contexts = [{'side': c['side_code'], 'line': c['line_code'],
                         'tokens': [('LOSS' if t['unknown_span'] else
                                     ('*' if t['doubtful'] else '')+t['sign'])
                                    for t in c['sequence']]}
                        for c in r.get('other_side_context', [])]
        index = r.get('indexed_M328_token_index_zero_based')
        if index is None:
            # Other pilot sections have exactly one U per indexed line.
            if sum(t.lstrip('*') == 'M328' for t in tokens) != 1:
                raise ValueError('Repeated U requires an explicit indexed position')
            index = next(i for i,t in enumerate(tokens) if t.lstrip('*') == 'M328')
        if not 0 <= index < len(tokens) or tokens[index].lstrip('*') != 'M328':
            raise ValueError('Invalid indexed position')
        rows.append({'reference': str(r['reference']),
                     'side': str(r.get('side', r.get('side_code'))),
                     'line': str(r.get('line', r.get('line_code'))),
                     'pdf_page': r['pdf_page'], 'printed_page': r['printed_page'],
                     'tokens': tokens, 'indexed_U_position': index,
                     'has_loss': 'LOSS' in tokens,
                     'has_reviewer_unknown': 'UNKNOWN' in tokens,
                     'has_doubt': any(t.startswith('*') for t in tokens),
                     'exact_simple_field_graphic_count': simple_field(tokens),
                     'contexts': contexts,
                     'full_sequence_primary_checked': r.get('full_sequence_primary_checked', True),
                     'ledger': path})
    return rows


def main():
    verified = {}; rows = []
    for path in PILOTS:
        ledger = json.loads((ROOT/path).read_text())
        verify_fingerprints(ledger, verified)
        rows.extend(normalize(ledger, path))
    indexed_keys = [(r['reference'], r['side'], r['line'], r['indexed_U_position']) for r in rows]
    if len(set(indexed_keys)) != len(indexed_keys):
        raise ValueError('Duplicate indexed occurrence across pilot ledgers')
    review = json.loads((ROOT/REVIEW).read_text())
    verify_fingerprints(review, verified)
    counterexamples = json.loads((ROOT/COUNTEREXAMPLES).read_text())
    verify_fingerprints(counterexamples, verified)
    # Supplemental cases are retained separately from the nine-page denominator.
    fields = rows + review.get('supplemental_fields', [])
    reviewed = defaultdict(list)
    for c in review['contexts']:
        reviewed[c['reference']].append(c)
    pairs = []
    for r in fields:
        if simple_field(r['tokens']) is None:
            continue
        contexts = list(r.get('contexts', [])) + reviewed[r['reference']]
        for c in contexts:
            if str(c['side']) == str(r['side']) and str(c['line']) == str(r['line']):
                continue
            pairs.append({'reference': r['reference'], 'main': c['tokens'], 'field': r['tokens'],
                          'main_side': str(c['side']), 'main_line': str(c['line']),
                          'field_side': str(r['side']), 'field_line': str(r['line']),
                          'pdf_page': r['pdf_page'], 'source': r.get('ledger', REVIEW)})
    groups = group_contexts(pairs)
    contrasts = [g for g in groups if len(g['observed_stroke_counts']) > 1]

    # Discovery-only comparison to one digital sequence per reference. Never
    # treat that sequence as a main side when it is the indexed field itself.
    candidate = {r['source_reference']: r for r in read_jsonl('data/processed/m77_candidate_records.jsonl')}
    candidate_groups = defaultdict(list); retained_fields = []
    for r in rows:
        if simple_field(r['tokens']) is None:
            continue
        c = candidate[r['reference']]
        seq = [('LOSS' if t['unknown_span'] else ('*' if t['doubtful'] else '')+t['sign']) for t in c['tokens']]
        if seq == r['tokens']:
            retained_fields.append(r['reference'])
            continue
        if clean(seq):
            candidate_groups[tuple(seq)].append({'reference':r['reference'], 'field':r['tokens'],
                                                'graphic_count':simple_field(r['tokens']), 'pdf_page':r['pdf_page']})
    discovered = [{'candidate_main':list(k),'observed_stroke_counts': sorted({r['graphic_count'] for r in v}),
                   'witnesses':v} for k,v in sorted(candidate_groups.items())
                  if len({r['graphic_count'] for r in v}) > 1]
    summary = {
        'indexed_groups':len(rows), 'pages':sorted({r['pdf_page'] for r in rows}),
        'groups_by_page':dict(sorted(Counter(r['pdf_page'] for r in rows).items())),
        'all_U_instances_in_indexed_lines':sum(sum(t.lstrip('*')=='M328' for t in r['tokens']) for r in rows),
        'lines_with_primary_loss':sum(r['has_loss'] for r in rows),
        'lines_with_primary_doubt':sum(r['has_doubt'] for r in rows),
        'lines_with_reviewer_unknown':sum(r['has_reviewer_unknown'] for r in rows),
        'undoubted_exact_simple_fields':sum(simple_field(r['tokens']) is not None for r in rows),
        'simple_fields_by_graphic_count':dict(sorted(Counter(simple_field(r['tokens']) for r in rows if simple_field(r['tokens']) is not None).items())),
        'selected_primary_contrast_main_patterns':len(contrasts),
        'supplemental_fields_outside_pilot_denominator':len(review.get('supplemental_fields',[])),
        'candidate_export_already_contains_indexed_simple_field_references':sorted(set(retained_fields)),
        'new_established_semantic_or_phonetic_readings':0}
    write_jsonl('data/processed/m77_u_pilot_normalized.jsonl', rows)
    write_json('results/m77_u_field_analysis.json', {
        'summary':summary,
        'input_sha256': {p:sha256(ROOT/p) for p in PILOTS+[REVIEW,COUNTEREXAMPLES,'data/processed/m77_candidate_records.jsonl']},
        'verified_source_fingerprints': verified, 'primary_context_groups':groups,
        'primary_contrasts':contrasts, 'candidate_export_discovery_groups':discovered,
        'proof':review['proof'], 'countermodels':review['countermodels'],
        'original_metadata_review':review.get('original_metadata_review', []),
        'counterexample_ledger':COUNTEREXAMPLES,
        'limits':review['limits']+[
            'Concordance sorting clusters contexts; no random-sample prevalence or p-value is warranted.',
            'Selected other-side transcriptions are incomplete; no claim that all matched patterns have been found.',
            'Secondary export joins remain discovery-only unless separately visually authenticated.',
            'M328 also occurs solus, initially and medially. This two-sign field is not its universal syntax.',
            'Primary recovery is from normalized catalogue drawings, not independent autopsy of artifacts.']})
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
