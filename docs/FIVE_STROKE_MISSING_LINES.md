# Five-stroke coverage audit: M096 and M106

The five missing occurrences are on omitted sides of records already present in the secondary export. Recovering those sides reconciles both total frequency and all four position columns in Mahadevan's Table I. This repairs a coverage gap; it supplies no numerical, phonetic, or semantic values and does not merge M096 with M106.

| Sign | Export occurrences | Newly recovered | Combined | Table I: solus / initial / medial / final |
|---|---:|---:|---:|---|
| M096 | 20 | 2 | 22 | 1 / 2 / 13 / 6 |
| M106 | 35 | 3 | 38 | 1 / 18 / 18 / 1 |

The target occurrences were enumerated visually from the entire M096 concordance block, printed pp. 310–311 (PDF 321–322), and M106 block, printed pp. 352–354 (PDF 363–365). The ledger records all 22 and 38 reference/side/line locations. It does not claim to authenticate every other token in the 55 previously exported occurrences.

## Recovered complete printed fields

Tokens follow the publication's normalized right-to-left display. `*` preserves the source's doubtful-sign mark; `LOSS` is an illegible or lost passage of one or more signs, with unknown extent.

| Reference | Side / line | Tokens | Texts printed page / PDF | Concordance printed page / PDF |
|---|---|---|---|---|
| 2921 | 1 / 0 | M096 | 85 / 96 | 310 / 321 |
| 1325 | 2 / 0 | M025 M409 M096 | 49 / 60 | 311 / 322 |
| 8301 | 2 / 0 | M106 | 158 / 169 | 353 / 364 |
| 2923 | 2 / 0 | M387 M015 M104 M106 M312 | 85 / 96 | 354 / 365 |
| 2636 | 2 / 0 | M267 M099 *M106 LOSS | 78 / 89 | 353 / 364 |

Each recovered field was viewed in both the original Texts and its concordance listing, then checked against the sign list (printed pp. 32, 34–35). Full pages and legible detail crops remain in `results/primary_pages/`; exact pixel boxes, rendering commands, original PDF fingerprint, candidate-export fingerprint, and 27 evidence-file hashes are in the [review ledger](../data/processed/five_stroke_missing_review.json). The separate [recovered-lines file](../data/processed/five_stroke_missing_lines.jsonl) preserves each side as its own record. No candidate-corpus edits were made.

Reference 2636 appears twice in the M106 concordance with both sides displayed each time. These are two target occurrences on one two-sided object, not four occurrences or two new objects. The missing side has doubt and loss and must be excluded from intact, doubt-free context comparisons. Its retained source metadata fragment is `22501`; the last digit gives direction 1.

The added 2921 and 8301 fields are solus signs (direction code 3). The added 2923 field has actual direction code 4, defined in the codebook as top to bottom; the publication's normalized row still determines the token order used here. Reference 1325 side 2 has direction code 1. Do not reverse or concatenate these fields based on the exported record's direction or document count. Export 8301 reports two source documents, consistent with the two printed sides. An earlier draft incorrectly carried over the one-document count from the OCR-misidentified reference 6301; that prose error is corrected here.

## What changed and what did not

M096 gains one solus and one final occurrence. M106 gains one solus and two medial occurrences, one of them doubtful in a damaged field. These increments exactly explain the export/Table I discrepancies. They show that an export restricted to one retained sequence per reference misses meaningful sign contexts.

The concordance and Texts are two presentations within the same publication. Agreement is a transcription check, not an independent ancient witness. This audit does not establish object provenance, manufacturing dates, quantities, allography, or a decipherment. Any comparison of the three five-stroke codes must keep doubtful/damaged fields separate and identify the selection scope of intact-field tests.

## Locator errors retained

OCR misread 8301 as 6301; visual inspection corrected it before final transcription. Early tentative labels for the two non-stroke signs in 1325 were replaced with M025 and M409 after sign-list inspection. PDF 41–42 were initially requested as possible sign-list pages; they proved to be the codebook and were useful for checking side, line, direction, doubt, and loss conventions. PDF 323 was rendered as a boundary locator; it was not needed for the target counts. One attempt to view PDF 364 before its render process finished failed with an unsupported-image error; the same process was allowed to finish and the final image was reviewed successfully.
