"""Test an arch-composition bound while permitting nonnegative residual signs."""
from fractions import Fraction as F
from collections import Counter
import csv
import json
from common import ROOT, sha256, write_json, write_jsonl


def exact(v):
    return {'fraction':str(v), 'decimal':float(v)}


def bound(small, large, chisel, minimum_arch_units):
    s,l,k,n = map(F,(small,large,chisel,minimum_arch_units))
    if min(s,l,k,n)<=0:
        raise ValueError('Positive masses and minimum arch count required')
    cap=s+7*k/n
    deficit=l-cap
    return {'minimum_arch_units_in_chisel':exact(n),
            'large_axe_upper_bound_g':exact(cap),
            'large_axe_observed_g':exact(l), 'deficit_g':exact(deficit),
            'combined_premises_inconsistent':deficit>0,
            'minimum_chisel_mass_if_axes_held_fixed_g':exact(max(F(0),n*(l-s)/7)),
            'minimum_added_chisel_mass_if_axes_held_fixed_g':exact(max(F(0),deficit*n/7)),
            'minimum_added_small_axe_mass_if_other_two_held_fixed_g':exact(max(F(0),deficit)),
            'damage_constraint':{'coefficient_small_axe': '1','coefficient_chisel':str(7/n),
                                 'coefficient_large_axe':'-1','lower_bound_g':str(deficit)},
            'proof':'S=A+r with r>=0; K=n*u+q with q>=0. Hence L=A+7u<=S+7K/n. No assumption r=0 or A=6i is required.'}


def main():
    primary_path=ROOT/'data/processed/metal_original_records.json'
    later_path=ROOT/'data/processed/metal_tool_weight_anchors.json'
    review_path=ROOT/'data/processed/arch_extension_catalogue_review.json'
    protocol_path=ROOT/'data/processed/arch_mass_bound_protocol.json'
    records=json.loads(primary_path.read_text())['records']
    by_locator={r['stable_primary_locator']:r for r in records}
    s=by_locator['Plate CXXVI, no. 3']['mass_grams_literal']
    l=by_locator['Plate CXXVI, no. 5']['mass_grams_literal']
    for number in (3,5):
        pin=by_locator[f'Plate CXXVI, no. {number}']['mass_evidence']
        assert sha256(ROOT/pin['path'])==pin['sha256']
    later=json.loads(later_path.read_text())
    k=next(r for r in later['nine_object_table']['rows'] if r['object']=='K-121')['reported_surviving_mass_g']
    review=json.loads(review_path.read_text())
    for pin in review['evidence_files']:
        p=ROOT/pin['path'];assert p.stat().st_size==pin['bytes'] and sha256(p)==pin['sha256'],pin['path']
    fields={r['line_id']:r for r in review['lines']}
    assert len(fields)==len(review['lines'])==6
    for key,tokens in {'2924.0.0':['M108','M342','M001','M375'],
                       '2925.2.0':['M108','M315']}.items():
        field=fields[key]
        assert field['tokens']==tokens and not field['has_loss']
        assert field['doubtful_token_indices']==field['loss_token_indices']==[]
        assert field['texts_field_visually_checked_this_review']
    assert review['graphic_descriptions']['M315']['repeated_plain_arches']==7
    assert review['graphic_descriptions']['M315']['catalogue_tokens']==1
    assert fields['2925.1.0']['doubtful_token_indices']==[4]
    assert fields['4032.0.0']['loss_token_indices']==[1]
    assert fields['4032.0.0']['direction_code']==9
    table_path=ROOT/'data/processed/mahadevan_1977_table_i.csv'
    table={r['sign']:r for r in csv.DictReader(table_path.open())}
    counts={sign:Counter() for sign in ('M315','M316','M317','M318')}
    for occ in review['selected_occurrences']:
        field=fields[f"{occ['reference']}.{occ['side']}.{occ['line']}"]
        i=occ['token_index']; tokens=field['tokens']
        assert tokens[i]==occ['sign']
        position='solus' if len(tokens)==1 else 'initial' if i==0 else 'final' if i==len(tokens)-1 else 'medial'
        assert position==occ['position_class']
        counts[occ['sign']][position]+=1
        counts[occ['sign']]['total']+=1
    for sign,count in counts.items():
        for position in ('solus','initial','medial','final','total'):
            assert count[position]==review['table_i_verified'][sign][position]==int(table[sign][position])
    # Preserve the photographic limits of the chisel interpretation as an input.
    k_review_path=ROOT/'data/processed/kalibangan_tool_record_review.json'
    write_jsonl('data/processed/arch_extension_primary_lines.jsonl',review['lines'])
    result={'scope':'Conditional shared additive weight model, not established numeral values',
            'mass_inputs_g':{'small_axe':s,'large_axe':l,'K121':k},
            'branches':{'at_least_one_u':bound(s,l,k,'1'),'at_least_two_u':bound(s,l,k,'2')},
            'protocol':json.loads(protocol_path.read_text()),
            'primary_fields':review['lines'],
            'selected_occurrences':review['selected_occurrences'],
            'primary_counts_reconciled':{sign:dict(c) for sign,c in counts.items()},
            'coverage_scope':'Six source-qualified fields, overlapping earlier reviews; do not add their counts as independent corpus observations',
            'new_mass_observations':0,'established_semantic_values':0,'established_phonetic_values':0,
            'input_sha256':{str(p.relative_to(ROOT)):sha256(p) for p in (primary_path,later_path,review_path,protocol_path,table_path,k_review_path)}}
    write_json('results/arch_mass_bound.json',result)
    print(json.dumps(result['branches'],indent=2))


if __name__=='__main__':
    main()
