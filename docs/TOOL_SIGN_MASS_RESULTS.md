# A mass-model test using the same catalogue sign

The newly recovered reverse of M77 2923 belongs to the previously measured
DK7856 chisel tang. It supplies a firmer catalogue-to-object connection, **not a
new independent mass measurement**. The same five-stroke catalogue sign, M106,
also occurs as the sole recorded reverse sign of Kalibangan axe K-122 / M77 8301.
This permits a simple conditional test without choosing values for the other signs.

## The preserved graphical evidence

The complete 2923 reverse is M387 M015 M104 M106 M312. The
[object-specific bridge](TOOL_SIGN_BRIDGE_REVIEW.md) aligns M104 with four transverse
strokes, M106 with five upright strokes, and M312 with an arch in the original
published drawing. Pettersson's selected expression calls these `4t`, `5i` and
`1u`. M387 and M015 remain **uninterpreted residual signs**. The selected numerical
expression does not translate the whole face, much less both faces of the object.

M77 normalizes M104 as upright strokes despite the original transverse orientation.
That is a warning against deriving equal values or a universal `t` identity from
normalized appearance. Likewise, one M106 token represents a five-stroke group;
it is not five occurrences of an independently identified unit sign.

The [identity review](BRONZE2923_IDENTITY.md) establishes 2923 = FEM CXXVI2.
The secure mass join is through plate and item. The damaged tang's reported mass
is 165.343 g; its original complete mass is unknown. The published 476 g for K-122
is also a surviving-object measurement. The probable museum match at 476.70 g
is not promoted or substituted here.

## Conditional inequality and its assumptions

Assume all of the following:

1. The sole recorded M106 is the complete K-122 mass expression and denotes its
   exact reported current mass, 476 g.
2. M106 contributes the same mass amount on the chisel, across the two contexts.
3. Other elements do not reduce that contribution: their net contribution is
   nonnegative, with no subtractive or divisive operation.

Let q be the mass contribution of M106, and r the net contribution of everything
else on the chisel face. Then:

```
q = 476 g
chisel mass = q + r, where r >= 0
therefore chisel mass >= 476 g
```

The surviving chisel is 165.343 g, a shortfall of **310.657 g**. This contradicts
an exact-current-total-mass interpretation under these assumptions. It needs no
choice of `u/i`, no equality of upright/transverse stroke values, and no reading
of M387 or M015. The assumption r≥0 is nevertheless consequential; the residual
signs have not been shown to be semantically inert or additive.

If the inscription instead refers to the complete original chisel, its unknown
mass prevents the same direct comparison. The model would require an original
to surviving mass ratio of at least **476000/165343 ≈ 2.878864**. Equivalently,
at least **65.2641%** of the original mass would have to be missing. These are
conditional requirements, not measured loss estimates.

The previously discussed reconstruction hypothesis, original mass less than
2.6 times the surviving tang mass, would cap it below **429.8918 g**. It remains
inconsistent with the 476 g lower bound by **46.1082 g**. That reconstruction
factor is itself disputed; rejecting the combination does not authenticate it.
Increasing the allowed original mass can remove this particular conflict.

## What this does and does not resolve

A fixed numeral value can coexist with different units. The inequality tests a
fixed **mass contribution**, not the hypothesis that M106 represents the number
five. Context-dependent units, different referents, nonadditive operations,
lost signs or a non-mass interpretation change the premises. None is selected
as the correct reading by this test.

The two artifacts were already part of the weight investigation. Their new
catalogue crosswalk cannot be counted as held-out confirmation. No sign meaning
or sound is established. The practical gain is a precisely stated constraint
and a record of the signs and source details that a proposed reading must explain.

## Saved analysis

The [script](../scripts/audit_tool_sign_mass.py) uses exact rational arithmetic,
checks the two evidence ledgers and reads the existing reported masses. Its
[result](../results/tool_sign_mass_audit.json) preserves the assumptions, proof,
exact bounds and source fingerprints. Two tests verify the strict upper-bound
case and distinguish an original-mass allowance from an observed current mass.
The protocol explicitly labels this an exploratory, conditional model test.

The [417-sign evidence index](../results/sign_evidence_417.json) now attaches the
object-specific graphical mappings to M104, M106 and M312, and retains M387/M015
as residuals. All other signs have empty lists for this narrowly scoped evidence;
all 417 semantic and phonetic fields remain null. No downloads were required.
