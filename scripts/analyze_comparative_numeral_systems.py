"""Exact, bounded comparison of source-reviewed numerical graphs."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def pin(path):
    b = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def main():
    systems = {
        "PC_S": {"N1":F(1), "N14":F(10), "N34":F(60), "N48":F(600), "N45":F(3600), "N50":F(36000)},
        "PC_B": {"N1":F(1), "N14":F(10), "N34":F(60), "N51":F(120), "N54":F(1200), "N56":F(7200)},
        "PC_SE": {"N39":F(1,5), "N1":F(1), "N14":F(6), "N45":F(60), "N34":F(180), "N48":F(1800)},
    }
    for sign, denominator in {"N24":2,"N26":3,"N28":4,"N29":5,"N30a":6,"N30c":10}.items():
        systems["PC_SE"][sign] = systems["PC_SE"]["N39"] / denominator
    graphs = {}
    for name, values in systems.items():
        order = sorted(values, key=values.get)
        graphs[name] = {"values_relative_to_N1": {k:str(v) for k,v in values.items()}, "derived_ascending_edges": [{"low":a,"high":b,"ratio":str(values[b]/values[a])} for a,b in zip(order,order[1:])], "ordered_pairs_examined":len(values)*(len(values)-1), "two_thirds_pairs":[{"numerator":a,"denominator":b,"ratio":str(values[a]/values[b])} for a in values for b in values if a!=b and values[a]/values[b]==F(2,3)]}
    assert graphs["PC_S"]["two_thirds_pairs"] == graphs["PC_B"]["two_thirds_pairs"] == []
    assert {(x["numerator"],x["denominator"]) for x in graphs["PC_SE"]["two_thirds_pairs"]} == {("N26","N24"),("N30a","N28")}
    assert systems["PC_S"]["N14"]/systems["PC_S"]["N1"] == 10
    assert systems["PC_SE"]["N14"]/systems["PC_SE"]["N1"] == 6
    assert sum([520,80,720,60]) == 1380
    evidence = [pin(p) for p in ["data/raw/comparative-numerals-oct10-englund2004a.pdf", "data/raw/comparative-numerals-oct10-englund2004c.pdf", "results/comparative_numerals_pc-10.png", "results/comparative_numerals_pc-11.png", "results/comparative_numerals_pe-08.png", "docs/COMPARATIVE_NUMERAL_SYSTEMS.md", "scripts/analyze_comparative_numeral_systems.py"]]
    result = {"date_local":"2026-10-10", "graphs":graphs, "figure_locators":{"PC_S":"Englund2004a p32/PDF10 Fig4a", "PC_B":"Englund2004a p32/PDF10 Fig4a", "PC_SE":"Englund2004a p33/PDF11 Fig4b", "PE":"Englund2004c p107/PDF8 Fig5.4"}, "PE_relative_value_levels":{"S":[1,10,60,600,3600],"B":[1,10,60,120,1200],"D":[1,10,100,1000,10000]}, "PE_source_reported_sum":{"locator":"Englund2004c p113/PDF14, Scheil1935 no27", "terms":[520,80,720,60],"total":1380,"fresh_tablet_collation":False}, "excluded_ambiguity":{"PC_S_N8":["1/2","1/10"]}, "Indus_comparison":{"conditional_ratio":"2/3", "mapping_to_foreign_signs":None,"distinctive_cultural_fingerprint":False,"heldout_equation":"2*stacked_count - 3*long_count = 0", "eligibility":"Independent equal-quantity premise; fixed marker/context, class crosswalk and physical-artifact holdout; no fitted residual contributions", "validation_executed":False, "all417_readings_established":False}, "evidence":evidence}
    (ROOT/'results/comparative_numeral_systems.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'data/processed/comparative_numeral_systems.json').write_text(json.dumps(result,indent=2)+'\n')
    sources=[]
    for suffix in ['a','c']:
        meta=json.loads((ROOT/f'data/processed/fetch_comparative-numerals-oct10-englund2004{suffix}_pdf.json').read_text())
        for path,kind in [(meta['path'],'original_public_research_PDF'),(meta['header_artifact']['path'],'locally_serialized_HTTP_response_headers')]:
            row=pin(path);row.update(url=meta['url'],research_date='2026-10-10',kind=kind,original_document_bytes=path.endswith('.pdf'));sources.append(row)
    row=pin('data/raw/comparative-numerals-oct10-web-capture.json');row.update(url=None,source_urls=['https://cdli.earth/files-up/publications/englund2004a.pdf','https://cdli.earth/files-up/publications/englund2004c.pdf'],research_date='2026-10-10',kind='web_tool_capture_not_original_document',original_document_bytes=False,refetchable=False);sources.append(row)
    (ROOT/'data/processed/comparative_numerals_oct10_new_sources.json').write_text(json.dumps({'sources':sources},indent=2)+'\n')
    print(json.dumps({'systems':len(graphs),'pairs_examined':sum(x['ordered_pairs_examined'] for x in graphs.values()),'two_thirds_matches':sum(len(x['two_thirds_pairs']) for x in graphs.values()),'raw_sources':len(sources)}))

if __name__=='__main__':main()
