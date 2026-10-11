# Signed three-tool mass model: independent review

A common signed additive model fits the three assumed exact surviving-mass
equations uniquely, but requires **positive i and negative t**. Allowing a negative
i alone therefore does not rescue this particular three-object model. Allowing
unrestricted signed parameters does rescue it algebraically; this must not be
reported as rejection of every signed system.

The selected expressions are interpretive inputs. The original reported metric
masses in `metal_original_records.json` are 262.233 g for CXXVI.3, 1910.030 g for
CXXVI.5 and 165.343 g for the surviving CXXVI.2 tang. Taking these decimal literals
as exact for this conditional calculation gives:

```
6i = 262.233
7u + 6i = 1910.030
u + 5i + 4t = 165.343
```

The triangular system has a nonzero determinant and the unique solution:

| Parameter | Exact grams | Decimal grams |
|---|---:|---:|
| i | 87411/2000 | 43.7055 |
| u | 1647797/7000 | 235.399571428571… |
| t | −4040177/56000 | −72.146017857142… |

Direct substitution makes all three residuals exactly zero. This is a saturated
three-equation, three-parameter fit, with no independent validation equation.
A negative fitted contribution is permitted when the model explicitly allows
subtraction; its sign alone is not a contradiction in that enlarged model.

Eliminating u from the large axe and tang gives `29i + 28t = −752.629`.
If t≥0, this pair requires `i ≤ −752629/29000 ≈ −25.95272414 g`.
The small-axe equation instead forces i=43.7055 g, so the particular option
**negative i with nonnegative t** cannot satisfy all three exact equations.
If t=i is additionally imposed, the unique signed solution above does not satisfy
that constraint either. These are model comparisons, not identified ancient values.

At t=0 the two axes imply a minimum chisel contribution
`u+5i = 6354979/14000 ≈ 453.92707143 g`. It exceeds the surviving tang by
`4040177/14000 ≈ 288.58407143 g`; the fitted four-t term is exactly the negative
of that gap. If the independent premise of the disputed 2.6-times reconstruction
is added, its cap is 429.8918 g, still smaller than the nonnegative-t lower bound
by `1682469/70000 ≈ 24.03527143 g`. None of these differences estimates real damage.

## Premises and a residual-sign counterexample

The equations assume a shared scalar contribution for each proposed unit, additive
composition, the selected segmentation, no contribution from the other visible
complex signs, and equality to present surviving mass. They are not literal
translations of every sign on every face. In particular, the small axe has other
signs; setting their contribution to zero is a substantive premise.

If a free additive contribution r is allowed for those other small-axe signs,
then `6i+r=262.233` no longer fixes i. For example:

```
i = −30
u = 209003/700
 t = 117371/28000
r = 442233/1000
```

These values satisfy `6i+r=262.233`, `7u+6i=1910.030` and
`u+5i+4t=165.343` exactly, with u,t,r positive and i negative. Thus adding a free
residual can restore the subtractive-i option. This is an intentionally
underdetermined counterexample, not a reading or evidence that any complex sign
denotes 442.233 g. The example keeps all other residual contributions zero and
needs no claim about how they would work semantically.

Original masses and object-specific corrosion/cleaning losses are unmeasured.
The existing unrestricted-loss proof already explains why arbitrary fitted losses
cannot identify a unit system. The broken tang's original mass is unknown. The
printed decimals also do not establish milligram measurement precision. The
large axe's primary field number 7535 versus later 7835 discrepancy and its
imperial/metric inconsistency remain preserved; the secure join used here is
plate CXXVI item 5, and the calculation uses the printed metric literal.

## Novelty and verification

The existing [three-object check](METAL_TOOL_THREE_OBJECT_CHECK.md) already proves
the nonnegative-t lower-bound conflict. Its precision sensitivity retained the
rounded 262 g small-axe input. The [numeral identifiability review](METAL_NUMERAL_IDENTIFIABILITY.md)
already uses 262.233 g for its two-axe carrying test and proves unrestricted-loss
non-identifiability. This note does not reclassify those results as new findings.
Its additions are the explicit all-three-primary-mass **signed** solution,
distinction between negative-i-only and unrestricted signed models, and the
residual-sign counterexample. The parent's current mass-audit script independently
contains the signed fitting function; no competing implementation was added.

Both solutions and all differences above were independently calculated with
Python `fractions.Fraction`, decimal inputs supplied as strings. Reproduce the
principal calculation with:

```python
from fractions import Fraction as F
S, L, C = map(F, ('262.233', '1910.030', '165.343'))
i = S/6
u = (L-S)/7
t = (C-u-5*i)/4
assert (i, u, t) == (F(87411,2000), F(1647797,7000), F(-4040177,56000))
assert (6*i-S, 7*u+6*i-L, u+5*i+4*t-C) == (0, 0, 0)
```

No downloads, shared scripts, source manifests or research-log edits were made.
