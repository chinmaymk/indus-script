# The proposed equivalence of crab and crab + fish

The named objects do share the ending cited by Parpola, and their photographs
support the compared local sign arrangement. They have different earlier text,
however, and other signs also occur before that ending. This supports a structural
parallel; it does not independently establish synonymy, a planet reference, or
the proposed sounds.

## Exact claim and source identities

Parpola2009, printed p50/PDF14, proposes a relationship between the Dravidian
forms `kooL` and `kooL-miin` and compares CISI M-387 with M-57. He reports three
crab–fish occurrences and argues from the identical **subsequent part**. He does
not claim identical complete surroundings or require every crab sign to accompany
a fish. These remain the author's linguistic proposals, not accepted readings.

The [saved paper](../data/raw/parpola_2009_hind_leg_fish.pdf) and the
[source review](../data/processed/crab_fish_primary_review.json) preserve the
argument and its scope. No Sanskrit translations from the secondary dataset were
used in this audit.

| Object | CISI photograph | Exact metadata join | Photo reference |
|---|---|---|---|
| M-57 | p26/PDF62, original and impression | Finnish2340, DK5742, ASI63.10.89; metadata p366/PDF402 | HU175 |
| M-387 | p95/PDF131, original and impression | Finnish2041, DK10231, ASI63.10.209; metadata p368/PDF404 | HU202 |

Finnish identifiers are not silently treated as Mahadevan text numbers. The
photographs authenticate the compared local layout, not a complete fine-grained
Wells variant transcription or the identification of the forms with ancient
words. M-387's small reproduction and the export's Poor condition flag remain
limitations. This was a source-exposed review, not blinded reading or an autopsy.

## What the transcription comparison actually is

The raw export supplies these literal strings in file order:

```
M-57:  W226 W032 W231 W798 W002 W693
M-387: W226 W032      W798 W742 W060 W920
```

Both rows report right-to-left reading. The shared reading ending is therefore
`W032 W226`. M-57 has `W798 W231` before it; M-387 has `W798`. Their earlier
parts differ. This is precisely a subsequent-context comparison, not a complete
minimal pair differing only by one optional fish.

The feature catalogue links W798 to the P075/M053 family, alongside W193 and
W797. Those variants are not merged here. W231 is the internally marked fish
linked to P056/M070; the plain fish is W220/P050/M059. The ending consists of
W032/P145/M087 and the externally marked fish W226/P051/M060. These source
crosswalks are qualified; the audit does not establish universal code equivalence.
In particular, the marked fish must not silently be replaced by plain fish to
make a phonetic argument easier.

## Counts, duplicates and comparison cases

The [protocol](../data/processed/crab_fish_protocol.json) preceded new counts.
Every one of5680 raw rows was searched for exact tokens. Adjacency does not cross
line separators or uncertainty marks; unknown000 is retained as an unknown
neighbor rather than treated as a sign. Right-to-left and other/unknown directions
are distinguished. Of151 literal W798 rows,104 belong to the existing strict
subset. None of these counts establishes the total ancient corpus frequency.

Six rows have immediate reading-order W798→W231:

| Object | Raw row | Strict? | Qualification |
|---|---|---|---|
| H-132 | 1173.1 | Yes | Additional complete text |
| M-57 | 2585.1 | Yes | Named in the source argument |
| H-2584 | 2919.2 | No | Incomplete/damaged field |
| M-606 | 3067.2 | Yes | Same literal text as M-1568 |
| M-1303 | 3608.1 | No | Incomplete/damaged field |
| M-1568 | 3797.2 | Yes | Same literal text as M-606 |

Thus four strict rows represent **three distinct complete strings**. This is
compatible with a count of three text types, but does not prove that these were
the author's three selected occurrences. The four object identifiers are not
collapsed into three physical objects. Outside the named M-57/M-387 comparison, two distinct
strict strings retain this adjacency; they do not have independently known
meanings and are not retrospective blind semantic tests.

No literal W798→plain W220 adjacency occurs in reported right-to-left rows. A
predeclared simple-fish-family sensitivity finds35 adjacencies, principally20
to W240 and6 each to W231/W233. Other fish variants remain separate in the
results. Neither the narrow absence nor broad count refutes or validates the
author's linguistic proposal. No enrichment test or astral meaning follows from
these descriptive numbers.

The separate related-code scan finds three W193 rows and four W797 rows, none
with an immediate reported-right-to-left W231 neighbor. They are retained as
seven separate observations and are not pooled with W798 as proven allographs.

Five strict records share the exact file prefix W226 W032, hence the proposed
reading suffix. The next file-order code differs in all five:

| Object | Next file-order code | Role |
|---|---|---|
| M-1793 | W060 | Comparison case |
| M-57 | W231, followed by W798 | Proposed crab + fish |
| M-70 | W002 | Comparison case |
| M-387 | W798 | Proposed crab alone |
| M-811 | W803 | Comparison case |

Only three of these five have Good/Fair/Fine condition; that filter removes
M-387 as well as M-1793. Strict syntactic parsing therefore must not be mistaken
for photographic reliability. The complete earlier strings are retained in the
[result file](../results/crab_fish_audit.json).

As a separate stronger check, the previous all-sign M77 screen contains no exact
whole-prefix-and-suffix M053↔M053 M070 replacement in either order, in either
the broad or strict subset. This is conditional on the source crosswalk and the
incomplete export. It is not a refutation of the weaker published suffix claim.

## Conclusion and reproduction

The paper's local parallel is real enough to investigate, and the crab–marked-fish
adjacency repeats beyond the named example. Neither fact chooses synonymy over
different expressions sharing an ending. Independent semantic anchors, or a
frozen reading rule predicting additional independently interpretable texts,
remain absent. No sound, word, language or celestial referent is established.

Reproduce with [the audit script](../scripts/audit_crab_fish.py). The
[tests](../tests/test_crab_fish.py) guard reading direction, damage boundaries,
unknown codes and suffix anchoring. All downloads remain in `data/raw`; this phase
used retained sources only. The all417 inventory remains without established
semantic or phonetic assignments.
