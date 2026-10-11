# Review of two conditional orientation claims

Both proposed claims are mathematically sound with the qualifications below.
They constrain models; neither proves a numerical interpretation of the marks.
The selected expressions are from the existing Pettersson nine-object ledger,
not independent measured readings. The numerical interpretation of the spear's `7i 4t` remains conditional.
Correction after this review: Pettersson labels a tilted row; the earlier claimed
conflict with upright individual strokes is withdrawn. See
[the attribution correction](PETTERSSON_ORIENTATION_ATTRIBUTION.md).

## Local contribution versus whole-object agreement

The knife's original description has four vertical and four horizontal strokes.
M77 2928 normalizes the two groups to `M104 M104`. Suppose contributions belong
to a common scalar scale and all of the following are imposed:

1. Each M104 occurrence contributes the same value v104, independent of its
   original orientation and position.
2. Each stroke in the first original group contributes i, and each stroke in the
   second original group contributes t.
3. The code-to-original correspondence preserves the contribution of **each
   occurrence separately**, with additive composition inside both groups.

Then `v104 = 4i` and `v104 = 4t`; subtracting yields `4(i − t) = 0`, hence
**i = t** over the real or rational scalars. Thus i≠t contradicts this joint
local interpretation. The code normalization by itself supplies none of these
semantic premises. A context-sensitive decoder can assign `4i` to the vertical
M104 occurrence and `4t` to the horizontal occurrence if original orientation
metadata is retained, while using the same normalized code. That decoder simply
abandons premise 1.

Preserving only the whole expression is weaker:

```
2v104 = 4i + 4t  ⇒  v104 = 2(i + t).
```

For a concrete counterexample, take i=8, t=1 and v104=18. Both whole totals are
36, although the original group contributions are 32 and 4, while the two code
contributions are 18 and 18. This disproves any inference of i=t from total
agreement alone. It is not a proposed Indus reading and does not claim to fit
other inscriptions. Additional independently constrained objects might exclude
this example; such an exclusion needs its own assumptions and equations.

An affine per-group offset shared by both occurrences does not rescue the local
inequality: `v104 = a + 4i = a + 4t` still forces i=t. Different offsets can rescue
it, but add context dependence. Nor does an unchanged additive residual elsewhere
in the inscription alter this local argument. A total-only residual that can vary
between interpretations weakens total identifiability further.

The scope should be stated as **incompatibility of unequal oriented stroke values
with one occurrence-preserving, invariant scalar value per normalized code**.
It is not a rejection of unequal denominations, all numeral systems, all
contextual uses of M104, or the M77 classification itself. Common scalar scale
matters: separate units, referents or vector-valued categories require a different
model before equating contributions.

## Fixed four-stroke group versus an indivisible component

In the selected nine-expression ledger, every nonzero coefficient of t is four.
It occurs in the knife `4i 4t`, spear `7i 4t`, and tang `1u 5i 4t`; the remaining
selected expressions have no t term. Let z_j be 1 when that group is included and
0 otherwise, and let A_j collect the rest of an expression. Then

```
Q_j = A_j + 4 z_j t
    = A_j + z_j c, with c = 4t.
```

For unrestricted positive real or rational scalar values, t↔c/4 is a bijective
parameter change. The models make exactly the same predictions on every selected
row, with the same number of free parameters. Any likelihood based only on these
predictions and the same error model is unchanged. This remains true after
removing the spear in a sensitivity check: it reduces evidence, not the algebraic
equivalence for the remaining fixed-four terms.

The alternative c must mean an **indivisible but quantitatively valued component**
for this exact additive equivalence. Merely calling it a nonnumerical category does
not define a prediction model; a separate rule would be needed to map that
category to an amount. Conversely, estimating a numerical t from independent
amount observations would estimate c as well, but would not by itself prove that
the four visible strokes were four compositional units in the ancient system.
The sample can estimate an aggregate contribution under strong external premises
without identifying its internal decomposition.

Equivalence assumes matched parameter domains. If t is restricted to integers,
then c must be restricted to multiples of four to preserve the bijection. A prior,
fixed radix, denomination ordering, integer-unit convention or externally anchored
stroke value can also break equivalence, but that distinction then comes from the
additional premise, not the selected constant coefficient. A prior must be
transformed with its Jacobian before comparing Bayesian evidence under a pure
reparameterization; independently chosen priors can create an artificial preference.

An authenticated comparable expression with a different count in a comparable t-labelled group would
supply a new test. For example, an `n t` group with n≠4 predicts `(n/4)c` under
stroke composition, whereas assigning the same indivisible component contribution
c to every such group predicts c. Independent context or quantity evidence would
still be needed to select between these models. Simply discovering a differently
shaped group does not establish that both belong to the same semantic component.

## Evidence inspected and review limits

Read the existing `metal_tool_weight_anchors.json` nine-object expressions,
`metal_numeral_convention_review.json` restrictions, and this turn's primary M77
coverage and original-tool reviews. The numerical counterexample and algebra were
checked directly. No new data, code or shared research-log changes were made.
This is a bounded mathematical review after seeing the hypotheses, not an
independent decipherment or an empirical out-of-sample confirmation.
