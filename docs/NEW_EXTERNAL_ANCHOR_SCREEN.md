# Five-query screen for new external anchors, 2024–2026

28 September2026. **No qualifying new artifact-to-referent anchor was authenticated in this bounded search.** This is a five-query screen, not evidence that no such discovery exists. The most relevant uncompleted lead is a December2024 Kotada Bhadli residue study: independently measured vessel contents are reported, but a join to an inscription on the same sampled artifact was not recovered. Full-text access failed, so absence of that join from the full paper is not asserted.

The inclusion rule required a primary report or original study with a specific artifact identity linking an Indus inscription to independently measured contents/counts, an independently known referent, or a parallel known-language text. New interpretations, site-wide associations, statistical structure and similar-looking non-Indus marks do not meet that rule. I first read the existing evidence-gap review and README, then checked the existing residue review to avoid treating its2025 material as new.

## Five exact queries

1. `Indus inscribed pottery residue analysis 2024 2025 2026`
2. `Harappan seals sealings contents excavation 2024 2025 journal`
3. `Indus bilingual inscription new discovery 2024 2025 2026 journal`
4. `2024 2025 2026 Indus inscription seal contents residue site:cambridge.org OR site:nature.com OR site:sciencedirect.com`
5. `2024 2025 2026 Harappan inscribed vessel quantity capacity excavation site:asi.nic.in OR site:harappa.com OR site:penn.museum`

Exact returned results are retained in `data/raw/new-anchor-2026-search-results.json`. Search dates and snippets were discovery aids, not accepted publication dates. Follow-up opens/finds/clicks are preserved in the separate primary-page capture. Both are typed **web-tool serializations**, not original HTTP pages. Nonprimary results were not used to substantiate conclusions.

## Candidate dispositions and missing joins

| Candidate | Date and what actually exists | Required join and result |
|---|---|---|
| Kotada Bhadli protein/lipid study | Publisher result identifies December2024, volume2(6),100038. It reports analyses of11 ceramic sherds, with lipid evidence; proteins did not securely identify foods. Excavation/discovery dates were not established here. | Sampled sherd→authenticated inscription photograph/sign record is still missing from the accessible material. Publisher open returned403; not retried or bypassed. **Measurement-side lead only; full-paper inspection unavailable.** [Original publisher record](https://www.sciencedirect.com/science/article/pii/S2950236524000367). |
| Karanpura/Ropar form/function study | March2025 issue; online December2024 already documented in this project's residue review. Fifteen samples and supplements previously examined. | Existing audit found no authenticated inscription-to-sample join. **Already reviewed, no new evidence in this screen.** [Publisher](https://www.sciencedirect.com/science/article/pii/S2950236524000483), [prior audit](RESIDUE_ANCHOR_AUDIT.md). |
| Rakhigarhi RGR3 first-season report | Excavation2021–22. Author repository metadata says August2025/upload2August2025, while deposited text carries a2026 issue header; release/version chronology remains unresolved. | Full-text Antiquities section, printed38, locates the steatite seal in TrenchS40W10 and explicitly says it has no Harappan characters or animal depiction. Thus the artifact/context join exists, but the inscription endpoint is absent for this reported seal. **Not an external script anchor.** [Author-deposited report](https://www.researchgate.net/publication/394241579_A_NOTE_ON_HARAPPAN_CULTURE_WITH_SOME_HIGHLIGHTS_OF_FIRST_SEASON%27S_EXCAVATION_AT_RAKHIGARHI_MOUND_NO_3_2021-22). |
| Bahaj seals and sealings | Printed2026; excavation January2024–July2025. Primary PDF retained. | Item14 is explicitly tied to BHJ-II,ZB5/Q1,825cm and to Brahmi–Kharoshthi inscriptions, pp44–45/PDF18–19. The necessary object/locus/text join exists **for other scripts**, not Indus. Jasper item3 is discussed as Early Mauryan in a Kushan deposit; stylistic continuity claims do not supply an Indus bilingual. **Scope exclusion, not a challenge to its other archaeological findings.** [Publisher PDF](https://bssspublications.com/PublishedPaper/Publish_751.pdf?v=639159167669753099). |
| Official ASI download60 | Search result presented it as recent; actual title and copyright pages identify Kalibangan, excavations1960–69, publication2015. | **Not new2024–26 evidence.** The downloaded330-page segment is byte-identical to retained `pipes_kalibangan_excavation_2015_part1.pdf`; both acquisition records remain preserved. No fresh contents/inscription join was claimed or searched through this old report. [Official PDF](https://asi.nic.in/admin/publications/ePublicationReportsDetails/download/60). |
| Merchant-mark working paper | Cambridge Open Engage version1,14November2025, explicitly not peer reviewed at posting. | Repository abstract describes aggregate catalogue/context interpretation and a proposed Dholavira cart reading. It offers no independently identified new measured artifact-to-sign join in the screened record. **Interpretation, not qualifying anchor.** Full paper not audited. [Author working-paper record](https://www.cambridge.org/engage/coe/article-details/6914735f65a54c2d4acf319d). |
| Administrative-media reassessment | Journal page says30June2026. | Abstract expressly describes a synthesis of existing reports/corpora and proposes future residue work. **No new anchor reported in the screened record.** Full paper not audited; its displayed DOI is incomplete, so no valid DOI was inferred. [Journal record](https://gipublishing.org/index.php/jis/article/view/115). |

The searches also returned2023 stylistic analysis, older linguistic/statistical papers, a2026 synthetic-baseline preprint, and non-Indus Bactrian decipherment. These do not meet the date/evidence/type rule; none was promoted to an artifact anchor. Search snippets reporting recent crawls or uploads were not treated as excavation dates.

## What is enabled next

The only retained new measurement-side lead worth a targeted continuation is the Kotada Bhadli2024 paper and its supporting sample/photo inventory. A useful next step would retrieve an openly available author or institutional version and inspect whether each sampled vessel has a field identifier and a visible inscription. A chemical measurement by itself cannot identify the signs' referent, and an inscription somewhere at the same site cannot repair that join. No extra search was run after the declared five-query bound.

No bilingual or measured-count anchor was authenticated. The Rakhigarhi and Bahaj exclusions rest on concrete object-level report statements, rather than merely reading their abstracts. The Kotada Bhadli result remains unresolved at the required artifact join, not rejected by an unseen full text.

## Persistence, errors and validation

All six new raw artifacts are in `data/raw/` with the `new-anchor-2026` prefix: two web-tool captures, two primary PDFs and their two header records. The separate [download manifest](../data/processed/new_external_anchor_downloads.json) provides kinds, URLs, sizes and SHA256, including the duplicate Kalibangan acquisition. The [machine-readable screen](../data/processed/new_external_anchor_screen.json) preserves date distinctions, joined and missing endpoints, scope and evidence pins.

The web tool could not open the17MB ASI body because of its size; the streaming download helper succeeded. The publisher residue page returned403 and was not retried. The Rakhigarhi PDF link returned a cache miss; its author-deposited full-text extraction was retained instead. The BahajPDF render emitted font-cache warnings but completed; the English item14 metadata and script names were visually checked on printed44. The Kalibangan2015 title was also visually checked. No contact, outreach, central registry edit, old-result edit or new translation occurred.
