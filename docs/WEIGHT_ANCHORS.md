# Physical weights as possible numerical anchors

The reviewed evidence does not establish a numerical value for an Indus sign.
It does yield exact constraints on a specific metal-tool interpretation, including
an algebra correction and an incompatible three-object mass model. All quantities
below are conditional on the proposed readings; they are not a translation.

**Source follow-up:** the [original-record and photo audit](TOOL_RECORD_FOLLOWUP.md)
now verifies the262.233g primary small-axe mass, exposes primary field7535 versus
later7835, and authenticates the two Kalibangan object joins. Calculations below
retain the later paper's inputs; the follow-up computes primary-mass sensitivity
separately and preserves the unresolved identifier and reading issues.

## What the sources actually connect

| Route | Result | Evidence |
| --- | --- | --- |
| Harappan stone weights | Measured masses without authenticated ancient Indus inscriptions on the reviewed objects | [Excavation review](INSCRIBED_WEIGHT_SEARCH.md) |
| Kenoyer's two early weights | 1.7 g and 102.95 g; nearby seals do not label the weights | [Bounded text ledger](../data/processed/kenoyer_weight_anchor_review.json) |
| Ur and Bahrain weights | Three identified objects; reported Mesopotamian numerical marks on one, no demonstrated Indus sign/value join | [Imported-weight review](DILMUN_WEIGHT_ANCHORS.md) |
| Inscribed metal tools | Nine listed objects, five reported surviving masses; uncertain segmentation and reconstructed original masses | [Primary-paper review](METAL_TOOL_WEIGHT_ANCHORS.md) |

These are bounded reviews. They do not establish that no inscribed Harappan weight
exists. Susa stroke-mark examples and a separate cuneiform Dilmun conversion tablet
cannot be silently assigned to Indus inscriptions. The downloaded originals and
clearly labeled text captures are all in `data/raw/`, with hashes in
[`data/sources.json`](../data/sources.json).

## An exact contradiction for surviving metal-tool masses

Pettersson's [1999 paper](https://insa.nic.in/writereaddata/UpLoadedFiles/IJHS/Vol34_2_1_JSPettersson.pdf),
printed pp.98–101, provides the following proposed expressions and reported masses.
The variables are **the paper's local notation**, without an authenticated mapping
to Mahadevan sign IDs.

| Object | Proposed expression | Surviving mass |
| --- | --- | ---: |
| DK-7856, broken chisel tang | u + 5i + 4t | 165.343 g |
| DK-7835, axe | 7u + 6i | 1910.030 g |

If the expressions add positive mass units and label the surviving pieces, seven
times the first equation minus the second requires

```text
29i + 28t = 7(165.343) − 1910.030 = −752.629 g.
```

The left side is nonnegative when i,t ≥ 0; the right side is negative. This is an
exact contradiction, unaffected by rounding both masses to 165 and 1910 g.
It rejects this narrow present-mass model. The original whole chisel was heavier
than its surviving tang, and corrosion/chemical treatment changed the tools;
the contradiction does not reject every possible original-mass interpretation.
The paper itself discusses the negative-value problem; this audit supplies a
reproducible certificate, not a claim to first notice it.

## Correcting the reconstructed-chisel constraint

The author instead hypothesizes that the whole chisel weighed less than 2.6 times
the surviving tang, based on comparisons of tool geometry. Using the paper's
rounded masses gives:

```text
u + 5i + 4t < 429;  7u + 6i = 1910
29i + 28t < 1093
i + (28/29)t < 1093/29.
```

The printed p.99 coefficient **4/29 should be 28/29**. The retrieved official
indexed [errata](https://kau.diva-portal.org/smash/get/diva2%3A593951/ERRATA01.pdf)
do not list this correction; PDF bytes of that errata were unavailable and the
local artifact is explicitly a text capture.

With the additional assumption t=i>0, the corrected bounds are **i<19.17544 g**,
**u>256.42105 g**, and **u/i>13.37237**, rather than the paper's i<33.13 g.
Using the more precise reported masses gives i<19.28444 g and u/i>13.29217.
These are algebraic bounds under a reconstruction, not measured uncertainties.

For t=i and a fixed ratio u/i of 8, 10 or 16, the required whole-chisel/tang mass
ratios are respectively 3.1740, 2.8939 and 2.4525 using rounded masses. Thus the
first two fail the assumed <2.6 bound; the third is compatible with this pair.
Compatibility does not establish base 16 or any other base. Different t/i,
different original masses or a different meaning of the marks change the test.

## A third object and the cost of alternative readings

The table's DK-7855 axe reportedly weighs 262 g and has six strokes alongside
other signs. If those six strokes alone denote its full mass, then 6i=262.
Combining that with 7u+6i=1910 yields i=131/3 g and u=1648/7 g. Consequently,
for t≥0 the chisel must weigh at least **9529/21 = 453.76190 g**. That exceeds
429 g; its required mass ratio is at least 2.75007. The reported-precision
variant also fails the 2.6 bound. This quantifies the conflict already noted by
the author on p.101; it depends on a disputed separation of six strokes from
adjacent signs. See the [independent arithmetic crosscheck](METAL_TOOL_THREE_OBJECT_CHECK.md).

Kalibangan K-121 and K-122 illustrate the competing choices. Their reported
210 g and 476 g masses give u/i=75/68, 75/34 or 7/34 under three proposed
segmentations. Each merely calibrates two unknowns on two objects. Changing the
second object's original mass to an assumed 500 g produces the attractive ratio
i/u=10 for one reading, but that extra 24 g is unmeasured. No independent
prediction selects that fit.

## Reproduction and consequence

[`audit_metal_weight_anchors.py`](../scripts/audit_metal_weight_anchors.py) uses exact
rational arithmetic, verifies evidence hashes and writes
[`metal_weight_anchor_audit.json`](../results/metal_weight_anchor_audit.json).
Four focused tests cover the contradiction and a feasible control, strict-bound
behavior, precision sensitivity and the three-object conflict. The script is part
of `scripts/run_all.py`. The [input ledger](../data/processed/metal_tool_weight_anchors.json)
preserves all nine table rows, ambiguous readings and missing masses.

The useful conclusion is a restriction: an unadjusted universal positive additive
weight code cannot fit this selected set of expressions and mass assumptions.
Quantity notation remains plausible in some contexts, but physical masses have
not established any sign value here. All 417 semantic and phonetic assignments
remain unresolved. A stronger test requires verified tool photographs, original
excavation mass records and a justified damage model, with further objects reserved
for prediction rather than calibration.

The subsequent [plate audit](METAL_PLATE_AUDIT.md) checks the three published
drawings, and the [numeral-convention study](METAL_NUMERAL_IDENTIFIABILITY.md)
proves that counts alone admit every uniform integer base≥8 under canonical
carrying. Its pair calibrations use i/t=R, unlike the t=i assumption tested here.
It also gives a two-axe contradiction without a chisel reconstruction and a proof
that unrestricted per-object loss cannot identify a unit system. The historic
equations and input assumptions in this report remain separate.


## Signed contributions and the original metric masses

A later sensitivity check now uses all three original printed metric masses,
including small axe262.233g, rather than the table's rounded262g. The existing
`reported_precision` branch preserves its historical mixed-precision inputs;
`original_metric` names the new branch explicitly. These printed decimals do not
establish milligram measurement accuracy.

Allowing signed contributions solves the three assumed complete expressions:

```
6i = 262.233
7u + 6i = 1910.030
u + 5i + 4t = 165.343

i = 87411/2000 = 43.7055
u = 1647797/7000 ≈ 235.399571
t = -4040177/56000 ≈ -72.146018
```

All three residuals are exactly zero. Thus the nonnegative contradiction is not
an algebraic impossibility after negative t is allowed. Negative i cannot rescue
this particular three-object model: its first equation forces i>0. The fit also
has t≠i. It adds a subtractive interpretation, not an independent observation of
ancient subtraction. Three free values fitted to three equations provide zero
independent validation equations. Uninterpreted neighboring signs, original mass
loss and uncertain segmentation remain outside this calculation.

With t≥0, the same original-metric inputs instead give tang-expression mass
at least6354979/14000≈453.927071g, or2.745366times its surviving mass. This still
exceeds the hypothetical strict2.6cap. The signed solution matches the surviving
fragment; it does not reconstruct the lost original chisel. See the
[independent signed-model review](THREE_TOOL_SIGNED_MODEL_REVIEW.md).


Allowing a free aggregate contribution r from the small axe's other signs changes
its equation to6i+r=262.233. The script also reproduces the independent review's
counterexample i=−30,u=209003/700,t=117371/28000,r=442233/1000. All mass residuals
vanish, and u,t,r are positive. Thus even the negative-i exclusion depends on
omitting those signs' contributions. This is a deliberately underdetermined
four-parameter model with three equations; r is fitted, not observed or read.
