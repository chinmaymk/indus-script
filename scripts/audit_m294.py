"""Audit literal parallels for the clipped seal M-294; no decipherment assumed."""
import csv
import json
from collections import Counter
from common import ROOT, sha256, read_jsonl, write_json

FIELDS = ('id', 'cisi', 'site', 'excavation-idno', 'area-section', 'block-house',
          'room-grid', 'depth', 'type', 'preservation', 'complete', 'condition',
          'dir.', 'text', 'symbol')


def classify(sequence, target, direction):
    """Keep physical file order separate from inferred reading order."""
    n = len(target)
    matches = []
    for i in range(len(sequence)-n+1):
        if sequence[i:i+n] != target:
            continue
        left, right = sequence[:i], sequence[i+n:]
        matches.append({'file_left': left, 'file_right': right,
                        'exact': not left and not right,
                        'reading_prefix_extension_if_reported_RL':
                            bool(right) if direction == 'R/L' else None,
                        'reading_suffix_extension_if_reported_RL':
                            bool(left) if direction == 'R/L' else None})
    return matches


def main():
    inputs = ['data/processed/m294_protocol.json', 'data/raw/lipi_inscriptions.csv',
              'data/processed/lipi_strict.jsonl']
    protocol = json.loads((ROOT/inputs[0]).read_text())
    with (ROOT/inputs[1]).open() as f:
        rows = [{k:r.get(k, '') for k in FIELDS} for r in csv.DictReader(f)]
    byid = {r['id']:r for r in rows}
    strict = read_jsonl(inputs[2])
    results = []
    for target in protocol['literal_file_order_targets']:
        hits = []
        for r in strict:
            raw = byid[r['id']]
            for match in classify(r['sequence'], target, raw['dir.']):
                hits.append(dict(raw, sequence=r['sequence'], **match))
        results.append({'target':target, 'exact_rows':sum(h['exact'] for h in hits),
                        'longer_rows':sum(not h['exact'] for h in hits),
                        'distinct_strings':len({tuple(h['sequence']) for h in hits}),
                        'conditions':dict(Counter(h['condition'] for h in hits)),
                        'hits':hits})
    reviews = {}
    for label in ('primary', 'completeness', 'room_context'):
        p = f'data/processed/m294_{label}_review.json'
        review = json.loads((ROOT/p).read_text())
        for pin in review.get('evidence_files', []):
            file = ROOT/pin['path']
            assert file.stat().st_size == pin['bytes'] and sha256(file) == pin['sha256'], pin['path']
        reviews[label] = review
        inputs.append(p)
    output = {'protocol':protocol, 'named_rows':{c:byid[i] for c,i in protocol['named_rows'].items()},
              'strict_rows_searched':len(strict), 'comparisons':results, 'reviews':reviews,
              'input_sha256':{p:sha256(ROOT/p) for p in inputs},
              'established_semantic_values':0, 'established_phonetic_values':0}
    write_json('results/m294_audit.json', output)
    print(json.dumps([{k:v for k,v in r.items() if k != 'hits'} for r in results], indent=2))


if __name__ == '__main__':
    main()
