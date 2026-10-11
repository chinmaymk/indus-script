# An exact audit of a proposed numerical key

**The proposed values (10, 8, 6) satisfy two published equations. They are not
uniquely determined without an additional assumption.** A second solution,
(36, 20, 4), survives the same minimum-base constraints. This is a conditional
mathematical result, not an assertion that either system was used historically.

## Inputs and their evidential status

[Fuls (2020)](https://www.researchgate.net/publication/361812318_Ancient_Writing_and_Modern_Technologies_-_Structural_Analysis_of_Numerical_Indus_Inscriptions)
uses a two-face comparison (Formula 2, Figure 16) and a proposed total on CISI
artifact M-331 (Figure 18) to constrain long- and short-stroke bases and sign 900.
The text was checked in [a second public rendering](https://www.academia.edu/41952485/Ancient_Writing_and_Modern_Technologies_Structural_Analysis_of_Numerical_Indus_Inscriptions).
The PDF figures were not verified visually. The author invokes the bangle argument
discussed in our [quantity audit](QUANTITY_ANCHORS.md); this is not a new independent
contents measurement.

Let L be the proposed long-stroke base, S the short-stroke base, and v the value of
source sign 900. We audit the following interpretation exactly:

```
3L + v = 2L + 2S       (A)
vL + 1 = 3S + 5 + 4S   (B)
```

The [claim ledger](../data/processed/numeral_equation_claims.json) fixes these inputs,
their source locators, assumptions and limits. Arithmetic notation is not evidence
that a scribe intended equality, addition, or positional multiplication. Those are
hypotheses about grouping, numerical role, commensurate units and relations between
faces; they remain to be checked independently.

## Complete solution, without a search cutoff

Assume L, S and v are positive integers. From (A), v = 2S − L. Substitution into (B)
gives

```
(2L − 7)S = L² + 4.
```

The right side is positive, so 2L − 7 > 0. Write d = 2L − 7. Then

```
4(L² + 4) = (2L − 7)(2L + 7) + 65.
```

Since d divides L² + 4, it divides 65. The positive divisors of 65 are exactly
1, 5, 13 and 65. Check each with L = (d + 7)/2, S = (L² + 4)/d and v = 2S − L:

| d | L | S | v | Meets L ≥ 10 and S ≥ 8? |
|---|---|---|---|---|
| 1 | 4 | 20 | 36 | No |
| 5 | 6 | 8 | 10 | No |
| 13 | 10 | 8 | 6 | Yes |
| 65 | 36 | 20 | 4 | Yes |

These are **all** positive integer solutions. Completeness follows from divisibility,
not from guessing a convenient maximum base. The minimum-base screen assumes
the observed stroke counts are normalized digits with carrying; it is itself a
numerical-system assumption, not a consequence of a stroke's appearance.

The surviving alternative satisfies both equations exactly:

```
3×36 + 4 = 2×36 + 2×20 = 112
4×36 + 1 = 3×20 + 5 + 4×20 = 145.
```

If one additionally accepts 8 ≤ L ≤ 13 from the disputed bangle anchor with the
short-stroke value fixed to one, only (10,8,6) remains. There is no need to exclude
odd or prime bases to obtain that conditional uniqueness. Removing the bangle
assumption restores the second solution. Choosing the smallest bases is a reasonable
model preference, but does not turn a preference into external identification.

Equation (A) alone also does not force S even. For example, L = 10, S = 9 and v = 8
satisfy (A); they do **not** satisfy (B). Divisibility of v + L by two means the sum
is even, not that its half is even. This example tests the algebra and is not a
proposed Indus reading.

## Artifact and namespace checks

The [selected literal corpus records](../results/numeral_source_records.csv) retain
all four M-331 faces, the M-1383 sealing row and the local row numbered 3786.1.
Proposed translations and Sanskrit columns are excluded. The source is our already
pinned secondary transcription, not a new independent archaeological witness.

- M-331's two-sign face is encoded locally as `+001-899+`. Equating local W899
  with source sign 900 requires visual and signary verification.
- Its three-stroke face is fourth in the local rows, while the article prose calls
  the three-stroke face Side 3. Face numbering cannot silently join the records.
- Local ID 3786.1 identifies M-1540 with one listed face. Therefore an article's
  bare integer ID 3786 is insufficient to identify the two-face example in this
  release. This is an unverified crosswalk, not proof that the source ID is wrong.

No mappings, reconstructed signs or face associations have been silently corrected
to make the equations fit. All these examples are selected from the proposal;
none is an untouched prediction made by our model.

## What would strengthen the candidate

First verify the illustrations and artifact crosswalks. Then freeze the assignments,
rules for additive versus positional readings, treatment of intervening signs,
and when faces are expected to balance. Apply them to every eligible object in a
defined corpus, retaining failures and damaged cases. A small number of equations
chosen after seeing their numbers cannot establish a universal numerical system.
Different units or lists without totals are possible and would change the model.

The result supports (10,8,6) as a compact **candidate under explicit assumptions**.
It does not identify a language, prove a weight or capacity unit, or assign meanings
to all 417 signs. The full decipherment remains unresolved.

Follow-up: the [complete two-marker corpus screen](NUMERAL_SCREEN.md) finds H-904
as a proposed match for the two-face pattern, retains every exclusion, and exposes
a conditional counterexample when L/R-labelled texts are admitted. This does not
authenticate the source figure or resolve the M-331 sign-code mismatch.

The later [catalogue-image audit](NUMERAL_IMAGES.md) joins the four local M-331
rows to physical CISI faces A, B, F and D. It clarifies the face-order issue without
equating W899 and W900. H-306's stroke counts now also have photographic and
primary-transcription support.

Reproduce with `python3 scripts/audit_numeral_equations.py`.
The [script](../scripts/audit_numeral_equations.py),
[result](../results/numeral_equation_audit.json), and
[tests](../tests/test_numeral_equations.py) preserve the complete calculation.
