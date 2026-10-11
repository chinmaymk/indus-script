# Patronymic-chain feasibility audit

Follow-up: [prefix and suffix template results](RELATION_TEMPLATE_RESULTS.md)
now cover the endpoint placements excluded by this original internal-only test.

The available strict foreign sample cannot test the plain-human internal-separator hypothesis: none of its four strings contains M001. The domestic candidate sample supplies five complete `A M001 B` parses and no exact `A M001 B` → `B M001 C` chain. This is a narrow failed search for a literal pattern, not evidence that patronymics are absent from Indus writing. Six other delimiter codes produce ten exact chain pairs, demonstrating why even a positive chain requires external validation.

## Source and sign identity

Vidale, *The Short-Horned Bull on the Indus Seals* (2005), printed155–157/PDF10–12, proposes a relationship between western inscriptions' human-like signs and patronymics. Printed156 suggests future searches for names repeated between generations but explicitly judges the five then-known Bahrain inscriptions too few and damaged. The paper does not supply a tested translation of those inscriptions. Its categorical opening claim that domestic inscriptions lack patronymics rests on expected frequency and position regularities, not independent identification of domestic names or kinship terms.

I visually inspected [Fig5, printed155](../results/primary_pages/hybrid-pat-vidale-10.png), [printed156](../results/primary_pages/hybrid-pat-vidale-11.png), [M77 sign list printed32](../results/primary_pages/hybrid-pat-m77-43.png), and [M77 western texts printed160](../results/primary_pages/hybrid-pat-m77-171.png). Fig5's plain human shape corresponds to M001. M77 separately numbers numerous modified human-like forms; they are not automatically synonyms. Vidale supplies no exhaustive variant-to-M77 code list. The exact catalogue identity and segmentation of his “twins” remain **unresolved** here; neither M016 nor two adjacent M001 tokens is silently substituted for it. This audit therefore tests plain M001 only, with all other individual codes used as descriptive controls. It does not replicate the paper's aggregate “man and variants” frequency claim. Fig5's caption says absolute frequency while the discussion uses proportions; raw denominators are not reconstructed from its perspective bars.

## Computation and coverage

[`scripts/audit_patronymic_chains.py`](../scripts/audit_patronymic_chains.py) reuses the existing foreign-comparison eligibility criteria: seal object-code1; one exported document; direction1 or2; at least two slots; no unknown span or doubtful token. Candidate arrays retain their existing normalized order, including direction2. Whole identical strings are collapsed and their references preserved. The domestic site ranges are those already authenticated in the [foreign selection review](M77_FOREIGN_SELECTION.md).

The catalogue selection consists of 17 objects and 18 printed lines; the secondary candidate export contains 17 object records and does not recover both lines of9845. This is not an authenticated complete 18-line computational corpus. Four named-site and three probable-provenance records pass the filters; they remain separate. Twelve named-site objects do not become twelve eligible complete strings. None of the seven eligible strings contains M001. M001 is visible in the printed damaged9833 and9845 rows and as two adjacent glyphs in probable9902; losses/doubt prevent treating these as intact full-name pairs.

The domestic selection is **1,175 records, 1,066 distinct candidate strings**. These records are secondary transcriptions with selected primary checks, not a fully reread archaeological corpus. M001 occurs in44 records/43 unique strings:37 unique strings place it only finally, five place a single M001 internally, and one contains repeated M001. No included unique string has a lone initial M001. Those positions describe this filtered export, not all Indus inscriptions.

The narrowly specified parser requires exactly one occurrence of delimiter D and two nonempty, **entire** flanks. It adds no word divisions inside those flanks. A chain requires the right flank of one full string to equal the complete left flank of a different full string. Empty flanks, repeated delimiters, approximate matches, sign-family substitutions and concatenations across objects are excluded. A final/initial marker cannot be made internal by reversing the string. Prefix constructions such as `D A B`, suffix constructions, unmarked relationships, phonetic spelling variation and multi-sign relationship terms fall outside this test.

## Exact main observations

| M77 reference | A | D | B |
|---|---|---|---|
|4164|M102 M059 M342|M001|M176|
|2404|M124 M409 M096 M342|M001|M176|
|2538|M162|M001|M162 M048 M342|
|2445|M391|M001|M134 M086 M415|
|1553|M397|M001|M267 M099 M067 M342 M112 M194 M342|

These five candidate pairs produce **zero exact chains**. The M162 prefix within2538's right flank is not a complete matching bundle and cannot license a match to its left flank. The common M176 right flank in4164/2404 is a repeated positioned bundle; there is no independently identified person, patronym, father or genealogical relationship. No semantic or phonetic value is assigned.

## Positive controls and what they do not establish

The same parser scanned all417 individual M codes.229 have at least one eligible internal split; six have distinct-string chains. This is an exploratory control scan, not a set of independent hypothesis tests or a corrected significance result. Full tokens and reference lists are saved in [`results/patronymic_chain_audit.json`](../results/patronymic_chain_audit.json).

| Delimiter | Eligible split strings | Chain pairs | Exact reference pairs |
|---|---:|---:|---|
|M017|27|1|1038→2105|
|M028|19|1|1015→1060|
|M098|39|2|3044→1439;4118→2369|
|M099|331|2|7095→2281;7111→5080|
|M180|21|1|2495→2468|
|M336|82|3|3105→1056;3105→1310;7065→2440|

For example,1038 is `M244 M017 M336` and2105 is `M336 M017 M402`. This forms the exact abstract pattern with M017 in the separator slot. It supplies no proof that M244/M336/M402 are people or that M017 means descent. The six positives also differ greatly in occurrence frequency and split opportunities; comparing raw counts directly would confound those differences. The1038→2105 pair was subsequently authenticated against the primary catalogue drawings, as recorded below; the other matched domestic strings remain candidate readings pending targeted primary verification. These exploratory positives must not be turned into candidate sign meanings merely because they match the requested pattern.

## A null model that fails mathematically

Represent each parsed inscription as a directed edge A→B. Let L(x) count edges with left endpoint x and R(x) count edges with right endpoint x. The number of ordered length-two walks, allowing an edge to pair with itself, is exactly

`T = sum_x R(x) L(x)`.

Randomly re-pairing the same left and right endpoints preserves both marginals, so **T is invariant**. Such an endpoint-permutation “null” cannot establish that observed chains exceed chance: the requested count was conditioned on in advance. If self-edge pairings are excluded, the statistic becomes `T − number_of_self_loop_edges`; changes can then reflect only how many A→A inscriptions the rewiring produces. They do not establish genealogy. The unit test includes a three-edge cycle and a rewired three-self-loop configuration: both have T=3, but their distinct-edge chain counts are3 and0. The difference is entirely the excluded self loops.

A more informative future control must introduce information not fixed by these marginals. One option is to authenticate archaeological horizons and independent person identifications, then assess whether B consistently occurs in an older/younger role across dated, independently made objects. A conditional chronology permutation would preserve texts, sites and date-resolution groups but shuffle independently assigned temporal ranks; its exchangeability assumptions would have to be defended, and long-lived seals make manufacture versus deposition dates non-interchangeable. Another is a preregistered held-out inscription test of a fixed parser and reading, compared against non-kinship label formulae. Neither control is executable with the present foreign strings because no authenticated name-to-person or sufficient chronological linkage has been established. Randomizing token order could test a compositional repetition pattern, but rejecting it still would not identify family relationships.

## Reproduction and research record

Run `python3 scripts/audit_patronymic_chains.py`. It fingerprints its input corpus, selection code/ledger, source PDFs and four visually reviewed page renders. Run `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_patronymic_chains.py` for the three boundary/marginal tests. All three passed in this audit.

Work used already downloaded PDFs; no new external source was downloaded. The local extraction contains NUL characters, so a temporary in-memory sanitized string was used for textual locating; the persisted source extraction was not altered. An initial file glob for a pre-existing page43 render matched nothing; the exact primary pages were then rendered from the source PDF and inspected. Render outputs for Vidale9/12 were generated but not used as visually authenticated evidence in this report. No corpus record, sign meaning, phonetic assignment, source provenance or decipherment status was changed.

## Addendum: one positive chain survives primary catalogue review

The full rows for1038 ([printed40/PDF51](../results/primary_pages/hybrid-pat-pair-51.png)) and2105 ([printed61/PDF72](../results/primary_pages/hybrid-pat-pair-72.png)) confirm the exported sequences without discrepancy. Both print metadata `100101`, with seal object-code1, only-side/only-line codes0, and direction1. Neither row carries a doubtful-sign asterisk, lost-span hatching or a continuation line. The normalized reading sequence is right to left on the page. The relevant glyphs were compared against labelled M017 on printed32/PDF43, M244 on printed34/PDF45, and M336/M402 on printed35/PDF46. In particular, M336 has an inner vertical drop-like stroke and is not replaced with plain U-shaped M328.

The retained row details are [1038](../results/primary_pages/hybrid-pat-pair-1038-detail.png) and [2105](../results/primary_pages/hybrid-pat-pair-2105-detail.png). Thus `A D B` → `B D C`, with A=M244, D=M017, B=M336 and C=M402, is supported by the two printed catalogue rows. It is not merely an export-generated match. This authenticates an abstract symbol pattern, not a genealogy, the interpretation of any sign, or the catalogue's fidelity to original objects. No independent person identity or chronological relation was established.

[`data/processed/patronymic_primary_pair_review.json`](../data/processed/patronymic_primary_pair_review.json) records the row metadata, glyph comparisons, nine source/image fingerprints, rendering command and exact crop coordinates. The crops use the original rendered pixels without rotation, resampling or contrast alteration. An attempted view of page46 while Poppler was still writing yielded an invalid-image error; after waiting for process completion the final image was successfully inspected. No new source download or corpus rewrite was required, and the chain-count script was not changed.
