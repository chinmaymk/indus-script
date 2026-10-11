# Primary contents review: Vats jars 5919 and 10252

Vats explicitly reports inscriptions on both jars and plant remains in their excavated contents. Table I supplies no dimensions for either jar. This is evidence of reported co-recovery, not an identification of the inscriptions' meaning, the vessels' original commodity, or a measured capacity. The two cases were selected from the narrative on printed p.253; they are not an exhaustive inventory or an unbiased comparison sample.

The source is M. S. Vats, *Excavations at Harappā*, volume I (1940), printed pp.165, 253, 256–257 and 266–267. Public Archive page JPEGs are retained under `data/raw/inscribed-contents-vats-leaf*.jpg`; p.253 was already retained as `capacity-context-vats-leaf279.jpg`. Table rows were read visually, including their column headings. Retained OCR was used only to navigate. The accompanying JSON pins every reviewed source and crop.

| Field | Jar 5919, Table I no.35 | Jar 10252, Table I no.116 |
|---|---|---|
| Table pages | 256–257 | 266–267 |
| Mound / trench | AB / Ex. P. I & II | F / IV |
| Square in table | P23/10 | I12/4 |
| Depth / stratum | 10 ft / IV | 9 ft / IV |
| Measurements | Dotted blank; unreported | Dotted blank; unreported |
| Description | Large, inscribed napiform | Round, in pieces |
| Inscription statement | Explicitly inscribed; no sign count in the reviewed passages | Explicitly two lines with seven pictograms |
| Plant material | Decayed cereal and leafy impressions in porous greenish earth | Decayed cereal, chaff, straw, melon seeds and leaf impressions in porous earth |

For 5919, the other reported contents include several bones, including charred pieces; a bull's head and wheel fragment; fragments of seven or eight cakes; assorted pottery sherds; bangle fragments; tiny charcoal pieces; a river shell inside a fragmentary oval vase; a chert scraper and slag. The table describes the lower four-fifths of the jar as containing the earth and plant material. The narrative on p.165 specifies four-fifths of its **height**, describes the vessel as crushed, and reports its depth as 10 ft. This is neither a mass of cereal nor a four-fifths capacity measurement. It also locates the two jars discussed there in **P23/5**, whereas Table I explicitly gives **P23/10** for 5919. Both location readings are retained unresolved.

For 10252, the table separately lists several bones, an oval long-necked vase and a small squat vase, a wheel, cake fragments, assorted sherds, two bangle pieces, charcoal, two small river-shell pieces, decayed cereal and slag. It then lists a discoid faience sealing, lentoid in section, with the reference **Plate C, 671**. The final remark describes the jar itself as inscribed in two lines with seven pictograms. **671 denotes the separately contained sealing; the table does not identify it as the jar's own inscription.** There is no jar-inscription illustration reference in this row. The companion catalogue-bridge investigation handles that separate object and does not supply missing jar glyphs here.

The source establishes that the excavator associated these contents with these numbered jars. It does not date the act of inscription relative to the plant deposition or sealing's deposition, demonstrate a primary storage assemblage, or show that the contents were the original commodity. The historical post-cremation interpretation in the chapter heading and narrative is recorded as the author's interpretation. Neither that interpretation nor a commodity reading follows automatically from the table. Dotted cells remain null, not zero; neighboring dimensions and ditto marks were not propagated into either selected row.

## New correction layer: row 18 plate reference

The prior frozen `capacity_context_independent_review.json` and its report transcribed the reference for jar 3822 as Plate XXIII,c. That letter was insufficiently checked and is corrected here to **XXIII,e**. On reinspection the small table letter is compatible with *e*; the plate provides the decisive contextual check: panel (e) is captioned as an inscribed jar and jar-stands of Stratum VI in square M12/6, matching row 18. Panel (c) instead shows hearths and mangers in M12/19. The prior files remain unchanged and are pinned as the explicit superseded claim. This correction does not change the earlier dimensions, table row identity or reported three-pictogram count. It does not establish a readable glyph transcription from the distant photograph.

## Research log and reproducibility

1. Read retained printed p.253 and OCR; located 5919 in row 35 and 10252 in row 116.
2. Retrieved leaves 282–283 (pp.256–257); visually checked every selected row 35 column.
3. Retrieved leaf 290 (p.264) for table navigation; it covers rows 100–115, so the target is on the following spread.
4. Retrieved leaf 191 (p.165) and leaves 292–293 (pp.266–267); visually checked narrative and row 116. The p.165 and p.267 fetches duplicated parallel acquisitions before coordination messages arrived. All response bytes and headers remain preserved and explicitly classified; duplicate captures are not independent evidence.
5. Rechecked row 18's tiny plate letter and Plate XXIII captions; recorded the correction in this new layer without changing frozen artifacts.
6. `scripts/persist_inscribed_jar_contents_review.py` writes native rectangular crops, structured transcriptions, SHA-256 pins and a pending typed source registry. No meaning, phonetic value, missing dimension or capacity is assigned. All 417 semantic and phonetic values remain null.
