# Primary audit of the five-stroke signs

The original Mahadevan 1977 concordance contains **six occurrences of M107**, not
just the five references retained by the candidate export. The missing occurrence
is the second line on the first side of object 1471. Recovering this line reconciles
all six occurrences with the original Table I positional counts. This is a
coverage correction, not evidence for a deciphered meaning.

## Complete M107 inventory in this publication

All sequences below follow the printed normalized right-to-left order. M-numbers
identify catalogue signs, not sounds or meanings. PDF page numbers are one-based.
The whole target entries were visually inspected; none of these six target lines
has a printed loss or doubtful sign.

| Reference | Primary heading | PDF / printed page | Printed metadata | Normalized sequence | M107 position |
| --- | --- | --- | --- | --- | --- |
| 1157 | Mohenjodaro | 54 / 43 | 100101 | M267 M099 M107 M162 | Medial |
| 6111 | Chanhudaro | 157 / 146 | 100001 | M107 M017 M087 M391 M087 | Initial |
| 7072 | Lothal | 162 / 151 | 100001 | M107 M169 | Initial |
| 8016 | Kalibangan | 166 / 155 | 100001 | M307 M086 M099 M098 M107 | Final |
| 9846 | West Asian Finds | 171 / 160 | 100401 | M171 M387 M097 M341 M107 | Final |
| 1471, side 1, line 2 | Mohenjodaro | 64 / 53 | Continuation 21 after 910011 | M104 M205 M107 | Final |

The six-reference list is printed together under the M107 index in **Concordance
R, PDF 365 / printed 354**. The order there is 6111, 7072, 8016, 1157, 1471, 9846.
The concordance codes for object 1471 are 11, 12, 20, 30, 40; M107 is in line 12.
These encode side and line. The Texts continuation `21` means second line,
direction 1; it must not be mistaken for side 2, line 1.

For 1157, the earlier [stroke review](../data/processed/stroke_curve_primary_review.json)
was reused and its exact row image inspected again. For 9846, the earlier
[foreign-sign review](../data/processed/m77_foreign_primary_parent_review.json)
was reused and a fresh full page and row crop were rendered and inspected. This
review checks the catalogue transcription, not the physical objects themselves.

## The omitted line on 1471

The Texts entry gives type code 9, miscellaneous. Its five printed lines occur on
four sides; none shows loss or doubt:

| Side | Line | Printed metadata | Normalized sequence |
| --- | --- | --- | --- |
| 1 | 1 | 910011 | M240 M302 M156 |
| 1 | 2 | 21 | M104 M205 M107 |
| 2 | 0 | 20001 | M098 M287 |
| 3 | 0 | 30001 | M287 M136 M323 M287 |
| 4 | 0 | 40003 | M102 |

M205 is the segmented wedge in the second line, not a fish sign. The existing
candidate record GLI-IND-M77-01471 retains only `+287-136-323-287+`, the third
side, while reporting `source_doc_count: 5`. Its exclusion for unrecovered
multiple source documents is appropriate. Adding M107 to that retained line
would create a false inscription; the recovered line requires its own side/line
identity. The candidate's unverified Harappa site label also disagrees with the
primary page's Mohenjodaro heading.

## Shapes and marginal totals

The labelled original sign list at PDF 43 / printed 32 distinguishes:

- M096: five long vertical strokes in one row.
- M106: five short vertical strokes in one row.
- M107: five short vertical strokes, three above two.

Table I, PDF 729 / printed 718, was inspected directly, including enlarged crops:

| Sign | Solus | Initial | Medial | Final | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| M096 | 1 | 2 | 13 | 6 | 22 |
| M106 | 1 | 18 | 18 | 1 | 38 |
| M107 | 0 | 2 | 1 | 3 | 6 |

The complete M107 inventory gives exactly two initial, one medial and three final
occurrences. Agreement between two parts of the same publication is an internal
consistency check. It does not independently validate every ancient mark or
modern sign classification.

The three shapes are compatible with a hypothesis involving five units, but
shape and distribution alone do not establish a numerical value, common sound,
or allographic identity. Keep their separate catalogue codes. Their different
stroke lengths and arrangements should remain visible in any comparison.

## Retained evidence and method

The [machine-readable review](../data/processed/five_stroke_primary_review.json)
contains all target lines, full object 1471, exact locators, crop boxes, rendering
commands and 26 SHA256-pinned evidence files. The source PDF remains in
`data/raw/`; this audit downloaded nothing.

The original PDF was rendered with the repository's `inspect_research_pdf.py`
and Poppler at a 3000-pixel longest edge. Full pages were inspected before crops;
crops used Pillow without resampling or contrast alteration. Numbered original
sign-list pages 32-35 were used to check the identified forms.

Failures retained in the review: OCR did not locate Texts 1471; tentative PDF 65
began at 1491, so the already retained PDF 64 was used instead. An attempted
preview of PDF 365 before rendering finished returned invalid image data; the
same live rendering process was allowed to finish and the completed image was
then inspected. Neither event was treated as negative textual evidence.
