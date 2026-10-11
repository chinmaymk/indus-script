"""Compare published heights by excavation identifier, without merging CISI aliases.

Manual primary-page readings are explicit below. This is an identity/measurement
audit, not a new capacity calibration or statistical test of a numerical reading.
"""
import json
from decimal import Decimal
from common import ROOT,sha256,write_json

def main():
    old=json.loads((ROOT/'data/processed/capacity_table_followup.json').read_text())
    rows=[]
    for serial,identifier,feet,inches in [(2,'1033A',3,0),(3,'1033B',2,10)]:
        prior=next(r for r in old['table1']['rows'] if r['excavation_number'].lower()==identifier.lower())
        cm=Decimal(feet*12+inches)*Decimal('2.54')
        reported=Decimal(str(prior['external_height']))
        rows.append(dict(table_serial=serial,excavation_identifier=identifier,
            primary_height_feet=feet,primary_height_inches=inches,
            primary_height_cm=float(cm),primary_dimension_type='Ht.; external/internal not explicitly specified in Vats cell',
            fuls_public_text_external_height_cm=float(reported),
            absolute_difference_cm=float(abs(cm-reported)),
            agrees_when_rounded_to_one_decimal=round(cm,1)==reported,
            cisi_label_claimed_in_fuls_text=prior['cisi'],
            cisi_alias_accepted_here=identifier=='1033A',
            context=dict(mound='F',trench='I',square='M11/16',stratum='III',depth_feet=5,depth_inches=6,
                         primary_locator='Vats1940 volumeI printed254–255, tableI rows2–3; printed91'),
            primary_description='large, napiform' if serial==2 else 'Do. referring to large, napiform',
            directly_measured_capacity_litres=None,numeral_value=None))
    pins=['data/processed/capacity_table_followup.json','data/processed/capacity_h370_identities.json',
          'data/processed/capacity_md1374_cisi2_review.json','data/processed/capacity_table_primary_review.json',
          'data/processed/capacity_context_crop_manifest.json',
          'data/raw/vats_1940_plates_9842.pdf','scripts/analyze_capacity_context.py']
    pins += [f'data/raw/capacity-context-vats-leaf{n}.jpg' for n in (117,277,278,279,280,281)]
    output=dict(scope='Primary measurement agreement by excavation number; no semantic assignment',
        reviewed_rows=rows, shared_find_context_groups=1,
        reported_contents={
            '1033A':{'locator':'printed255,row2','observations':['seated male toy','miscellaneous potsherds','round faience bead','some charcoal']},
            '1033B':{'locator':'printed255,row3','observations':['cake fragments','goblet/vase potsherds','bangle fragments','charred wheat and slag']},
            'limit':'Recorded deposition assemblages, not direct evidence for original use, fill volume or inscription referent.'},
        independent_test_candidate=dict(identifier='3822',table_serial=18,primary_height_feet=2,primary_height_inches=3,
            primary_height_cm=68.58,mouth_diameter_inches=11,mouth_diameter_cm=27.94,
            context='F/I/M12/6, stratumVI, depth15ft9in',
            reported_inscription='3 pictograms at shoulder',
            eligible_for_current_tally_capacity_test=False,
            reasons=['Shoulder pictograms not authenticated as counted rim tallies','No internal profile or measured fill volume recovered','Not a prospectively selected independent sample']),
        new_direct_fill_measurements=0,new_complete_external_test_pairs=0,
        calibration_refit_performed=False,established_semantic_values=0,established_phonetic_values=0,
        conclusion='The old field-number heights agree after conversion. This does not settle contradictory aliases, sign segmentation or a capacity-per-stroke prediction.',
        input_sha256={p:sha256(ROOT/p) for p in pins})
    write_json('results/capacity_context_measurements.json',output)
    print(json.dumps({k:output[k] for k in ('new_direct_fill_measurements','new_complete_external_test_pairs','calibration_refit_performed')}))

if __name__=='__main__':main()
