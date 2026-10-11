# Chanhudaro local primary comparators

28 September 2026. Source-exposed review of three physical objects: CH2285, CH3215 and CH3207. The question is visible graphic presence and preservation, not a reading. Multiple photographs/impressions of one object are not independent observations. No original data or frozen family definition is changed.

No securely identifiable fish-shaped member of the fixed P050, P051, P056–P064 family is established in the visible portions of these three objects. CH2285 has substantial loss of its inscribed face, so absence from its original whole text is **unknown**. The asymmetric/limb-like forms on CH3215 and CH3207 should not be promoted into that family from a small-image resemblance.

## Identity and primary sources

Mackay's printed p292 and Plate LI provide explicit field-number-to-photograph joins:

| Object | Plate | Catalogue provenance | Catalogue dimensions (inches) |
|---|---|---|---|
| CH3215 | LI.14 | White steatite; 9/B, locus 283, +6.9 ft | 0.75 × 0.78 × 0.43 |
| CH2285 | LI.15 | White steatite; 9/D, locus 215, +10.4 ft | 1.04 × 1.04 × 0.5 |
| CH3207 | LI.22 | White steatite; 9/B, locus 442, +7.7 ft | 0.83 × 0.82 × 0.39 |

CISI1 metadata p374/PDF410 independently identifies **C17 = CH3207**, Finnish reference 5022, ASI63.12.29, HU817, with impression `a: CE pl.LI.22`. Its original A and impression a are printed p331/PDF367. CISI1 p375/PDF411 identifies **C22 = CH2285**, Finnish reference 5015, ASI63.12.16, HU804, with `a: CE pl.LI.15`; original A and two impressions a/a bis are printed p332/PDF368. These explicit field and plate links authenticate the object joins without treating Finnish numbers as Mahadevan references.

The **C74** alias for CH3215 is supported here by secondary row76.1's exact `CH 3215Pl. LI:14` label and the primary Mackay join. An original CISI C74 photograph/basic-data entry was not independently located in this bounded pass. The CISI1 data section inspected ends its Chanhudaro sequence at C50; that limitation is not evidence C74 is absent from all CISI volumes.

## Graphic observations before code assignments

**CH3215 / LI.14.** The upper band shows an asymmetric complex form near the left, a pair of short uprights, and a lozenge-like outline near the right in the published impression. The complex form has a long stem/limb structure and a curved or angular attachment on one side; its sides do not securely enclose the symmetric body characteristic of the plain closed fish outline. The low-resolution resemblance was misleading. The rectangular printed image includes the apparent text band, but it is an impression with straight photographic boundaries, not a new original-surface examination proving every edge intact. No securely visible fixed-family fish is established; this is an observation about the displayed field, not a restoration of unavailable surfaces.

**CH3207 / C17.** Beside a large U-shaped element is a tall form with diverging lower strokes, lateral hanging strokes and upper extensions. The enlarged original and mirrored impression support a limb-like structure rather than a closed fish body. Several upper details meet the image/object boundary and the original's left outline is irregular; do not claim pristine physical completeness from the secondary `complete=Y` flag. The preserved recognizable forms do not establish a fixed-family fish. The figure within/below the animal field is not automatically another line of text.

**CH2285 / C22.** The original A photograph clearly loses a substantial upper-right corner, with rough fractured surface extending into the upper inscription. The corresponding loss appears on the upper left of the later mirrored impression a bis. Mackay LI.15 and the older impression a have a rectangular presentation that obscures the physical extent of the missing corner; they cannot prove an intact face. Surviving elements include a plain narrow oval/leaf outline, upright and forked marks and other damaged forms. No securely identifiable fixed-family fish is visible in the surviving field. The loop alone lacks diagnostic tail/other required structure. The curving form across the animal's underside is part of the illustrated motif area and is not promoted into a textual fish.

The secondary row109.1 calls preservation `complete` but separately marks `complete=N`. The original photo supports loss of **part of the inscribed face**; it does not show that an entire second face is missing or that another face's transcription was omitted. This review cannot establish exactly why the export author set the flag. The primary physical loss is sufficient to retain original-whole-text uncertainty.

## Local catalogue comparisons and control forms

After recording the morphology, the exact secondary strings were consulted without translation fields: C74 row76.1 `+125-002-861+`; C17 row105.1 `+740-100+`; C22 row109.1 `+440-390-032/368-390-790+`. These are source transcriptions, not a new full reading from photographs.

The feature crosswalk asserts W125 → P035/M028 and W100 → P009/M008. The primary M77 sign-list p32 shows M028's asymmetric side attachment and M008's divergent limb/upper structure. This comparison supports rejecting the initial fish resemblance. It does not independently authenticate a global W-to-M map or assign a meaning. Neither W125 nor W100 is W221, and no new broad-family sensitivity is justified by these images.

The parent subsequently requested two specific C22 control checks after obtaining its computational result; these checks are therefore post-selection and must remain so labelled:

- **W790 / source-asserted P355:** the simple oval/leaf outline is securely visible in original A and both impressions (upper left in original, upper right in impressions). Graphic presence is independently supported. P355 points to M261/M373/M374; the M77 p34–35 representatives include lozenge and oval forms. The exact M number is not resolved from this broad mapping.
- **W368 / source-asserted P202/M402:** at the opposite damaged upper corner, a long shaft and attached broadened, wing-like remnant survive. The break crosses the form; a complete triangular perimeter and internal divisions are not securely recoverable. The p35 M402 representative supplies a comparison, not a restoration. W368 remains present in the export, with **partial visual support**, not independently certain complete diagnostic morphology in these photos. Preserve the frozen statistical output and report this qualification separately.

## Research log and reproduction

1. Viewed full Mackay catalogue p292 and Plate LI, then made native-pixel crops of LI.14, LI.15 and LI.22. Preliminary small-image “fish-like” suggestions for LI.14/22 were recorded to the parent, then explicitly withdrawn after native enlargement and primary sign-list comparison. They are not findings.
2. Read only selected identity/preservation fields from the secondary CSV to derive C17 and locate the original CISI pages. Initial navigation pages PDF366/369 were retained but do not supply the target observations.
3. Rendered CISI1 original/impression pages 367/368 at 4000-pixel page height and metadata pages410/411. Original C22 exposes the missing corner hidden by the older rectangular impression presentation.
4. Compared M008/M028 representatives and the two later requested C22 controls. No exact global mapping, complete transcription or missing sign was invented.

`scripts/render_chanhu_local_comparators.py` reproduces the page renders and crop boxes. `data/processed/chanhu_local_comparators_crop_manifest.json` records native pixel coordinates; crops use no enhancement, rotation, mirroring or restoration. All source bytes were already retained; no downloads were needed. Evidence hashes are in `data/processed/chanhu_local_primary_comparators_review.json`.
