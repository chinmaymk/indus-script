"""Literal counterpart check anchored to separately reviewed primary artifacts."""
import csv
import json
from common import ROOT, sha256, read_jsonl, write_json

def main():
    paths=['data/processed/comb_variation_review.json',
           'data/processed/m934_primary_review.json','data/processed/ending_mapping_review.json',
           'data/raw/lipi_inscriptions.csv','data/processed/m77_candidate_strict.jsonl']
    review=json.loads((ROOT/paths[0]).read_text())
    for source in paths[:3]:
        for pin in json.loads((ROOT/source).read_text())['evidence_files']:
            assert sha256(ROOT/pin['path'])==pin['sha256'],pin['path']
            assert (ROOT/pin['path']).stat().st_size==pin['bytes'],pin['path']
    with (ROOT/paths[3]).open() as f:
        rows={r['id']:{k:r[k] for k in ['id','cisi','text','excavation-idno','type','preservation']}
              for r in csv.DictReader(f) if r['id'] in ['3329.1','2043.1']}
    a,b=[rows[i]['text'][1:-1].split('-') for i in ['3329.1','2043.1']]
    assert a[0]=='526' and b[0]=='527' and a[1:]==b[1:]
    m={r['source_reference']:r for r in read_jsonl(paths[4]) if r['source_reference'] in ['1158','7090']}
    assert m['1158']['sequence']==m['7090']['sequence']==['M267','M099','M065','M222','M254']
    write_json('results/comb_variation_audit.json',{
        'primary_review':review,'secondary_rows':rows,'M77_candidate_rows':m,
        'only_literal_W_difference':'W526 versus W527 at file first token',
        'identity_basis':'Reviewed original excavation/plate numbers and explicit M77 catalogue references, not sequence similarity',
        'interpretation':'Primary-supported candidate orientation variant in this context; global allography, phonetic and semantic identity unresolved',
        'established_semantic_values':0,'established_phonetic_values':0,
        'input_sha256':{p:sha256(ROOT/p) for p in paths}})
    print('MIC158/DM50 and L89 comparison verified; global allography remains unresolved.')

if __name__=='__main__':main()
