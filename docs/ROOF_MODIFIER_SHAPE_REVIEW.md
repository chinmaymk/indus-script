# Roof-like additions: primary shape review

Date: 2026-09-27. The representative Mahadevan1977 sign-list drawings support **six candidate base/modified pairs sharing a small apex-up, two-oblique-stroke mark above a similar underlying form**. These are visual hypotheses selected without sequence counts, matching contexts, corpus frequencies or translations. Two pairs share the fish base and must not be treated as six wholly independent graphic families. No meaning, sound, productive affix, or sign decomposition is established.

The review covers all four retained primary representative pages, printed32–35/PDF43–46. The supplied417 individual PNGs were not needed and were not used to override the numbered primary drawings. The source is `data/raw/mahadevan_1977_text.pdf`; the specific full-page renders and unretouched numbered crops are pinned in the companion JSON.

## Shape-selected core

| Pair | Printed page | Visible comparison | Variant caveat |
|---|---|---|---|
| M059→M065 | 32 | Similar oval fish-shaped body and crossed lower strokes; M065 has a separated shallow apex-up roof above. | M059 bears a dagger in the representative list. |
| M060→M066 | 32 | The flanked fish form preserves four short surrounding strokes; M066 adds the roof. | M060 bears a dagger. This is the same fish-base family as059→065, with a further shared surrounding feature. |
| M089→M092 | 32 | Three tall parallel vertical strokes; M092 adds the roof above them. | M089 bears a dagger. Do not substitute the shorter grouped strokes of M102 merely because their count is also three. |
| M137→M138 | 33 | A plain X-shaped crossing; M138 places the roof above it. | M137 bears a dagger. Relative spacing and arm angles are representative drawing choices, not exact geometric invariants. |
| M162→M163 | 33 | A U-shaped trident top with a central downward stem; M163 adds the roof above. | M162 bears a dagger. |
| M333→M334 | 35 | A U-shaped form with central and oblique basal projections; M334 adds a roof above. | M334 bears a dagger. This is visually distinct from the downward-stem-only trident family. |

The arrows mean only “compare the first representative drawing with the second after hypothesizing an added roof.” They do not claim historical derivation, reading order, or a grammatical operation. Each candidate is numbered by the original sign-list label, not by inference from a standalone part.

Mahadevan's note below printed35 says the dagger marks entries with graphic variants in the separate list at printed785–792. Those variant pages were not reviewed in this bounded task. Consequently these hypotheses concern the representative drawings, not every attested variant or every inscription carrying the same code. Even a strong representative match does not demonstrate that the roof is detachable on original artifacts.

## Standalone M134 and exclusions

M134 was inspected at printed33/PDF44 and cropped with its number. It is indeed a standalone **apex-up caret formed by two oblique strokes**. It is relatively acute and tall; several added roofs above are much shallower. This is a broad shape resemblance. The review does **not** identify the added component as tokenM134, assert that the modified signs are sequences of two signs, or permit splitting their corpus tokens.

| Considered form or pair | Disposition and reason |
|---|---|
| M158→M159 | Rejected from the core after close crop inspection: M159 also has a short central upper vertical stroke absent from representative M158. The roof is not the only change. This corrects an initial whole-page impression before the final candidate set was fixed. |
| M141→M159 | Weak alternative only, excluded from the strict set: both have a central vertical through crossing obliques, but the relative extension of the lower stem and arms changes substantially. A formal variant review would be needed to use it. |
| M195→M196 | Excluded: the added top is a flat-topped, three-segment cap rather than the simple two-segment caret selected here. |
| M202→M203 | Excluded for the same flat-topped cap geometry. |
| M410→M411 | Excluded for the same flat-topped cap geometry. |
| M137→M139; M141→M142; M233→M234 | Excluded: rectangular/bracket-like caps are visually different additions. They are possible comparison features for a separately designed study, not members silently merged here. |
| M075 | It has a roof above a hatched fish-like body, but this review did not securely identify an otherwise identical unroofed representative base. No pair is fabricated by deleting multiple features from another fish drawing. |
| M316→M318 | Excluded: curved overhead form and substantial interior differences; not the selected two-oblique addition alone. |

The distinction between acute caret, shallow roof, flat-topped cap and curved arch is retained explicitly. A later broader graphic-family experiment could choose different grouping rules, but must prerecord those rules and not revise them solely to improve context matches.

## Research log and reproducibility

1. Inspected the four primary numbered representative pages in full without opening sequence/context results.
2. Selected the fish examples, parallel-stroke example, crossed-stroke example, trident example and U-with-basal-projections example on visible similarity alone.
3. Inspected individual crops, including the standalone134. Rejected158→159 because of its additional upper stem and kept141→159 outside the strict set. Reported that correction to the parent before finalizing.
4. Distinguished flat-topped, rectangular and curved additions and recorded unsuccessful exact-base identification for075.
5. Checked the primary dagger note; limited conclusions to representative glyphs because variants and original artifact execution were not reviewed here.
6. Fixed the six core pairs and exclusions in the companion JSON. No sequence statistics or semantic claims were produced, and no downloads or central edits were made.

`scripts/render_roof_modifier_crops.py` reproduces unretouched numbered crops with exact fractional coordinates recorded in `data/processed/roof_modifier_crop_manifest.json`. Initial crop offsets that clipped labels were corrected and regenerated before evidence was pinned. `data/processed/roof_modifier_shape_review.json` records the frozen shape-only selection, caveats, exclusions and source hashes. These files support a future independent context test; they are not its results.
