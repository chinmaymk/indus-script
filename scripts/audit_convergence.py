"""Verify final primary reviews, historical pins, crops and conditional graph."""
import json
from PIL import Image
from common import ROOT,sha256,write_json

def main():
    paths=['data/processed/balanced_tablet_primary_review.json','data/processed/h1923_report_search.json',
           'data/processed/research_route_audit.json','results/numeral_class_constraints.json',
           'data/processed/h1923_report_new_sources.json']
    values=[json.loads((ROOT/p).read_text()) for p in paths];pins=set()
    oldlog=next(p['sha256'] for p in values[2]['source_pins'] if p['path']=='docs/RESEARCH_LOG.md')
    def verify(path,h,size=None):
        actual='results/research_route_audit_log_input.md' if path=='docs/RESEARCH_LOG.md' and h==oldlog else path
        assert sha256(ROOT/actual)==h,actual
        if size is not None: assert (ROOT/actual).stat().st_size==size,actual
        pins.add(actual)
    def visit(x):
        if isinstance(x,dict):
            if 'path' in x and 'sha256' in x:verify(x['path'],x['sha256'],x.get('bytes'))
            for p,h in x.get('input_sha256',{}).items():verify(p,h)
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    for v in values:visit(v)
    review=values[0];graph=values[3]
    for crop in review['crop_records']:
        with Image.open(ROOT/crop['source']) as src,Image.open(ROOT/crop['output']) as dst:
            expected=src.crop(crop['box'])
            assert (expected.mode,expected.size,expected.tobytes())==(dst.mode,dst.size,dst.tobytes())
    independent=review['independent_graph_check']
    assert independent['mismatches']==0 and not independent['producer_imported']
    assert not review['equal_represented_quantities_established']
    assert not graph['all_source_records']['positive_solution_exists']
    assert graph['without_unverified_H1923']['normalized_component_values']=={'W700:long':'1','W840:long':'3/2','W840:stacked':'1'}
    assert not graph['without_H1923_but_equating_long_and_stacked']['positive_solution_exists']
    write_json('results/convergence_audit.json',{'verified_pins':len(pins),'exact_crops':len(review['crop_records']),
      'independent_graph_mismatches':0,'semantic_values_assigned':0,
      'scope':'Integrity and conditional equations; not proof of any ancient reading.',
      'input_sha256':{p:sha256(ROOT/p) for p in paths}})
    print(f'Convergence audit: {len(pins)} pins, {len(review["crop_records"])} exact crops; independent graph agrees.')
if __name__=='__main__':main()
