"""Conditional richness estimators and finite-catalogue rarefaction, not decipherment.

N: occurrences; S: observed types; f_k: types appearing k times. Chao1 follows
Gotelli & Chao2013 eq7. Rarefaction eq2 samples tokens without replacement.
No archaeological independence, chronology, or script-type labels are inferred.
"""
from collections import Counter
import csv
import math
from common import ROOT,sha256,write_json,write_csv
from extract_primary_table import validate_rows


def positive_counts(values):
    if any(type(v) is not int or v < 0 for v in values):
        raise ValueError('Counts must be nonnegative integers')
    values=[v for v in values if v]
    if not values:raise ValueError('At least one positive count required')
    return values


def estimate(values):
    values=positive_counts(values); frequencies=Counter(values)
    n=sum(values); s=len(values); f1=frequencies[1]; f2=frequencies[2]
    unseen=f1*f1/(2*f2) if f2 else f1*(f1-1)/2
    return {'tokens':n,'observed_types':s,'singletons':f1,'doubletons':f2,
            'good_turing_unseen_token_mass':f1/n,
            'chao1_unseen_types':unseen,'chao1_total_types':s+unseen,
            'chao1_formula_branch':'f1_squared_over_2f2' if f2 else 'f1_times_f1_minus1_over2',
            'interpretation':'Model-dependent estimator; not a guaranteed lower bound on the historical inventory.'}


def rarefaction(values, sample_tokens):
    values=positive_counts(values);n=sum(values)
    if type(sample_tokens) is not int or not 0<=sample_tokens<=n:
        raise ValueError('Rarefaction requires an integer between0 and observed token count')
    # C(N-f,m)/C(N,m) = product_{j=0}^{f-1}(1-m/(N-j)).
    # log1p/expm1 avoids cancellation; no Monte Carlo or extrapolation.
    total=0.0
    for f,multiplicity in Counter(values).items():
        present=1.0 if sample_tokens>n-f else -math.expm1(sum(math.log1p(-sample_tokens/(n-j)) for j in range(f)))
        total+=multiplicity*present
    return total


def draw_chart(curve):
    from pathlib import Path
    import reportlab
    from reportlab import rl_config
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    rl_config.invariant=1
    fonts=Path(reportlab.__file__).parent/'fonts'
    pdfmetrics.registerFont(TTFont('InventoryVera',str(fonts/'Vera.ttf')))
    pdfmetrics.registerFont(TTFont('InventoryVeraBold',str(fonts/'VeraBd.ttf')))
    from reportlab.graphics.shapes import Drawing,String
    from reportlab.graphics.charts.lineplots import LinePlot
    from reportlab.graphics import renderPDF
    from reportlab.lib.colors import HexColor
    d=Drawing(650,420)
    d.add(String(40,394,'M77: expected sign types in a random token subset',fontName='InventoryVeraBold',fontSize=14))
    chart=LinePlot();chart.x=62;chart.y=72;chart.width=548;chart.height=285
    chart.data=[[(r['sample_tokens'],r['expected_observed_types']) for r in curve]]
    chart.lines[0].strokeColor=HexColor('#176b91');chart.lines[0].strokeWidth=2
    chart.xValueAxis.valueMin=0;chart.xValueAxis.valueMax=13372
    chart.xValueAxis.valueSteps=[0,2000,4000,6000,8000,10000,12000,13372]
    chart.xValueAxis.labels.fontSize=9
    chart.xValueAxis.labels.fontName='InventoryVera'
    chart.yValueAxis.valueMin=0;chart.yValueAxis.valueMax=450
    chart.yValueAxis.valueSteps=[0,100,200,300,400];chart.yValueAxis.labels.fontSize=9
    chart.yValueAxis.labels.fontName='InventoryVera'
    d.add(chart)
    d.add(String(195,42,'Sign occurrences sampled without replacement',fontName='InventoryVera',fontSize=11))
    d.add(String(62,367,'Expected distinct M77 sign IDs',fontName='InventoryVera',fontSize=10))
    d.add(String(40,17,'Finite-catalogue interpolation only; no unseen-type prediction or confidence band.',fontName='InventoryVera',fontSize=9))
    renderPDF.drawToFile(d,str(ROOT/'results/inventory_rarefaction.pdf'))


def main():
    path=ROOT/'data/processed/mahadevan_1977_table_i.csv'
    rows=list(csv.DictReader(path.open()));validate_rows(rows)
    counts=[int(r['total']) for r in rows];n=sum(counts)
    summary=estimate(counts)
    points=sorted({0,1,100,500,1000,n//4,n//2,3*n//4,n,*[round(n*i/80) for i in range(81)]})
    curve=[{'sample_tokens':m,'expected_observed_types':rarefaction(counts,m)} for m in points]
    sources=['data/processed/mahadevan_1977_table_i.csv','data/raw/mahadevan_1977_text.pdf',
             'data/raw/inventory-oct10-gotelli-chao2013-www.pdf','data/raw/inventory-oct10-drukh-mansour2005.pdf']
    report={'research_date':'2026-10-10','source_pins':[{'path':p,'sha256':sha256(ROOT/p)} for p in sources],
       'full_table':summary,'frequency_spectrum':dict(sorted(Counter(counts).items())),
       'position_strata':{k:estimate([int(r[k]) for r in rows]) for k in ['solus','initial','medial','final']},
       'synthetic_exact_duplication':{'description':'Counterexample sensitivity only, not a second historical sample. Every original occurrence is copied once.',
                                    'result':estimate([2*c for c in counts]),'relative_frequencies_unchanged':True},
       'type_label_permutation_check':estimate(list(reversed(counts)))==summary,
       'terminal_rarefaction_increment':rarefaction(counts,n)-rarefaction(counts,n-1),
       'rare_type_sensitivity':[
         {'scenario':'All112 singleton sign classes omitted entirely; extreme recoding/error scenario, not a proposed correction.',
          'result':estimate([c for c in counts if c>1])}],
       'limitations':['Repeated inscriptions, formulaic dependence and collection selection violate a simple iid interpretation.',
         'The closed M77 codebook has417 entries by definition; Chao1 here concerns a hypothetical larger population classified consistently, not hidden codebook entries.',
         'M77 sign normalization defines the type inventory; another sign-splitting convention changes the estimand.',
         'Good-Turing estimates probability mass; Chao1 estimates type richness. Their denominators differ.',
         'No confidence interval is justified for the archaeological population from these aggregate counts alone.',
         'Positional-stratum estimates cannot be added; types overlap and populations differ.',
         'Rarefaction is finite-catalogue interpolation. It is not chronological growth or a cross-script comparison.',
         'Permuting sign labels leaves every reported statistic unchanged; these summaries cannot identify sign meanings.',
         'No phonetic/semantic value or script-type classification follows.'],
       'method_locators':{'chao1':'Gotelli & Chao2013, printed200/PDF7 eq7',
         'rarefaction':'same, printed199/PDF6 eq2','good_turing':'Drukh & Mansour2005, printed1232/PDF2 section1.1; iid model on1233/PDF3'}}
    write_json('results/inventory_richness.json',report)
    write_csv('results/inventory_rarefaction.csv',curve)
    draw_chart(curve)
    print(summary)

if __name__=='__main__':main()
