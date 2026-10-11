"""Keep primary artifact identity and compatible-context discovery separate."""
import csv
import json
from common import ROOT, sha256, write_json

def main():
    paths=['data/processed/pincer_primary_review.json','results/pincer_context_screen.json',
           'data/processed/mahadevan_1977_table_i.csv']
    review=json.loads((ROOT/paths[0]).read_text())
    for pin in review['evidence_files']:
        assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
        assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
    screen=json.loads((ROOT/paths[1]).read_text())
    candidates=[p for p in screen['candidate_pairs']
                if p['lipi_row']['id']=='2591.1' and p['m77_candidate_row']['source_reference']=='3068']
    assert len(candidates)==1
    pair=candidates[0]
    with (ROOT/paths[2]).open() as f:
        position_profiles=[{k:(int(v) if k in ['solus','initial','medial','final','total'] else v)
                            for k,v in row.items()} for row in csv.DictReader(f)
                           if row['sign'] in ('M216','M222')]
    assert pair['lipi_row']['sequence']==review['W_file_sequence']
    assert pair['m77_candidate_row']['sequence']==review['M_candidate_reading_sequence']
    assert {(p['w'],p['m']) for p in pair['target_assignments']}=={
        (p['W'],p['M']) for p in review['local_target_correspondences']}
    write_json('results/pincer_primary_audit.json',{
        'primary_review':review,'matching_screen_pair_id':pair['pair_id'],
        'identity_basis':'Primary excavation DK8333 and photograph references, not computed context match',
        'global_mapping_established':False,'allography_or_separate_values_resolved':False,
        'primary_Table_I_position_profiles':position_profiles,
        'profile_scope':'Reused historical primary transcription, not new counts; descriptive positions do not resolve allography or meaning',
        'input_sha256':{p:sha256(ROOT/p) for p in paths},
        'established_semantic_values':0,'established_phonetic_values':0})
    print('M63 primary pins and separately computed context match agree; no global mapping promoted.')

if __name__=='__main__':main()
