# What exact substitutions can and cannot establish

**The corpus contains interchangeable positions, but their occupants cannot be
automatically merged into a meaning, sound or grammatical class.** This audit
extends the earlier graphic-family analysis to every W code in the strict corpus.
It retains every counterexample and every sign without substitution evidence.

## Exhaustive coverage

The existing strict subset has 2,914 source rows, 1,848 distinct complete texts,
8,489 deduplicated tokens and 575 W codes. Replace one position with a wildcard;
two signs have a substitution connection only if all other positions match exactly.
No transliterations or proposed meanings are used. Repeated copies of the same
text do not inflate counts, and all corresponding artifact/source identifiers survive.

There are **329 shared frames**, connecting **2,318 sign pairs** through2,660
pair/frame observations. **276 codes** have at least one connection; **299** have
none. Of the connected pairs, **2,104 share only one frame**. These counts describe
this selected transcription corpus, not all surviving Indus objects.

Short contexts dominate:

| Minimum complete-text length | Shared frames | Connected pairs | Codes with a connection |
|---|---:|---:|---:|
| 2 | 329 | 2,318 | 276 |
| 3 | 251 | 617 | 210 |
| 4 | 142 | 274 | 148 |
| 5 | 64 | 87 | 90 |

The two-sign frame `W740 ?` alone has48 different replacements, creating1,128
pair connections before accounting for overlap with other frames. Such a broad
one-neighbor context is insufficient to establish that all48 signs do the same job.
Requiring longer exact frames reduces support substantially; it does not prove
that short inscriptions are uninformative or that their signs differ in meaning.

Restricting source conditions to exactly Good, Fair or Fine before deduplication
retains2,005 rows and1,378 distinct texts with527 codes. It yields214 shared frames
and946 connected pairs; requiring length≥5 leaves42 pairs. Thus substitution
evidence survives that restriction, but many connections depend on poorer-condition
records. These are source labels, not independent image-quality assessments.

## Cooccurrence constrains restrictive field models

**545 connected pairs also occur together** in at least one complete text. A further
25 individual W codes repeat within66 distinct texts. These are explicit witnesses
against a proposed rule allowing at most one member of the relevant class in the
whole inscription. They do not refute repeated fields, contextual substitution,
allography, synonymy or ordinary linguistic writing.

For example, the pair W090/W400 shares `? W740 W220` in the export:

- H-1342, source4084.1, Poor: `W090 W740 W220`.
- M-1312, source3617.1, Fair: `W400 W740 W220`.

Those replacement witnesses come from different sites and object types and remain
unverified photographically. Both codes also occur in Good-labelled H-188
(`W400 W090 W740 W100 W415`) and M-263
(`W090 W740 W400 W350 W031 W545`).

Saved CISI photographs corroborate the latter two cooccurrences at the broad
graphic level: H-188 faceA, printed210/PDF246, shows a comb-like form followed by a
person-like form; M-263 originalA and impressiona, printed65/PDF101, show both forms
with a jar-shaped form between them. The formal catalogue puts W090 viaP013 with
M001, and W400/W402 viaP098 withM176. This check does not discriminate every
comb variant or create a new W–M identity. The [primary review ledger](../data/processed/substitution_primary_review.json)
retains all locators and the weaker status of the replacement witnesses.

## Why connected groups are not equivalence classes

The observed network supplies a direct logical counterexample to transitive closure:
W151 connects toW740 in eight frames, while W740 connects toW741 in three;
no W151–W741 shared frame occurs in this subset. Longer examples are
`? W100 W220` for the first pair and `W520 W240 ? W590 W575` for the second.
The underlying records include Fair and Poor objects and remain source-level evidence.

Thus replacing a chain of observed connections by a single equivalence class adds
relationships that were never observed. Missing connections are not evidence of
impossibility: sparse sampling may explain them. The conclusion is that equivalence
requires additional evidence, not that these three signs must differ in meaning.

## Relation to all 417 supplied signs

The consolidated evidence index now preserves candidate catalogue paths from
**300 M entries** to observed W codes, including W codes with no connections.
Of those,181 have at least one candidate W code with a substitution connection;
119 link only to codes with none in this subset.
The other117 M entries still retain their primary positional evidence without
this additional corpus link. **170 observed W codes** have no M link in the source
catalogue and are listed separately. These numbers reflect different inventories;
they are not counts of deciphered signs.

Every path retains all M and W members of its P catalogue entry. No result is
silently copied as an individual identity through an ambiguous grouping. All417
semantic and phonetic values remain undetermined.

## Reasonable conclusion

The evidence favors testing short formulae with replaceable components and allows
some components to recur or combine. It does not justify a single fixed,
one-sign-per-field schema across all texts. A proposed reading must explain both
its shared frames and its cooccurrence witnesses, preserve graphic distinctions,
and account explicitly for signs whose contexts are too sparse to classify.
This constraint applies equally to linguistic and nonlinguistic interpretations.

## Reproduction

- [Enumeration script](../scripts/audit_substitution_network.py)
- [All575 sign summaries, protocol and source hashes](../results/substitution_network.json)
- [Every text and associated source record](../results/substitution_network_texts.jsonl)
- [Exact frames](../results/substitution_network_frames.jsonl)
- [Pair witnesses](../results/substitution_network_pairs.jsonl)
- [Compact pair table](../results/substitution_network_pairs.csv)

Run `python3 scripts/audit_substitution_network.py`, then
`python3 scripts/build_evidence_index.py`, or use the full offline pipeline.
Tests cover deduplication, exact-position matching, missing transitive edges,
cooccurrence, repeated signs, isolated signs and stable enumeration.
