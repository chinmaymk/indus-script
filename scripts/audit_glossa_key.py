"""Audit a pinned external proposal, without treating candidate readings as evidence.

No downloaded program is imported/executed. Coverage is inventory coverage, never
translation accuracy. External hypotheses do not modify sign_evidence_417.json.
"""
import csv
import hashlib
import json
from collections import Counter
from common import ROOT

PIN = '40812fc54470d5508b47af5fabcea7ccf044036c'
INVENTORY = tuple(f'M{i:03d}' for i in range(1, 418))


def audit_key(document, frequencies):
    anchors = document['anchors']
    domain = set(frequencies)
    counts = dict(sorted(Counter(v.get('confidence', 'UNSPECIFIED') for v in anchors.values()).items()))
    present = domain & anchors.keys()
    hm = {k for k in present if anchors[k].get('confidence') in ('HIGH', 'MEDIUM')}
    denominator = sum(frequencies.values())
    return {
        'entry_count': len(anchors), 'recomputed_confidence_counts': counts,
        'm77_present_count': len(present), 'm77_missing': sorted(domain - anchors.keys()),
        'outside_m77_inventory': sorted(anchors.keys() - domain),
        'high_medium_m77_count': len(hm),
        'm77_table_i_token_denominator': denominator,
        'nominal_id_coverage_tokens': sum(frequencies[k] for k in present),
        'nominal_high_medium_id_coverage_tokens': sum(frequencies[k] for k in hm),
        'coverage_warning': 'M77-ID matching only; neither transcription alignment nor reading validation. Confidence labels are the proposer\'s.',
        'reported_metadata': {k: document.get(k) for k in ('total', 'total_all_entries', 'by_confidence', 'n_high', 'n_medium', 'n_low', 'metadata', 'corpus_tokens', 'corpus_token_coverage')},
    }


def verify_review_sources(review):
    for name, expected in review['source_hashes'].items():
        observed = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if observed != expected:
            raise ValueError(f'Manual review is stale: {name}')


def compare_417(release, backend, review):
    reviewed = {r['id']: r for r in review['reviewed_anchors']}
    rows = []
    for sign in INVENTORY:
        a, b = release['anchors'].get(sign), backend['anchors'].get(sign)
        r = reviewed.get(sign)
        rows.append({
            'sign': sign,
            'release_candidate': None if a is None else {k: a.get(k) for k in ('reading', 'confidence')},
            'backend_candidate': None if b is None else {k: b.get(k) for k in ('reading', 'confidence')},
            'candidate_reading_changed': a is not None and b is not None and a.get('reading') != b.get('reading'),
            'manual_shape_review': None if r is None else {k: r[k] for k in ('morphology_observed', 'assessment', 'inference_limit', 'primary')},
            'reviewed_basis_retained_in_backend': None if r is None or a is None or b is None else a['basis'] in b['basis'],
            'established_phonetic_value': None, 'established_semantic_value': None,
            'status': 'external hypothesis only; not accepted as a decipherment',
        })
    return rows


def main():
    names = ['data/raw/glossa_anchor_table.json', 'data/raw/glossa_backend_anchors.json',
             'data/processed/glossa_sign_identity_review.json', 'data/processed/mahadevan_1977_table_i.csv']
    release, backend, review = [json.loads((ROOT / n).read_text()) for n in names[:3]]
    verify_review_sources(review)
    with (ROOT / names[3]).open() as f:
        frequencies = {r['sign']: int(r['total']) for r in csv.DictReader(f)}
    if set(frequencies) != set(INVENTORY):
        raise ValueError('Expected complete 417-sign primary inventory')
    rows = compare_417(release, backend, review)
    result = {
        'status': 'bounded external-proposal audit; not a decipherment', 'repository_commit': PIN,
        'source_sha256': {n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in names},
        'release': audit_key(release, frequencies), 'backend': audit_key(backend, frequencies),
        'changes': {
            'shared_entries': len(release['anchors'].keys() & backend['anchors'].keys()),
            'shared_reading_changed': sum(r['candidate_reading_changed'] for r in rows),
            'reviewed_entries': sum(r['manual_shape_review'] is not None for r in rows),
            'reviewed_bases_retained_in_backend': sum(r['reviewed_basis_retained_in_backend'] is True for r in rows),
        },
        'scope': 'Five deliberately selected identity checks, not a random sample or population error rate. Wrong pictorial support does not logically refute an arbitrary sound/meaning. No M/W/P numbers merged by numerical equality.',
    }
    (ROOT / 'results/glossa_key_audit.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    (ROOT / 'results/glossa_candidate_comparison_417.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'release': result['release']['entry_count'], 'backend': result['backend']['entry_count'], 'changes': result['changes']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
