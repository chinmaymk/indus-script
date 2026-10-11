# Exact artifact bridge for M77 4508, 4509 and 4548

Three selected inscriptions can now be joined to **three photographed artifacts and three primary excavation-catalogue entries**. All are described as steatite. They differ in shape and find context; there is no evidence here for a shared mold. No primary CISI or museum-accession join was authenticated.

| M77 reference | Vats II plate/item | Excavation no. | Other-face strokes + U | Vats I catalogue | Shape | Stated size, inches | Find square; depth below surface |
|---|---|---|---|---|---|---|---|
| 4508 | XCVII / 508 | 2568 | 4 + U | p121, item4 | rectangular | 7/16 × 1/4 | N9/10; 19ft6in |
| 4509 | XCVII / 509 | 1280 | 3 + U | p95, item29 | rectangular | 3/8 × 1/4 | M11/18; 13ft |
| 4548 | XCVII / 548 | 2642 | 2 + U | p110, item15 | oval | 5/16 × 1/4 | M11/16; 16ft |

The main text in the earlier authenticated M77 transcription is M048–M342–M176 for all three. The other-face M sequences are M095–M328, M089–M328 and M087–M328 respectively. These are Mahadevan identifiers, not inferred W/P equivalences.

## How the join is authenticated

M77 Appendix V, printed821/PDF830, explicitly assigns references4001–4713 to EH volumeII items1–713 respectively, across platesLXXXV–CI. This documented range yields the three exact item references; numeric equality across catalogues was not assumed. [Durable primary render](../results/primary_pages/m77-u-bridge-830.png).

Vats II PlateXCVII, PDF202 of the downloaded plate scan, visibly labels508,509,548 and shows two faces beneath each label. [Full plate](../results/primary_pages/m77-u-bridge-vats-202.png). The two rectangular artifacts differ from the oval548. Enlarged unretouched crops show four, three and two strokes adjacent to the U consistently with M77: [508](../results/primary_pages/m77-u-bridge-EH508-detail.png), [509](../results/primary_pages/m77-u-bridge-EH509-detail.png), [548](../results/primary_pages/m77-u-bridge-EH548-detail.png). The underlying plate image is only957×1256pixels. The crops enlarge existing pixels, and are insufficient for reliable toolmark, mold, exact surface-condition or every-glyph reauthentication. The reproduced faces show U to the left of strokes; that is image layout, not an independently established historical reading direction.

The three Vats I entries explicitly name their exact plate item, excavation number, material, size, square and depth. Those primary pages were visually checked, not accepted from OCR: [p95](../data/raw/vats_1940_text_leaf121.jpg), [p110](../data/raw/vats_1940_text_leaf136.jpg), [p121](../data/raw/vats_1940_text_leaf147.jpg). The immediate paragraph on p121 assigns its four listed finds, including508, to StratumVII. The other two target pages do not establish a stratum label directly, so none is added as primary-verified. Different depths in different squares cannot by themselves date or order manufacture.

The catalogue calls each a tiny seal, with three pictograms on one face and one on the other. This is Vats's historical grouping, not a modern count of atomic glyphs: it must not replace M77's segmentation. None of these exact entries explicitly describes breakage; the photos appear broadly intact in outline, but scan quality precludes a complete condition assessment. Incision versus molding, workshop, thickness, mass, contents, and current accession remain unverified.

## A descriptive size correspondence, not a decipherment

In this already-selected trio, nominal length is5/16,6/16,7/16inch for two, three and four strokes. These are published tablet dimensions, not vessel capacity or independently known quantities. The sample was selected for its text/count contrast, has only three members, includes a shape change, and has no thickness measurements. Additional strokes requiring additional writing space, manufacture or object class, find context and chance remain possible. No correlation test or semantic inference is justified from these three lengths. The shared stated width is1/4inch; converting to millimetres does not increase the original measurement precision.

The subsequent [frozen length test](M77_U_LENGTH_HOLDOUT.md) recovered five
additional measurements and rejected the exact size formula suggested by this
trio. Three-stroke EH405 is substantially longer than predicted in both Vats's
narrative and table. The follow-up also preserves differing fractional and decimal
measurements for these training objects. The descriptive fit here must not be
generalized to the auxiliary field or treated as a quantity calibration.

## Limits of the CISI bridge

A secondary lead in `data/raw/lipi_inscriptions.csv` associates the exact excavation+Vats-item strings2568508,1280509,2642548 with H-1273,H-935,H-962 respectively; matching shapes and find contexts strengthen the lead. This is explicitly unverified against primary CISI. Those high-numbered Harappa items are beyond the available first volume's illustrated range, so no CISI1 photo or museum number is substituted. Secondary dimensions differ in rounding and, for548, width; they are not silently merged with Vats's measurements. The ledger records all three candidates separately from verified joins.

## Sources and reproducibility

The public ASI/IGNCA scan hosted at [Internet Archive9842](https://archive.org/details/in.gov.ignca.9842) supplies the plates, despite its misleading volumeI metadata and the Harappa portal linking both volumes to it. The [18220 scan](https://archive.org/details/in.gov.ignca.18220) supplies genuine volumeI text. To avoid another whole-volume download, only its small OCR/index and three individual primary page images were saved. All nine new downloaded files remain in `data/raw/`; their exact URLs, SHA256 hashes and byte counts are in `sources.downloads` of [the evidence ledger](../data/processed/m77_u_artifact_bridge.json). No source registry edit was made by this subagent.

The ledger preserves3 artifacts,6 pictured faces,3 visually verified catalogue entries and0 primary CISI joins. `scripts/build_m77_u_artifact_bridge.py` rebuilds the ledger from manually reviewed observations and hashes existing evidence; it does not perform OCR inference or download anything. The earlier sign-level evidence is [M77_U_COUNTEREXAMPLES.md](M77_U_COUNTEREXAMPLES.md). No canonical corpus, strict set, sign value or translation is changed.
