"""Exact falsification screen for a universal monotone tally-field grammar.

All orders are enumerated; no quantity or boundary is asserted as deciphered.
"""
import csv
import itertools
import json
from collections import Counter
from common import ROOT, sha256, write_json, write_csv
from prepare_corpora import parse_lipi
from screen_numeral_pairs import literal_tokens


def maximal_runs(sequence, classes):
    membership = {token: name for name, tokens in classes.items() for token in tokens}
    if len(membership) != sum(map(len, classes.values())):
        raise ValueError('Classes overlap')
    start = 0
    while start < len(sequence):
        if sequence[start] not in membership:
            start += 1
            continue
        end = start + 1
        while end < len(sequence) and sequence[end] in membership:
            end += 1
        yield dict(start=start, end=end, tokens=sequence[start:end],
                   classes=[membership[t] for t in sequence[start:end]])
        start = end


def descents(classes, order, merge):
    ranks = {c: i for i, c in enumerate(order)}
    values = [ranks[merge.get(c, c)] for c in classes]
    # Index i means the boundary immediately BEFORE token i.
    return [i for i in range(1, len(values)) if values[i-1] > values[i]]


def models():
    result = []
    for name, merge, alphabet in [
        ('separate', {}, ['long', 'short', 'stacked']),
        ('stacked_as_long', {'stacked': 'long'}, ['long', 'short']),
        ('stacked_as_short', {'stacked': 'short'}, ['long', 'short'])]:
        for order in itertools.permutations(alphabet):
            result.append(dict(id=name + ':' + '<'.join(order), family=name,
                               order=list(order), merge=merge))
    return result


def unique_runs(runs, mode):
    if mode == 'row_runs':
        return runs
    dedup = {}
    for run in runs:
        if mode == 'artifact_text_runs':
            key = (run['artifact'], tuple(run['sequence']), run['start'])
        elif mode == 'text_runs':
            key = (tuple(run['sequence']), run['start'])
        elif mode == 'run_patterns':
            key = tuple(run['tokens'])
        else:
            raise ValueError(mode)
        dedup.setdefault(key, run)
    return list(dedup.values())


def summarize(runs):
    summaries = {}
    for unit in ('row_runs', 'artifact_text_runs', 'text_runs', 'run_patterns'):
        selected = unique_runs(runs, unit)
        multi = [r for r in selected if len(r['tokens']) >= 2]
        evaluations = []
        for model in models():
            errors = [descents(r['classes'], model['order'], model['merge']) for r in multi]
            evaluations.append(dict(**model, failures=sum(bool(e) for e in errors),
                                    minimum_additional_boundaries=sum(map(len, errors))))
        best = {}
        for family in sorted({m['family'] for m in evaluations}):
            scores = [m for m in evaluations if m['family'] == family]
            minimum = min(m['failures'] for m in scores)
            best[family] = dict(minimum_failures=minimum,
                best_orders=[m['order'] for m in scores if m['failures'] == minimum])
        summaries[unit] = dict(all_runs=len(selected), multi_sign_runs=len(multi),
            evaluations=evaluations, best=best)
    return summaries


def reversed_pairs_within_metadata(runs):
    """Find opposite non-palindromic run orders without selecting examples by hand."""
    groups = {}
    for run in runs:
        if len(set(run['classes'])) < 2:
            continue
        key = (run['site'], run['type'], tuple(run['tokens']))
        groups.setdefault(key, []).append(run['id'])
    pairs = []
    for (site, kind, tokens), ids in sorted(groups.items()):
        reverse = tuple(reversed(tokens))
        if tokens >= reverse or (site, kind, reverse) not in groups:
            continue
        pairs.append(dict(site=site, type=kind, forward=list(tokens), reverse=list(reverse),
                          forward_row_ids=sorted(set(ids)),
                          reverse_row_ids=sorted(set(groups[site, kind, reverse]))))
    return pairs


def select_rows(rows, allow_lr):
    selected, exclusions = [], []
    for row in rows:
        sequence, reasons = parse_lipi(row)
        if allow_lr and row['dir.'].strip().upper() == 'L/R':
            reasons = [x for x in reasons if x != 'direction_not_R/L']
        if reasons:
            exclusions.append(dict(id=row['id'], cisi=row['cisi'], text=row['text'],
                                   direction=row['dir.'], reasons=reasons))
        else:
            artifact = row['cisi'].strip()
            if artifact in ('', '-', '--', '?'):
                artifact = 'lipi_id:' + row['id'].split('.')[0]
            selected.append(dict(id=row['id'], artifact=artifact, text=row['text'],
                sequence=sequence, direction=row['dir.'], condition=row['condition'],
                preservation=row['preservation'], type=row['type'], site=row['site']))
    return selected, exclusions


def main():
    protocol_file = ROOT/'data/processed/numeral_theory_protocol.json'
    protocol = json.loads(protocol_file.read_text())
    source = ROOT/'data/raw/lipi_inscriptions.csv'
    with source.open() as f:
        rows = list(csv.DictReader(f))
    result = dict(source_sha256=sha256(source), protocol_sha256=sha256(protocol_file),
                  status=protocol['status'], all_source_rows=len(rows), screens={},
                  new_established_sign_values=0)
    # Keep manually reviewed primary patterns separate from corpus counts.
    primary_path = ROOT/'data/processed/primary_tally_patterns.json'
    primary = json.loads(primary_path.read_text())
    if sha256(ROOT/primary['source']) != primary['source_sha256']:
        raise ValueError('Primary tally review no longer matches its source')
    evaluations = []
    for order in itertools.permutations(['long', 'short']):
        evaluations.append({'order': list(order), 'patterns': [
            {'reference': p['reference'], 'classes': p['classes'],
             'required_cuts_before_indices': descents(p['classes'], order, {})}
            for p in primary['patterns']]})
    write_json('results/primary_tally_order_check.json', {
        'manual_ledger_sha256': sha256(primary_path),
        'assumption': primary['assumption_for_order_test'],
        'limits': primary['limits'], 'evaluations': evaluations,
        'orders_fitting_all_patterns': [e['order'] for e in evaluations
            if all(not p['required_cuts_before_indices'] for p in e['patterns'])]})
    witnesses = []
    for scope in ('classes', 'conservative_classes'):
        classes = protocol[scope]
        members = {t for family in classes.values() for t in family}
        relevant = [r for r in rows if members.intersection(literal_tokens(r['text']))]
        for allow_lr in (False, True):
            key = scope + ('_allow_LR' if allow_lr else '_strict')
            selected, exclusions = select_rows(relevant, allow_lr)
            runs = [dict(**row, **run) for row in selected for run in maximal_runs(row['sequence'], classes)]
            views = {}
            for quality, conditions in [('all', None), ('fair_or_better', {'good', 'fine', 'fair'}),
                                        ('good_or_fine', {'good', 'fine'})]:
                chosen = [r for r in runs if conditions is None or r['condition'].strip().lower() in conditions]
                views[quality] = summarize(chosen)
            graph = Counter((a,b) for r in runs for a,b in zip(r['classes'], r['classes'][1:]) if a != b)
            result['screens'][key] = dict(candidate_source_rows=len(relevant),
                eligible_rows=len(selected), excluded_rows=len(exclusions),
                eligible_condition_labels=dict(Counter(r["condition"] for r in selected)),
                exclusions=exclusions, runs=runs, summaries=views,
                good_fine_reversed_pairs_same_site_type=reversed_pairs_within_metadata(
                    [r for r in runs if r["condition"].strip().lower() in ("good", "fine")]),
                distinct_class_transitions=[dict(before=a, after=b, count=n) for (a,b),n in sorted(graph.items())])
            if key == 'classes_strict':
                for run in runs:
                    if len(run['tokens']) < 2:
                        continue
                    witnesses.append(dict(id=run['id'], artifact=run['artifact'],
                        condition=run['condition'], direction=run['direction'],
                        full_text=run['text'], start_index=run['start'],
                        run=' '.join(run['tokens']), classes=' '.join(run['classes']),
                        violating_orders=';'.join(m['id'] for m in models()
                            if descents(run['classes'], m['order'], m['merge']))))
    write_json('results/numeral_theory_audit.json', result)
    write_csv('results/numeral_theory_runs.csv', witnesses)
    for key, screen in result['screens'].items():
        print(key, 'eligible', screen['eligible_rows'], 'excluded', screen['excluded_rows'])
        for quality, summaries in screen['summaries'].items():
            s=summaries['text_runs']
            print(quality, 'all runs',s['all_runs'],'multi',s['multi_sign_runs'],s['best'])


if __name__ == '__main__':
    main()
