# Roof-cross coverage extension: M77 references3319 and3320

2026-09-27. Bounded primary-source extension; semantic and phonetic values remain null. Previous reviews and central corpora are unchanged.

**Both numbered M77 entries contain a clear normalized roof-cross M138 on their second face. Both also have a separate two-sign first face omitted from the retained flattened exports. Explicit excavation and museum-number matches authenticate3319 as CISI1 M510 and3320 as M509; both pairs of photographs are recovered.** This does not establish that the secondary W678 category covers all M138 occurrences.

## Exact retained export syntax

The records in `data/raw/glossa_icit_export.json` give3319 exactly as `+000-342-067-138+` and3320 as `+201-099-048-342-067-138+`. There is **no asterisk** in3319. The corresponding canonical-object records use the same strings, with raw arrays `["0","342","67","138"]` and `["201","99","48","342","67","138"]` and `doc_count:2`. These are secondary export strings, not literal numeric strings printed by M77. They retain the longer second face and omit the two-sign first face; they must not be concatenated or treated as complete object records. The `000` is an unknown span with unresolved original length, not an identified sign or an automatically single missing sign.

## Complete primary printed entries

M77 printed93/PDF104 prints the following, with signs read in the catalogue's normalized right-to-left order. Both complete numbered entries fit on this page; neither has an additional line on a neighbouring page.

|Reference and field|Literal metadata|Tokens in normalized reading order|Primary qualification|
|---|---|---|---|
|3319:1:0|510001|M287 M319|Two script signs, not an animal icon field.|
|3319:2:0|20001|unknown span; M342 M067 M138|Rightmost hatched block in the printed drawing.|
|3320:1:0|510001|M287 M319|Same normalized two-sign field.|
|3320:2:0|20001|M201 M099 M048 M342 M067 M138|Six normalized signs; no hatched span printed.|

The first digit5 marks copper tablets. Each face has field00, line0, direction1; the second line omits the repeated object-type digit, as specified by the established codebook. M287 is the curved arc, and M319 the pointed loop with an inward terminal stroke, checked against the original numbered sign list on printed34/PDF45. M138 is the peaked cap over a diagonal cross, checked against the primary numbered representative previously retained. The exact first-field signs are preserved without forcing them into the second-field string. No reading of the hatched span in3319 is supplied by analogy with3320.

## Object identity and provenance

M77 AppendixV printed820/PDF829, copper-tablet subsection, explicitly records3319 as DK4067 / ASI63.10.271 and3320 as DK4069 / ASI63.10.270. CISI1 basic data printed369/PDF405 independently lists M510 with DK4067 / ASI63.10.271 / HU264, and M509 with DK4069 / ASI63.10.270 / HU263. Finnish column values0420 and0421 are not used to identify a Mahadevan reference. The agreement in excavation and museum numbers establishes the two joins.

CISI1 printed128/PDF164 supplies M509A/B and M510A/B beneath the heading identifying incised copper tablets. The book's A/B order differs from M77's field order: **CISI A is M77 side2; CISI B is M77 side1.** Each A/B pair is one catalogued object. Two distinct identifiers and separately photographed surfaces support two separately catalogued physical tablets, not four objects. Shared manufacture, transaction, chronology or archaeological independence is not established. No exact depth, room, trench or find group was recovered by this bounded review; these are left null rather than inferred from DK.

## Observations from all four photographs

M509A shows a several-sign row on a roughly square tablet with surface scratches and mottling. A left-end diagonal/capped configuration and adjacent narrow upright/fish-like and U-like forms are broadly compatible with the normalized second face. Fine strokes overlap scratches and are unevenly visible; the photograph does not certify every normalized stroke or restore variants. M509B shows a pointed loop with an internal upward stroke and a separate curved stroke to its right; additional surface streaks are not promoted to extra signs. This broadly supports the two-sign first face.

M510A is similarly roughly square but has a different surface and outline, with a painted museum number matching63.10.271 visible upside down near its lower edge. The inscribed row is weak and scratched. Its left/central surviving forms broadly agree with the normalized second face; the right-hand part is poorly resolved. The primary M77 drawing's hatched unknown span remains unknown. Its extent is not read from this photograph and it is not filled from M509. M510B shows a central pointed loop/inward stroke and a separate curved mark to the right, broadly corresponding to the first-face pair.

For both tablets, complete outer outlines of the illustrated faces are visible and there is no securely identified large missing chunk in this scan. Fine surface loss, corrosion, abrasion and photographic contrast cannot be cleanly separated. Surface impairment and reading loss must not be mislabeled physical fracture. The roof-cross is **secure as a primary normalized catalogue occurrence** in both entries; the photographs authenticate their artifacts and broad layouts but do not provide an independently exact stroke transcription of M138 in either case. Four unretouched face crops preserve these limitations for review.

## Coverage consequences and exclusions

The three secondary W678 rows supplied as the task locator were not used as a complete M138 inventory. This extension authenticates two additional M77 native occurrences in copper tablets at Mohenjo-daro, with complete field structure, beyond the previously reviewed Harappa entries. It supplies no W-code mapping for these two tablets. It does not merge them with H1319/EH407, H1320/EH558, or the fragmentary Lakhanjo-daro record, and does not promote the unresolved5444 photo identity. The original task's approximate3319 asterisk notation is corrected only in this local ledger.

## Research log and failed paths

1. Located3319/3320 in retained exports and extracted primary text. Original extraction revealed two printed fields each; raw OCR glyph strings were not treated as transcriptions.
2. Rendered M77 PDF104 and829 at4200 pixels. Inspected full entries, exact appendix rows and numbered sign representatives. Recovered four separate script fields, including the first-face pair omitted by both exports.
3. Rendered CISI1 PDF405 at4200 pixels. Matched both DK and ASI identities. Rejected Finnish-number equality as a join mechanism.
4. Text-layer search in CISI1 did not recover photo locators. Used existing nearby photo pages160/163/180 to locate the exact sequential plate, then rendered PDF164 at5400 pixels. Preserved all four relevant face images and their labels.
5. Attempted to verify fine roof/cross morphology directly from photographs. Broad layouts are compatible, but scratches and weak contrast prevent independent certification of all strokes. No enhancement, tracing or reconstruction was substituted.
6. Stopped with unknown span3319 unresolved and no exact find-depth metadata. No new downloads were needed.

## Reproduction and evidence

Renders are recorded in `results/roof-cross-extension-m77_extraction.json`, `results/roof-cross-extension-cisi_extraction.json`, and `results/roof-cross-extension-photo_extraction.json`. `scripts/render_roof_cross_extension_crops.py` regenerates ten crops; `data/processed/roof_cross_extension_crop_manifest.json` stores their coordinates. The machine-readable review pins source PDFs, source exports, complete renders, crops, sign-list evidence and codebook evidence. `data/processed/roof_cross_extension_new_sources.json` records that no new originals were downloaded. Central files and frozen reviews were not modified.
