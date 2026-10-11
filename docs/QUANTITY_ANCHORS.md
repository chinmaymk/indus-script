# Quantity hypotheses: what would identify a number?

**Result: quantity notation remains a reasonable partial hypothesis, but the
examined arguments do not uniquely establish decimal values, litres, or words.**
This analysis supplements the distributional evidence without importing a proposed
translation into the corpus.

## Evidence ledger

[Rao's 2018 paper](https://arxiv.org/abs/1812.00049) proposes rationing uses for
repeated miniature-tablet inscriptions. Its group of sixteen tablets and Figure 5
were examined visually. Repetition and handwriting variation are observations;
the occupation and ration readings are hypotheses. The plain U shape resembles
M328, not the distinct M342 jar form. This is a candidate visual identification,
not an authenticated crosswalk. Rao's capacity estimate depends on Wells, so these
are not two independent calibrations. Figure 7's schematic includes open-ended
categories; a fixed exhaustive grammar would be needed to test all inscriptions.

[Wells 2015](https://ru.scribd.com/document/1007007442/The-Archaeology-and-Epigraphy-of-Indus-Writing-Bryan-K-Wells-Andreas-Fuls-Archaeopress-Publishing-Ltd-Oxford-2015-Archaeopress-Publishing),
pp. 60–63, proposes a capacity calibration from three pots. The public text was
read, but its measurement-table cells were unavailable in the extracted text.
We therefore have no independently checked volume dataset to fit. A subsequent
[source recovery and conditional fit](CAPACITY_MODELS.md) uses an earlier Fuls
table, explicitly preserving its unverified layout and conflicting identifiers;
it does not fill the missing Wells2015 table. His bangle
argument, pp. 94–95, supplies an uncertain reconstruction interval rather than an
exact observed total. See the [factual ledger](../data/processed/quantity_anchor_ledger.json)
for source locators and explicit dependencies. Numerical claims there are conditional
inputs, not established observations by this project.

### Primary-context check

The [original field report](https://ignca.gov.in/Asi_data/74331.pdf) separates two
objects. Halim and Vidale associate at least 83 bangle fragments with **jar G**
(printed pp. 75, 77; Figures 40–41); they had not systematically restored them.
The photographed unicorn sealing belongs to **jar E** (p. 82; Figures 55–56).
Jar E's surviving primary deposit is described separately (p. 78). Franke also
identifies E as the jar with the readable impression (p. 118).
These pages were visually checked against the saved scan.

**Our inference:** this report does not verify a link between that sealing and that
fragment group. Later documentation could change the assessment; no such bridge
has been checked here. Do not merge the jars or promote a reconstructed total into
an exact external anchor. The calculations below remain conditional even if the
published interval is accepted.

## Proof 1: capacity fits cannot resolve numerical scale

Suppose a proposed numerical value is nᵢ and measured capacity is Vᵢ. A model
predicts Vᵢ ≈ u nᵢ, with unknown unit size u. For every k > 0,

```
nᵢ′ = k nᵢ,     u′ = u/k,     u′ nᵢ′ = u nᵢ.
```

Every predicted capacity, residual and likelihood based only on these predictions
is unchanged. This remains true with noisy measurements and through-origin least
squares. Multiplying a stroke value by ten and dividing the unit size by ten is
observationally equivalent in this model. Relative proportionality can be tested;
an independently known count or unit convention must fix absolute numerical scale.
This is a symmetry of the specified model, not proof that quantity readings are false.

The saved script demonstrates the identity with exact rational arithmetic on
explicitly **synthetic** capacities. No invented values fill the missing source table.

## Proof 2: an unknown photographic scale cannot confirm its assumed capacity

For fixed dimensionless vessel geometry from an image, let C > 0 absorb the shape
and pixel dimensions. If linear scale is s, volume is V = C s³. A proposed count n
and unit u can always be made to fit by choosing

```
s = (n u / C)^(1/3).
```

Thus selecting a photographic scale from the proposed capacity and then recovering
that capacity is circular. Doubling u changes the fitted linear scale by 2^(1/3),
about 1.260. Independent scale information would break this freedom. A labelled
ruler, known vessel dimensions or a securely documented scale bar would provide
that information; an unlabelled bar chosen to make the volume agree would not.

## Proof 3: an interval-compatible total is not a unique decipherment

Conditionally suppose an inscription has one long stroke and seven short strokes,
denotes its container's item count additively, and the actual total is in [15,20].
Let a and b be positive integer values per long and short stroke. Then

```
15 ≤ a + 7b ≤ 20.
```

All solutions are:

| Assumed short-stroke value b | Compatible long-stroke values a |
|---|---|
| 1 | 8, 9, 10, 11, 12, 13 |
| 2 | 1, 2, 3, 4, 5, 6 |

There are twelve assignments; ten remain if a > b is required. Even fixing b = 1
leaves six possibilities. The decimal pair (10,1) fits, while (1,1) does not.
These are conditional eliminations, not probabilities over ancient numeral systems.
There is no justification here for a uniform prior over these possibilities.

Even an exact total of seventeen would require b = 1 or another constraint to
identify a uniquely. And two stroke types with additive weights do not establish
positional place-value notation: that needs evidence that a symbol's numerical
contribution changes with position. Reconstructing damaged signs or assigning all
fragments to contents adds archaeological uncertainty beyond this simple model.

## Reproduction and next evidence

- [Calculation script](../scripts/audit_quantity_anchors.py)
- [All candidate weights and exact symmetry check](../results/quantity_anchor_audit.json)
- [Tests](../tests/test_quantity_anchors.py)
- [PDF extraction/rendering script](../scripts/inspect_research_pdf.py)

`python3 scripts/audit_quantity_anchors.py` is part of the offline pipeline.
The optional PDF inspection helper requires pypdf, Poppler and, for OCR, Tesseract.
Source PDFs stay in `data/raw/`; rendered and extracted derivatives stay in `results/`.

Useful next evidence is artifact-level linkage between a checked inscription and
independently reconstructed contents, followed by another container whose count
was not used to select the numerical rule. For capacity, recover the actual
measurement table and independently scaled vessels, record model uncertainty,
freeze the calibration, and predict new examples. No semantic or phonetic value
for any of the 417 signs becomes established by the calculations here.
