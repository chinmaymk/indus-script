# Roof candidates before M176: primary field review

Date: 2026-09-27. **All four proposed first-field strings are confirmed in Mahadevan's printed normalized texts.** Their additional entries differ and must remain separate: the two roof-X references have a two-long-strokes-plus-U side, the roof-fish reference has a four-long-strokes-plus-U side, and the unroofed flanked-fish reference has a symbol-only side. These observations do not supply a complete roof-transfer comparison or a semantic reading.

## Exact printed entries

The following sequences are transcribed in the publication's normalized right-to-left order. The physical displayed order on the page is the reverse. The final metadata digit records the original direction separately; notably,5477 has direction2 despite its normalized display. Object-type3 is inherited across each reference's later entries and denotes the catalogue's miniature-tablet category, not a specific material.

| Reference; printed/PDF page | Side; line | Literal metadata | Field-symbol code | Original direction code | Normalized text |
|---|---|---|---|---|---|
| 4407;111/122 | 1;0 | `319101` | 91 | 1 | M138 M176 |
| 4407;111/122 | 2;0 | `29101` | 91 | 1 | M087 M328 |
| 4493;116/127 | 1;0 | `310001` | 00 | 1 | M066 M176 |
| 4493;116/127 | 2;0 | `20001` | 00 | 1 | M095 M328 |
| 5444;142/153 | 1;0 | `319101` | 91 | 1 | M138 M176 |
| 5444;142/153 | 2;0 | `29101` | 91 | 1 | M087 M328 |
| 5477;144/155 | 1;0 | `310002` | 00 | 2 | M060 M176 |
| 5477;144/155 | 2;9 | `28390` | 83 | 0 | No text: symbol-only side |

M087 is the pair of **long** strokes, not the short pairM099. M095 is the group of four long strokes. These identities were checked against the numbered representative sign list along with M060,M066,M138,M176 andM328. No doubt asterisk or loss block is printed on these seven text-bearing lines. The symbol-only entry has no script tokens; its field-symbol83 is not converted to a signM083 or treated as missing text.

There are eight printed entries across the four selected references: seven script lines and one symbol-only entry. This is an accounting of the selected records, not a claim of four independently authenticated physical objects or four independent statistical trials. The two roof-X records share both recorded texts and field-symbol codes; this review does not decide whether their underlying artifacts are distinct, duplicates or related products.

The codebook at printed19–20/PDF30–31 explains omitted repeated metadata and normalized direction. Printed30–31/PDF41–42 defines type3, sides, field symbols, line0/9 and direction0/1/2. A second entry's five-digit string is not a new object type. Side/line values identify the field; entries are never concatenated into one long string.

## Source metadata and identity limits

AppendixV printed821/PDF830 explicitly maps references4001–4713 to EH volumeII items1–713 respectively. It therefore authenticates **4407→EH407** and **4493→EH493** without guessing a split identifier. This condensed appendix does not supply their excavation numbers; those remain null here. The corresponding EH photographs and excavation tables were not newly inspected in this bounded M77-field review.

AppendixV printed824/PDF833 directly gives **5444→excavation3027(2), photographic sourcePu.35:3863**, and **5477→excavation13592, photographic sourcePu.61:4076**. Parentheses in3027(2) are preserved without interpreting them as a side number or separate count. These catalogue joins are not new photographic verification. No modern CISI alias, find depth, date, mould relationship or semantic label is imported.

## What this does and does not add

The first-field candidates need no code correction: the plain flanked fish is M060, the roofed flanked fish M066, and both roof-X occurrences M138, each followed by M176 in normalized order. Their printed neighbouring fields now have explicit records rather than being folded into those short strings.

The matched first-field setting is a shared final sign only. The roof-X references do not provide the corresponding plain-X/M137 field, and their other-side texts differ from the fish references. This review does not treat different bases under one roof as equivalent or infer that the roof contributes a common meaning. Whether a preregistered context test admits any comparison is a separate computational question; the primary review neither creates missing combinations nor joins sides to make one.

## Research log and reproduction

1. Used local extracted text only to locate the four references and appendix rows. OCR was not accepted as a transcription; it mangles several sign shapes.
2. Rendered and inspected complete primary pages122/127/153/155 and appendices830/833. Crops retain each complete two-entry reference block, including5477's symbol-only side.
3. Compared numbered primary glyphs and reread the original metadata/normalization codebook. Recovered all additional printed fields and preserved the different direction on5477.
4. Verified the explicit EH numbering rule and the two direct excavation/photo-source rows. Did not infer additional field numbers, artifact duplicates or aliases.
5. Recorded the eight entries individually in `data/processed/roof_m176_primary_review.json`, including seven script lines and one symbol-only side. No sign correction, download, central corpus edit or alteration of the earlier shape selection was made.

The retained source is `data/raw/mahadevan_1977_text.pdf`. `scripts/inspect_research_pdf.py` rendered pages122/127/153/155/830/833 with prefix `roof-m176`,scale3600. `scripts/render_roof_m176_crops.py` reproduces exact fractional crops recorded in `data/processed/roof_m176_crop_manifest.json`. The companion review pins the full pages, numbered-sign evidence, codebook, crops and scripts by SHA256. These are verified published catalogue fields, not fresh readings of the original artifacts.
