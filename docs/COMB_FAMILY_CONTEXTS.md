# Comb-family contexts: W525, W526, W527

The strict corpus supplies **no exact whole-string counterparts differing only by W525↔W526 or W525↔W527 at one position**. Its W525 contexts therefore do not add direct interchangeability evidence under this deliberately narrow test. This does not refute the local primary catalogue correspondences, and it does not establish that the signs have different meanings.

The protocol was saved before these counts. The question and sign selection are source exposed, motivated by local W525/M254 anchors and earlier W526/W527/M254 examples. This is an exploratory corpus description, not a held-out test.

## Counts and position

| Code | Rows / occurrences | Distinct whole strings | All-row position categories | Distinct-string position categories |
|---|---:|---:|---|---|
| W525 | 10 / 10 | 6 | final 1, medial 9 | final 1, medial 5 |
| W526 | 9 / 9 | 7 | final 9 | final 7 |
| W527 | 45 / 45 | 43 | final 40, initial 1, medial 4 | final 38, initial 1, medial 4 |

Positions use the reversed source-file sequence as the right-to-left reading convention. Direction has not been independently established for every row. “Final” describes the edge of the retained row, not a certified original text boundary. There are no singleton examples, mixed-form rows, or rows repeating the same target form. Across the three codes there are 64 selected rows and 56 distinct strings.

The JSON also gives exact zero-based reading indices, offsets from the reading end, and rational normalized positions. For W525, eight rows have one token after it in this convention, one has three tokens after it, and one is final. After string deduplication those counts are four, one and one.

## Source metadata distributions

Each count below counts a source row once for that sign, preserving the literal metadata labels.

| Code | Site | Object type | Source preservation |
|---|---|---|---|
| W525 | Harappa 9; Mohenjo-daro 1 | TAB:B 9; TAB:I 1 | chipped 1; complete 9 |
| W526 | Chanhu-daro 1; Harappa 4; Lothal 1; Mohenjo-daro 2; Nausharo 1 | SEAL:S 5; TAB:B 3; TAB:I 1 | chipped 1; complete 7; slightly chipped 1 |
| W527 | Bala-kot 1; Harappa 9; Lothal 5; Mohenjo-daro 30 | MISC 1; POT:T:s 2; ROD 1; SEAL:R 7; SEAL:S 31; TAB:B 2; TAB:I 1 | chipped 1; complete 37; fragment 4; slightly chipped 3 |

W525's ten records are all tablet-labelled, nine from Harappa. W526 and W527 are mostly seal-labelled and occupy the final retained position much more often. The sampled contexts differ, but object type, site, formula, preservation, row segmentation and transcription choices are confounded. No inference about function, grammar, chronology or pronunciation follows from these marginals.

Positional graphic variation remains possible: the source codes might distinguish shapes used in different positions without distinguishing semantic values. The observed distributions neither establish that explanation nor rule it out. The global marginal contrast must not be described as a functional distinction.

The deduplicated JSON preserves each string's complete set of site/type/preservation labels instead of selecting an arbitrary representative. For example, one W526 string occurs under both Harappa and Lothal and under both SEAL:S and TAB:I. A metadata set is counted once as a set; these are not independent archaeological observations. Source `complete` labels are retained without certifying physical completeness; earlier primary review found corner damage on L-9 despite its label.

H-1123 row 313.1 is retained exactly as source-labelled, including preservation `complete`. Its excavation/plate identity conflict is documented in `docs/W525_PRIMARY_REVIEW.md`; the corpus label is not an authenticated object join.

**H-1123 is W525's sole final-position row.** The separately retained retrospective omission leaves nine W525 rows and five distinct strings, all medial under reversal. Their source metadata remains eight Harappa and one Mohenjo-daro, eight TAB:B and one TAB:I, eight `complete` and one `chipped`. This sensitivity strengthens the descriptive concentration in medial positions; it still cannot distinguish positional graphic variation from a difference in function or meaning. The main ten-row analysis remains unchanged.

## Shared site × type × length coverage

This descriptive extension was added to the protocol after observing the initial marginal distributions and zero-counterpart result, before computing these coverage counts. There are 35 observed literal site × type × token-length strata, but only **one** contains W525 and either W526 or W527.

| Analysis | Shared / observed strata | W525 rows in shared strata / all W525 rows | W526/W527 rows in shared strata / all pooled rows | Distinct strings in shared strata, W525 : pooled |
|---|---:|---:|---:|---:|
| Source-labelled main analysis | 1 / 35 | 2 / 10 | 1 / 54 | 2 : 1 |
| Retrospective omission of H-1123 | 1 / 35 | 1 / 9 | 1 / 54 | 1 : 1 |

The shared stratum is **Harappa × TAB:B × length 3**:

| Source row | Source-file sequence | Target position under reversal | Source preservation |
|---|---|---|---|
| 313.1 H-1123 | `W525 W550 W220` | final | complete |
| 624.2 H-1817 | `W400 W525 W554` | medial | complete |
| 1729.1 H-843 | `W400 W527 W195` | medial | complete |

It contains no W526 row. Excluding the identity-conflicted H-1123 leaves one medial W525 and one medial W527 row; they also differ at W554/W195, so they are not exact substitution counterparts. Thus the surviving shared stratum supplies almost no comparable coverage and no clean one-sign contrast. Its presence shows that W527 can occur medially on a tablet, but it cannot separate positional variation from different formulas or meanings. The exclusion is retrospective and does not replace the original analysis. Full member records for all 35 strata are preserved in the JSON. No inferential p-value is calculated.

## W525 contexts, with repetitions exposed

These are the six complete token strings in **source-file order**, not the reversed order used for the positional summaries. CISI labels are retained from the source and are not newly authenticated artifact identifications.

| Source-file sequence | Rows and source labels |
|---|---|
| `W400 W525 W550` | 3684.1 M-1390 |
| `W400 W525 W550 W033 W705 W220` | 653.1 H-1813 |
| `W400 W525 W550 W033 W705 W240` | 512.2 H-1816; 635.1 H-1814; 867.1 H-1812; 916.1 H-1811; 1666.1 H-774 |
| `W400 W525 W554` | 624.2 H-1817 |
| `W525 W550 W220` | 313.1 H-1123 |
| `W700 W034 W400 W525 W550` | 532.2 H-2069 |

The five copies of the six-token W525 string are one observed string context. They do not provide five independent demonstrations of interchangeability.

## Exact-counterpart and co-occurrence tests

The script indexes all 2,914 strict rows by entire literal sequence. For each W525 occurrence it substitutes W526 or W527 at exactly that position and requires every other token and the token count to remain identical. It finds zero distinct sequence pairs for either substitution. Multiple substitutions, partial overlaps, removal of W400, token expansion and broad feature-family equivalence are excluded by the saved protocol. No row contains two different members of this three-code set, and no row repeats one member.

A null exact-counterpart result can reflect limited coverage, missing records, site/type specialization, tokenization, damage or a real sign distinction. It cannot establish which explanation applies. A positive result would likewise show compatible contexts rather than prove allography. The local primary correspondences remain a separate kind of evidence; this screen cannot extend them into universal W525=W526=W527 equivalence.

## Reproduction and retained evidence

- Protocol: `data/processed/comb_family_context_protocol.json`.
- Run: `python3 scripts/audit_comb_family_contexts.py`.
- Output, all 64 source rows, all 56 string groups, complete distributions and input SHA256 pins: `results/comb_family_contexts.json`.
- Tests: `python3 -m unittest discover -s tests -p test_comb_family_contexts.py` (two pass).
- Independent check: `python3 scripts/verify_comb_family_contexts.py`, with output
  `results/comb_family_contexts_independent.json`. It imports no audit helpers,
  scans unequal positions in every selected-versus-all row pair, computes edge
  categories in file coordinates, and checks all shared-stratum member records.

Tests enforce exactly one changed position with identical remaining tokens, preservation of duplicate rows inside a string group, reversed-order position indexing and singleton handling. No downloads were needed. No global allography, semantic value or phonetic value is promoted.
