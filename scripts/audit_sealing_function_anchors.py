"""Audit conditional container-label constraints, preserving unknown contexts.

Reported stamp identity and container interpretations are source hypotheses.
An empty domain intersection rejects a restricted exact-label model only under
those hypotheses. It does not reject commodity, owner or authority readings.
"""
import json
from common import ROOT,sha256,write_json


def shared_label(domains):
    """None is unobserved, not an impossible or empty category."""
    known=[set(d) for d in domains if d is not None]
    if any(not d for d in known):
        raise ValueError('Empty observed domain is invalid; use None for unknown')
    if not known:
        return {'status':'unconstrained','possible_labels':None}
    intersection=set.intersection(*known)
    return {'status':'compatible' if intersection else 'incompatible',
            'possible_labels':sorted(intersection)}


def main():
    path=ROOT/'data/processed/sealing_function_review.json'
    review=json.loads(path.read_text())
    for e in review['evidence']:
        assert sha256(ROOT/e['path'])==e['sha256'],e['path']
    rows=review['recurrent_stamp_cases']
    result=shared_label([r['hypothetical_container_domain'] for r in rows])
    assert result['status']=='incompatible'
    # A deliberately weaker sensitivity: retain only the three singly stamped
    # items, and then remove the uncertain leather interpretation entirely.
    singles=[r for r in rows if r['cisi_id'] in ('L-124','L-125','L-126')]
    without_leather=[None if r['cisi_id']=='L-126' else r['hypothetical_container_domain']
                     for r in singles]
    write_json('results/sealing_function_anchors.json',{
        'source_review_sha256':sha256(path),
        'distinct_reviewed_recurrent_stamp_items':len(rows),
        'source_reported_total_impressions_of_this_stamp':16,
        'cases_are_selected_not_a_complete_16_impression_inventory':True,
        'exact_exclusive_container_label_model':result,
        'three_single_impression_examples':shared_label([r['hypothetical_container_domain'] for r in singles]),
        'three_examples_with_leather_identification_unconstrained':shared_label(without_leather),
        'scope':'Conditional on author-reported stamp identity and explicitly encoded container domains. No sign transcription, translation or individual sign meaning follows.',
        'contents_identified':False,
        'independent_semantic_anchors':0,
        'warehouse_context_warning':'W1 is inferred using recurrent seal identity; it is not an independent findspot observation.',
        'new_established_sign_values':0})
    print('Sealing function: one reported stamp crosses container domains; dropping uncertain leather removes the three-case contradiction.')


if __name__=='__main__':main()
