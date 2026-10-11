# Sources and provenance

Accessed 22–24 September 2026; individual retrieval dates are retained. Download hashes and immutable Git revisions are recorded
in [`data/sources.json`](../data/sources.json). Do not equate a repository's claim with
an independently verified reading.

## Data actually used

The [dated Yale-document investigation](DATED_DOCUMENT_BRIDGE.md) adds eight
records totaling88,404,089bytes: Buchanan1981, the original AS16 volume and its
publisher redirectHTML, Charpin's ARCHIBAB4, the ARCHIBAB application shell,
Ricetti2020, and two bounded web/UI captures. Original catalogue, tablet-edition
and comparison-table pages were visually checked. ARCHIBAB explicitly links
YBC5447 toP306518, but no direct CDLI page or image was recovered. The current
registry has170files:142downloads,24bounded captures and4archived HTTP responses.
All remain together in `data/raw/`; the new source and review fingerprints are
verified by the offline dated-document audit.

The [BM122187 follow-up](BM122187_AUDIT.md) reuses Gadd1932, Mahadevan1977 and
Parpola1994 primary PDFs and adds one2,502-byte bounded web capture of a candidate
museum registration search. Its original catalogue pages were not recovered;
the candidate official record returned403. Registration stays unconfirmed.
At that phase the registry had162rawfiles:136downloads,22web captures and4archived HTTP
responses, all in `data/raw/`. The relation-template extension uses existing data.

The [hybrid-seal and patronymic investigation](HYBRID_SEAL_SEMANTICS.md) adds
Gadd1932's original44-page scan, the DAI edition of Vidale2005, Frenez's public
CV dated10July2024, and a bounded Vidale2004 web capture. Four new records total
7,389,069bytes. Original Gadd prose/plate and Vidale pages151–153/156 were
visually checked; the CV's publication status is a dated statement, not a current
publication guarantee. At that phase the registry contained161rawfiles:136downloads,
21web captures and4archived HTTP responses. No full Glassner2002 chapter or
authenticated Paris object image was recovered in this phase.

The [Umma audit](UMMA_ANCHOR_AUDIT.md) adds13records: the original2021IAA
project HTML, Parpola1994book scan, four archive search responses, five bounded
web captures and two failed-retrieval HTTP bodies. At that phase the registry had
157rawfiles:133downloads,20web captures and4archived HTTP responses. All are
in `data/raw/`; all13 additions have verified bytes and SHA256. The2017report's
front matter was available through web extraction, but its object page and figure
were not retrieved. The exact modern inventory ID is a labelled discovery lead.
The older published accession and five-unit M77 row were visually checked.

The residue audit retains Suryanarayan et al.2021
[paper](https://doi.org/10.1016/j.jas.2020.105291), SI3 and
[Cambridge data](https://doi.org/10.17863/CAM.54273), plus Ghosh et al.2025
[study](https://doi.org/10.1016/j.qeh.2024.100050) publisher supplements and Figure3.
The latter main-text record is a bounded author-page web extraction, not a PDF.
The PMC download interstitial is retained as an HTTP response, not scientific
content. See [the audit](RESIDUE_ANCHOR_AUDIT.md) for failed retrievals and exact
sample/photo scope. After this phase the central registry contains144rawfiles:
127downloads,15web-extraction captures and two archived HTTP responses. All are
under `data/raw/`; local derived tables and renders are separate.

The sealing follow-up uses Frenez and Tosi (2005),
[author deposit5514283](https://doi.org/10.5281/zenodo.5514283), saved as
`data/raw/sealing_frenez_tosi_2005.pdf` (1,931,287bytes). The deposit MD5 and local
SHA256 were checked. This is a primary reexamination of physical sealings, while
its container identifications and inferred contexts remain qualified. All93 rows
of Table1 are retained with discrepancies against the prose. The current analysis
does not silently substitute later contextual interpretations for the2005table.

The latest plate recovery adds eight files from the
[Mackay volume II scan](https://archive.org/details/in.gov.ignca.9954): discovery
and archive metadata, OCR, page map, OCR coordinates, and leaves12/265/275.
The plate list distinguishes drawings CXXVI from photographs CXXXI. Archive
metadata dates this volume1937; its title-page date was not newly checked.
See [the source audit](METAL_PLATE_AUDIT.md). At completion of that phase the registry contained117
downloads,14 explicitly labeled web extraction captures and one archived HTTP
response, all under `data/raw/`. Local renderings and inspection crops are derived
evidence, not additional downloads.

0. **Primary printed catalogue, added after the initial sequence study.**
   Iravatham Mahadevan (1977), *The Indus Script: Texts, Concordance and Tables*,
   Memoirs of the Archaeological Survey of India No. 77. An
   [Internet Archive scan](https://archive.org/details/TheIndusScript.TextConcordanceAndTablesIravathanMahadevan)
   and its OCR/PDF companions are stored in `data/raw/mahadevan_1977*`.
   Table I, printed pp. 717–723, supplies direct positional counts for all 417 signs.
   The sign list occupies printed pp. 32–35; the earlier derivative attribution to
   pp. 32–34 is not used as an exact primary-page reference. Source pages, cell OCR,
   corrections, and validation records are retained. Hosting does not imply an open
   redistribution license. This is a local research copy, not a new publication.
   A later inspection found a scan gap: PDF p. 768 is printed p. 757, followed by
   printed p. 760 at PDF p. 769. Printed pp. 758–759 are missing there, including
   the jar-family object-type rows. Completeness of the entire scan is not certified.
   The selected site/object rows and this limitation are recorded in
   [primary_context_subset.json](../data/processed/primary_context_subset.json).

1. **User-supplied IM-417-150.** 417 PNGs and a CSV pixel matrix. The filename and
   format correspond to the [Kaggle dataset](https://www.kaggle.com/datasets/storesource/im-417-150).
   Attribution to Mahadevan is also described by the
   [induscorpus project](https://github.com/jocchanon-prog/induscorpus).
   We verified local pixel correspondence, not the full chain back to printed sign
   plates. We do not rely on that project's example DOI or licensing claim as verified
   bibliographic metadata. The files have no inscription contexts.

2. **Secondary Wells/ICIT transcription.**
   [yajnadevam/lipi](https://github.com/yajnadevam/lipi), revision
   `fc8813a52e183d19c441631dc26c33a4dccbea39`,
   `src/assets/data/inscriptions.csv`. 5,680 rows, with excavation metadata and proposed
   readings intermixed. Only literal sign strings and selection/provenance metadata
   are used. No proposed transliterations, translations, word splits, or canonical
   sign substitutions are used. This is not an authenticated release from Wells/Fuls.
   No redistribution license for this CSV was verified; it is retained locally for
   research audit. The export can contain errors or modern edits.

3. **Independent small transcription and crosswalk.**
   [mayig/indus-valley-script-corpus](https://github.com/mayig/indus-valley-script-corpus),
   revision `ad2f1e218a34b8c33c57de0d6cb8d99272765bbb`.
   Its README explains display direction, sign features, uncertainty, and the
   work-in-progress nature of its CISI transcription. Its feature records assert
   Parpola/Mahadevan/Wells correspondences. We preserve these as provisional, including
   ambiguities. Its MIT license is saved in `data/raw/mayig_LICENSE`.
   Raw archive includes files not executed by this pipeline; only JSON and the license
   are read. These data overlap with the larger corpus and are not pooled with it.

4. **Author-published controls.** Richard Sproat's
   [nonlinguistic corpora](https://richardsproat.com/data/non-linguistic-symbols/),
   accompanying his 2014 study in *Language*, 90(2), 457–481,
   [DOI 10.1353/lan.2014.0031](https://doi.org/10.1353/lan.2014.0031).
   XML source files carry Apache-2.0 license notices. The archive includes a small
   Indus bar-seal sample and diverse comparison systems. Retain original attribution
   and license headers. Our extraction treats explicit XML lines separately.

## Research consulted

- Yadav et al. (2010), [Statistical Analysis of the Indus Script Using n-Grams](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009506).
  Primary peer-reviewed structural study. It describes Mahadevan's inventory and its
  carefully filtered EBUDS subset. Our corpus is different; our counts and scores are
  not a claimed exact replication of theirs.
- Rao et al. (2009), [A Markov model of the Indus script](https://pmc.ncbi.nlm.nih.gov/articles/PMC2721819/).
  Primary example of predicting signs without assigning established meanings.
- Rao et al. (2010), [Entropy, the Indus Script, and Language: A Reply to R. Sproat](https://aclanthology.org/J10-4016/).
  Read alongside Sproat's work; the interpretation of entropic evidence is disputed.
- Ansumali Mukhopadhyay (2019), [Interrogating Indus inscriptions to unravel their mechanisms of meaning conveyance](https://www.nature.com/articles/s41599-019-0274-1).
  Discusses numerical signs and functional sign classes. Its semantic interpretation
  is a hypothesis, not a key assumed in our models.
- Ansumali Mukhopadhyay (2023), [Semantic scope of Indus inscriptions comprising taxation, trade and craft licensing, commodity control and access control](https://www.nature.com/articles/s41599-023-02320-7).
  Provides an explicit administrative interpretation to test against alternatives.
  We do not import its semantic assignments as ground truth.

## Official source access and evidence gaps

The [Roja Muthiah Research Library's Indus Research Centre](https://rmrl.in/en/irc)
identifies [indusscript.in](https://indusscript.in/) as its corpus application. Its
public page and client were inspected. A single unauthenticated data-endpoint probe
returned `403 PERMISSION_DENIED`; access was not bypassed or retried with credentials.
The official application's machine-readable text corpus was therefore not obtained.
A scan of the printed 1977 catalogue has since been obtained from the public archive;
these are distinct sources/access routes.

This is an access limitation of this attempt, not a claim that the official corpus is
unavailable to researchers. A properly obtained, independently checked M77/IDF80
transcription would greatly improve the all-sign analysis.

Search also surfaced recent online decipherment proposals. They were not used as
accepted translations, independent confirmations, or sources of phonetic anchors.

## Quantity-anchor investigation

- J. M. Kenoyer, *The Origin, Context and Function of the Indus Script: Recent
  Insights from Harappa*, [public journal PDF](https://mohenjodarorj.sindhila.org/index.php/journal/article/download/105/81),
  saved as `data/raw/kenoyer_sindhila_inscribed_pottery.pdf`. Hosted2025 according
  to the landing page, with older field evidence reproduced; no claim of a2025
  discovery. PDF21/printed156 Figure7.2 has the H95/6640-501 drawing and labelled
  scale used for the [capacity trace](H95_PROFILE_CAPACITY.md). Drawing and caption
  accession numbers conflict; the shared excavation identifier and both labels are retained.

- Andreas Fuls (2012), *Volumenmaße von Tongefäßen der Induskultur*.
  [Author-posted public text](https://www.academia.edu/8808307/VOLUMENMA%C3%9FE_VON_TONGEF%C3%84%C3%9FEN_DER_INDUSKULTUR)
  supplies provisional Tables1–3 cells. It reports Wells2009 measurements, not
  another independent campaign. Direct PDF/page downloads returned403 and saved
  no files. The [recovery ledger](CAPACITY_TABLE_FOLLOWUP.md) preserves column and
  identifier uncertainties; [conditional calculations](CAPACITY_MODELS.md) do not
  promote these cells to visually verified observations.

- Rajesh P. N. Rao (2018), *The Indus Script and Economics. A Role for Indus
  Seals and Tablets in Rationing and Administration of Labor*, in
  *Walking with the Unicorn*, pp. 518–525.
  [Versioned author manuscript](https://arxiv.org/pdf/1812.00049v1) saved in the
  common raw folder. See [the audit](QUANTITY_ANCHORS.md); its interpretation is
  not used as training data or accepted sign values.
- Bryan K. Wells (2015), *The Archaeology and Epigraphy of Indus Writing*,
  Archaeopress, ISBN 9781784910464. Public text on
  [Scribd](https://ru.scribd.com/document/1007007442/The-Archaeology-and-Epigraphy-of-Indus-Writing-Bryan-K-Wells-Andreas-Fuls-Archaeopress-Publishing-Ltd-Oxford-2015-Archaeopress-Publishing)
  inspected for source tracing. No complete book downloaded; no login or restricted
  access used. Factual notes and access limits are in the quantity-anchor ledger.
- Jansen and Urban, eds., *Reports on Field Work Carried out at Mohenjo-Daro,
  Interim Reports Vol. 1, Pakistan 1982–83*, IsMEO / RWTH Aachen.
  [IGNCA/ASI library scan](https://ignca.gov.in/Asi_data/74331.pdf), 214 image pages,
  saved as `data/raw/mohenjo_daro_inscribed_objects_74331.pdf`.
  Includes Halim and Vidale, *Kilns, Bangles and Coated Vessels*, pp. 63–98,
  and Ute Franke, *A Selection of Inscribed Objects Recovered from Mohenjo-Daro*,
  pp. 117–138. The title and contents were checked visually. Empty PDF text extraction
  is not evidence of absent text; selected pages are rendered and OCRed for review.

These local copies are for research; public hosting is not a redistribution license.
All actual downloads, including these PDFs, have byte counts and SHA-256 hashes in
`data/sources.json`. A Kenoyer 2006 PDF request returned HTTP 403 and saved no file.

- Andreas Fuls (2020), *Ancient Writing and Modern Technologies – Structural
  Analysis of Numerical Indus Inscriptions*, *Studies on Indus Script*, pp. 57–90.
  Public author-uploaded text inspected on
  [ResearchGate](https://www.researchgate.net/publication/361812318_Ancient_Writing_and_Modern_Technologies_-_Structural_Analysis_of_Numerical_Indus_Inscriptions)
  and [Academia](https://www.academia.edu/41952485/Ancient_Writing_and_Modern_Technologies_Structural_Analysis_of_Numerical_Indus_Inscriptions).
  Browser-indexed page labels vary between versions; use formula/figure locators.
  The direct ResearchGate request returned 403, saving no file. Only the claim
  ledger is persisted; no PDF or visual verification is claimed. See the exact
  [equation audit](NUMERAL_EQUATIONS.md).

  A subsequent [local corpus screen](NUMERAL_SCREEN.md) uses the already pinned
  transcription export to test a narrow extension of the two-face interpretation.
  Its H-904 crosswalk is proposed from matching sign patterns, not authenticated
  from the publication's figure. No new source file was downloaded for that screen.

## Numeral artifact photographs

- Jagat Pati Joshi and Asko Parpola, eds. (1987), *Corpus of Indus Seals and
  Inscriptions 1: Collections in India*, Helsinki, Suomalainen Tiedeakatemia;
  Memoirs of the Archaeological Survey of India 86. The
  [IGNCA/ASI scan](https://ignca.gov.in/Asi_data/76884.pdf) is saved in the common
  raw folder as `cisi_76884.pdf`. The title page was visually checked. Its 862 PDF
  pages contain two copies of 431 pages, not two different volumes; all paired
  embedded image streams match. H-306 and M-331 pages were checked visually;
  most pages were not reviewed. See [the image audit](NUMERAL_IMAGES.md).
- Steve Farmer (2004), *Mythological functions of Indus inscriptions*, Sixth
  Harvard Indology Roundtable, 8-10 May 2004.
  [Public presentation](https://safarmer.com/indus/Harvard2004.pdf), 46 pages, saved
  as `farmer_2004_harvard.pdf`. Slide 30 located an H-306 photograph; its semantic
  interpretations are not accepted readings. A reproduced catalogue photograph
  is not a second independent artifact observation.

## Sign-family background

Shruti Daggumati and Peter Z. Revesz (2021), *A method of identifying allographs in
undeciphered scripts and its application to the Indus Valley Script*, Humanities
and Social Sciences Communications 8, 50, DOI 10.1057/s41599-021-00713-0.
The [university repository abstract](https://digitalcommons.unl.edu/mechengfacpub/563/)
was initially read as background. At that stage no full paper was downloaded and no
proposed equivalence list was imported; our predictive comparison does not claim
to replicate its method. A subsequent H-598 photograph follow-up downloaded the
full publisher paper to check a particular reported orientation correction.
The candidate families come from the previously pinned feature catalogue, with
mapping uncertainty retained.

## Primary photograph and correction follow-up

Parpola (2009), *‘Hind Leg’ + ‘Fish’: Towards Further Understanding of the Indus
Script*, Scripta 1:37–76, is archived as `data/raw/parpola_2009_hind_leg_fish.pdf`
from the public Helsinki author copy. It provides the H-598 impression and a
specific phonetic hypothesis for later testing. Its proposed readings are not
accepted decipherments in this project.

Daggumati and Revesz (2021), DOI 10.1057/s41599-021-00713-0, is archived as
`data/raw/daggumati_revesz_2021_allographs.pdf`. The publisher PDF was located
through `data/raw/revesz_publications.html`. The inspected correction concerns a
bent/Z-like sign, not H-598's final compound. Source URLs, sizes and hashes are in
`data/sources.json`; detailed access and visual evidence are in the
[photograph follow-up](ICONOGRAPHY_PHOTO_FOLLOWUP.md). Denied downloads were not
bypassed; public alternate copies supplied the retained files.

## Copper-tablet type study (additional archived source)

Asko Parpola (2008), *Copper Tablets from Mohenjo-daro and the Study of the Indus
Script*, pp.132–139, is saved as `data/raw/parpola_2008_copper_tablets.pdf` from
[the author-hosted Helsinki copy](https://tuhat.helsinki.fi/ws/portalfiles/portal/127257447/Parpola_A_2008._Copper_tablets_from_Mohenjo_daro._ECL_During_Caspers_Vol.pdf).
The download is hashed in `data/sources.json`. Figures 1a–b were visually inspected;
their subtype counts and links are retained in a separate processed ledger. These
are reconstructed types, not independent artifact-level observations. Proposed
religious or linguistic interpretations were not imported as readings. The paper
shares earlier source material with other editions and is not treated as an
independent corpus. See [the analysis and artifact-photo limitations](COPPER_BRIDGES.md).


## Bounded web-text captures for tablet context

Two clearly labeled JSON captures in `data/raw/` preserve web-tool extracts from
Meadow and Kenoyer2000, Kenoyer and Meadow2010, and Parpola2008. Original PDF
requests returned403; no original PDF bytes or unviewed-page authentication is
claimed. The source registry records URLs, extraction method, byte counts and
hashes under `web_extraction_captures`. These archived responses are verified
but not fetched as if their URLs returned identical JSON. See
[external anchors](M77_U_EXTERNAL_ANCHORS.md), [alternative models](M77_U_ALTERNATIVES.md),
and [repetition comparisons](REPETITION_EXPANSION.md).

## Exact Vats tablet records

The public Internet Archive scans of M. S. Vats, *Excavations at Harappa* (1940),
provide the photographs and excavation descriptions for the miniature-tablet
follow-up. The retained material includes the plates PDF, the text volume's OCR,
archive metadata, page-number map and selected original page JPEGs. All are in
`data/raw/`; URLs, byte counts and hashes are registered in `data/sources.json`.
Archive item `in.gov.ignca.9842` contains the plates despite its volume metadata;
`in.gov.ignca.18220` supplies the text. OCR locates passages; visible primary pages
authenticate the recorded observations.

Mahadevan's Appendix V supplies the explicit EH catalogue-number mapping. This
supports exact joins for selected references, not a general assumption that
different catalogues share numeric identifiers. Vats's descriptive fractions and
summary-table decimal measurements are preserved separately. Tablet dimensions
measure the inscribed object, not the quantity its inscription might represent.
See [the artifact bridge](M77_U_ARTIFACT_BRIDGE.md) and
[the fixed-rule follow-up](M77_U_LENGTH_HOLDOUT.md).

## Foreign artifacts and external names

`data/raw/louvre_sb2425_record.json` is the official museum JSON for the artifact
joined to M77 reference9801. Two separate JSON captures preserve bounded web-tool
responses for foreign artifact contexts and external name-anchor claims. They are
labeled extracted responses, not original PDF/HTML bytes, and are verified without
automatic refetch as if the source URLs returned identical JSON. Exact source URLs,
sizes and hashes are in `data/sources.json`; retrieved claims and unresolved joins
are separated in [the artifact review](FOREIGN_ARTIFACT_ANCHORS.md) and
[the name-anchor review](EXTERNAL_NAME_ANCHORS.md). No source-proposed translation
was added to the main corpus or sign dossiers.

## P453801 primary handcopy and versioned catalogue exports

The follow-up retains CDLI HTML/JSON and ATF exports for P453801 and P516366,
including both historical2249158 and current2289564 versions of P453801's text.
BDTNS192941 supplies the exact Owen handcopy credited to *Nisaba*15/2 no.371;
the catalogue HTML and JPEG are retained together with the other downloads.
The drawing's unread-seal legend does not identify an Indus script or owner.
Two additional web-response captures document discovery and identity checks,
clearly separated from original downloaded bytes. All URLs, sizes and hashes are
registered. See [the result and limitations](P453801_FOLLOWUP.md).

## Four-citation Meluhha name pool

The [pool audit](MELUHHA_NAME_POOL.md) adds official CDLI HTML, JSON and ATF
for P516138/CUSAS40,1354, and BDTNS catalogue, bibliography and credited handcopy
for UCTIS099/BDTNS205179/IM226931. It also retains the public search forms and
result pages used to authenticate the otherwise ambiguous UCTIS abbreviation.
Two search-result HTML snapshots depend on the preceding session; they are hash
verified but not automatically refetched from their bare URLs.

Twelve original response files and four labeled web-tool captures were added in
this phase, all in `data/raw/`. Source ledgers distinguish original bytes from
extracted web text and preserve exact URLs, hashes, dates and access failures.
The restricted Surdi/De Graef article PDF, full UCTIS book and P516138 photograph
were not obtained. The partial book preview is not a substitute for a handcopy.
The registry contains92 downloads,10 web captures and1 archived HTTP response.

## Physical-weight anchors

The [weight-anchor audit](WEIGHT_ANCHORS.md) adds eight downloaded files: the
Pettersson1999 publisher PDF, Hemmy1931/1938 weight chapters, two Vats page images,
the Hafford/Einwag/Otto2023 Ur paper, and Bibby's Bahrain paper plus publisher HTML.
Two additional web-tool captures preserve Kenoyer2010 text and Pettersson's
official indexed errata; these are explicitly not original PDF bytes. All ten
artifacts are in `data/raw/`. Failed access attempts and the original mass versus
reconstruction distinction are recorded in the accompanying ledgers and log.
The updated registry contains100 downloads,12 web captures and1 archived HTTP
response, each with URL, byte count and SHA-256 hash. The new numerical audit
reproduces conditional algebra; no local u/i/t notation is equated to an M77 ID.

## Original tool records and Kalibangan photographs

The [tool follow-up](TOOL_RECORD_FOLLOWUP.md) retains eight bounded Mackay archive
downloads (metadata, OCR, page map and five original page images), the official
2020 Kalibangan Part II report, and two NMMA indexed-text captures. Direct NMMA
HTML retrieval timed out; no museum image or original HTML is claimed. The report
PDF downloaded successfully despite the web reader's size limit. All11 additions
remain in `data/raw/`; separate ledgers record exact URLs and hashes. Current
registry:109 downloads,14 web captures and1 archived HTTP response,124 files total.
Existing CISI1 and Mahadevan sources were reused for artifact-identity checks.


## Bahrain tablet and 2026 token audit

Seven retained sources were added: five downloads and two bounded web captures,
totaling 26,993,686 bytes. All are in `data/raw/`. Gelb1980 AS21 was recovered
from the publisher's current S3 link; the obsolete PDF URLs failed. The original
page supporting the three-person list was rendered and visually inspected.
The 2026 token paper is represented by its university record, publisher's first
page and first-author public announcement; its full publisher PDF was not
recovered and the repository lists an embargo until2027-04-01.

Laursen2010 was readable through the web reader, but three direct download
routes returned403. Its limited catalogue crosswalk is therefore explicitly a
bounded extraction, not an archived complete article or inspected plate. The
other capture records excavation leads and failed retrievals. The central
registry now contains177 records:147 downloads,26 captures and4 archived HTTP
responses. The common Bahrain audit verifies13 distinct retained evidence files;
file hashes establish integrity, not the truth of an ancient reading.


## Three-chain artifact identities

Six original excavation page images from the Internet Archive were retained in
`data/raw/` (11,974,995 bytes). Four support the accepted Mackay/Vats field-number
and context checks; two initial page-locator misses are retained and marked
unused. Existing M77, CISI1 and Vats plate PDFs supply catalogue crosswalks and
published photographs. The central registry now contains 183 files: 153 downloads,
26 captures and 4 archived HTTP responses. Every entry has a URL, size and SHA-256.
The [artifact review](CHAIN_ARTIFACT_IDENTITIES.md) distinguishes printed evidence,
locator failures and unresolved accessions.


## HR2240 / M77 1471 physical context

Four Marshall1931 volumeII archive files were retained together in data/raw:
metadata, OCR, scan metadata and searchable PDF, totaling13,401,464 bytes.
The [object audit](STONE1471_CONTEXT.md) identifies the printed excavation number
and repeated figure entries, then cross-checks the already retained CISI catalogue
and photographs. New primary textual recovery reused the existing M77 PDF.
Registry total187 files:157 downloads,26 captures,4 archived HTTP responses.
Original mass, precise room and an absolute date remain unauthenticated.
