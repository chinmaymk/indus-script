# One authenticated artifact, two tokenizations of the paired grids

CISI M-81, excavationC3133, Marshall seal180 and Mahadevan text1180 refer to
one artifact through independently checked catalogue links. On this artifact,
the secondary export's single token **W617** spans the two grid drawings that
Mahadevan prints as **M245 M245**. This is an authenticated local tokenization
correspondence. It does not establish a numeral, semantic repetition, phonetic
reduplication, or a global rule that every W617 must expand identically.

## Identity chain and primary evidence

1. CISI1 printed366/PDF402 explicitly gives M-81, excavation **C3133**, museum
   **ASI63.10.321**, Finnish1180 and photoHU391 (other impression references
   are listed separately). The existing primary India review checked this row;
   its retained [metadata crop](../results/primary_pages/ending-india-m81-metadata.png)
   was reused here.
2. Marshall VolumeII **printed403/PDF54**, row **180**, explicitly gives
   **C3133**, 1.05×1.05in, typeB, white steatite, depth6ft0in below surface.
   The [row crop](../results/primary_pages/double-grid-mic180-table.png) establishes
   MIC180↔C3133. Printed404/PDF55 was a proposed navigation lead, not the
   actual table page; no unnecessary new page was downloaded.
3. The retained Marshall VolumeIII leaf191 contains numbered seal **180**.
   Its [old impression](../results/primary_pages/double-grid-mic180.png) has the
   same text arrangement, animal and stand as CISIM-81's original/impressions
   on printed34/PDF70. In particular, the two rectangular gridded forms and
   neighbouring fish/strokes appear in the same order after appropriate reflection
   of original versus impression. The several views count as one artifact.
4. Mahadevan AppendixV, **printed818/PDF827**, explicitly maps references
   **1001–1560** to MICVolumeIII items **1–560 respectively**. The
   [rule crop](../results/primary_pages/double-grid-m77-mic-rule.png) therefore
   yields MIC180→Mahadevan1180. This is an application of a printed catalogue
   rule, **not** an inference from the coincident Finnish1180 number.
5. Mahadevan **printed44/PDF55**, reference1180, visibly prints two separate
   grid forms in the line. The [line crop](../results/primary_pages/double-grid-m77-1180.png)
   retains the reference and metadata code100101. The adjacent grids match the
   numbered sign-list glyph245 on **printed34/PDF45**; the
   [glyph crop](../results/primary_pages/double-grid-m245-sign.png) includes245.

The code100101 is a metadata string accompanying the text, not six additional
signs. No missing sign is invented to reconcile the counts.

## The correspondence, with ordering kept explicit

The W export row2608.1 is `+527-555-240-002-617-070+`: six tokens, in its
preserved file order. The Mahadevan-derived digital sequence is
`M155 M245 M245 M099 M067 M222 M254`: seven tokens in reading order. Its
printed line supports that sequence when read right-to-left. The following
alignment is presented in the W file order/left-to-right impression order:

| W export unit | Corresponding Mahadevan unit(s) on this artifact |
|---|---|
| W527 | M254 |
| W555 | M222 |
| W240 | M067 |
| W002 | M099 |
| **W617** | **M245 M245** |
| W070 | M155 |

The important primary observation is the pair of grids: the print contains two
separately drawn grid forms and the physical photographs show their paired
arrangement. The secondary W sequence packages that span as one unit. The
numeric M codes are checked against the printed glyphs and existing sign list;
this is not a new independent machine transcription of the whole corpus.

The previous India review's “six encoded sign units” refers to the six W units,
including the paired-grid unit. It should not be interpreted as six independent
outlined glyph drawings or as proof that the ancient writer treated the grids
as one grapheme. The photos alone do not settle the ancient segmentation rule.
Nor does standardization in the sign list establish that every physical grid had
exactly the same number of internal cells; no cell-count numerical reading is
assigned here.

This case shows why exact string matching across inventories can fail even when
artifact identity is correct: a one-token grid pair in one encoding is a
repeated two-token sequence in another. The safe implementation is a documented,
artifact-specific span alignment, with a broader conversion rule left unproven.

## Provenance and attempts

No downloads were necessary; all primary source files were already retained in
`data/raw/`. `double_grid_new_sources.json` records an empty new-source list.
The existing source registry was not modified. The M77text page55 was rendered
anew; the extraction record specifies source hash, scale and page. Reproducible
fractional crops are in
[`render_double_grid_crops.py`](../scripts/render_double_grid_crops.py).
All crops were inspected after generation, with no image retouching or invented
strokes. Full pages retain the surrounding rows and catalogue headings.

The initially suggested Marshall page404 was resolved to403 by the existing
page's visible row180. TableI grid forms were inspected as a cross-check, but
the **numbered sign list** supplied the explicit245 label; the unnumbered
frequency table alone was not used to assign that code. No failed download or
unresolved network process remains.

The [machine-readable review](../data/processed/double_grid_primary_review.json)
records identity links, evidence hashes and the narrowly scoped alignment.
Semantic and phonetic values remain null.
