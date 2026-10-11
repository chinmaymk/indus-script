# Original Lothal record for seal L-51

Independent context review, 2026-09-25. The target was selected from Mukhopadhyay's 2025 fish-sign argument; this is a source audit, not a blind validation. The parent audit checks the CISI identity independently.

## What the original report establishes

Rao's *Lothal: A Harappan Port Town*, volume II (1985), printed p.310 (retained PDF page 61), identifies terracotta seal **11358**, plate **CLIX C5**. Its motif occupies the upper panel and its inscription the lower. The narrative calls the motif unique and says it looks like a seed drill. This is a resemblance judgement, not a recovered tool's functional identification.

Printed p.317 (PDF page 68) records **phase IV; SRG 2; C25; a pit sealed by layer 2; depth 1 ft 0 in**. The reverse button is broken. The entry again calls the upper motif a seed drill. The quoted pages provide no contents of this pit, no necklace found with the seal, no associated beadworking installation, and no diagnostic comparison explaining the seed-drill interpretation. These absences refer to the inspected passages; they do not establish that no other excavation record exists.

The physical artifact is a terracotta seal, not a necklace or an excavated seed drill. Its phase is recorded; no absolute age is derived here without separately auditing the phase chronology. A pit sealed beneath a layer is not automatically a primary workshop floor deposit.

Plate CLIX (PDF page 489), viewed after rotating the page clockwise 90 degrees, locates item C5 and repeats the seed-drill motif classification. Its caption groups C1–2 and C4–5 as terracotta and describes the miscellany as unperforated. The scan is severely thresholded; C5 is very small. It is inadequate for deciding fine motif details. No independent comparative physical seed drill is illustrated on this plate.

## What remains interpretation

Mukhopadhyay's IRC Bulletin 6 (2025), printed p.19 / PDF page 25, calls L-51 a multi-strand necklace and compares it with an ancient necklace and modern examples in Figure 7. The subsequent jeweller/gemstone-guild reading additionally assumes that the iconography identifies the seal issuer's organization and that the fish signs name its commodity or craft. Neither assumption follows from the excavation location above.

A necklace is a candidate visual analogy; the original seed-drill description is another candidate analogy. The cited evidence does not establish either object's identity, nor adjudicate their relative probabilities. Neither should become a labelled training example for fish-sign semantics. Confirmation would require independently diagnostic motif features and contextual evidence, preferably across additional objects chosen independently of their fish-sign inscriptions.

## Reproducibility and limitations

- [Original report](https://archive.org/details/masi78lothalaharappanporttownraos.r.part2_531_D) retained as `data/raw/l51_rao1985_volume2.pdf` (638 PDF pages).
- The archive's OCR is largely wrong-script output and unusable for reliable text search. Fresh Tesseract OCR and visual inspection establish the two cited passages.
- Page-map leaf 60 corresponds to PDF 61 / printed 310; leaf 67 to PDF 68 / printed 317. Initial neighboring renders PDF 60/67 were retained as navigation history.
- Navigational samples PDF 440/450/460/470 and plates PDF 488/490 are retained. The plate scan itself was initially rotated the wrong direction for inspection, then corrected to clockwise 90 degrees before review and hashing.
- Recreate evidence with `scripts/render_l51_primary.py --pdftoppm PATH --tesseract PATH`; source registrations and hashes are in `data/processed/l51_new_sources.json`, evidence pins in `data/processed/l51_context_review.json`.

No semantic or phonetic value is established by this review.
