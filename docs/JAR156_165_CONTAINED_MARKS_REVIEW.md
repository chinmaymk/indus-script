# Contained marks in Vats Table I, rows 156 and 165

The primary table authenticates a reported unicorn-seal fragment inside one jar and a four-stroke goblet inside another. It supplies no explicit illustration reference or separate object number for either contained find. This bounded follow-up has **not** established a photograph, CISI alias, M77 text, complete sign sequence, or numeric value for either. The contained marks must not be transferred to the jars themselves.

The inspected source is Vats, *Excavations at Harappā* (1940), volume I, printed pp.270–271, Archive leaves 296–297. Leaf 297 was retained already as `data/raw/inscribed-frame-vats-leaf297.jpg`; the newly retrieved left page is `data/raw/jar156165-vats-leaf296.jpg`. Native row crops and hashes accompany `data/processed/jar156_165_contained_marks_review.json`.

| Field | Table I no.156 | Table I no.165 |
|---|---|---|
| Container register number | Dotted blank; unknown | 7737 |
| Mound / trench | AB / Ex. P. I & II | F / G. G. Area |
| Square | Q24/18 | I9/5 |
| Depth below surface | 5 ft 3 in | 3 ft 4 in |
| Stratum | II | II |
| Container description | Very fragmentary | Do.; continues “Very fragmentary” from row 162 through rows 163–164 |
| Container measurements | Unreported | Unreported |
| Relevant contained object | Fragment of a unicorn seal | One of three goblets with pointed bases |
| Reported marks | No sign count or surviving script detail given | A series of four vertical strokes incised on one goblet |
| Separate find number / image reference | Unreported | Unreported |

Row 156 also lists a ram in the toys column, tumbler and dish sherds, and charcoal. The ram is a separate listed object, not a description of the seal's motif. The table's “unicorn seal” description establishes the excavator's classification; it does not establish that script survives on this particular fragment. The bones cell has a small printed weight fraction that is not needed for this task and is not numerically transcribed.

Row 165 lists three bones, three pointed-base goblets and a small discoid paste bead. Its remark explicitly applies the incisions to **one goblet**. The three goblets are a source object count; the four strokes are a source graphic count. Neither count supplies the mark's value, function or ancient unit, and the description does not establish whether it belongs to the Indus sign system. It also does not establish marking before/after firing, a numeric reading, the goblet's dimensions, or the timing of the mark relative to its placement in jar 7737. Blanks remain null; the explicit description-column ditto is expanded only within that column.

## Bounded locator attempts

The retained Vats OCR was searched for the literal container number 7737, the two grid references, and variants of the four-stroke/goblet description. It did not recover a numbered contained object or illustration reference. OCR missed the very table statements independently visible in the JPEGs, so these negative searches cannot establish that an illustration was never published.

The grid hit Q24/18 in the Vats narrative concerns copper rod 2551 at 10 ft 6 in, not this jar at 5 ft 3 in. It is not an identity bridge. The I9/5 locator is a dog figurine (7071) at 3 ft 2 in, with no stated connection to the goblet. A keyword hit in the Area G account concerns an incised ivory baluster, not an incised goblet. A separate paragraph on printed p.251 links jar **12414**, Trench IV, Mound F, to a unicorn seal in Plate LXXXVII,47; that is a different numbered container and location and is not used for row 156. The incised-pottery discussion on pp.286–287 gives examples and broad plate ranges, without identifying jar 7737 or its contained goblet. These OCR passages were used as rejected or unresolved locators, not as independently verified transcriptions of those pages.

The retained partial CISI/M77 text extracts and already generated CISI/M77 page OCR were searched for 7737 and the two grids. The secondary lipi CSV was searched only in Harappa identity/location metadata, excluding translation columns, for the container number or exact normalized grids. No eligible locator emerged. These are searches of available text, not complete visual audits of either corpus, and the container's number would not by itself identify the goblet. No bare-number or four-stroke shape match was promoted to identity. No additional broad source acquisition followed the missing identity references.

## Reproducibility and result

`scripts/persist_jar156_165_review.py` reproduces the bounded locator queries, preserves their hits and coverage, writes native crops and structured observations, and verifies SHA-256 pins. `data/processed/jar156_165_new_sources.json` records the one downloaded page and its separately retained HTTP headers. The result is two reported contained-mark contexts with unresolved physical object identities. No semantic or phonetic values were assigned; all 417 values remain null.
