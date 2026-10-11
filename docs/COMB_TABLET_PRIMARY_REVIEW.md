# Comb-tablet primary review: H-1817 and H-843

Date: 2026-09-27. This bounded, source-exposed review **does not authenticate either requested modern catalogue alias to an original illustrated object**. A promising older locator, Mahadevan 5326, has a verifiable printed transcription and photograph of a crosshatched face, but its excavation number is blank. Consequently the graphic equivalence or difference between the two requested tablets remains untested. All semantic and phonetic values are null.

## Requested objects and evidence boundary

The secondary Lipi export gives H-1817 as rows624.1/624.2, raw identifier `H94-2326Figure 26.06`, Trench10W/11, faience, rectangular,13.5×8×3.3mm. It codes one face `+700-034+` and the other `+400-525-554+`. H-843 is row1729.1, raw identifier `14307`, prism with triangular section,29×11mm, text `+400-527-195+`, and field-symbol label `Xhch`. These are retained source claims, not newly verified metadata. The export's meanings, transliterations and cross-reference interpretation are excluded by the audit script.

In particular, common site/type/length filters do not establish that these objects share a precise tablet form: the secondary shape/section and dimensions already differ. This review does not decide whether that difference is ancient, classificatory, or erroneous. Neither side has an authenticated inscription photograph here; no stroke count, comb orientation, edge damage, or final-sign morphology is asserted for H-1817 or H-843 themselves.

## H-843: candidate 5326 is promising but not joined

Exact `14307` and spaced/punctuated `14[\s,.]*307` searches in retained Vats OCR and Mahadevan extracted text return no matches. OCR absence does not prove absence from the original volumes. The Vats class30 discussion around printed pp333–334 lists triangular prism sealings under other numbers; it supplies no safe14307 identification. No nearby number was substituted.

After the parent's masked computational discovery supplied locator5326, the following original Mahadevan pages were visually inspected:

| Source | Personally verified observation |
|---|---|
| AppendixV, printed823/PDF832 | Ref5326 has a **blank excavation-number field**, and source `Pu.63:4394–95`; refs5327–5329 cite the same photographic pair. |
| Texts, printed138/PDF149 | Ref5326 has three glyphs displayed left to right **M176, M254, M054**, followed by another metadata line `29790`. The second line has no additional script glyphs printed against it. |
| Numbered sign list, printed32/PDF43 | M054 is the looped multi-stroke form with rightward curving branches, matching the last displayed glyph under5326. It differs visibly from the straight triangular-cross M216 in the numbered sign list. |
| AppendixIII key, printed812/PDF821 | Figure139 is explicitly linked to ref5326, field-symbol code97, photographic source `Pu.63:4395`. |
| AppendixIII PlateVII, printed813/PDF822 | Figure139 photographs a narrow face bearing crossing diagonal strokes, forming a crosshatched pattern. It does **not** show the three-sign inscription face. |

The M176 and M254 identifications use the already inspected primary numbered list at printed33–34/PDF44–45; those pages are pinned again as evidence. The candidate's normalized right-to-left script sequence is M054–M254–M176. No new reading of the missing inscription photograph is claimed.

The combination of three-sign context and crosshatched face makes5326 a useful locator for H-843, whose secondary symbol field is `Xhch`. But shape/context agreement does not provide the missing **14307 ↔5326** or **H-843 ↔5326** identity bridge. No new W195→M054 rule is established by this review. The parent's independently selected M-735 case is outside this review's scope.

The alternate computational locator2868 was previously authenticated as DK8489/FEM CII15, a round elephant-impressed object with an incised winged reverse (`W525_PRIMARY_REVIEW.md`). That existing identity cannot be transferred to the secondary prism14307 merely because a candidate text matches.

## H-1817: exact report/figure remains unavailable

Public searches for H94-2326, H-1817, Figure26.06 and the1994 Harappa report did not locate an authenticated target illustration. The [1997 excavation paper](https://www.harappa.com/sites/default/files/pdf/Kenoyer1997_Excavations%20at%20Harappa%201994-1995%20New%20Perspective.pdf) has a different figure scheme. Its extracted figure11 metadata lists moulded tablets with other registration numbers; no2326 text match was returned. It is not the cited Figure26.06.

The [original authors'2010 CISI introductory essay](https://www.harappa.com/sites/default/files/pdf/Kenoyer-Meadow-2010-HARP.pdf) is a17-page extract, not the complete CISI3 photographic and basic-data catalogue. It cites a distinct Harappa1994 report submitted on30August1994. Searches within that extract returned no2326 or1817 matches. This supports a publication locator but does not authenticate the tablet's field number, context or signs.

Direct retrieval of the1997 PDF with Python and then curl both returned HTTP403. The public web reader supplied text, retained as explicit **web-extraction captures**, not mislabelled original PDF bytes. Its screenshot calls supplied references but no inspectable image payload in this tool route, so no visual assessment of these web-only figures is claimed. No downloaded original PDF or target photograph was obtained in this phase.

## Research log and exclusions

1. Selected the three specified secondary rows; omitted translation/transliteration fields. Reproducible output: `comb_tablet_source_audit.json`.
2. Searched Vats and Mahadevan local text for14307 and spacing/punctuation variants: no hits. Reviewed Vats prism discussion as a locator; no identity established.
3. Searched public sources by exact modern aliases, field number and figure, and by1994 report title. Results mainly led to the1997 paper,2010 extract and bibliography, not the requested figure. These are limited searches, not proof that no copy exists.
4. Inspected public1997/2010 extracted metadata; retained two raw JSON captures under `data/raw/`. Original PDF download failed twice with HTTP403. No access restriction was bypassed.
5. Reopened the prior Internet Archive `corpus-vol-2` metadata: it actually describes volume1, so it is not a Pakistan-volume source. Search listings for the actual volume2 did not yield a usable original target page in this phase.
6. Followed the parent-supplied5326 locator only after computational discovery; rendered and visually inspected its text, numbered sign, appendix reference, field-symbol key and crosshatched-face photograph. The blank excavation field prevents promotion to H-843.
7. Retained both targets as **unresolved for artifact-level graphic comparison**. Do not count this pair as a primary-confirmed comb allograph, final-sign substitution, same-mould pair, or chronological contrast.

Remaining concrete sources are the full CISI2 H-843 photo/basic-data entry or ASI Punjab photographic album63 photos4394–95 with an inventory bridge, and the full1994 HARP report Figure26.06 or CISI3 H-1817 photo/basic-data entry. No request was sent to any person or institution.

## Reproduction and retained artifacts

`scripts/audit_comb_tablet_sources.py` reproduces row selection and local text searches. `scripts/render_comb_tablet_crops.py` gives fractional crop coordinates and preserves unretouched candidate images. `scripts/download_comb_tablet_sources.py` retains any successful public download under `data/raw/` and records provenance; the attempted source returned403. `data/processed/comb_tablet_new_sources.json` lists retained web captures distinctly from downloads, with URL/bytes/SHA256. The central registry was not edited.

PDF renders used `scripts/inspect_research_pdf.py` with source `mahadevan_1977_text.pdf`, pages149/822 at scale3200 (prefix `comb-tablet-m77`), and pages43/821 at scale3600 (prefix `comb-tablet-m77-detail`). Its manifests pin the original PDF. The machine-readable review pins the source files, observations, scripts and crops.
