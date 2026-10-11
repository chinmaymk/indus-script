"""Exhaustive local occurrence audit of Parpola's hind-leg reading candidates.

The W278/W279 candidates are object/position alignments, not accepted P/M aliases.
No proposed translations from the secondary CSV enter this analysis.
"""
import csv
import json
import re
from collections import Counter
from common import ROOT, read_jsonl, sha256, write_csv, write_json

CANDIDATES = {'278','279'}
RELATED = {'280','281'}
EXPOSURE = {'M-1690':'discovery_context','M-71':'shape_illustration','M-290':'author_proposed_followup'}
FIELDS = ('id','cisi','site','type','condition','preservation','complete','dir.','class','text')


def occurrences(text, codes):
    """Find exact three-digit tokens; don't bridge uncertainty or line delimiters."""
    output = []
    for match in re.finditer(r'(?<!\d)\d{3}(?!\d)',text):
        if match.group() not in codes:
            continue
        left = re.search(r'(?<!\d)(\d{3})-$',text[:match.start()])
        right = re.match(r'-(\d{3})(?!\d)',text[match.end():])
        output.append(dict(code='W'+match.group(),start=match.start(),end=match.end(),
            file_left='W'+left.group(1) if left else '',
            file_right='W'+right.group(1) if right else ''))
    return output


def scan(rows, strict_ids, codes):
    output = []
    for row in rows:
        for hit in occurrences(row['text'],codes):
            entry = {k:row.get(k,'') for k in FIELDS}
            entry.update(hit)
            entry['in_strict_subset'] = row['id'] in strict_ids
            entry['paper_exposure'] = EXPOSURE.get(row['cisi'],'not_named_in_selected_argument')
            entry['next_if_reported_RL'] = hit['file_left'] if row['dir.']=='R/L' else ''
            entry['plain_fish_after_in_reported_RL'] = row['dir.']=='R/L' and hit['file_left']=='W220'
            output.append(entry)
    return output


def count_summary(rows):
    return dict(occurrences=len(rows), rows=len({r['id'] for r in rows}),
        codes=dict(Counter(r['code'] for r in rows)),
        strict_occurrences=sum(r['in_strict_subset'] for r in rows),
        known_RL_occurrences=sum(r['dir.']=='R/L' for r in rows),
        plain_fish_after_in_reported_RL=sum(r['plain_fish_after_in_reported_RL'] for r in rows),
        by_paper_exposure=dict(Counter(r['paper_exposure'] for r in rows)))


def main():
    raw=ROOT/'data/raw/lipi_inscriptions.csv'
    with raw.open() as handle:
        rows=list(csv.DictReader(handle))
    strict_ids={r['id'] for r in read_jsonl('data/processed/lipi_strict.jsonl')}
    features=json.loads((ROOT/'data/processed/catalogue_features.json').read_text())
    main_rows=scan(rows,strict_ids,CANDIDATES)
    related=scan(rows,strict_ids,RELATED)
    main_rows.sort(key=lambda r:float(r['id']))
    related.sort(key=lambda r:float(r['id']))
    write_csv('results/hind_leg_occurrences.csv',main_rows)
    write_csv('results/hind_leg_related_not_merged.csv',related)
    result=dict(source_rows_scanned=len(rows),raw_sha256=sha256(raw),
        paper_sha256=sha256(ROOT/'data/raw/parpola_2009_hind_leg_fish.pdf'),
        primary_candidate_summary=count_summary(main_rows),
        outside_discovery_summary=count_summary([r for r in main_rows if r['cisi']!='M-1690']),
        not_named_in_argument_summary=count_summary([r for r in main_rows if r['paper_exposure']=='not_named_in_selected_argument']),
        related_codes_not_merged_summary=count_summary(related),
        direct_catalogue_entries={code:[f for f in features if code in f['wells_graphemes']]
            for code in ['W278','W279','W280','W281','W220','W345']},
        interpretation='Occurrence counts and source-aligned candidate codes, not semantic validation or a universal star-name rule.')
    write_json('results/hind_leg_audit.json',result)
    print(json.dumps(result['primary_candidate_summary'],indent=2))


if __name__=='__main__':
    main()
