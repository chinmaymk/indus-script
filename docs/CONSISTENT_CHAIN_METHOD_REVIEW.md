# Consistent three-string relation chains: independent method review

The proposed test measures how often two individually possible bundle matches can use the same boundary in their shared inscription. This removes one specific source of inflated chains in the [terminal-marker search](TERMINAL_RELATION_METHOD_REVIEW.md). It does not identify names, kinship, language, or sign meanings. A successful three-string chain remains an existential local interpretation: different successful triples may require conflicting parses of the same inscription.

This review is an exploratory mathematical audit using the existing parser and corpus protocol. It introduces no downloaded data and no semantic assignments.

## Definitions and proof

Fix one marker and one template. Collapse identical complete strings before parsing, retain their reference lists, and enumerate the existing two-nonempty-bundle parses. Exactly one occurrence of the marker is permitted. Let P(s) be the set of distinct parses of complete string s, each parse p having bundles L(p), R(p).

For three pairwise distinct strings a,b,c, define:

- A naive triple exists if some p∈P(a), q∈P(b) satisfy R(p)=L(q), and some q′∈P(b), r∈P(c) satisfy R(q′)=L(r). The independently chosen q and q′ need not agree.
- A consistent realization is a triple of parses (p,q,r) satisfying both R(p)=L(q) and R(q)=L(r). Its middle parse is shared by both comparisons.
- A consistent string triple has at least one consistent realization. Count the ordered string triple once regardless of how many realizations exist.
- A rejected naive triple has no consistent realization at all. One incompatible pair of witnesses does not make a triple rejected if another compatible realization exists.

Every consistent triple is naive, by taking q′=q. The converse fails because the two existential choices of a middle boundary are independent. Consequently the compatible and rejected sets partition the naive triple set, and their counts must add exactly. Parse-realization counts are separate and can exceed consistent string-triple counts.

For internal markers there is at most one parse of each eligible string. Therefore q=q′ whenever both exist: every naive triple must be consistent. A rejected internal triple indicates a defect in this protocol's implementation or its inputs.

All three complete strings must differ, including a≠c. Otherwise a two-string cycle can be reported as three observations. Deduplicating by reference ID or parsed-edge identity is insufficient. Parse identity is (complete string, left bundle, right bundle); multiple records or duplicate parse objects must not multiply its realization count. Within a fixed marker/template, the actual parser produces one parse per cut, so duplicate parses should not arise; a reusable standalone routine should nevertheless either deduplicate or state and validate this precondition.

## Independent terminal-overlap oracle

For prefix or suffix templates, remove the single terminal marker and write the bodies as u,v,w. Define

`K(u,v) = { k : 1 ≤ k ≤ min(|u|−1, |v|−1), suffix_k(u) = prefix_k(v) }`.

The proper-overlap criterion in the preceding review proves that a pair match is equivalent to nonempty K. A naive triple therefore requires both K(u,v) and K(v,w) to be nonempty.

A consistent triple requires more: there must be i∈K(u,v) and j∈K(v,w) such that

`i + j = |v|`.

Proof: the first overlap is the whole left bundle of v, of length i; the second overlap is the whole right bundle of v, of length j. A single complete two-bundle parse partitions v, so their lengths sum to |v|. Conversely, complementary overlap lengths give exactly the three permitted cuts `|u|−i`, `i`, and `j` in u,v,w and satisfy both bundle equalities. Nonempty complements follow from K's proper-overlap bounds.

Each complementary pair gives exactly one parse realization. Hence the realization count for the ordered triple is

`#{ i ∈ K(u,v) : |v|−i ∈ K(v,w) }`.

This provides an independent oracle without invoking `parse_strings`, `chain_witnesses`, or any production parse index. For all binary bodies of lengths two through four, enumerate ordered triples of distinct bodies, calculate K using direct tuple slicing, and compare the complete naive, consistent, rejected, and realization sets or counts against the production implementation. Repeat with the marker at the opposite end and explicitly compare the reversal mapping. This tests more than matching a few aggregate totals.

## Counterexamples and boundary cases

Take distinct signs x,a,b,c,y and suffix marker D:

`x a b D → a b c D → b c y D`.

The first edge requires `x|ab → ab|c`; the second requires `a|bc → bc|y`. Their overlap lengths are 2 and 2, while the middle body has length 3. Both naive links exist, but no consistent realization does. This is a complete counterexample, not just a demonstration that one arbitrary parse choice fails.

By contrast, the distinct strings `a a a D`, `a a a a D`, `a a a a a D` in that order have two consistent realizations: middle cuts after one or two signs. Count one consistent string triple and two realizations. Repeated tokens do not erase the distinction between cut positions or authorize choosing both simultaneously in a fixed-reading theory.

Retain cases with fewer than three unique complete strings, zero or repeated markers, a one-sign terminal body, duplicate references, and a→b→a cycles. None supplies an eligible three-distinct-string triple. A valid triple plus an additional incompatible pair of middle parses must remain classified as consistent, since classification is existential.

## Reversal and inference limits

Reversal maps a parse (L,R) to (rev(R),rev(L)). It maps a triple (a,b,c) to (rev(c),rev(b),rev(a)), exchanges prefix and suffix templates, and preserves the internal template. Both bundle equalities survive under this transformation. It is an involution, hence a bijection on naive triples, consistent triples, rejected triples, and consistent parse realizations. Counts cannot determine reading direction; comparing mapped witnesses is stronger validation than comparing totals alone.

Three-string consistency is necessary for the literal fixed-boundary interpretation of those three inscriptions, but it is insufficient for a coherent interpretation of the whole corpus. It also does not prefer kinship over a two-field classification scheme. For example, the forced-boundary category strings `a b D`, `b c D`, `c d D` give a consistent triple even if a,b,c,d denote administrative categories. A nonempty count is structural evidence only.

More generally, include all q² two-field strings over q category signs, each followed by D. Every quadruple (a,b,c,d) produces the forced-boundary path abD→bcD→cdD. Of q⁴ paths, exclude equality of the first two, last two, or first and last strings. Each equality event has q² members, every pairwise intersection has q members, and the triple intersection also has q. Inclusion–exclusion gives exactly **q⁴−3q²+2q** paths with three distinct strings, all consistent and none requiring kinship. Independent direct enumeration for q=1 through 5 gives 0, 8, 60, 216, and 560, agreeing with the formula. This is a logical countermodel, not a fitted explanation of the archaeological corpus.

No calibrated probability or semantic enrichment follows from scanning all 417 markers and three templates. Marker frequency, bundle repetition, body lengths, and boundary opportunities vary. Rejected triples quantify an ambiguity in the chosen model; they are not evidence that ancient users made inconsistent statements. Zero compatible triples does not refute kinship, since this selected corpus and literal exact-string model may omit actual related persons, spelling variation, or their relation formula.

## Implementation review status

I inspected [`audit_relation_templates.py`](../scripts/audit_relation_templates.py) and [`audit_consistent_chains.py`](../scripts/audit_consistent_chains.py). The composition routine groups witnesses by the complete middle string, compares both middle bundles, excludes all repeated-string triples, and retains the distinction between string-triple counts and parse-realization counts. `parse_key` need not include the sequence because the middle-string grouping has already fixed it. No defect was found for the unique upstream witness input. At the initial implementation review, a standalone call with duplicate witness objects could inflate realization counts; this was reported to the parent for an explicit uniqueness precondition or defensive deduplication. It does not affect the existing upstream generation, which emits each parse pair once.

I independently ran the proper-overlap oracle on all 28 binary bodies of lengths two through four, comparing the entire keyed triple map and both per-triple counts against the production parser and composition routine. Both prefix and suffix cases agreed: 7,450 naive ordered triples, 3,126 compatible, 4,324 rejected, 10,464 pair-witness combinations, and 3,200 compatible parse realizations. These synthetic numbers validate the combinatorial implementation, not the Indus interpretation. The counterexample target triple returned one pair-witness combination and zero realizations; the repeated-token target returned six combinations and two realizations, as predicted. This independent review did not rerun or authenticate the archaeological corpus.


## Follow-up to the duplicate-input caveat

After this independent review, the parent added explicit duplicate-witness
rejection and a regression check. Identical pair witnesses now raise ValueError
instead of inflating realization counts. Upstream corpus witnesses remain unique;
the change does not alter the observed results. The parent also checked the sole
multi-sign-on-both-sides survivor against the original printed catalogue, as
recorded separately in CONSISTENT_CHAIN_RESULTS.md. This paragraph records the
parent's follow-up; the independent review above remains scoped to its own checks.
