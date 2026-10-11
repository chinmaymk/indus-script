"""Independent masked-W525 computation check; diagnostic locators stay separate."""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def independently_align(w_source, m_sequence, memberships):
    # Construct expanded position constraints before looking at M tokens.
    expanded, groups = [], []
    for w in w_source[::-1]:
        start = len(expanded)
        if w == 'W617':
            expanded += [('grid', {'M245'}), ('grid', {'M245'})]
        elif w == 'W525':
            expanded.append(('masked', {f'M{i:03d}' for i in range(1, 418)}))
        elif w in ('W550', 'W555'):
            expanded.append(('pincer', {'M216', 'M222'}))
        else:
            expanded.append(('family', memberships.get(w, set())))
        groups.append((w, list(range(start, len(expanded)))))
    if len(expanded) != len(m_sequence):
        return None
    if any(m not in choices for m, (_, choices) in zip(m_sequence, expanded)):
        return None
    masked_values = {m for m, (kind, _) in zip(m_sequence, expanded) if kind == 'masked'}
    if len(masked_values) != 1:
        return None
    bases = {'grid': 'declared_double_grid_span',
             'masked': 'masked_candidate_not_established_mapping',
             'pincer': 'source_exposed_pincer_candidates',
             'family': 'catalogue_family_membership'}
    segments = [{'reversed_W_position': i, 'W': w, 'M_positions': indices,
                 'M': [m_sequence[j] for j in indices], 'basis': bases[expanded[indices[0]][0]]}
                for i, (w, indices) in enumerate(groups)]
    return {'W525_candidate': next(iter(masked_values)), 'segments': segments}


def main():
    paths = ['data/processed/w525_protocol.json', 'data/processed/lipi_strict.jsonl',
             'data/processed/m77_candidate_strict.jsonl', 'data/processed/catalogue_features.json',
             'results/pincer_context_screen.json', 'data/processed/m77_candidate_records.jsonl',
             'results/w525_screen.json']
    protocol = json.loads((ROOT / paths[0]).read_text())
    datasets = {p: [json.loads(line) for line in (ROOT / p).read_text().splitlines() if line.strip()]
                for p in (paths[1], paths[2], paths[5])}
    features = json.loads((ROOT / paths[3]).read_text())
    prior = json.loads((ROOT / paths[4]).read_text())
    reported = json.loads((ROOT / paths[6]).read_text())
    assert protocol == reported['protocol']
    for p, digest in reported['input_sha256'].items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == digest, p
    memberships = defaultdict(set)
    for feature in features:
        for w in feature['wells_graphemes']:
            memberships[w].update(feature['mahadevan_graphemes'])
    assert not memberships.get('W525')
    assert independently_align(['W525', 'W525'], ['M254', 'M254'], {}) is not None
    assert independently_align(['W525', 'W525'], ['M254', 'M253'], {}) is None
    assert independently_align(['W525'], ['M418'], {}) is None
    assert independently_align(['W525'], ['M000'], {}) is None
    assert independently_align(['W617', 'W525'], ['M254', 'M245', 'M245'], {}) is not None
    assert independently_align(['W617', 'W525'], ['M254', 'M245'], {}) is None
    prior_ids = {r['lipi_row']['id'] for r in prior['selected_rows']}
    selected = [r for r in datasets[paths[1]] if 'W525' in r['sequence']]
    rows, pairs = [], []
    for row in selected:
        matches = []
        for candidate in datasets[paths[2]]:
            aligned = independently_align(row['sequence'], candidate['sequence'], memberships)
            if aligned is None:
                continue
            pair = {'pair_id': row['id'] + '__' + candidate['id'], 'lipi_row': row,
                    'm77_candidate_row': candidate, **aligned, 'archaeological_identity': None}
            pairs.append(pair)
            matches.append(pair)
        rows.append({'lipi_row': row, 'in_previous_pincer_selection': row['id'] in prior_ids,
                     'W525_candidates': sorted({p['W525_candidate'] for p in matches}),
                     'candidate_pair_ids': [p['pair_id'] for p in matches],
                     'unmapped_non_target_codes': sorted({w for w in row['sequence']
                         if w not in ('W525', 'W617', 'W550', 'W555') and not memberships.get(w)})})
    summary = {'selected_rows': len(rows), 'matched_rows': sum(bool(r['candidate_pair_ids']) for r in rows),
               'candidate_pairs': len(pairs),
               'rows_with_multiple_candidate_codes': sum(len(r['W525_candidates']) > 1 for r in rows),
               'candidate_code_pair_incidences': dict(Counter(p['W525_candidate'] for p in pairs)),
               'previous_pincer_rows': sum(r['in_previous_pincer_selection'] for r in rows),
               'matched_previous_pincer_rows': sum(r['in_previous_pincer_selection'] and bool(r['candidate_pair_ids']) for r in rows)}
    assert rows == reported['rows']
    assert pairs == reported['candidate_pairs']
    assert summary == reported['summary']
    eligible_diagnostics = []
    for record in datasets[paths[5]]:
        all_known = bool(record['tokens']) and all(t['sign'] is not None and not t['doubtful'] and not t['unknown_span'] for t in record['tokens'])
        if all_known and record['source_doc_count'] > 1 and str(record['source_direction_code']) == '1':
            eligible_diagnostics.append(record)
    diagnostic = []
    for row in selected:
        for record in eligible_diagnostics:
            seq = [token['sign'] for token in record['tokens']]
            aligned = independently_align(row['sequence'], seq, memberships)
            if aligned:
                diagnostic.append({'lipi_row': row, 'source_locator_record': record, **aligned,
                    'status': 'Unverified multi-document flat-array source locator only; not a recovered face-level text'})
    assert diagnostic == reported['post_null_multidocument_locator_candidates']
    assert len(rows) == 10 and summary['previous_pincer_rows'] == 9 and not pairs
    assert len(diagnostic) == 6 and {d['W525_candidate'] for d in diagnostic} == {'M254'}
    for key in ['established_semantic_values', 'established_phonetic_values', 'promoted_artifact_identifications']:
        assert reported[key] == 0
    output = {
        'all_checks_passed': True, 'summary': summary,
        'strict_M77_rows_searched': len(datasets[paths[2]]),
        'eligible_multidocument_diagnostic_records': len(eligible_diagnostics),
        'diagnostic_locator_count': len(diagnostic),
        'diagnostic_locator_list': [{'lipi_id': d['lipi_row']['id'], 'cisi_label': d['lipi_row']['cisi_original'],
                                    'M77_source_reference': d['source_locator_record']['source_reference'],
                                    'W525_candidate': d['W525_candidate']} for d in diagnostic],
        'verified_fields': ['full strict selected rows and metadata', 'strict candidate pairs', 'strict summary',
                            'full separate diagnostic records and ordered alignment segments', 'input hashes', 'zero promotions'],
        'independence': 'No imports from production helpers; expands reversed W sequences into constrained positions before examining candidate M sequences, separately enforcing one consistent M001–M417 value across all masked occurrences.',
        'scope': 'Computational verification only. The strict null is conditional on sparse corpora, existing feature memberships and declared tokenization; it does not refute a W525 mapping. Six post-null flat-array locators remain outside the strict result and supply no recovered face identity, independent sample, or established sign value.',
        'input_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'promoted_artifact_identifications': 0,
    }
    (ROOT / 'results/w525_independent.json').write_text(json.dumps(output, indent=2, sort_keys=True) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
