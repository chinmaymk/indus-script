# What the metal-tool numerals can and cannot identify

The recovered drawings support the proposed stroke counts on three Mohenjo-daro
tools. Those counts do **not** select base eight. Under an explicitly stated
carrying convention, every integer base of eight or greater fits the nine proposed
expressions. A separate calculation rejects a shared, regularly carried weight
code for the two surviving axe masses. Unknown original masses leave that broader
interpretation unresolved.

These are conditional mathematical results about selected expressions. They do
not translate the full inscriptions or assign meanings to the 417 signs.

## Evidence and scope

The [original-plate audit](METAL_PLATE_AUDIT.md) distinguishes published drawings
from surface photographs. Plate CXXVI shows one arch, five upright strokes and
four transverse strokes on item 2; six upright strokes on item 3; and seven arches
with six upright strokes on item 5. The parent researcher independently inspected
the full drawing and all three crops after the plate audit. Neither review was
blinded to the proposed counts. The small axe has an adjoining complex sign, so
extracting `6i` as a complete numerical expression remains an assumption.

The [original records](METAL_ORIGINAL_RECORDS.md) supply the masses and document
unquantified chemical-cleaning losses. Plate/item joins are stronger than the
unresolved large-axe field number, printed 7535 in the primary catalogue and 7835
in the later study. We preserve both. Local `t,i,u,x` are analytical shape labels,
not authenticated Mahadevan sign identities or phonetic values.

The nine expressions, taken from the previously checked Pettersson table, are
`2x+3u`, `3u+5i`, `4i+4t`, `7i+4t`, `6i`, `u+5i+4t`, `7u+6i`,
the uncertain K-121 `u`, and K-122 `5i`. The source questions some marks; alternative
K-121 readings `2u` and `u+2i` are retained. This is not nine newly authenticated
artifact readings. See the [input ledger](../data/processed/metal_tool_weight_anchors.json)
and [new source review](../data/processed/metal_numeral_convention_review.json).

## Count patterns allow infinitely many bases

Assume ordered denominations `t<i<u<x`, integer ratios between consecutive units,
and canonical carrying: each lower coefficient is smaller than the ratio to the
next denomination. No upper denomination is invented above `x`.

For a uniform integer base R, choose `(t,i,u,x)=(1,R,R²,R³)`. The largest observed
lower coefficients are 4 for t, 7 for i, and 7 for u. Consequently every expression
is canonical **if and only if R≥8**. There is no upper bound. This proof covers
both K-121 alternatives too. Without canonical carrying, even that lower bound
does not follow from the counts alone.

The implementation constructs bases 8, 9, 10 and 12 and the mixed system
`(1,8,80,800)`. The mixed system satisfies `4t=i/2` while `u/i=10`.
Thus interpreting four transverse strokes as a half-unit still does not establish
a uniform base unless equal ratios between successive denominations are assumed.
The recurring four-stroke group itself does not prove a half-unit interpretation;
a nonnumerical marker remains possible. No probability is assigned to missing
eight- or nine-stroke groups without a justified model of how amounts were sampled.

## The axe–chisel pair does not remove that ambiguity

For the rounded large-axe mass M=1910g and surviving tang mass m=165g, let
`b=u/i` and `c=i/t`. The proposed large-axe expression fixes

```
i = M/(7b+6)
required whole-chisel / tang ratio = M(b+5+4/c) / [m(7b+6)].
```

The following ratios all satisfy the hypothetical strict upper limit of 2.6:

| b=u/i | c=i/t | Required ratio |
|---:|---:|---:|
|8|8|2.520528|
|9|9|2.423266|
|10|10|2.345614|
|12|12|2.229405|
|10|8|2.360845|

This extends to **every uniform R≥8**. Apart from the positive factor M/m,
the ratio is `(R²+5R+4)/(7R²+6R)`. Its derivative has numerator
`−(29R²+56R+24)`, so it decreases for R>0; its value at eight already lies below
2.6. The 2.6 bound is a reconstruction assumption, not a measured original mass.

The earlier [weight audit](WEIGHT_ANCHORS.md) found base ten failed when **t=i**.
There is no contradiction: that test used c=1; this countermodel uses c=10.
Changing an assumption changes the fitted model. Neither calculation establishes
the value of a transverse stroke.

## Two surviving axe masses contradict regular carrying

Use the primary recorded metric masses s=262.233g and M=1910.030g, with the
proposed complete expressions `6i=s` and `7u+6i=M`. Exact arithmetic gives

```
i = s/6 = 43.7055g
u/i = 6(M−s)/(7s) = 3295594/611877 ≈ 5.386040.
```

Under canonical integer carrying, the six i signs on the large axe alone require
u/i≥7. That would require M≥55s/6=2403.8025g, exceeding the recorded mass by
493.7725g. The complete nine-expression convention requires u/i≥8 and
M≥62s/6=2709.741g, a discrepancy of 799.711g. This contradiction needs no
chisel reconstruction.

The conclusion is restricted to **shared units, the proposed segmentation,
canonical carrying and the surviving masses as exact encoded quantities**.
The source decimals are not a claim of milligram precision. More consequentially,
chemical losses are documented but unmeasured. Original masses, different sign
grouping, noncanonical repetition or another denotation change the hypothesis.
The calculation does not disprove all numerical interpretations.

## Why unrestricted damage corrections cannot decide

There is also a general proof of non-identifiability. For any positive proposed
quantities q_j and surviving masses m_j, choose

```
s = max_j(m_j/q_j)
L_j = s q_j − m_j.
```

Every L_j is nonnegative, and every surviving mass is reproduced by subtracting
L_j from the invented original mass s q_j. Therefore, if each object is allowed
an arbitrary unmeasured loss, **any positive unit system can be made to fit**.
The script demonstrates this for bases eight and ten on five reported masses.
These are overfitting examples, not estimates of archaeological damage; the
chisel geometry limit is not imposed in this demonstration.

A discriminating mass test would need independent restrictions on original mass
or loss, secure segmentation and unit comparability. Reconstructing each object's
loss to obtain a desired base supplies no such test.

## Reproduction

[`audit_metal_numeral_conventions.py`](../scripts/audit_metal_numeral_conventions.py)
uses exact fractions, verifies source/image fingerprints, checks its expressions
against the earlier ledger, and writes
[`metal_numeral_conventions.json`](../results/metal_numeral_conventions.json).
Five focused tests cover carrying boundaries, the mixed-ratio counterexample,
distinct pair calibrations, contradictory and feasible axe controls, and free-loss
reconstruction. It runs in `scripts/run_all.py`.

This work strengthens the evidence for the drawn patterns and excludes particular
weight models. It establishes no new semantic or phonetic assignment.
