# Roofed basal-U coverage: two original artifacts

2026-09-27. This review authenticates two existing M77 M334 occurrences against original artifact photographs: **1403 = MIC403 = D262 = CISI M354**, and **2364 = FEM364 = DK5890 = CISI M810**. It adds documentary and photographic support, not two new corpus occurrences. No meaning or sound is assigned.

## Identity chains

M77 Appendix V printed818/PDF827 explicitly maps references1001–1560 to MIC items1–560, and references2002–2704 to FEM items2–704. These printed correspondence rules justify MIC403→1403 and FEM364→2364; matching terminal digits alone would not.

Marshall volumeII printed404/PDF55 gives MIC403 as D262, typeF, white steatite, 2.25×0.6 inches, depth unreported. Marshall volumeIII plateCXII, item403, supplies the historical image. CISI1 printed368/PDF404 gives M354, D262, NMI15 and photographHU912. Its separate Finnish number1403 is not used as the joining rule. CISI1 printed88/PDF124 shows M354A (face), a (impression), B (back) and C (profile). These are views of one catalogued object.

Mackay printed380, row364, gives DK5890, typeB, steatite (ditto from the table's material column), 1.02×1.02×0.26 inches, locus 'Bet. Bls. 1 (V) & 10', level−11.7 feet. This is a recorded excavation level, not a modern chronological date. CISI2 printed436/PDF471 gives M810, DK5890, MD195, JL311 and impressionP231. The following small museum accession appears as50.14 but is not used as a secure join or silently normalized. CISI2 printed70/PDF105 shows M810A and a. They are the original and impression of one object, not two attestations.

## Primary normalized fields and photographs

|M77 reference|Literal metadata|Normalized token sequence|Photographic observation|
|---|---|---|---|
|1403, printed51/PDF62|100001|M028 M303 M100 M066 M407 M169 M334 M342|M354 has eight apparent sign groups; next to the jar-like terminal, a roofed narrow U-like body has short basal projections and a long oblique extension.|
|2364, printed69/PDF80|100101|M334 M342|M810 has two clear upper sign groups; the roofed body has short oblique basal projections and a longer central downward stem.|

The sequence order here follows M77, not a new reversal of the physical seal. The historical403 image and CISI M354 impression agree broadly. The modern M354 face/impression pair and M810 face/impression pair visibly confirm the roof/body/basal arrangement at the target positions. Differences in the direction and curvature of the long basal extension are real in the published photographs, compatible with the two M334 variants already printed in M77 AppendixI. This is not an independent certification of every stroke in every neighbouring sign, an allograph proof, or evidence that the cap is a separately written M134.

M354 has a broadly preserved rectangular text field with uneven edges and surface marks. M810 has a substantial chipped/missing lower corner in the animal field. The upper two-sign inscription is not cut by that large break. Artifact condition and inscription condition must remain separate; neither is called microscopically intact. No damage label or strict-corpus flag was changed.

## Local cross-catalogue consequence

The retained secondary row2850.1 identifies M-354 with concatenated locatorD262403 and text `+740-729-407-845-236-002-906-125+`. Row3223.1 identifies M-810 with locatorDK5890364 and text `+740-731+`. Both strings have the jar-like token first in their stored order. At the corresponding adjacent positions, **W729 on M354 and W731 on M810 locally correspond to the two M334 forms**. The identity chains above, not an assumed global code conversion, support that comparison.

The retained feature entryP314 lists W731/M334. No feature entry for W729 was found in this snapshot. Therefore a search restricted to W731 can miss an M334 object. Conversely, this two-object finding does not establish W729=W731 everywhere, semantic interchangeability, or that every W731 occurrence is M334. The old and new catalogues partition shape variation differently at these two positions. The surrounding texts and artifact types differ; the pair is not a controlled substitution proving a shared function.

## Attempts, limits and reproduction

Started with all four nativeM334 references and the secondary W731 row. Located M354's W729 row through its exact object identity, preserving raw strings and metadata. Reviewed primary M77 fields and its explicit publication correspondence rules; retrieved two old publication pages into `data/raw/` with URL, byte count and hash. These are the only new downloads for this subtask.

Initial Marshall PDF57–59 locator guesses led to printed406–408, not the required table. The actual row is printed404/PDF55; all renders are retained with distinct prefixes. Initial archive page-number metadata did not supply printed labels, so final page assignments were visually verified. OCR did not reliably locate DK5890; the table image supplied it. System Python lacked pypdf, so the bundled runtime was used. An early shell glob for a guessed document name matched nothing; subsequent discovery used rg. A pre-existing CISI1 text extraction with an inconsistent page count was not used as identity evidence; the source PDF and photographed page labels were checked directly.

The [machine-readable review](../data/processed/roof_u_artifact_extension.json) pins primary sources, raw/derived records, extraction manifests and excerpts. [Crop code](../scripts/render_roof_u_extension_crops.py) and its [manifest](../data/processed/roof_u_extension_crop_manifest.json) reproduce thirteen unretouched crops. Hash and pixel checks establish file integrity; the visual assessments above remain explicit human-review judgments. Earlier roof protocols, counts and evidence reviews remain frozen.
