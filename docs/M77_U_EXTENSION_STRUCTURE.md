# M328 concordance extension: PDF 585–587

Primary visual review completed 2026-09-23. The inspected pages are printed **574–576**, and every page remains in the **M328** concordance block. The ledger records **48 indexed sightings, 48 distinct reference/side/line keys, and 47 object references**. This is coverage of these three pages only.

## Method and identifiers

Each full page was rendered at 150 dpi; special cases were inspected in 300 dpi source crops. Only the line whose indexed M328 is aligned with the printed R-column is transcribed. Other sides shown as context are excluded. Tokens follow normalized right-to-left order; the object's actual direction is not inferred from this layout.

M089 was authenticated against the numbered primary sign list on printed32/PDF43: three long vertical strokes in one row, distinct from short-stroke M102. M328 was authenticated against label328 on printed34/PDF45. M028 in reference5283 was checked against enlarged numbered labels27/28; the distinctive bow component matches28, not27. No secondary export was consulted to supply glyph identities.

`*M...` preserves Mahadevan's primary doubt mark. `LOSS` would represent a positive damaged span of unspecified length; `UNKNOWN` would represent a visible glyph that this reviewer could not identify. Neither occurs in the indexed lines here, although some excluded contextual lines contain loss. The ledger retains these separate fields rather than equating absence, damage and reviewer uncertainty.

## Indexed lines

Unless specified below, the indexed line is side2/line0 (`20`) with tokens `M089 M328`. Line0 means the only line on that side. All indexed M328 positions are zero-based index1.

| PDF / printed page | References in printed index order |
|---|---|
| 585 / 574 | 5411, 5412, 5416, 5419, 5421, 5422, 5423, 5425, 5434, 5437, 5442, 5449, 5457, 5499, 5413, 4352 |
| 586 / 575 | 4444, 4456, 4605, 4704, 4666, 4602, 4646, 5276, 4523, 4457, 4455, 4492, 4504, 4510, 4371, 4674 |
| 587 / 576 | 5274, 4596, 4373, 4702, 5283, 4490, 4374, 5496, 4673, 4718, 5495, 5478, 4410, 4468, 4675, 5413 |

| Exception | Complete indexed tokens / metadata |
|---|---|
| 5425, PDF585 entry8 | `M089 *M328`; the source doubts U |
| 5449, PDF585 entry12 | `*M089 M328`; the source doubts the stroke sign |
| 4596, PDF587 entry2 | `M089 *M328`; the source doubts U |
| 5283, PDF587 entry5 | `M089 M328 M028`; U is not the last token |
| 5413, PDF587 entry16 | Side3/line0 (`30`), `M089 M328` |

Reference5413 is indexed once by side20 on PDF585 and once by side30 on PDF587. Both sides are shown on both pages, but their horizontal placement identifies which occurrence is indexed. Counting both printed sides at both sightings would double count. They remain two separate line keys.

There are **44 plain `M089 M328` lines**, **2 `M089 *M328` lines**, **1 `*M089 M328` line**, and **1 `M089 M328 M028` line**. These are transcription counts, not independent artifact counts, quantity meanings or evidence of a reading.

## Evidence and validation

Source: `data/raw/mahadevan_1977_text.pdf`, 119302608 bytes, SHA-256 `6dcdd074a0174e5fab149590fbbf82342711d345764e9763f8e5e92c81cf7f99`.

The machine-readable ledger is `data/processed/m77_u_extension_structure.json`. It contains the requested normalized row keys, exact indexed positions, page/row locators, explicit doubt/loss/unknown fields, and SHA-256/size metadata for the source, numbered-list images and nine inspected renders. Render prefix: `results/primary_pages/structure-u-extension`.

Validation checked 16 indexed sightings per page, 48 unique reference/side/line keys, and that every indexed position points to M328 or source-doubtful M328. No canonical-corpus omission or duplication claim is made here; that comparison belongs to the parent's joined corpus audit.
