# Independent review of terminal-marker relation searches

The proposed extension is a useful descriptive test of repeated bundles around a marker. Allowing every internal boundary in a marker-free body increases coverage, but also changes the question: terminal cases test whether two strings have a proper suffix–prefix overlap. Their positive matches cannot independently identify names, word boundaries, kinship, or the marker's meaning. A final position for M001 makes this a reasonable extension of the earlier internal-only search; it does not establish that a final marker expresses a relationship.

This review uses the existing [patronymic feasibility audit](PATRONYMIC_TEST_DESIGN.md), its [implementation](../scripts/audit_patronymic_chains.py), and their already archived source context. It does not download sources, rerun the corpus, authenticate additional inscriptions, or assign sign values. The 37 final and five internal M001 strings reported there are position counts in the filtered candidate corpus. The number of eligible terminal bodies must be counted separately: a string with fewer than two body signs offers no two-nonempty-bundle split. The present review is exploratory method checking, not a preregistration.

## Exact scope and counting units

Keep exactly one occurrence of a specified marker D in a complete normalized candidate string. Retain its original template and split only as follows:

| Template | Eligible form | Permitted boundary |
|---|---|---|
| Internal | A D B | The marker fixes both entire flanks |
| Prefix | D A B | Every cut of the marker-free body into two nonempty complete bundles |
| Suffix | A B D | Every cut of the marker-free body into two nonempty complete bundles |

The boundary choices do not permit dropping a sign, crossing inscriptions, matching only part of an already chosen bundle, or introducing another marker. Repeated markers, including a second D inside a proposed name, are excluded by the specified model. A real language could violate these restrictions; rejection is therefore limited to this literal model.

For each marker/template, record separately: complete marker-bearing strings; eligible complete strings; candidate parses; ordered pairs of distinct complete strings with at least one matching parse; and the individual matching parse pairs, including both cut positions and the shared bundle. Retain all reference lists after whole-string deduplication. Two object references with the same complete string are not two distinct-string witnesses, and even different strings are not automatically independent people or archaeological events.

Count a witness pair once even if several boundaries make it match. Require the same marker and template for both strings. Exclude pairs derived from the same complete string, not merely the same parsed edge. The internal-only implementation's `i != j` rule works because there is at most one edge per string; copying it unchanged to terminal multicut edges would admit spurious self-witnesses.

## What a terminal match mathematically means

Let marker-free bodies be u and v, with lengths n and m. An ordered terminal witness u→v exists precisely when, for some integer

`1 <= k <= min(n - 1, m - 1)`,

the last k signs of u equal the first k signs of v. Proof: if u=A B and v=B C with A and C nonempty, k=length(B) obeys the bounds and gives the overlap. Conversely any overlap satisfying those bounds supplies the nonempty complements A and C and hence a permitted parse. The marker's placement adds no internal boundary information.

For example, bodies `a a a` and `a a a a` match at both k=1 and k=2 in each ordered direction. There are two distinct ordered string pairs and four matching parse pairs. Reporting four independent chain witnesses would inflate the evidence. A lone body `a a a` also has the edges a→aa and aa→a; these form parsed-edge matches with each other but supply **zero** distinct-string witness pairs.

The minimum body length of two implies an inscription length of at least three signs, including D. At body length two the sole cut is forced. Longer bodies offer n−1 candidate boundaries and more chances to match. This difference is a model opportunity count, not stronger evidence for a particular interpretation.

## Reversal symmetry prevents directional inference

Write rev(X) for a bundle with its sign order reversed. Reversing every string maps

`A D B, B D C` to `rev(B) D rev(A), rev(C) D rev(B)`.

The chain survives with the inscription-pair order reversed. A prefix chain `D A B, D B C` becomes the suffix chain `rev(C) rev(B) D, rev(B) rev(A) D`, again after reversing the pair order. Suffix chains correspondingly become prefix chains. This is a bijection on permitted parses and on distinct ordered witness pairs, so aggregate chain counts are invariant under global reversal when prefix and suffix template labels are exchanged. Individual bundles and directed pairs change; the totals do not.

Consequently a larger suffix count than prefix count in the established normalized orientation describes marker position, not independently inferred reading direction or descent direction. An implementation reversal check is valuable, but its success is an algebraic property, not new archaeological evidence. Keep the corpus's existing direction normalization; do not choose per-inscription reversals to maximize matches.

## Pairwise matches need not admit one consistent segmentation

Take three suffix-marker strings, with a, b, c, x and y distinct signs:

`x a b D` ; `a b c D` ; `b c y D`.

The first→middle witness uses x|ab and ab|c. The middle→last witness uses a|bc and bc|y. Both pairwise tests succeed, but the middle string cannot have both boundaries at once. No single two-bundle parsing of all three strings realizes both relations. A displayed network that combines such matches must retain boundary alternatives; otherwise it can manufacture a multi-generation chain that no consistent interpretation supports.

The pairwise exploratory search may deliberately avoid selecting a global segmentation. Its output must then be described as existential local matches. A subsequent fixed-name or pedigree theory would require one coherent set of boundaries, or an independently justified reason for a string's contextual ambiguity, and independent evidence that the bundles denote individuals.

## A positive count has a simple non-kinship countermodel

Let an alphabet contain q category signs and take every two-sign body `a b`, followed by the same final approval marker D. Interpret a and b as any two classification fields; no name or family relation is present. Every triple a,b,c supplies a chain `a b D`→`b c D`. There are q³ ordered parsed matches, and exactly q forbidden identical-string matches, because equality of `a b` and `b c` requires a=b=c. Thus the distinct-string count is

`q^3 - q`.

With two category signs this already gives six positive witness pairs, all with forced boundaries, in a system that is not genealogical. The point is logical underdetermination, not a claim that the Indus corpus follows this artificial model. Relabelling abstract bundles with people or commodities also leaves all exact string statistics unchanged. A match alone cannot select between those interpretations.

## Null models and conclusions

For the multiset of candidate parse edges, define L(x) and R(x) as left and right endpoint counts. The total ordered parse matches, including all self-string cases, remains

`T = sum_x R(x) L(x)`.

If L_s(x) and R_s(x) are the counts contributed by complete string s, the number of parsed matches between different strings is exactly

`T_distinct_strings_as_parses = T - sum_s sum_x R_s(x) L_s(x)`.

This differs from the earlier one-edge-per-string correction, which only subtracts self-loop edges. It still counts multiple matches for a given ordered string pair. The existential witness statistic is instead a sum of indicators over different s,t that at least one compatible edge match exists.

Re-pairing endpoints with fixed marginals leaves T unchanged. It can alter the within-string correction or existential deduplication, but may also destroy the requirement that all alternate edges are cuts of the same observed complete string. Such a randomization does not become a valid kinship null merely because a modified statistic changes. A defensible null must specify its sampling unit, preserved constraints, exchangeability assumptions, and the non-kinship mechanism it represents. None is supplied by this descriptive extension.

Scanning 417 codes across three templates involves unequal marker frequencies, text lengths, positions, numbers of cuts, and recurring short bundles. These are not 1,251 independent experiments, and raw maxima or ranks do not identify relationship markers. Dividing by opportunities can describe rates but does not remove dependence or create a probability of meaning. A positive M001 result would show compatibility with a flexible repeated-bundle formula; a zero would reject only this exact-string, single-marker, two-bundle realization in the selected sample. Neither result establishes or rules out patronymics generally.

Useful next evidence would be primary authentication of reported witnesses, an independently supported boundary/reading scheme tested on held-out inscriptions, or independently identified and dated people. Chronology would also require attention to seal manufacture, use and deposition, which need not coincide. Graph density or token-order randomization can concern textual structure; even a valid structure result does not establish genealogy.

## Boundary checks worth retaining

1. Zero or multiple occurrences of D, an empty body, and a one-sign terminal body yield no edges. A two-sign body yields exactly one edge. A marker at the opposite end is assigned only to its actual template.
2. Two identical strings with different reference IDs collapse to one witness unit. One string with different cuts cannot witness a chain with itself. The `aaa` example above catches the failure of parsed-edge identity checks.
3. The `aaa`/`aaaa` pair yields two ordered witness pairs and four parse matches. Output preserves k=1 and k=2 rather than arbitrarily choosing a boundary.
4. A marker/template mismatch yields no witness, even if the bodies overlap. Exact full-bundle matching rejects a shared prefix that is shorter than the chosen entire right bundle.
5. Reversing the complete input swaps prefix/suffix totals and reverses matched pair order; internal totals remain equal. Check the mapped bundles too, rather than only totals.
6. The `xab`/`abc`/`bcy` construction yields two local pairwise witnesses but has no single consistent middle boundary supporting both. Do not silently present it as a fixed three-person lineage.
7. On tiny exhaustive alphabets, compare the optimized parser against direct split-pair enumeration, verify the overlap criterion, and verify both marginal formulas. For all two-sign bodies over q=2, expect six distinct-string witnesses.

These checks validate the stated combinatorial search. They do not validate a proposed ancient reading. No sign meaning, phonetic value, primary transcription, or central research conclusion is changed by this review.

## Implementation and saved-result review

I inspected [`audit_relation_templates.py`](../scripts/audit_relation_templates.py) and the initial four checks in [`test_relation_templates.py`](../tests/test_relation_templates.py). In the invoked workflow, parsing is separated by marker/template, the hash join compares entire bundles, same-complete-string alternatives are excluded, and the reported ordered-pair set collapses multiple matching boundaries. No implementation defect was found in those reviewed operations. `chain_witnesses` receives one marker/template's parses at a time; its standalone interface should continue to be used that way because parse objects themselves do not carry a marker/template label.

Direct inspection of the saved [`relation_template_audit.json`](../results/relation_template_audit.json) confirms 1,175 eligible candidate records and 1,066 unique strings. This review did not independently rerun that corpus computation.

| M001 template | Eligible strings | Candidate parses | Distinct ordered witness pairs |
|---|---:|---:|---:|
| Prefix | 0 | 0 | 0 |
| Internal | 5 | 5 | 0 |
| Suffix | 36 | 131 | 0 |

The final-position inventory's remaining string has only one body sign and is ineligible for the two-bundle terminal test. Thus the extension tests the substantial final-position population rather than mistaking the five internal examples for all plausible placements. Its negative result still does not refute kinship: related persons may not co-occur in the selected sample, names may not have invariant exact spellings, or a relationship could be expressed outside the three specified templates.

Across all 417 individual codes, the saved totals are 130 parsed/129 distinct-pair prefix witnesses through 16 markers, ten/ten internal witnesses through six markers, and 1,002/1,002 suffix witnesses through 13 markers. These are template-specific sums over marker hypotheses, not counts of independent semantic confirmations. The positive controls show that this broader pattern occurs elsewhere in the candidate corpus; they do not make a positive control marker a translated relation word.
