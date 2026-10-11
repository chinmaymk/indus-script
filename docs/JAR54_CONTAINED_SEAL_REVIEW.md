# Table I row54: container XII and the unidentified contained seal

Independent bounded review,2026-09-27. The container identity and report of a contained seal are authenticated. The **contained seal's separate field number remains unresolved**. J630/EH446 is a contextual candidate, not a promoted identity.

## Container and contained object

Vats volumeI printed258–259, TableI serial54 (Archive leaves284–285), gives:

| Field | Exact reading |
|---|---|
| Register of container | XII (Roman numeral) |
| Mound | D |
| Trench | III |
| Square | S30/1 |
| Depth below surface | 3ft6in |
| Stratum | II |
| Description | Large, napiform, bottom portion |
| Measurements | No measurement given in row54 |

The right-hand continuation, column19, reports one tiny rectangular steatite seal inscribed on both sides. No separate seal field number, sign sequence, sign count or plate reference is supplied in that row. This is an object among the container's reported contents; **XII belongs to the containing jar and is not assigned to the seal**. No inscription on jarXII itself is reported here. The row's cereal/remarks cells are not used as observed absence, commodity evidence or sign meaning.

## Candidate J630: authenticated separate chain, missing containment join

Searching the retained Vats narrative by S30/1 led to printed189. The original scan confirms a tiny rectangular steatite seal J630 with six pictograms on one side and four on the other, PlateXCVI446, S30/1, depth3ft6in, under StratumII scattered finds. Printed188 supplies the section heading **TrenchII**. It does not say this object was inside jarXII.

The positive contextual similarities are square, depth, stratum, material, rectangular form and inscriptions on both sides. The material caveats are an actual trench discrepancy (tableIII versus narrativeII) and no explicit containment statement. These cannot be repaired by assuming a typographical error. This is insufficient to identify the row54 seal as J630.

The candidate's separate original catalogue chain is nevertheless clear:

- Vats narrative printed189: **J630 → PlateXCVI446**.
- Vats plates PDF200, PlateXCVI: number446 has two illustrated inscribed surfaces. This confirms the labelled publication image, not the jar association.
- Genuine CISI2 basic data printed444/PDF479: **H-890, FC3446, excavationJ630, museumHM297**; photograph-source column explicitly refers to EH plateXCVI446 and additional views. Its exact line is retained as a crop. FC3446 is not silently treated as a Mahadevan reference.
- M77 AppendixV printed821/PDF830 explicitly maps references4001–4713 to EH1–713 respectively, so **EH446 → M774446** follows the primary rule. This is a valid chain for candidate J630; it does not establish M774446 as the row54 seal.

This bounded task does not retranscribe J630's signs, assign semantic values, or copy a candidate text into the table's seal record. Both candidate photographed surfaces are retained together.

## Research log, failures and disposition

1. Requested left page258/leaf284 using the preserving fetch helper. Initial sandbox DNS failure produced no response body; its failure record is retained. A permitted retry retrieved the complete image into `data/raw/jar54-vats-leaf284-retry.jpg`.
2. Read the full headings and row54. Registered the Roman container number independently of any seal catalogue.
3. Searched retained Vats OCR for the square and two-sided seal descriptions. Generic shape descriptions were nonunique. The S30/1 hit located J630; retrieved original printed188–189 to check the heading and exact wording.
4. Inspected candidate plate446, CISI H890 basic-data row and the existing primary M77 EH numbering rule. Established the separate candidate chain while retaining the trench mismatch and missing containment statement.
5. Stopped the bounded join search with `contained_seal_field_number=null`. No matching integer, shape similarity or shared location was used as an explicit identity bridge. No central or frozen review was changed.

The three successful original-page downloads and one failed no-body attempt are recorded in `data/processed/jar54_new_sources.json`, including URLs, byte counts, hashes and content-review status. All downloaded bodies and HTTP headers are under `data/raw`. Re-run `scripts/render_jar54_crops.py` for six native-pixel crop-only views; exact boxes are in `jar54_crop_manifest.json`. The companion review JSON pins the complete source pages, publication PDFs, crop outputs and scripts.
