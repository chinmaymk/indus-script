# Copper tablets: external associations without a premature reading

**The evidence supports testing associations between whole inscriptions and motifs,
but does not yet establish a word or sound.** The literal export links the same W777
singleton to both `Goat:8` and `Anth` through different shared inscriptions. This is
a concrete obstacle to assigning it a unique pictured-animal name *if* those links
and their semantic equivalence are accepted. The goat bridge disappears when poor
source-condition rows are excluded. Neither its truth nor its falsity follows from
that sensitivity alone.

## Published type evidence

[Parpola (2008), pp. 132–139](https://tuhat.helsinki.fi/ws/portalfiles/portal/127257447/Parpola_A_2008._Copper_tablets_from_Mohenjo_daro._ECL_During_Caspers_Vol.pdf)
supplies reconstructed copper-tablet types. Classification can use partly preserved
text or imagery. Consequently, these types cannot serve as independent, fully read
artifact observations. Figures 1a–b depict the same reverse pictogram on C5 and C6,
linked through inscriptions to B9 and B19 respectively. The depicted motifs differ:
a goat-like creature and an archer. The proposed religious interpretation remains
a hypothesis.

The [transcribed count ledger](../data/processed/copper_types_2008.json) contains all
46 depicted subtypes. Its sums reproduce the reported shape totals: A=34, B=144,
C=39, total 217. This verifies our count transcription, not the underlying object
classification. It is a single visual pass. The eight published links are retained,
including the exceptional B12-reverse/B6-obverse link. C1 has a geometric motif,
so not all linked reverses should be labelled single written signs. No full
artifact-to-type membership list accompanies the figures.

## An independently executed check of the literal export

The [script](../scripts/audit_copper_bridges.py) searches the pinned transcription
export, without importing its language readings. This is a separate calculation,
**not independent archaeological evidence**: the export and paper can rely on the
same objects and earlier editions.

The [protocol](../data/processed/copper_bridge_protocol.json) requires:

1. Mohenjo-daro rows labelled `TAB:C`, complete literal text, no unknown signs,
   and the existing strict parsing rules. `NR` is additionally allowed for a single
   token, whose order cannot be reversed.
2. A donor artifact with exactly one qualifying singleton row and one qualifying
   longer-text row, and no qualifying motif-bearing row. This does not establish
   that all physical faces were recorded.
3. A different artifact with exactly the same longer text and a recorded motif.

No sign variants are merged. No left-to-right text is reversed into a match. Missing
signs are not reconstructed. Literal labels such as `Othr`, `Buff`, and `Goat:8`
remain source annotations rather than harmonized zoological identifications.

There are **191 eligible rows** and **10 singleton/text/motif triples**, involving
seven distinct singleton codes. The [full witness ledger](../results/copper_bridge_audit.json)
retains both donor-side IDs and every matching motif row. The
[compact table](../results/copper_bridges.csv) lists their artifacts. Repeated rows
of the same artifact do not increase its artifact count.

| Singleton | Literal motif labels linked through shared text |
|---|---|
| W341 | Rhin |
| W749 | Othr |
| W753 | Hare |
| W777 | Anth, Buff, Goat:8, Othr |
| W780 | Anth |
| W781 | Anth |
| W782 | Anth |

These labels are not the meanings of the signs. In particular, different codes
linked to `Anth` are not automatically allographs. Similar text contexts can also
accommodate distinct roles or categories. The export's `TAB:C` category is not
assumed identical to the paper's incised/painted-tablet definition.

## Exact W777 witnesses and sensitivity

The goat-side bridge is:

```
M-1555 / M-1556 / M-1557 / M-1558
  singleton: W777
  other text: W407 W032 W520 W095 W585 W017 W231
same text on M-548, motif label Goat:8
```

The human-figure bridge includes:

```
M-604
  singleton: W777
  other text: W740 W900 W850 W407 W061 W845 W806
same text on M-585 and M-587, motif label Anth
```

The first text also connects to `Othr` on M-547 and `Buff` on an object without a
CISI identifier (`lipi_id:5587`). These labels could reflect inconsistent motif
classification; they are not evidence of four securely distinct ancient concepts.

Requiring **Good or Fair on every contributing row** leaves 94 eligible rows and
three triples: W777, W780, and W782, all connected to `Anth` through the same longer
text. The goat donors are all Poor. The hare donors are Poor, and the only literal
rhinoceros recipient is Poor. Thus the result depends materially on reading damaged
objects. This screen is not a statistical significance test: duplicates and shared
editorial reconstruction cannot be turned into independent confirmations by counting.

## What the photographs actually verify

The [visual ledger](../data/processed/copper_visual_review.json) records page and
artifact locators, source hash, observations, and unresolved details. It uses the
first copy in the archived CISI volume.

- M-534, printed p.134/PDF170, clearly pairs a multi-sign inscription with a
  long-eared animal and vegetation. It supports the physical text–motif pairing.
- M-593, p.150/PDF186, has a similar text on A, but its B photograph is too faint
  to authenticate the proposed W753 singleton. The hare bridge is therefore not
  fully verified by these two photographs.
- M-585 and M-587, p.148/PDF184, show archer-like imagery. Their A texts are worn.
- M-604, p.152/PDF188, has an A text and two photographs of B. Fine details remain
  degraded; the source's Good label is not a substitute for exact visual verification.
- M-599, p.151/PDF187, is visible but its L/R transcription is outside this literal
  R/L screen. It is not forced into a matching sequence.

The goat singleton donors M-1555–1558 are outside the downloaded volume. **No entire
bridge has yet been independently authenticated on both donor and motif objects
from these photographs.** That limit applies even though the literal matches and
published reconstructed-type links are reproducible.

## Constraint on a proposed decipherment

Let R(s,m) mean that this procedure connects singleton s with motif m. A proposed
rule that every such connection is a literal, unique animal-name translation
requires each sign's distinct animal referents to collapse to one. The two W777
paths challenge that rule, conditional on the source identifications being correct.

Several alternatives fit the observed association: a shared institution could use
different emblems; a ritual category could encompass several figures; or the text
and reverse might be related without saying the same thing. These are countermodels,
not established historical explanations. The pictures alone do not select one.

Nor does a seven-sign text paired with a hare identify which of its signs, if any,
means “hare.” Reading W753 as that word additionally assumes equivalence of the two
reverses, correct glyph identification, and literal naming. Assigning sounds would
require further evidence beyond those assumptions.

The next discriminating evidence is legible artifact-level confirmation of the
donor sides, followed by testing a fixed interpretation on further objects and
contexts. This audit has supplied specific targets and a quality sensitivity;
it has not established a phonetic or semantic value for any of the 417 signs.
