# Primary object-type audit of 61 M328-bearing references

All **61 unique references below4400** selected from `data/processed/m77_u_recovered_lines.jsonl` were located in Mahadevan's primary *Texts* section and their object-type digits visually checked. None remains unverified.

| Primary code | Catalogue class | Selected references |
|---|---|---:|
| 1 | Seals | 13 |
| 2 | Sealings | 45 |
| 5 | Copper tablets | 2 |
| 7 | Ivory or bone rods | 1 |

The seals are1165,1206,1475,1477,1527,2035,2169,2188,2208,2604,4132,4147 and4231. The copper tablets are2905 and2906; the ivory-or-bone rod is1532. The remaining45 selected references are sealings. In particular, the selected4300-series records through4387 are explicitly printed with object-type code2; they must not be reclassified as miniature tablets merely from their short auxiliary strings or similarity to later objects.

## Primary evidence and procedure

The primary codebook, printed30/PDF41, defines **numerical column5** as object type. The four-digit reference occupies columns1–4; the first digit of the following six-digit metadata string is therefore the type. Column6 gives side and column9 gives line. Side0 and line0 retain their primary meanings, rather than being changed to1. Code3 denotes miniature tablets of stone, terracotta or faience; no selected reference in this bounded audit carries it.

Primary PDF text extraction was used only to locate entries. Each selected reference and its complete first-line metadata code were then read from rendered image strips. Some locator OCR was wrong:2208,2604 and3234 were found and resolved on the images, not copied from OCR. No candidate corpus object code or numeric reference range supplied a type.

The reviewed Texts pages are PDF55,56,64,65,67,70,74,75,88,92,93,95,101,102,112,113,114,117,118,119,120 and121. The corresponding printed-page offset is11. Metadata strips preserve reference/code association and neighboring entries; some odd-page footers extend beyond the strip. Printed-page locators were checked against the book sequence and available footer/text-layer evidence.

Examples that preserve materially different metadata:

| Reference | PDF / printed page | Literal first-line metadata | Type | First side / line |
|---|---|---|---|---|
| 1527 | 65 / 54 | `110012` | 1 | 1 / 1 |
| 1532 | 65 / 54 | `700001` | 7 | 0 / 0 |
| 1623 | 67 / 56 | `210001` | 2 | 1 / 0 |
| 2604 | 88 / 77 | `110012` | 1 | 1 / 1 |
| 2905 | 95 / 84 | `510001` | 5 | 1 / 0 |
| 2906 | 95 / 84 | `510001` | 5 | 1 / 0 |
| 4316 | 117 / 106 | `210001` | 2 | 1 / 0 |
| 4386 | 121 / 110 | `210011` | 2 | 1 / 1 |
| 4387 | 121 / 110 | `219301` | 2 | 1 / 0 |

All61 literal codes and locators are in `data/processed/m77_u_types_structure.json`; typographic tracking between digits is collapsed without changing digits. The ledger retains the first displayed line, which need not be the M328-bearing line. Its direction code is not propagated to other lines or sides.

## Scope and reproducibility

Source: `data/raw/mahadevan_1977_text.pdf`,119302608 bytes, SHA-256 `6dcdd074a0174e5fab149590fbbf82342711d345764e9763f8e5e92c81cf7f99`. The ledger records the selection-input hash, source hash, codebook-image hash and all22 rendered-image hashes. The final render parameters are180dpi, crop x50/y0/width700/height2300; narrower preliminary renders were superseded before hashing.

Validation establishes exact set equality between the61 requested references and61 verified ledger rows, unique reference keys, six-digit metadata strings, and agreement between the type field and the first metadata digit. These are primary catalogue classifications, not new material examinations, an unbiased corpus frequency estimate, or semantic readings of M328. No downloads or changes to existing corpus ledgers were made.
