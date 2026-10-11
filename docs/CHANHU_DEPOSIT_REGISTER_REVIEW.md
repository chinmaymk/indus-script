# Chanhudaro illustrated seal register: bounded provenance audit

Original printed pages292–293 contain the complete **65-entry PlateLI–LII frame**: LI1–33, LII1–3 on292; LII4–32 on293. The headings identify these as seal-amulets of the Harappa period. This is a finite frame of illustrated objects, not an authenticated census of all excavated seals, inscriptions, whole seal faces, or independent deposits. No sign sequences, values, fish labels or sign/context outcome counts were extracted.

The machine-readable transcription is [chanhu_deposit_seal_register.json](../data/processed/chanhu_deposit_seal_register.json); its `rows` contain exactly65 objects, with raw plate/item, excavation number including suffix, material, square or trench, explicit mound/cutting, locus and signed level. Every row identifies its printed page, archive leaf and original image. [build_chanhu_deposit_register.py](../scripts/build_chanhu_deposit_register.py) preserves the manual transcription and regenerates the JSON, checks the finite item ranges, and hashes its source files and text crops. Source hashes and crop coordinates are in the JSON. The reviewed sources are the retained `chanhu_context_leaf312.jpg` and313.jpg, checked against visible page headers and `c40_mackay1943_page_numbers.json`.

## Coverage and missingness

All65 rows supply excavation number, material abbreviation, locus and level. Sixty supply a square; the other five instead supply a trench: LI3/4 B(5), LI18 E(1), LI21 F(2), and LII9 J(1). Six explicitly say MoundI and three explicitly say `Cut.`. Missing mound or cutting fields are null, not an assignment to a different mound or excavation unit. Every level is reported in feet; a positive or negative sign is preserved. No ambiguous digit remains in the requested fields of the65 core rows after image review.

No core entry explicitly labels itself a fragment in these catalogue lines. That absence does not certify intactness. LI6,19,24 have question marks in their dimensions, while LI23 prints only two dimensions; these are recorded as limitations rather than converted into fragment diagnoses. The prior [workshop context review](CHANHU_WORKSHOP_CONTEXT_REVIEW.md) physically assessed LII12/CH2558 as a broken lower fragment. Its separate status is retained with attribution; no new seal photograph was interpreted in this task.

The preceding six rows at the top of292 belong to PlateL, not LI. They are preserved under `adjacent_excluded_rows`, outside the65-object core. The retained OCR on291 heads this earlier section as Jhukar seal-amulets and impressions; that heading was located in text, without obtaining a291 page image. Their metadata were visually read on292. PlateL15 has an unusual cross-shaped mark before10.3; its signed numeric elevation is left null rather than guessed. After LII32, page293 visibly starts PlateLIII, Figurines, ChapterX. OCR294 continues the figurine catalogue. Thus adjacent pages extend other illustrated-object sections, not the LI/LII item range. This bounded check cannot prove that no other seal appears elsewhere in the book or remained unpublished.

## Image-checked corrections and unresolved source issues

These are source readings, not edits to a secondary corpus:

- LI14 is **3215**, square9/B, locus283, +6.9ft. The OCR's3115 is wrong. The prior review records a square/context discrepancy; it remains unresolved.
- LI26 is **3043**, square8/E, locus430, +7.3ft. LI25 is3817. A parent-reported secondary duplicate3817 atLI26 cannot silently merge these original entries; the secondary file was not examined in this bounded audit.
- LII2/2848 is square8/E, locus425, **+8.0ft**; LII3/3359 is **Wh.steat., square7/F**, locus110, +7.1ft. These native-text readings replace provisional low-resolution readings.
- LI9/2000 prints **Gr.st.**. The abbreviation is preserved without silently replacing it with steatite.
- Exact suffixes survive:3485,b and3485,a;2594,h;2529,CC. Matching only the unsuffixed integers would discard source distinctions.
- LI29/2297 prints square9/D, locus174, +10.0ft. The earlier review reports a conflicting narrative association with beads at another level. This register retains the catalogue value and records the conflict.
- LII5/4852 prints Cutting9/F,469,−2.8ft; LII29/3811 prints Cutting9/F,468,+3.8ft. LII32/3492 separately has8/C,289,+8.6ft. These rows must not exchange metadata.

A subsequent metadata-only discrepancy report from the parent prompted four native-resolution crop checks. LII15 explicitly reads **2531**,8/D,178,+9.6ft; LI26 reads **3043**; LI12 explicitly reads **+7.0ft**; LI31 explicitly reads **+14.9ft**. All four original readings were confirmed, with no digit ambiguity. Dedicated `chanhu-register-confirm-` crops and coordinates are pinned in the register. The reported secondary alternatives2431,3817,+7.2,+14.1 were not substituted.

## Production and photographic coverage

The newly retained original page145 (archive leaf165) was visually checked for production and photographic-method statements. Mackay explicitly identifies LI1–10 as unfinished specimens and separately discusses incomplete finishing on LI12,18,21. These statements concern stages of manufacture, not a declaration that the text face is absent. Page145 says LII1–6 and11 were photographed directly because fragility made impressions unsafe; the remainder in LI/LII are photographs of plasticine impressions. This supplies an important source-method distinction for any later photographic review. It does not establish readable text on every entry, an exhaustive excavation denominator, or archaeological independence.

The first request for145 failed at DNS resolution in the restricted environment and returned no response bytes; its fetch metadata remain retained. The approved retry used a separate basename and succeeded. The original JPEG and serialized response headers are the only new raw artifacts, listed with URL, size and SHA256 in [chanhu_deposit_register_downloads.json](../data/processed/chanhu_deposit_register_downloads.json). No central registry, research log, frozen protocol or corpus was edited.

## Implications for a prospective craft comparison

The register supplies a sign-free illustrated-object frame and provenance fields, not an already valid deposit denominator. A square is too coarse to certify a workshop context; a locus number can also conceal different levels or episodes. Context conflicts, physical condition, direct photograph versus impression, and the availability of any readable inscription must be handled independently before assigning analytic eligibility. The presence of the same square/locus in multiple rows is not proof that those objects form independent finds or a closed deposit. These limitations preclude treating an unclassified or broken face as a negative sign observation.

## Attempt and validation record

1. Used retained OCR to locate the plate-section boundaries; did not use its corrupted digits as final data.
2. Inspected both full original catalogue pages and overlapping enlarged text crops covering every core entry.
3. Preserved the six adjacent PlateL rows separately, including the unresolved elevation mark.
4. Obtained and visually inspected original145 for bounded production/photo coverage, without reading sign values or counting signs.
5. Regenerated65 rows and checked plate/item completeness, unique row IDs, field presence, every retained source/crop hash, and the acquisition manifest. These checks verify transcription structure and reproducible pins, not correctness of ancient meanings or the excavation author's interpretations.
