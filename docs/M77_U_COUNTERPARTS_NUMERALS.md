# Primary counterpart recovery: numerals partition

The frozen `partitions.numerals` selection is fully accounted for: **76 references, 84 separate counterpart text lines, and 11 symbol-only entries**. Every accepted counterpart glyph was visually checked in Mahadevan's primary *Texts* against the primary sign inventory. The ledger is `data/processed/m77_u_counterparts_numerals.json`; it preserves the protocol fingerprint, PDF and image fingerprints, exact side/line identifiers, complete token sequences, and per-reference locators.

The evidence is PDF pages 129–139, 144, 146 and 147 (printed 118–128, 133, 135 and 136). Full-page images retain the reference, metadata, and all continuation rows; enlarged glyph-column crops were viewed directly from the same PDF. No new source was downloaded. Candidate strings provided possible sign IDs but were not accepted without visual comparison.

Only the exact selected field IDs in the frozen protocol are excluded. Other text is kept as separate positioned lines, in the catalogue's normalized right-to-left reading order. The counterpart bundle must not be flattened or reduced to whichever line appeared in a one-string export.

Eight references have two counterpart text lines: **4576, 4581, 4586, 4588, 4589, 4591, 4642 and 4645**. Examples that materially affect matching are:

| Reference | Side 1, line 0 | Side 2, line 0 | Selected field |
| --- | --- | --- | --- |
| 4576 | M059 | M067 M244 M149 M342 | side 3, line 0 |
| 4581 | M137 | *M119 M087 M342 M176 | side 3, line 0 |
| 4586 | M048 M342 M176 | M267 M402 M149 | side 3, line 0 |
| 4588 | M059 | M006 M176 | side 3, line 0 |
| 4589 | M048 M047 M379 M245 M245 | M307 M267 | side 3, line 0 |
| 4591 | M059 | *M119 M087 M342 M176 | side 3, line 0 |
| 4642 | M059 | M245 M245 M307 M342 M176 | side 3, line 0 |
| 4645 | M059 | M245 M245 M307 M342 M176 | side 3, line 0 |

These single-fish or X entries have text metadata and cannot be dropped as decoration. Conversely, the third-side entries for 4574, 4575, 4580, 4582, 4587, 4593, 4597, 4641, 4647, 4649 and 4718 have primary line code 9 and direction 0. The codebook identifies these as field-symbol-only entries. Their literal continuation metadata is retained separately; no script tokens are invented for them.

There are **65 clean, fully checked counterpart lines**. Twelve lines contain primary hatching (`LOSS`); ten contain at least one primary doubtful sign (`*Mddd`), with overlap. No unresolved visible glyph required `UNKNOWN` after comparison with the inventory. References 4660 and 4671 have a damage-only counterpart on side 1: `LOSS` is a positive printed lost passage, not an empty or nonexistent counterpart. Neither is suitable for clean-text matching. A hatching block does not imply that exactly one sign is missing.

The source inventory preserves distinctions relevant to exact matching, including M059/M072, open-ended M149/closed M150, M015/M012, M102/M089, and the modified M343/M342/M336 forms. Reference 4718 reads M343 M162 M343 M086 M336 M089 M211; each M343 includes one short internal stroke as part of the glyph, not an independent text token. Reference 5269 reads M409 M096 M171, with five long strokes assigned M096 from the primary sign list.

Validation checks exact coverage of the 76 frozen references, unique counterpart line IDs, exclusion of all selected field IDs, valid M001–M417 tokens, and source/image fingerprints. `all_counterpart_lines_accounted_for` means that every other line printed for this reference in *Texts* is inventoried. It does not certify an intact original object, an independent archaeological rereading, or a semantic interpretation. No commodity, numeral value, or unit is assigned.
