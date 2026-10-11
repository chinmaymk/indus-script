# Reproducible methods and limitations

## Primary M77 inventory extension

The later [primary-inventory transcription](PRIMARY_INVENTORY.md) supplies direct
position counts for all 417 M signs, independently of W/P correspondence. Its table
unit is a line and it retains repeated inscriptions. Source OCR coordinates and
explicit visually checked corrections generate the table; failed row sums, column
totals, or the introduction's frequency-band checks stop downstream primary profiling.
This is a distinct analysis from the secondary sequence experiments described below.
All seven table pages were visually inspected; this was not independent double-entry
transcription. Coarse primary role thresholds are documented in the linked report.

## Input and filtering

`prepare_corpora.py` retains a secondary-export row only when its text is exactly
`+ddd-ddd-...+`, has no `000` or `999` token, is marked complete, has direction `R/L`,
is not classed `2L`/`3L`, and agrees with the numerical sign-count field when present.
All other cases receive explicit, possibly overlapping reasons in the exclusion
ledger. No fragments are joined across damage and no uncertain signs are guessed.
This filter leaves 2,914 rows and 1,848 distinct sequences; it is not EBUDS.

These rows happen to have lengths 2–13. Single-sign inscriptions are **not thereby
shown to be absent**: they are excluded by this combination of metadata requirements.
Nor do these lengths describe the longest Indus inscription in the archaeological
record. Selection on completeness, direction, and cataloguer judgments introduces bias.

The mayig subset excludes entire sides with any annotated damage/uncertainty,
unrecognized sign IDs, or more than one line. It retains 98 sides, 97 distinct texts.
This is a convenience sample concentrated on Mohenjo-daro.

No source is silently corrected. Original files, rejected rows, and disagreement
ledgers remain available. The saved counts are conditional on these transcriptions.

## Direction and identifiers

M = Mahadevan-style image inventory; P = Parpola catalogue; W = Wells/ICIT-style
secondary-export codes. Identical integers in different namespaces are not identities.
The primary sequence calculations use original file order, with names `file_start`
and `file_end`. The independent catalogue documents left-to-right display order. In
81 comparable overlapping objects, 65 are compatible in file order and none in reverse;
16 disagree. This supports, but does not prove universally, the display-order convention.

The external feature catalogue links 359 supplied M IDs to descriptions and 334 to
one or more W IDs. A **source-asserted reciprocal one-to-one** M/W relation is required
before a W profile is conditionally shown in an M dossier. This leaves 216 candidates,
184 with observations in the strict corpus. No inferred many-to-many collapse is made.
Correspondence is still provisional even when it is one-to-one.

## Structural measurements and permutation nulls

Statistics normally weight each distinct whole text once. Raw-row statistics are
also saved. Deduplication prevents manufactured duplicates or common formulae from
dominating a structure test; it also removes genuine differences in ancient usage
frequency. Neither weighting is a universal account of ancient text production.

- Unigram entropy: `−Σ p(s) log2 p(s)`.
- Adjacent mutual information: `Σ p(a,b) log2[p(a,b)/(p_left(a)p_right(b))]`, using
  within-text adjacent pairs only, without boundary markers.
- Endpoint Jensen–Shannon divergence: `H((p_start+p_end)/2) − (H(p_start)+H(p_end))/2`,
  for texts longer than one sign.

The plug-in estimates are finite-sample biased, especially with many rare signs.
They should not be directly compared across corpora with different inventories and
sizes to classify language.

Two nulls retain relevant observed marginals:

1. **Within-text shuffle:** preserves every text's length and multiset of signs.
   Tests whether its observed arrangement matters beyond membership.
2. **Length-and-position shuffle:** permutes signs across texts within each exact
   `(length, position)` slot. Preserves all positional frequencies conditional on length;
   tests dependencies beyond independent position-specific draws.

For 499 seeded draws, `p = (1 + number of null statistics ≥ observed)/(499 + 1)`.
The smallest reportable p is 0.002; it does not mean zero probability. Sensitivity
checks use 199 draws, with a floor of 0.005. These are exploratory tests and controls,
not preregistered discoveries. The three primary tests would still pass a Bonferroni
adjustment over those three tests; wider hypothesis families require their own accounting.

## Held-out prediction

Connected components join records sharing either an identical sequence or an artifact
ID. A missing artifact ID uses a namespaced source parent-ID fallback, never a shared
`-`. A component cannot cross folds. Each distinct sequence is then scored once.
This does not guarantee independence between near-duplicates, seals from one workshop,
or records whose duplicate artifact IDs were never reconciled.

There are 1,564 connected groups; the largest contains 205 distinct texts linked by
shared artifact sides and repeated short strings. It is deliberately kept intact,
so the five folds have unequal sizes. Breaking that group to balance folds would
reintroduce the leakage the grouping is designed to prevent.

Five folds are assigned by SHA-256 of sorted group text content, modulo five. Each
outer test fold remains untouched; the next fold validates smoothing strength, and
the remaining three train. After tuning, fit on train + validation, then test. The
fixed inventory is W001–W998; W000 and W999 are excluded. Unobserved genuine types
receive nonzero probability. Future catalogue changes require an explicit new inventory.

Models condition on known text length and score sign tokens only:

| Model | Probability information |
|---|---|
| Unigram | Global sign counts; add-0.5 smoothing |
| Position | First/interior/last/single sign counts, smoothed toward unigram |
| Bigram | Previous sign, or beginning marker, smoothed toward unigram |
| Bigram + position | Previous sign and position jointly, smoothed toward position |

Smoothing strengths are selected from `{1, 5, 20, 100}` on validation loss. The
unigram model has no tuned strength. Scores are negative log2 probability per sign;
smaller is better. This tests predictability, not restored-sign accuracy or translations.

Saved per-text losses support paired differences. Intervals use 1,000 bootstrap
resamples of connected groups, holding fitted models fixed. They describe conditional
score uncertainty, not uncertainty from complete model retraining or ancient corpus
sampling. Cross-site evaluation uses fixed strength 20 and removes all exact test
sequences from training; all other sites form the training pool.

## Morphology and partial hypotheses

Images are grayscale, foreground >127. Nearest-neighbor retrieval crops to foreground,
fits in a 56×56 box on a 64×64 canvas, and compares L2-normalized intensity vectors
by cosine similarity. These scores are uncalibrated shape similarities. They do not
establish that two signs are variants, share a sound, or share a meaning.

Candidate tally series come from explicit stroke-count descriptions in the attributed
catalogue. Short and tall series remain separate. A substitution frame is a complete
sequence with exactly one position masked. A frame counts as a tally candidate when
at least two signs with different described stroke counts occur in that same frame.
This is descriptive discovery, not a significance test of numerical semantics.

The dossier's positional role is deliberately coarse: fewer than 10 tokens gives
`insufficient evidence`; at least 80% at one edge gives an edge-concentration label;
otherwise `mixed/interior`. The actual counts are the evidence. These heuristic labels
are not fitted grammatical categories or meanings. In particular, M342's conditional
72.8% file-start frequency does not cross the arbitrary 80% threshold.

## What has not been established

No sound values, translations, language family, arithmetic units, or complete grammar
have been identified. No direct archaeological-image transcription audit of all objects
has been completed. The comparative data do not match Indus sampling perfectly, and
Pictish symbols are themselves disputed; weather icons supply the clearest unambiguous
nonlinguistic control. No pooled sample treats overlapping corpora as independent finds.
