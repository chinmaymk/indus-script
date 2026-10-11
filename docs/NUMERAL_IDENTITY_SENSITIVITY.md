# The numerical candidate set depends on a shared value across objects

**The two surviving numerical candidates are a result of the shared-value
model, not a conclusion independent of sign identification.** If the value on
the first proposed equation is allowed to differ from the value on M-331, there
are infinitely many positive integer solutions, even when both values must be
smaller than both bases. This calculation does not show that the ancient values
actually differed.

The [original conditional audit](NUMERAL_EQUATIONS.md) used one variable v:

```
3L+v = 2L+2S
vL+1 = 7S+5.
```

The published proposal intentionally treats its sign900 as having one value.
The local catalogue instead uses W900 in the proposed H-904 counterpart and
W899 on M-331. Different modern codes are not proof of different ancient signs;
the [earlier image review](NUMERAL_IMAGES.md) left that equivalence unresolved.
This sensitivity therefore asks what follows **if the cross-object shared
value has not yet been independently justified**, without changing the
author's stated equations or silently merging catalogue codes.

## Exact infinite families

Separate the proposed values into vA and vB:

```
3L+vA = 2L+2S
vB·L+1 = 7S+5.
```

Require integer L≥10, S≥8, and `0<vA<min(L,S)`, `0<vB<min(L,S)`.
These upper bounds are stronger than the earlier positive-integer audit used.
Two explicit families satisfy every condition:

| Parameter domain | L | S | vA | vB | Shared-value intersection |
|---|---:|---:|---:|---:|---|
| Integer t≥2 | 7t+1 | 4t | t−1 | 4 | t=5 gives (36,20,4,4) |
| Integer t≥1 | 7t+3 | 6t+2 | 5t+1 | 6 | t=1 gives (10,8,6,6) |

For the first family, `L+vA−2S=0` and
`vB·L−7S−4=4(7t+1)−28t−4=0` identically. For the second,
`L+vA−2S=0` and `6(7t+3)−7(6t+2)−4=0` identically.
All positivity and upper-bound margins are affine functions that are
nonnegative at the minimum t and never decrease. L strictly increases with t,
so each family contains infinitely many distinct admissible tuples. This is
an algebraic certificate, not an inference from a finite search cutoff.

For example, `(L,S,vA,vB)=(15,8,1,4)` gives
`3×15+1=2×15+2×8=46` and `4×15+1=7×8+5=61`.
Replacing the two values by either1 or4 fails one equality. This is a synthetic
witness of assumption sensitivity, not a proposed ancient key.

Within the first family, `vA=vB` forces t=5; within the second, it forces t=1.
These recover the two earlier shared-value candidates. The two families are
not asserted to exhaust the split-value solution set. The earlier divisor
proof, separately, exhausts the stated shared-value positive-integer model.

## What this changes

The [two-candidate ratio test](NUMERAL_CALIBRATION_DESIGN.md) remains exactly
correct for its specified shared-value model. Its approximately6.718% accuracy
threshold is not a guarantee for a larger model class with independently
varying values, changed segmentation or per-object units. Those alternatives
must be fixed or bounded before interpreting any future measurement as choosing
between just two candidates.

Photographs can help determine whether two modern codes describe the same
graphic form. They cannot alone prove a numerical interpretation or a constant
value across contexts. Conversely, a visible graphic difference can be
allographic and need not entail a different value. A robust reading must make
these equivalences explicit and test them beyond the examples used to derive it.

The [exact script](../scripts/analyze_numeral_identity_sensitivity.py),
[coefficient certificates](../results/numeral_identity_sensitivity.json) and
[independent integer checks](../tests/test_numeral_identity_sensitivity.py)
preserve the result. No signs receive semantic or phonetic values from this
proof. The complete417-sign decipherment remains unresolved.

## New source and graphic checks

The [Fuls follow-up](FULS_NUMERAL_FIGURE_FOLLOWUP.md) recovered another rendering
of the author's text. It explicitly uses source sign900 in both arguments, so
the shared value is part of the proposal rather than an accidental equation
merge by this project. Its Figures16/18 remain uninspected. At captured
lines677–678, the prose calls three long strokes “032,” whereas the local
H-904B export uses033 for three and H-904A uses032 for two. This textual/code
discrepancy could reflect numbering, error or extraction; unseen figures cannot
settle it. We preserve literal counts and each namespace rather than silently
correcting either source.

The [H-904 primary review](H904_NUMERAL_GLYPH_REVIEW.md) now supplies the original
CISI2 photographs and catalogue row. H-904B's angular open arc and M-331B's
smoother open arc are broadly compatible in shape and orientation as displayed.
That is positive local graphic evidence, not a global W899/W900 alias or an
authenticated numerical value. The proposed source ID3786 remains distinct
from a verified source-figure identity. The [H-1923 locator review](H1923_PRIMARY_NUMERAL_REVIEW.md)
records the scope of the retained volumes and the remaining photograph gap for
the other object used in the constant-unit contradiction. Earlier conditional
results are not upgraded beyond the evidence that supports each physical object.
