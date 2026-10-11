# M77 field-symbol metadata: primary review

Date: 2026-10-10. Release 5 cannot yet compare text across identified seal-animal classes. Its 185 references comprise 182 with the unicorn category and three with an uncertain animal. The only side coded as having no field symbol belongs to an object whose other side has a unicorn. Further corpus expansion and complete Table V extraction are deferred for the finite motif-transfer route using the separately frozen protocol; no W-to-M sign mapping or new semantic conclusion follows from this metadata update.

This review visually checked nine pages of the existing `data/raw/mahadevan_1977_text.pdf`. The [ledger](../data/processed/m77_field_symbol_review.json) pins that PDF, every reviewed render, and the release-4 corpus. OCR located passages but did not authenticate the readings. No download was needed.

## Native categories and counting units

| Code | Primary classification, paraphrased | Verified location |
| --- | --- | --- |
| `01` | Unicorn motif, usually facing a ritual object | Appendix II, printed 793 / PDF 802 |
| `35` | Animal of uncertain identity, usually bovine in appearance | Appendix II, printed 794 / PDF 803 |
| `00` | No field motif on this side | Code 4, printed 30 / PDF 41 |
| `99` | Motif obscured by damage or illegibility | Code 4, printed 30 / PDF 41 |

The appendix prints frequencies 1,159 for code `01` and 62 for `35`; these are source totals, not release-4 observations. It gives figures 1–7 for `01` and explicitly provides no illustration for `35`. Code `35` must not be relabelled as an identified bull, nor `00` treated as damaged or missing metadata. A source-classified unicorn is not a decoded word or an independent zoological identification.

Sections 8.1–8.2, printed 8–9 / PDF 19–20, define a field symbol separately from script signs. Each side has one combined motif category or none: a scene with several animals may be one category. Sometimes the symbolic shape of an object supplies the category for each text-bearing side. Motif-only sides can also receive codes. Consequently, these codes are broader than an animal-species variable.

Section 5.1, printed 6 / PDF 17, assigns a reference to an object and its text, which can span several sides and lines. Sections 7.2–7.3 explain that blank sides are not numbered, text-bearing sides precede motif-only sides, and side order is provisional and may use textual evidence. Section 9.1 distinguishes lines within sides. Repeated line-level field codes therefore do not give independent animal observations.

## Current release 5

The [release-5 metadata profile](../results/m77_metadata_v5.json) records 198 lines, 186 represented sides and 185 references, all coded as seals. Field code `01` occurs on 193 lines and 182 sides/references; `35` on four lines and three sides/references; `00` on one line and one side/reference. The sole overlapping reference remains 1018 with codes `00` and `01`. Thus the larger release still has no wholly motif-absent object group and no confirmed second specific animal class. These counts do not turn the uncertain code `35` into a bull category or establish independent artifacts/dies.

## Historical release 4

| Code | Printed lines | Distinct represented sides | Objects carrying that code on at least one side |
| --- | ---: | ---: | ---: |
| `01` | 129 | 121 | 121 |
| `35` | 2 | 1 | 1 |
| `00` | 1 | 1 | 1 |

The 132 lines represent 123 sides on 122 objects. Both `35` lines belong to reference 1001, side 0. The `00` line is reference 1018, side 1; reference 1018, side 2 has `01`. Object presence counts thus overlap. At whole-object association level no release-4 object is wholly without a recorded motif. Treating the three row-level codes as three animal classes would confuse uncertainty, side-level absence, and repeated lines.

Code 1 on printed 30 / PDF 41 groups reference numbers by site and source publication. In particular, 1001–1905 is a Mohenjodaro block attributed to MIC volume III. The inspected rules do **not** establish a general ordering by animal within that block, and they supply no phase dates. The observed near-uniform early-page motif distribution must remain a sampling limitation rather than an assumed chronological or zoological ordering rule.

## Table V offers broader evidence, with different semantics

The opening Table V page is printed 760 / PDF 769; its last page and notes are printed 775 / PDF 784. These endpoints were visually checked. The existing OCR locates intervening Table V headings, but this bounded review did not authenticate every intervening page. The alternative scan's previously checked PDF 770 corresponds to printed 760; offsets must not be transferred between scans.

Section 15.7, printed 24 / PDF 35, and Table V notes 3–4 explicitly use the whole object for association: a sign and a field motif can be associated across different sides. Signs without any associated motif are excluded. This is different from asking whether a text and animal share a seal face.

Table V prints sign glyphs and repeated field-code/frequency pairs. A single sign's entries can wrap across physical rows. The first page confirms that extraction is feasible, but each glyph must be matched to the primary sign list; assuming that row number equals M77 sign number would silently mislabel entries if a sign is omitted. Full glyph groups, page boundaries, and omitted categories need coverage checks before assigning zeros.

The notes identify occurrence frequency and whole-object association, but do not explicitly settle how repeated instances of the same sign within one object, or repeated same-code motifs across sides, affect a cell. Those counting details need validation against primary object examples before interpreting the matrix as binary object incidence or token frequency. The inspected Table V notes also do not separately specify treatment of code `99`. Do not derive `00` counts by subtracting Table V sums from Table I totals: different units and multiple cross-side associations could invalidate that calculation.

A complete checked Table V extraction could support broader sign–motif descriptive comparisons without waiting for all text sequences. It would still aggregate away joint site, phase, object type, and duplicate dependence. It cannot by itself distinguish personal names from offices, identify a language, or establish that an associated sign names an animal.

## Reproduction

Renders use `scripts/inspect_research_pdf.py`, source `mahadevan_1977_text.pdf`, `--render-only --scale 3000`, and the available Poppler `pdftoppm` executable. Prefix `m77-v5-fieldcodes` covers PDF pages 17, 19, 20, 41, 802 and 803; `m77-v5-fieldcodes-table` covers 784; `m77-v5-fieldcodes-context` covers 35 and 769. Their extraction manifests and full-page PNGs are saved under `results/`. An initial attempt to view page 803 while rendering was unfinished failed; it was reopened and checked after successful completion.

Release counts are derived from `corpus_v4.json`: count rows by `field_symbol_code`; deduplicate `(reference, side)` for side counts, verifying the code is constant across a side's lines; group the sets of side codes by reference for object presence. The separate reproducible [metadata profile](../results/m77_metadata_v4.json), generated by [profile_m77_metadata.py](../scripts/profile_m77_metadata.py), reports raw-code counts without inferring these labels. These are metadata calculations, not new sign transcriptions or artifact identifications.
