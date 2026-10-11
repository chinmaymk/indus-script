# Reference 1001: recovery of both printed lines

**Corrected identification: the second line is M393, not M317.** The clearer alternative scan shows an internally divided closed oval beneath an arch, with two short strokes below. This matches the directly numbered primary Sign List M393 on printed page 35/PDF page 46. Reference 1001 has these two printed lines:

1. **Unknown span — M067 — M072 — M008 — M342**
2. **M393**

The first line reads right to left on the normalized printed page; the second is a singleton. This recovers all *printed* lines, not the signs lost from the ancient object.

## Correction history

The initial review incorrectly identified the blurred interior as three upper strokes and two lower strokes and assigned M317. Parent flagged a conflict with the existing Table I transcription: M317 has total 1, initial 1 and final 0. That triggered a fresh image check rather than an attempt to fit the counts.

The alternative scan's printed page 39/PDF page 51 distinctly preserves the enclosed oval, ruling out M317's three separate upper ticks. Direct primary Sign List comparison establishes **M393**. Its enlarged labelled glyph and the text glyph agree. The old M317 comparison image remains solely as a record of the rejected identification; the ledger explicitly marks it superseded. Existing Table I transcription gives M393 total 7, solus 5 and final 2; those counts are a diagnostic, not the basis of identification, and were not visually re-audited here. The [position-count review](M77_POSITION_COUNT_REVIEW.md) verifies that Table I uses line-level solus: this complete singleton contributes one such occurrence. Whole-text concordance sorting is a separate convention.

## Lines and metadata

The original source text is printed page 39/PDF page 50 of `data/raw/mahadevan_1977_text.pdf`; the alternative scan shows the same printed page at PDF page 51. Both 1001 lines precede reference 1002. The first-line IDs and loss marker were established in the earlier [primary pilot](M77_EXPORT_PRIMARY_PILOT.md); this review adds the missing second line.

| Printed metadata | Expanded ten-digit code | Interpretation |
|---|---|---|
| `1001 103511` | `1001103511` | Object 1001; type 1=seal; side 0=only side; field symbol 35; line 1; direction 1=right to left |
| continuation `23` | `1001103523` | Inherit object/type/side/field symbol; line 2; direction 3=single sign in the line |

The code `23` is not a second-side number or a sign. Definitions were visually checked on printed pages 30–31/PDF pages 41–42. No doubtful-reading asterisk is attached to the recovered M393. The dark star visible lower down in the alternative detail belongs to the next object, 1002.

There are **five identified sign positions and one unknown span** across the two lines. The span stands for one or more signs, giving a minimum of six ancient signs and no exact total. The exported `000 067 072 008 342` sequence covers only the first printed line and omits `M393`. Canonical data and the parser were not changed.

[The corrected recovery ledger](../data/processed/m77_1001_recovered_lines.json) preserves per-line tokens, uncertainty, metadata, both PDF hashes, image hashes, crop commands and the explicit correction history. Decisive evidence is `results/primary_pages/m77-1001-corrected-glyph-detail.png` and `results/primary_pages/m77-1001-sign393-detail.png`, alongside the full pages. This remains an identification of normalized scholarly drawings, not autopsy of the seal or a phonetic interpretation.
