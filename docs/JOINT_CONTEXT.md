# Joint-context replication in the secondary corpus

The jar and fish positional contrasts remain visible when comparing signs within
the same recorded **site, object-type code and text length** in the secondary W
corpus. This reduces a specific joint-context concern left open by the primary
marginal proof. It does not identify meanings or remove transcription and mapping
uncertainty.

The distinction between sources is essential: these are the literal W identifiers
from the secondary export, with candidate M correspondences from the saved crosswalk.
They are not new joint counts from Mahadevan's printed catalogue. No proposed
translations are read and no primary and secondary counts are pooled.

## Results with repeated sequences reduced

For this table, duplicate occurrences of the same complete sequence within the same
site/type context are reduced to one record. Matching additionally fixes text length.
Only strata containing at least five occurrences of **each** compared sign/group
are included. The threshold is a descriptive support screen, not a confidence level.

| W signs/groups | Candidate M labels | Position | Shared strata | Matched tokens, first / second | Weighted rates, first / second |
|---|---|---|---:|---:|---:|
| W740 / W741 | M342 / M343 | Final | 6 | 295 / 76 | 77.55% / 0.00% |
| W740 / {W742,W743,W744} | M342 / candidate M344 group | Final | 1 | 51 / 5 | 74.51% / 0.00% |
| W740 / {W745,W746,W747} | M342 / candidate M345 group | Final | 0 | 0 / 0 | Not estimable |
| W032 / W002 | M087 / **M099 or M100 unresolved** | Initial | 10 | 88 / 269 | 17.07% / 0.25% |
| W220 / W235 | M059 / M065 | Initial | 6 | 80 / 55 | 3.45% / 24.58% |

The first and last comparisons retain the directions seen in the primary source.
The M344-candidate result rests on a single supported stratum and five comparator
tokens; it does not justify a broad generalization. The M345-candidate comparison
has no qualifying stratum, so no matched effect is reported. The stroke comparison
is only a related W-code contrast: **W002 has reverse correspondences to both M099
and M100**, and must not be presented as a uniquely identified M099 replication.

The final-rate zero for matched W741 is not a claim that W741 never occurs finally.
There are two such occurrences in the full strict source selection; they fall
outside these qualifying shared strata. The deduplicated context corpus contains
959 W740 tokens and 135 W741 tokens altogether, of which only 295 and 76 enter this
particular matched summary. Unmatched support is visible in the result files.

## Method and sensitivity

The starting data are the previously defined complete, single-line, R/L-filtered
2,914 secondary records. Eighteen records have missing site/type metadata and are
excluded from this analysis. Remaining record counts are:

| Weighting regime | Records |
|---|---:|
| All eligible rows | 2,896 |
| Unique artifact × sequence × site/type | 2,880 |
| Unique sequence × site/type | 1,983 |

The last count differs from global unique-sequence counts because the same sequence
can legitimately contribute in different recorded contexts. Occurrences of a sign
repeated within one sequence remain separate sign tokens. None of these regimes
guarantees independent archaeological observations or removes all shared templates.

Site and type strings are retained exactly, without translating secondary type codes
into Mahadevan's object classes. Two matching definitions are reported: site × type,
and site × type × exact sign count. For each stratum containing both groups, define
`w = 2*n_first*n_second/(n_first+n_second)`. Each group's matched event rate is
the weighted average of its own within-stratum rates, using the same weights.
This harmonic weight emphasizes contexts with overlap and reduces the influence of
strata dominated by one group. It defines a descriptive target population; it is
not the overall corpus rate or an estimator with a claimed causal interpretation.

The files include both minimum-one and minimum-five support screens under all three
weighting regimes. Under site/type/length matching with the minimum-five screen,
the W740–W741 gap is 69.33 percentage points using all eligible rows, 69.24 after
artifact/sequence/context deduplication, and 77.55 after sequence/context
deduplication. For W220–W235, the corresponding signed initial-rate differences are
−34.73, −34.73 and −21.14 points. The conclusions about direction persist; the
magnitudes depend on weighting and support.

Positions follow the established file-order interpretation for this filtered
corpus: the file-left edge corresponds to reading-final and the file-right edge
to reading-initial. Single-sign texts are labeled separately and do not become
artificial final-position events. This relies on the export convention and prior
overlap checks, not a new determination of ancient direction from statistics.

## Evidence and limits

- [Analysis script](../scripts/analyze_joint_context.py)
- [All matched summaries, denominators and reverse-M ambiguities](../results/joint_context_summary.csv)
- [Every context's counts and rates, including unmatched contexts](../results/joint_context_strata.csv)
- [Mappings, selection and caveats](../results/joint_context_audit.json)
- [Tests of singleton handling, matching and deduplication](../tests/test_joint_context.py)

The five shape comparisons predate this replication, but the project remains
exploratory; no preregistration, blind semantic test or independent digitization is
claimed. The mapping source is provisional, even for one-to-one entries. Chronology,
neighboring signs, object subtypes, measurement error and selection bias remain.
There are no p-values, confidence intervals or claims of population significance.

The combined result is a better-supported constraint: a candidate reading must
explain substantial positional differences among related shapes within observed
shared contexts. Freely substituting the forms without contextual rules loses
observed distinctions. Position-conditioned allographs, grammatical variants,
quantity modifiers and separate lexical signs remain possible explanations.

## Missing-page recovery

The attempted alternate Archive item reports `is_dark=true`; no attempt was made
to obtain files through another server. A public library download page could not
be reached because its hostname did not resolve. The
[RMRL book page](https://rmrl.in/en/dl/research-papers/mahadevan/ebook?id=The+Indus+script+-text+%2C+concordance+and+table_1977)
links to a public flipbook, but its visible page counter has 48 pages and the last
page is the “Tables” divider. It does not recover the two missing Table IV pages.

The [recovery log](../results/source_recovery_attempts.json) records these outcomes.
Downloaded discovery metadata, HTML and configuration remain together with all
other downloads in `data/raw/`, with hashes in `data/sources.json`. The unresolved
primary object counts have not been silently supplied by this secondary analysis.

Reproduce with `python scripts/analyze_joint_context.py` after the corpus preparation
and crosswalk generation steps, or run the full offline pipeline.
