"""Explore a photographed crossed field without silently flattening its grammar."""
import json
from collections import Counter
from itertools import combinations
from common import ROOT, read_jsonl, sha256, write_json, write_jsonl


def compare_deletions(tokens, records, excluded_reference):
    comparisons = []
    for row in records:
        if row['source_reference'] == excluded_reference:
            continue
        if not row['tokens'] or any(t['doubtful'] or t['unknown_span'] or t['sign'] is None for t in row['tokens']):
            continue
        comparisons.append((row, [t['sign'] for t in row['tokens']]))
    def info(row, seq):
        return {'reference': row['source_reference'], 'tokens': seq,
                'source_document_count': row['source_doc_count'],
                'source_direction_code': row['source_direction_code'],
                'source_object_code': row['source_object_code']}
    results = []
    for start in range(len(tokens)-1):
        shortened = tokens[:start]+tokens[start+2:]
        exact, near = [], []
        for row, seq in comparisons:
            if len(seq) != len(shortened):
                continue
            differing = [j for j, (a,b) in enumerate(zip(shortened,seq)) if a != b]
            if not differing:
                exact.append(info(row, seq))
            elif len(differing) == 1:
                near.append(dict(info(row,seq), differing_index=differing[0]))
        results.append({'removed_indices': [start,start+1], 'removed_tokens': tokens[start:start+2],
                        'projected_tokens': shortened, 'exact_matches': exact,
                        'one_token_difference_matches': near})
    full = [info(row,seq) for row,seq in comparisons if seq == tokens]
    return {'comparison_records': len(comparisons),
            'comparison_unique_strings': len({tuple(s) for _,s in comparisons}),
            'comparison_multi_document_records': sum(r['source_doc_count']>1 for r,_ in comparisons),
            'full_original_string_matches': full, 'deletions': results}


def main():
    protocol_path = ROOT/'data/processed/c40_layout_protocol.json'
    protocol = json.loads(protocol_path.read_text())
    source_path = ROOT/'data/processed/m77_candidate_records.jsonl'
    records = read_jsonl(source_path)
    selected = [r for r in records if r['source_reference'] == protocol['reference']]
    assert len(selected) == 1
    tokens = [t['sign'] for t in selected[0]['tokens']]
    assert tokens == protocol['normalized_tokens']
    assert not any(t['doubtful'] or t['unknown_span'] for t in selected[0]['tokens'])
    result = compare_deletions(tokens, records, protocol['reference'])
    review_paths = [ROOT/'data/processed'/f'c40_{name}_review.json' for name in ('catalogue','photo','original')]
    reviews = [json.loads(p.read_text()) for p in review_paths]
    for review in reviews:
        for pin in review['evidence_files']:
            p = ROOT/pin['path']
            assert p.stat().st_size == pin['bytes'] and sha256(p) == pin['sha256'], pin['path']
    catalogue = reviews[0]
    first = next(r for r in catalogue['lines'] if r['side'] == 1)
    assert first['tokens'] == tokens and first['doubtful_token_indices'] == []
    assert {r['line_id'] for r in catalogue['lines']} == {'6306.1.0','6306.2.0'}
    for row in catalogue['lines']:
        assert [t['code'] for t in row['token_details']] == row['tokens']
        assert [i for i,t in enumerate(row['token_details']) if t['doubtful']] == row['doubtful_token_indices']
    counts = {}
    occurrences = catalogue['selected_arch_occurrences']
    assert len({(r['sign'],r['reference'],r['side'],r['line'],r['token_index']) for r in occurrences}) == len(occurrences)
    for sign in ('M312','M313','M314'):
        selected_occurrences = [r for r in occurrences if r['sign'] == sign]
        positions = Counter()
        for row in selected_occurrences:
            i, seq = row['token_index'], row['tokens']
            assert seq[i] == sign
            position = 'solus' if len(seq)==1 else 'initial' if i==0 else 'final' if i==len(seq)-1 else 'medial'
            assert position == row['position_class']
            positions[position] += 1
        counts[sign] = {k:positions[k] for k in ('solus','initial','medial','final')}
        counts[sign]['total'] = len(selected_occurrences)
        assert counts[sign] == catalogue['table_i_verified'][sign]
    result['selected_arch_primary_counts'] = counts
    shared = []
    for left, right in combinations(occurrences,2):
        if left['sign'] == right['sign'] or left['token_index'] != right['token_index']:
            continue
        def frame(row):
            return row['tokens'][:row['token_index']]+['?']+row['tokens'][row['token_index']+1:]
        if frame(left) == frame(right):
            shared.append({'frame':frame(left),
                           'signs':[left['sign'],right['sign']],
                           'references':[left['reference'],right['reference']],
                           'both_complete_fields_clear':not(left['doubtful_token_indices'] or right['doubtful_token_indices'] or left['has_loss'] or right['has_loss'])})
    result['selected_arch_shared_contexts'] = shared
    result['selected_arch_occurrences'] = occurrences
    result['primary_c40_lines'] = catalogue['lines']
    result['new_recovered_c40_fields'] = sum(r['recovered_from_primary_this_review'] for r in catalogue['lines'])
    result['new_independent_mass_observations'] = 0
    write_jsonl('data/processed/c40_primary_lines.jsonl', catalogue['lines'])
    result['protocol'] = protocol
    for row in result['deletions']:
        row['source_motivated_projection'] = row['removed_indices'] == protocol['candidate_separate_group_token_indices']
    result['input_sha256'] = {str(p.relative_to(ROOT)): sha256(p) for p in (protocol_path,source_path,*review_paths)}
    result['established_semantic_values'] = 0
    result['established_phonetic_values'] = 0
    write_json('results/c40_layout_audit.json', result)
    print(json.dumps({
        'comparison_records':result['comparison_records'],
        'full_matches':len(result['full_original_string_matches']),
        'deletions':[{'indices':r['removed_indices'], 'exact':len(r['exact_matches']),
                      'one_difference':len(r['one_token_difference_matches'])} for r in result['deletions']]},indent=2))


if __name__ == '__main__':
    main()
