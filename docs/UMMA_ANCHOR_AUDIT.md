# Umma: contact evidence without an authenticated reading anchor

This audit distinguishes the older Ashmolean clay tag from the modern SAHI
surface-find lead. Neither currently supplies a verified correspondence between
an Indus inscription and readable cuneiform. No semantic or phonetic value follows.

| Case | Evidence recovered | Limit |
|---|---|---|
| Older Umma/Djoka, M77 9811 | Parpola1994 Fig7.16 identifies Ashmolean1931.120; parent and agent viewed both photographs and caption | Dealer-attributed findspot, no excavated context authenticated |
| Modern SAHI find, provisionally TJ17-PRO-S56 | Project director reports Harappan impressions recovered in topographic survey; Frenez2023 Fig3D cites2017report p59 Fig6.61 | Primary object page and photograph not recovered; exact ID known only through a discovery post |
| TJ19-2A-K54-T1 | Project director describes an excavated Sumerian field-sale tablet, Early DynasticIIIb | Separate object; no reported physical join or shared sealing with either Indus object |

## What was checked

The [older-object audit](UMMA_OLDER_SEALING_IDENTITY.md) identifies the clay tag as
Ashmolean1931.120 using Parpola's published caption. The reverse photograph supports
cloth contact. Tosi's account reconstructs a cloth-covered jar mouth, but no
contents, fiber identification or quantity was authenticated. The historical
Umma attribution is explicitly unconfirmed in that account. It cannot be used
to assign the sign sequence to a particular Umma merchant or contract.

The [project director's account](https://iaassyriology.com/in-the-field-the-project-sahi-tell-jokha/)
was downloaded as original HTML. Its article body identifies Drahoslav Hulínek
as author; the page's publisher metadata names Stefania Ermidoro. The page was
published22January2021. It reports Harappan seal impressions found in topographic
survey without listing their individual identifiers. The separate paragraph on
TJ19-2A-K54-T1 describes a Sumerian contract involving a partly named shepherd,
Lu-kala-ga, and a governor whose name is incomplete. That tablet comes from
Trench2A. The article establishes no same-object connection between this contract
and an Indus inscription. Even secure co-location would not itself establish
parallel wording or identify an Indus seal owner.

Frenez2023's [author-deposited review](https://www.academia.edu/108938835/Indus_Valley_Early_Commercial_Connections_with_Central_and_Western_Asia)
distinguishes old Fig3E from new Fig3D, citing the2017SAHIreport p59 Fig6.61 forD.
It calls the new object a square seal associated with recent excavations. This
secondary shorthand must not override the project's survey description. The
correspondence between the general survey statement and this particular object
remains unverified without the primary report page.

The exact number **TJ17-PRO-S56**, report's alleged seal-or-impression ambiguity,
PRO/S code expansions, and proposed180degree rotation were encountered in a
[June2026 discovery post](https://www.reddit.com/r/Dravidiology/comments/1u1cgao/dug_in_some_dig_reports/).
The duplicate post is not independent evidence. These claims are retained as
leads, not primary observations. No modern-find image was successfully retrieved
or visually examined, no rotation was performed, and no sign transcription or
direction was assigned. Seal and impression would require different treatment
of mirroring; the unavailable image cannot resolve that question.

## Retrieval and pagination limits

ResearchGate identifies the2017report, its editors and ISBN978-80-89704-05-7.
The author's Academia page exposes its front matter and contents, but not p59.
Those contents start the small-finds chapter at53 and textual records at61;
other bibliographic search results give54–61 and62–63. These may reflect versions
or pagination differences, but no offset is assumed. The2018imprint appears in
the recovered front matter. The report's excavation year is2017.

The SAHI landing-page request timed out after45seconds. ResearchGate's extracted
download link led to a malformed URL/404; the corrected public URL returned403
through curl and a cache miss through web retrieval. Academia direct HTML returned403;
its download link produced a cache miss, and the auto-download variant failed.
Direct Harappa review-page and figure requests also returned403. None of these
failed requests yielded a primary PDF or figure. These failures are not evidence
that the objects are absent. The successful IAA download and bounded web captures
are retained in `data/raw/`; failures with no saved body are logged here only.

## Consequence for decipherment

The new lead strengthens the case for investigating actual administrative use
of Indus seals outside the Indus region, subject to primary verification. The
older clay tag supports physical contact with a textile surface. Neither supplies
a dictionary entry. Matching the word Umma across an object catalogue and a
cuneiform tablet would create an unsupported identity join. Matching cloth traces
to an Indus sign would likewise conflate packaging with inscription content.

The [structured review](../data/processed/umma_anchor_review.json) preserves the
three object identities and missing joins. The [offline audit script](../scripts/audit_umma_anchors.py)
checks source fingerprints and reconstructs the relevant IAA paragraphs from the
archived HTML, recording no authenticated bilingual or contents anchor. Its
output is an audit of these reviewed cases, not a statistical test of every
Umma find or a proof that undiscovered anchors cannot exist.

The most useful next evidence is the actual2017report object page and catalogue
entry, museum accession records for1931.120, and any documented physical join to
a cuneiform envelope or authenticated contents sample. Improving orientation or
glyph segmentation alone would improve the corpus without establishing meaning.
