"""Independent reconstruction of the frozen DHR-24475 locator; no producer imports.

Literal matching uses direct tuple comparisons. Slash compatibility is obtained
by enumerating every Cartesian-product reading, not the producer's distance
bounds. Expanded options remain verification devices, never attestations.
"""
import csv
import hashlib
import itertools
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = 'data/processed/dhr24475_context_protocol.json'
OUTPUT = 'results/dhr24475_context_screen.json'
EXPECTED_PROTOCOL = '56b5e3b0477baa90297b5397c09c95aba767b02033ad2404ac2d2f11292ab7c5'
OMIT = {'sanskrit', 'translation', 'notes'}
TARGET = ('391', '002', '365', '550')
PATTERN = re.compile(r'([+\[\]])([0-9]{3}(?:/[0-9]{3})*(?:-[0-9]{3}(?:/[0-9]{3})*){3})([+\[\]])')


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def classify(raw):
    value = raw.strip()
    matched = PATTERN.fullmatch(value)
    if not matched:
        if len(value) < 2 or value[0] not in '+[]' or value[-1] not in '+[]':
            reason = 'missing_or_invalid_endpoint'
        elif value[1:-1].count('-') != 3:
            reason = 'not_four_cells'
        else:
            reason = 'malformed_cell_or_interior_boundary'
        return 'other_excluded', reason, None
    left, middle, right = matched.groups()
    options = tuple(tuple(sorted(set(cell.split('/')))) for cell in middle.split('-'))
    if {'000', '999'}.intersection(itertools.chain.from_iterable(options)):
        return 'unknown_four_cell', 'unknown_or_separator_token', options
    if '/' in middle:
        return 'slash_sensitivity', None, options
    return ('primary' if (left, right) == ('+', '+') else 'boundary_sensitivity'), None, options


def literal_classes(sequence):
    flags = []
    if sequence == TARGET:
        flags.append('exact_duplicate')
    # Explicitly compare the unchanged three-slot projection at each position.
    one_change = any(
        sequence[i] != TARGET[i]
        and sequence[:i] + sequence[i + 1:] == TARGET[:i] + TARGET[i + 1:]
        for i in range(4)
    )
    if one_change:
        flags.append('one_position_substitution')
    if sequence[0] != TARGET[0] and sequence[1:] == TARGET[1:]:
        flags.append('initial_substitution_exact_tail')
    return flags


def slash_oracle(options):
    expansions = list(itertools.product(*options))
    distances = [sum(a != b for a, b in zip(seq, TARGET)) for seq in expansions]
    flags = []
    if TARGET in expansions:
        flags.append('possible_duplicate')
    if 1 in distances:
        flags.append('possible_one_position')
    if any(seq[0] != TARGET[0] and seq[1:] == TARGET[1:] for seq in expansions):
        flags.append('possible_initial_substitution_exact_tail')
    return flags, min(distances), max(distances), len(expansions)


def main():
    observed = json.loads((ROOT / OUTPUT).read_text())
    protocol = json.loads((ROOT / PROTOCOL).read_text())
    checks, failures = [], []

    def check(name, actual, expected):
        ok = actual == expected
        checks.append({'name': name, 'passed': ok})
        if not ok:
            failures.append({'name': name, 'actual': actual, 'expected': expected})

    check('frozen_protocol_sha256', digest(PROTOCOL), EXPECTED_PROTOCOL)
    check('embedded_protocol', observed['protocol'], protocol)
    for path, expected in observed['input_sha256'].items():
        check('input_pin:' + path, digest(path), expected)
    source = protocol['source']
    check('protocol_source_sha256', digest(source['path']), source['sha256'])
    check('protocol_source_bytes', (ROOT / source['path']).stat().st_size, source['bytes'])
    check('target_tokens', protocol['seed']['tokens'], list(TARGET))
    check('translation_columns_excluded', set(protocol['scope']['excluded_columns']), OMIT)
    check('unknown_clarification', observed['implementation_unknown_tokens'], ['000', '999'])
    required_pins = {PROTOCOL, source['path'], 'docs/DHR24475_CONTEXT_DESIGN.md',
                     'docs/DHR24475_CONTEXT_IMPLEMENTATION.md', 'scripts/screen_dhr24475_contexts.py',
                     'scripts/prepare_corpora.py', 'tests/test_dhr24475_contexts.py'}
    check('complete_input_pin_inventory', set(observed['input_sha256']), required_pins)

    with (ROOT / source['path']).open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    ledger, uncertain, hits, slash_audit = [], [], [], []
    eligible_literal_checks = 0
    for index, raw in enumerate(rows, 2):
        branch, reason, options = classify(raw['text'])
        ledger.append({'csv_row': index, 'id': raw['id'], 'text': raw['text'],
                       'branch': branch, 'exclusion_reason': reason})
        family = re.fullmatch(r'([0-9]+)\.[0-9]+', raw['id'])
        record = {'csv_row': index, 'raw': {k: v for k, v in raw.items() if k not in OMIT},
                  'branch': branch, 'is_seed': raw['id'] == protocol['seed']['id'],
                  'literal_seed_text_equal': raw['text'] == protocol['seed']['text'],
                  'possible_row_family': family.group(1) if family else None}
        if branch == 'unknown_four_cell':
            uncertain.append(record)
        elif options is not None:
            record['slots'] = [list(slot) for slot in options]
            if branch == 'slash_sensitivity':
                flags, low, high, count = slash_oracle(options)
                record.update(flags=flags, minimum_distance=low, maximum_distance=high)
                slash_audit.append({'csv_row': index, 'id': raw['id'], 'text': raw['text'],
                                    'expanded_verification_options': count,
                                    'minimum_distance': low, 'maximum_distance': high,
                                    'possible_flags': flags})
            else:
                sequence = tuple(slot[0] for slot in options)
                eligible_literal_checks += 1
                record.update(tokens=list(sequence), flags=literal_classes(sequence),
                              changed_positions=[i for i, (x, y) in enumerate(zip(sequence, TARGET)) if x != y])
            if record['flags']:
                hits.append(record)
        # Per-row comparison gives actionable diagnostics, not only equal totals.
        check('parser_row:' + str(index), observed['parser_ledger'][index - 2], ledger[-1])

    check('parser_ledger_complete', observed['parser_ledger'], ledger)
    check('hit_rows_flags_metadata', observed['hits'], hits)
    check('unknown_rows_metadata', observed['uncertainty_ledger'], uncertain)
    check('seed_metadata', [r['raw'] for r in hits if r['is_seed']], [protocol['seed']['raw_metadata']])
    counts = {}
    for branch in ('primary', 'boundary_sensitivity', 'slash_sensitivity'):
        classes = (('possible_duplicate', 'possible_one_position', 'possible_initial_substitution_exact_tail')
                   if branch == 'slash_sensitivity' else
                   ('exact_duplicate', 'one_position_substitution', 'initial_substitution_exact_tail'))
        counts[branch] = {}
        for name in classes:
            selected = [r for r in hits if r['branch'] == branch and name in r['flags']]
            count = {'rows': len(selected), 'distinct_raw_strings': len({r['raw']['text'] for r in selected}),
                     'seed_rows': sum(r['is_seed'] for r in selected),
                     'additional_rows': sum(not r['is_seed'] for r in selected)}
            if branch != 'slash_sensitivity':
                count['distinct_token_tuples'] = len({tuple(r['tokens']) for r in selected})
            counts[branch][name] = count
    summary = {'source_rows': len(rows), 'parser_categories': dict(Counter(r['branch'] for r in ledger)),
               'exclusion_reasons': dict(Counter(r['exclusion_reason'] for r in ledger if r['exclusion_reason'])),
               'counts_by_branch_class': counts, 'distinct_matching_source_rows': len(hits)}
    check('all_summary_counts', observed['summary'], summary)
    families = {r['possible_row_family'] for r in hits if r['possible_row_family'] is not None}
    hit_indices = {r['csv_row'] for r in hits}
    companions = []
    for index, row in enumerate(rows, 2):
        family = re.fullmatch(r'([0-9]+)\.[0-9]+', row['id'])
        if family and family.group(1) in families:
            companions.append({'csv_row': index, 'raw': {k: v for k, v in row.items() if k not in OMIT},
                               'is_hit': index in hit_indices})
    check('companion_rows_metadata_and_hit_flags', observed['same_stem_companions_not_extra_hits'], companions)
    check('physical_count_unresolved', observed['physical_artifact_count'], None)
    check('no_semantic_values', observed['established_semantic_values'], 0)
    check('no_phonetic_values', observed['established_phonetic_values'], 0)

    report = {'scope': 'Independent reconstruction of the stored-string screen, not graphical or semantic validation.',
              'method': 'Standard-library-only verifier; no producer imports. Whole-string grammar, direct literal tuple equality/projections, exhaustive Cartesian slash expansions.',
              'checks_passed': sum(c['passed'] for c in checks), 'checks_total': len(checks),
              'passed': not failures, 'failures': failures, 'checks': checks,
              'independent_summary': summary, 'literal_rows_reconstructed': eligible_literal_checks,
              'slash_expansion_audit': slash_audit,
              'companion_rows': companions,
              'input_sha256': {p: digest(p) for p in sorted(required_pins | {OUTPUT, 'scripts/verify_dhr24475_contexts.py'})},
              'differences': [],
              'limitations': ['Excluding 999 is the saved pre-count conservative clarification, not a new decipherment claim.',
                              'The six producer tests exercise helper functions; this verifier separately checks every actual runner parse and all ten slash rows.',
                              'All source counts are row/formula counts; physical identity and archaeological independence remain unresolved.',
                              'Hash equality checks current retained files, not independently authenticated chronology of the freeze.']}
    destination = ROOT / 'results/dhr24475_context_independent.json'
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: report[k] for k in ('passed', 'checks_passed', 'checks_total', 'literal_rows_reconstructed', 'failures')}, indent=2))
    print(json.dumps(summary, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
