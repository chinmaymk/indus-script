"""Exact full-context substitutions for two catalogue stroke forms.

This is descriptive structural evidence, not an assignment of numerical values.
"""
from collections import defaultdict
import json
from common import ROOT, sha256, write_json
from analyze_m77_foreign import eligible, sequence
from audit_chain_segments import domestic, positions

TARGETS = ('M102', 'M106')
ANCHOR = ('M287', 'M342')
INVENTORY = tuple(f'M{i:03d}' for i in range(1, 418))


def frame_index(strings):
    frames = defaultdict(dict)
    for seq, refs in sorted(strings.items()):
        if not seq or '?' in seq:
            raise ValueError('Nonempty literal strings required')
        for i, sign in enumerate(seq):
            frame = seq[:i] + ('?',) + seq[i+1:]
            frames[frame][sign] = {'sequence': list(seq), 'references': sorted(refs)}
    return frames


def frame_row(frame, members):
    i = frame.index('?')
    return {'frame': list(frame), 'slot_index': i, 'length': len(frame),
            'slot_followed_by_anchor': frame[i+1:i+3] == ANCHOR,
            'anchor_at_end': frame[i+1:] == ANCHOR,
            'members': members}


def analyze(strings):
    frames = frame_index(strings)
    shared = [frame_row(f, m) for f, m in sorted(frames.items())
              if all(t in m for t in TARGETS)]
    target_frames = [frame_row(f, m) for f, m in sorted(frames.items())
                     if any(t in m for t in TARGETS)]
    occurrences = []
    for seq, refs in sorted(strings.items()):
        for i in positions(seq, ANCHOR):
            occurrences.append({'sequence': list(seq), 'references': sorted(refs),
                                'anchor_start_index': i,
                                'predecessor': seq[i-1] if i else 'BOS',
                                'anchor_at_end': i+len(ANCHOR) == len(seq)})
    signs = []
    for sign in INVENTORY:
        observed = [s for s in strings if sign in s]
        anchor_rows = [o for o in occurrences if o['predecessor'] == sign]
        signs.append({'sign': sign, 'complete_strings': len(observed),
                      'shared_full_frames_with': {
                          t: [r['frame'] for r in target_frames
                              if sign != t and sign in r['members'] and t in r['members']]
                          for t in TARGETS},
                      'before_anchor_occurrences': len(anchor_rows),
                      'before_final_anchor_occurrences': sum(o['anchor_at_end'] for o in anchor_rows),
                      'before_anchor_unique_strings': len({tuple(o['sequence']) for o in anchor_rows}),
                      'before_anchor_references': sorted({ref for o in anchor_rows for ref in o['references']})})
    return {'samples': {'records': sum(map(len, strings.values())), 'unique_strings': len(strings)},
            'targets': TARGETS, 'anchor': ANCHOR,
            'shared_full_frames': shared,
            'shared_frame_counts': {'all': len(shared),
                                    'minimum_length_3': sum(r['length'] >= 3 for r in shared),
                                    'minimum_length_4': sum(r['length'] >= 4 for r in shared),
                                    'followed_by_anchor': sum(r['slot_followed_by_anchor'] for r in shared)},
            'all_target_bearing_frames': target_frames,
            'anchor_occurrences': occurrences,
            'anchor_at_beginning_occurrences': sum(o['predecessor']=='BOS' for o in occurrences),
            'all_417_sign_comparisons': signs}


def main():
    source = 'data/processed/m77_candidate_records.jsonl'
    rows = [json.loads(line) for line in (ROOT/source).read_text().splitlines()]
    strings = defaultdict(list)
    excluded = []
    for row in rows:
        seq = sequence(row)
        reasons = eligible(row) + ([] if domestic(row) else ['not_named_domestic'])
        if not reasons:
            strings[seq].append(row['source_reference'])
        elif any(seq[i] in TARGETS and seq[i+1:i+3] == ANCHOR for i in range(len(seq))):
            excluded.append({'reference': row['source_reference'], 'diplomatic': row['diplomatic'],
                             'exclusions': reasons})
    result = analyze(strings)
    result['excluded_target_anchor_records'] = excluded
    primary_path = 'data/processed/stroke_curve_primary_review.json'
    primary = json.loads((ROOT/primary_path).read_text())
    for item in primary['evidence_files']:
        p = ROOT/item['path']
        assert p.stat().st_size == item['bytes'] and sha256(p) == item['sha256'], item['path']
    byref = {r['source_reference']: r for r in rows}
    for checked in primary['rows']:
        assert list(sequence(byref[checked['reference']])) == checked['tokens']
        assert not eligible(byref[checked['reference']])
    for checked in primary.get('doubtful_rows', []):
        assert list(sequence(byref[checked['reference']])) == checked['tokens']
        assert 'doubt' in eligible(byref[checked['reference']])
    independent_path = 'results/stroke_substitution_independent_review.json'
    independent = json.loads((ROOT/independent_path).read_text())
    for p, expected in independent['input_sha256'].items():
        assert sha256(ROOT/p) == expected, p
    assert independent['sample']['records'] == result['samples']['records']
    assert independent['sample']['unique_strings'] == result['samples']['unique_strings']
    observed_frames = {tuple(r['frame']): r['members'] for r in result['shared_full_frames']}
    reference_frames = {tuple(r['frame']): {m['sign']: {
        'sequence': m['sequence'], 'references': m['references']} for m in r['occupants']}
        for r in independent['target_exact_frames_with_all_occupants']}
    assert observed_frames == reference_frames
    assert result['shared_frame_counts']['followed_by_anchor'] == len(independent['target_pairs_followed_by_M287_M342'])
    result['primary_review'] = {'path': primary_path, 'rows_checked': len(primary['rows']),
                                 'doubtful_rows_checked': len(primary.get('doubtful_rows', [])),
                                 'evidence_files_checked': len(primary['evidence_files'])}
    result['independent_algorithm_agreement'] = True
    inputs = [source, 'data/processed/stroke_substitution_protocol.json',
              'scripts/analyze_m77_foreign.py', 'scripts/audit_chain_segments.py',
              primary_path, independent_path, 'scripts/verify_stroke_substitutions_independent.py']
    result['input_sha256'] = {p: sha256(ROOT/p) for p in inputs}
    result['limits'] = [
        'Exploratory selected corpus; no significance or representative-population claim',
        'Exact slot matches do not establish equivalence, a numerical scale, units or language',
        'Common local continuations with different prefixes are not complete-string substitutions',
        'Absence of exact counterparts is not evidence that numerical readings are impossible',
        'Catalogue stroke counts are visual descriptions, not assigned numerical values',
    ]
    result['new_semantic_values'] = result['new_phonetic_values'] = 0
    write_json('results/stroke_substitution_audit.json', result)
    print(json.dumps({'samples': result['samples'], 'shared_frame_counts': result['shared_frame_counts'],
                      'anchor_predecessors': [r for r in result['all_417_sign_comparisons']
                                               if r['before_anchor_occurrences']]}, indent=2))


if __name__ == '__main__':
    main()
