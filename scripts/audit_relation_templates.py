"""Explore relation-marker placement without assigning names or meanings.

Prefix/suffix parses enumerate every boundary; alternatives for one string are
mutually exclusive hypotheses, NOT independently observed relations.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path

from analyze_m77_foreign import DOMESTIC_RANGES, NAMED_OTHER, eligible, sequence

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ("prefix", "internal", "suffix")


def parse_strings(strings, marker, template):
    if template not in TEMPLATES:
        raise ValueError(template)
    parses = []
    for seq, refs in sorted(strings.items()):
        if seq.count(marker) != 1 or len(seq) < 3:
            continue
        i = seq.index(marker)
        if template == "internal":
            splits = [(seq[:i], seq[i+1:])] if 0 < i < len(seq)-1 else []
        elif template == "prefix":
            body = seq[1:]
            splits = [(body[:k], body[k:]) for k in range(1, len(body))] if i == 0 else []
        else:
            body = seq[:-1]
            splits = [(body[:k], body[k:]) for k in range(1, len(body))] if i == len(seq)-1 else []
        for left, right in splits:
            parses.append({"sequence": list(seq), "references": sorted(refs),
                           "left": list(left), "right": list(right)})
    return parses


def chain_witnesses(parses):
    by_left = defaultdict(list)
    for p in parses:
        by_left[tuple(p["left"])].append(p)
    return [{"first": a, "second": b, "shared_bundle": a["right"]}
            for a in parses for b in by_left[tuple(a["right"])]
            if a["sequence"] != b["sequence"]]


def summarize(strings, marker, template):
    parses = parse_strings(strings, marker, template)
    witnesses = chain_witnesses(parses)
    per_string = defaultdict(int)
    for p in parses:
        per_string[tuple(p["sequence"])] += 1
    pairs = {(tuple(w["first"]["sequence"]), tuple(w["second"]["sequence"]))
             for w in witnesses}
    return {"marker": marker, "template": template,
            "eligible_unique_strings": len(per_string),
            "alternative_parses": len(parses),
            "strings_with_multiple_boundaries": sum(n > 1 for n in per_string.values()),
            "parse_witnesses": len(witnesses), "distinct_ordered_string_pairs": len(pairs),
            "witnesses": witnesses}


def main():
    corpus_path = ROOT / 'data/processed/m77_candidate_records.jsonl'
    rows = [json.loads(s) for s in corpus_path.read_text().splitlines()]
    strings = defaultdict(list)
    for row in rows:
        ref = row['source_reference']
        if not eligible(row) and (ref in NAMED_OTHER or any(
                lo <= int(ref) <= hi for lo, hi in DOMESTIC_RANGES)):
            strings[sequence(row)].append(ref)
    controls = [summarize(strings, f'M{i:03d}', t)
                for i in range(1, 418) for t in TEMPLATES]
    main_results = [x for x in controls if x['marker'] == 'M001']
    compact = lambda x: {k: v for k, v in x.items() if k != 'witnesses'}
    result = {
        'status': 'Exploratory exhaustive placement/boundary screen; no semantic identification',
        'protocol': {
            'marker_count': 'Exactly one marker; no allograph merging',
            'templates': {'prefix': 'D A B', 'internal': 'A D B', 'suffix': 'A B D'},
            'endpoint_boundaries': 'Every split into two nonempty contiguous bundles',
            'matching': 'Entire right bundle equals entire left bundle of a different complete string',
            'deduplication': 'Identical complete strings collapsed before parsing',
            'scope': 'Previously filtered domestic candidate seals, same as internal-only audit',
            'warnings': [
                'Alternative boundaries for one string are not simultaneous observations',
                'Witness pairs do not establish globally consistent parses of all inscriptions',
                'Same-template counts exclude hypotheses mixing marker placement',
                'All-sign search has no calibrated p-value or independent semantic labels',
                'Reversing all strings swaps prefix/suffix and chain direction; total counts cannot infer reading direction',
                'Zero witnesses do not refute kinship; actual related persons may be absent',
                'Candidate transcription is not a full primary-source corpus']},
        'samples': {'records': sum(map(len, strings.values())), 'unique_strings': len(strings)},
        'target_M001': main_results,
        'target_M001_eligible_parses': {t: parse_strings(strings, 'M001', t) for t in TEMPLATES},
        'control_summary': {t: {
            'markers_with_eligible_strings': sum(x['eligible_unique_strings'] > 0 for x in controls if x['template'] == t),
            'markers_with_witnesses': sum(x['parse_witnesses'] > 0 for x in controls if x['template'] == t),
            'parse_witnesses': sum(x['parse_witnesses'] for x in controls if x['template'] == t),
            'distinct_ordered_pairs_summed_by_marker': sum(x['distinct_ordered_string_pairs'] for x in controls if x['template'] == t)
        } for t in TEMPLATES},
        'all_417_controls': controls,
        'input_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
            'data/processed/m77_candidate_records.jsonl', 'scripts/analyze_m77_foreign.py',
            'data/raw/hybrid_vidale_2005.pdf', 'results/patronymic_chain_audit.json']}}
    (ROOT/'results/relation_template_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'samples': result['samples'], 'M001': list(map(compact, main_results)),
                      'controls': result['control_summary']}, indent=2))


if __name__ == '__main__':
    main()
