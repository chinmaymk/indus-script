"""Conditional structural replication in source M IDs; no decipherment or W join."""
from collections import Counter, defaultdict
import json
from common import ROOT, sha256, write_json
from analyze_sequences import summarize, permutation_test


def main():
    path = 'data/processed/m77_candidate_strict.jsonl'
    rows = [json.loads(l) for l in (ROOT/path).read_text().splitlines()]
    sequences = sorted({tuple(r['sequence']) for r in rows})
    seals = sorted({tuple(r['sequence']) for r in rows if r['source_object_code'] == '1'})
    # Maximal adjacent runs of JUST the two shape-authenticated selected M signs.
    # No assertion of a common numeral field or of numeric values is made.
    witnesses = defaultdict(list)
    for r in rows:
        run = []
        for token in r['sequence'] + [None]:
            if token in ('M086', 'M099'):
                run.append(token)
            else:
                if len(set(run)) == 2:
                    witnesses[tuple(run)].append(r['source_reference'])
                run = []
    result = {
        'input_sha256': {path: sha256(ROOT/path)},
        'all_strict_unique': {'summary': summarize(sequences), 'permutations': permutation_test(sequences, 499)},
        'seal_only_unique': {'summary': summarize(seals), 'permutations': permutation_test(seals, 499)},
        'selected_stroke_run_witnesses': [{'sequence': list(s), 'source_references': refs} for s, refs in sorted(witnesses.items())],
        'scope': [
            'Every test uses whole-text deduplication; no tokens bridge line boundaries.',
            'The length-position null preserves each (length, slot) frequency exactly.',
            'Seal-only replication controls this source object code, not all archaeological confounds.',
            'Two complete lines, one damaged first line and one multiline-object first line checked against primary images; no corpus-wide transcription accuracy established.',
            'M77 and W datasets can describe the same physical objects: not independent archaeological evidence.',
            'Sign order dependence is not proof of language or of a particular linguistic family.',
            'Stroke runs do not establish numerical values or segmentation into numeral fields.',
        ]}
    write_json('results/m77_candidate_structure.json', result)
    print(json.dumps({k: {'summary': result[k]['summary'], 'length_position_mi': result[k]['permutations']['length_position']['mi']} for k in ('all_strict_unique', 'seal_only_unique')}, indent=2))


if __name__ == '__main__':
    main()
