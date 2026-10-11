# Do the five-stroke forms behave like variants?

The inline short-stroke sign M106 and stacked short-stroke sign M107 share two
exact complete inscription frames. The long-stroke sign M096 shares neither of
those contexts with them in the tested samples. This makes M106/M107 a reasonable
pair for investigating graphic variation, but it does not establish identical
values. Both shared frames also admit other stroke counts, so substitution itself
cannot distinguish an alternative spelling from a different number or label.

## Three samples, kept separate

| Sample | References / unique complete strings | M096 unique strings | M106 unique strings | M107 unique strings |
|---|---:|---:|---:|---:|
| Previous domestic seals | 1,175 / 1,066 | 4 | 16 | 4 |
| Same seal filter, every site | 1,182 / 1,073 | 4 | 16 | 5 |
| All object types, clear single document, including solus | 1,342 / 1,170 | 5 | 19 | 5 |

The first sample keeps the existing minimum two-sign, single-document, no-loss,
no-doubt seal filter and named domestic sites. The second drops only the domestic
restriction. The third allows all object codes and one-sign texts, while retaining
a single source document, no loss or doubt, and original direction codes 1 or 2.
It is a different sample, not a retroactive change to the first test.

All three samples give the same exact pair result: two M106/M107 shared frames,
zero M096/M106 frames, and zero M096/M107 frames. The shared frames are `? M169`
and `M267 M099 ? M162`. Both admit M102 and M104 too; the shorter one also admits
M100 and M112. Thus equal graphic stroke count does not have a uniquely distinctive
substitution pattern here. The M106 and M107 longer-frame examples 1131 and 1157
are both in the Mohenjodaro catalogue series, so a rule assigning the two forms
exclusively to different sites would not explain those examples. This establishes
neither contemporaneity nor a shared workshop.

No pair of the three signs cooccurs in an eligible complete string in these
samples. Their scarcity makes that absence weak evidence: it does not prove
mutual exclusivity, identical meaning, or allography. The wider source includes
multi-sided objects and damaged readings outside these samples.

A counterfactual M106/M107 merge reduces the number of distinct strings by two
in each sample. Merging M096 with either short-stroke form reduces it by zero.
These are bookkeeping effects of the observed matches, not a criterion that
licenses merging signs. Original codes, sequences and source references are
preserved. Every target-bearing frame and its occupants across all 417 codes
remain available in the result.

## The digital export was missing six relevant occurrences

| Sign | Primary Table I occurrences | Export occurrences, including uncertain records | Difference |
|---|---:|---:|---:|
| M096 | 22 | 20 | 2 |
| M106 | 38 | 35 | 3 |
| M107 | 6 | 5 | 1 |

These totals are not the clear-text sample sizes above. They count occurrences,
including source uncertainty. A numerical deficit alone would not identify a
missing line. Original concordance and Texts checks now locate the omitted lines:

| Sign | Object / side / line | Recovered normalized sequence |
|---|---|---|
| M096 | 2921 / 1 / 0 | M096 |
| M096 | 1325 / 2 / 0 | M025 M409 M096 |
| M106 | 8301 / 2 / 0 | M106 |
| M106 | 2923 / 2 / 0 | M387 M015 M104 M106 M312 |
| M106 | 2636 / 2 / 0 | M267 M099 **doubtful M106** LOSS |
| M107 | 1471 / 1 / 2 | M104 M205 M107 |

The rows are retained separately from the export. Multi-document objects remain
outside the single-document sample; 2923 has original direction code 4, and 2636
has both doubt and terminal loss. Recovering text does not automatically make it
eligible for a quality filter. The original glyph identities, boundaries and
uncertainty are more important than obtaining a convenient comparison pair.

All six M107 occurrences are now directly checked in the primary catalogue:
1157, 6111, 7072, 8016, 9846 and the missing line of 1471. Their positions reconcile
Table I's two initial, one medial and three final occurrences. This covers that
catalogue's six occurrences, not all archaeological examples ever discovered.
The full object 1471 has five printed lines on four sides; the export kept only
side 3. Its missing M107 line is additional text, not a corrected sign reading.

As a separately labelled sensitivity check, the script adds the five intact
recovered fields to the broad export sample, accepting their primary-normalized
order even for direction codes 3 and 4. It retains their side/line identities and
excludes damaged 2636. This is a target-selected supplement, not a full recovery
of all multi-sided objects. M106/M107 still share the same two frames. M096/M106
now share the one-position frame `?` because each has a recovered solus field.
That frame contains **no surrounding text**, so it does not supply contextual
evidence of equal function. M096/M107 still have no exact match in this supplement.

The [physical-object check](STONE1471_CONTEXT.md) identifies 1471 as HR2240,
CISI M-331 (NMI155), described by the excavators as a white steatite bossless
seal. Published photographs show four inscribed surfaces and five text lines.
The 0.7 × 0.7 inch dimensions and 9-foot find depth provide no authenticated mass,
counted contents, arithmetic equation or absolute date. M77's type9 classification
and the earlier excavator's seal terminology are both preserved; the object is
still outside the original single-document sample. Perforation wording is
apparently inconsistent or has an ambiguous illustration-list scope.

## Consequence for a decipherment

The two short-stroke forms retain a plausible relationship worth investigating.
No reading or arithmetic identity follows from their two matching frames. The
long-stroke control also shows why visually counting five strokes is insufficient
to collapse every five-stroke form. Sparse nonoverlap cannot establish that the
long form has a different value either. A numerical interpretation still needs
independent quantities, metrology, or predictive arithmetic constraints.

No semantic or phonetic assignments have been made. The concrete gains are a
more complete primary record, explicit context overlap and limits on what that
overlap can justify.

## Reproduction

Run `python scripts/audit_five_stroke_contexts.py`. The
[protocol](../data/processed/five_stroke_context_protocol.json) records the
exploratory selection and sample definitions. The
[result](../results/five_stroke_context_audit.json) retains every context, all 417
replacement summaries in each scope, counterfactual merge groups and source hashes.
A separate pairwise Hamming-distance enumeration checks the masked context index
for all three sign pairs in every sample.

The [M107 primary audit](FIVE_STROKE_PRIMARY.md) and
[missing M096/M106 line audit](FIVE_STROKE_MISSING_LINES.md) preserve original
page locators, images, uncertainty and failed lookups. These use already retained
PDFs; no new source download was needed for the textual checks. The separate
physical-object audit retained four Marshall archive files, all in `data/raw/`.

The [subsequent tool crosswalk](TOOL_SIGN_MASS_RESULTS.md) identifies recovered
2923 as the already measured chisel tang. It connects M106 to the existing mass
debate without adding an independent measured artifact or assigning a sign value.
