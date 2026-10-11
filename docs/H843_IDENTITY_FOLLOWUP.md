# H-843 identity follow-up

Date: 2026-09-27. **The previously missing CISI2 source has been recovered, and H-843 is now directly authenticated to excavation number14307 and photographs of the inscribed prism.** The exact identity between this object and Mahadevan1977 reference5326 remains unproved. No semantic or phonetic value is assigned.

## Recovered source and identity

The distinct Internet Archive item [`corpus-vol-2_202409`](https://archive.org/details/corpus-vol-2_202409) supplies an accessible [original PDF scan](https://archive.org/download/corpus-vol-2_202409/CorpusVol2.pdf), retained intact at `data/raw/h843_identity_CorpusVol2.pdf`. This is not the previously rejected item `corpus-vol-2`. Its actual title page, PDF4, identifies **Corpus of Indus Seals and Inscriptions, 2. Collections in Pakistan**, edited by Sayid Ghulam Mustafa Shah and Asko Parpola, Helsinki1991. The scan has486 PDF pages. The cover bears an ASI Central Archaeological Library accession; the hosting item is a public contributed copy, not an institutional repository endorsement.

The basic-data key at printed434/PDF469 explains the five columns. The second is the Finnish concordance, explicitly not interchangeable with Mahadevan numbering; the third is the excavation identifier; the fourth museum information; and the fifth photographic source. At printed444/PDF479, the H-843 row gives:

| Field | Primary entry |
|---|---|
| CISI identifier | H-843 |
| Finnish concordance | 4162 |
| Excavation number | 14307 |
| Museum | HM269: Harappa Museum |
| Photography | AV405; B+C: P859 |

The key identifies AV as Arto Vuohelainen and P as S.M. Ilyas photography for the corpus. The first photographic reference covers unspecified views. This is an explicit **H-843↔14307** bridge independent of matching script strings. It confirms the selected secondary identifier, without importing the secondary dimensions, preservation classification, detailed find context, or meanings.

## Personally inspected photographs

Printed331/PDF366 labels views H-843 A, B, C, F, and B+C. A shows a narrow, rounded rectangular inscribed surface. B and C show distinct diagonal crosshatching. F shows a triangular end; the combination verifies a prism with multiple long faces. These are labelled uppercase object views, not lowercase impression views.

The inscription photograph supports three visible sign groups. The central comb has a vertical stem on the left and short strokes extending right in the published orientation. Its surface is uneven and dark, so the photograph does not justify an exact tooth count. The rightmost group has a curved or looped body and projecting branches, consistent in broad graphic structure with the numbered Mahadevan sign M054, and unlike a simple straight triangular cross. The full topology of faint strokes is less clear than the printed sign-list drawing; this assessment is explicitly a visual comparison, not a catalogue assertion that H-843 is text5326. No horizontal flip, contrast reconstruction, or AI restoration was applied.

The A face retains both ends and does not appear to have a large missing fragment through the central or rightmost group. Fine surface loss, glare and shadow are visible. This is not evidence that every stroke is intact, nor a quantitative preservation grade. The white bright area near the right end is not interpreted as a sign. Primary shape evidence now supports discussing H-843 directly, but cannot establish equivalence with the still-unavailable H-1817 photograph.

## Mahadevan5326 remains a separate candidate

The earlier review established M77ref5326's printed three-sign sequence and source `Pu.63:4394–95`, with the excavation-number field blank. Its field-symbol photograph is figure139 at printed813/PDF822, linked by the key at printed812/PDF821 to Pu.63:4395. That crop was compared again with CISI2 H-843 B and C.

Both sources show crosshatched narrow faces, but the old figure139 is too small and indistinct to demonstrate a unique damaged edge, individual diagonal intersection, or distinctive pattern boundary that would securely identify the same physical face. Lighting and scale differ substantially. Generic crosshatching and a compatible three-sign text do not resolve identity. CISI2's H-843 row cites AV405/P859, not Pu.63 or Mahadevan5326. The Finnish number4162 must not be transformed into a Mahadevan reference by numerical analogy. Thus **H-843↔14307 is authenticated; H-843↔M775326 and14307↔Pu.63:4394–95 remain unresolved**.

## Bounded research log

1. Read the existing `COMB_TABLET_PRIMARY_REVIEW.md` and its unresolved source requirements. Did not repeat the rejected `corpus-vol-2` download.
2. Searched Helsinki author/institution repositories (helda.helsinki.fi and tuhat.helsinki.fi), IGNCA holdings, and ASI photography catalogues. Returned citations and the already-known IGNCA volume1, not a new full volume2. Exact queries and returned text are retained in `h843_identity_institution_search.json`.
3. Examined the [Harappa original-excavation photographic project](https://www.harappa.com/content/introduction-discovery-harappa) and its first-excavations link. Searches for14307 and4395 did not return a target inventory join. The project is a plausible photo route, not evidence that a target is absent.
4. Queried British Library Harappa photographic records. [Photo685(142)](https://searcharchives.bl.uk/catalog/040-003100967) identifies small seals/sealings; other returned records list different field numbers. No14307/Pu.63 bridge or accessible target image was obtained. These are catalogue locators, not an inspected substitute photograph.
5. Tested [Lahore Fort catalogue](https://lahorefortarchives.com/catalogues/) and [National Library of Finland bibliographic record](https://data.nationallibrary.fi/bib/me/W00003846100): web fetch respectively exceeded its content-size limit and returned cache-miss. No original bytes were downloaded from either. Captures preserve the failures rather than treating them as absence.
6. Internet Archive's [title query API](https://archive.org/advancedsearch.php?q=title%3A%28Corpus+Indus+Seals%29&output=json&rows=50) returned three items, including the distinct `corpus-vol-2_202409`. Downloaded its metadata,35,870,617-byte PDF,OCR companion and page mapping; authenticated the title visually before using it. The parent's other source-recovery agent independently noticed the same item; coordination avoided duplicate PDF downloads.
7. The PDF's native extraction contains no useful text. Companion OCR finds the H843 photo locator but fails on14307 and5326; it is therefore only a locator. Printed331 maps to leaf365/PDF366, and printed444 to leaf478/PDF479. An initial off-by-one exploratory render of367/480 was not used as target evidence; corrected pages were then inspected directly.
8. Inspected title, metadata key, H-843 row, A/B/C/F photographs, existing M054 numbered sign and M775326 reverse. Persisted unretouched crops, exact coordinates, source hashes and limited conclusions. Stopped the source search after the requested primary photographic and field identity evidence was recovered.

## Reproduction and boundaries

`scripts/download_h843_followup_sources.py` downloads publicly accessible bytes to the shared raw folder and records URL,redirect,size,SHA256. `scripts/render_h843_identity_crops.py` reproduces fractional-coordinate crops. Renders use `scripts/inspect_research_pdf.py` with the retained PDF: prefix `h843-cisi2-target`, pages366/479,scale4200; prefix `h843-cisi2-key`, pages469/470/28,scale3000; title page4 appears in prefix `h843-cisi2-main`,scale3600. Render manifests are retained. The companion machine-readable review pins all evidence used.

`data/processed/h843_identity_new_sources.json` distinguishes five original downloaded files from three web-extraction captures. The latter are tool-response records and cannot be reproduced as original page bytes. This follow-up did not alter the central source registry or overwrite the earlier review's historical conclusions. No person was contacted, no payment made, and no access restriction bypassed.
