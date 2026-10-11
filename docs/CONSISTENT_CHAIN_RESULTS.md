# Consistent segmentation across three inscriptions

Of 1,483 apparent ordered three-string paths in the existing relation-template
screen, **1,152 require contradictory splits of the middle string**. Only 331
admit one consistent middle split. This is a constraint on a literal proposed
formula, not a decipherment or a probability of kinship.

The input remains 1,175 filtered domestic candidate seal records, collapsed to
1,066 complete strings. All 417 markers receive all three original placements.
No corpus transcription or sign family is changed. The
[protocol](../data/processed/consistent_chain_protocol.json) was saved before
computing these three-string results, although the earlier pair results were
already known. The length breakdown and primary-example selection below were
subsequent exploratory analyses.

| Placement | Apparent ordered triples | Consistent triples | Contradictory triples |
|---|---:|---:|---:|
| Prefix |20|1|19|
| Internal |0|0|0|
| Suffix |1,463|330|1,133|

Counts are summed over marker hypotheses and use three distinct complete strings.
They are neither independent artifacts nor independent statistical tests.
M001 still has no paths; this follows from its earlier absence of pair matches
and is not a new refutation of a kinship interpretation.

| Marker and placement | Apparent | Consistent | Contradictory |
|---|---:|---:|---:|
|M012 suffix|3|3|0|
|M162 suffix|3|0|3|
|M211 suffix|34|20|14|
|M249 prefix|18|1|17|
|M254 suffix|14|0|14|
|M267 prefix|2|0|2|
|M342 suffix|1,409|307|1,102|

All other marker/placement combinations have zero triples. Frequency and the
number of possible boundaries differ substantially; the table cannot rank
markers by semantic plausibility. M342 has 393 eligible strings and 1,395 possible
parses in the earlier screen.

## What is tested

Each inscription contributes a candidate relation between two complete contiguous
bundles. An internal marker fixes the split; a terminal marker permits every
nonempty two-part split of the body. Pairwise witnesses may use different splits
of a shared string. For three strings X,Y,Z, this test requires the **same split
of Y** to support X→Y and Y→Z. At least one compatible realization is enough to
retain the ordered triple; failed alternative realizations do not invalidate a
successful one.

For terminal bodies u,v,w, let K(u,v) be the permitted suffix–prefix overlap
lengths. A path exists before checking consistency when K(u,v) and K(v,w) are
nonempty. It has a consistent middle split exactly when some i in K(u,v) and j
in K(v,w) satisfy **i+j=length(v)**. The incoming match fixes the first part of v
to length i; the outgoing match fixes its second part to length j. Both parts
cover v precisely when their lengths sum to its length. The
[independent review](CONSISTENT_CHAIN_METHOD_REVIEW.md) supplies the full proof,
reversal argument and an independently implemented exhaustive check.

For example, `xabD → abcD → bcyD` passes both pair tests. The first forces
`ab|c` in the middle while the second forces `a|bc`. Both overlaps have length 2,
but the middle body has length 3, so no common split exists.

The code rejects duplicate input witnesses rather than counting them again.
In this particular corpus every apparent triple has one pair-witness combination,
and every retained triple has one compatible realization. This is an observed
property of this sample; the implementation and tests allow multiple alternatives.

## Surviving multi-sign example checked in the primary catalogue

Of the 331 retained triples, 304 use middle bundles of lengths 1 and 1; 26 use 1 and 2;
one uses 3 and 2. These lengths count catalogue sign codes, not phonemes, syllables
or words. Longer matching sequences were not a preregistered significance test.

The exceptional candidate matches complete normalized drawings in Mahadevan 1977:

| Reference | Proposed split in normalized reading order | Printed/PDF page |
|---|---|---|
|2463|M343 **\| M391 M099 M387** M342|72/83|
|2302|**M391 M099 M387 \| M102 M287** M342|67/78|
|4084|**M102 M287 \|** M329 M343 M067 M008 M342|100/111|

The bars are analytical boundaries; they are **not printed word dividers**.
All three rows end in M342 in normalized reading order, with original direction
digit 1. Metadata is 100301,100001 and 100101 respectively. The field-symbol codes
03,00 and01 are separate from the final direction digit. All signs, row numbers
and metadata were checked in the retained page renders; none of these rows has
a continuation, loss marker or doubtful-sign marker. The sign identities were
compared with labelled primary signlist pages32,34 and35.

The [review ledger](../data/processed/consistent_chain_primary_review.json) pins
the full pages, row crops and signlist images. This establishes one genuine
abstract chain in the printed corpus. It does not establish artifact photographs,
ancient word boundaries, personal identities, contemporaneity or descent.

## Why consistency still does not identify kinship

Take q category labels and every two-field string `abD`. This system can describe
ordinary classifications with an approval marker D. Its number of ordered
three-distinct-string paths is **q⁴−3q²+2q**, all with forced consistent splits.
Each path corresponds to four category labels. Excluding equality of any two
of its three strings removes three sets of size q²; their intersections all
have size q, yielding the formula by inclusion–exclusion. For q=2 there are 8
positive paths with no genealogy in the construction.

Global reversal reverses the path order and swaps prefix with suffix while
preserving all these counts. The test cannot infer reading or descent direction.
Moreover, separate retained triples may demand incompatible splits when combined
into one larger network. Three-string feasibility is not a globally consistent
parsing of the corpus. A family interpretation still needs independently grounded
names, grammar and chronology. An absence of matches does not rule it out when
related people or their spellings may be absent from the selected corpus.

## Reproduction

Run `python3 scripts/audit_consistent_chains.py` after the relation-template audit,
or `python3 scripts/run_all.py`. The result preserves all 1,251 marker/template
rows, rejected triples with their conflicting middle parses, every compatible
realization and source fingerprints in
[consistent_chain_audit.json](../results/consistent_chain_audit.json).

Eight focused tests cover ambiguity, rejection of duplicate witnesses, distinct
strings, fixed internal boundaries, reversal and the non-kinship countermodel.
An independent oracle checks every ordered distinct triple among the 28 binary
bodies of lengths 2–4: 7,450 apparent triples, 3,126 consistent, 4,324 rejected for
each terminal placement. Those are synthetic validation counts, not Indus counts.
No downloads or semantic/phonetic assignments were added by this phase.
