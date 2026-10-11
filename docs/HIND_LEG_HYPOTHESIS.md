# Auditing the proposed “hind leg” reading

**The local corpus supplies no independent semantic confirmation of the proposed
`taaL` reading.** It supplies eight occurrences of two candidate codes, including
one leg–fish combination already used to construct the hypothesis. The remaining
contexts are useful constraints, but none has an independently known reading.
There is also a concrete catalogue-mapping gap that must be retained.

## What the paper actually proposes

Parpola's 2009 paper, printed pp.62–64 (PDF pp.26–28), proposes `taaL` for the
limb-shaped sign and `taaL + miin` for its combination with plain fish on M-1690.
The argument connects a Tamil leg word and a celestial usage; it allows a compound
not directly attested in the cited lexicon. M-71 illustrates the limb's shape.
The author explicitly seeks testing in other contexts and points to M-290, whose
next sign he identifies tentatively as dog or wild ass. He does **not** require
every limb occurrence to precede fish or denote a star.

Source: [saved paper](../data/raw/parpola_2009_hind_leg_fish.pdf).
The precise argument, page references, source hashes and visual observations are
retained in the [audit ledger](../data/processed/hind_leg_hypothesis_ledger.json).
These are the author's proposed interpretations, not established sign values.

## Identifiers and reading order

The literal secondary records align the proposed limb with **W278 on M-1690** and
**W279 on M-71 and M-290**. Fig.15a puts fish immediately to the display-left of
the limb. With the source's right-to-left direction, the literal file pair
`W220 W278` corresponds to the paper's proposed reading sequence leg → fish.
Reversing the pair silently would produce the wrong adjacency test.

The M-71 impression in CISI volume 1, printed p.31/PDF p.67, visibly places the
hatched limb at the export's second position from the left, supporting the W279
alignment. This corroborates an object/position correspondence, not the full
meaning or historical pronunciation. The M-290 photograph at printed p.70/PDF
p.106 was also inspected; its small animal figure does not settle species.

The pinned feature catalogue contains **no W278 or W279 crosswalk entry**.
The supplied **M084** image resembles M-71's limb, and **P045** has a matching
limb description, but P045/M084 formally lists **W280**, a different code.
Consequently M084/P045 is a visual-family candidate, not an authenticated alias
for W278/W279. No dossier mapping has been overwritten. P046/M085/W281 is a
further decorated relative and likewise remains separate.

Plain fish has the source-asserted mapping W220/P050/M059. The animal following
the limb on M-290 is W345, grouped by the feature catalogue under P043/M050 with
a deer description. That differs from the paper's dog/wild-ass interpretation.
This disagreement is material: selecting an animal word requires first resolving
which animal, if any, the sign depicts.

## Every recorded candidate occurrence

The script searches **all 5,680 raw rows**, including rejected, damaged and
unknown-direction records. It matches exact three-digit tokens and never joins
neighbors across damage or line separators. Digits in this table are W codes;
all sequences retain literal file order.

| Object / local row | Literal sequence | Strict subset | Role in paper's argument |
|---|---|---|---|
| K-45 / 1911.1 | `391 741 442 279` | No: unknown direction | Not named |
| M-1864 / 2207.1 | `]460 503 741 279+` | No: damaged/uncertain completeness | Not named |
| M-1690 / 2403.1 | `520 070 220 032 240 838 741 958 220 278` | Yes | Discovery context |
| M-71 / 2599.1 | `151 279 142 002 390 095` | Yes | Shape illustration |
| M-226 / 2750.1 | `740 365 278 061` | Yes | Not named |
| M-290 / 2810.1 | `400 345 279` | Yes | Proposed additional context |
| Salut / 4173.1, no CISI ID | `392 004 002 278 595` | Yes | Not named |
| Dholavira / 4209.1, no CISI ID | `740 384 002 629 279` | Yes | Not named |

There are three W278 and five W279 occurrences, each on a different source row.
Seven have reported right-to-left direction; six meet the strict corpus filter.
Only M-1690 has immediate plain fish after the candidate in that reading order.
Outside M-1690 there are seven rows and zero such pairs. This absence does not
falsify the paper's phonetic proposal, because it makes no universal adjacency
claim. It does mean this local export offers **no replication of the proposed
compound on another object**.

Five objects are not named in this selected argument; only three of those meet
the strict filter. “Not named” is not proof that the author never saw them, and
we cannot turn them into a historical blind test retroactively. M-71 and M-290
are explicitly source-exposed and must not be described as withheld validation.

The related-code sensitivity is saved separately: W280 appears on H-90; W281
appears on H-447 and local 5235.1 at Lakhanjo-daro. None supplies an additional
plain-fish pair in its reported reading direction. These three occurrences are
**not** included in the eight-candidate count or silently merged with W278/W279.

## What can actually be predicted and tested

A fixed `taaL` value would constrain an independently identified neighboring
word on another object. For example, M-290 gives the conditional sequence
`taaL + value(W345) + value(W400)` in the reported reading direction. Neither
remaining value has an independently established sound here. Choosing dog, wild
ass or deer, then searching flexible lexica for a plausible compound, would add
uncontrolled choices rather than score a fixed prediction.

The three strict, unmentioned contexts are more concrete future test targets:
M-226 pairs the candidate with W365 on its display-left; Salut 4173.1 with W002;
Dholavira 4209.1 with W629. Their complete literal strings and surrounding signs
are retained. A semantic test would require a prediction fixed before consulting
an independent translation, named astronomical scene, bilingual correspondence,
or otherwise externally identified referent. None is available for these objects
in the inspected sources. Mere compatibility with some later word is insufficient
to distinguish `taaL` from alternative phonetic proposals.

Thus the present result is **a bounded, unconfirmed reading hypothesis with an
explicit evidence gap**, rather than its verification or refutation. Its relevant
next needs are an authenticated W278/W279-to-primary-sign crosswalk, resolved
neighboring sign identities, and a semantic observation not used to construct
the proposed reading.

## Reproduce

Run `python3 scripts/audit_hind_leg_hypothesis.py`. The
[script](../scripts/audit_hind_leg_hypothesis.py) writes
[all candidate witnesses](../results/hind_leg_occurrences.csv),
[separate related-code witnesses](../results/hind_leg_related_not_merged.csv), and
the [machine-readable summary and catalogue entries](../results/hind_leg_audit.json).
No secondary-export translation column is used. Four
[tests](../tests/test_hind_leg_hypothesis.py) check exact token boundaries,
damage handling, reading direction and source-exposure classification. No new
file was downloaded for this audit; existing raw sources remain together in
`data/raw/`.
