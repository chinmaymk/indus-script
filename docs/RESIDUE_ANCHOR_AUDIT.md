# Residue-to-inscription anchor audit

Research date: 2026-09-24. This bounded audit found **no authenticated join between an Indus sign sequence and chemically identified contents** in the two targeted studies. This is a result about the reviewed records, not a claim that such a vessel cannot exist.

## Suryanarayan et al. 2021

The [primary paper](https://doi.org/10.1016/j.jas.2020.105291) analyzes 172 pottery fragments. Its [Cambridge dataset](https://doi.org/10.17863/CAM.54273) contains 124 CSV rows: 122 archaeological records across seven sites and two modern comparators. It is not the full 172-fragment inventory. There are no inscription or glyph columns. SI3 supplies sample identifiers, contexts, vessel classifications, photographs and chemical results; its text contains no inscription transcription.

All 24 SI3 pages containing photographs were visually reviewed at 1500-pixel page resolution: 1–2, 6–9, 13–16, 19–21, 23–24, 26–29, 32–36. This is a screening review of published small photographs, not artifact authentication. Paint bands, perforations and modern inventory ink are visible; no secure script sequence was established. Some records lack photographs or one side. FRN24 has a painted band pattern and a CSV lipid yield of 7.087342989 µg/g, but no isotope values; its pattern was not identified as writing. FRN27 has painted decoration but is starred as below the 5 µg/g threshold. Neither establishes a content word.

## Ghosh et al. 2025 (online December 2024)

The [author-deposited text](https://www.researchgate.net/publication/387048617_Does_Form_entail_Function_Understanding_Pottery_Functionalities_through_Absorbed_Residues_within_Ceramics_from_the_Harappan_Sites_of_Karanpura_and_Ropar_in_India) mentions Ropar inscriptions in site background, without joining them to residue samples. Figure 3, reviewed directly, shows KRN15 with repeated wavy incisions and RPR153 with parallel grooves. These are not authenticated sign sequences. Its RPR62 photograph is perforated, matching the caption but conflicting with the supplement's cooking-pot classification.

Downloaded publisher SI I and SI II contain nine Karanpura and six Ropar sample rows. The columns join contexts, vessel types and chemical measurements, but contain no sign descriptions. KRN15 and RPR153 report NA for composition/yield; KRN18 and KRN13 report small yields of 3.4401 and 2.6190 µg/g. These numbers do not establish specific contents or meanings. SI II includes post-Gupta RPR18, so all fifteen are not Harappan-period samples.

SI III has additional unresolved identifier conflicts: rows sharing context/yield/porosity with SI I change KRN15→KRN16, KRN02→KRN183, KRN183→KRN187 and KRN76→KRN77. These are correspondences by other fields, not proven identity corrections; no names were silently repaired.

## Consequence for decipherment

A residue measurement is an independent measurement of a vessel's use history. It becomes a candidate semantic anchor only after the measured sherd is securely joined to an authenticated inscription, and an association between that inscription and contents is tested against alternatives such as owner, maker, capacity or repeated use. Vessel shape, regional cuisine and a site-level report of writing cannot supply that missing join. This audit therefore adds no semantic or phonetic values to the 417-sign inventory.

The main opportunity is to obtain the original photographic/sample registers for decorated or inscribed sherds, with conservation histories and repeatable sign transcriptions, then compare contents across multiple securely identified objects. A single pot's chemical residue need not be the object named by its text.

## Retrieval and reproducibility

All eleven saved remote records/captures are under `data/raw/residue_*`; `data/processed/residue_downloads.json` records URLs, bytes and SHA256. One is a PMC download-interstitial HTML response, explicitly not a PDF. One is a web-tool extraction of the author's page, not original HTML. Main 2021 PDF, SI3 PDF, CSV, repository HTML, PMC HTML, three 2025 DOCX supplements and Figure 3 were retrieved directly.

Failures: initial sandbox curl could not resolve Oxford; authorized network retrieval succeeded. Web browsing of PMC returned a browser-check page; direct HTML retrieval succeeded. ScienceDirect and direct ResearchGate HTML/PDF returned 403; a web-tool ResearchGate download link returned 404. PMC SI3 returned an HTML download interstitial with status success; it was renamed and retained. The Elsevier CDN supplied SI3 and the three later supplements. A preliminary local BeautifulSoup import failed because that optional package is absent; standard-library parsing replaced it. No protection was bypassed.

Run `python3 scripts/audit_residue_samples.py` to regenerate the metadata audit. Literal DOCX tables are retained in `results/residue_sample_metadata.json`; visual evidence and limitations are in `data/processed/residue_anchor_audit.json`. Rendering used bundled Poppler with `-scale-to 1500 -png`; 42 local page PNGs remain in `results/primary_pages/residue-si3-*`. The 18 non-photographic pages were text-extracted, not all visually inspected. No absence claim is based solely on a keyword search.
