# What measurement would distinguish the two numerical candidates?

**A single quantity measurement cannot choose between the two surviving
conditional numerical keys when their physical unit is unrestricted. Two
securely linked, commensurate quantities can do so if their predicted ratios
differ.** This is a mathematical design result. No such new archaeological
measurement pair has been authenticated in the reviewed evidence.

The [earlier exact equation audit](NUMERAL_EQUATIONS.md) leaves candidates
`(L,S,v)=(10,8,6)` and `(36,20,4)` after its conditional digit bounds. Both
satisfy the proposed equalities. They predict the following totals:

| Hypothesized quantity | Expression | Candidate (10,8,6) | Candidate (36,20,4) |
|---|---|---:|---:|
| A, the two-face example's total | 3L+v = 2L+2S | 36 | 112 |
| B, the M-331 proposed total | vL+1 = 7S+5 | 61 | 145 |
| B/A, independent of a common unit | | 61/36 ≈1.69444 | 145/112 ≈1.29464 |

These are proposed represented totals, not the artifacts' measured masses or
volumes. H-904 is a proposed crosswalk for the first example; the original
article identifier and local W899/source900 issue remain qualified as in the
[corpus screen](NUMERAL_SCREEN.md) and [image review](NUMERAL_IMAGES.md). The
arithmetic does not authenticate equality between faces, a total relation,
positional multiplication or a shared unit across these objects.

## Why one anchor is insufficient under an unknown scale

Suppose an independently known positive amount q corresponds to numerical
total n, with physical unit u>0. Then q=un. For every positive candidate n,
choosing u=q/n gives an exact fit. For example, the explicitly hypothetical
amount100 would fit A=36 with unit25/9, or A=112 with unit25/28. Neither amount
nor unit is an archaeological observation. A separately established unit or
a justified restricted set of units would change this conclusion.

With two quantities measured in the same physical dimension and using a
common unit, qB/qA=nB/nA. The scale cancels. Nonproportional predictions can
therefore differ even when each model is allowed its own overall unit. If
independent units are allowed for A and B, the distinction disappears again.
Two proportional numerical vectors also remain indistinguishable by this test.

## Exact accuracy requirement

Let each observed amount qi have a bounded relative uncertainty e, with
0≤e<1. A candidate fits if one u>0 satisfies

```
qi(1−e) ≤ u ni ≤ qi(1+e)   for each i.
```

For a candidate predicted ratio r=nB/nA, the compatible observed ratio lies in

```
[ r(1−e)/(1+e), r(1+e)/(1−e) ].
```

This follows directly by intersecting the two permissible unit intervals.
The two candidates' intervals are strictly disjoint exactly when

```
R = (61/36)/(145/112) = 1708/1305
R(1−e)^2 > (1+e)^2
403e^2 − 6026e + 403 > 0.
```

For0≤e<1, the boundary is
`e*=(√R−1)/(√R+1) ≈0.0671786805`.
Thus independent per-object error bounds **strictly below about6.718%** give
disjoint ratio predictions for these two particular totals. At the boundary,
the intervals touch, so a boundary observation can fit both. All comparisons
in the script use exact rational arithmetic; the decimal threshold is for display.

At5% per-object error, the respective compatible ratio intervals are
`[1159/756,1281/684]` and `[2755/2352,3045/2128]`, which do not overlap.
At10%, they overlap. Overlap does not mean every possible observation is
ambiguous: some observations still select one candidate or reject both.
The bound treats errors adversarially and separately for each quantity. A
perfectly shared multiplicative calibration error cancels from the ratio.

## What has to be established before using this test

1. Authenticate the sign forms, grouping, operations and exact artifact identity.
2. Independently show what amount the inscription represents. A seal's weight,
   a container's capacity and its actual contents are different possible quantities.
3. Establish commensurability and a common unit without using the numerical fit.
4. Bound loss, reconstruction error and object-specific measurement uncertainty.
   Glyph ambiguity creates discrete alternative predictions and is not absorbed
   automatically into a small measurement-error percentage.
5. Freeze the prediction and inclusion rule before inspecting the new quantities.
   Report results that reject both candidates as readily as a successful fit.

The present [external-anchor screen](EXTERNAL_ANCHOR_RENEWED_RESULTS.md) has not
supplied these joins. Even successful discrimination would support a restricted
numerical interpretation, not identify a language or assign all417 readings.
It would also leave other numerical systems and nonnumerical alternatives to
be tested. The numerical candidates are not an exhaustive history of the script.

The [script](../scripts/analyze_numeral_calibration_design.py),
[exact results](../results/numeral_calibration_design.json) and
[independent feasibility examples](../tests/test_numeral_calibration_design.py)
preserve the derivation, source hashes, unit intervals and synthetic controls.
No downloaded data or new ancient sign values were needed for this calculation.

The parallel [sample-photo follow-up](KOTADA_SAMPLE_PHOTO_REVIEW.md) recovered
publisher images and original residue tables, but still no authenticated
inscription-to-residue match. An [independent table extraction](../results/kotada_supplement_independent.json)
confirms ten exact sample-label matches, an unmatched KB61 and conflicting
KB106 residue entries. These chemical data are not represented numerical
amounts for A or B. The [Umma entry follow-up](UMMA_ORIGINAL_ENTRY_FOLLOWUP.md)
located a precise institutional chapter citation but did not recover the
original object entry. The [independent inventory review](ALL_INVENTORY_NEXT_TEST_REVIEW.md)
checks the ratio proof and explains why none of these gains yet supplies a
reading for the full sign inventory.
