"""Verify the extreme association completions using independent closed-form bounds.

This proves nonidentification for a documentary reporting outcome, not for ancient
commodity use. No missing inscription or grain observation becomes an absence.
"""
import json
from fractions import Fraction
from common import ROOT,sha256,write_json

def main():
    path='results/inscribed_jar_frame.json';frame=json.loads((ROOT/path).read_text())
    rows=frame['rows'];assert len(rows)==176
    assert {r['serial'] for r in rows}==set(range(1,177))
    reports={r['serial'] for r in rows if r['cereal_related_mention']}
    positives={r['serial'] for r in rows if r['jar_inscription_status']=='explicitly_reported'}
    assert positives=={18,35,116} and positives & reports=={35,116}
    assert not any(r['observed_uninscribed'] for r in rows)
    def bounds(reports):
        n=len(rows);g=len(reports);a=len(positives&reports);b=len(positives-reports)
        # Every inscribed group contains the a known cereal mentions and b known
        # nonmentions. Group all g mentions with those b rows for the upper bound;
        # group all n-g nonmentions with those a rows for the lower bound.
        upper=Fraction(g,g+b)
        lower=Fraction(a,n-g+a)-1
        return dict(mention_rows=g,lower_exact=str(lower),upper_exact=str(upper),
                    lower=float(lower),upper=float(upper),both_directions_possible=lower<0<upper)
    broad=bounds(reports)
    expected=frame['documentary_association_nonidentifiability']
    assert expected['minimum']['difference_exact']==broad['lower_exact']
    assert expected['maximum']['difference_exact']==broad['upper_exact']
    for key in ('minimum','maximum'):
        c=expected[key]
        first=Fraction(c['inscribed_group_cereal_mentions'],c['inscribed_group_rows'])
        other=Fraction(c['other_group_cereal_mentions'],c['other_group_rows'])
        assert str(first-other)==c['difference_exact']
        assert c['inscribed_group_rows']+c['other_group_rows']==len(rows)
    strict=bounds(reports-{30,135})
    write_json('results/inscribed_jar_bounds_independent.json',dict(
        broad_reporting_outcome=broad,excluding_apparent_fill_and_cereal_like_impression=strict,
        proof='A known-positive set contains a cereal mentions and b nonmentions. The upper bound g/(g+b) is achieved by assigning every cereal mention to the inscribed group; the lower bound a/(n-g+a)-1 is achieved by assigning every nonmention to that group. Both keep the other group nonempty.',
        applicability='Only completed latent inscription statuses and documentary cereal reports within176 printed serials; no archaeological noninscription or commodity absence inferred.',
        input_sha256={p:sha256(ROOT/p) for p in [path,'scripts/verify_inscribed_jar_bounds.py']}))
    print(f'Independent sharp bounds verified: {broad["lower_exact"]} to {broad["upper_exact"]}; stricter reporting sensitivity also crosses zero.')

if __name__=='__main__':main()
