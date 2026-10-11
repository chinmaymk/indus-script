"""Describe recorded field codes without conflating lines, sides and references."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def profile(corpus):
    if (corpus.get('schema_version') != 'verified-m77-1'
            or corpus.get('coverage_complete_for_manifest') is not True
            or corpus.get('unresolved_rows') != 0):
        raise ValueError('Requires complete verified corpus')
    seen, sides, references = set(), {}, defaultdict(set)
    line_counts, object_types = Counter(), defaultdict(set)
    for row in corpus['rows']:
        key = tuple(row[k] for k in ('reference', 'side', 'line'))
        if key in seen:
            raise ValueError('Duplicate row key')
        seen.add(key)
        code = row['field_symbol_code']
        if not isinstance(code, str) or not re.fullmatch(r'[0-9]{2}', code):
            raise ValueError('Invalid field code')
        side = key[:2]
        if side in sides and sides[side] != code:
            raise ValueError('Conflicting field codes on one recorded side')
        sides[side] = code
        references[key[0]].add(code)
        object_types[key[0]].add(row['object_type_code'])
        line_counts[code] += 1
    if any(len(types) != 1 for types in object_types.values()):
        raise ValueError('Conflicting object types for one reference')
    return {
        'counts': {'lines': len(seen), 'represented_sides': len(sides),
                   'references': len(references)},
        'line_field_code_counts': dict(sorted(line_counts.items())),
        'side_field_code_counts': dict(sorted(Counter(sides.values()).items())),
        'reference_field_code_incidence_overlapping': dict(sorted(Counter(
            code for codes in references.values() for code in codes).items())),
        'reference_code_sets': [{'codes': list(codes), 'reference_count': n}
            for codes, n in sorted(Counter(tuple(sorted(v)) for v in references.values()).items())],
        'object_type_reference_counts': dict(sorted(Counter(
            next(iter(v)) for v in object_types.values()).items())),
        'references_with_multiple_codes': [{'reference': ref, 'codes': sorted(codes)}
            for ref, codes in sorted(references.items()) if len(codes) > 1],
        'limitations': [
            'Raw code incidence only; interpret labels using the separately verified primary codebook.',
            'Reference incidences overlap when different sides have different codes.',
            'Only represented sides are counted; this does not reconstruct missing or uncatalogued surfaces.',
            'Distinct catalogue references do not prove independent objects or dies.',
            'No sequence association, animal identity, chronology or semantic value is inferred.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = profile(json.loads(args.corpus.read_bytes()))
    result['source_pins'] = [{'path': str(p.resolve().relative_to(ROOT)),
                            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                           for p in (args.corpus, Path(__file__))]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['counts']))


if __name__ == '__main__':
    main()
