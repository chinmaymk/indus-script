"""Reproduce and pin local H904/M331 photograph review; no global mapping change."""
from pathlib import Path
from PIL import Image
from fractions import Fraction
import argparse, csv, hashlib, json, subprocess

ROOT=Path(__file__).resolve().parents[1]
PDFTOPPM=Path('/Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm')
SOURCES=[('data/raw/h843_identity_CorpusVol2.pdf',[373,479],'h904-numeral-cisi2'),
         ('data/raw/cisi_76884.pdf',[120],'h904-numeral-m331')]
CROPS=[('h904-numeral-cisi2-373.png','h904-numeral-h904-faces.png',(258,2054,1807,2453)),
       ('h904-numeral-cisi2-479.png','h904-numeral-metadata.png',(239,3576,1676,3806)),
       ('h904-numeral-m331-120.png','h904-numeral-m331-Bb.png',(186,1392,1659,2150))]

def pin(path):
 p=ROOT/path
 return {'path':path,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--render',action='store_true');args=parser.parse_args()
 base=ROOT/'results/primary_pages'
 if args.render:
  for src,pages,prefix in SOURCES:
   for page in pages:
    subprocess.run([str(PDFTOPPM),'-f',str(page),'-l',str(page),'-singlefile','-scale-to','4800','-png',str(ROOT/src),str(base/f'{prefix}-{page}')],check=True)
 crop_records=[]
 for src,out,box in CROPS:
  im=Image.open(base/src)
  assert max(im.size)==4800
  assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
  im.crop(box).save(base/out)
  crop_records.append({'source':'results/primary_pages/'+src,'output':'results/primary_pages/'+out,
                       'source_pixels':list(im.size),'box':list(box),'transforms':'native crop only; no flip, rotation, rescaling, contrast or restoration'})
 features=json.loads((ROOT/'data/processed/catalogue_features.json').read_text())
 candidate=[r for r in features if 'W900' in r.get('wells_graphemes',[])]
 assert len(candidate)==1 and candidate[0]['id']=='P154'
 assert not any('W899' in r.get('wells_graphemes',[]) for r in features)
 rows=[]
 for src in ['results/numeral_pair_source_rows.csv','results/numeral_source_records.csv']:
  with (ROOT/src).open() as stream:
   for row in csv.DictReader(stream):
    if any(v in ['1786.1','1786.2','2849.2'] for v in row.values()):
     rows.append({'source':src,'row':row})
 assert len(rows)==3
 # Independently reconstruct the split-value affine certificate, without any
 # import from analyze_numeral_identity_sensitivity or its polynomial helpers.
 sensitivity=json.loads((ROOT/'results/numeral_identity_sensitivity.json').read_text())
 expected_specs=[(2,(1,7),(0,4),(-1,1),4),(1,(3,7),(2,6),(1,5),6)]
 theory_checks=[]
 intersections=[]
 for row,(t0,L,S,a,b) in zip(sensitivity['families'],expected_specs,strict=True):
  # Pairs are constant and slope. vB is constant in these two exhibited families.
  residual_a=(L[0]+a[0]-2*S[0],L[1]+a[1]-2*S[1])
  residual_b=(b*L[0]-7*S[0]-4,b*L[1]-7*S[1])
  assert residual_a==residual_b==(0,0)
  bounds={'L_minus_10':(L[0]-10,L[1]),'S_minus_8':(S[0]-8,S[1]),
          'vA_minus_1':(a[0]-1,a[1]),'vB_minus_1':(b-1,0),
          'L_minus_vA_minus_1':(L[0]-a[0]-1,L[1]-a[1]),
          'S_minus_vA_minus_1':(S[0]-a[0]-1,S[1]-a[1]),
          'L_minus_vB_minus_1':(L[0]-b-1,L[1]),
          'S_minus_vB_minus_1':(S[0]-b-1,S[1])}
  canonical={k:[c,m] if m else [c] for k,(c,m) in bounds.items()}
  assert canonical==row['bound_polynomials_nonnegative_on_domain']
  assert all(m>=0 and c+m*t0>=0 for c,m in bounds.values())
  assert row['equation_residual_polynomials']==[[0],[0]]
  assert L[1]>0
  shared=Fraction(b-a[0],a[1]);assert shared.denominator==1 and shared>=t0
  assert row['vA_minus_vB_polynomial']==[a[0]-b,a[1]]
  assert row['parameterization']['shared_value_t']==int(shared)
  assert row['parameterization']['t_min']==t0
  assert row['parameterization']['L']==list(L) and row['parameterization']['S']==list(S)
  assert row['parameterization']['vA']==list(a) and row['parameterization']['vB']==[b]
  intersections.append({'L':L[0]+L[1]*int(shared),'S':S[0]+S[1]*int(shared),'v':b})
  for example in row['examples']:
   t=example['t'];assert t>=t0
   calculated={'L':L[0]+L[1]*t,'S':S[0]+S[1]*t,'vA':a[0]+a[1]*t,'vB':b}
   assert all(example[k]==v for k,v in calculated.items())
   assert example['shared_value']==(calculated['vA']==b)
  theory_checks.append({'t_min':t0,'residuals_affine':[list(residual_a),list(residual_b)],
       'bound_coefficients':canonical,'bound_values_at_t_min':{k:c+m*t0 for k,(c,m) in bounds.items()},
       'shared_value_t':int(shared),'strictly_increasing_L_slope':L[1]})
 assert sensitivity['shared_value_intersections']==intersections
 theory_hashes={p:pin(p)['sha256']==h for p,h in sensitivity['input_sha256'].items()}
 assert all(theory_hashes.values())
 result={
  'date':'2026-09-28','scope':'Local primary photograph and identity review, with separate conditional algebra sanity check',
  'identity':{'cisi':'H-904','excavation_printed':'J 213 D','finnish_concordance':'3477',
              'museum_field_printed':'HM 434, 32.3018','photograph_reference':'P 1213',
              'metadata_locator':{'volume':2,'printed':444,'pdf':479},
              'photo_locator':{'volume':2,'printed':338,'pdf':373},
              'key_locator':{'volume':2,'printed':434,'pdf':469},
              'secondary_excavation_raw':'J213 (D)477','appended_477_origin_authenticated':False,
              'figure16_id3786_identity_authenticated':False,'M77_text_reference_assigned':None},
  'local_face_joins':[{'local_row':'1786.1','cisi_face':'H-904 A'},
                      {'local_row':'1786.2','cisi_face':'H-904 B'},
                      {'local_row':'2849.2','cisi_face':'M-331 B','prior_join_reinspected':True}],
  'literal_source_records':rows,
  'visual_observations':{
   'H904_A':'Two tall uprights and two shorter right strokes with intervening compound; no numerical values assigned.',
   'H904_B':'Three tall uprights followed in displayed order by single angular right-bulging/open-left curve before crossed form; further residual signs retained.',
   'M331_B':'Single smoother right-bulging/open-left curve beside one shorter upright; lowercase b impression reverses order and curve.',
   'comparison':'Broad local graphic compatibility positively supported; fine terminal topology unresolved.',
   'capital_vs_lowercase_rule_verified':True,
   'perfect_glyph_identity_established':False,'essential_graphic_distinction_established':False,
   'all_edges_and_faint_strokes_certified_complete':False},
  'catalogue_candidate_only':candidate[0],'feature_W899_entry_present':False,
  'global_W899_W900_alias_established':False,'same_numeric_value_established':False,
  'numerical_operations_established':False,
  'algebra_sensitivity':{
   'conditional_equations':['vA = 2*S-L','vB*L+1 = 7*S+5'],
   'families':[{'t_min':2,'L':'7*t+1','S':'4*t','vA':'t-1','vB':'4'},
               {'t_min':1,'L':'7*t+3','S':'6*t+2','vA':'5*t+1','vB':'6'}],
   'symbolic_checks':['2*(4t)-(7t+1)=t-1','4*(7t+1)+1=7*(4t)+5',
                      '2*(6t+2)-(7t+3)=5t+1','6*(7t+3)+1=7*(6t+2)+5'],
   'proof_scope':'Removing shared numerical value permits infinite alternatives; not evidence actual signs or values differed.'},
  'independent_split_value_validation':{'producer_imported':False,'family_checks':theory_checks,
    'intersections':intersections,'input_hash_checks':theory_hashes,'mismatches':0,
    'exhaustive_parameterization_claimed':False},
  'source_code_discrepancy':{'capture':'data/raw/fuls-numeral-figure-primary-captures.json',
    'captured_prose_lines':[677,678],'source_description':'Sign032, three long strokes',
    'local_H904_B_three_strokes':'W033','local_H904_A_two_strokes':'W032',
    'cause_resolved':False,'source_sign900_equals_local_W900_by_number_alone':False,
    'M331_source_sign14_referent_reconciled':False},
  'attempts':[{'method':'retained multilingual OCR exact H904/J213 search','outcome':'no target match'},
              {'method':'adjacent known CISI2 H886–898 page visual bracket','outcome':'next PDF373 found H904A/B'},
              {'method':'CISI2 metadata PDF479 and column key','outcome':'exact H904/J213D row recovered'},
              {'method':'direct object-view comparison with M331 B/b','outcome':'broad graphic compatibility; no global alias or value'}],
  'crop_records':crop_records,'render_scale_long_edge':4800,'downloads':0,
  'established_semantic_values':0,'established_phonetic_values':0,
  'semantic_values':None,'phonetic_values':None,
 }
 paths=[src for src,_,_ in SOURCES]+[r[k] for r in crop_records for k in ['source','output']]+[
  'data/raw/h843_identity_CorpusVol2_djvu.txt','data/processed/m331_visual_evidence.json',
  'data/processed/catalogue_features.json','data/processed/numeral_equation_claims.json',
  'docs/NUMERAL_IMAGES.md','docs/NUMERAL_SCREEN.md','docs/H904_NUMERAL_GLYPH_REVIEW.md',
  'results/numeral_pair_source_rows.csv','results/numeral_source_records.csv',
  'results/primary_pages/h843-cisi2-key-469.png','results/primary_pages/h843-cisi2-key-28.png',
  'results/primary_pages/cisi1-28.png','results/h904-numeral-cisi2_extraction.json',
  'results/h904-numeral-m331_extraction.json',
  'data/raw/fuls-numeral-figure-primary-captures.json',
  'results/numeral_identity_sensitivity.json','scripts/analyze_numeral_identity_sensitivity.py',
  *sensitivity['input_sha256'],str(Path(__file__).resolve().relative_to(ROOT))]
 result['evidence_files']=[pin(p) for p in sorted(set(paths))]
 out=ROOT/'data/processed/h904_numeral_glyph_review.json';out.write_text(json.dumps(result,indent=2)+'\n')
 assert all(pin(x['path'])==x for x in result['evidence_files'])
 print(json.dumps({'output':str(out.relative_to(ROOT)),'pins':len(result['evidence_files']),
                   'H904_identity_recovered':True,'global_alias_or_value':False}))

if __name__=='__main__':main()
