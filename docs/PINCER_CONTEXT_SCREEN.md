# Pincer-context candidate screen

This screen finds compatible transcription contexts, not artifact identities or meanings. It was motivated by the already selected M-63 / M77 3068 comparison. The protocol was saved before this screen's counts, but the candidate alphabet and question are source exposed; this is not a blind test.

## Method and restrictions

Use the 2,914 existing strict Lipi rows and 1,293 existing strict M77 candidate rows. Select every Lipi row containing W550 or W555 (93 rows), reverse its source-file token order, and compare only equal-length M77 sequences. For the two target W codes, allow either M216 or M222. Every other aligned token must have explicit membership in a shared catalogue feature. Retain all supporting feature IDs and the full M-candidate family at every context position. There are no wildcard substitutions, sign splits, merges, alternate rotations, site filters, preservation filters, or archaeological identity joins.

Reversal is the screen's comparison convention, not independently established reading direction for every row. “Strict” names the existing parser datasets; it does not certify physical completeness or correct tokenization. The existing catalogue's target memberships remain visible: both W550 and W555 are assigned to M216 through P230. The expanded target set here is a hypothesis under examination, not an overwrite of that catalogue.

## Results

- 36 of 93 selected rows have at least one compatible candidate; 26 have one candidate row and 10 have multiple candidate rows.
- 57 have no candidate. In 23 of those, at least one non-target W sign has no M candidate in the feature map; the other 34 fail the full context/length constraints. Neither kind establishes a different sign value.
- There are 55 candidate pairs, with 21 pairs using at least one context sign whose feature membership admits more than one M sign.
- Seven Lipi rows permit both M216 and M222 at a target code across their compatible candidate rows.
- The known M-63 row 2591.1 survives as a single candidate, M77 3068: reversed `W550 W060 W555 W526` aligns with `M216 M123 M222 M254`. W550→M216 and W555→M222 is the compatible assignment in that sequence. Primary authentication is a separate task; this result does not supply it.

| Target code | Candidate M code | Candidate pairs containing that assignment |
|---|---|---:|
| W550 | M216 | 27 |
| W550 | M222 | 6 |
| W555 | M216 | 6 |
| W555 | M222 | 17 |

These are pair incidences, not artifact frequencies or independent observations. A pair can contribute to both W-code tables (M-63 does), and multiple M77 rows can contain the same sequence. They cannot be pooled into a common-object denominator.

A useful counterexample to automatic global mapping is M-897: its context admits three M222 candidates, despite its target being W550. This can reflect a transcription or catalogue error, broad context equivalence, shared formula, or distinct artifacts with related texts. It does not establish W550=M222. Likewise, the short sequence of M-1351 permits M216 and M222 here even though a separately authenticated artifact may resolve it. Context matching alone cannot perform that resolution.

## Complete list of selected rows with candidates

The CISI labels below are inherited Lipi labels. The last column lists compatible M77 source-reference strings; an entry does **not** assert the labels identify the same artifact. The JSON records all 93 rows (including every unmatched row), exact sequences, candidate-pair IDs, positionwise feature support, and separate per-target mapping tables.

| Lipi row | Source CISI label | Target candidates across matches | Compatible M77 source references |
|---|---|---|---|
| 472.1 | H-2084 | W555→M216,M222 | 1269, 2142 |
| 1061.1 | H-1294 | W550→M216 | 5469 |
| 1423.1 | H-421 | W550→M216 | 4026 |
| 1449.1 | H-459 | W555→M222 | 4092 |
| 1551.1 | H-611 | W550→M216 | 4260 |
| 1984.1 | L-1 | W550→M216 | 7015 |
| 1988.1 | L-9 | W555→M216,M222 | 1269, 2142 |
| 2025.1 | L-58 | W550→M216 | 7029 |
| 2043.1 | L-89 | W555→M222 | 1158, 2545, 7090 |
| 2067.1 | L-122 | W550→M216 | 7069 |
| 2181.1 | M-1847 | W550→M216,M222 | 1269, 2142 |
| 2196.1 | M-1764 | W550→M216 | 1136 |
| 2243.1 | M-940 | W555→M222 | 2060 |
| 2253.1 | M-1800 | W550→M216,M222 | 1238, 2244, 2652, 7011 |
| 2294.1 | M-1917 | W555→M222 | 1350 |
| 2359.1 | M-1693 | W555→M222 | 2583 |
| 2437.1 | M-821 | W555→M216,M222 | 1238, 2244, 2652, 7011 |
| 2570.1 | M-42 | W550→M216 | 1096 |
| 2584.1 | M-56 | W550→M216 | 2406 |
| 2591.1 | M-63 | W550→M216; W555→M222 | 3068 |
| 2609.1 | M-82 | W550→M216 | 2451 |
| 2676.1 | M-149 | W550→M216 | 1233 |
| 2684.1 | M-158 | W550→M216 | 2198 |
| 2826.1 | M-307 | W550→M216 | 2122 |
| 2861.1 | M-365 | W550→M216 | 2273 |
| 3282.1 | M-873 | W550→M216 | 1170 |
| 3302.1 | M-897 | W550→M222 | 1158, 2545, 7090 |
| 3329.1 | M-934 | W555→M222 | 1158, 2545, 7090 |
| 3334.1 | M-939 | W550→M216,M222 | 1238, 2244, 2652, 7011 |
| 3358.1 | M-964 | W550→M216 | 2010 |
| 3455.1 | M-1081 | W555→M222 | 2129 |
| 3604.1 | M-1299 | W550→M216 | 1456 |
| 3625.1 | M-1320 | W555→M222 | 1447 |
| 3652.1 | M-1351 | W555→M216,M222 | 1269, 2142 |
| 3670.1 | M-1371 | W550→M216 | 1559 |
| 3677.1 | M-1381 | W550→M216 | 1559 |

## Interpretation limits and next test

The feature crosswalk is incomplete and often many-to-many. A match establishes compatibility with those candidate sets, not character identity; no match can arise from a missing mapping, a different transcription boundary, a sign variant, an absent source text, or an incompatible order. The two corpora can describe the same physical objects, so this is not replication in a separate archaeological sample. Repeated inscriptions and short formulae create further multiplicity. No statistical significance or general mapping accuracy is estimated.

The strongest actionable output is a list for primary-image and catalogue-number review. M-63 / 3068 is an already selected case, so its survival tests implementation consistency rather than predictive success. M-897's mixed result is another explicit candidate for checking source drawings and object numbers before accepting a global W550/M216 and W555/M222 split. All established semantic and phonetic values remain unset.

## Reproduction

- Protocol: `data/processed/pincer_context_protocol.json` (saved before counts).
- Script: `python3 scripts/screen_pincer_contexts.py`.
- Full output and input SHA256 pins: `results/pincer_context_screen.json`.
- Focused tests: `python3 -m unittest discover -s tests -p test_pincer_context_screen.py`.

The two tests check reversal, exact token count, rejection of unsupported non-target mappings, and preservation of many-to-many feature memberships/provenance. Both pass. No files were downloaded for this screen.
