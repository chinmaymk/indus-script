# Four cited tablets: external-name anchor audit

The four personal-name citations in Surdi and De Graef (2025), note22, supply
**no established Indus sequence independently attributable to a named person** in
the evidence recovered here. One additional record preserves part of a cuneiform
seal legend; another is explicitly marked unsealed in its catalogue. These results
narrow this particular route to testing phonetic readings. They do not determine
whether Indus texts elsewhere contain personal names.

## Selection and results

The [fixed scope](../data/processed/meluhha_name_pool_protocol.json) includes the
note's four personal-name citations. Its two village/granary examples are outside
this test. The note and institutional bibliography were available through web
extraction; the restricted article PDF was not obtained. This is not an exhaustive
search of every Meluhha-associated person. [Article, note22](https://www.tandfonline.com/doi/full/10.1080/00856401.2025.2488137).

| Publication | Authenticated record | Seal evidence recovered | Name-anchor result |
|---|---|---|---|
| Nisaba15/2,371 | CDLI P453801; BDTNS192941 | Published drawing labels seal illegible, with no seal signs drawn | No readable Indus string |
| CUSAS40/2,1582 | CDLI P516366 | Export marks seal illegible; possible duplicate of preceding text, with date conflict | No readable Indus string or independent witness established |
| CUSAS40/2,1354 | CDLI P516138 | Export gives three seal lines: lost material, a partially restored scribe title, and a patronymic with the name lost | Partly readable cuneiform legend; no recovered Indus/name pairing |
| UCTIS099 | BDTNS205179; IM226931 | Catalogue explicitly marks Seal=N; credited handcopy shows two cuneiform faces | No seal or Indus sequence supplied by the inspected record |

Detailed reviews: [P453801/P516366](P453801_FOLLOWUP.md),
[P516138](P516138_ANCHOR_REVIEW.md), and [UCTIS099](UCTIS99_ANCHOR_REVIEW.md).

## What the names actually establish

The three CDLI exports contain `na-na-sa3`, `sa6-ma-ar` and `a-li-a-hi dam-a-ni`.
The UCTIS catalogue reads the first name as Na-na-za; the older P453801 revision
also has `na-na-za`. Spelling/editorial differences are retained. They do not
license arbitrary substitutions in a proposed Indus phonetic key.

All four records report the same basic oil-allotment pattern: one unit for each
of the first two named recipients and half for Ali-ahi, with the wife relationship
expressed in the text. Damage and restoration are explicit in the exports. The
records associate the recipients with Meluhha. That association alone does not
identify the language of each name, or establish that a recipient owned the seal.
These statements use catalogue readings, not a fresh decipherment of cuneiform.

P516138's seal field reads `[...]`, `dub-[sar]`, `dumu [...]`. It preserves a
partially restored professional title and a patronymic formula; the individual
names are missing. Its top-level Sumerian metadata is not being used to classify
an otherwise unread seal: here the export actually supplies seal-specific
cuneiform transliteration. No photograph or primary handcopy of that impression
was recovered in this bounded search. [Official record](https://cdli.earth/artifacts/516138).

The UCTIS drawing was independently viewed by the parent and reviewing agent.
It shows two cuneiform tablet faces and no separately drawn seal legend. Its
catalogue's explicit N flag is stronger than merely finding no seal field in an
export, but remains a published catalogue assessment rather than a new autopsy.
[BDTNS205179](https://bdtns.cesga.es/205179).

## Independence and missing evidence

Four publication citations are not four independently established physical
witnesses. The P453801/P516366 possible duplication remains unresolved. P516138
is dated SS06.03.00 in CDLI, while its actual year formula is damaged; UCTIS099 is
dated SS09.01.00 in BDTNS. These dates help distinguish catalogue records but do
not justify silently resolving the existing date conflict or assigning identities
to unknown sealers. Shared generic P533185/S999999 seal relations do not identify
a common physical seal.

No admitted name pair remains on which to fit or score an Indus reading key in
this finite pool. This is an evidence-availability result, not a failed phonetic
prediction, a statistical p-value, or proof that no bilingual can exist. A
meaningful next test requires a readable Indus impression plus independent
evidence assigning the represented name to it, or recovery of a separately
identified repeated impression that supplies the missing link.

## Reproduction

`scripts/audit_meluhha_name_pool.py` compares the three pinned CDLI JSON exports,
preserves exact line text and seal fields, and locates literal name spellings.
The UCTIS record remains a separately sourced BDTNS review; it is not fabricated
as a CDLI export. The [output](../results/meluhha_name_pool_audit.json) distinguishes
publication count, export count and unknown independent-object count. Exact-token
matching deliberately does not repair damaged names or expand suffixed forms.

All downloads remain in `data/raw/`, with URLs, byte counts and hashes in
`data/sources.json`. The [research log](RESEARCH_LOG.md) records retrieval failures,
corrections, evidence limits and validation. No ancient Indus sound or meaning
was assigned by this audit.
