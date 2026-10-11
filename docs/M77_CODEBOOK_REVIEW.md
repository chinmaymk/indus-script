# Mahadevan 1977: primary codebook review

The primary page images authenticate the direction, object-type, asterisk and loss-marker conventions below. **Object code 8 is not defined**, and the printed loss marker represents an unknown number of signs. The upstream digital `000` and `doc_count` fields require separate interpretation; neither is a named convention in the inspected primary codebook.

Source: Iravatham Mahadevan, *The Indus Script: Texts, Concordance and Tables* (1977), existing `data/raw/mahadevan_1977_text.pdf`. Printed pages 19, 20, 30 and 31 correspond to PDF pages 30, 31, 41 and 42. All four rendered pages were visually inspected. The [machine-readable ledger](../data/processed/m77_codebook_review.json) records the source hash, image paths, exact mappings and limits. No downloads occurred.

## Verified codes

| Direction code | Meaning |
|---|---|
| 1 | Right to left |
| 2 | Left to right |
| 3 | Single sign in the line |
| 4 | Top to bottom |
| 5 | Symmetrical arrangement of signs |
| 9 | Doubtful because of damaged or illegible signs |
| 0 | No line of text |

Code 6, printed 31/PDF 42, defines direction for **each line**, in column 10 of the *Texts*. Note 4 specifies that right and left refer to seal impressions and originals of other objects.

| Object-type code | Meaning |
|---|---|
| 1 | Seals |
| 2 | Sealings |
| 3 | Miniature tablets of stone, terracotta or faience |
| 4 | Pottery graffiti |
| 5 | Copper tablets |
| 6 | Bronze implements |
| 7 | Ivory or bone rods |
| 8 | **Not defined in the table** |
| 9 | Miscellaneous inscribed objects |

Code 2, printed 30/PDF 41, defines object type in column 5. The ledger also records the side and line codes: side `0` means the only side, with `1`–`6` enumerating multiple sides; line `0` means the only line on a side, `1`–`3` enumerate lines, and line `9` means a symbol-only side. Direction `0`, side `0`, line `0` and field-symbol `00` must not be conflated with a sign token.

## Printed normalization and damage

Sections 13.2(i–iii), printed 19–20/PDF 30–31, establish two distinct operations. Seal texts are copied as impressions. Then **every printed line is normalized to run right to left**, independently of its actual direction, which is retained in a numerical metadata code. Signs are also normalized; variants are not distinguished in the *Texts*, *Concordance* and *Tables*.

Consequently, a digital row's `direction=2` is not by itself an instruction to reverse its exported array. The digital serialization order relative to the normalized printed line must first be checked.

The asterisk marks a doubtfully read sign, positioned at its top right. The hatched block marks an illegible or lost passage containing **one or more signs**. Section 12.1 explicitly explains that the number of lost signs cannot be counted. No printed `000` convention appears on these pages. Canonical digital record 1001 contains raw token `0` represented as `000` in its diplomatic string; this shows padding within that digital record, not an independently verified bridge to the primary loss block. Treating each `000` as exactly one missing sign would invent text length.

## A concrete multiline warning

A subsequent [record1001 image check](M77_EXPORT_PRIMARY_PILOT.md) verifies the
digital `000` to hatched-span correspondence for that particular first line.
It supports excluding such rows without assigning an exact missing-sign count;
it does not make `000` a printed codebook convention.

The specimen for text **2405**, printed 20/PDF 31, has six sides and seven displayed line entries. Its direction codes, in displayed order, are `1, 2, 1, 1, 1, 3, 9`. The final line is wholly illegible and is included because the other lines are legible. The [reviewed page](../results/primary_pages/m77-codebook-31.png) makes this directly inspectable.

The canonical digital record with `source_object_id="2405"` has `doc_count=7`, but only one sequence, `+293-123-343-065-294-342+`, and one `direction="1"`. The numerical coincidence with seven primary entries is a useful lead; it does not establish the general meaning of `doc_count`. One sequence and one direction value cannot preserve all seven primary entries and their different directions.

**The exported sequence matches the first side's only line.** Comparing the [magnified specimen](../results/primary_pages/m77-codebook-2405-first-line-detail.png) with primary sign-list pages 32–35/PDF 43–46 identifies displayed left-to-right `M342 M294 M065 M343 M123 M293`. Reading the normalized page right-to-left gives exactly `M293 M123 M343 M065 M294 M342`. Its metadata is side `1`, line `0`, field symbol `01`, direction `1`. The other six displayed line entries are absent from this canonical row's single sequence. This authenticates one concrete truncation witness and its order; it does not establish serialization for every exported row. The ledger preserves crop coordinates, reviewed sign-list images and image hashes.

The primary corpus count is 2,906 texts in **3,573 lines**, with 13,372 legible sign occurrences (section 13.1). A digital export with 2,906 rows therefore does not demonstrate that all lines were retained. Multiline, multiside and symbol-only entries need explicit source-level accounting before this export supports sequence statistics.

## Reproducing the page renders

Use the existing `scripts/inspect_research_pdf.py` with source `mahadevan_1977_text.pdf`, prefix `m77-codebook`, pages `30 31 41 42`, `--render-only`, and `--scale 2600`, supplying the local `pdftoppm` path. The script-generated `results/m77-codebook_extraction.json` retains rendering metadata. The visual authentication is recorded separately in this review and its ledger; rendering alone does not validate transcription.
