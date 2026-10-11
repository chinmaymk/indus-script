# CISI H-370, H-371 and H-372: independent identity review

Reviewed 2026-09-27. This review uses retained CISI volume 1 photographs and its column key. It does not use a desired capacity/count fit. No new downloads were needed.

## Exact catalogue identities

CISI printed p.372 / PDF408 gives the following complete rows. The columns are decoded from printed pp.365–366 / PDF401–402, not inferred from equal numbers in another corpus.

| CISI | Finnish Concordance (FC) | Excavation number | Museum | Photograph |
|---|---|---|---|---|
| H-370 | 4607 | 12908 | ASI | HU 1302 |
| H-371 | 4608 | 1033a | ASI | HU 1304 |
| H-372 | 4609 | ??? | ASI | HU 1307 |

The lowercase `a` in 1033a has no appended query. The key explicitly defines `???` as data not available. ASI in the museum column denotes the Archaeological Survey of India, Purana Qila, New Delhi; these rows give no museum registration numbers. HU identifies photographs taken by Ms Erja Lahdenperä for the CISI project through Helsinki University, Department of Asian and African Studies.

Column 2 is explicitly the Finnish Concordance, **not a Mahadevan reference**. The older `capacity_primary_review.json` calls these values `mahadevan_ref`; this review does not retain that promotion. A targeted independent check demonstrates the danger: M77 printed p.123 / PDF134 has reference 4607 as two fields, `210002` (a complex figure and two oval forms) and `20001` (U and three strokes); the list then proceeds to 4610 without separate 4608 or 4609 entries. Appendix V printed p.821 / PDF830 maps references 4001–4713 to EH items 1–713 respectively. That establishes M77 4607 → EH607, **not H-370 → M77 4607**. No M77 reference for these three jars is established here.

## Photographs and visible marks

Printed p.233 / PDF269 labels H-370 A(1) as the whole vessel and H-370 A(2) (100%) as the inscription detail. Printed p.234 / PDF270 does the same for H-371 and H-372. The same-side general/detail convention is explicit in the introduction, printed p.XXV / PDF29. There are three catalogue objects and two photographs of each, not six objects or two inscribed sides per jar. No mismatch between whole-vessel and detail labels is visible.

Counts below refer to **visible graphic traces**, not a settled numeral segmentation or numerical value. Images remain in their published orientation, with no mirroring or restoration.

- **H-370:** seven clear, long, approximately parallel upright traces. A shorter and fainter upright trace is visible between the third and fourth clear traces from the left. An eighth intentional stroke is possible, but the photograph does not securely distinguish that trace from incidental surface marking. Exact intentional stroke total remains uncertain; seven is the secure long-trace count, not a certified value of seven. No clear separate angular/U-like group is evident.
- **H-371:** seven clear long upright traces, including one interrupted trace, and an oblique trace at the right. The final upright and oblique approach the same lower area, but a continuous connecting bottom is not securely resolved. They could be the two arms of one angular/U-like sign. Thus six separate tallies plus a two-arm sign remains a plausible segmentation; seven upright primitives must not be reported as seven numerals. The earlier six-stroke/U reading is not refuted merely by counting all upright primitives. Neither a categorical U assignment nor categorical U absence is established by this photo alone.
- **H-372:** three clear long upright traces at the left. To their right is an angular form with an oblique arm and a more upright arm, and farther right a short separate trace. The three left uprights are securely distinguishable as a group, but the other marks are retained. The angular form cannot be declared absent just because its bottom is not rounded. Its exact sign identity and the short trace's function remain unsettled.

The pottery surface and photographic contrast interrupt some grooves. This review does not reconstruct missing strokes. A photographic shape count cannot resolve every incision, its intentionality, or sign boundaries.

## Vessel class, dimensions and the identity conflict

The photo section is headed GRAFFITI. The full views depict bellied pottery jars with comparatively short necks, rims and narrower rounded lower bodies. No formal vessel subtype, numerical height, diameter or capacity is explicitly provided in the three inspected metadata rows or captions. Those fields remain null. A typological name from a separate excavation passage needs its own exact field-number bridge.

The 100% captions belong to the inscription details. They are printed image-scale statements, not numerical vessel measurements, and are not a scale for the adjacent whole-vessel photographs. The introduction distinguishes image scaling from actual object measurements and warns that reproductions can be inaccurate. This review performs no raster-to-centimetre conversion and derives no capacity.

The conflict described in `CAPACITY_TABLE_FOLLOWUP.md` remains a source conflict: its reported Fuls assignment H-372=12908 disagrees with the directly observed CISI H-370=12908. CISI H-371=1033a is secure; CISI H-372 has no recorded excavation number. Neither H-370=1033b nor H-372=12908 is established by these CISI pages. The labels are not silently swapped and the missing H-372 field is not filled from a count/size expectation. Parent-led work on Vats 1033A/B context is outside this independent review's evidence scope.

## Research log and reproducibility

1. Read the basic-data column key and all three full metadata rows. Resolved `???` and FC numbering explicitly.
2. Inspected both photo pages, labels, full vessels and detail views. Rendered retained pages at 5200 pixels and saved crop-only views with exact pixel coordinates in `capacity_h370_crop_manifest.json`.
3. Counted primitive traces before assigning sign boundaries. The H-371 terminal grouping and H-370 short trace prevent a categorical numerical reading.
4. Read the older `capacity_primary_review.json` only after independent trace observations. Its H-371 six-stroke entry may describe a different segmentation; it is not overwritten. Its `mahadevan_ref` identity fields are unsupported by the CISI column key.
5. Tested the equal-number M77 locator. PDF133 was a one-page-early locator (printed122, ending at4599); PDF134 contains4607. Appendix PDF830 confirms the EH numbering rule. This attempt does not authenticate the jar-to-M77 join.
6. Inspected the introduction's same-side photo convention and scaling discussion. No dimensions were recovered. No further source search or downloads occurred.

Re-render with `scripts/inspect_research_pdf.py cisi_76884.pdf --prefix capacity-h370-source --pages 269 270 402 --render-only --scale 5200 --pdftoppm <pdftoppm>`; the metadata and first key page reuse pinned earlier renders. Run `scripts/render_capacity_h370_crops.py` for the ten exact crops. M77 renders use prefix `capacity-h370-m77` for pages133 and830, and `capacity-h370-m77-followup` for134, scale3200. All evidence byte counts and SHA-256 hashes are listed in the companion JSON. No central data, earlier reviews or hypotheses were modified.
