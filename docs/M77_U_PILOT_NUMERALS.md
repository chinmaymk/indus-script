# Three-page primary M328 pilot

This manual pilot covers every M328 reference-column group on Mahadevan 1977 **printed pages 565–567/PDF pages 576–578**. It preserves all 47 groups, including damaged and non-stroke contexts. The ordering of a concordance groups similar contexts, so these counts are not estimates of corpus-wide prevalence or independent artifact frequencies.

The [ledger](../data/processed/m77_u_pilot_numerals.json) contains page and row locators, text references, side and line codes, full normalized reading-order token lists, primary doubt and loss marks, reviewer uncertainties, other-side context, and per-occurrence M328 records. The [packaging script](../scripts/build_m77_u_pilot_numerals.py) reproduces the ledger from explicit manual observations: `python3 scripts/build_m77_u_pilot_numerals.py`. It does not infer readings from OCR or join any canonical export.

## Observed inventory

| Measure | Count |
|---|---:|
| Indexed groups on PDF 576 / 577 / 578 | 15 / 16 / 16 |
| Total indexed groups and unique indexed lines | 47 |
| M328 occurrences within those lines | 51 |
| Reference U immediately preceded by one long stroke | 7 |
| Reference U immediately preceded by two long strokes | 31 |
| Other or lost immediate predecessor | 9 |
| Indexed lines with primary doubtful readings | 8 |
| Indexed lines with a hatched loss passage | 4 |
| Indexed lines with reviewer-unidentified visible glyphs | 4 |

Texts **1623 and 2847** each have three consecutive U signs in the indexed first-side line. Each contributes one reference-column occurrence and three within-line occurrences; their additional U-bearing third-side lines are stored as context rather than counted again as indexed pilot lines. The ledger identifies the reference occurrence separately. None of these three adjacent U signs was silently interpreted as a number.

## Discriminating contexts retained

- **4452, side 2, line 0**, PDF 576 group 9: `M095 M059 M328`. Four long vertical strokes are followed by a fish-shaped sign and then U. The four strokes do **not** immediately precede U.
- **5303, side 2, line 0**, PDF 578 group 2: `M167 M087 M328`. A branching sign precedes the two-stroke group. The line is longer than a bare stroke-plus-U pair.
- **4487 and 5481, side 2, line 0**, PDF 576 groups 7–8: a human/bow-like visible glyph precedes U. Its precise catalogue identity remains `UNKNOWN`; it is not replaced with a stroke sign.
- **4494, 5428, 4546 and 5281, side 2, line 0**, PDF 576 groups 1–4: a hatched lost passage precedes U. No stroke count is supplied.
- Doubtful one-stroke readings occur in 4552, 4354, 4667, 4566, 5414 and 4661. Doubtful two-stroke readings occur in 5429 and 4475. The primary asterisks remain attached to the stroke token.

## Authentication and notation

Primary sign-list printed page 32/PDF 43 distinguishes **M086 = one long stroke, M087 = two, M089 = three, M095 = four long strokes; M104 = four short strokes**. These are graphic counts, not decoded numerical values. **Correction:** an earlier version mistakenly described M104 as five long strokes. Reinspection of primary PDF43 and supplied `IM_417_150_PNG/104.png` confirms four short strokes. M104 is not assigned in any pilot row, so the row ledger and its counts are unaffected. M167 was checked against printed 33/PDF 44 and M328 against printed 34/PDF 45. Existing sign-list images and the newly rendered pages were visually inspected; their hashes are retained.

Token `*Mddd` preserves a primary doubtful reading. `LOSS` represents the primary hatched passage of one or more unknown signs. `UNKNOWN` means the reviewer could not safely identify an otherwise visible glyph; it does not stand for physical damage. Thus `complete_line=true` means no hatched loss passage is present, and does not by itself imply that every sign is identified or undoubted.

The reference column R aligns the occurrence being indexed. All M328 occurrences on that indexed line are additionally inventoried. Nearby lines belonging to the same text are retained as context, with their own side/line identifiers. An omitted four-digit reference on a continuation inherits the displayed text reference; side `2`, line `0` means the only line on the second side, not a second line on the first side.

Other-side strings are transcribed where legible, with unresolved glyphs retained rather than chosen from lookalike catalogue forms. Eleven groups satisfy the ledger's conservative pairing filter: both listed strings are fully identified, loss-free and undoubted. This filter is a review convenience, not a claim of archaeological independence or a rule about how upstream canonical records select sides. Canonical joins and any missing-line claims are left to a separate review.

All sequences follow the book's normalized right-to-left reading order. No translation, unit, numerical value, or equation is assigned. New output images are under `results/primary_pages/numeral-u-pilot-*`; no files were downloaded.
