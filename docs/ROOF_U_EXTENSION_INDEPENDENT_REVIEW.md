# Independent review of the roofed-U artifact extension

2026-09-27. Reviewer: independent source-review subagent. Scope: `ROOF_U_ARTIFACT_EXTENSION.md`, its machine-readable ledger, source identities, target shapes, order and limits. The hypotheses were known before review; this was not a blind classification exercise. No audited or central file was edited.

**Result: no substantive correction required.** The two identity chains and the narrowly stated W729/W731-to-M334 correspondences are supported by the inspected evidence. One minor provenance improvement is noted below. No decipherment or universal crosswalk follows.

## Findings

1. **M354 identity passes.** M77's original AppendixV rule explicitly maps MIC1–560 to references1001–1560. The Marshall table row403 reads D262,2.25×0.6in,typeF, white in the steatite column, with a dash for depth. CISI1's exact M354 row gives D262,NMI15,HU912. The old403 image and the labelled M354 face/impression agree in broad text layout. This uses the publication rule and field number, not coincidental Finnish1403. ViewsA,a,B,C are one catalogued seal, not four objects.
2. **M810 identity passes.** The FEM range rule maps item364 to2364. Original Mackay printed380 was inspected in full as well as in crop: row364 aligns with1.02×1.02×0.26in,typeB, material ditto carried from steatite, locusBet.Bls.1(V)&10, level−11.7ft, fieldDK5890 (DK carried from the field-number column). CISI2's M810 row repeatsDK5890 and givesMD195,JL311,a:P231. The tiny following museum accession is not reliably resolved here either; retaining it as tentative and unused is appropriate. Level−11.7 is not converted to11ft7in or a chronology.
3. **Primary target drawings and order pass.** The1403 and2364 crops visibly place the roofed basal-U target next to the terminal jar-like sign. Literal metadata100001 and100101 agree with the ledger. The normalized sequences read in M77 order, while both secondary W strings store the jar-like sign first. The target remains the adjacent position, so the local comparison does not depend on falsely equating sequence order across namespaces. Exact neighboring signs were not independently recertified in this bounded review.
4. **Target shape comparison passes with existing limits.** M354's impression shows a peaked cap over a narrow U-like body, short basal projections and a long curved/oblique extension. M810's impression shows a peaked cap, narrow body, short oblique basal projections and a longer near-vertical central stem. Comparing impression with impression preserves that difference; it is not merely the expected horizontal reflection between a seal and its impression. The cap-to-body gap is not asserted invariant. The original AppendixI printed790/PDF799 explicitly labels its twoM334 drawings2364 and1403, and depicts vertical versus oblique long stems. This is especially direct support for catalogue classification, without proving functional allography or that the cap is a separately writtenM134.
5. **Damage statements pass.** M354's long text field has broadly continuous borders with irregularities and surface marks. M810 has a large lost lower corner in the animal field, mirrored to the opposite side in the impression. The upper two-sign field is outside that large break. Neither statement warrants microscopic intactness or a change to strict-corpus eligibility, and the audited review makes neither claim.
6. **Local cross-catalogue scope passes.** Direct CSV reads confirm row2850.1,M-354,D262403,`+740-729-407-845-236-002-906-125+`, and row3223.1,M-810,DK5890364,`+740-731+`. Both have stored directionR/L. The artifact identities and target positions support localW729→M334 andW731→M334. The retained feature catalogue'sP314 explicitly listsW731/M334; noW729 entry was found in that snapshot. This supports the stated coverage warning for aW731-only search, not globalW729=W731, a semantic equation, or an unrestricted code conversion. Source translations were not used.

## Minor provenance note

The artifact extension refers to the two AppendixI M334 variants, but its own45-file evidence list does not explicitly include their page/crop or `roof_nonfish_variant_review.json`. The primary M77 PDF itself is pinned, so this is not a missing source or a substantive evidentiary failure. For convenient standalone checking, cite printed790/PDF799 and include the existing variant crop or earlier review. This independent review supplies hashes for those additional, visually checked files below; no change was made to the audited ledger.

## Verification and limits

All45 `evidence_files` entries in the audited JSON matched their retained byte counts and SHA256 values at review time. All13 crop-manifest outputs matched the exact source-image pixels within the recorded boxes, and their source hashes matched. These integrity checks do not prove a visual interpretation. Independently viewed evidence comprises the13 linked crops, full Mackay printed380, and the full AppendixI printed790 page plus itsM334 crop. The CSV rows and feature entry were checked as data. Download URLs were not re-fetched, and no new downloads occurred.

The review authenticates two already present catalogue occurrences and their photographs. It does not establish linguistic values, function, manufacture independence, or all instances of eitherW code. The audited review and JSON remained unchanged.

## Reviewed-file hashes

The following pins record the exact reviewed artifacts and additional variant evidence. The audited JSON itself contains the complete45-file source registry verified above.

|File|Bytes|SHA256|
|---|---:|---|
|`docs/ROOF_U_ARTIFACT_EXTENSION.md`|5833|`d84ad4bfddf0084d4d7076384b6e278f76fb84d6ac288b47fd7cd69e5e76d9c0`|
|`data/processed/roof_u_artifact_extension.json`|12194|`9af11ff57ef825d5d7ac6706720c408cb9c3005fb399f7b7bde4a27e7d8e2ca9`|
|`data/processed/roof_u_extension_crop_manifest.json`|6575|`9dd45a9d8cca0b026c21bf2442818427e94f88cd8a288e11b0ca662900fc409a`|
|`scripts/render_roof_u_extension_crops.py`|1819|`33dc203e1de81c7aa938a2d1e5ac7799bbe947652e03ebf1b814aceedc12dcc7`|
|`data/raw/lipi_inscriptions.csv`|1204921|`b8dcb325a2e2cd3cde12ac12e7a418b0348e45713c9ee28aad81b645d2ac5ee4`|
|`data/processed/catalogue_features.json`|189902|`00836515c6f3beec28b3b66e13d8a9c6e94571cfb2e9dbb4b148651b7ff0032d`|
|`data/raw/roof_u_mackay_leaf402.jpg`|1751342|`56ba3d75f9d00fda1177a75ab2ce2475a5ce7d5bf6fdd02716966bc65672d540`|
|`results/primary_pages/roof-variants-agent-799.png`|3070917|`8680830631009b9dbec944ffe35b58b568a4f3589f51048e328de5265c508129`|
|`results/primary_pages/roof-nonfish-M334-variants.png`|132311|`b4b8cd5f2e62a3059e86d13b018fae9e84d558383d7ee7d6dff49a08172252e7`|
|`data/processed/roof_nonfish_variant_review.json`|11161|`4bbbf76187d53e0bc615558a537ceef1964722a3e39012216db32396b64112d0`|
|`results/primary_pages/roof-u-extension-appendix-fem-crop.png`|101194|`821388227776760c0dd9d11f9465226fd3c8f7ba2de96a2ddbfa4ecd122dc15d`|
|`results/primary_pages/roof-u-extension-appendix-mic-crop.png`|183660|`ad16f9f5b2a2b7999107d4add952ebf1c8ac28061afc07ec9f6f80eeccd6dca9`|
|`results/primary_pages/roof-u-extension-mic-403-crop.png`|34053|`df5c37ef2b420149b7d86d233285132846a85c3f2b5dfb08144c1e211d7a4513`|
|`results/primary_pages/roof-u-extension-mic-header-crop.png`|92275|`83413aad2d635a277a38b23d76ef02ef9b1780b5816047d951b43d58de31fdd1`|
|`results/primary_pages/roof-u-extension-mackay-364-crop.png`|319018|`d7b188ae609ff009632b6d4fa51ce8195bf3f20d5a23096ad4620118b8c887d0`|
|`results/primary_pages/roof-u-extension-mackay-header-crop.png`|1206853|`c3046fda84dc2cea3bb4b826554eb2da9dce68d8727819f8980b5dad480c3308`|
|`results/primary_pages/roof-u-extension-M354-metadata-crop.png`|34594|`b5763291520af8f52ced82df639720d5b0c9cbd01529fe4933e345dd137f359f`|
|`results/primary_pages/roof-u-extension-M810-metadata-crop.png`|30118|`d90de59b8c11c6e2d39246b074ece7ebef385276af8abf24f3055171b6116a3e`|
|`results/primary_pages/roof-u-extension-1403-crop.png`|113513|`16f9963212a8d0156ca3c8faca7ebf24f18c120c439a66dc6d613ee82672f4e8`|
|`results/primary_pages/roof-u-extension-2364-crop.png`|71604|`911aa5ad66ef42c19230156f900d5c9c3a822e8248ea297375710f1b8128e0a8`|
|`results/primary_pages/roof-u-extension-M354-views-crop.png`|895103|`535edea949b67942f96eca6f0433bc59447fed084f52d84efbe87e18a43b0fa3`|
|`results/primary_pages/roof-u-extension-M810-views-crop.png`|565776|`2d775334f1105de0ca99e73c7bf97ec056dc089824a019ef74c3885dc60d9069`|
|`results/primary_pages/roof-u-extension-marshall-403-crop.png`|125548|`24b135911856bb463f0dad47a510dc59774cbc68f899e15bb4d0640b75357d48`|
