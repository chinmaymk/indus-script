# A dated document is not automatically an Indus bilingual

Yale Babylonian Collection tablet **YBC5447** is a concrete test of a promising
decipherment route: a readable document with an ancient seal impression on it.
Its published date and personal names can constrain the historical setting, but
an Indus reading additionally requires an authenticated Indus sign sequence and
evidence relating that sequence to the readable text. Neither is supplied by a
shared motif or by a comparison seal placed beside its photograph.

This investigation follows the [foreign-name audit](EXTERNAL_NAME_ANCHORS.md)
and [hybrid-seal review](HYBRID_SEAL_SEMANTICS.md). It uses original catalogue
evidence for this particular tablet, rather than treating every artifact in an
“Indus Valley” chapter as an Indus inscription.

## What the existing primary reproduction establishes

Parpola1994, printed274/PDF292, Fig15.1, identifies YBC5447 and dates the tablet
to Gungunum's tenth year, converted there to1923BCE under the middle chronology.
The caption calls its impression a Dilmun seal and notes Amorite personal names.
Printed130/PDF148 discusses an obligated party and his father in the agreement;
the underlying cuneiform publication must govern their exact reading and roles.
The tablet's photographed surfaces were visually checked here. Their degraded
reproduction is not used for an independent fine-glyph transcription.

Printed273/PDF291 explicitly presents a merchant's Indus seal on a readable
contract as a possible future discovery. The next-page Yale illustration is a
comparison, not a claim that such an Indus bilingual has already been found.
The same section's proposed religious or pictorial correspondences are separate
interpretive hypotheses, not words independently translated by YBC5447.

## The original contract and the inferred sealer

Hallo's1965 original publication, AS16 printed200/PDF220, gives the transaction
as four talents of wool, two gur of wheat and two gur of sesame, consigned by
Luma'a to Hatin-Ibanum, son of Apkallum. It includes witnesses and an obligation
to render clearance after the journey. The edition contains restored or supplied
readings; its interpretation is preserved rather than represented as a new
cuneiform collation. No modern kilogram or litre conversion is needed here.

On printed202/PDF222, Hallo attributes the impressions to the debtor or obligated
partner as a likelihood and consequently proposes Hatin-Ibanum as the sealer.
This is a reasonable inference from the contract's roles, but it is not a name
read from the impression. Parent independently viewed both pages. The commodity
quantities belong to the cuneiform text; there is no demonstrated equation
between them and the three horizontal motif strokes in the seal reconstruction.

Thus this case improves the historical evidence for a seal used on a named,
dated commercial agreement. It does not provide an aligned Indus personal name,
commodity word or numeral value. Even accepting the proposed sealer would leave
the missing sign sequence and textual equivalence unresolved.

The [independent tablet audit](GUNGUNUM_TABLET_AUDIT.md) recovered ARCHIBAB
T24413, which explicitly identifies YBC5447 and links to CDLI P306518. The CDLI
page itself remained inaccessible; the identifier is verified through that
outgoing link. ARCHIBAB describes the impressions as uninscribed. Its date
header and a2020 table give day2, whereas Hallo's edition and ARCHIBAB's own
transliteration give day20. That discrepancy remains visible in the ledger.
ARCHIBAB's reference to two impressions is not treated as evidence of two dies;
the Yale catalogue describes stamps on several surfaces. Ur provenance remains
a textual inference, not an independently recovered excavation context.

## A separate seal must be independently matched

Ricetti2020, printed224/PDF4, Table1 no1, discusses a proposed match between
YBC5447 and a Failaka seal published as FailakaV and Kjaerum1983 no176. It reports
that the designs are variants of a common theme, attributing the rejected exact
match to Hallo2001, pp239–240. This audit recovered and viewed Ricetti's original
table, but did not recover the original Hallo chapter. That source distinction
is preserved rather than calling the later summary a fresh object autopsy.

The original Yale1981 catalogue supplies a direct visual check: printed382 and
its facing illustrations separate the YBC5447 reconstruction1090c from the
Failaka comparison1090d. The former has a circle flanked by grids above the
bucranium; the latter has a plant flanked by birds. Parent and catalogue-review
agent independently viewed these pages. Those published reconstructions differ;
this is not an autopsy or a test of whether a seal could have been recut.

The same catalogue describes Indus characters on entries1088 and1089, separate
objects above1090. Its1090 entry describes the figures and motifs without
identifying a corresponding Indus inscription. Neither the section heading nor
the proximity of1088/1089 transfers their sign status to the dated tablet.

The [original seal-discussion audit](YALE_DATED_SEAL_AUDIT.md) also preserves an
important qualification. Buchanan1965, printed206–207 and note17, compares the
Yale grids with Marshall signs ccxcvi–ccc. He discusses their possible survival
as motifs within his TypeIII designs, rather than supplying a written sequence.
The resemblance is real as a published proposal; it supplies neither an M77
code mapping nor a name or commodity reading. His drawing is a composite of
visible impression fragments, with possible seal-edge strokes at its bottom.

Table1 no2 concerns a different proposed pair: Mackay1938 seal661 and
impression20. It labels that pair doubtful. No inscription or identity from
those Mohenjo-daro objects is transferred to YBC5447.

An exact seal-impression match could connect two artifacts. A merely similar
scene cannot. Even an exact match would not by itself prove that the scene or
an adjacent inscription spelled the document's debtor, creditor or witness.
The identity of the sealer and the semantic relationship between texts remain
separate questions.

## Persisted source review

The parent review is in
[yale_anchor_parent_review.json](../data/processed/yale_anchor_parent_review.json).
It pins the source PDFs, the bounded search capture and parent-viewed renders.
The full Ricetti text extraction is retained for navigation; the source PDF and
page images govern table layout and attribution. Downloads remain in `data/raw/`.
The [original Yale catalogue review](YALE_DATED_SEAL_AUDIT.md) also covers
Buchanan's original1965 motif discussion, including its visual analogies and
limitations. The [separate tablet review](GUNGUNUM_TABLET_AUDIT.md) preserves
contract readings and restorations. `scripts/audit_dated_document_bridge.py` verifies the retained
evidence and reproduces the parent source extracts in the offline pipeline.

The three ledgers collectively pin32 distinct evidence files. Their source
claims, human visual checks and exact byte verification remain separate evidence
layers. The results are saved in
[dated_document_bridge_audit.json](../results/dated_document_bridge_audit.json).

No Indus code is assigned from an isolated geometric resemblance, and no
semantic or phonetic value is established by these parent-reviewed pages.
