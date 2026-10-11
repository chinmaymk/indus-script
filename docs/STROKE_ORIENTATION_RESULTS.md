# What stroke orientation can and cannot establish

The knife DK7800 exposes information lost in normalized sign codes. Mackay's
original description reports four vertical strokes immediately above four
horizontal strokes; Mahadevan records the object as2928 with two identical
M104 tokens. A model that assigns different contributions to those orientations
cannot interpret each occurrence from M104 alone. This is a representational
constraint, not a deciphered numeral or a proof that the orientations differ
in meaning.

Pettersson already emphasized the loss of row arrangement in sequential
transcriptions on printed p90. This audit adds checked object/catalogue joins
and explicit conditional proofs; the general normalization concern is not new.

The [original-source audit](STROKE_ORIENTATION_TOOLS.md) and
[catalogue audit](ORIENTATION_CORPUS_COVERAGE.md) establish the joins separately.
Both2928 and spearhead2926 were already included in M77 and the local export.
The initially proposed CXXVI1/4 locators were wrong; the correct locators are
CXXXIII1 and CXXVII1 respectively. No omission or exclusion policy can be inferred
from the failed initial search.

| Object | Normalized field | What survives in original sources |
|---|---|---|
| DK7800 /2928 | M104 M104 | Prose explicitly distinguishes four vertical from four horizontal; photo cannot independently verify all eight |
| DK7857 /2926 | M104 M110 | Prose reports four and seven; drawing shows upright strokes with a tilted upper group, compatible with the later tilted-row label |

Code5 on2928 means symmetrical arrangement, not doubtful direction. No token index
is assigned to either orientation and no ancient reading order is inferred.
Pettersson's `t` denotes a tilted row, not necessarily individually horizontal strokes. Our earlier claim that the drawing challenged his notation is [withdrawn](PETTERSSON_ORIENTATION_ATTRIBUTION.md). Its numerical interpretation remains conditional. Neither object adds
a measured mass, and original dimensions are insufficient to reconstruct one.

## Conditional proof and an essential counterexample

Let each vertical stroke contribute i and each horizontal stroke contribute t.
These are hypothetical units, not established readings. If each normalized M104
occurrence must also have one invariant additive contribution v, agreement at
each group requires

```
v = 4i
v = 4t
therefore i = t.
```

Thus a strict t<i hypothesis cannot also retain that local invariant mapping.
Orientation, position or another context would have to be retained, or one of
the model premises abandoned. Equal numerical value four with different units
is still possible; the proof concerns the scalar contribution after units and
operations are chosen.

Matching a whole inscription's total is weaker. The equation2v=4i+4t permits
v=2(i+t). For example, i=8 and t=1 give groups32 and4, while v=18 gives groups18
and18. Both totals are36. This prevents an invalid inference of i=t from total
agreement alone. No observed knife mass chooses between these models.

## A fixed group does not identify its internal arithmetic

In Pettersson's selected nine-tool table, every proposed t-bearing component
has coefficient4: knife, spearhead and tang. For coefficients k in{0,4},

```
k*t = 1[k>0]*c, with c=4*t.
```

On this support, replacing each4t component with one quantitatively valued,
indivisible component c leaves every additive prediction unchanged. The map is
bijective over nonnegative real or rational units. This does not establish that
the component is nonnumeric; a nonnumeric category by itself predicts no mass.
It establishes failure to distinguish two quantitative decompositions from
constant-count observations alone. Excluding the spearhead as a sensitivity check leaves
the same limitation on knife and tang.

Independent unit evidence or verified occurrences with varying counts in comparable t-labelled groups
could separate these models. Imposing integer domains, radix rules or priors
would add assumptions; those are not discoveries from this table. The exact
script demonstrates how a hypothetical three-stroke component breaks the fixed-c
replacement when t>0, without claiming that such an object was found.

## Reproduction and scope

Run `python scripts/audit_stroke_orientation.py`; it verifies both source ledgers,
preserves the attribution correction, extracts coefficients from the retained later
table and writes [machine-readable results](../results/stroke_orientation_audit.json).
The [protocol](../data/processed/stroke_orientation_protocol.json) is explicitly
post-exploration. The [independent mathematical review](ORIENTATION_MODEL_REVIEW.md)
checks the premises and counterexample. Two regression tests protect these
inference boundaries; finite examples support implementation checks, while the
algebra above provides the general proofs.

The417-sign index now attaches these object-level reviews to M104 and M110, with
empty review lists for other codes. This does not expand the sample into417
orientation observations. All semantic and phonetic values remain unresolved.
