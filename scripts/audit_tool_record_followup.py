"""Keep new physical records separate from earlier hypothetical mass calibrations."""
from fractions import Fraction as F
import json
from common import ROOT, sha256, write_json
from audit_metal_weight_anchors import encoded, three_object_constraint


def calibrations(chisel, axe):
    i=F(axe)/5
    return [{'reading':reading,'u_g':encoded(u),'i_g':encoded(i),'u_over_i':encoded(u/i)}
            for reading,u in [('2u',F(chisel)/2),('1u ignoring other mark',F(chisel)),
                              ('u+2i',F(chisel)-2*i)]]


def main():
    path=ROOT/'data/processed/kalibangan_tool_record_review.json'
    review=json.loads(path.read_text())
    original_path=ROOT/'data/processed/metal_original_records.json'
    original=json.loads(original_path.read_text())
    for source in original['raw_sources']+original['evidence_crops']:
        assert sha256(ROOT/source['path'])==source['sha256'],source['path']
    original_by_plate={r['stable_primary_locator']:r for r in original['records']}
    tang=original_by_plate['Plate CXXVI, no. 2']
    small=original_by_plate['Plate CXXVI, no. 3']
    large=original_by_plate['Plate CXXVI, no. 5']
    for source in review['evidence']:
        assert sha256(ROOT/source['path'])==source['sha256'],source['path']
    chisel,axe=review['objects']
    assert (chisel['cisi_id'],axe['cisi_id'])==('K-121','K-122')
    for obj in review['objects']:
        assert obj['nmma_candidate']['join_status'].startswith('probable'), 'Do not silently promote the accession join'
    result={
        'scope':'Source-level follow-up; calibration is not validation or decipherment.',
        'kalibangan_review_sha256':sha256(path),
        'mackay_original_review_sha256':sha256(original_path),
        'kalibangan_pettersson_masses':calibrations('210','476'),
        'kalibangan_nmma_candidate_masses':calibrations(chisel['nmma_candidate']['reported_mass_g'],axe['nmma_candidate']['reported_mass_g']),
        'nmma_join_authenticated':False,
        'nmma_independent_reweighing_demonstrated':False,
        'mohenjo_primary_metric_sensitivity':three_object_constraint(tang['mass_grams_literal'],large['mass_grams_literal'],small['mass_grams_literal']),
        'mohenjo_sensitivity_assumptions':'Same proposed u/i/t expressions as Pettersson; primary plate CXXVI2/3/5 mass joins; field7535 vs7835 unresolved; p<2.6 retained only as a hypothesis.',
        'large_axe_field_id_conflict':{'mackay1938_table_p489':large['primary_field_number_reading'],'pettersson1999':'7835','resolved':False},
        'new_established_sign_values':0}
    write_json('results/tool_record_followup.json',result)
    print('Tool records: 2 primary Kalibangan joins; 2 provisional museum matches; 1 unresolved axe-ID conflict; 0 sign values.')


if __name__=='__main__':
    main()
