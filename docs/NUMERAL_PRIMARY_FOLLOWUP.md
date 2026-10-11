# Primary-catalogue follow-up of two numeral-order witnesses

**Mahadevan's normalized drawings corroborate the relevant stroke-order patterns.**
The drawing at reference 1066 contains two short strokes immediately followed by
one long stroke in displayed left-to-right order. Reference 2427 contains one long
stroke, two short strokes, and another long stroke, without an intervening
non-stroke glyph. These observations do not themselves establish numerical values
or show that adjacent strokes belong to a single numerical field.

The review used the existing [1977 catalogue scan](../data/raw/mahadevan_1977_text.pdf)
and the literal source rows already used in the [numeral grammar test](NUMERAL_THEORY.md).
No new files were downloaded. The observations, source hashes, unresolved links,
and reproducible crop coordinates are in the
[review ledger](../data/processed/numeral_primary_followup.json).

| Proposed object match | Raw export excavation field | Catalogue reference | Drawing locator | Graphic observation |
|---|---|---|---|---|
| M-678; local 3116.1 | `VS 1059066` | 1066 | Printed p.41; PDF p.52 | Two short strokes, then one long stroke |
| M-1745; local 2393.1 | `DK8359427` | 2427 | Printed p.71; PDF p.82 | Long, two short, long |

Both literal export rows have direction R/L. Their raw identifiers and literal
W-code sequences are retained in the ledger without correction. The short-stroke
pair is a graphic count of two visible marks; calling its numerical value two
would be an additional, unproved interpretation.

## What the identifier check establishes

Appendix V, printed pp.816 and 818 (PDF pp.825 and 827), explicitly maps catalogue
references 1001-1560 to items 1-560 in Marshall's *Mohenjo-daro and the Indus
Civilization*, volume III, and references 2002-2704 to items 2-704 in Mackay's
*Further Excavations at Mohenjodaro*, volume II. Consequently, catalogue 1066 maps
to Marshall item 66, and catalogue 2427 to Mackay item 427.

The export excavation fields end in `066` and `427`, respectively, and the surrounding
normalized shapes agree with the proposed source-row matches. This provides a
reasonable proposed crosswalk. However, Appendix V does **not** give individual
excavation IDs for these two entries in its principal-publication ranges. The
excavation-number bridge to CISI M-678 and M-1745 is therefore **not independently
authenticated here**. It would be wrong to split the strings silently into a verified
excavation number plus a verified publication reference, or equate whole sign
namespaces from similar drawings.

This limitation does not erase the direct observations about catalogue references
1066 and 2427. They can be cited under those identifiers without asserting a fully
verified CISI crosswalk. Reference 2427's long-short-long pattern in particular
fails either strict monotone long/short ordering, conditional on treating that
adjacent group as one ordered numerical field. Multiple fields, order-free addition,
and nonnumerical stroke uses remain alternatives. No ancient boundary is inferred.

## Cross-check against a photographed seal

A separate parent review locates CISI M-160 in volume 1, printed p.48/PDF84,
with both original and impression. The impression displays one long stroke
followed immediately by two short strokes. The catalogue data row on printed
p.367/PDF403 explicitly links M-160 with Mahadevan reference 2286, excavation
DK12449 and museum ASI63.10.88. The export field `DK12449286` is malformed or
concatenated; it has not been silently corrected. The
[M-160 review ledger](../data/processed/m160_primary_review.json) retains this mismatch.

Reference 2286, printed p.66/PDF77 of Mahadevan, displays the same order. Therefore
references 2286 and 1066 show opposite orders **within the same normalized edition**;
this comparison does not mix a seal original with a mirrored impression.
Reference 2427 supplies the returning long–short–long pattern at the level of
the printed edition.

The [three manually reviewed class patterns](../data/processed/primary_tally_patterns.json)
are evaluated separately by `scripts/audit_numeral_theory.py`, using its existing
exhaustively tested descent calculation. The
[primary-pattern result](../results/primary_tally_order_check.json) retains both
rank orders and necessary cuts. Neither order fits all patterns; reference 2427
requires at least one cut under either order if monotone fields are required.
These are conditional cuts, not identified ancient boundaries. The three selected
examples are not added to the corpus frequency denominator.

## Extent and reproduction

This was one manual visual review of complete relevant catalogue pages and enlarged
detail crops. The source is a normalized catalogue transcription, **not a newly
checked artifact photograph**. Different publications of an object would not
constitute independent archaeological samples. These selected checks add no new
corpus frequency estimate or general authentication of every row in the export.

Reproduce the saved images with:

```sh
python3 scripts/render_numeral_followup.py --pdftoppm /path/to/pdftoppm
```

The [rendering script](../scripts/render_numeral_followup.py) invokes the existing
PDF helper at scale 2600 and saves pages under `results/primary_pages/numeral-followup-*`.
Its detail crops only magnify source pixels; no signs are repaired or redrawn.
It requires pypdf, Pillow and Poppler. Page 81 was retained as a locating page;
the target reference 2427 is on page 82. OCR helped locate entries, while the
reported stroke counts and Appendix mapping were checked visually.
