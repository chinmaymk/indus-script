# H-1817 identity follow-up

The bounded follow-up did **not recover an accessible original illustration or basic-data entry for H-1817 / H94-2326 / Figure26.06**. Its artifact-level identification and graphic comparison remain unresolved. This is an access/search outcome, not evidence that the object or publication does not exist.

## Routes tested

1. Exact field, catalogue alias and figure searches: `"Harappa" "1994" "26.06"`, `"Harappa" "H94-2326"`, `"H1817" Indus corpus`, and later `"Harappa" "2326" tablet`. No authenticated target page emerged. The short H1817 query produced unrelated Hebrew concordance/medical identifiers; those were rejected.
2. Author/institution/report route: searches restricted to Harvard, Wisconsin and DASH, plus the HARP project page. Results led to project descriptions, faculty pages, published syntheses and citations of the 1994 submitted report, not its Figure26.06. A direct web-reader attempt at Harvard's faculty page returned403; no access restriction was bypassed. The accessible [HARP page](https://www.harappa.com/content/harp) supplied no report attachment in the retrieved representation.
3. Full CISI3.1 route: title, ISBN9789514110405, MASI96 and publisher/institution searches. The [University of Helsinki record](https://researchportal.helsinki.fi/en/publications/corpus-of-indus-seals-and-inscriptions-volume-3-new-material-untr/) identifies the 2010 volume, 504 pages, ISBN978-951-41-1040-5, but the retrieved record provides bibliography rather than the requested photographic/basic-data pages. Other results included the already known introductory extract, other volumes, reviews and bibliographies; none was promoted to a full-volume source.
4. Public Archive catalogue API: `title:(Harappa) AND (1994 OR "Archaeological Research Project")` returned one record, the **1986–1990** excavation reports. `title:("Corpus of Indus Seals")` returned two records: `corpus-vol-2`, whose title actually says volume1, and `corpus-vol-2_202409`, labelled volume2. Neither returned record is the requested volume3.1. The API's actual JSON bytes are retained; these limited title queries do not exhaust every possible archive item.
5. Alternate public scan index: the [Sanskrit Documents index of ASI/IGNCA scans](https://sanskritdocuments.org/scannedbooks/asiallpdfs.html) was checked as a locator. Its retrieved `Corpus` matches concern *Corpus Inscriptionum Indicarum*, and the broad96 match is unrelated numbering. No authenticated MASI96/CISI3.1 target link was obtained. This secondary index is not evidence for the tablet.

The earlier 1997 paper and 17-page 2010 introductory extract had already failed to supply H94-2326/Figure26.06 in `docs/COMB_TABLET_PRIMARY_REVIEW.md`. Their prior403 direct-download attempts were not repeated. A bibliography or a similarly dated excavation paper is not substituted for the cited 1994 report.

## Retained material and stopping point

- `data/raw/h1817_archive_report_search.json` and `data/raw/h1817_archive_cisi_search.json`: original public API response bytes, **not original excavation reports or catalogues**.
- `data/raw/h1817_identity_web_captures.json`: eight web-tool search/open capture batches, explicitly **not original source-document bytes**.
- `data/processed/h1817_identity_followup.json`: exact search strings, inspected URLs, outcomes and evidence hashes.
- `data/processed/h1817_identity_new_sources.json`: pending typed source provenance; no central registry edit.
- `scripts/download_h1817_identity_sources.py` and its saved request plan reproduce the two public catalogue queries.

The bounded search stops here after these distinct routes. Further useful evidence would be an accessible original HARP1994 Figure26.06 or the full CISI3.1 H-1817 photograph plus basic-data entry. No messages were sent, purchases made, or restricted files accessed. No sign value, object identity, allography, or chronological inference is promoted by this follow-up.
