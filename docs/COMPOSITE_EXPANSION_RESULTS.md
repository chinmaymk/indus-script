# Composite shapes and one-sign/two-sign replacements

Two newly checked primary pairs show that a single sign and a two-sign sequence
can occupy the same complete textual context. They do not establish that the
single sign combines the meanings or sounds of the pair. A screen of every
catalogue code finds thousands of such replacements, most in very short contexts.

This distinction matters for a proposed account of all signs: **graphical parts,
replaceable sequences, and compositional meaning are three separate claims**.
The earlier report's phrase “partly compositional notation” was too broad without
that distinction and has been qualified.

## Shape review before inspecting counts

The primary representative signlist, printed pp32–35 (PDF43–46), was inspected
across all417 codes. M317 has an enclosing arch around three upper and two lower
short strokes. Its interior resembles M107 more closely than M106, whose five
strokes sit in one row. However, the candidate outer M312 is a low rounded arch,
whereas M317 has a tall pointed enclosure. These are provisional graphic
comparisons, not established component identities.

The sole indexed M317 field, `M317 LOSS` on4032, has loss and doubtful original
direction. **There is no eligible complete M317 field for this exact-context
test.** It receives no negative semantic inference. M316 has an H-like interior,
but no exact standalone representative H was authenticated. A secondary feature
description maps “large H” to M199; the primary representative M199 is a crowned
gate, so that description cannot supply the needed exact component bridge.
The complete variant inventory was not searched, and absence there is not claimed.
M318 was left undecomposed.

The [shape ledger](../data/processed/arch_component_review.json) records these
limits and source hashes. No visual variant was merged, no code rotated into
another, and no part was assigned a word or sound.

## Fixed screen and complete controls

The [protocol](../data/processed/composite_expansion_protocol.json) was saved
before this screen's counts. It compares complete, undoubted secondary M77
strings using an identical entire prefix and suffix around one token versus an
adjacent pair. Both component orders are distinct. At least one surrounding
token and a different-reference witness are required. Duplicate strings receive
one context/replacement instance; overlapping frames are still dependent.
All source object types and directions remain eligible and their metadata is
preserved. Strict-candidate filtering is a sensitivity analysis.

| Corpus | Records | Distinct strings | Replacement instances | Target signs with matches | Instances with at least two context tokens |
|---|---:|---:|---:|---:|---:|
| Complete undoubted export | 2056 | 1520 | 5902 | 186 | 1639 |
| Strict-candidate subset | 1293 | 1141 | 3111 | 159 | 940 |

Of5902 instances,4263 have only one surrounding token. The number with context
lengths2,3,4,5,6 is respectively981,496,145,16,1. The strict subset has2171 at
length1 and459,352,117,11,1 at lengths2–6. Target signs with at least two context
tokens number144 and122 respectively. These are discovery counts, not independent
observations, significance results, or signs with identified meanings.

An additional descriptive split, introduced after seeing the first counts,
flags318/177 instances where the target itself remains in the replacement pair.
Those are also compatible with an optional adjacent sign, without graphic fusion.
All instances remain in the results. A separate pairwise brute-force algorithm
reproduces every instance in both corpora, without using the frame index.

## Two primary checks selected after the screen

The unique longest match retains six surrounding tokens:

```
2541: M053      M171 M059 M336 M089 M216 M254
2273: M216 M123 M171 M059 M336 M089 M216 M254
```

Both complete catalogue lines are clear, metadata100001: seal class, side0,
field-symbol code00, line0, direction1. They were checked on printed pp74/PDF85
and66/PDF77 against the numbered representative signs. Thus the variable initial
part occupies the same normalized frame in these two records. This does not
identify names, titles, words, semantic equality or a segmentation shared by
every inscription. No literal fusion of M216 and M123 into M053 is established.

The sole M318 screen match has a two-token prefix:

```
1548.0.0: M121 M342 M318
3155.0.1: M121 M342 M391 M099
3155.0.2: M397                  [separate additional line]
```

1548 was already checked on printed p54/PDF65. The3155 lines are verified on
printed p89/PDF100. First-line metadata100112 means seal class, side0, field01,
line1, direction2 (left to right on the original); abbreviated second-line23
expands to100123, line2, direction3 (solus). M397 is recovered separately from
the export's omitted line. The catalogue nevertheless prints normalized strings
right to left. 1548 has direction1 and only one line. These are selected-line
parallels, not identical complete objects or physical layouts.

A follow-up on2026-09-25 also checked the concordance on printed p699/PDF710.
It independently confirms3155's separate solusM397 line, within the M397 group
and distinct from the following M398 group.

M318's roofed multi-stroke shape is not authenticated as a combination of the
six-spoked M391 and two-stroke M099. The primary pair therefore illustrates the
gap between a valid contextual replacement and a claimed graphic decomposition.
It does not prove different meanings either. The strict subset excludes3155
because the secondary export has not preserved all its lines; this audit retains
the newly checked lines separately, without silently replacing the global corpus.

The [primary ledger](../data/processed/composite_primary_review.json) records all
five lines and their evidence. Native crops and coordinates are retained. These
checks authenticate catalogue records; artifact photographs and excavation joins
have not yet been checked for these pairs.

## Consequence for interpretation

A single frame can accommodate different names, quantities, titles or grammatical
expressions. Conversely, equal meanings can have different spellings. Exact
substitution alone does not distinguish these possibilities. The many comparison
matches show why selecting one attractive pair after inspecting the corpus is
insufficient evidence for a semantic equation. A defensible composition claim
needs an authenticated shape relation plus independent predictions beyond the
discovery frame, ideally with an external semantic anchor.

The [script](../scripts/audit_composite_expansion.py), [tests](../tests/test_composite_expansion.py),
[all results](../results/composite_expansion_audit.json), and
[separate primary lines](../data/processed/composite_primary_lines.jsonl) are saved.
All417 codes receive a profile in the main evidence index, including zeros with
no negative interpretation. Every semantic and phonetic value remains null.
