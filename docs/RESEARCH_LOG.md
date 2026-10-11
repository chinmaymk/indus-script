# Research log: attempts, results and corrections

Last updated: 25 September 2026. This is the continuing research record for the
Indus-script investigation. Full decipherment remains unresolved.

Earlier progress entries below are preserved. The backfill at the end was
reconstructed on 23 September from saved reports, scripts, ledgers and outputs;
its order is thematic, not an invented timestamped history. This logs research
attempts and consequential operational failures, not every terminal invocation.
Detailed exclusions, individual witnesses and numerical outputs remain in the
linked evidence files. A hypothesis being compatible with the data is not a
verified reading; failed tests and corrections stay in this record.

## How to continue this log

Append an entry for every substantive investigation, including unsuccessful
searches and negative results. Record the date, question or fixed prediction,
data and selection rules, method/script, result, interpretation limits, evidence
paths, corrections, and next discriminating test. Say when a test was exploratory
or a rule was changed after viewing results. Do not erase failed predictions or
silently replace earlier observations. Record a later correction explicitly and
link the superseding evidence. Keep all downloads in `data/raw/` and register
their provenance in `data/sources.json`. Update this log before reporting a
research phase as finished, then refresh the run manifest.

## Evidence index for the original progress entries

| Investigation | Detailed method, results and evidence |
|---|---|
| Input audit, sequence controls, held-out prediction and identifiability | [Methods](METHODS.md), [main report](REPORT.md), [proof](IDENTIFIABILITY.md), `scripts/audit_images.py`, `scripts/analyze_sequences.py`, `scripts/suggest_sign.py` |
| All 417 primary position profiles | [Primary inventory](PRIMARY_INVENTORY.md), `scripts/extract_primary_table.py`, `scripts/analyze_primary_inventory.py` |
| Site/object marginal bounds and joint-context comparisons | [Bounds](CONTEXT_BOUNDS.md), [joint analysis](JOINT_CONTEXT.md), `scripts/analyze_context_bounds.py`, `scripts/analyze_joint_context.py` |
| Bangle/jar provenance and numerical underdetermination | [Anchor audit](QUANTITY_ANCHORS.md), [MD1374 source follow-up](MD1374_SOURCE_FOLLOWUP.md), `scripts/audit_quantity_anchors.py` |
| Numerical equations, coverage, photographs and conversion counterexample | [Equations](NUMERAL_EQUATIONS.md), [screen](NUMERAL_SCREEN.md), [image checks](NUMERAL_IMAGES.md), `scripts/audit_numeral_equations.py`, `scripts/screen_numeral_pairs.py` |
| Graphic families and allograph hypotheses | [Family audit](SIGN_FAMILIES.md), `scripts/analyze_sign_families.py` |
| Copper motifs and cross-object transfer | [Copper bridges](COPPER_BRIDGES.md), [imagery hypothesis](ICONOGRAPHY_THEORY.md), [photographs](ICONOGRAPHY_PHOTO_FOLLOWUP.md), `scripts/audit_copper_bridges.py`, `scripts/audit_iconography_theory.py` |
| Parallel ordering and context-model tests | [Comparison](PARALLEL_THEORIES.md), [numeral ordering](NUMERAL_THEORY.md), [primary witnesses](NUMERAL_PRIMARY_FOLLOWUP.md), [structure models](STRUCTURE_THEORY.md) |
| Published hind-leg/fish phonetic proposal | [Audit](HIND_LEG_HYPOTHESIS.md), `scripts/audit_hind_leg_hypothesis.py` |
| All-sign integration and hypothesis tracking | [All-sign evidence](ALL_SIGN_EVIDENCE.md), [hypotheses](HYPOTHESES.md), `scripts/build_evidence_index.py` |
| Downloads, unsuccessful access and provenance | [Sources](SOURCES.md), `data/sources.json`, `scripts/fetch_data.py` |

## Original progress entries

Primary-source validation now also checks all four archive book files against
archive sizes and MD5 checksums. Actual table contents are revalidated when profiles
are generated, rather than trusting a potentially stale audit. A four-line visual
transcription pilot preserves damage, source doubt and the editor's normalized
right-to-left direction. Text 1004 visibly demonstrates an internal M342. The pilot
is purposively selected, not held-out evaluation or a representative corpus.

## 22 September 2026: first investigation

Progress: preserved input audits, secondary sequence data, controls, held-out tests,
all-sign dossiers, and a scoped identifiability proof. No complete reading was found.

## 22 September 2026: download consolidation

Progress: every task download previously stored in temporary space was copied into
`data/raw/`, hash-verified, and indexed. Future downloads are kept there.

## 22 September 2026: primary catalogue extension

Previous goal turn classification: **progress**, because consolidation changed the
authoritative retained data and its provenance, rather than merely restating status.

New progress: downloaded the primary printed M77 catalogue and OCR; transcribed all
417 frequency-table rows; corrected 112 cells against the scans; verified every row,
all five column totals, seven frequency bands, and positional type counts. Added
direct M-number profiles to every atlas entry. Recorded non-interchangeable positional
behavior within jar and repeated-stroke families, with confounds left explicit.

Completion audit: data/script persistence is satisfied for the work so far. A verified
meaning/sound assignment covering the signs is still absent. Distributional profiles
and aggregate agreement do not prove decipherment. The original goal remains active.

Next concrete route: inspect the primary printed text pages for a reliable glyph-to-ID
transcription path, retain ambiguity/damage, and compare recovered texts to the original
tables. This would reduce dependence on the secondary export and its provisional mapping.
No impasse is declared: the newly acquired primary source enables meaningful further work.

## 22 September 2026: context bounds

Previous goal turn classification: **progress**. It added checked primary profiles,
archive integrity checks, a damage-preserving sequence pilot and an explicit internal-jar
witness. The full decipherment was not achieved.

New evidence: transcribed 12 primary context rows covering eight signs from the five
previous shape contrasts. A total-variation bound shows that different site mixtures
with shared empirical within-site position rates cannot reproduce any of those five
contrasts. Separate object-type mixtures also fail this necessary condition for the
fish and two-stroke comparisons. A sharp intersection bound forces a final-position
rate difference of at least 39.70 percentage points between M342 and M343 within
Mohenjodaro. Saved the proof, exact-rational calculations and tests of the bounds.

Source correction: the inspected PDF omits printed pp. 758–759 at the Table IV/V
boundary. Removed the claim that a complete printed catalogue was obtained. Jar
object-type counts remain missing, with no imputation.

Completion audit: no semantic/phonetic key covering the inventory exists. The new
proof narrows contextual explanations but cannot identify word values. The objective
remains active. Next useful evidence is a second scan for the missing pages and
checked joint context/position records; neither missing joint data nor this local
scan gap constitutes a general research impasse.

## 22 September 2026: joint contexts and source recovery

Previous completed goal turn classification: **progress**. Primary context
transcription and exact bounds changed the evidence available for shape contrasts.
The intervening search found candidate recovery routes; the continuation resumed
those routes without restarting or treating unfinished work as completion.

The alternate Archive item is dark; no inaccessible files were pursued. The official
RMRL public flipbook contains only a 48-page excerpt ending at the Tables divider.
The missing Table IV pages remain unrecovered. Discovery downloads and their
provenance are retained in the common raw-data folder.

New analysis compares the selected W-code groups within joint site/type/length
strata under three deduplication regimes, without importing proposed readings.
The W740/W741 and W220/W235 positional differences persist. The reverse mapping
W002→M099/M100 is explicitly ambiguous, the M344-candidate group has only one
well-supported matched stratum, and the M345-candidate group has none under the
minimum-five screen. Every stratum and excluded denominator is retained.

Completion audit: these are constraints on candidate readings, not a decipherment.
No all-sign semantic or phonetic assignment has been verified. The goal remains
active. Further progress should prioritize independently anchored quantity or
semantic hypotheses and primary text transcription, rather than treating more
descriptive fit as a translation.

## 22 September 2026: quantity anchors and artifact provenance

Previous completed goal turn classification: **progress**. Joint-context comparisons
added constraints, while the scan-gap recovery search remained unsuccessful.

Shifted from distributional evidence to proposed independent numerical anchors.
Downloaded Rao's versioned 2018 manuscript and the original Mohenjo-Daro field
report into the same raw folder; registered and checked both hashes. Retained
source renders, OCR, extraction code, claim dependencies and mathematical proofs.
No source-proposed translations were added to the corpus.

The field report distinguishes the jar associated with the large fragment group
from the jar bearing the readable sealing. This breaks the assumed verified
artifact-level pairing unless later documentation supplies the missing link.
The quantity audit also shows that twelve positive integer weight assignments fit
the stated contents interval under a simple additive model. Decimal notation is
compatible but not uniquely identified. Capacity fits have a numerical-scale
symmetry, and choosing unknown photographic scale from expected capacity adds no
independent calibration.

Completion audit: useful new source evidence and falsifiable constraints were
obtained. Full decipherment remains unresolved; no sign meaning has become
established. The goal remains active. Further productive work includes checking
later bangle reconstructions against artifact identifiers and recovering independently
measured capacity tables. No recurring impasse is declared.

Validation: the full offline pipeline completed with 31 passing tests, all twenty
download hashes verified, and no broken local documentation links. The final
manifest was refreshed after the bibliography and visual-review ledger updates.

## 22 September 2026: complete conditional numeral-equation solution

Previous goal turn classification: **progress**. It added primary artifact-context
evidence, a quantity-anchor ledger, exact calculations and reproducible scripts.

Investigated later bangle work and found a new, explicit numerical proposal by
Fuls (2020). No later independently checked E/G artifact bridge was obtained.
Public text in two renderings supplied two equations. A divisor proof gives all
four positive integer solutions; two survive the proposal's minimum-base bounds.
The published (10,8,6) candidate becomes unique only with an additional bounded
assumption such as the disputed bangle anchor. Prime-base exclusions are unnecessary
for that conditional result. A second solution, (36,20,4), is a precise witness to
remaining ambiguity, not a claim about historical practice.

Selected literal corpus records expose unresolved sign-code, face-number and
artifact-ID joins. Proposed readings were excluded; source figures remain unchecked.
Saved the source-access ledger, complete proof, solver, all solutions and tests.

Completion audit: the calculations identify a compact partial candidate under
explicit assumptions, but do not establish those assumptions or cover all signs.
The goal remains active. Next discriminating work is artifact-image validation and
testing fixed numerical rules on all eligible examples, including failures, rather
than selecting more examples that happen to balance. Meaningful progress was made;
the blocked threshold does not apply.

## 22 September 2026: complete denominator for the two-marker numeral rule

Previous goal turn classification: **progress**. It established a complete
conditional algebraic solution set while retaining unresolved artifact joins.

Screened all 5,680 source rows, grouped into 4,695 local objects, for literal W700
and W840. All twenty candidate groups and their 44 rows are preserved. The fixed
adjacent-run rule admits five under strict quality filters, but they contain only
three distinct text pairs. Four equalities are identities; the fifth is the
already-used construction equation. Both surviving numerical candidates fit, so
this is not independent identification of their values.

H-904 is a proposed pattern-based crosswalk to the paper's two-face example. Its
local ID is 1786, while the paper gives 3786. No artifact identifier or sign code
was rewritten. The figure and artifact photograph remain unverified.

Because additive flanking sums are direction invariant, a sensitivity admits
complete L/R-labelled faces. H-306 then supplies a mismatch with residual L, which
cannot vanish for any positive long-stroke value under the fixed rule. This is a
conditional secondary-transcription counterexample, not an authenticated primary
artifact result. A separate stacked-stroke scale sensitivity demonstrates that
three of the five strict matches depend on that scale assumption.

Persisted the exploratory protocol, parser, full exclusion and residual-sign
ledger, numerical results, proof of the mismatch, and four validity tests. No new
data were downloaded; existing downloads remain together in data/raw/. The full
pipeline's test stage passes all forty tests.

Completion audit: the narrow numerical interpretation has documented coverage and
a retained counterexample. It does not explain all signs or establish a unique
numerical key. Full decipherment remains unresolved and the goal remains active.
Productive next work includes primary-image checks of H-306/H-904, the M-331 sign
crosswalk, and independently measured capacity data. This turn made progress;
there is no repeated blocking condition to declare.

## 22 September 2026: photograph and identifier verification

Previous goal turn classification: **progress**. It preserved the complete
two-marker screen, limited its apparent fit, and retained a conditional mismatch.

Obtained two public PDFs in the same raw-data folder: Farmer's 2004 presentation
and Joshi/Parpola's 1987 CISI volume 1. The first located an H-306 photograph; the
second supplies the catalogue image and object identifiers. Together with the
existing Mahadevan catalogue, the excavation/museum chain now corroborates the
two-versus-three stroke pattern. This is stronger evidence than the modern CSV,
but the numerical interpretation and face equality remain assumptions. These are
reproductions of the same object, not additional independent samples.

The CISI scan consists of two image-identical 431-page copies, despite having 862
PDF pages. Saved a script and all 431 nonempty image-stream comparisons; always use
the first copy for locators. This is volume 1 only. No H-904 image verification is
claimed from it. A slow download exceeded its initial deadline; the live retry
was interrupted and the remaining file resumed successfully with a longer limit.
The final full-file size and SHA256 are recorded, with an appropriate refetch timeout.

Visually reviewed M-331's photographs and identifier row. Its four inscribed
physical faces map to local rows A, B, F, D; the author's prose appears to order
them A, B, D, F. This clarifies the ordinal mismatch, while W899/W900 identification
and the proposed total relation remain unresolved. Both visual ledgers separate
observations, joins, and interpretation.

Extended the exact arithmetic check to allow any positive constant stroke value
in each marker context. The H-1923 and H-306 recorded pairs require incompatible
ratios 1 and 3/2. Saved the algebra, rational constraints and a validity test;
the H-1923 record still needs primary-image verification.

Completion audit: the work adds primary corroboration and a broader constraint;
it does not decipher all symbols or establish semantic values. The goal remains
active. Next useful evidence includes the H-904 and H-1923 images in other volumes,
an authenticated W899/W900 signary comparison, and independently measured quantity
anchors. This turn made progress and is not a repeated impasse.

Validation: the full offline pipeline completed with 41 passing tests and all 22
download hashes verified. The separate PDF audit checks every duplicate-page pair;
both visual ledgers match their registered source hashes. Local documentation links
were checked and the run manifest refreshed after the final notes.

## 22 September 2026: whole-inventory sign-family comparison

Previous goal turn classification: **progress**. It corroborated H-306 through
catalogue images and identifiers, clarified physical-face ordering on M-331, and
extended the numerical counterexample to constant unit conversions.

Extended the investigation beyond the numerical subset. All 76 source feature
entries with multiple W identifiers now have descriptive substitution witnesses,
co-occurrence checks, and variant-prediction results. Twenty meet the stated
support gate. A separate index covers every one of the 417 M signs without
pretending that many-to-many catalogue links identify each M variant. Its coverage
categories are 31 linked to supported families, 73 linked only to sparse families,
and 313 without an asserted multi-W family.

Added five-fold prediction with connected artifact and family-normalized-text
grouping. All variants of an otherwise identical text stay together, preventing
near-duplicate leakage. Predictions are conditional on the family being known.
The 2,283 supported-family tokens show a small neighbor gain at the specified
smoothing strength, 0.0217 bits per token, with ten families gaining and ten losing.
The largest connected component is substantial. Added an explicitly post-result
weighting sensitivity: results weaken or change sign under some smoothing choices.
No allograph status or meaning is inferred from either gain or lack of gain.

Saved the protocol, normalized-probability model, all token scores, all 76 family
summaries, fold assignments, exact witnesses, and all-sign coverage index. The
public repository abstract of Daggumati/Revesz 2021 supplied background only; no
additional file was downloaded or proposed merger list imported.

An exploratory P364 witness pair, K-62/M-503, was located in the already downloaded
CISI volume. The latter photograph is too degraded to authenticate the fine variant
contrast. Persisted this failed verification in a visual ledger instead of treating
a located photograph as automatic confirmation. No source sign was changed.

Validation: the full offline pipeline completed with 46 passing tests and all 22
download hashes verified. Tests cover normalization with unseen variants, exclusion
of the target from predictors, transitive grouping, duplicate-frame counting, and
ambiguous catalogue memberships. Actual grouping checks report zero artifacts and
zero family-normalized texts crossing folds.

Completion audit: the work gives broader, explicitly limited constraints and
prioritizes concrete image checks; it does not provide a semantic or phonetic key
for all signs. Full decipherment remains unresolved and the goal remains active.
Meaningful progress was made. Future progress can use clearer candidate-variant
images and external anchors; no repeated blocking condition is declared.
## 22 September 2026: copper-tablet external associations

Previous goal turn classification: **progress**. The family comparison added
whole-inventory coverage, predictive results, and a failed fine-variant image check.
The next step was to investigate external text–image anchors.

Downloaded Parpola's eight-page 2008 copper-tablet paper into the same `data/raw/`
folder and registered its hash and URL. Rendered and inspected the reconstructed
type figures. Transcribed all 46 subtype counts; their totals reproduce A=34,
B=144, C=39, total 217. Saved the eight published links separately from any
artifact-level measurements. The source's classification can use surviving text or
motif traces, so its reconstructed pairings are not independent fully read examples.

Added a literal bridge search across the existing export's Mohenjo-daro TAB:C rows.
It joins a singleton reverse and its longer companion text to a different object
with the exact same text and a recorded motif. Original W codes, direction, source
labels, IDs, and conditions remain visible. The search imports no language reading
or translation. It finds 10 singleton/text/motif triples among 191 qualified rows,
involving seven singleton codes. Good/Fair-only filtering leaves 3 triples among
94 qualified rows, all connected to Anth through the same longer text.

W777 has an exact-code goat-side bridge through M-1555–1558 and M-548, and a separate
human-figure bridge through M-604 and several objects including M-585/M-587. The
former relies on Poor donors. The raw label conflicts Buff/Goat:8/Othr are retained,
not inflated into securely distinct ancient meanings. The observed paths challenge
a direct unique animal-name interpretation conditional on correct source readings;
they do not disprove broader religious or institutional associations.

Located and reviewed CISI photographs M-534, M-593, M-585/M-587, M-599 and M-604.
Some motifs and texts are clear, but crucial fine details are degraded. Recorded
these limits explicitly: no complete bridge was independently authenticated from
both donor and motif photographs. M-1555–1558 are outside the downloaded volume.
No source code, allograph grouping, or semantic value was changed.

Validation: full offline pipeline completed with **50 passing tests** and **23
registered download hashes verified**, plus the archived denied response. New tests
cover singleton NR handling, unknown/damaged exclusions, exact-match isolation,
duplicate-artifact counting, ambiguous donors, and quality-filter disappearance.
Saved code, protocol, type ledger, visual ledger, complete witnesses and summary.

Completion audit: the requested universal decipherment remains unproved. The work
has narrowed a concrete class of semantic hypotheses and identified precisely
which object images could strengthen or overturn it. This is meaningful progress,
not a repeated impasse; the goal remains active. Further work should prioritize
legible donor images and independent contexts, rather than treating another count
of the same reconstructed types as a new semantic anchor.

## 22 September 2026: authorized parallel theory tests and all-sign integration

Previous goal turn classification: **progress**. It added the copper bridge audit,
a registered primary-author source, and a condition sensitivity with photographic
limitations. The user explicitly authorized subagents to test theories in parallel.
Three bounded investigations ran concurrently; each preserved its protocol, code,
results, and tests in separate files. No additional source was downloaded.

The imagery investigation found two non-copper transfer cases: W777 on Good H-598
with Bull1:W, and the exact rhinoceros-linked copper text on Good M-1803 with Bull1:I.
Only the first remains testable after rebuilding discovery under Good/Fair filtering.
Six other singleton candidates and four other whole texts lack external occurrences.
An excavation match locates H-598 in Mahadevan ref5073, printed131/PDF142 and
appendix822/PDF831; both agent and parent inspected the saved pages. This corroborates
the locator and a drawing, not a photo, exact W code, or motif classification.
The explicit target is a universal motif-caption rule, not generic animal words.

The numeral investigation exhaustively tested all fixed class orders for maximal
adjacent tally runs. Best distinct-class order fails 26/186 unique-text multi-sign
runs; 12/89 survive in the Good/Fine subset. M-160 and M-678 are Good, from the same
site/type, and R/L-labelled, yet contain the same two codes in opposite orders.
The mathematical minimum-boundary result is checked against exhaustive partitions.
It is conditional on a run being one field; addition and multiple fields remain
countermodels. Source quality labels Good/Fine differ intentionally from the
imagery Good/Fair sensitivity and are documented with exact denominators.

The structure investigation compared length/position-conditioned one-sign,
two-sign and first-plus-two-sign contexts with connected artifact/text folds.
Two-sign context gains 0.02290 bits at alpha20, but only 0.00734 over a post-result
sharpening control; site/type-set sensitivity reduces the latter to 0.00271.
First-sign residual is 0.000237 with an interval crossing zero. Controls retain
child support, so they are not exhaustive independence nulls. Weather icons also
benefit; synthetic controls detect planted dependencies. No language is inferred.
Parent review clarified the calibration and metadata limits before integration.

Added a consolidated 417-row evidence index linking direct primary positional
profiles, family coverage, and conditional copper associations. Six M entries
have catalogue paths to copper candidates, with full many-to-many memberships
retained; W780/W781 remain explicitly unmapped. All 417 sounds and meanings are
undetermined. Tests reject duplicate/missing M rows and preserve mapping ambiguity.
The atlas links to this index's documentation.

The first integrated test run caught a module-name collision because analysis
scripts shared test filenames. Renamed the analysis scripts to audit_iconography_theory.py
and analyze_structure_theory.py, updated references, then reran the full pipeline.
It completed successfully with **66 tests passing**, all **23 registered download
hashes** verified, and the archived denied response verified. Documentation links
and the new visual ledger's source hash were also checked. The final manifest was
refreshed after these notes.

Completion audit: all three bounded investigations finished and were integrated;
the full user goal remains unresolved. Counterexamples narrow specific strong
assumptions but do not establish a semantic/phonetic key for all signs. Meaningful
new evidence was produced, so no repeated blocker is declared. Next useful work
includes photographic authentication of the concrete transfer/order witnesses and
alternative rules specified before testing further objects. Parallel delegation
is now explicitly authorized for future bounded theory tests.

## 22 September 2026: primary witness checks and a published phonetic proposal

Previous goal turn classification: **progress**. Three parallel theory tests were
completed and integrated with 66 passing tests and all-sign evidence coverage.
This turn pursued their concrete authentication gaps while auditing an actual
published reading proposal. Authorized subagents handled distinct bounded checks;
the parent reviewed and integrated their evidence.

M-160 was located in CISI1 printed48/PDF84, showing original and impression. Its
impression clearly has one long stroke followed by two short strokes in display
order. The data row at printed367/PDF403 links it to Mahadevan2286, DK12449,
ASI63.10.88. The export's DK12449286 is retained as an unresolved malformed or
concatenated field. Mahadevan2286, printed66/PDF77, has the same displayed order.

The normalized drawings at Mahadevan1066 (printed41/PDF52) and2427 (printed71/PDF82)
show short–long and long–short–long respectively. Parent and subagent both inspected
the saved pages. The proposed CISI M-678/M-1745 crosswalks remain incomplete: the
appendix supplies publication-item ranges, not individual excavation IDs. Direct
claims use the Mahadevan references instead. Persisted three manual class patterns
and evaluated both rank orders separately with the existing descent calculation.
Neither fits all; 2427 needs a boundary under either ordering if monotone fields
are required. No ancient segmentation or numerical value follows, and these
selected overlapping examples are not added to corpus counts.

Downloaded a public author-hosted Parpola2009 paper, Daggumati/Revesz2021 publisher
PDF and its author-publication index, all into data/raw. Registered URLs, sizes and
verified hashes: now 26 downloads. Public alternate copies were used after other
hosts denied downloads; denials were not bypassed. Parpola's figure5a explicitly
identifies H-598 and photographically places the compound glyph and single-horn
animal on the same impression face. The rightmost compound agrees in broad form
with the earlier drawing, but exact W777 allocation and the copper donor remain
unverified. A reported H-598 orientation correction concerns the bent/Z-like
W435/W436 candidate family, not the final compound; no transcription was changed.

The newly available paper also proposes taaL for a hind-leg sign, with taaL+miin
in M-1690. An exhaustive scan of W278/W279 candidates finds eight occurrences,
six strict, and only the discovery object with the leg→plain-fish adjacency.
The author does not assert universal fish adjacency, so the other contexts do not
refute the reading. Five objects are not named in the selected argument, but
none supplies an independent semantic target; no historical blind test is claimed.
The candidate codes lack direct P/M feature entries. M084 is visually plausible
but formally maps only to W280; it is not silently reassigned. W345 on the author's
proposed follow-up M-290 has conflicting animal identifications. All occurrences,
related codes, direction conventions, source exposure and mapping gaps are saved.

Added render-only mode to the PDF helper and a reproducible numeral-page/crop
script. The render-only path was exercised successfully. New visual ledgers and
three evidence chapters are linked from the existing reports; stale no-photo
statements are explicitly superseded for H-598. The hind-leg scan is integrated
into the offline pipeline. Full validation passes **70 tests**, verifies all **26
registered downloads** plus the archived denied response, and reproduces both
new audits. Source hashes, image paths, documentation links, candidate counts,
primary order results and all 417 unresolved reading statuses were checked.

Completion audit: the universal decipherment remains unproved. Primary observation
support improved and one actual phonetic proposal received exhaustive contextual
scrutiny, but no new sound or ancient meaning was established. This is progress,
not a repeated impasse; the goal remains active. Concrete next needs include exact
variant authentication for the copper donor, primary W278/W279 mapping, and external
semantic evidence capable of distinguishing the proposed reading from alternatives.

## 23 September 2026: retrospective backfill of remaining investigations

These entries document work already performed during 22–23 September. Individual
execution times were not consistently recorded, so none are invented here.
Numbers describe the specified source/subset, not the entire archaeological corpus.

### R01 — Initial image, sequence and identifiability experiments

Question: can the supplied inventory or sequence statistics identify a reading?
Audited all417 PNGs against the pixel matrix: every image is150×150 and every row
matches. Filtered5680 secondary inscription rows to2914 complete rows,1848 distinct
texts,8489 deduplicated tokens and575 W codes, keeping exclusion reasons. Used
shuffle and position-conditioned controls, grouped held-out sign prediction and
structured nonlinguistic controls. Order contains predictive information, but that
does not identify spoken language. A universal five-sign/one-sign-per-field schema
fails:1482 of1848 distinct texts are not length five. A label-permutation proof
shows why distributional fit alone cannot select sounds or meanings; it does not
prove decipherment impossible with external evidence. No linguistic key was
silently assumed. [Methods](METHODS.md), [proof](IDENTIFIABILITY.md),
[report](REPORT.md); `scripts/hypothesis_checks.py`, `scripts/check_transcriptions.py`.

### R02 — Recovering a vessel-capacity source

Sought Wells2015 Table4.1 and independent measured quantities. The target table
remained unavailable. An earlier Fuls2012 public-text source supplied Wells2009
measurements and calculated capacities, so it is not an independent measuring
campaign. H-370/H-372 excavation-number assignments conflict with CISI; no silent
reassignment was made. K-90's claimed30cm photo scale was not authenticated.
[Recovery and retained conflicts](CAPACITY_TABLE_FOLLOWUP.md).

### R03 — Testing a common litres-per-stroke rule

Visually checked H-370/H-371/H-372 stroke groups and fitted proportional capacity
models for three published geometries, including leave-one-vessel-out predictions.
The selected3/6/7-stroke trio fits approximately40–42L per stroke. Other published
vessels do not share that constant. The geometries reuse the same measurements,
and uncertain source identity remains; the fit establishes neither a universal
unit nor a sign meaning. [Results](CAPACITY_MODELS.md);
`scripts/analyze_capacity_models.py`.

### R04 — An independently scaled vessel profile

Recovered a labelled0–20cm profile for excavation6640-501. Preserved the caption/
drawing H95-2662/H95-2661 discrepancy. Traced the interior without calibrating its
scale to a proposed reading: estimated85.955L, with geometric sensitivity roughly
78.019–94.659L, not a statistical confidence interval. Four rim traces are favored,
with a three-trace sensitivity; the vessel also has separate body inscriptions.
This does not fit a universal40L-per-stroke rule and is not a direct fill measurement.
[Profile](H95_PROFILE_CAPACITY.md), [inscription review](H95_INSCRIPTION_REVIEW.md);
`scripts/analyze_h95_profile.py`.

### R05 — Exhaustive exact-frame substitutions

Extended comparisons beyond preselected graphic families to all575 observed W
codes. Wildcarded one position while retaining the exact remaining text and
deduplicating inscriptions:329 shared frames,2318 connected pairs,276 connected
codes,299 without a connection. Of the pairs,2104 share only one frame. Longer
contexts greatly reduce support. Shared placement does not prove allography,
synonymy or equal phonetic values. Preserved cooccurrence and unmapped signs rather
than merging them. [Audit](SUBSTITUTION_NETWORK.md);
`scripts/audit_substitution_network.py`.

### R06 — Auditing a published 2026 reading key

Pinned Glossa commit40812fc54470d5508b47af5fabcea7ccf044036c; compared the397-entry
research key with the287-entry backend key and made a row for each supplied sign.
There are115 changed readings among shared entries. Primary images contradict
several stated pictorial identifications, including M012/M047/M059/M099/M328.
Assignment coverage is not verified reading accuracy. No proposed translation
entered the main corpora or unresolved meaning fields. This audit rejects accepting
these artifacts as a demonstrated key; it does not reject all Dravidian hypotheses.
[Key audit](GLOSSA_KEY_AUDIT.md), [sign review](GLOSSA_SIGN_IDENTITY_REVIEW.md);
`scripts/audit_glossa_key.py`.

### R07 — Checking the candidate key's validation and data provenance

Inspected competing manuscripts and validation code as text; did not execute
downloaded scripts. Found differing scope claims, circular anchor promotion,
problems with the uniform baseline and entropy calculation, cross-object bigrams,
and reuse of priors as supposed validation. Private Holdat data prevented an exact
historical rerun. Separately distinguished whole-book OCR, a flat numeric export
and canonical object records: no reproducible raw-OCR-to-final-export chain was
established. [Methodology](GLOSSA_METHODOLOGY_REVIEW.md),
[export review](GLOSSA_EXPORT_REVIEW.md), [ingestion](M77_INGESTION_REVIEW.md);
`scripts/audit_glossa_export.py`.

### R08 — Reviewing a statistical-specificity counterexample

Read the2026 SIGIL critique and inspected its public source/metadata. Its registry
has54 entries but six dependent outcomes are exactly scored; these are not54
independent successful tests or recovered Indus meanings. The example challenges
claims that particular statistics necessarily imply linguistic encoding. It does
not establish that Indus was nonlinguistic. No external experiment was claimed as
locally replicated. [Bounded review and reproducibility limits](NONSPECIFICITY_2026_REVIEW.md).

### R09 — Recovering native Mahadevan-number sequences

Extracted2906 M77-attributed rows from19925 canonical objects without translations.
Decoded object, side, line and direction codes against primary definitions;
upstream blanket artifact labels were not trusted. `000` is an unknown span, not
one missing sign. Printed drawings are normalized RTL even when original direction
is2; no extra reversal was applied. Selected primary checks agree with complete
exported lines, but this does not authenticate the whole export. A conservative
subset has1293 rows,1141 distinct strings and332 M codes. Adjacency dependence
persists beyond the position null; meanings remain unknown.
[Codebook](M77_CODEBOOK_REVIEW.md), [primary pilot](M77_EXPORT_PRIMARY_PILOT.md),
[corpus and selection limits](M77_CANDIDATE_CORPUS.md);
`scripts/prepare_m77_candidate.py`, `scripts/analyze_m77_candidate.py`.

### R10 — A second scan and missing-page search

Downloaded an alternative M77 scan and visually checked the table transition.
It also jumps from printed757 to760; missing758–759 were not recovered. The
public flipbook excerpt likewise did not supply them. Kept unresolved object-type
counts rather than substituting the following field-symbol table. The alternate
scan did help read a different inscription. [Scan review](M77_ALTERNATIVE_SCAN_REVIEW.md).

### R11 — Recovering omitted lines and correcting a glyph

Primary M77 reference2405 has seven displayed entries on six sides, with19 known
positions and two unknown spans: minimum21 positions, not a fully known length.
Recovered1001's second line as **M393**, correcting an earlier M317 identification
using the clearer scan and sign forms. The combined recovery preserves nine lines,
24 known positions,22 types and three unknown spans. Seven lines were absent from
the single-sequence export; boundaries and damage were retained.
[2405](M77_2405_RECOVERY.md), [1001 and correction](M77_1001_RECOVERY.md);
`scripts/verify_m77_recoveries.py`.

### R12 — Quantifying selection effects without inventing missing positions

Checked primary counting definitions: TableI counts individual lines and includes
doubtful legible signs; no explicit damaged-edge allocation algorithm was found.
M328's primary counts are323 total and274 final, versus49 total in the export.
Under an explicit injective-subset assumption,225–274 final occurrences must be
missing. Derived sharp bounds for every sign and tested the formulas exhaustively
on small cases. These are conditional accounting bounds, not evidence that the
subset assumption holds or a reconstruction of damaged lines.
[Definitions](M77_POSITION_COUNT_REVIEW.md), [proof](M77_OMISSION_BOUNDS.md);
`scripts/audit_m77_omissions.py`.

### R13 — Primary U-field transcription and paired-side contrasts

Parallel manual reviews of nine concordance pages recovered141 indexed U-bearing
groups and145 U instances. Of these,110 complete undoubted exact two-sign fields
have one/two/three preceding strokes in counts1/70/39. Loss, doubt and reviewer
unknowns remain separately marked; the selected pages are not a representative
corpus. A supplemental fourth-stroke witness was not added to that denominator.
References4548/4509/4508 share main M048 M342 M176 with two/three/four long strokes
before U on another side. Other matched main texts have two/three contrasts.
This rejects a deterministic main-text-only auxiliary count, but does not separate
quantities from unknown categories. [Combined results](M77_U_FIELDS.md),
[numeral pilot](M77_U_PILOT_NUMERALS.md), [structure pilot](M77_U_PILOT_STRUCTURE.md);
`scripts/build_m77_u_pilot_numerals.py`, `scripts/analyze_m77_u_fields.py`.

### R14 — Looking for counterexamples to a universal U quantity field

Checked primary solus, initial, medial and non-stroke U occurrences, including1206,
1532,4231,8202,4401 and5461, and preserved damaged cases separately. These prevent
making the simple stroke-plus-U field its universal context. Identical main texts
4373/4702 both have three strokes, so they were not claimed as a quantity contrast.
Unknown residual glyphs in repeated-U lines were not guessed.
[Counterexamples and locators](M77_U_COUNTEREXAMPLES.md).

### R15 — Testing repetition versus a stroke modifier

Screened all417 possible target codes for maximal repeated runs, both modifier
orders and exact surrounding strings. Enumerated other replacements too. The
complete-undoubted export has1520 distinct strings,102 runs and four graphic-count
matches; only one has nonempty outside context. Primary references4232 and1551
confirm a two-fish versus two-long-strokes-plus-fish alternation. The same frame
also accepts four short strokes plus fish and modified-fish plus fish (1019/2523),
so shared position is not an equality of quantities. Other matches have empty
frames and different object contexts. The subset's lack of triple U does not erase
primary repeated-U lines omitted from the export. [Full audit](REPETITION_EXPANSION.md);
`scripts/audit_repetition_expansion.py`.

Correction preserved: M104 is **four short strokes**, not the earlier pilot
description “five long.” The source sign image and primary sign list were checked,
the pilot builder and ledger corrected, and outputs regenerated. No M104 occurs
in the pilot observations, so its U counts did not change.

### R16 — Alternative explanations and independent archaeological anchors

Compared quantity, category, replication, allography, production-lot, date and
damage explanations. Deduplicating nine selected references leaves seven main/
auxiliary patterns and retains the two/three/four contrast. Duplication alone
does not explain it; production or date hypotheses require independent labels.
HARP sources discuss copied tablets, varied engravers, secondary deposits and
changing dating interpretations, but supplied no independently represented amount
for the exact target trio. Copy counts count artifacts, not the goods represented.
[Alternatives and falsifiers](M77_U_ALTERNATIVES.md),
[external-anchor review](M77_U_EXTERNAL_ANCHORS.md).

### R17 — Exact tablet photographs, materials and excavation joins

Recovered Vats plates, OCR, metadata and selected text pages. M77 AppendixV
explicitly supports4508→EH508→exc2568,4509→EH509→exc1280 and4548→EH548→exc2642.
All three are steatite;548 is oval and the other two rectangular. Preserved their
squares, depths and stated dimensions; depths in different squares do not order
manufacture. Photos support broad forms but not a common mold or fine tooling.
Candidate CISI IDs from the secondary export remain unverified. Training narrative
lengths5/16,3/8,7/16inch for two/three/four strokes suggested an exploratory size
rule, which was then frozen and tested below rather than accepted as a quantity
anchor. [Exact bridge](M77_U_ARTIFACT_BRIDGE.md);
`scripts/build_m77_u_artifact_bridge.py`.

### R18 — Prospective test of the tablet-length rule: failed

Froze `length_inches = (graphic_stroke_count + 3)/16` and five references before
targeted dimension lookup. This was internally prospective, not externally
registered or blinded. Read4476 first and saved its doubtful four-stroke prediction
at2026-09-23 18:13:27UTC. Recovered dimensions for all five without changing the
subset or formula. The decisive4405/EH405 predicts3/8inch, but its exact find2355
has table0.6inch and narrative5/8inch. The frozen rule fails under either source
representation. None of the five exact decimal values matches, but small residuals
may be rounding; damaged4403 and doubtful/broken4476 are not needed for rejection.
Preserved training fraction/decimal discrepancies too. This rejects the size rule,
not every numerical interpretation. [Result](M77_U_LENGTH_HOLDOUT.md),
`data/processed/m77_u_length_prediction_protocol.json`,
`data/processed/m77_u_length_holdout.json`, `scripts/check_m77_u_length_holdout.py`.

### R19 — Unsuccessful access, source handling and reproducibility

Recorded inaccessible official/Firestore, ICIT and ResearchGate routes without
bypassing denials. Some Harappa PDF requests returned403; bounded web-tool text
captures are explicitly JSON extracts, not original PDF downloads. A README-linked
Glossa PDF returned404; a differently named available version was archived with
its own identity. Some Vats archive volume/page metadata is wrong: actual content
and printed page numbers were checked visually. Unused discovery pages remain
saved, not silently deleted. The duplicate CISI scan is one volume repeated, not
two independent volumes. Source details and access limitations are in the linked
reviews and [source registry](../data/sources.json).

Processing issues were resolved without changing research observations: the earlier
test-module naming collision was fixed; PDF rendering was separated from whole-book
extraction to handle scanned sources; fontconfig output was controlled. The live
pipeline log was excluded from hash snapshots because it may still be written while
the manifest is generated. These are operational corrections, not scientific tests.

### R20 — Final integration and verification of this research phase

All417 supplied signs retain explicit unresolved meanings and sounds. Positive
structural evidence, negative predictions, source conflicts and per-sign coverage
remain separate. The latest complete offline run passed105 tests and every pipeline
step. Verified70 downloaded files, two bounded web captures and one archived HTTP
response; all persistent downloads are in `data/raw/`. No unregistered downloads
or stale file hashes remained after the manifest refresh. The locally written raw
README and archive-extracted license are not separate downloads.

Evidence: `results/latest_run.log`, `results/run_manifest.json`,
`scripts/run_all.py`, [project instructions](../README.md).

## 23 September 2026: explicit continuing-log request

The user requested a log of everything tried and its results. Retained the original
progress history, added the evidence index and retrospective entries above, and
made ongoing logging part of the project instructions. Backfill is distinguished
from contemporaneous records; no earlier timestamps or independent confirmations
were invented. This documentation update does not change any scientific result.

## 23 September 2026: foreign-findspot selection and primary glyph checks

Previous research turn classification: **progress**. A fixed tablet-length
prediction was rejected and retained; the explicit log request then caused the
earlier investigations to be backfilled. The next research question was whether
foreign inscriptions offer independent linguistic or semantic anchors.

Three authorized subagents separately reviewed primary findspot definitions,
artifact identities/context, and proposed external names. The parent specified
and computed a sequence comparison. An initial search assumption was corrected
before quantitative selection:8000-series references are Kalibangan, not foreign.
M77's explicit foreign list has12 named-site references and5 probable West Asian
attributions. It is not every integer in the9801–9905 range. All17 objects have
only-side code0;9845 has two lines, yielding18 primary lines across the list.
Sixteen objects are seals and9811 is a sealing. These are catalogue attributions,
not independent confirmation of manufacturing origin or language.

Primary-reviewed domestic selection uses the named major-site ranges plus33
explicit other-site references. Unknown-provenance9701 remains separate. On
printed160/PDF171, the four eligible target arrays were checked against primary
drawings and numbered sign forms. The parent reviewed9832/9846; the other reviewer
checked9801/9822. The short-stroke M102 in9822 was additionally checked against its
concordance entry, printed346/PDF357. Catalogue agreement does not authenticate
the original artifact or every exported transcription.

Evidence: [selection review](M77_FOREIGN_SELECTION.md),
[two-target glyph review](M77_FOREIGN_GLYPHS_AGENT.md),
`data/processed/m77_foreign_selection_review.json`,
`data/processed/m77_foreign_glyph_review_agent.json`,
`data/processed/m77_foreign_primary_parent_review.json`.

## 23 September 2026: fixed comparison of foreign and domestic seal strings

Saved the exploratory protocol before inspecting target strings and calculating
their scores. This was internally prospective, not externally registered or blind.
Kept seals with one export document, original direction1/2, at least two slots,
and no doubtful sign or unknown span. Already-normalized order was not reversed
for direction2. The rules admit9801/9822/9832/9846 from the named-site group; all
other foreign references remain visible with exclusions or probable provenance.

The domestic comparison has1175 records and1066 distinct strings. Exact target
strings are excluded globally from training; none has a domestic full-string match.
Scored internal adjacent-pair novelty and a fixed add-one417-sign transition model.
Each domestic control excludes its own complete string from training; controls
are matched by length. All control scores, pair counts and reversed diagnostics
are retained. The one-string training-size difference, remaining artifact
dependence, selected corpus and incomplete authentication are explicit limits.

Unseen adjacent pairs are5/7 for Susa9801,1/7 for Kish9822,4/4 for Ur9832 and4/4
for Ur9846. Their mean transition surprisals are8.481,6.369,8.713 and8.845 bits.
Among50 length-eight domestic controls,50 score below9801 and16 below9822.
Among228 length-five controls,220 score below9832 and226 below9846; six controls
also have every adjacent pair unseen. These are descriptive counts, not p-values.
Kish uses predominantly domestically attested combinations. The mixed result
does not support treating all foreign strings as one exceptional grammatical
system, and it identifies no language, word or sound. Reversed strings are only
diagnostics; no transcription was changed to improve model fit.

Evidence: [comparison](M77_FOREIGN_COMPARISON.md),
`data/processed/m77_foreign_comparison_protocol.json`,
`scripts/analyze_m77_foreign.py`, `tests/test_m77_foreign.py`,
`results/m77_foreign_comparison.json`. Six new tests check pair-boundary isolation,
full exclusion of repeated pairs, survival of shared pairs, damage/multiline
exclusions, probability normalization and reference ties.

## 23 September 2026: museum joins and external name-anchor audit

Recovered exact9801→Louvre SB2425 through its Delaporte publication entry and
9846→BM123208 through Gadd1932 no16. The Susa object is a cylinder seal; its
findspot alone does not establish an owner or linguistic content. The Ur object
came from PG1847 shaft fill, has damage, and the museum questions whether its
inscription is pseudo-script. Do not confuse its Mitchell1986 item2 citation with
Gadd1932 item2, the reference for9832; the latter's accession remains unresolved.
Langdon's Kish report warns of downward displacement, so the deep find is not a
secure early date. A nearby cuneiform pommel is a different object, not a parallel
translation. Bahrain/Failaka examples judged possible imitation remain separate
from the417-sign corpus. [Artifact review](FOREIGN_ARTIFACT_ANCHORS.md).

The name-anchor review distinguishes AO22310, the cuneiform seal of a Meluhha
interpreter, from an actual bilingual. Museum and CDLI period/language labels
differ and are retained as alternatives. BM120573/U7683 is Indus-style but has
cuneiform alone. Neither gives paired Indus values. The Lu-Sunzida translated-name
interpretation is inferential; the proposed Ur-du-du identification was explicitly
hypothetical. No proposed name was accepted as a deciphered Indus string.

CDLI P453801 / Nisaba15,0371 supplies a concrete follow-up: its record names
Meluhha-associated people and records an illegible seal. That seal has not been
identified as Indus or linked to one named person's inscription. Photograph review
is a test to pursue, not a bilingual already discovered. A candidate name key must
freeze spellings, segmentation and allowances and compare the entire candidate
pool; owner-name function cannot simply be assumed. [Name-anchor review](EXTERNAL_NAME_ANCHORS.md).

All new downloaded material remains in `data/raw/`: one official Louvre JSON and
two labeled web-tool captures. Captures are not original PDF/HTML files. The
registry now holds71 downloads,4 web captures and1 archived HTTP response, with
hashes and retrieval methods. No new ancient semantic or phonetic value follows.

## 23 September 2026: storage interruption, recovery and persistence

Disk-full errors interrupted new file writes, image rendering and even goal-status
updates over several continuation turns. Early turns still produced bounded
in-memory reviews and comparisons; later turns could make no further progress
without reliable storage. Attempts to mark the goal blocked also failed with
database/disk-full errors. Those tool failures did not change the goal to complete
or establish a scientific impasse.

Removed19 task-created temporary files only after confirming exact size and SHA256
matches to retained project copies, freeing20136663 bytes. Removed one failed,
truncated new PNG after verifying it could not be loaded. The three remaining
temporary images had no pixel-identical retained counterpart, so they were left
intact. No raw source or durable evidence was removed. Some primary pages were
reviewed by rendering JPEG directly to memory; source/page locators are retained
without claiming saved image files that do not exist.

Small writes intermittently recovered, allowing partial persistence. Later the
filesystem reported about12GB available, and integration resumed. Saved the pending
analysis, tests, comparison, source ledgers and reports, registered all new sources,
and restored this log. Source-selection and glyph-review consistency checks were
added to the new analysis. The complete offline pipeline then finished successfully
with111 passing tests, including the new foreign comparison. All new source hashes
were verified; no unregistered downloads or broken local links remained. The final
manifest was refreshed after this completion entry.

The objective remains unresolved: all417 signs have evidence assessments, but no
verified sound/meaning key covers them. The foreign context review narrows claimed
anchors and provides a specific new photograph lead; it does not substitute
structural compatibility for decipherment.

## 23 September 2026: P453801 seal-image and name-anchor follow-up

Previous goal turn classification: **progress**. Storage recovered, the foreign
comparison and external-name review were fully persisted, and111 tests passed.
The user confirmed the storage issue was handled and asked to continue.

Tested the concrete remaining lead: does the recorded seal on P453801 provide a
readable Indus string independently associated with a known name? The parent
retrieved current CDLI HTML/JSON and current/historical ATF exports. Parallel
reviews checked record identity and looked for the original published image.
Initial web-tool opens failed transiently; a normal public catalogue download
and subsequent linked opens succeeded. No access control was bypassed.

The primary handcopy was found through CDLI P453801 → BDTNS192941 → Owen,
Nisaba15/2 no.371. BDTNS explicitly credits the image to Owen/CDL Press. Both the
image reviewer and parent inspected it: two cuneiform tablet faces are drawn,
followed by the exact caption “Seal illegible.” No separate seal motif or sign
sequence is given. CDLI itself has a no-image placeholder. This does not classify
the actual seal's script, nor prove that a better photograph cannot exist. It
does show that the recovered published drawing supplies no readable Indus anchor.

The identity audit found two material complications. First, the2015 revision has
`na-na-za`/Nanaza; the current2017 revision has `na-na-sa3`/Nanasa. Both snapshots
are retained rather than pooled as unconstrained phonetic alternatives. Second,
P516366/CUSAS40,1582 may duplicate P453801/Nisaba15,371. BDTNS expressly attributes
that probable identification to Sigrist/Ozaki while warning of different year
names. CDLI's year6 and BDTNS's year8/boat formula remain unreconciled; no fresh
cuneiform collation or secure physical-object identity is claimed.

Both CDLI records link P533185/S999999, explicitly a dummy composite for
unidentified seals. It is not a matched physical seal or independent ownership
evidence. The text's recipients cannot automatically be equated with its sealer.
The catalogue's tablet-language label is not copied onto the unread seal.

Wrote a deterministic export audit: exact JSON/ATF identity checks; face/line
differences with damage and spelling retained; HTML image links; and exclusion of
generic seal links from shared-ID evidence. Four focused tests cover these failure
modes. No ancient sign values were assigned. The lead remains unresolved at the
seal-reading step; a better image or a separately identified repeat impression is
required before testing a fixed phonetic key against this tablet.

Evidence: [follow-up](P453801_FOLLOWUP.md), [identity audit](P453801_IDENTITY.md),
[image search](P453801_IMAGE_SEARCH.md), `scripts/audit_p453801_anchor.py`,
`tests/test_p453801_anchor.py`, `results/p453801_anchor_audit.json` and the linked
manual ledgers. Nine primary files and two bounded web captures were added, all in
`data/raw/`; the registry now contains80 downloads,6 captures and1 archived HTTP
response. Current and historical files have distinct URLs and hashes. The complete
offline pipeline finished successfully with115 passing tests. Primary ledger
hashes and sizes matched, every new download was registered, and updated local
links resolved. The final manifest was refreshed after this log entry.

## 23 September 2026: audit of the complete four-citation personal-name pool

Previous goal turn classification: **progress**. The P453801 lead yielded a
published handcopy and a corrected current name spelling; no readable Indus
pairing was established. The goal remains active and full decipherment unresolved.

Tested whether the remaining personal-name citations in Surdi/De Graef2025 note22
provide a usable external phonetic anchor. Fixed this finite selection after the
earlier two-record review and before results of the two remaining artifact checks.
The note's two village/granary examples are excluded from this personal-name test.
Its available web extraction was saved; no restricted full article was obtained.

Parallel agents authenticated CUSAS40/2,1354 and UCTIS099 while the parent built
an exact-export comparison and integrated the four records. UCTIS initially failed
ordinary search/CDLI abbreviation discovery, but BDTNS's own bibliography resolved
it to Basima Jalil Abid's2017 Arabic publication. Its exact catalogue record is
BDTNS205179, Iraq Museum IM226931, dateSS09-01-00. No CDLI P-number was exposed and
none was invented. The credited Abid handcopy was recovered and independently
viewed by agent and parent: two cuneiform faces, no separately drawn seal legend.
The catalogue explicitly says Seal=N. That is a catalogue assessment, not a new
physical autopsy of every surface.

P516138's official export preserves a partly readable seal: lost material, a
partially restored scribe title, and a patronymic with the name lost. No readable
Indus sequence or recipient-to-sealer identity is supplied. CDLI has no photograph
in its viewer and links the generic dummy seal already encountered in the other
records. A generated social-preview URL was not accepted as an available image.
The book preview supplied only limited front matter. Initial CDLI curl timeout
and web-export errors were followed by successful ordinary downloads; simultaneous
parent/agent JSON retrievals returned the same retained bytes, verified by hash.
The official ATF and JSON text match exactly. Metadata givesSS06.03.00, but the
year formula itself is damaged, so year6 is retained as metadata rather than a
fresh restoration.

All four records have the same basic1/1/half oil allotments and three-name pattern.
An early agent message tentatively called the UCTIS commodity different; this was
checked against the saved ATF and corrected before the final report. UCTIS lacks
the royal-offering/herdsmen clauses present in the other texts. Month/year and seal
differences are retained. Repeated recipients neither prove common ownership nor
allow merging physical tablets; the prior P453801/P516366 possible duplicate and
year conflict remain explicit. Current Nanasa and historical/UCTIS Nanaza readings
are not silently pooled as arbitrary phonetic alternatives.

Result: zero established externally attributed Indus name strings in this bounded
four-citation pool. Consequently no phonetic key was fitted or scored. This is a
failure to obtain eligible evidence, not a falsified name-reading hypothesis or
proof of universal absence. A separate Borrelli PDF request failed403 and saved no
PDF; no restricted source was bypassed. All searches, files and failures are in
the two agent ledgers and pool source capture.

Saved `docs/MELUHHA_NAME_POOL.md`, the two individual reviews, frozen selection,
record-input ledger, `scripts/audit_meluhha_name_pool.py`, output JSON and four
validity tests. The tests check identity mismatches, damaged/extended name tokens,
missing seal evidence, and recipient-versus-owner inference. Twelve downloaded
response files and four web captures were registered, all under `data/raw/`.
The source registry now holds92 downloads,10 captures and1 archived HTTP response.
Two session-dependent search pages are verified but not automatically refetched
from bare URLs. Full offline validation follows below.

Validation completed: the full offline pipeline exited successfully with119
passing tests. All103 registered files (92 downloads,10 captures,1 archived
response) matched both retained byte counts and hashes. No unregistered raw
download or broken link in the updated reports remained. The final manifest was
refreshed after this completion entry. No established Indus meaning or sound was
added; all417 sign dossiers continue to distinguish evidence coverage from a
demonstrated reading.

## 23 September 2026: complete primary M328 concordance recovery

Previous goal turn classification: **progress**. The four-citation external-name
audit resolved two remaining records, preserved a partial cuneiform seal legend,
and found no eligible Indus name pairing.119 tests passed; full decipherment was
not achieved. This phase returns to a known input defect that changes inferred
syntax: the export preserves only49 of the primary323 M328 occurrences.

Inspected the current omission analysis and existing141-line U pilot, then split
independent primary transcription across PDF585–587 and588–590. A third agent
audited safe promotion of the existing pilot and subsequently transcribed the
opening boundary on PDF575. The parent inspected the closing block through595.
The index begins with M328 partway through575 and changes to M329 after reference
7001 on595. All21 intervening pages were covered, not a subset selected for a
desired stroke pattern. Existing raw PDF and numbered sign-list images sufficed;
newly rendered pages and detail crops are derived artifacts, not downloads.

New material comprises17 boundary sightings,48 structure-agent sightings,50
iconography-agent sightings and67 parent sightings. Together with the earlier141,
these give323 R-column indexed occurrences. Deduplication by reference/side/line
produces313 lines across310 references. Repeated U occurrences retain distinct
token positions; for instance,4653/20 has three indexed listings of one three-U
line. Every U token in the merged lines has its own indexed sighting. The program
rejects repeated occurrence keys, conflicting full-line observations, invented
sign IDs and unresolved total/position mismatches.

The full reconstruction exactly reproduces Table I: solus1, initial19, medial29,
final274. Loss-free lines alone give1/17/26/268. Physical LOSS remains a positive
unknown-length span and is never deleted or converted to one glyph. This exact
match supports the adopted positional treatment for M328; it does not establish
all damaged-edge conventions for the other416 signs. The corpus contains21 lines
with source doubt,11 with loss,10 with unidentified visible glyphs, and274 fully
identified undoubted loss-free lines. These categories overlap.752 identified
tokens span59 M codes.227 undoubted exact two-sign fields contain one/two/three/four
long strokes before U, in counts1/70/107/49. Graphic counts remain uncalibrated
as ancient quantities or units.

The promotion review found that93 older rows inherit review status from a visual
transcription protocol rather than an explicit per-row flag. The new output
preserves that provenance distinction, source notes and completeness flags. It
also detects *UNKNOWN correctly by retaining the doubt marker separately from
the token base. Context-only lines are not promoted. Reference4316 had an explicit
candidate-derived prefix: independent reinspection confirmed six identities but
left the carrying-person glyph UNKNOWN with nearby inventory alternatives. A
separate correction ledger supersedes this row only in the new corpus; the
historical pilot remains intact.

Export disagreements prompted two further primary checks.2208's fish-like glyph
was corrected M059→M070 after enlargement revealed the inner vertical stroke.
4309/22's cross-like glyph was corrected M149→M141 after independent inspection of
both primary sightings showed straight vertical inner strokes. Neither correction
was made merely to match the export; source crops/coordinates, sign-list evidence,
old choices and correction history are preserved. Independent review also confirms
M345 (three internal ticks) on six jar-plus-U lines and the indexed positions of
repeated U signs on593–594. These reviews change neighboring glyph IDs, not U
counts or positional results.

All49 exported U tokens fall within the reviewed reference set.41 of45 U-positive
export records match a reviewed whole string exactly, accounting for45 U tokens.
The other four whole-string comparisons retain UNKNOWN neighbors rather than
borrowing their IDs from the export.265 references whose exported strings have no
U contain268 U occurrences on the reviewed primary lines. The per-reference sum
of missing-count lower bounds is274, conditional on correct reference identity
and injective exported U tokens. This localizes the aggregate deficit. Exact
string matching still does not establish side identity when the export omits it.

Saved the merged corpus, audit output, packaging/recovery scripts and five tests
covering repeated-index inflation, side identity, conflicts, uncertainty and
ambiguous string-to-line matching. The417-sign evidence index now includes a
separate reviewed-U-context count for each sign; original global/candidate counts
and null reading fields remain unchanged. The result constrains interpretations:
M328 is predominantly final but also initial, medial, solitary and repeated. A
universal terminal-only rule fails; a recurring short field remains compatible
with quantity or category notation without identifying a meaning.

Evidence: [complete recovery](M77_U_COMPLETE_RECOVERY.md), its four extension
ledgers, promotion review,4316 correction, independent crosschecks,
`scripts/recover_m77_u_concordance.py` and
`data/processed/m77_u_recovered_lines.jsonl`. No new downloads or semantic values.
Full offline validation follows below.

Validation completed: the entire offline pipeline exited successfully with124
passing tests. Primary-source and review-image hashes matched; the full323-entry
and positional checks passed; updated local links resolved; no unregistered raw
download was present. The rebuilt evidence index contains exactly417 unique sign
rows,752 reviewed-context tokens and323 for M328, with all semantic/phonetic values
still null. The final manifest was refreshed after this completion entry. The
goal remains active: complete M328 context recovery is not complete decipherment.


## 2026-09-23 — M328 object-type census from primary Texts

Question: does the recovered M328 position/short-field pattern vary with object
class? An exploratory candidate cross-tabulation was examined first and explicitly
recorded as such in m77_u_type_protocol.json. No preregistration or independent-trial
p-value is claimed. Four reviewers then directly checked object-type column5 for
all310 target references, divided61/142/100/7. Exact codes, source/page/image hashes
and uncertainty are preserved. All310 type digits are verified, with no candidate
classification disagreement. Reference ranges were selection partitions only,
never evidence of an object type. Several unusual codes and late miniature-tablet
entries make that distinction consequential.

Primary review located targets beyond initially expected page windows:4704/4718
onPDF139;5077on142; and the seven late references on157,160,164,166,168,169,170.
Parent discovery-only pages158,161,165,167 are retained. Agent reports record their
additional locator searches and resolved OCR errors. No new raw download.

The first integration run rejected metadata side/line consistency. Inspection of
the primary codebook showed that my parser had placed line at the third metadata
digit. Correct layout is type,side,field-symbol-two-digits,line,direction; line is
fifth. I corrected the parser, retained the agent literal codes, and added a test
using110012 so that field and line cannot be conflated. No source transcription or
object type was altered to make the join pass.

Results:16seals/19U,131sealings/140U,159miniaturetablets/160U,1pottery/1U,
2copper/2U,1ivory-or-bone/1U. Final-position counts are3,117,154,0,0,0 respectively,
summing274 and preserving all323 occurrences across313 distinct lines. The227
clear exact stroke-plus-U lines occur only on sealings(93) and miniaturetablets(134).
They collapse to four distinct strings; repetitions are not independent semantic
anchors. Loss-free and fully identified/undoubted restrictions preserve the main
association. Two-sign length matching does not force final U: seals4231/6109 have
[U M307]; sealings4363/5250 and tablet5484 have[U M059]. The latter shared string
also prevents an exclusive object-type explanation. A miniaturetablet-only final
rule fails on six occurrences, five even after strict uncertainty exclusion.

Saved primary type/line joins, full cross-tabs and counterexample list, script,
five tests, four review reports and docs/M77_U_OBJECT_TYPES.md. This reconstructs
one sign's object distribution from Texts; it does not recover missing TableIV
pages. Type association constrains viable formats without identifying semantics,
phonetics, language or real-world independent transactions. All417 reading fields
remain null; decipherment goal remains active. Full-pipeline validation pending.

Independent implementation review confirmed the aggregate counts and identified a
useful additional constraint: all227 exactstrokeUfields are on numbered side2/3
(sealing91/2,miniature125/9). The miniature134lines represent133references because
5413 has two. These quantities are now emitted by the script and included in the
report. Future unresolved type joins are explicitly listed as unclassified lines,
not silently borrowed from candidate metadata; currently there are none.

Validation completed: all129 tests pass and the full offline pipeline exited0.
The type join verifies68 input/evidence files, exact310-reference coverage and
313-line/323-U totals; no unresolved types or candidate type disagreements remain.
Updated local document links resolve. All103 registered raw files remain accounted
for with no unregistered downloads; no raw data were added in this phase. The
417-sign evidence index still has null semantic and phonetic values throughout.
Manifest refreshed after this completion entry. Next discriminating work is to
authenticate counterpart inscriptions for the short fields and compare graphic
count variation within identical main texts and object classes, with duplicate
impressions/molds retained as a possible dependence.


## 2026-09-23 — Complete selection for stroke-U counterpart recovery

The preceding goal turn made verified progress: a primary type census of310
references and the full offline129-test pass. The next test now selects all227
exact undoubted long-stroke+M328 fields, on226 references. Protocol saved before
new counterpart recovery; earlier nine matched-context examples remain acknowledged
prior knowledge. Three primary reviewers split76/76/74 references. They must
account for every other textual line on each reference and record symbol-only
entries separately. UNKNOWN, source doubt and positive unknown-length LOSS are
retained. The field selection is fixed and its input hash is pinned.

The parent implemented an exact relation audit: group separate positioned
counterpart lines with object type and selected-field side/line layout held fixed;
then inspect the tuple of graphic counts. One reference with two fields is one
multifield observation. A group with state counts n_j requires at least
sum(n_j)-max(n_j) reference exceptions to any single-valued mapping from those
inputs. This is a finite-data contradiction bound, not a population error estimate
or independent-trial test. Five tests cover duplicated or reused lines, uncertainty,
multifield references, type/layout stratification and the bound. Initial tests pass.

A diagnostic examination of the226 candidate export rows found188 with doc_count2,
36with3 and2with4;139distinct exported strings,21rows with unknown spans and23with
doubt flags. These are secondary discovery figures only and will not replace the
primary counterpart review. Some exports preserve the field rather than its mate.
The next analysis will crosscheck any newly reviewed U-bearing counterpart against
the previously complete U recovery, exposing conflicts rather than silently
selecting one version. No new downloads so far. Primary reviews are in progress.


Counterpart recovery completed for all226 selected references:237 other text-bearing
lines and28 symbol-only entries, with26 loss-bearing and23 doubtful lines (five
with both). Close image review resolved all visible counterpart glyphs, while
source doubt/loss remain; older U-bearing lines still retain UNKNOWN. There are763
assigned counterpart tokens across121 signs. The clean exact-bundle analysis
admits183 references/184fields, producing110 type/layout/context groups. Twelve
groups vary in stroke state (four sealing,eight miniaturetablet); four span2/3/4.
The variable groups contain64 references. The single-valued-map exception bound
is27 references (4sealing,23miniature), a finite observed-data result, not a
population estimate. The largest exact main[048342176] group has31references with
counts2:2,3:19,4:10. No numerical or lexical value follows.

Historical comparisons:70 prior context observations,57matches,9resolvedUNKNOWNs,
4changed glyphIDs. Second reviews confirm4359M178→402,4370M216→226,
5323M060→071,5410M178→402. All9 dedicated matched-context-review strings remain
unchanged. Independent carrying-person checks support4357/4404/4461M015 and4479M012.
A morphology explanation was reversed:012 lacks the detached inner-leg stroke,
013has it. Corrected explanatory notes at4353,4479,4489 without changing tokens.
All226 candidate strings match some assembled primary line; candidate suggestions
were disclosed and this is not a blind error-rate estimate or automatic side ID.

Combining all prior U lines and the new counterparts initially FAILED the primary
marginal bound: M280 appeared3times againstTableI2. This was substantive evidence,
not a reason to loosen the check. Parent inspectedTableI PDF732; agent+parent
compared3234/10,5325/20,4468/10, and parent located the glyph's own Concordance index
onPDF544–545 using localOCR only as a locator. Primary images confirm5325/20 and
4468/10 are M280.3234/10 has an extra right-edge enclosed cell and oblique internal
stem matchingM283; it is explicitly in the M283 index block (4165,2855,2851,3234),
not the two-entry M280 block. Corrected finalM280→M283, retaining leadingUNKNOWN.
This changes no U count, position or field selection. No frequency-forced guessing.

Versioning: saved m77_u_3234_primary_review.json with exact old/new strings and
historical/input evidence hashes. Earlier stage corpus/typed outputs and their
pinned selection provenance remain reproducible; the new combined authoritative
corpus applies this explicit correction while preserving its original value in
row provenance. The all-sign index now uses the corrected U counts. Reports link
the correction instead of silently rewriting historical primary-review claims.
The corrected union passes every sign's full-corpus marginal bound:550distinct
lines,1515assigned tokens,143observedtypes. This is83new counterpart types beyond
the old59-type U corpus plus the newly distinguishedM283, not143deciphered signs.

Saved scripts,6focusedtests, newcombinedcorpus, per-referencepairs, allcrosschecks,
results and docs/M77_U_COUNTERPARTS.md. All downloads remain together indata/raw;
none added inthisphase. Full offline validation follows. The decipherment goal
remains active; no established meaning or phonetic value has been assigned.

Validation completed: all135 tests pass; the full offline pipeline exits0. All
new source/image fingerprints and exact coverage checks pass, including the
previously failing combined marginal bound after the source-grounded correction.
Updated document links resolve. The source registry remains103rawfiles with no
unregistered downloads. All417 index rows remain unique with null semantic and
phonetic values; corrected U-context coverage is60types/752tokens and counterpart
coverage121types/763tokens, with143types in the deduplicated union. The final
manifest was refreshed after this entry. Full decipherment remains unresolved.


## 2026-09-23 — Independent mass/measure anchors after counterpart recovery

Previous turn was progress:237additional primary lines,12variable-context groups,
M280→M283correction,135tests passing. To distinguish quantity from arbitrary
categorylabels, opened a bounded search for inscriptions tied to independently
known physical amounts. Three parallel subtasks inspect originalHarappanstone
weight reports, Pettersson1999metaltools plusauthorerrata, and imported/Dilmun
weights withreadableexternalinscriptions. Parent checks Kenoyer2010.

Searches found officialINSAmetadata and authorerrata forPettersson; originals of
Hemmy/Marshallweightchapters; and Hafford/Einwag/OttoUrweightstudy. Speculative
modern dictionaryclaims and socialmedia translations were discoveryonly, not
acceptedvalues. Agents record their exactsourceURLs/hashes separately for later
centralregistrymerge; alldownloadsremain data/raw.

Parentcurl forpublicKenoyerPDF returnedHTTP403 (exit56); noPDFwascreated. Theweb
reader could access text, archived as kenoyer_2010_measuring_web_capture.json and
registered explicitly as webextraction, notPDFbytes. A PDF screenshot call returned
onlya citation handle to this toolintegration; no locally inspectable image, so
no visualtablevalidationclaimed. Metadata-inspection helper accidentallyprinted
stringcharacterindices; no researchdatawerealtered by that diagnostic mistake.

Kenoyer's twoKotDijiweight descriptions provide reportedmasses1.7g and102.95g,
but no Indusinscription on eitherweight in the inspecteddescription. Thefirst
is associated withseal/administrativematerial, which is not a same-object mark–mass
link. Thesecond waspossiblyreused ashammerstone/pestle. Table9.3weightdenominations
cannot automaticallybecome Indussignvalues. The two measuringrod/plaque descriptions
also do not supply a decipheredunitword. Saved boundedledger withlocators and
limits. Primary parallelchecks continue; no newreadingassigned.

### Weight-anchor outcomes and exact arithmetic audit

Three parallel reviews completed. Hemmy1931 explicitly reports no inscription or
value mark on the reviewed weights; Vats' measured examples and plate CXVIII did
not authenticate ancient signs. Visually checked originals corrected OCR masses
and object IDs (2652.8g,4368). Hemmy1938's promising four-/six-stroke examples
refer to Susa, with disputed Indus attribution and no exact IDs/depictions in the
excerpt. Saved INSCRIBED_WEIGHT_SEARCH.md and its source/evidence ledgers.

Ur2111, U.18699E and Bahrain520.TH were checked in published reports. The duck has
reported Mesopotamian numerical markings, not demonstrated Indus signs. UETV796
is a separate cuneiform tablet; it cannot label the Bahrain cube. Saved
DILMUN_WEIGHT_ANCHORS.md and three identified-object records. No direct Indus
sign/value join was found in these bounded cases; no global absence claim made.

Pettersson1999 supplies nine tool rows and five reported surviving masses. The
publisher PDF was downloaded after an initial network failure. Direct official
errata requests failed DNS/timed out twice; official indexed text was captured
and labeled as such. A DiVA anti-bot page was not bypassed. Parent independently
viewed pp92–94,98–101, including all nine rows and the proposed inequalities.
Local u/i/t variables remain separate from M77 IDs. Missing masses remain null.

Added exact Fraction-based audit_metal_weight_anchors.py. Seven times the tang
expression minus the axe expression gives29i+28t=-752.629 with precise reported
masses, or-755 with the paper's rounded masses: no nonnegative additive model
of these surviving masses. The paper already discusses this negative-value
problem; our result is an exact reproducible certificate, not claimed discovery.
Its reconstructed whole-chisel bound instead gives29i+28t<1093. Printed4/29 is
an algebra error for28/29, not listed in the retrieved indexed errata. Witht=i,
i<1093/57, u>4872/19 andu/i>14616/1093. Preserved strictness and distinguished
rounded masses from precision sensitivity; no statistical error bars invented.

Additional three-object check uses disputed6i=262g onDK7855: combined with the
axe it forces originalchisel>=9529/21=453.761905g, exceeding429g. Independent
agent derived the same result and precise-mass sensitivity. Pettersson already
notes conflict onp101; the new artifact quantifies its dependency on segmentation
and reconstruction. Ratiosu/i=8,10,16 witht=i needp=3.1740,2.8939,2.4525;
compatibility of16 with the two-object bound is not evidence ofbase16.

Kalibangan alternatives were solved without selecting a preferred reading:
u/i=75/68,75/34,7/34 on two objects. Assuming500g rather than reported476g
creates a10:1 relation; that24g is not an observation or held-out prediction.
The new summary WEIGHT_ANCHORS.md links all reports, exact results and provenance.
Four meaningful tests pass, covering an impossible pair plus a feasible control,
strict boundary, precision/base sensitivity, and the third-object conflict.

Merged nine newly retained agent artifacts into the central source registry,
after byte-count/SHA verification; including earlier Kenoyer capture, this phase
adds ten raw artifacts. Registry now has100downloads,12webcaptures and1HTTP
archive=113files. No unregistered raw downloads. Full pipeline validation follows.
The goal remains active and unmet; no semantic or phonetic value is promoted.

Full validation completed:139 tests passed and the entire offline pipeline exited0.
All113registered rawfiles verified;39nested evidence fingerprints in the four
new review ledgers verified; new report/README links resolve. The all-sign index
still contains417rows with null semantic/phonetic values. Every code, processed
data and result checksum in the completed run manifest matched. Refreshed the
manifest once more after recording this result. No decipherment is claimed.

## 2026-09-23 — Tool photographs and original-record verification

Previous goal turn classified as progress: original sources, exact arithmetic
correction, three-object inconsistency,139passingtests. Next evidential bottleneck
is authentication of the expressions and artifact masses. Parallel tasks opened
for originalMackaytext, MohenjodaroCISIphotographs, and internal numeral conventions;
parent checksKalibangan. Photoagent's first turn ended with streamdisconnect;
authoritative terminalerror received, then same bounded task resumed.

Parent renderedCISI1PDF361/362 (printed325/326) and provisionaldata-page candidates
412/413. PDF412 is map rather than catalogue; no catalogue claim based on it.
K122B visiblyhas five strokes in enlargement; K121B contains unlike shapes rather
than a clean repeatedUU sequence. Photo appears highlighted; reading must remain
qualified. Search found officialNMMArecords1391408chisel210.59g and1391390axe476.70g,
withmatching general descriptions; exactIDjoin still underreview. Webresponse
saved as metal_kalibangan_nmma_web_capture.json, notoriginalHTML. DirectNMMAcurl
failedDNS in sandbox; publicread retried withnetworkpermission, bounded45seconds.

### Original records, photographs and catalogue discrepancies

OriginalMackay audit completed from bounded archive metadata/OCR/page-map plus
five pageimages (eight downloads total). Printedp454 confirms165.343g tang,
1910.030g largeaxe and262.233g smallaxe. Printedp489 gives commoncontext and
plateCXXVI2/3/5 joins. Largeaxe fieldnumber reads7535, conflicting with later
Pettersson7835. Parent independently inspected fullp454 and catalogue crops,
confirming the7535conflict; tangfielddigit remains blurqualified. The primary
metric decimals accompany imperial values and are not milligram precision claims.
Parent also viewed the smallfractioncrop: largeaxe looks4lb3⅛oz, which conflicts
with metric1910.030g; possiblefraction/printingambiguity preserved without repair.

Printedp473 originalchisel length>15in is an author reconstruction. Dividing by
5.22in surviving length gives>2.874lengthratio, not a measuredmassratio. Chemical
bath losses are explicit and unquantified. The later2.6massupperfactor cannot be
upgraded to an excavationmeasurement. New precise262.233g sensitivity retains
three-object contradiction under the same hypothetical expressions and2.6bound:
chisel>=453.927071g,ratio>=2.745366. HistoricalPetterssonmodel unchanged.

Parent downloaded official2020KalibanganPartII,13,694,349bytes, after webreader
rejected its size. ReviewedCISI1printed325/326photos and374catalogue; M77printed
158/159texts and828appendix;2020reportprinted769–771photos/entry. Exactjoins:
K121=Finnish7080=exc16948=M77ref8302; K122=Finnish7081=exc14983=M77ref8301.
IDs are artifact/textreferences, notsignIDs. K122B hasfivevisiblestrokes. K121B
has unlike upperbent/lowerarch forms, withhighlighting anddamage; its proposed
2u/1u/u+2i readings remainunresolved. M77stacked-arcs depiction retained separately.
Repeatedphotos/publications are not independentancientsamples.

OfficialNMMAindexed chisel210.59g andaxe476.70g closelymatch descriptions, but
oldexcavationnumbers andimagejoins absent. Directnetworkcurl timedout45seconds;
noHTMLbytescreated. Savedtwo explicitlylabeled indexedtextcaptures. Matchesremain
probable, notexact. Newfraction-based sensitivityreports threeconditionalu/i
ratios1.104416,2.208832,0.208832. Noindependentreweighing ordatingdemonstrated.

The Mohenjo-photo agent failed twice with confirmedstreamdisconnect terminal
errors; the numeral-identifiability agent failed twice after an intermediate
argument but before saving a completed artifact. No process was silentlyrestarted
while live; resumed only terminalfailedagents. Preliminaryinternalconventionlead:
maximumseven repetitions alone cannot select baseeight without assumptions about
carrying and samplecoverage; mixeddenominations may alsofit. This was not promoted
to a verified newresult or saved as a completedagentreport. Mohenjoplateglyph
verification and a fullyreproduced conventiontest remainfuturework.

Saved TOOL_RECORD_FOLLOWUP.md, originalreport, bothstructuredreviews, follow-up
script and JSON, and updatedmainreports/sourceguide. Parent sourceledger and
agentdownloadsmergedafterSHA/sizeverification:124rawfiles=109downloads+14web
captures+1HTTParchive; noneunregistered. All newdownloads remain data/raw.

## 2026-09-24 — Follow-up consolidation and validation

Resumed activegoal after date/context update; preceding work is progress, not
blocked: newprimaryrecords, authenticatedKalibanganjoins andanunresolvedIDconflict
change the nexttest. Script now reads all primarymasses from the saved original
ledger and verifies bothreviewevidence sets, rather than hardcodingnewobservations.
No newunit-testcountclaimed: existingexactarithmetictests cover the reused bound
function; newdata are checked by hash and explicitprovenance audits. Full offline
pipeline validation follows. All417meaning/soundassignments remainunresolved.

Validation completed: fullofflinepipeline exits0; all139tests pass. Verified41
nested source/image fingerprints across the two newreviewledgers and allreport
links. All124registeredrawfiles passedverification. Runmanifest hashes match
code/docs/results/processeddata andsource registry. All417signindexrows retain
nullsemantic/phoneticvalues. Refreshedmanifest afterthisentry. Full decipherment
is not achieved; nextwork remains primaryglyphauthentication and discriminating
numericalconventions rather than additional fittedweights.

## 2026-09-24 — Original plate counts and numerical identifiability

Continued the active goal with two distinct tasks: recovering the original tool
illustrations and testing whether the proposed counts identify a base. The plate
subagent completed its audit and saved eight downloads (6,083,064 bytes), all in
data/raw. Parent verified byte counts and SHA256 before merging them into the
central registry: 117 downloads + 14 web captures + 1 HTTP archive = 132 files.
CXXVI drawings, CXXXI photographs and the plate list are retained separately.

Published drawings support the tang's one arch/five upright/four transverse
strokes, the small axe's six uprights and the large axe's seven arches/six strokes.
Parent independently viewed the full drawing and three crops; the small axe's
adjoining angular sign makes numerical segmentation uncertain. This was not a
blinded review. Photographs are corroded and do not provide independent reliable
counts; individual photographic joins remain tentative. The 7535/7835 catalogue
conflict remains unresolved. Plate metadata says1937; no new title-page check.

Parent inspected the numeral discussion on Pettersson printed pp.101–108,
including six new renders for103–108. Rendering completed successfully; harmless
font-cache warnings were retained. The analytical nine-expression table is checked
against the existing ledger, not promoted to nine newly verified artifact readings.

New exact-fraction script audit_metal_numeral_conventions.py proves that canonical
integer carrying with uniform denominations permits exactly all integer bases R≥8
for these counts. It constructs bases8/9/10/12 and mixed ratios8/10/10. The latter
satisfies4t=i/2 without u/i=8. No probability for absent eight/nine counts is claimed.
The rounded large-axe/chisel pair and hypothetical2.6 bound permit all R≥8: the
required ratio is decreasing and already below2.6 at8. This assumes i/t=R,
whereas the previous base-ten failure assumed t=i; the distinction is explicit.

The two surviving axe masses imply u/i=3295594/611877≈5.386040. Even these two
expressions alone require integer u/i≥7 under canonical carrying, predicting
large mass≥2403.8025g against1910.030g. The full expression set requires≥8,
predicting≥2709.741g. Neither contradiction needs chisel geometry. Shared units,
complete proposed expressions and surviving-mass interpretation remain assumptions.

A general free-loss proof shows why arbitrary original-mass corrections cannot
select a base: for positive quantities q_j and masses m_j, choose scale
s=max(m_j/q_j), then L_j=s*q_j−m_j≥0 fits every object. Saved examples for bases8
and10 use five masses, explicitly as overfitting demonstrations, not damage
estimates. This demonstration does not impose the2.6 geometry bound.

A second subagent independently reviewed the proofs, source fingerprints and five
focused tests. It confirmed the substantive results but caught a helper-label
issue: satisfying a ratio lower bound alone does not enforce an integer ratio.
Parent corrected axes_constraint to expose both conditions and require both for
compatibility; added the reviewer’s ratio8.5 counterexample to the existing test.
No current archaeological conclusion changed. The review and its resolution are
preserved separately. Main report, source guide and earlier follow-up links updated.
Full pipeline and final provenance validation follow. No established sign value
has been added; the decipherment goal remains unmet and active.

Final validation for this phase: offline scripts/run_all.py exited0 and all144
tests passed (139 previous + five new). The independent reviewer rechecked the
integer-ratio fix and appended its resolution. All132 registered raw files have
matching hashes and byte counts where recorded; no unregistered downloads remain.
Links in the six updated main/source reports resolve. Generated run-manifest hashes
match all recorded code/docs, processed data, results and the source registry.
All417 sign-evidence rows retain null semantic and phonetic values. Refreshed the
manifest after this log entry. Next discriminating work needs independent quantity
anchors or independently bounded damage, not further unconstrained fits to these
same masses. The full decipherment objective remains unmet.

## 2026-09-24 — Independent contents and sealing-context search

Previous goal turn classified as progress: numeral proofs, source registration,
review correction and144 passing tests changed the next action. Continued with
physical container traces and laboratory residue evidence rather than more free
mass fitting. Two bounded agents were assigned primary residue/sample joins and
complete Lothal Table1 recovery; parent reviewed physical-use evidence.

Search located Frenez/Tosi2005 author deposit doi10.5281/zenodo.5514283, rather
than relying on later interpretive claims about taxation. WebPDF fetch timed out.
First download permission review timed out without decision; one retry, explicitly
permitted by the tool, succeeded. No safety refusal was inferred from timeout.
Saved1,931,287bytes as data/raw/sealing_frenez_tosi_2005.pdf; source MD5 and local
SHA256 verified and registered. Extracted41pages using existing PDF helper.
Parent viewed printed71/72/78/79/80/81/82/84 and Figures6/7 at101/102, preserving
hypotheses about bags, wood and closures separately from visible surface traces.
Additional renders are retained without claiming every one was visually reviewed.

Source reports its most recurrent stamp on16 impressions; parent ledger retains
only10 specifically listed sealing objects, not a fabricated complete inventory.
Selected source interpretations cross pottery/wood/bag/structure/peg closure domains.
An exact exclusive-container-label hypothesis fails conditional on those identities
and interpretations. In the three single-impression examples L124/125/126,
allowing L125 pottery alternative still leaves no shared category; dropping the
uncertain leather interpretation altogether restores a pottery possibility. New
script/tests preserve unknowns as unconstrained, not false counterexamples.
This does not reject commodities across containers, names, authorities or mixed
texts and does not assign individual sign values.

L161–172 report one four-sign elephant stamp, separately added fingernail marks
up to six and no preserved marks on L165/170 (possible damage). Parent inspected
Figure6 but did not create a complete tally transcription. Twelve sealings do not
establish twelve different boxes or independently known quantities. Contents
remain unknown. Stable stamped information plus ancillary variation is compatible
with the evidence; specific numerical or administrative semantics are not selected.

Complete Table1 recovered all93rows by agent, with parent checking both renders.
Table context counts W35/W1 18/W2 11/O10/?19 differ from proseO11/?17. W1 is
inferred using recurrent seal identity, so is unsuitable as independent evidence
for stamp-to-warehouse association. W-only and inferred-group results are separate.
Agent's initial render command failed filename validation (exit2), then corrected
without a download. Table133impressions also differs from prose130; item-level
and aggregate discrepancies are being preserved rather than silently reconciled.

Additional discovery leads: Mukhopadhyay2023 DOI10.1057/s41599-023-02320-7 asserts
semantic taxation/licensing interpretations; these are hypotheses, not physical
contents identifications. Frenez2024 DOI10.1080/02666030.2024.2401206 revisits
administrative archives; publisher/author webtext found, but this phase's quantitative
ledger is explicitly the2005table, not a claimed2024 update. Searches for ivory
scales did not yet yield a sign/value bridge. Residue-agent findings pending.

Table follow-up completed:133=62single+71impressions on31multi-impression objects
versus prose130=63+67. L174 has one impression in the table but two in prose;
changing that row alone would increase the total to134, not repair130. L209 is
W2 in the table but called not contextualized in prose; general-area versus exact
findspot precision may explain that difference. Parent and agent separately viewed
the relevant prose/table pages. All original cells retained. Main report and
hypothesis/source guides updated. Focused domain tests and current full unit suite
pass147tests (three added); full offline pipeline follows after residue-source merge.

Residue audit completed. Suryanarayan2021 mainpaper reports172fragments; recovered
CSV124rows comprise122archaeological records from seven sites and two modern
comparators, not the full172inventory. Agent viewed all24photographic SI3 pages
at1500pixels; eighteen nonphotographic pages were text-extracted only. No secure
script sequence established. FRN24 bands and FRN27 decoration remain candidates
for better photography, not readings. Parent separately viewed SI3pages27/29.

Ghosh2025 (onlineDecember2024) has9Karanpura+6Ropar sample rows; oneRopar sample
is post-Gupta, notHarappan. Figure3 RPR62 is perforated butSI2 calls it cookingpot.
SI3 also changes several KRNidentifiers for otherwise matching fields; no identity
repair is made. KRN15/RPR153 incisions are decorative groove patterns in the
reviewed image, withNAcomposition/yield fields. Parent checked Figure3 andSI2text.
Site-level mentions of inscriptions do not join those inscriptions to lab samples.
No authenticated inscription-to-content link was established in these two studies.

Agent saved11records,11,608,902bytes:9downloads,1boundedwebcapture and1HTTP
interstitial. Parent verified every byte count/SHA and merged by record_type.
Currentregistry144files=127downloads+15webcaptures+2HTTPresponses, all data/raw.
Recorded failures include initial sandboxDNS, browser-check/interstitial responses,
403/404fetches and unavailable optionalBeautifulSoup; permitted public retrieval
and standard-library parsing resolved the actionable cases. No inaccessiblecontent
was treated as read. Agent report preserves complete failure/scope details.

Three new offline analyses integrated: sealing-function domain sensitivity,
complete93-row Lothal table and residue sample metadata. Residue script now also
verifies all manual-review evidence fingerprints and records reviewhash. An earlier
fullpipeline completed147tests while the residue review was finishing; final full
run is repeated because the new residue analysis and sources have since been added.
This is research progress; all417 semantic/phonetic values remain unestablished.

Final validation: current full offline pipeline exited0, all147tests passed, and
all three new audit scripts ran before final manifest generation. Verified all144
raw source records and50evidence fingerprints across the three new reviewledgers;
no unregistered downloads remain. All updated report links resolve. Manifest
hashes match recorded code/docs, processed data, results and source registry.
All417 sign-evidence rows retain null semantic and phonetic values. Refreshing
manifest after this entry. This phase gives source-grounded function constraints
and bounded negative anchor searches, not a decipherment. New independent
inscription/content or inscription/value evidence remains the discriminating need;
the goal remains active and unmet.

## 2026-09-24 — Umma object identities and possible cuneiform anchors

Parent followed a modern SAHI Tell Jokha find lead while subagent
umma_old_identity audited the older Scheil1925 clay tag. Aim: seek an independent
inscription-to-readable-text or inscription-to-contents anchor, without joining
objects merely because both are called Umma. No new semantic key was assumed.

Modern lead: two duplicate June2026 Reddit posts identify TJ17-PRO-S56 and quote
the2017report p59 Fig6.61 as a surface find, seal or impression. They propose a
180degree rotation. These remain discovery claims: exact primary page and image
were not retrieved. Parent did not rotate or transcribe the unavailable image.
Frenez2023 author webtext independently distinguishes old Fig3E and new Fig3D,
cites the2017report p59Fig6.61, and calls the latter an excavated square seal.
Its wording is insufficient to establish stratification or settle object type.

Parent successfully downloaded the original IAA2021 project account. Body credits
director DrahoslavHulínek; publisher metadata names StefaniaErmidoro. It explicitly
reports Harappan impressions in topographic survey, without individual IDs.
Separately it describes TJ19-2A-K54-T1, a Trench2A Sumerian field-sale tablet dated
EDIIIb2550/2540–2350BC. No shared physical object, seal impression, owner identity
or parallel wording connects that contract to either Indus case. Site association
does not identify the Indus text as the personal names in the contract.

Retrieval limits: SAHI2017landing timeout45s; ResearchGate extracted malformed
download link404; corrected directPDF403 and webcachemiss. Academia public
extraction exposes front matter/contents only; directHTML403, download cachemiss,
auto-download variant failed. DirectHarappa review page and comparisonfigure403.
Searches by report title,ISBN,exactinventoryID and Harappan/survey phrases found
bibliographic corroboration but no recovered primarybody. Frontmatter chapter
starts53/61 differ from bibliographic54–61/62–63; no pagination offset imposed.
No primaryPDF or modernobjectimage is represented as downloaded/read.

Older audit: Parpola1994 p113/PDF131Fig7.16 visually identifies Ashmolean1931.120;
parent separately viewed that page. Both faces support Indus inscription/unicorn
and reverseclothtrace. Tosi account quoted onHarappa reports Louvre dealer
acquisition beforeWWI and Ashmoleantransfer1931 with unconfirmedJhoka findspot.
Jar-mouth/string reconstruction does not establish contents, cottonfiber or mass.
OriginalScheil article located bibliographically as RA22(2),1925,55–56,JSTOR23290782,
but itsPDFrequest yielded a challenge. Officialmuseumaccession record not recovered.
Four IAsearches failed to locate originalarticle. UnrelatedmuseumprismEAMd.13 rejected.

Agent follow-up directly checked M77reference9811 printed160/PDF171 and signlist
32/33/35: five unitsM029–M336–M099–M104–M162 match the candidateexport.
ComplexM029/M336 each count as one catalogueunit. Tosi's reportedsix remains
unexplained; neither a definite separate sixth glyph nor its absence can be
established from the halftonedphoto. Apparentphoto arrangement differs fromM77
normalizedrow; no token or direction changed. Frenez2023 also reportsfive, but
that agreement does not resolve why theTosiaccount sayssix. Agent retained all
render/crop/sourcefingerprints; no newdownload on this follow-up.

Saved docs/UMMA_ANCHOR_AUDIT.md, UMMA_OLDER_SEALING_IDENTITY.md, two structured
reviews and source proposals. New scripts preserve olderledger generation and
offline parent source-paragraph/provenance validation. run_all.py includes newaudit.
Registered13newrecords19,295,090bytes after verifying every hash/length:
6downloads+5boundedwebcaptures+2archivedHTTPresponses. Current157totalrecords:
133downloads+20captures+4HTTPresponses, all in data/raw; no unregisteredfiles.
This is a bounded negative anchor search and a positive catalogue-segmentation
verification, not decipherment. All417 signvalues remain unestablished.

Final validation: full offline pipeline exited0 with all147tests passing. New
Umma audit ran successfully. Parent also viewed the M77 9811 row crop; the five
graphic groups agree with the agent's count. Verified all157rawrecords, all29
fingerprints across the two new reviews, and both new reports' local links.
Manifest matched code/docs, processed data, outputs and source registry; all417
semantic/phonetic values remain null. Refreshing manifest after this entry.
Goal remains active and incomplete; these findings restrict unsupported joins
and improve transcription provenance without establishing a reading.

## 2026-09-24 — Hybrid seals and a literal patronymic-chain test

Previous goal turn classified as progress: Umma source identity and a primary
five-unit segmentation were verified. This turn followed a different route:
readable cuneiform on Indus-style seals, then a concrete predicted pattern for
personal names and descent. Parent audited the Paris case; cuneiform_bm_seal
checked BM120573; patronymic_test_design tested the proposed pattern independently.

Downloaded Vidale2005 from DAI (13PDFpages, printed147–158 plus cover). Parent
viewed printed151,152,153,156 (PDF6,7,8,11). Paris Cabinet desMedailles seal is
reported bought in Beirut; Lebanese/Syrian origin remains conjectural. Vidale
attributes preliminary Ur.dNin.Ildum dumu Ur.gi7 to Glassner2002 p361 n215.
Personal designation/patronymic interpretations have alternatives; carpenter-deity
association does not establish timber cargo, owner occupation or an Indus value.
No current official accession record, original Glassner chapter, or examined
Paris artifact photo recovered. BnF indexed searches returned unrelated Gudea
and administrative tablets; these were rejected. Secondary online rebus claims
were treated as leads, not translations.

Vidale2004 originalPDF web reader succeeded; directdownload403 yielded no file.
A bounded web capture retains attributed reading and explicit limits. Searches
by exacttitle, deity-name variants and Glassner bibliography did not recover
the original footnote. The author's public university CV downloaded successfully;
its own date is10July2024. PDFp7 labels HybridIdentities as in preparation,
while earlier pages list2014talks. Frenez2023 cites a2014conference presentation.
These source statuses do not prove that a later article is absent; none was
recovered in this search. The CV and paper text extracts are reproducible.

BM120573: directmuseumweb/curl403; Gaddwebreadtimeout but authorizeddownload
succeeded (44pages,3,152,198bytes). Text layer unhelpful; page-marker extraction
retained and Poppler/Tesseract used for navigation. Agent viewed originalpp5–6,
PlateI and reused Parpola1994 p131; parent independently viewed Gaddp6 and
Parpolap131. Gadd lists SAG(K)/KA, KU/possibleLU, nearlycertainŠI, uncertain
possiblefourth; provisional sak-ku-ši--. Meaning unknown. Parpola insteadlists
šak/ka,ku/ma,ši/ba and speculative names. Some onlineversions mix sources and
replaceši withzi; they are not faithful quotations. Museum'sSumerian label is
not a demonstrated reading or knowntextlanguage. NoInduscounterpart exists in
the reviewedobject. Newphotographicrender supports modernregistration1928,1009.56.
Gaddp6 also identifies no2 asBM122187, a useful separate futurejoin lead.

Patronymic proposal: Vidale2005p156 suggests A D B / B D C as a futurefamily
sequence test. Agent matched plainhuman Fig5 to primaryM001 but did not force
an unresolvedtwins or fullvariant-family mapping. Reused existing seal-only
eligibility:1175domesticcandidate records/1066unique strings; fournamedforeign
andthreeprobableforeign strings, nonewithM001. Foreign17object/18printedline
catalogue is not an18linecomplete exportedcorpus. Damaged9833/9845 and
probable9902 are retained in inventory but excluded by statedfilters.

M001 occurs44records/43strings:37final,5internal,1repeated. Fiveexactfull-flank
internalparses yield zerochains. Prefix/suffix constructions, multisignmarkers,
variants, phoneticchanges and damagedtexts are outside this narrowtest.
All417delimiter controls:229permitinternal splits; sixyieldtenchainpairs
(M017,M028,M098,M099,M180,M336). These are descriptive controls, no p-values
or semanticassignments. Onepositivepair1038→2105 undergoingprimarycheck.

Proof: for edgeA→B, totalorderedtwo-edgewalks including selfpairings is
T=sum_x R(x)L(x). Re-pairingendpoints with unchangedmarginals leavesTinvariant;
excludingthesameedge changesonlyselfloopcontribution. Three-edgecycle versus
three-selfloop unitcase confirms this. Such anullcannotdistinguishkinship.
Tests also guardwholeflankmatching and exclusionofempty/repeateddelimiters.
This proof concerns thisspecificstatistic/null, not every possible genealogicaltest.

Saved HYBRID_SEAL_SEMANTICS.md, BM120573_CUNEIFORM_AUDIT.md,
PATRONYMIC_TEST_DESIGN.md; sourceledgers, computation, all417controls andtests.
Integrated sourceaudit andchaintest into run_all.py. Initialcentral-docspatch
failedatomically on an unmatchedheading; verifiednofilechanges and reapplied
correctedpatch. Source registrymergedfourverifiednewrecords7,389,069bytes:
threedownloads andonewebcapture. Current161records=136downloads+21captures+
4archivedHTTPresponses, all data/raw; no unregisteredfiles. Fullvalidation
willfollow after primarypaircheck. No signmeaning or phoneticvalue established.

Primary positive control completed: M77 1038 printed40/PDF51 is
M244 M017 M336;2105 printed61/PDF72 is M336 M017 M402. Both metadata100101,
complete rows with no doubt/loss/continuation. Agent checked labelled signlist
32/34/35. Nine source/image fingerprints and crop reproduction saved in
data/processed/patronymic_primary_pair_review.json; no new downloads. Initial
page46view failed while rendering was still writing; confirmed completion then
viewed successfully. Script now checks these pinned sources and candidate rows
and reproduces exactly one M017 chain. This improves primary support for an
abstract pattern but supplies no named persons or kinship relation. Three new
boundary/invariance tests pass. Full offline validation follows.

Validation completed on continuation: the already-running full offline pipeline
exited successfully with 150 tests. Parent also viewed both primary control-row
crops. All 161 registered files passed byte-count/SHA-256 verification; all 417
semantic and phonetic values remain null. The goal remains active and unmet.

## 2026-09-24 — endpoint relation templates and a second Ur seal

Continued the patronymic test because the internal-only parser excludes the
dominant final position of M001. Before inspecting these new counts, specified
prefix D A B, internal A D B, and suffix A B D with exactly one marker; two
nonempty complete bundles; all possible endpoint-template boundaries; distinct
whole strings only. Reused the same domestic eligibility and deduplication.
No variants, approximate matches or mixed-placement chains introduced.
Delegated independent method review to terminal_relation_review and primary
Gadd no.2/BM122187 identity/context audit to bm122187_followup. These are bounded
extensions of the previous findings, not new proposed decipherments.

Implemented scripts/audit_relation_templates.py and four scientific-boundary
tests. Initial execution passed all four. The 1,175 candidate records yield
1,066 unique strings. M001: no prefix examples; five internal parses; 36 eligible
suffix strings supplying 131 alternative splits; no chains in any template.
The earlier 37 final strings include one two-sign string that cannot contain
two nonempty name bundles. All 36 eligible suffix strings have multiple possible
boundaries; none is authenticated as a word boundary. Alternative splits of one
string cannot chain to that same string, including when source references differ.

All 417 codes screened per template. Prefix:186 eligible markers,16 with chains,
130 parse witnesses across129 distinct ordered string pairs. Internal:229,6,10,10,
reproducing the earlier result. Suffix:99,13,1002,1002. Counts are descriptive and
frequency/opportunity-confounded. A boundary overlap is not a person identity;
zero chains do not establish absence of kinship. Results retained in
results/relation_template_audit.json. Independent review and final validation
will follow; no new semantic or phonetic assignment.

Independent review found no defect in the invoked per-marker/template workflow.
It proved terminal matching is a proper suffix-prefix overlap, established global
reversal symmetry, and demonstrated pairwise matches with incompatible cuts in
their shared middle string. The countermodel of all two-field classification
labels gives q^3-q chains without kinship. Review saved in
docs/TERMINAL_RELATION_METHOD_REVIEW.md. Added two meaningful checks: four parse
matches versus two string pairs for aaaD/aaaaD, and exhaustive agreement with an
independent overlap oracle over binary bodies of length2–4. All six new tests pass.
Persisted every eligible M001 parse/reference for audit; reference1288 is the
excluded short final string M028 M001. M342 contributes894 suffix pairs but has393
eligible strings/1395parses, so its raw count is not semantic evidence. Saved
docs/RELATION_TEMPLATE_RESULTS.md and linked central reports. No downloads used.

BM122187 follow-up completed: original Gadd1932 no2, printed6–7/PDF13,16 and
PlateI, joins through M77 AppendixV printed829/PDF838 to9832. Re-viewed primary
row printed160/PDF171 and retained existing parent-verified sequence
M254 M074 M297 M184 M003, metadata100401. Gadd explicitly says obtained at Ur
in1928–29 but precise findspot unknown. No independently known owner, commodity,
associated cuneiform or semantic value. Parent independently viewed Gaddpp6–7
and M77p829 in this continuation and confirmed both identity and limitation.

Agent searched exact museum number and registration variants. Many hits conflated
nearby objects; no identities transferred. An indexed exhibition catalogue offers
candidate1929,1017.725 without big-number confirmation; original page not viewed
and candidate official museum URL403. Neighbor1929,1017.726/BM122188 is not a
proof of adjacency. Exact122187 text search in Parpola returnedzero; PDF150–151
were visually checked but independently named interpreterAO22310 belongs to
another object. Font-cache warning nonfatal. Current Wikipedia lacked the old
link; mirror cache miss. All negative attempts and next source leads are saved.

Saved docs/BM122187_AUDIT.md and data/processed/bm122187_review.json with13
verified source/image/prior-review fingerprints. Integrated those checks and
five-unit prior-review agreement into audit_hybrid_sources.py. Updated earlier
foreign-artifact report's unresolved-accession statement. Merged one2,502-byte
bounded web capture, no new original PDF. Registry162=136downloads+22captures+
4archivedHTTPresponses. A diagnostic rg used a mistaken shortened parent-review
filename, returned an error, and was corrected to the existing
m77_foreign_primary_parent_review.json; no source evidence was lost or changed.

Final validation: full offline pipeline exited0 with156 tests, including the six
new relation-template tests. All162 registered source files passed byte/SHA256
checks; only raw README and retained repository LICENSE are outside the registry.
All13 BM122187 source/image/prior-review fingerprints separately verified.
Local links in six new/updated entry documents resolved. Every one of the417
signs retains null semantic and phonetic values. Refreshed and verified the run
manifest after this log update. This phase makes concrete scope/provenance
progress but does not achieve the decipherment goal; goal remains active.

## 2026-09-24 — dated Yale document and proposed seal correspondence

Classified the previous goal turn as progress: it added authenticated BM122187
identity and tested all417 codes under three relation templates. Current-source
inspection confirmed those saved results; no live unfinished process was assumed.
Continued searching for independently readable seal-and-document associations,
rather than assigning a person's name to an unrelated text. Broad searches
rediscovered the already-audited interpreter and four Meluhha tablets, but also
located Buchanan's Gungunum-year10 sealed tablet, Yale catalogue1090/YBC5447.
Delegated original Yale catalogue/photo review and exact readable-tablet/owner
review as independent bounded subtasks.

Parent extracted Parpola1994 and viewed printed130,273,274/PDF148,291,292.
Fig15.1 identifies YBC5447 and a Dilmun seal; the preceding page proposes an
Indus bilingual merchant contract as a possible future find. It does not label
this tablet bilingual. Printed130 names an obligated party/father but exact
primary cuneiform interpretation is reserved to the independent tablet audit.
The caption's1923BCE is middle chronology, not an unqualified absolute date.
Full-source extraction was used only to locate relevant pages. Render font-cache
warnings were nonfatal; final images were viewed after completion.

Downloaded Ricetti2020's20-page article from the University of Trieste repository.
Web reader and direct landing-page opens timed out; first sandbox curl could not
resolve host; authorized curl completed successfully. Saved all original bytes
in data/raw/yale_ricetti_2020.pdf. Viewed printed223–224/PDF3–4, including Table1.
It attributes rejection of the FailakaV/Kjaerum176=YBC5447 same-seal claim to
Hallo2001pp239–240, distinguishing variants of a common theme. Bounded exact-title
search recovered bibliographic references but no original Hallo2001 chapter.
This remains a documented attribution, not an independently examined original
Hallo argument. The separate Mackay1938seal661/impression20 pair is labelled
doubtful; its inscription cannot be transferred to the Yale tablet.

A Possehl anthology search snippet appeared to juxtapose an unmistakable Indus
character with the Yale tablet. Follow-up searches located the character phrase
as a Gaddno7/IM8028 quotation in another reprinted article. The apparent Yale
claim was rejected before it entered an evidence ledger; agent was notified of
the correction. Broad speculative rebus results were not treated as translations.
Exact parent query history and selected bounded paraphrases are retained in
data/raw/yale_anchor_parent_web_capture.json. Diagnostic zsh glob with an absent
gungunum filename failed without changing files; subsequent rg inventory worked.

Saved initial docs/DATED_DOCUMENT_BRIDGE.md and parent review with8 fingerprints.
Two parent source proposals total2,358,812bytes. Other agents' primary-source work
continues; central source registry will be merged after verified records arrive.

Yale catalogue original25,377,330-bytePDF recovered by agent. Parent independently
viewed printed382/PDF400 and facingphoto/drawingPDF401. Entries1088/1089 discuss
Induscharacters;1090/YBC5447 describes seateddrinkers andmotifs. Drawing1090c has
circle+flankinggrids; separateFailaka1090d hasplant+flankingbirds. These published
designs differ; no unchanged-dieidentity orIndusname alignment inferred. Parent
review now11fingerprints. A read of the AS16redirectHTML produced large truncated
diagnostic output; it was not mistaken forPDF. Agent subsequently recovered the
actual42.9MBprimary AS16PDF fromthe publisher'scurrentlink and is checkingtext.

Original AS16 now adds substantive evidence. Hallo printed200/PDF220 translates
fourtalentswool, twogurwheat, twogursesame, fromLuma'a toHatin-IbanumsonApkallum.
The text contains supplied/restored readings, witnesses andfutureclearanceoath.
Printed202/PDF222 explicitly infers rather thanreadsHatin-Ibanum aslikelysealer
fromhisobligatedpartnerrole. Parent independentlyviewedbothpages; noquantity
conversion orsealstrokeequationinferred. Parent reviewexpandedto14fingerprints.

Catalogueagent's originalBuchanan1965 review readpp204–209 andviewedPDF224,225,
228,229. Yale drawingiscompositeofvisibletraces withpossibleedgeatbottom.
CrosshatchedsquarescomparetoMarshallccxcvi–ccc innote17, butauthorregardsmost
TypeIII motifs asnolongerwriting, possibleGadd12exception. NoM77identity or
writtensequenceestablished. Preservedthisqualification: absenceofanauthenticated
textdoesnotmeanabsenceofvisualresemblance. Agentledgerpins2sources+10images.

Tablet audit completed. Recovered original AS16PDF45,022,472bytes (about42.9MiB)
after legacyURLreturned realpublisherHTML186,519bytes; bothretained. Recovered
ARCHIBAB4(2020),15,455,227bytes; printed50tablepointsT24413. Initialexcerptloop
overwroteitsnavigationexcerptwithlastmatchingpage; agentreplacedwith explicit
multi-pageextract50,57,347,348,549,originalPDFuntouched. Tablepage50viewed.

ARCHIBABcurlreturned1,476-byteappshell. PublicbrowserUI succeeded withoutlogin:
T24413=YBC5447 andexplicitoutgoingCDLIP306518. DirectCDLIlinkclickdidnotnavigate;
newtabvisibilityerror, subsequentnavigationtimeout,webfailure and30-secondcurl
zero-byte timeout retained asfailedattempts; noCDLIHTMLorimageclaimed. A bounded
UIcapture2,253bytes preserves provenance andbriefexactuninscribed-sealnote.
USCISF_TXT_01101 remains anunverified extra lead,notassertedidentity.

ARCHIBABcallsseal impressionsuninscribed. Itsheaderday2 and2020tableday2 conflict
withownline14U4 20.KAM andHallo'sday20; retainedboth. Thewording2impressions versus
Yaleseveralstamped surfaces is notproof oftwo differentdies. Hatin-Ibanumowner,
Urprovenance andGulfdestination remain qualifiedinferences. Persons, restored
witnessname, suppliedreceiptpredicate andtentativewoolgrade preserved inledger.
Noethnicity, Indussignsequence, commodityword orsound assigned.

Merged8verifiednewrecords88,404,089bytes, sixdownloads+twoboundedcaptures.
Centralregistry170=142downloads+24captures+4archivedHTTPresponses. Allraw files
remain data/raw. Three reviews together pin32distinct evidencefiles; focused
scripts/audit_dated_document_bridge.py execution passed, preserving dateconflict,
goods andidentity scope. Integrated audit inrun_all.py andupdated centralreports.
The originalHallo2001 andBuchanan1967 articles remain unrecovered, but original
Hallo/Buchanan1965 andYale1981 supply the bounded conclusions. Fullvalidation next.

Final validation completed: full offline pipeline exited0 with156 tests passing,
including the integrated dated-document source audit. All170 registered rawfiles
passed exactbyte/SHA256 verification; only README andretainedLICENSE are outside
registry. Local links in seven changed entrydocuments resolved. The dated-document
audit pins32distinct files across14parent,12catalogue and12tablet-ledger references
(shared evidence deduplicated). All417 semantic/phoneticvalues remain null.
Refreshed and verified manifest after this log update. The goal remains active
and unmet: this phase establishes documentarycontext and rejects an unsupported
alignment, not a decipherment. Useful unresolved leads include directCDLIimages,
the distinct Bahrainassociatedtablet/seal case, and originalcatalogueidentity of
otherforeignobjects; these are leads, not evidence of successful translations.


## 2026-09-24 — Bahrain associated tablet, catalogue crosswalk and new tokens

Continued the foreign-name-anchor investigation with two parallel agents: one
traced the old three-name tablet, the other checked the 2026 token publication.
The parent independently checked the older seal identities, Parpola's page and
the retrieved primary reading. All downloaded files remain together in data/raw.

The old tablet reading was recovered in Gelb1980 AS21, printed2/PDF18, through
the publisher's current versioned S3 URL. Gelb explicitly worked from a rough
copy carried from Denmark by Juris Zarins. The page lists three people and says
the third is son of the first. Both agent and parent viewed the page. First-name
Ia-a-bi-na-im versus patronymic I-a-bi-na-im is preserved as printed, alongside
Gelb's identification of them as the same name. No new cuneiform collation,
artifact accession, exact find distance, seal owner or Indus counterpart was
established. The edition lead is Brunswig/Parpola/Potts1983 BBVO2 p107/pl3fig12,
located in Potts1990's account; the original chapter remains unrecovered.

ResearchGate Qalaat1 download attempts failed; Sind Through the Centuries and
Sind Quarterly PDF requests returned403. An indexed half-metre association is
retained as unverified and its corrupted relative-depth wording remains null.
Neither three centimetres nor three hundred is adopted. Two obsolete ISAC paths
returned404 before the current publisher link succeeded. Læssøe1957's capacity
potsherd and Bibby1964's Kassite-building tablet were rejected as different
artifacts, based on their publisher abstracts. Exact attempts and source URLs
are preserved in the agent review/capture.

Parent inspected retained Parpola1994 printed11/PDF29: it reports the Bahrain
association and a palaeographic date about2050–1900BCE. Adjacent Fig1.7 is Lothal
L-123, not the Bahrain seal. Printed130/PDF148 repeats the Bahrain claim separately
from Yale's contract. A provisional guess that PDF327–328 might provide the
relevant contextual notes was wrong: they are bibliography pages309–310. Their
renders remain generated navigation artifacts, not claimed seal/tablet checks.
References to Parpola1994 pp309–310 in later Gulf literature must be resolved by
publication title; they cannot be assumed to refer to this book's narrative.

Laursen2010 primary PDF was accessible as39 pages of web-extracted text, but
canonicalwww, redirectednonwww and browser-agent download URL attempts all
returned403. No complete PDF is claimed. Screenshot requests for PDF5/15 yielded
no usable image content in this session, so no table/plate visual check is
claimed. Table1 printed100 gives no6=Kjærum1994fig1726 and no7=fig1725 plus
Al-Sindi1999no279, both Qalaat; Failaka no13 instead=Kjærum1983no279. The repeated
279 is a catalogue namespace collision, not an object join. Printed121–122 gives
phase-level chronology only. No nearby seal is selected from those two objects.
The limited paraphrase, query history and access failures are preserved in
bahrain_laursen_web_capture.json; unrelated search hits were not used.

The 2026 JNES article DOI10.1086/739820 is authenticated. Its repository abstract
reports3 tokens with2 cuneiform seals naming Yagli-el and Panipa, while explicitly
posing the same-person versus namesake question. Public first-page115 was
independently viewed by parent and agent: AlMaqsha introduction, no object photos.
The university record marks the full PDF embargoed until2027-04-01. Publisher
full/PDF routes and author-copy searches yielded no complete paper. A public
first-author announcement reports2AlMaqsha tokens,1Qalaat token and repeatedseal,
plus3StyleII impressions. The nearby royal-mound date1665–1540BCE is not silently
assigned to the tokens. No contacts were sent, and no actual Indus text or owner
join was recovered. Absence in the limited accessible material does not prove
absence in the complete paper.

Merged7 verified source records totaling26,993,686bytes:5downloads+2captures.
Registry now177=147downloads+26captures+4archivedHTTPresponses. The sole raw
exceptions remain README and retainedLICENSE. Added common offline audit
scripts/audit_bahrain_anchors.py, integrated into run_all.py; it pins13 distinct
evidence files, reextracts the primary pages and preserves the independent cases.
Updated README, report, hypotheses and sources; focused audit passed. All417
semantic/phonetic values remain unresolved. No arbitrary name or DUMU alignment
was fitted. Full offline verification follows.


Bahrain phase verification completed: full offline pipeline exited0 with156
tests passing, including the new13-file evidence audit. All177 source records
passed exact bytes/SHA256 checks; all417 semantic and phonetic values remain
null. Local links in seven edited entry documents resolved. Refreshed and
verified the manifest after this final log entry. This phase authenticates a
published name-list reading and prevents catalogue conflation; it does not
supply an Indus translation. Goal remains active and unmet, with the original
1983 tablet edition and Qalaat find register still useful retrieval targets.


## 2026-09-24 — Consistent segmentation of three-inscription chains

Previous goal turn classified as progress: it recovered a bounded primary
Bahrain reading, corrected catalogue identity and persisted verified evidence.
This turn moved from inaccessible external name joins to a discriminating local
constraint on the already computed relation patterns. Saved protocol before
computing the extension, explicitly acknowledging earlier pair results were
known. No additional source files were downloaded; registry remains177.

Tested all417 markers across prefix/internal/suffix placements using the unchanged
1,175 domestic candidate records collapsed to1,066 strings. Three complete strings
must be distinct. Incoming and outgoing matches must use exactly the same middle
parse. Counted ordered triples separately from pair-witness combinations and
compatible parse realizations; no name, kinship, word boundary or statistical
confidence was inferred. A subagent independently derived the terminal overlap
criterion i+j=middle-body-length, the reversal bijection and the non-kinship
q^4−3q²+2q category-model counterexample.

Computed prefix20apparent→1consistent, internal0→0, suffix1463→330. Thus1152
of1483 apparent paths fail the same-middle-parse requirement. Markers with
consistent paths are M012suffix3, M211suffix20, M249prefix1, M342suffix307.
All417×3 result rows and all conflicting/compatible middle parses are saved.
M001 has no paths, implied by its prior lack of pairs; it is not a new negative
semantic finding. These counts are hypothesis sums, not independent artifacts.

Eight focused algorithm tests passed, including an independent complementary-
overlap oracle over28 binary strings length2–4. Both terminal templates yielded
7450apparent,3126consistent,4324rejected synthetic triples; the independent agent
obtained the same complete maps without using the production parser in its oracle.
Agent spotted a standalone duplicate-input counting caveat: parent added explicit
ValueError rejection and a test. Current upstream witnesses are unique, so corpus
counts unchanged. Two-string closed walks are excluded; at least one successful
realization suffices even when other boundary combinations fail.

Post-result exploratory length audit:304 retained triples have1+1 middle bundles,
26 have1+2, and one has3+2. Selected that sole multi-sign case for primary review:
2463→2302→4084 through terminalM342. Rendered original M77 Texts PDF83,78,111
(printed72,67,100), reviewed full pages and exact-row crops, and compared signs
with labelled primary signlist PDF43,45,46. Complete sequences agree with candidate
export. Metadata100301/100001/100101 all ends in direction1; field-symbol codes
03/00/01 are kept separate. No doubtful/lost/continuation markers on these rows.
The extra signlistPDF44 render was generated before noticing sign102 is already
onPDF43; PDF44 is not counted as inspected evidence. Crops use PILcrop only.

Saved11-file primary fingerprint ledger, protocol, analysis script,8tests,
independent proof review and result discussion. Primary verification establishes
a repeated-bundle pattern, not photographs, actual word divisions, dated people
or genealogy. A consistent triple need not be compatible with other triples in
a single corpus-wide segmentation. No semantic or phonetic values assigned.
Integrated script into offline pipeline and updated README/report/hypotheses
and earlier relation report. Full verification follows.


Final consistency-phase verification: full offline pipeline exited0; all164 tests
passed (8 new meaningful checks). All177 registered source files passed exact
byte/SHA256 verification. The1,251 control rows reproduce1483apparent/331consistent/
1152contradictory ordered triples, and the11 pinned primary-example files verify.
Local links in six changed entry/review documents resolve. All417 semantic and
phonetic values remain null. Refreshed and checked the manifest after this entry.
Goal remains active and unmet; consistency filters and authentic repeated strings
constrain theories but do not establish sounds, meanings or the language.


## 2026-09-24 — Shared-segment alternatives and chain artifact context

Previous turn classified as progress: quantified contradictory chain boundaries,
proved a sharper consistency condition and checked one multi-sign pattern against
the primary catalogue. This phase tests whether its selected shared bundles recur
with competing boundaries, while an independent agent traces the physical objects.
The same1,175-record/1,066-string domestic sample is retained; no allographs merge.

Exploratory scan found M391M099M387 in4 complete strings and M102M287 in9. After
excluding the entire three selected strings,2 and7 remain. Explicitly no held-out
validation claim: the example was discovered in this same corpus. Overlapping
pairs M391M099 andM099M387 occur in49/19 unique strings (50/20 references), while
M102M287M329M343 is an initial four-sign segment of2084 and4084. Recurrence thus
does not single out the two chosen bundles as indivisible names. The frame
M391–X–M387 has X=M099 in4 strings and X=M123 in3091; the latter identity remains
candidate transcription here, with no allograph or numerical equivalence inferred.

M102M287M342 occurs in4 unique strings, M106M287M342 in5 (7 references). These
catalogue stroke forms motivate a quantity-like alternative for a subset of
contexts, but no arithmetic values or units follow. M287 also has non-stroke
predecessors and begins3 eligible strings. Output retains all predecessor rows
and all417 possible neighboring-sign counts for each selected pattern. Eight
otherwise matching records remain excluded for loss, doubt or multiple export
documents;2659's doubtfulM102 is not promoted to a clean minimal counterpart.

Located2084 atPDF71 by OCR; OCR missed1088/1126. TentativePDF53/54 renders showed
1126 on53 and no target on54; shifted toPDF52 and verified1088 there. Parent
viewed full rows and crops:1088p41,1126p42,2084p60, all metadata100101, no doubtful,
lost or continuation markers. Sequences match the export. SignlistPDF43/45/46
reused; previously generatedPDF44 now viewed forM211 (not retroactively claimed
as inspected last phase). The two background three-sign occurrences and longer
four-sign prefix are authenticated in printed drawings. No artifact autopsy or
word divider is claimed. The parent review pins12 files; crop coordinates saved.

Added scripts/audit_chain_segments.py and integrated it after consistency audit.
An independent regex search agrees on all seven complete-string occurrence counts.
Focused execution passes; selected primary rows and file fingerprints are checked
at runtime. No new unit tests added for the straightforward extraction. Updated
README/report/hypotheses and new context report. Artifact agent's exact original
catalogue/depth findings and source registration will follow before final checks.


Artifact follow-up completed by the independent agent and reviewed by the parent.
M77 appendix V authenticates FEM and EH catalogue ranges. Original tables identify
2463 as FEM463/DK7722 (block10, houseII, room26, level −13.6ft), 2302 as
FEM302/DK3463 (between blocks3 and4, −10.2ft), and 4084 as EH84/find474
(moundF, 7ft3in below surface). CISI1 adds M-384/ASI63.10.187 for DK3463; its
Finnish-Concordance column is not treated as a general M77 crosswalk.

The parent visually checked all three table details, M77 appendix p816/PDF825,
CISI1 p368/PDF404 and photo p95/PDF131, Vats plate84 detail and p38/leaf64.
Vats places find474 and find272 on either side of a wall in the StratumIII
account without assigning474 its own side or exact square. The companion is
not either Mohenjodaro chain member. Depths have separate contexts and cannot
establish generations, chronological succession or contemporaneity. The
published seal photograph is not an independent palaeographic edition.

Registered all six new JPGs (11,974,995 bytes) in data/sources.json, including
two excluded locator misses: Mackay leaf398/p376 and Vats leaf365/p339.
Additional misses recorded in the artifact ledger: Vats plates PDF100 (correct
184); M77 PDF829/832 (appendix offset differs from Texts); several CISI table
pages without further target identities. CISI132 rendered but not inspected.
Accepted and locator evidence are pinned in a 30-file artifact review, now
checked by audit_chain_segments.py together with its 12-file recurrence review.
The output embeds the accepted object rows and hashes the review inputs.
Registry total183:153 downloads,26 captures,4 archived HTTP responses.
No semantic/phonetic values assigned. Full offline verification follows.

Final verification for this phase: the complete offline pipeline exited 0 and
all 164 tests passed. All 183 registered raw sources pass size/SHA-256 checks;
the only unregistered raw-directory files are its README and the retained
repository license. The recurrence audit verifies its 12 evidence pins and
the artifact review's 30 pins. All 170 local links in the six checked entry and
review documents resolve. All 417 semantic and phonetic values remain null.
Refreshed and checked all manifest groups after this log entry. This is progress
in authentication and testing alternative boundaries, not a decipherment.
The active goal remains unmet; no external anchor yet singles out the proposed
bundles as names, quantities, or any other established reading.


## 2026-09-24 — Exact substitutions for the stroke-and-curve hypothesis

Previous turn classified as progress: authenticated artifact identities, integrated
30 evidence pins and registered six sources. The next test asks whether M102 and
M106 occur in otherwise identical complete inscriptions. This targets the quantity-like
alternative directly, rather than treating a common two-sign continuation as an
exact substitution. Read the current segment audit and prior W-code substitution
work; retain the unchanged domestic M77 sample and all graphic distinctions.

Initial exploratory mask enumeration finds three full frames shared by M102/M106:
? M015; ? M169; M267 M099 ? M162. None is immediately before M287 M342. The latter
anchor has three preceding catalogue signs in this sample: M102, M106 and M373.
No shape or number inferred for M373. A written exploratory protocol now fixes
all417 comparisons and exact full-context criteria; it explicitly postdates these
findings. Delegated primary verification of the longer frame (1091/1131, with
other occupants1143/1157) and an independent Hamming-distance enumeration.

Parent mask-index audit enumerated every target-bearing frame and all417
replacement summaries. M102/M106 share exactly3 complete frames, only1 with
length at least3. M287 M342 has predecessors M102 in4 strings, M106 in5,
and M373 in5; the latter is retained without a geometric or semantic guess.
The independent agent checked83,691 unordered same-length pairs by Hamming
distance, finding681 one-position substitutions overall and the same3 target
frames with identical occupants/reference lists. Runtime cross-check compares
full results, not just totals. Original shared-frame reference total22 does
not imply22 independent observations.

Four new regression checks cover changed-prefix false positives, repeated
reference counts, medial/final anchor distinction and a synthetic exhaustive
Hamming oracle. First focused unittest invocation failed on import because it
relied on other tests setting sys.path; made the new test self-contained, then
all4 passed. Both independent verifier and new audit added to offline pipeline.

Primary agent checked the four longer-frame examples1091/1131/1143/1157 plus
six surrounding examples. Parent independently viewed the four exact-frame
crops,2254 and the labelled signlist. M102/M104/M106/M107 show3/4/5/5 strokes,
with the last arranged3above2 rather than in one row. Neither five-stroke form
is merged or assigned a value. Exact categorical-label substitutions reproduce
the same observations without numerical semantics; the positive finding is a
shared structural role, not a uniquely forced numerical reading.

Independent review flagged2659 as the only apparent solus M102 counterpart.
Follow-up primary PDF89/p78 shows the source doubt mark next to M102, metadata
103501, also independently viewed in the parent detail image. Uncertainty is
therefore retained as catalogue uncertainty, not repaired by assuming the
expected pattern. The primary review separates clear and doubtful rows.
No downloads or new readings; final verification follows.

Final phase verification: full offline pipeline exited0; all168 tests passed
(4 new). The primary ledger pins29 files, with10 clear rows and1 doubtful row;
the new audit checks both the clear-row eligibility and2659's retained doubt.
Independent input fingerprints and sample sizes are checked before comparing
all target frames and occupants. All183 retained raw sources pass byte/SHA-256
checks. All160 local links checked across seven entry/review documents resolve.
No raw downloads added. All417 semantic and phonetic values remain null.
Refreshed and verified all three manifest groups after this entry.

This turn is progress: it identifies and authenticates a stronger four-sign
substitution frame while distinguishing a weaker local-ending comparison and
verifying why its tempting counterpart remains doubtful. The active goal is
still unmet: the stroke-family hypothesis lacks an external numerical/linguistic
anchor, and neither an all-symbol semantic key nor a decipherment is established.


## 2026-09-24 — Five-stroke variants, contextual scope and missing primary lines

Previous goal turn classified as progress: independently enumerated exact
substitutions and authenticated primary stroke patterns and2659's doubt. This
phase investigates M106/M107 beyond the selected four-sign frame, with M096
(long five strokes) as a visual-count control. All remain distinct signs.
Current-worktree inspection exposes source coverage gaps: TableI has22/38/6
occurrences for M096/M106/M107, while the candidate export has20/35/5.
M107's five export references1157,6111,7072,8016,9846 cannot therefore be treated
as its complete primary corpus. Delegated original concordance checks, including
recovering missing lines, in two independent bounded tasks.

Wrote an exploratory protocol retaining the original domestic sample, with
separate global-seal and all-object single-document clear-text sensitivity scopes.
The latter allows solus inscriptions; it is not silently pooled with the original
minimum-two-sign seal sample. All417 replacements will be retained. Counterfactual
merge collisions are bookkeeping, not evidence sufficient to merge signs.

Results: domestic1175/1066, global-seal1182/1073, and all-object clear single-
document including solus1342/1170 samples all show2 M106/M107 full shared frames,
0 for either pair involving M096. No pair cooccurs in an eligible string.
Counterfactual M106/M107 merging reduces distinct strings by2; other merges0.
All417 replacements per sample are retained. A separate pairwise Hamming oracle
checks the indexed target pairs in every scope. Shared frames also admit other
stroke counts, so they cannot prove equality of the two five-stroke values.

Recovered M1071471 side1 line2 M104 M205 M107, with the full five-line four-sided
object recorded. Texts continuation21 means line2/direction1, while Concordance12
means side1/line2; preserved distinct metadata conventions. All6 M107 occurrences
now visually checked and reconcile TableI2initial/1medial/3final.
Recovered M0962921side1 solus;1325side2 M025 M409 M096. Recovered M1068301side2
solus;2923side2 M387 M015 M104 M106 M312;2636side2 M267 M099 doubtfulM106 LOSS.
The six additions reconcile not just totals22/38/6 but all primary position counts
and target-sign reference multiplicities. Concordance authentication for M096/M106
checks target-occurrence identities; it does not authenticate every non-target
glyph in all their exported lines. No global corpus records overwritten.

Failures/corrections: Texts1471 OCR search missed it; trialPDF65 starts1491, so
existing64 used. Early views of still-rendering365/364 returned invalid image data;
same processes completed and images were then inspected. OCR6301 corrected to
8301 visually; tentative1325 IDs014/149 corrected to025/409. PDF41–42 were codebook,
not signlist, and used for metadata conventions; PDF323 boundary locator starts
next sign. All retained in the two primary reviews and linked reports.

A separately labelled target-selected supplement adds the5 intact recovered fields
to the broad export sample, permitting their already normalized direction3/4 and
multi-field objects, while excluding2636's doubt/loss. M096/M106 then share only
the empty-context one-position frame?, from their two solus fields. This is not
surrounding-context evidence or an allographic proof. Other target-pair shared
frames unchanged. Original sample definitions and catalogue codes remain intact.

A third agent traced1471 to HR2240/MIC471–473/CISI M-331/NMI155. Parent visually
inspected the original table crop and CISI fullpage/crop, plus Marshallpp372–373.
The stone is classified in that report as a white steatite bossless seal,0.7×0.7in,
9ft0in below surface; no mass, thickness, room or absolute date authenticated.
Four inscribed surfaces/five lines agree with primary text recovery; modern
accession marking on surfaceE is not ancient text. Perforation is explicitly
excepted onp372, whereas thep373 hole-wear paragraph ends with figs471/472 in a
list. Parent refined initial 'contradiction' to apparent inconsistency or ambiguous
illustration-list scope; no hole assumed. No reading order across faces or unit
value follows. OriginalMIC volumeIII plate not recovered; laterCISI photographs
provide the physical views. Web searchHR2240 gave irrelevant legislative hits.

Registered4 new Marshall archivefiles indata/raw,13,401,464bytes; sources total187
(157 downloads,26 captures,4 archived responses). Three reviews pin26/27/16 files
with overlaps, verified at runtime; output preserves the object identity and
caveats. Updated README/report and specific theory reports. No new unit tests
for these extractions; existing mask tests plus independent enumeration and
primary marginal/reference assertions supply direct checks. Full pipeline follows.

Final verification: full offline pipeline exited0; all168 tests passed. New
audit's independent pair enumeration agrees in all3 original scopes and the
separate targeted supplement. Recomputed totals22/38/6 and all four position
columns match TableI; reference multiplicities match the inspected concordances.
All187 raw source files pass byte/SHA-256 checks; raw-directory extras are only
README and retained license. The3 evidence ledgers cover63 distinct pinned files.
All165 local links checked across8 entry/review documents resolve. All417 output
rows remain present in each comparison and all417 semantic/phonetic fields are
null. Refreshed and verified the manifest after this entry. Goal remains active
and unmet: recovered primary fields and object context strengthen the evidence
base but establish no numerical unit, equal sign values or decipherment.


## 2026-09-24 — Linking the recovered tool field to measured objects

Previous turn classified as progress: six primary omissions recovered, positional
marginals reconciled and HR2240 physical identity authenticated. Current task
checks whether newly recovered2923 is a new physical mass anchor. Re-read original
weight audits and current export before tracing its appendix mapping.

Found and corrected a prose error in FIVE_STROKE_MISSING_LINES.md:8301 actually
has source_doc_count2, not1. The ledger and export were correct; the sentence
had retained6301's count from an earlier OCRmisidentification. No data or sample
counts changed. Recorded the correction explicitly.

Independent artifact search establishes2923=FEM CXXVI2, already measured tang
DK7856. It is not a new mass observation. Delegate primary/CISI identity check
and separate graphical review of the object-specific u/i/t toM77 associations.
Parent inspected the saved original tang drawing and normalized2923side2.
The original plate distinguishes stroke orientations, while the normalized
M77 row showsM104/M106 as upright groups. The local proposed1u5i4t expression
needs explicit residual-sign coverage rather than being called a complete reading.

Primary appendix crop now directly verifies2923=CXXVI2,2924=CXXVI3,2925=CXXVI5.
Parent viewed crop. Source field7856 has blurred third digit, but plate/item join
is secure. No new CISI or museum identifier authenticated: retained incomplete
CISI OCR search and inspectedPDF406 failed; targeted webqueries7856chisel,DK7856
corpus,2923CXXVI returned later papers, speculative sites or number collisions.
No search snippet was adopted as primary evidence. PhotoCXXXI31 remains tentative.

Independent graphic review alignsM104 with4 transverse strokes,M106 with5upright,
M312 with1arch onthisobjectonly. Original orientation differs from normalized
uprightM104. ResidualM387/M015 remain; the old drawing is insufficient to
independently authenticate every feature of its upper complex sign. Pettersson
p101 acknowledges two further signs. His u5i4t order is opposite the normalized
tail; addition itself discards that ordering difference. K122/8301 soleM106 has
five photographed strokes; no universal unit is inferred from either object.

Saved exploratory conditional mass protocol, exact-rational script and proof.
If K122's soleM106 is complete exact476g mass expression, an invariant nonnegative
contribution ofM106 on2923 gives mass>=476g, contradicting165.343g by310.657g.
An original-mass interpretation instead requires factor>=476000/165343
(2.878863937...), with missing fraction>=65.2640756%; these are conditional
requirements, not observations. The separately hypothesized strict2.6 cap is
429.8918g and fails by46.1082g. No u/i ratio or equality of stroke orientations
is needed. Fixed numerical value5 with changing units is not rejected; fixed
mass contribution is the additional tested premise. Two tests verify strict
equality and distinguish a larger original allowance from current-mass fit.

Attached object-specific graphic links to all417 index rows: three mapped codes
and two residual codes have evidence, other entries empty for this limited
review. Runtime requires mapping indices and residuals cover the full printed
field. Semantic/phonetic values remain null; new mass observations0. Added the
audit to the pipeline, updated theory/report entries and linked new documents.
Identity and graphic ledgers pin16/20 evidence entries respectively. No new
downloads; source registry remains187. Full verification follows.

Final verification: full offline pipeline exited0; all170 tests passed (2new).
All187 source files pass byte/SHA-256 verification. Two new evidence ledgers cover
30 distinct files; all pins verify. All163 local links checked in8 entry/review
documents resolve. The regenerated417-sign index has qualified graphic evidence
forM104/M106/M312, explicit residualsM015/M387, and no semantic or phonetic values
for any sign. Protocol/model bounds reproduce exact fractions; no mass or body
loss was newly measured. Refreshed and verified manifest after this entry.

This is progress toward tested readings: the new physical join prevents duplicate
anchor counting and exposes a specific cross-object mass-model contradiction.
It does not establish a numeral, unit, language, or all-symbol decipherment.
The active goal remains unmet.

## 2026-09-24 — Original stroke orientations and normalized-code limits

Previous completed phase classified as progress: the recovered tool field was
joined to an already known mass observation, preventing duplicate anchor counting,
and an exact conditional M106 mass contradiction was established. This phase
examined whether original orientations survive the normalized M77 codes.

Two parallel agents checked original tools and catalogue inclusion. The initial
parent-supplied CXXVI1/4 locators were wrong: they identify DK7858 spearhead and
DK7853 axe, not target DK7857 and DK7800. The original tables instead establish
DK7857=CXXVII1 and DK7800=CXXXIII1; M77 Appendix V maps these to2926 and2928.
Discarded the tentative omission interpretation before accepting any exclusion
claim. PDF93 also missed the target text rows; PDF96 was correct. Bare OCR7800
collided with an unrelated seal-table row. These failures remain in the ledgers.

Primary catalogue fields are2926 M104 M110, metadata600004, and2928 M104 M104,
metadata600005. Both already existed in the export; no line recovered. Direction4
means top to bottom,5 symmetrical arrangement,9 doubtful. No local code5 error
was found in the previously saved codebook/repetition audit. General normalization
rules allow rotated variants up to90degrees; inclusion rules do not establish a
blanket stroke-only exclusion. Two included fields do not prove total coverage.

Original knife prose explicitly says four vertical strokes above four horizontal.
Parent viewed the saved prose crop and catalogue rows. Its photograph does not
independently resolve all eight. The original spearhead drawing, viewed by parent
and agent, depicts an upper four-mark group and lower seven-mark group with both
groups upright, despite a tilted upper patch. Thus later7i4t is not independently
confirmed as four transverse strokes. Original prose gives counts, not this
orientation contrast; photographs are too unclear to settle every stroke. Source
disagreement is retained, not reconciled by assumption.

No new numerical masses. Spearhead weighing was described as useless owing to
oxidation. Spearhead table/prose thickness0.11/0.13in remains unresolved; restored
length and estimated width cannot supply original mass. Knife is a different
locus (block3/VI/40/−18.4ft) from spearhead (12A/I/15/−24.4ft). No common hoard
was inferred. Five original-page JPGs totaling10,934,099bytes added underdata/raw
and verified/registered indata/sources.json. Source total now192:162downloads,
26webcaptures,4archivedHTTPresponses. Original/corpus ledgers pin23/22files.

Persisted an explicitly post-exploration protocol and exact-rational model audit.
If each knife group contributes4i or4t and each normalized M104 occurrence must
have invariant scalar contributionv, local agreement requiresv=4i=4t, hencei=t.
Strict t<i and this invariant local mapping cannot both hold. This does not
establish numerical meaning or reject numeral4 with context-dependent units.
A total-only counterexample prevents overclaiming: i8,t1,v18 gives32+4=18+18,
so matching inscription totals alone does not forcei=t.

The later nine-tool table uses only coefficient4 wherever t occurs. Exact
reparameterization c=4t replaces each such component with one quantitatively
valued indivisible component without changing any additive predictions on that
support. This is not evidence for a nonnumeric category. Removing contested
spearhead leaves the same limitation. A hypothetical varying count3 breaks the
fixed-component replacement for positivet; no such new object was claimed.
Independent mathematical reviewer accepted the scoped proofs and identified
integer-domain/prior restrictions as additional premises, not table evidence.

Added script to offline pipeline and two tests guarding total/local confusion
and fixed-count versus varying-count support, including zerot boundary. Both
focused tests pass. Index now attaches whole-object source comparisons toM104
andM110 without per-token orientation assignments on symmetric2928. Other rows
retain empty orientation-review lists; all417 semantic/phonetic values remain
unassigned. Updated report, hypotheses, index documentation and README links.
Full pipeline and final provenance verification follow.

Final verification: full offline pipeline exited0; all172tests passed. All192
registered source byte counts and SHA256 hashes verified. The two primary
ledgers cover40 distinct evidence files; pins still match after regeneration.
All178 local links in the8 updated entry/review documents resolve. Only the
pre-existing rawREADME and extractedmayig_LICENSE lack source-registry rows;
no unregistered download was found. The417-sign index attaches2926/2928 toM104
and2926 toM110, preserves null per-token orientation assignments, and retains
null semantic/phonetic values for every sign. Updated manifest after this entry.

This phase is progress: exact artifact joins corrected a failed search premise,
original sources weakened one orientation claim, and formal controls narrowed
what normalized codes and fixed-count expressions can identify. No language,
unit or complete reading has been established. The active goal remains unmet.

## 2026-09-24 — Correcting the tilted-row attribution; testing signed contributions

Previous phase classified as progress: verified tool joins, registered five source
images, and proved explicit representational/model limits. Revalidation found a
material overstatement in its spearhead conclusion. The existing earlier ledger
already called Pettersson's t a tilted-row stroke, whereas the new comparison
had treated it as requiring individually horizontal strokes. Re-read actual
Pettersson PDF10/printed98 and PDF13/printed101; parent visually inspected both
pages, plus PDF9/printed97 and PDF3/printed91 for context.

The source explicitly describes a tilted row, entertains t=i, and discusses both
an indivisible indicator and fraction alternatives. Upright individual strokes
in a tilted group therefore do NOT by themselves contradict7i4t. Withdrew that
inference in the original-tools review, protocol, source/results reports,
mathematical review, main report, hypotheses and index documentation. Preserved
superseded ledger wording in an explicit correction-history entry. The drawing
observations, plate joins and knife prose remain unchanged. Updated the script
so regenerated index entries carry the corrected comparison. Historical log
entries remain as history and are superseded by this correction. No claim that
a numerical reading or cross-object equivalence is now established.

Asked independent source reviewer to check exact attribution and preserve stable
primary evidence pins. Separately asked an arithmetic reviewer to assess the
paper's subtractive alternative. Found existing three-tool nonnegative proof,
so did not present it as a new discovery or create a duplicate pipeline. Extended
the existing weight-audit script to use all three primary metric masses under an
explicit original_metric branch:165.343,1910.030,262.233g. Earlier branch named
reported_precision actually retained small-axe262g; preserved it with an explicit
precision note instead of silently overwriting historical inputs.

The signed current-mass system6i=262.233,7u+6i=1910.030,u+5i+4t=165.343 has
unique solution i=87411/2000>0,u=1647797/7000>0,t=−4040177/56000<0. All three
residuals are exactly zero. Negativei is impossible if the small-axe equation
is retained, but allowing negativet supplies an algebraic fit. Thus rejecting
nonnegative contributions does not reject all subtraction models. This is a
saturated3parameter/3equation calibration, not independent confirmation of any
value or ancient subtraction. If t>=0 the original-metric lower bound is
6354979/14000g and factor6354979/2314802≈2.745366, still above hypothetical2.6.
Unmeasured original mass loss and residual complex signs remain explicit caveats.

One regression test verifies exact signed residuals and a genuinely positive
control. All five focused weight tests passed. A further lead from inspected
Petterssonp91 identifies C40=M776306 and crossing numerical/main-text layout;
export6306 containsM314/M106 within an eight-token line. No original C40 layout
or segmentation was authenticated in this phase; retained as a next source check,
not a new sign reading or completed result. Final independent reviews and pipeline
verification follow.


Source reviewer rendered the paper's opening terminology pages89/90. Parent
viewed both: p89 directly defines t through tilted rows, and p90 specifies rows
at an angle to other rows. Page90 already warns that sequential normalization
loses arrangement. Added attribution so that known concern is not represented
as this investigation's new discovery. The new contribution is the checked joins,
scoped proofs and correction, not novelty of the general layout warning.


Independent signed reviewer supplied a residual-sign counterexample: allowing
6i+r=262.233 restores negativei with i=−30,u=209003/700,t=117371/28000,
r=442233/1000. All three current masses fit, withu,t,rpositive. Persisted it in
the same audit and expanded the new test. This explicitly shows the negative-i
exclusion needs the no-other-sign-contribution premise; the extra free parameter
provides no semantic validation. Source attribution review pins17stable files;
no new downloads. All new/changed calculations now run in the existing pipeline.

Final verification: full offline pipeline exited0; all173tests passed. All192
registered sources verified, with no new download. Original-tool, catalogue and
attribution ledgers together pin55 distinct files; all byte counts/hashes match.
All202 local links in11 entry/review documents resolve. Regenerated417-sign index
now carries the corrected DK7857 attribution underM104 andM110; all semantic and
phonetic values remain null. Both signed examples have exact zero residuals and
explicit calibration/underdetermination labels. Refreshed manifest after this entry.

This is progress through error correction and stricter hypothesis testing. The
last phase's alleged spearhead/notation conflict is withdrawn, not counted as
surviving evidence against the published theory. The valid knife-layout observation
and mathematical limits remain. No full decipherment or unit value is established;
the active objective remains unmet.

## 2026-09-24 — C-40 crossed layout, reverse recovery and find-group controls

Previous phase classified as progress: corrected tilted-row attribution and
persisted exact signed/residual-sign counterexamples. Followed the concrete lead
in Petterssonp91 identifying C40=M776306 and an orthogonal arch/stroke group.
Parallel agents authenticated primary M77fields and original1943excavation
records; parent independently inspected CISI photographs/metadata and designed
an exploratory sequence test.

Parent used CISI contents to locate Chanhujo-daro pp327–343. InitialPDF375–377
render found C40reverse and neighboring Jhukar seals, not the front. Correct
frontPDF374/p338 and C39PDF373/p337 then rendered. No Jhukar-period label
transferred from neighbors. MetadataPDF411/p375 joinsC40=CH2596A=Finnish5075=
ASI74.1.76,photoHU828; C39=CH2529H=Finnish5083=ASI74.1.48. Initial low-resolution
photo-year reading1942 corrected to1982 from exactcrop; C39photo references are
Yale1982.10:31–32 and1981.13:10–12. InitialC39detailcrop cut part of column,
then expanded/reviewed; no fullXXUUU authentication claimed from it.

C40front photograph has a column of three arches extending above/below the main
row, with five short strokes above. Parent viewed native crop and later original
drawing. This is a post-hypothesis observation, not blinded confirmation or proof
of numerical composition. It does not establish engraving chronology, separate
message status, ancient reading order, or scalar meaning. SideB photograph is
faint; full code authentication came from catalogue rather than invented pixel
readings. Photographic ledger pins15files, crop coordinates retained.

Catalogue agent authenticated6306side1eightcodes M109 M059 M367 M380 M314 M106
M018 M162 and recovered omitted side2 *M129 M287 M086 M065 M067 M403 M087 M342.
Both direction1, metadata610001/continuation20001; only129doubt. Initialhourglass
identification resolvedM067 with numbered signlist and concordancePDF257. Parent
viewed bothfields and M312/313/314numberedshapes. Appendix825/PDF834 maps6306 to
CELXXIV1. Recoveredreverse remains separate; no concatenation or silentglobal
corpus replacement. Ledger pins31files. A navigation renderPDF550 foundM287,
not targetarches; finalselectedsectionsPDF567–568 and TableIPDF732 checked.

All five indexed occurrences of selected M312/M313/M314 were viewed with contexts
in contiguous concordance sections:3124802initial(doubtful)/2923final;
3134804initial/8302solus;3146306medial. Counts2/2/1 and allpositions matchTableI.
This is not every arch-like sign or every ancient occurrence. 4802/4804share
?M102 but312doubtprecludes a fully clear pair. M314 remains one code, not3tokens.
Existing2923recovery not duplicated. Runtime reconciles occurrences and writes
C40's two sourcefields with flags to a separate primaryline dataset.

Original-source agent's webbibliographic/Panjab route yielded no primary text;
poor indexedsearch replaced by Archive advancedsearch. Sevenitems returned;
publicIGNCA27263 supplied primarypages. Slowinitialresponse was awaited without
restart.13downloads (search,metadata,OCR,pageindex,9images) total24,416,229bytes,
all retaineddata/raw and registered after checks. Registry now205sources:
175downloads,26captures,4archivedresponses. Originalreview pins18files.

Exactp305records: CH2596A brokenaxe=LXXIV1/1a,3.43×2.67×0.28in,8/C locus297,
+9.3ft. CH2529H ingot=LXXIV2,13.75inlong×average1.4diameter,samecourtyard+10.4ft.
Parent viewed exacttable andp178sourcehypothesis. Mackay's35/36 alternative
already distinguishes a possible extra numeral from adjacent humanstaff, and his
inventory interpretation is expressly conditional. No mass for either target;
nearbyshovelweight not reassigned. Drawing/photo/sourceprose remain distinguished.

P43placesaxe inpan2596; ingotcatalogue belongs2529floorassemblage. P175's37piece
count is2529, notaxepan, so it cannot validate35/36. P43mentions an ingot inpan,
whilep305assigns illustratedC39to2529 andpp187–188describeonlytwoingots, second1113
elsewhere. Retained unresolveddetail rather than infer sameowner/deposition.
Parentnoticed p305headerGroups2529,2593; independentfollowup confirms headeromits
2596while exactfirstrowstates2596A. Laterrows really are2593; do not substitute
2593A for theaxe. Sourceledger/documentrecord the incompleteheader.

Froze exploratory deletionprotocol aftersourceview and before comparison counts.
One source-motivated projection deletes M314/M106; all7contiguous2tokendeletions
are comparisoncases. Excluded whole6306object; admitted2055nonempty secondary
records withoutdoubt/unknown,1519uniquestrings,644multidocumentrecords, allobject/
directioncategories. All7shortened6tokenstrings have0exact and0one-difference
matches; fulloriginal8tokenstringalso0otherexactmatches. No recurrence evidence
for chosenprojection; no refutation fromabsence in incompleteexport. Did not
relax criteriatochaseamatch. Testguardswholeobjectexclusion anddoubtfilter.

Added audit to existingofflinepipeline, links to all417index rows:16codeshave
C40fieldannotations,3selectedcodeshave5archoccurrencerecords; overlapwithother
reviews is explicitlynotindependent. Allsemantic/phoneticvaluesremainnull.
Originalprotocolandrawsourcespreserved; finalpipelineverification follows.

Final verification: the full offline pipeline exited0 and all174tests passed.
All205registered source byte counts and SHA256 hashes match. The three C40 source
ledgers pin64distinct files, all verified. All189local links in7entry/review
documents resolve. No unregistered downloads: only rawREADME and extracted
mayig_LICENSE remain outside the registry, as before. An independent comparison
check generated all417possible replacements at every position of each of the7
projected strings; none occurs in the same clear comparison set, confirming the
Hamming-search result without using its distance calculation.

The417-row index contains C40links for16codes, selected arch-occurrence lists for
3codes totaling5occurrences, and null meanings/sounds throughout. Recovered side2
has8tokens with M129doubt retained. Both C40fields remain separate. The only
shared selected-arch context is4802/4804 and is explicitly not entirely clear.
Refreshed and verified run manifest after this entry.

This is progress in authenticating the physical layout, completing one object's
catalogue transcription and ruling out an unsupported archaeological quantity
anchor. It does not establish the separate-field hypothesis,35/36 reading, mass
units, language, or all-symbol decipherment. The active goal remains unmet.

## 2026-09-24 — Arch extension and a bound allowing residual signs

Previous phase classified as progress: C40 reverse recovery, layout authentication
and excavation-context controls. This phase followed M315–M318 and tested whether
nonnegative contributions from unexplained signs can rescue a shared mass model.
Two agents independently reviewed catalogue coverage and C39 graphics; the latter
also checked the algebra. A follow-up to an older proof agent failed with the
agent-thread limit; the already active reviewer handled the bounded proof review.
No new downloads; all205 registered sources remain in data/raw.

Catalogue review verified six complete fields and all four indexed occurrences
of M315–M318, including Table I total/position counts (one each). M315 is seven
stacked arches, one code, on2925side2 beside M108. Supporting2924 has M108 M342
M001 M375. Other side2925 retains doubtfulM098. M317 on4032 retains loss and
direction9; initial is normalized position, not authenticated ancient direction.
M316/M317/M318 are complex forms, not established numeral multiples. Existing
1001=M393 correction retained. The agent corrected a clipped signlist crop and
an OCR navigation false hit before pinning28 files. Parent viewed the two axe
fields, numbered315–318 shapes and contiguous concordance contexts. The second
axe field has no doubt/loss; its seven arches are not seven corpus tokens.

Parent chose an exploratory protocol after source inspection and prior failures.
With S=A+r, L=A+7u, K=n*u+q, and r,q,u nonnegative, A<=S and u<=K/n imply
L<=S+7K/n. This does not assume A=6i or r=0, and does not require A>=0. It weakens
the older small-axe premise while still producing a contradiction for reported
surviving masses. Original S262.233 and L1910.030 plus later-published K121210
give weak n1 cap1732.233, deficit177.797; disputed n2 cap997.233, deficit912.797.
K121 photograph remains irregular; M313 normalization does not prove2equalunits.
No NMMA candidate mass substituted, no new weighing, no other-side concatenation.

Independent reviewer reproduced exact Fraction calculations and passed the two
focused tests: equality boundary, positive deficit, signed-residual escape and
conditional corrected-K boundary. Missing-mass inequality is
dS+(7/n)dK-dL>=D. Required added K alone25.399571…/260.799143…g is not measured
damage. Free unknown original masses remain nonidentifying. Negative residuals,
different units/targets or nonadditive composition change the premises. The proof
review pins an earlier script revision; subsequent parent changes authenticate
source fields/counts and export data, leaving the bound function unchanged.

C39 agent inspected whole photo and overlapping native-pixel crops, preserving
faint marks without declaring them characters or removing them. Angular and
curved forms support longitudinal layout and relative openings, but not an exact
completeXXUUU count. Crossing full-image band excluded from glyph counting.
Pettersson's Parpola234 attribution not equated with Mahadevan234. Full bounded
Chanhudaro AppendixV subsection includesLXXIV1=6306 but noLXXIV2/CH2529H/ASI74.1.48;
no global-absence claim or date-based argument. Review pins12files; parent viewed
wholephoto crop and accepted qualified result. No weight or numerical value added.

Added source assertions and all four count/position reconciliations to the new
audit, then integrated it in run_all and the417-row index. Six fields exported
separately with flags. New per-sign fields explicitly overlap earlier reviews;
no global frequencies are increased and all meanings/sounds remain null.
Saved proof, protocol, independent reviews, result JSON and two unit tests.
Full pipeline and final provenance verification follow below.

Final verification: full offline pipeline exited0; all176 tests passed. All205
source byte counts and SHA256 hashes match. The two new source ledgers have39
distinct verified evidence files (28+12 with one shared source). All162 local
links in README and six entry/review documents resolve. Only the preexisting
rawREADME and extracted mayig_LICENSE are outside the download registry.
The index has417 rows, all semantic/phonetic values null;17codes link to the six
extension fields, and four selected codes have one occurrence each. Source loss
on4032 and doubt on2925side1 remain present. Refreshed run manifest after this
entry and verified all three file-hash groups plus source-registry hash.

This phase made progress: four indexed sign contexts authenticated, a more
permissive shared-mass model conditionally falsified, and C39's proposed count
kept separate from observations. All-symbol decipherment remains unresolved;
the active goal is unmet. Further work must seek independent semantic or
quantity anchors rather than treat this failed mass model as a reading key.

## 2026-09-24 — Graphic components versus one-sign/two-sign context matches

Previous phase classified as progress: permissive residual-sign mass bound and
primary315–318coverage. This phase tests whether composite-looking symbols have
independently supported two-sign expansions. Parallel follow-ups were attempted
for shape and method reviews. The shape agent failed twice and method agent once
with stream-disconnection errors; no agent review was received or represented as
completed. Parent continued locally from retained sources. No downloads.

Before counting, froze exact whole-prefix/suffix replacement rules, different
reference witness, nonempty context, bothorders, all417targets, observedbigrams,
doubt/loss exclusion and strict-subset sensitivity. Parent inspected representative
signlist pp32–35. M317interior3+2 resemblesM107 more than single-rowM106, but its
tall pointed enclosure differs from lowM312. M316H-likeinterior has no authenticated
standalone representativeH. SecondaryP293 sayslargeH→M199, yetprimaryM199is a
crownedgate; not used as an H bridge. Fullvariantinventory not searched; no global
absenceclaim. M318leftundecomposed. These limits were saved before counts.

M77pp19–20confirm loss can represent multiple signs and catalogue normalization
suppresses actualdirection and variants; exact matches are therefore catalogue
sequence claims. A text search also found Parpola2009pp50–51's separatecrab+fish
andcrab-inside-figarguments. Their semantic claims were not imported into this
test, and the citedM57/M387pair was not promoted without a freshprimaryjoin.

All-clear secondaryscreen:2056records1520strings5902context/replacementinstances
cover186targetcodes,1639instanceswith>=2contexttokens,144targetcodesatthatgate.
Strictsubset:1293records1141strings3111instances159targets,940instanceswith>=2
tokens122targets. Contextlength1dominates4263/2171. These are dependent discovery
counts, no p-values or semantic coverage. Added a post-count descriptive split:
318/177instances retain target inpair (possible insertion, notnecessarilyfusion).
No cases dropped after seeing that split. Independent brute-force string-pair
enumeration reproduced5902/3111matches without usingframeindex. Two tests check
fullcontext, bothorders, emptycontext, samereference andduplicate suppression.

Selected primarychecks aftercounts: unique longest six-token context and sole
M318match.2273p66/PDF77and2541p74/PDF85 bothclear100001. Strings:
2273=M216 M123 M171 M059 M336 M089 M216 M254;
2541=M053 M171 M059 M336 M089 M216 M254. No semantic equation or graphicfusion
established. This is a valid variable-length initialslot in these two catalogue
records, not an inferred personalname/title or universalboundary.

1548p54/PDF65 verifiedagain via retainedcrop: M121 M342 M318,100101.3155p89/PDF100
has M121 M342 M391 M099,100112, and extra solusM397,abbreviation23→100123. Both
on side0, lines1/2, not separate sides. Direction2onfirstline differs from1548's
direction1; normalizedstringsstillRTL. Extra line recoveredseparately, not
concatenated. Initialnavigation renderedPDF103, corrected to100aftercheckingOCR
ranges. Nativecrops/coordinatespreserved. Noartifactphoto/autopsyjoinclaimed.

M318is not authenticated as fusionofM391wheel andM099two-strokes. Its replacement
is therefore structural evidencewithout a demonstratedgraphicdecomposition.
M317'ssoleindexedfieldhasloss/doubtfuldirectionand supplieszeroeligiblecomplete
fields; no negative semantic conclusion. M316componentunresolved, notinvented.

Added screen and primarysource assertions to offlinepipeline. All417indexrows
receive qualifiedprofilesincludingzeros. Corrected REPORT'sunqualified"partly
compositional"phrase to distinguish graphicalcomplexity from unestablishedsemantic
composition. Mainreport, twoledgers, protocol, raw-derivedcrops, fiveprimarylines,
scriptandtests saved. Fullpipeline andprovenanceverificationfollow.

### 2026-09-25 — Completion of this phase's verification

Resumed the exact live pipeline/render handles after the continuation; both
reported terminal exit0. No process was restarted on a timeout. The full pipeline
passed178tests. Parent then inspected the completed concordance render at printed
p699/PDF710:3155line02 is solusM397 within its own indexed group, before the next
M398 group. Added that source pin and concordance page flags to both3155lines.
An initial documentation patch missed a line-wrap context and applied nothing;
retried against the actual lines successfully. Updated research-date metadata.
Reran only the affected audit/index after this provenance addition; match counts
remain5902/3111 with independent pairwise agreement, no analysis-code changes.

Final checks verify205archived source byte counts/hashes and18distinct evidence
pins across the shape and primary reviews. All161local links inREADME and three
entry documents resolve. Raw extras remain onlyREADME and extractedmayig_LICENSE.
The index has417rows with two qualified screen profiles each,186with matches in
the broad screen, and all semantic/phonetic values null. Five primary lines are
saved with3155line2 separate and M397 confirmed. Source coverage is not reading
coverage. Refreshed manifest after this entry and verified its three hash groups
and source-registry digest. No new source downloads in this phase.

This phase is progress: two source parallels authenticated, one omitted line
recovered and an overbroad interpretation corrected. It leaves the actual
all-symbol decipherment objective active and unfulfilled. A concrete next lead
is the source-asserted crab/crab-plus-fish comparison (Parpola2009M57/M387), whose
specific semantic claim requires primary authentication and the same all-sign
controls rather than acceptance from a shared frame alone.

## 2026-09-25 — Published crab/crab-plus-fish hypothesis

Previous phase classified as progress: primary substitution parallels, recovered
M397 line, corrected composition wording. Followed the explicit Parpola2009
p50/PDF14 M57/M387 lead. No subagents retried after prior stream errors; parent
completed source inspection and computation locally. No new downloads.

Author proposes kooL/kooL-miin synonymy from identical subsequent text and reports
three crab+fish occurrences. The claim is not identical whole surroundings and
not universal crab-followed-by-fish. Preserved exact claim scope before testing.
Rawrecords show file-order M57=226032231798002693 and M387=226032798742060920.
Both reportedRL: shared reading suffix032226, preceding798231 versus798, with
different earlier strings. Source mapping231=P056/M070 markedfish, not plain
220=P050/M059. Crab798sourcefamilyP075/M053also lists193/797; no alias merger.

Initial expectedstrictfilename absent; inspected existing hindlegscript and used
lipi_strict.jsonl. Feature navigation printed requestedP050–P066entries then hit
non-numberedDefault_features in a numeric conversion; no data edits or counts
depended on failed conversion. Final script uses explicitIDset instead. Fishfamily
sensitivity fixed before counts: P050/P051/P056–P064, excludes compoundP052–P055
andbird-fishP065. Protocol freezesallrawscan, literal231/plain220split, relatedcodes,
no bridgingdamage, RLorientation, strictmembership, exactsuffixcontrols and prior
M77wholecontextquery. Existing source translations never imported into results.

Photographicnavigation: PDF63M58–60 correctedto62M57;130M376–381 then132M391–396
correctedto131M387.393wasKhirsara/Lohumjo-darophotos,400addenda,405otherMmetadata.
Exactmetadata eventuallychecked402p366M57and404p368M387. Redundantnavigationrenders
retainedasderivatives. Fullphotos and nativecrops show localpincer/leaf-like form,
markedfishinterventiononM57, itsabsenceatcomparedboundaryonM387, andsharedtwo-long-
strokes/cagedfishending. DoesnotauthenticateallfineWvariants, species or meanings.
M387Poorflagretained; originalandimpressionchecked, no autopsyclaim.

Exactjoins: M57=Finnish2340=DK5742=ASI63.10.89,HU175. M387=Finnish2041=DK10231=
ASI63.10.209,HU202. Finnishnumbers not treatedasM77IDs. M57squareunicorn-bearing
andM387rectangularwithoutthatmotif differphysicallyandinearliertext. Cropsboxes
and13evidencepins savedwithprimaryreview; paperpagevisuallychecked.

5680rawrows yield151literal798occurrences/rows,104strict. Initialdescriptiveneighbor
tableincluded7unknown000positions; correctedfollowingcode toNone while preserving
rawneighbor/row. Newtestguards000, separators, uncertainty, anddirection. Literal
798→231 appears6rows: H132,M57,H2584,M606,M1303,M1568. Fourstrictrows collapse
to3distinctcomplete strings becauseM606/M1568sameentiretext. Twofragmentrowsremain
excludedonlyfromstrictsummary. This couldaccordwiththree texttypes, notproof of
author'sexactselectionandnotthreephysicalobjects. Two distinctstrictstrings lie
outsidenamedM57/M387; no independentlyknownmeaning orhistoricalblindness.

Exact798→plain220zero. Predeclaredfishfamily35neighbors, including240twenty,
231six,233six,235two,236one. Descriptiveadjacency only, no enrichment/astral inference.
Related193threeand797fourrows yieldzero231adjacencies; notmerged. Author'suseof
fishmayincludevariants, so plainfishzeroisnotmisrepresented asrefutation.

Strictliteralprefix226032 yields5rows:M1793next060,M57next231then798,M70next002,
M387next798,M811next803. Five differentnextcodes;4distincttwo-codesequenceswhere
available. ConditionGood/Fair/Fine leaves3cases, removesM387/M1793; syntactic
strictnessisnotimagequality. Allfullstringssaved. StrongerM77wholecontextM053↔
M053M070,bothorders, haszeroexamplesinbroadandstrictpreexistingall-signscreen.
Qualifiedcrosswalk/incompletecorpuslimitsretained; thisdoesnotrefuteweakpublished
suffixclaim. Sourceexposedlayoutchecksandunanchoredrecurrencescannotestablish
semantic/phoneticsynonymy.

Added script, protocol, photo ledger, two meaningfultests and offlinepipeline
step. Reportpreservespositive localparallel and specificremainingambiguity.
All417establishedsemantic/phoneticvaluesremainnull. Fullvalidationfollows.

Final verification: full offline pipeline exited0 with180tests passing. Renamed
the output flag fromauthor_exposed to named_in_selected_argument to avoid implying
historical blindness for other examples; reran the affected two tests and audit,
all passed with unchangedcounts. All205source byte counts/hashes and13newreview
evidence pins verified. All140local links inREADME, REPORT andnewhypothesisdocument
resolve. Every result input hash matches, unknown000is not a validneighbor, and
no rawtranslation/Sanskrit columns appear in occurrenceoutputs. Existing417-row
index retains null meanings/sounds. Manifest refreshed afterthisentry and all
three file-hashgroups plus sourceregistrydigest verified. All downloads remain
in the shared rawfolder; no downloads addedinthisphase.

This is progress in testing a specific phonetic hypothesis against exact object
photographs, correctly scoped distributional controls and duplicate-sensitive
counts. It doesnotestablishkooL,miin,synonymy,planetmeaning orlanguage. The goal
remainsactive andunmet. Further useful discrimination requires an independently
interpretable anchor or a new prediction beyond this source-exposed suffix pair;
additional unanchored matches alone cannot establish the proposed semantics.

## 2026-09-25 — Fish/gemstone assemblage hypothesis: source recovery and denominator audit (ongoing)

Continued from the inscribed-weight search. Existing stone/Dilmun cases supplied
no new same-object inscription–mass anchor. Fresh search found Mukhopadhyay's2025
fish/gemstone hypothesis; chose its Harappa8650 assemblage for bounded primary
checking. No sound or meaning assigned. Proceedings/SSRN5079207 and June2025
bulletin are different versions; retrieved the50-page publisher bulletin.
Old rmrl.in/bulletin URL gave404, archived HTML (5318bytes), not a PDF. ResearchGate
returned429 and was not retried/bypassed. Defaultcurl DNS failed. Current RMRL
publications page linked the S3 PDF; webfetch hit10.9MB limit, escalated publiccurl
succeeded. All downloads retained in data/raw and registered. Primary Vats pages
58,59,60,435 retrieved from Archive18220 and visible page numbers checked.

Original narrative supports jewellery/bead association in H12/21 and I12/1 at
4–7ft. Nearby10928a location is I11/15, not OCR I11/13. Seven incised/sealing
catalogue groups a–g include nine b and four c objects; g has broken iconography
and no established surviving text. 8650h is gold bead/boss; 8650i weights26.3/4.3g;
8650m is decorated bead. The weights are separate objects, not inscribed mass
anchors. NarrativeIV versus p435 catalogue8650q StratumIII retained unresolved;
same squares/depth not proof of a closed workshop deposit or single event.

Figure4's core fish groups a,c,d,e and non-fish b,f reproduce claimed4/6 if each
letter is one complete inscription type. Initial arithmetic under that premise
was7/17 objects (gunknown excluded), but this is NOT a verified corrected rate.
A secondary export lookup (only identity and text fields used analytically)
flagged multiple different plate IDs under8650b. Original Vats tables now
confirm433,439,458 onp348 and486,488,489,493 onp349 all assigned8650b, all4–7ft.
PlateXCVI/PDF200 visibly shows differing inscriptions under these IDs. Thus
Figure4's nine-identical-b premise requires correction/reconciliation, rather
than simply contrasting4/6 with7/17. The secondary export alone was not accepted
as primary proof. Full modern crosswalk and corrected whole-assemblage numerator
remain unestablished. Some raw search output exposed proposed readings, but these
columns are excluded from structured analysis, evidence ledger and conclusions.

Navigation: archive page map labelsleaf374 as348, but image visibly346; retained
and renamed accordingly. Actual348 isleaf376; existing349leaf377 correct.
First attempted script name extract_pdf_pages.py and m77_candidate.jsonl didnot
exist; corrected to available inspector and candidate_records without changes
to data. Original platesrendered190,194,198,200,202,204,208,210. Native detailed
crop and reconstruction metadata being saved. Independent method agent reviewed
counting units, baseline dependence and semantic nonidentifiability, then was
asked to independently inspect the newly found primary-table contradiction.

Completed the bounded audit. Independent agent inspected originalp348/p349 and
PlateXCVI and confirmed differing433/458/489/493 face combinations within the
exact8650b group. Seven primary numberedplateentries are retained; not promoted
to a corrected population count or seven independent observations. Secondary
exactsite+excavation/plate joins recover7objectgroups/12rows/7distinctrawmultiline
signatures, corroboration only. No complete glyph verification or translation
import. Figure4 represents7of8 later same-areaobjects; omitted8154 isfragmentary.
10928a comprises2objects(onebadlybroken) butoneFigure4panel. Corrected numerator
and denominator remainnull; changes could affect both and no effect direction
is claimed. H366/8650e fish is an explicit separate-face description inVats,
but a symbolfield rather than text token insecondaryexport: classifications
must be harmonized before any automaticfish-count comparison.

Persisted docs/GEMSTONE_CONTEXT_AUDIT.md, independent GEMSTONE_METHOD_REVIEW.md,
protocol andprimaryreviewJSON, exactcropboxes, auditandrenderingscripts, and
results/gemstone_context_audit.json. Retained36primary/derivativeevidencepins.
Crops433labeland493leftedge initiallyclipped and werecorrected/reviewed; whole
plate alwaysretained. render_gemstone_evidence.py reproducedallimages withsame
hashes, followedby successfulaudit. Evidence indexing doesnotinventsemanticor
phoneticassignments. The hypotheticalbinomialtailcalculation inmethodreview
was independentlycheckedagainstclosedpolynomial, nottreatedasempiricalpvalue.
Two meaningfulnewtests guardfind-group/objectcountconflation, siteandexactID
boundaries, no translationimport, unknownfishstatus and probabilityarithmetic.

Full offlinepipeline exited0 with182tests passing. All213retainedsources
(182downloads,26webcaptures,5archivedHTTPresponses) haveverifiedbytecounts/hashes.
Onlydata/raw/README.md andmayig_LICENSE areoutside source-entrylisting, asbefore.
All152local links inREADME,REPORT andbothnewdocuments resolve. All36newpins and
resultinputhashesverified; all417indexsemantic_value andphonetic_value fields
remainnull. The source-map error and failedweb/downloadroutes remainlogged.
Manifest refreshedafterthisentry anditscode/docs,result,processed/sourcehashes
verified separately. The goal remainsactive/unmet; thisphase rejects an
unsupportedcountingsimplification, not the broaderpossiblefish/commoditylink.
Nextusefulwork: reconciled8650multiplicities/completefaces or independently
classified comparisoncontexts; avoid treatingalready-publishedexamplesasblind
semanticpredictions.

## 2026-09-25 — Chanhudaro fish/workshop comparison (ongoing)

Previous goalturn classifiedprogress: source-verified Harappa8650 catalogue
contradiction and reproducibleaudit. Continued with2025bulletinFigure5 rather
than treatingunknownmeaningsasresolved. Two boundedagents workedindependently:
archaeologicalcontext (withoutfishcounts) andfigurelabels/colors. Initialsite
fieldprobe includedothernamescontaininghan; allanalysisrestrictsexactChanhu-daro.
Protocolsaved before newrawfishcounts, afterpaperclaimandagentfigure5/8finding;
therefore source-exposed, notpreregistered semanticvalidation. Fixedfishfamily
P050/P051/P056–P064 reusedfromcrabaudit, plainW220sensitivity; unmappedW221 and
excludedcompoundcodesarenotautomaticallycounted. Absence isonlyselectedfamily.

Figureagentindependentlycounted47CISIIDs/46panels/17orangeacross17squares.
9/Dshows8IDs/5orange inbothmapandinscriptionpanels, notprose9/6. C87isatag;
C35/C38shareonepanel; C53/C58areseparatebutnear-identicaldrawings. Figurative
selectionincludespottery/metalimplements, notpureseals. Noassertionthatninth
artifactneverexisted. C38diagram/exportcontent-gridmismatchremainsunresolved.

Downloadedprimaryleaves61/62/64/66/72/77/263 and35/312/313; allvisibleprinted
numbersverifiedbycontextagent. Originalp52explicitlybeadworking8/C9/C9/D9/F
andelsewhere. Whole9/D isnotoneworkshop, andnon9Dsquaresarenotverifiednegative
craftcontrols. Room215,passage286,courtyard297 distinguishable; latter8/C.
Same loci spanmultiplelevels. CH2297 narrativejustbelow6.8ftvs catalogue10.0ft
unresolved. Weightcounts14room215,15corebuilding,22includingneighborhood distinct.

Primaryp293LII5CH4852=Cutting9/F469−2.8ft, supportedp15; secondaryC6says9/D.
Primaryp292LI14CH3215=9/B283+6.9ft; secondaryC74says9/D, butdifferentobject
cone3461at283islisted9/Dp57. Retaincatalogueoverlayasqualifiednotfinaltruth.
Primaryp293LII29CH3811=Cutting9/F468+3.8ft; secondaryC57's8/C289+8.6matches
DIFFERENTprimaryCH3492LII32. Causeunestablished. Rawexportunchanged.
LII12CH2558=9/D106+8.8ft, loweranimal-legfragment; no survivingtextestablished,
notanaddednegativeinscription. Originalplatenavigationfirstguessed393/395using
incorrecttwo-leafincrements, gotpottery; retained. CorrectLI416/LII417retrieved
andvisuallychecked. All14downloads incommonrawfolderregistered.

Initialsquareparser usedwordboundarybefore'sq' andmissedconcatenated215sq.
Meaningfultestcaughtfailure; changedtonegativeletterlookbehind allowingdigit
adjacency. Initialinvalidallunknown-squareoutputoverwrittenaftercorrection;
nointerpretiveconclusionsusedit. Testsnowpass. Firstcompleteaudit:72sourceobject
clusters/74rows. Raw9/Dseals5positive3negative1unknown/9; otherknown15positive
21negative9unknown/45. Selectedthreeprimarylocationoverlays yield9/D5positive
1negative1unknown/7; otherknown15positive23negative9unknown/47. Same9/Dpositives
C10,C53,C58,C65,C79; C22unknownincompleteflag,C55negative. C53/C58identicalrawtext
meansnotfiveindependenttexttypes. AlltypesincludesC87tag:5positive2negative
1unknown/8.8/E3positive/4. PlainW220in9/D2positive2negative3unknown/7.
Fixed-margintails.249raw/.058overlayareexplicitlydescriptiveNOTconfirmatory;
missingness,selection,clustering,unverifiedcontrolsandcohortdifferencesremain.

Retrospectivecoarsesensitivityaddedaftermaincountsandloggedprotocol:fourp52
explicitlynamedbeadworksquares20seals8positive9negative3unknown; remainingknown
34seals12positive15negative7unknown. Complementunclassifiednotnon-beadwork.
Outside9/Dbutinothernamedbeadsquares13seals3positive8negative2unknown. This
preservespositive localpatternwithoutpromotingit tocommodityorphoneticvalue.
Mainreport,figureinventory,contextreview,protocol,audit,primaryledgerandtwo
scientificvaliditytests persisted. Fullvalidation and independentcountcheckfollow.

IndependentcomputationalreviewusedaseparateCSVparser/tokenizer andexactrational
arithmeticwithoutimportingparentaudit. All72objects'primaryfamilyandplainW220
classifications, raw/overlaidcounts, andfixedmargintailsagree. ReviewscriptsHA
pinnedinCHANHU_FIGURE5_REVIEW.md. Same-locusC53/C58dependencyandallunspecified
phasefields highlighted. LiteraltypeSEAL:excludesbareSEAL C23, butunknownsquare
meansitdoesnotaltertarget/comparatorcounts. Fishsymbol sensitivityaddsnoobjects
because none ofsite'ssymbolfieldscontainsfish. No currentinputlogicbugfound.
Clarifiedprimaryledgerwording: tagC87isamong8IDs, notamong5orange. Rebuilt
resultafterthatwordingchange; no numericalchanges. Primaryrawsourcefilesunchanged.

Finalverification: fullofflinepipelineexited0 with184tests passing. All227sources
(196downloads,26captures,5archivedHTTPresponses) bytecounts/hashesverified, with
onlyrawREADME/licenseoutsideentriesasbefore. All147locallinks inREADME,REPORT,
mainChanhudaroaudit andtwoindependentreviewsresolve. All32primaryevidencepins
andresultinputhashesverified; all417establishedsemantic/phoneticvaluesremainnull.
Manifestrefreshedafterthisentry andall3hashgroups/source-registrydigestchecked.
Thisphaseisprogress: source-verifiedcontext/provenancechanges andanindependently
reproducedpositivebutqualifiedspatialpattern. Itdoesnotestablishfish=gemstone,
anypronunciation, or a complete decipherment. Goalactive/unmet. Nextusefulstep
wouldneedindependentlyclassifiedmatchedcontexts andcompleteartifact/phasejoins,
or an independentcontent/name/measurementanchor, ratherthanmoreuncontrolled
counts from the same illustrative source.


## 25 September 2026: M-294 jewellery-hoard context and clipping audit

Continued from the Chanhudaro phase by testing the 2025 bulletin §3.1 claim
that CISI M-294 comes from an undoubted jeweller's shop and certainly preserves
its complete three-sign inscription despite clipping. This is a source-exposed
investigation, not an independent discovery or preregistered test. Delegated
original room archaeology and an independent photograph review; the parent
checked CISI identity and searched literal corpus parallels.

**Identity and source acquisition.** CISI1 printed71/PDF107 shows the original
and impression. Metadata printed368/PDF404 verifies Finnish1376, HR4212e,
ASI63.10.378 and HU448. Finnish1376 is not assumed to be a Mahadevan text number.
The initial metadata guess PDF403 ends at M272; retained as a navigation attempt.
Exact-string web searches returned the known paper and irrelevant results.

Nine new files were downloaded into data/raw/ and registered: two Archive
search responses, volumeI metadata, OCR TXT/XML, scandata, and printed189/193/194
(leaves231/235/236). Scandata lacked printed labels; XML page objects supplied
the mapping. Initial leaf235/237 downloads failed with connection resets and
left no files. Leaf235 succeeded on retry; 237 was not retried because page194
contained the substantive find. Page195 OCR describes another seal HR5193/306
south of HouseVIII, not another Room8 seal. The nearby kiln description refers
to HouseVII courtyard17, not Room8 goldsmith production. The original image
pages and eight page-linked OCR extracts are persisted; OCR is navigation data.

**Archaeological result.** VolumeI194 places the find immediately beneath the
floor of Room8 (8×7ft), expressly including fragmentary seal CXII376 and a chert
scraper. VolumeII376 identifies seal376 as HR4212e. VolumeII493 describes silver
vases HR4212d/c with ornaments, beads and much scrap. VolumeII522 describes
Hoard3 HR4212a, Room8, HouseVIII, Block2, SectionB, six feet below the contemporary
surface. Most beads lay loose in soil with indications of former cloth wrapping.
The author infers probable goldsmith ownership from waste metal and rolled-up
ornaments retained for remelting. This supports a coherent occupationally
associated hoard, but does not prove an active production or retail room.
The seal is not placed inside a specific vessel by these passages.

VolumeI189 and volumeII493/522 agree on Block2; the secondary CSV says block-house
1VIII. Raw data remains unchanged. Original phase attribution does not independently
date the inscription. The parent visually rechecked volumeI194 and volumeII522.
Eight contextual claims are linked to pages, and all eight unique source/image
files have byte/hash pins in m294_room_context_review.json.

**Literal parallel search.** Protocol m294_protocol.json was saved after reviewing
the named rows/photo but before new counts. audit_m294.py searches 2,914 existing
strict secondary rows in exact Wells file order. W740 W220 W003 has five exact
rows (M294, M1439, M1441, M1442, M1443) and five longer-containing rows (H1056,
H68, K9, M725, M1429). All five longer rows have extra file-left/read-suffix
signs; four also have file-right/read-prefix signs, conditional on reported R/L.
W520 W220 W003 has one exact row (M1912) and one longer row (M1672), with a
reading-prefix extension only. W520 and W740 are not merged. These witnesses
include different object types and have not all been newly photo-authenticated.

The strict subset includes M294 because the source says complete=Y, although
preservation=fragment and condition=Poor. That editorial judgment is not an
independent completeness measurement. A direction/boundary test checks both
extension directions, unknown reading direction, intervening uncertainty, and
literal distinction between the two ending codes.

**Correction preserved.** The parent's first image note conflated seal and mirrored
impression, incorrectly placing clipping on the impression's stroke-side right.
The independent enlarged-image review corrected this: original M294A is clipped
at photo-right; impression M294a at photo-left. Both show the same physical edge
beside the ending-shaped form. The parent checked the enlarged crop, corrected
the primary ledger and draft report, and added a retrospective protocol note.
Thus file-left/read-suffix extensions are geometrically relevant; prefix counts
are supplementary and do not locate the break. Counts themselves did not change.

The seven hashed files in the independent completeness review show three visible
sign groups and surviving space near the ending. A complete short original is
reasonable but unresolved. The bulletin's dashed outline and restored animal
parts are reconstructions, not independent original-width measurements. No extra
lost glyph is identified. Neither completeness nor incompleteness is established.

**Persistence and conclusion.** Main report, README, three M294 reports, protocol,
source ledger, extraction script, audit script, test and result JSON are saved.
All three reviews are required audit inputs. The source review supports a seal
associated with probable goldsmith property, but not fish = gemstone, a tax rate,
a language identification or any phonetic reading. All 236 source records
(205 downloads, 26 captures, five HTTP responses) passed byte/hash verification;
only raw README and mayig_LICENSE lie outside the registry, as before.
Full offline pipeline was started once; final verification follows below.

Final checks: the full offline pipeline exited0 with185 tests passing. All161
local links in README, REPORT and the three M294 reports resolve. The final
pin-count check caught a schema mismatch: the independent completeness review
called its seven file hashes source_pins, whereas the parent audit verifies
evidence_files. Renamed that ledger key and reran the affected audit so all
22 review-file pins are now actually verified by the pipeline code; numerical
results did not change. All417 established semantic/phonetic values remain null.
The manifest is refreshed after this entry and all three hash groups checked.

This phase made progress by verifying an exact hoard association, correcting
provenance and mirrored-image orientation, and bounding a completeness claim.
The decipherment goal remains active and unmet. The next useful semantic test
requires independently classified comparison deposits or an external contents,
name or measurement anchor, rather than treating one occupational association
as a translation key.


## 25 September 2026: Kalibangan pipes and chain-sign matched comparisons

Previous goal turn classified as progress: it verified M294's hoard association,
corrected block provenance and mirrored-edge interpretation, and saved an audit.
This phase tests the 2025 fish bulletin's remaining proposed contents anchor:
Kalibangan pipes said to hold gemstone-bead strings, together with its chain-sign
co-occurrence argument. Delegated primary archaeology and independent figure
review while the parent specified and implemented the corpus comparison.

**Primary acquisition and archaeology.** Reused Kalibangan2020 PartII. Downloaded
ASI's official PartI files60 and61 to data/raw/; both registered with byte counts
and SHA256. File60 has330 pages and is only the first segment; file61 has415
pages and contains the needed catalogue. First attempted figure page249 was
ordinary pottery p557/fig9.92; retained. Correct pipe plate9.91 is p555/PDF247.
Architectural page98 was p76; plan5.24 is p77/PDF99. Initial rendering emitted
fontconfig warnings but succeeded; later runs used a writable cache.

PartI p74 says pipes were not in situ. Its p556 assigns the fish (M59) to21582
and connected ovals (compared with M415/417) to21583. PartII p1060 places the
pair in KLB1 ZA8 quadrant3, PhaseV, latePeriodII residential context. The socket
fit and reported56cm joined length are real evidence. Studio photographs do not
explicitly establish excavation already joined or original marked-face alignment.
The source's large-house/important-person interpretation is not a named merchant.
No bead contents, closures, residue, packaging or firing-relative incision timing
are reported in the checked pipe entries. Nearby general pottery discussion of
pre/post-firing marks does not classify these pipes. The long drainage comparison
quotes a Mohenjodaro installation; it is not Kalibangan use-wear evidence.
Parent visually checked p556 and the PartII fish-pipe photograph.

Two exact identity cautions remain. The secondary fish row K447/5351.1 assigns
21583, conflicting with the primary prose. K446/5350.1 has chainW215 but lacks
an excavation number; no silent assignment to the other registration. A naive
initial substring search for21583 also returned unrelated DK12158332/M1126;
rejected by site/exact identity. K20, used as a chain-sign seal analogy, belongs
to ZE10 earlyPeriodII/reg18902, not the late ZA8 pipe context.

**Published figure count.** Figure7A displays13 rows but12 distinct CISI labels;
M324 appears twice. Raw2842.1/.2 have identical text, excavationID and sides=2.
Fifteen chain-bearing rows across14 object groups comprise13 seal rows plus
K446 pipe and potteryM1599. Nine seal rows have more than two certain tokens.
H656's two surviving signs do not establish original length2. M1783 has missing
text. Unknown targets in unreadable rows are retained as unknown, while surviving
positive signs remain usable. The four named positives are fishM46/M636 and
U-shaped candidatesW705 inM1765/W706 inKrs1. M636 is incomplete and damaged.

**Consequential candidate correction.** Before new counts, protocol provisionally
identified W480 from the shared glyph in M1765/Krs1, expressly pending image
review. The first probe therefore produced5 union-positive rows and a small
W480 matched tail. The independent reviewer initially made the same inference,
then checked section4.1's actual pictures and corrected it: the author means the
U-shaped forms W705/W706, not the caretW480. The incorrect initial protocol and
probe result are preserved as pipes_initial_W480_protocol.json and
pipe_chain_rejected_W480_probe.json, explicitly superseded. No gold reading or
fifth positive M268 is inferred from that probe. Final targets remain exact705/706,
without expanding automatically to704/707. This is a retrospective correction,
not a preregistered choice. A later independent check caught stale W480 wording
in protocol target labels; corrected those labels before the final audit.

The raw certain-token parser was tightened to exclude slash-adjacent alternatives
and unknown000/999 rather than counting them as certain signs. Missing target
signs in incomplete rows now yield null rather than false. The matched strict
sample was unaffected, and the nine long-row count remained nine.

**Matched comparison.** Primary universe: single-row objects in the existing
strict corpus, complete=Y, preservation=complete, type startingSEAL, length>2.
Strata: site, literal type, exact length. These source-exposed rules were saved
before new counts; this is exploratory calibration. There are931 objects and
six chain cases. Fish-family1 observed/2.748506 expected, plainW2201/.836537,
U705/7062/1.927799, union3/4.031219. Exact upper tails respectively .989466,
.619671,.651758,.945658. Deduplicating whole sequences within site/type leaves918
text types and nearly unchanged results; uniontail .945934. Khirsara's one-object
stratum contributes a fixed positive, not independent comparison information.
The long-text union is already common in matched Mohenjodaro strata (18/25 at
length8 and17/18 atlength9). Small selected sample, grammatical positions,
chronology and actual craft contexts remain uncontrolled; these are descriptive
null comparisons, not proof of no association or rejection of bead semantics.

Independent verification used a separate selection and all64 Bernoulli-outcome
patterns for the six one-chain strata, with exact rational arithmetic and no
production-audit import. All eight comparisons, margins, means, full distributions
and fractions agree. Verification script and output are saved and integrated
immediately after the production audit. Two tests exercise exact fixed-margin
calculation, length strata and uncertain-token exclusion.

**Inference.** Physical compatibility and co-occurrence are verified observations.
Bead contents are not independently identified. Inferring bead storage from
hypothesized sign meanings and then validating those meanings from inferred
storage would be circular. All417 established values remain unresolved. Saved
three reports, protocols, raw sources, evidence ledgers, extraction/audit/verifier
scripts, tests and results; README, REPORT and HYPOTHESES updated. Full offline
pipeline and final hash/link checks follow below.

Final verification: the full offline pipeline exited0 with187 tests passing.
All238 source records (207 downloads,26 captures,five archived HTTP responses)
passed byte/hash verification; raw extras remain README and mayig_LICENSE only.
All180 local links in README, REPORT, HYPOTHESES and the three pipe reports
resolve. All27 primary/figure file pins and both audit/verifier input-hash sets
verify. All417 established semantic and phonetic values remain null. The rejected
W480 probe now points to its preserved initial protocol path with the same hash;
its raw token listing is explicitly labelled as predating the parser correction.
The final manifest is refreshed after this entry and all three hash groups checked.

This turn made progress: it authenticated a proposed object anchor, recovered
primary context and registration conflicts, reproduced the published examples,
and independently calibrated them against a specified comparison. The full
objective remains active and unmet. Useful next evidence would establish contents
or another external referent independently; these pipes cannot presently fix the
meanings of the fish, chain or U-shaped signs.


## 25 September 2026: L-51 motif and ending–fish association

Previous goal turn classified as progress: authenticated the Kalibangan pipe
pair and calibrated the selected chain-sign comparison. This phase examines
another proposed external referent, L51's claimed necklace motif, and the 2025
bulletin's accompanying greater-than80percent fish/metal association. Delegated
original archaeology and independent visual review; parent specified corpus
comparisons. This is a source-exposed audit, not blind semantic validation.

**Identity and sources.** CISI printed249/PDF285 provides original, impression,
back and edges. Initial metadata guessPDF409 was printed373, L99–266; corrected
to printed372/PDF408. L51=excavation11358, Finnish6037, LTH SRG1264, HU1019.
Museum accession is distinct from SRG2/C25 excavation context. Parent visually
checked the original and impression. Exact web searches found retained CISI and
bulletin pages, original Rao mirror and unrelated material; no new translation
claims from search results were treated as established evidence.

Five new Archive files were saved in data/raw/ and registered: search response,
Rao1985 metadata,638-page volumeII PDF, wrong-script OCR and page-number map.
The supplied OCR was unsuitable for reliable searching, so fresh Tesseract and
visual page review were used. Printed310 is PDF61, printed317 PDF68; initial
neighboring60/67 renders retained. Plate navigation sampled440/450/460/470 and
488/490, then located CLIX atPDF489. Initial wrong rotation was corrected to
clockwise90degrees. The very poor small C5 image cannot resolve finer motif
features. Agent initially included concurrent parent images in its hash-list
glob; corrected review scope to its own28 source/derivative files before delivery.

Rao310/317 establishes terracotta seal11358, plateCLIX C5, phaseIV, SRG2/C25,
pit sealed bylayer2, depth1ft, reversebuttonbroken. It offers seed-drill resemblance
without a diagnostic comparison. No jewellery contents or beadworking context
are stated in those passages. CISI says unidentified object. The bulletin's
necklace analogy remains plausible but unverified. Its Figure7C repeats CISI's
impression in the same orientation, not an independent original image. The
modern necklace better resembles the rows/fringe; the ancient necklace image
primarily resembles dangling projections and does not authenticate original
stringing by itself. No guild or commodity identity follows from these analogies.

**Claim scope and protocol.** Independent visual review confirms exact W527+W555
in the inline greater-than80percent claim onPDF25, repeated as the terminal pair
onPDF26 in M636. It does not explicitly depict W555 plus any possible ending.
Saved l51_protocol.json before new counts, after named examples and claim review.
Author-defined core segment has no executable boundary here; our whole remaining
text co-occurrence is an explicit proxy. W527/W555 file-prefix corresponds to a
reading ending only under reported R/L; all14 raw prefix witnesses report R/L.

Fourteen raw seal rows/groups have the exact prefix: fish/union11positive,
2negative,1unknown under source completeness flags. All14 observed fraction is
11/14=.7857; unknown-inclusive upper bound12/14=.8571. Excluding unknown gives
11/13=.8462, one possible explanation of greater-than80percent, not a recovered
author denominator. The U sign occurs on M1693 with a fish and adds no positive.
The raw ordinary fishW220 occurs only on damaged M636. Four pair occurrences
elsewhere—H21,M1917,M1053,M1293—remain separate, not relabelled text endings.

Independent review flagged M821: complete=Y but preservation=fragment, only
W527W555 visible. Preserve source-flag result, and add a retrospective conservative
preservation sensitivity that treats its absence as unknown:11positive,1negative,
2unknown; known-only11/12. No independent claim of original completeness follows.
The strict complete-preservation matched samples already exclude it.

**Positive structural result.** Complete-preservation, single-row strict seals
of length≥2 yield1082 records, nine exact-ending cases. Fixed margins within
site/literaltype/exactlength yield fish8 observed versus4.162527 expected,
upper tail649523/82608768=.00786264. PlainW220:0 versus1.214296; U705/706:1
versus.917820, tail.641097. Fish-or-U:8 versus4.492064, tail.01400224. Deduplicating
whole strings within site/type leaves1049 records; fish tail.00714892, union
.01310593. Among the nine ending records, modified fish are W235 on5, W231 on3,
W240 on2 and W233 on1, overlapping; no plainW220. This is a positive selected
pattern, not a semantic identification or a confirmatory test.

Restricting to the same W527 terminal leaves27 records. Seven of nine active
strata have only the selected ending record; the other two have one additional
control each, M833 and M133, both fish-positive. Fish/union count is therefore
fixed8, expectation8, tail1. This comparison is uninformative about W555's
incremental effect, not evidence of no effect. Selection, exact-stratum sparsity,
grammatical position, chronology, transcription and contextual confounds remain.

Independent verifier uses its own selection and512 Bernoulli patterns across
nine one-exposure strata, with rational arithmetic and no production imports.
All12 target×universe counts, margins, expectations and fractions agree; raw
counts and preservation sensitivity also agree. Saved verifier/code/result and
required it immediately after audit_l51.py in the offline pipeline. A meaningful
test checks terminal conditioning, internal-pair exclusion and unknown bounds.

**All-sign integration.** Added context_audit_links.json and conditional links for
M294, pipe-chain and L51 results into build_evidence_index.py. Twenty M rows have
candidate catalogue paths; all417 remain present. Each link preserves every M
candidate and W family member, and states that comparison targets need not occur
on the named artifact. A many-way mapping test confirms that W215's family link
does not collapse M415/M417 or assign a semantic/phonetic value. Index sources
pin the three audit outputs. No established values were added.

Saved three L51 reports, primary pages, protocols, audits, verifier, crop/render
scripts and tests. README, REPORT and HYPOTHESES updated. Full offline validation
and final source, link and manifest checks follow.

Final validation: full offline pipeline exited0 with189 tests passing. All243
source records (212 downloads,26 captures,five archived HTTP responses) passed
hash/byte verification; only rawREADME andmayig_LICENSE remain outside the
registry. All187 checked local links in README,REPORT,HYPOTHESES and the three
L51 reports resolve; ALL_SIGN_EVIDENCE was also updated with the integration.
All43 context/visual file pins and audit/verifier input hashes verify. The final
check initially assumed the verifier's hash key was input_sha256; its actual
key is inputs. Correcting the checker completed verification without changing
any result or analysis code. The index covers M001–M417 exactly once,20 rows
have qualified context links, all index source hashes verify, and every
established semantic/phonetic value remains null. Manifest refreshed after this
entry and all three hash groups verified.

This phase is progress: exact object/context authentication, a positive structural
association, explicit denominator and same-terminal limitations, and integration
into the complete evidence index. It does not establish the depicted object,
commodity, language or a full decipherment. Goal remains active/unmet. A next
useful step would test whether the modified-fish/ending relationship holds in
independently authenticated additional texts and obtain external evidence for
what either segment refers to; interpreting co-occurrence alone cannot supply
that referent.

## 2026-09-25 — Ending authentication, exact counterparts and a catalogue conflict

**Continuation assessment:** preceding work was progress: it added a reproducible
ending/modified-fish association, primary L51 context and an all-sign evidence
link. This continuation tested the strongest available structural lead against
additional originals and narrower alternative explanations. Decipherment remains
unachieved; neither a successful association nor verified code proves meanings.

**Protocol and computations.** Saved ending_validation_protocol.json after the
prior L51 analysis and before new counterpart counts. Search restricted to the
same1082 strict complete-preservation single-row SEAL-type rows of length≥2.
Deleting exactly second-token W555 from each of nine W527 W555 strings produces
zero complete-string counterparts, including across sites. This is no support
for an optional-marker interpretation, not a refutation in a sparse corpus.
Retrospective named-example exclusion removes only L51 (M636 already excluded):
1081 rows, eight ending cases, seven fish-positive. Site/type/length conditioned
fish expectation3.9125267, exact upper tail256039/10326096=.0247953341;
fish-or-U expectation4.2420641, tail29291209/688406400=.0425492979. Plain fish0,
U1; no new semantic evidence. This is explicitly not a blind holdout.

Other first-token search found two W526/W555 rows, each with an exact W527
substitution counterpart: L9/M1351 and M934/L89. No other token changes occur
in those pairs. The initial source complete flag was insufficient: primary
L9 photographs show missing upper-right original / upper-left impression corner
meeting the comb. W526/W527 intentional variation and whole-text completeness
therefore cannot be certified. A retrospective damage screen drops that pair;
M934 remains an unauthenticated candidate, not a confirmed allograph. Its
counterpart L89 is primary-checked. Fish-positive status survives L9's loss.

**India primary review.** Agent authenticated CISI M81, L89, M133, L9 identities,
photos and metadata. M81 and L89 support the modified-fish/pair order; M133 has
a different second sign W550 and modified/plain fish, supporting a positive
control outside the exact ending. Six exported M81 units include W617 as a
visually doubled grid: do not count that as two Wells tokens. Finnish numbers
are not Mahadevan text numbers. Navigation guesses PDF68,80,71,275 failed;
correct70,79,295,276 retained alongside them. M81 crop and L9 metadata crop
were corrected before final review. Thirty-seven evidence hashes recorded.

**Interrupted Pakistan review and recovery.** First agent stopped at a usage
limit after downloading13 sources, before writing its registry/review. A second
agent recovered12 JPEG URLs from retained Archive metadata and filenames,
re-downloaded in memory and byte-compared all12 exactly. The13th dynamic
metadata URL was inferred from embedded identifier corpus-vol-2, explicitly
not byte-reverified. That item's title/files describe Volume1: failed CISI2
lead, not Pakistan evidence. All13 downloads registered centrally and kept in
raw; no download lost or discarded. Recovery and crops have saved scripts.

Original FEM tables and impression plates verify60=DK12110,129=DK11349,
142=DK11456,583=DK7402. First agent initially split DK1211060 as DK1211+060;
printed table corrects this to DK12110+60. This correction is preserved. Original
impressions show no fish on60, two fish forms129, capped fish142 and capped
fish plus U-like form583. Proposed CISI aliases M940/M1081/M1351/M1693 are
consistent secondary joins, not independently checked CISI2 metadata. Bare
concatenated fields were not promoted to Mahadevan identities. FEM plate leaves
179/205 and table410 were wrong target navigation;375/394 retained unreviewed.
Other requested targets H459/M1320 and controls M833/M934 remain photo gaps.

**Primary M222 bridge.** Parent inspected Mahadevan sign list33/PDF44 and
34/PDF45: M216 and M222 are separately numbered shapes. Normalized primary
lines2060,2129,2142 show the M222-like crossed sign beside comb, with no fish,
modified fish forms, and one modified fish respectively. These line-level
checks alone do not prove artifact-number joins. A stronger independent identity
check links L89's CISI excavation15337 to M77 appendix text7090 excavation15337
(printed826/PDF835). Its normalized line printed151/PDF162 is compatible with
M267 M099 M065 M222 M254 and the photograph. Hence W555↔M222 is supported on
this artifact; source P230 grouping W550/W555 under M216 is not an exact
exhaustive conversion. Preserve source membership, annotate conflict, do not
replace all M216 mappings or collapse W550/W555. Substring OCR search initially
found PDF108 via7090 inside an object code; kept failed render, exact WORD search
located162. Fifteen candidate M77 rows ending M222 M254 were enumerated and
persisted, explicitly source-exposed/overlapping, not independent replication.

**Integration and verification.** Added audit_ending_validation.py, independent
raw-CSV verifier and meaningful tests for one-position deletion and a direct
primary conflict link coexisting with source-family membership. Independent code
reconstructs strict selection, both pair searches and256 binary outcomes for each
of four eight-stratum exact tails; every comparison agrees. Audit checks India,
Pakistan and mapping review file pins. Added both scripts to the offline pipeline.
All-sign index retains conditional P230→M216 links and adds explicit direct review
links to M216/M222/M254, including the conflict; no global conversion change and
no established values. New report ENDING_VALIDATION.md, two primary reviews,
README, REPORT, HYPOTHESES and ALL_SIGN_EVIDENCE explain the result and limits.
Full pipeline and final integrity checks are running; results recorded below.

Final checks: full offline pipeline exited0,191 tests passed. All256 source
records (225downloads,26web captures,fiveHTTP responses) passed SHA256/byte
checks; only rawREADME andmayig_LICENSE are outside the registry. All70 pins
across India37/Pakistan21/mapping12 verify. Both ending audit/verifier input
hash maps verify. All214 checked local links in the top-level reports and new
ending reports resolve. The index contains M001–M417 exactly once,21 rows with
qualified context links; all417 semantic/phonetic values remain null. Manifest
refreshed after this entry and all three groups verified. No full decipherment
claim is supported. Goal remains active; progress is a checked artifact bridge,
a correction to cross-catalogue use, physical preservation constraints and
reproducible tests of proposed structural interpretations.

## 2026-09-25 — Two crossed forms on one artifact and a context-wide mapping screen

**Continuation assessment:** prior turn made progress: authenticated L89↔7090,
retained the P230/M216 conflict, ruled out a proposed exact-deletion support in
its sample, and constrained a damaged allograph example. This turn investigates
whether the crossed-form distinction survives on the same object and whether
context matching can justify any global conversion. No goal-completion claim.

**Source-exposed discovery and protocol.** A preliminary rough raw-string
membership search returned111 W550 and24 W555 rows; this was navigation only,
not a validated denominator. It found M63 with both codes. The existing candidate
M77 corpus has3068 with both M216 andM222. These motivated the question before
screen protocol creation; this is not blind predictive evaluation. A parallel
agent saved pincer_context_protocol.json before computing its proper strict
screen. Select all93 of2914 strict Wells rows containing W550/W555; reverse file
order and compare only equal-length strings against1293 strict M77 candidate
rows. Target positions admit either M216/M222; every other position requires
explicit feature-derived family membership, preserving every alternative.

**Primary M63 identity.** Parent verified CISI printed366/PDF402: M63,
Finnish0223, DK8333, ASI63.10.12, HU98; impressionSi21p1:215. Mahadevan
appendix printed819/PDF828 independently lists3068, DK8333, Si21:215. The
shared excavation and photo references establish identity independently of the
computer's context match. Primary normalized line printed87/PDF98 contains
M216 M123 M222 M254 in candidate reading order; Wells file sequence is
W526 W555 W060 W550. No numerical meaning attached to the intervening form.

CISI photo printed28/PDF64 shows both crossed forms on the same seal,
separated by the stroke/curve form. Original and mirrored impression support
different treatments of open arm ends, consistent with primary sign list
M216/M222. Hence different sites or objects cannot be the sole cause of this
observed contrast. Position-dependent allography, scribal variation and separate
sign identity remain alternatives; co-occurrence does not establish two meanings.
The comb's extending stems survive and orientation differs from L89 in the same
impression orientation. No gross terminal corner loss like L9 is apparent;
minor wear/chipping remains. Independent agent agrees on the orientation and
preservation observation. This supports graphic variation, not interchangeability.

First photo guesses PDF66 (M67–69) and65 (M64–66) failed; retained both and
correct64. Reused extraction prefix pincer-cisi overwrote the small render metadata
JSON for66/402 when65 was rendered; preserved both invocations explicitly in
pincer_primary_review.json with page lists/scales, and all images remain pinned.
Crop script preserves original orientation without alteration. Primary Table I
already verified earlier gives M216 alone2/initial36/medial49/final3/total90,
M222 0/2/20/0/22. Reused these descriptive profiles; no new frequency sample
or significance claim. They do not resolve positional allography.

**Context screen results.** Of93 rows,36 have candidates:26 single-candidate,
10 multiple;57 unmatched. Twenty-three unmatched rows have an unmapped
non-target token,34 fail remaining exact length/context constraints.55 candidate
pairs;21 depend on a multi-candidate context family;seven Wells rows admit
both target M mappings. Assignment pair incidences:W550→M21627,M2226;
W555→M2166,M22217. These are overlapping pair incidences, not physical-object
counts. M63 uniquely matches3068, an implementation consistency check on an
already selected example. M897/W550 admits M222 contexts1158/2545/7090:
retain as a primary-review target, not as a proved global counterexample or
identity. Neither automatic global split nor automatic merge is warranted.

Saved screen script, full candidate/unmatched lists, protocol and report, plus
two focused tests covering reversed alignment, exact length, unsupported-context
rejection and many-way membership/provenance. Saved M63 primary review,
hash-pinned manual observations, reproducible crops and audit that keeps primary
identity separate from compatible-text matching. Integrated scripts into offline
pipeline and direct M216/M222/M254 context links; source family table unchanged.
README,REPORT,HYPOTHESES andALL_SIGN_EVIDENCE updated. M934 primary investigation
runs independently; its result and final validation will follow here.

**M934/MIC158 follow-up.** Parallel review located exact original table:
MarshallII printed403/localPDF54 gives seal158=DM50,0.95×0.95in,typeB,white
steatite,4ft7in below surface. No room/workshop context is supplied for the row.
Original volumeIII Archive48270 leaf191 contains numbered158 impression and
supports comb/crossed/capped-fish/two-strokes/interior-marked-diamond sequence.
Compared in the same impression orientation, the comb reverses L89's staggered
uprights while following signs keep the same order. Square animal-bearing158
and rectangular text-onlyL89 are distinct artifacts, not mirrored duplicateviews.
Neither has L9's conspicuous missing combcorner in these illustrations; imperfect
image quality and no physical autopsy limit preservation claims. This strengthens
an orientation-variant hypothesis in a matching context, not equalmeaning/sound.
CISI2's ownM934metadata remains unverified; the alias is a consistent secondary
join to authenticatedMIC158/DM50, not a fully certified catalogue entry.

Parent independently inspected M77appendix printed818/PDF827: MIC1–560 map
respectively to references1001–1560. ThusMIC158→1158 is established by an
explicit source rule, not inferred by adding1000 to an unexplainednumber.
Primary line1158 printed43/PDF54 matches M267 M099 M065 M222 M254, the same
normalized sequence asL89/7090. Exact OCR1158 search failed because the OCR
splits1 158; neighboring page inspection located54, then visually checked.
Agent's original report correctly leavesM77bridge outside its scope; parent
supplementrecords the addedverification separately, preserving its23filepins.
Parent draft initially supplied an unverifiedRomanplateCVI; removedbeforefinal
because the scanheading iscropped. Exactleaf191 andseal158 are the certified
locators. Agent's failedplate leaves203,183,189 are retained; correct191.

Nine newdownloads (search,metadata,OCRtext/XML,page mapping,fourleafJPEGs)
registered indata/sources.json andretained inraw. Added download/crop scripts,
M934_PRIMARY_REVIEW,COMB_VARIATION_REVIEW,sourcepinJSONs andaudit_comb_variation.py.
Auditchecks rawW526/W527-only difference andmatchingcandidateM77lines against
separatelyreviewed identity evidence. Addedpipeline step andM254 directcontext
link. EarlierENDING_VALIDATION now points tothislater update ratherthan quietly
claiming itsoriginalM934investigationwascomplete. PriorL9damage finding retained.

Full pipeline completed with193 tests andallpincerscreen/primarychecks passing.
M934supplement arrivedafterthat run: itsnewauditwas executed separately andpassed,
thenall-signindex rebuilt. All417valuesremainnull; finalsource,pin,link,andmanifest
checks follow. No broad test rerunneeded for these additional sourceannotations;
the newscript's entire executable check was run against its actual inputs.

Final integrity:265 source records verified (234downloads,26captures,fiveHTTP
responses), withonlyrawREADME andmayig_LICENSE outside registry. All48 new
reviewpins verify (M63review19,M934review23,parentcombsupplement6). Allthree
newanalysis inputhashmaps andeveryall-signindexsourcehash verify.225local
links resolve. M001–M417eachoccurexactlyonce;21rows havequalifiedcontextlinks;
allsemantic/phoneticvaluesnull. Refreshedmanifestafterthisentry andverified
allthreehashgroups. Thisturnisprogress: within-artifactgraphiccontrast,
authenticatedmatching-contextorientationvariant,andcompletecandidate-screen
failure/ambiguity accounting. Full decipherment remainsunresolved andgoalactive.
Nextdiscriminatingtargets includeM897's apparentW550/M222context inconsistency
andprimaryshared-objectreviews sufficient to distinguishmeaningfulcontrasts
fromorientation/positionalallography. No externalreferenthasyetidentifiedmeanings.

## 2026-09-25 — M-897 identity, unresolved fine reading and conversion sensitivity

**Continuation assessment:** the preceding turn was progress: it established a
within-artifact crossed-form contrast and a primary-supported comb-orientation
counterpart, and enumerated a systematic candidate screen. This turn investigates
that screen's most informative exception rather than silently accepting a global
conversion. No full decipherment or established meaning is claimed.

**Protocol and selection.** Read M897's raw row3302.1: W527 W550 W235 W002 W817,
excavation field DK9111545, preservation=fragment, complete=Y. Those flags are
not equivalent. Saved pincer_preservation_protocol.json after seeing that fragment
flag and before calculating the sensitivity partitions. This is retrospective and
source-exposed, not preregistered independent confirmation. Compare four fixed
maps: local split W550/M216,W555/M222; reversed split; bothM216; bothM222.
A row is compatible only when one whole candidate pair satisfies every target
occurrence simultaneously. No mixing positions from different candidate texts.
Rows without a candidate are uninformative, not model failures.

The all-row partition has93 selected rows,36 with candidates. Compatible counts
are35/8/26/16 respectively; only M897 is incompatible with the local split among
candidate-bearing rows. The literal source preservation=complete partition has
72 rows,27 with candidates; counts27/6/20/13. Requiring at least two non-target
positions gives67 rows,24 with candidates; counts24/4/17/11. The45 and43
unmatched rows in the last two subsets remain explicit unknowns. These are
existential compatibility counts conditional on the already constructed candidate
set, not mapping accuracy, statistical significance or authenticated object counts.
Dropping the anomalous fragment retrospectively cannot validate a favored rule.

Known earlier L9 damage remains in the source-complete subset. Added its prior
primary corner-loss annotation (and the other previously reviewed India objects)
without changing the fixed selection/counts. Unreviewed rows use null, not false.
M63, despite strong primary comparison, drops out of the literal complete subset
because its source calls it slightly chipped. These examples show why source flags
cannot substitute for physical review.

**Primary exception check.** Parallel reviewer reused FEM plateXCVII/Archive
leaf207 and located numbered545; downloaded exactly one new table leaf408,
printed386. It explicitly links FEM545 to DK9111: typeB, steatite (ditto to
material heading540),0.95×0.82×0.29in, block8, houseII, room18,−16.2ft.
No commodity, workshop or exact absolute date inferred. The CISI2M897 alias
remains a consistent secondary join; its own metadata is not newly verified.
Old impression shows comb, crossed/diamond-like form, capped fish, two strokes,
and final enclosure. Capped fish is a secure broad positive observation; blurred
arm endings cannot certify W550 or exclude a damaged W555. Conversely, no
specific missing diagnostic stroke is demonstrated. Keep rawW550 unchanged.
The cutout's lower animal loss cannot distinguish physical break from cropping;
the fragment flag remains a source assessment, not a certified physical cause.

Parent located M77 reference2545 by OCR page navigation and inspected normalized
line printed75/PDF86: M267 M099 M065 M222 M254. The already retained primary
appendix printed818/PDF827 explicitly maps FEM2–704 to refs2002–2704 respectively,
so this is an authenticated FEM545→2545 join, not just a similar text or suffix
guess. Parent supplement preserves the primary normalization alongside the
unresolved photographic geometry. It does not recode either raw corpus. A first
wording patch failed because an unrelated expected line did not match; the smaller
patch succeeded. Final report expressly distinguishes source fragment flag from
physical breakage.

**Implementation and independent check.** Added audit_pincer_preservation.py,
a protocol, full row/model/partition output, and a meaningful test that rejects
constructing a fictitious witness from positions drawn from two different pairs.
Independent verifier imports neither analysis helper nor screen implementation;
it reconstructs whole-pair fits from reversed W and M sequence arrays, checks
raw metadata, all93 row results and all12 model×partition full ordered lists.
All agree. It relies on existing candidate discovery rather than independently
revalidating that screen; the scope is explicit. Added both scripts to the offline
pipeline. The audit verifies primary M897/review file pins, and direct M216/M222
index links preserve the unresolved discrepancy. README, REPORT, HYPOTHESES,
ALL_SIGN_EVIDENCE and PINCER_MAPPING_SENSITIVITY explain the findings.

New table download retained in data/raw, with URL/bytes/SHA256 registered. Primary
review, mapping supplement and crop/download scripts are saved. Full pipeline is
running; final verification is recorded below. All established values remain null.

Final validation: full offline pipeline exited0 with194 tests passing, including
the new whole-witness test and both computational audits. All266 source records
verify (235 downloads,26 captures,five HTTP responses); only rawREADME and
mayig_LICENSE are outside the registry. All16 new primary pins verify (11 agent,
five parent), both new analysis input-hash maps verify, and224 checked local
links resolve. All index source hashes are current; M001–M417 occur exactly
once and all established semantic/phonetic values remain null. Manifest refreshed
after this entry and all three hash groups verified. This is progress through an
exact original identity, a retained unresolved reading, and a reproducible limit
on the proposed conversion. Full decipherment is still unmet; goal remains active.

## 2026-09-25 — Doubled-grid tokenization and unmatched context recovery

**Continuation assessment:** prior turn was progress: it authenticated the M897
exception and retained unresolved fine geometry while independently checking
mapping sensitivity. This turn addresses unmatched rows, since absence of a
compatible candidate cannot be treated as evidence against a meaning when the
catalogues segment the same written form differently.

Inspected the previous screen's missing-context ledger: W525 occurs in9 selected
rows, W617 in7; seven other missing codes each occur once. M81 was unmatched
because W617 has no feature-derived M candidate and its six Wells units differ
from the candidate M77 line's seven. Source P268 lists W615 against M241/M245,
not W617. No source feature was silently extended. Prior primary review already
recognized the visually doubled grid on M81; its identity/tokenization was the
source-exposed motivating example, not a new blind prediction.

Saved double_grid_protocol.json before expanded counts. Permit only W617→two
adjacent M245 tokens. Every other token retains the preceding context screen's
constraints, including its explicit M216/M222 candidate target set. Preserve
reversed Wells ordering, exact consumed lengths and original source positions.
No wildcards, deletion, additional expansion, arbitrary grid merging or semantic
composition. A pair records which M positions each original W token consumes.

**New counts.** Original pincer selection stays93 rows: matched rows increase
36→41 and candidate pairs55→66, with all55 old pairs preserved. Newly matched
H1767,H49,M401 each have identical W617 W550 W003 and each match candidates
1542,2346,4133. These contribute a3×3 context block, not nine new objects or
independent confirmations. M81 uniquely matches1180; M980 matches2317 but is
source-flagged fragmentary. Five new rows represent only three distinct Wells
strings, contributing11 pairs. H1951 andM1080 remain unmatched despite containing
W617; overall52/93 pincer rows still lack candidates.

All strict W617-bearing rows form a separate selection of59:22 have candidates,
38 pairs, eight rows with multiple candidates;37 unmatched. The union of this
selection and the93 pincer rows has145 rows,93 pairs and346 alignment segments.
Counts from these overlapping selections must not be added as independent data.
These are discoveries of compatible contexts, not identified archaeological
objects or validation of a universal W617 rule.

**Primary bridge in parallel.** Reviewer authenticated C3133 independently in
CISI M81 metadata and MarshallII printed403/localPDF54 row180. The row is not
on the initially suggestedp404: reused exactp403 instead. It gives1.05×1.05in,
6ft0in depth,typeB,white steatite,C3133. Original MarshallIII retainedleaf191
contains numbered180 and compatible text/animal arrangement. M77appendix
printed818/PDF827 explicitly maps MIC1–560 torefs1001–1560, supplying180→1180
without assuming Finnish1180 equalsM77reference1180. Primary M77line1180
printed44/PDF55 draws two separate grids; primary sign list identifiesM245.
Parent also inspected the retained table/photo/line crops. Thus one edition's
W617 corresponds locally to two M245 units on this authenticated object. This
is not proof of two words, a meaning 'two', a global ligature rule or a phonetic
value. Both raw corpus granularities and primary Table I counts remain unchanged.

**Verification and saved work.** Added screen_double_grid.py, explicit protocol,
full unmatched/matched row ledger and alignment segments. Two meaningful tests
require exactly two M245 per W617, reject unsupported non-target substitutions,
and preserve separate boundaries for repeated compounds. Independent verifier
imports no production helper: it flattens each reversed W sequence into constrained
M slots, expands W617 only into two singletonM245 slots, and checks every candidate
M77 row. All145 full row records,93 candidate pairs,346 segments/provenance and
summary fields agree. It validates computation, not archaeological identity.
Saved verifier and hash-pinned output; primary review/crops tracked separately.
New report DOUBLE_GRID_RESULTS explains limitations and pseudoreplication in the
three-by-three block. Pipeline integration and final integrity checks follow.

Primary review finalized with25 evidence-file pins and zero new downloads.
Its JSON explicitly limits W617→M245,M245 to the authenticated artifact and
leaves global segmentation, numerical, semantic and phonetic values unestablished.
The screen now verifies all primary pins and checks that its separately computed
M81/1180 candidate agrees with the reviewed source sequences; identity remains
based on catalogue links, not that computation. Both screen and independent
verifier are required pipeline steps. Added a direct qualified M245 index link;
source P268 and raw transcriptions remain unchanged. README, REPORT, HYPOTHESES
and ALL_SIGN_EVIDENCE explain the difference in editorial token counts and warn
against treating it as a word/numeral rule. Full pipeline is running, with final
integrity results below.

Final validation: full offline pipeline exited0 with196 tests passing. Independent
screen verification agrees on all145 rows,93 pairs and346 segments. All25 primary
evidence pins verify; both new screen/verifier input-hash maps are current. All266
source records still verify (no new downloads), with only rawREADME and
mayig_LICENSE outside the registry. All231 checked local links resolve. Index
covers M001–M417 exactly once, now22 rows with qualified context links including
M245; all source hashes verify and all established semantic/phonetic values remain
null. Manifest refreshed after this entry and all three hash groups verified.
This turn is progress: an authenticated catalogue token-boundary difference and
independently reproduced recovery of formerly unmatched contexts. Full decipherment
remains unresolved and the goal active; next work should inspect the remaining
unmapped families and shared objects before inferring meaning from corpus counts.


## 26–27 September 2026 — W525 missing correspondence and multi-document coverage

**Prior-turn classification: progress.** The earlier double-grid phase authenticated
an editorial token-boundary difference and recovered formerly unmatched contexts.
This phase continues the still-unresolved decipherment objective by testing the
most frequent missing non-target code in the pincer comparison, W525.

**Protocol and strict null.** Saved the source-exposed masked-search protocol before
candidate counting. All ten strict Wells rows containing W525 were selected; nine
were in the earlier pincer sample. Each target consumed one M001–M417 sign, repeated
targets had to agree, and existing background memberships plus the already declared
pincer and double-grid rules were required for every other token. No other unknown
could be a wildcard. Result: zero pairs against1,293 strict M77 texts. Every selected
row had known non-target memberships, so this was not a residual-unmapped-code null.

**Post-null diagnostic, explicitly separated.** After noticing record2868 outside
the strict set, added a documented diagnostic scan of526 multi-document records
with known, undoubted flat token arrays and direction1. It returns six locators:
H1816,H1814,H1812,H1811,H774 all point to4672; M1390 points to2868. All suggestM254.
These are repeated context matches, not six objects identified or face-level texts
recovered. Original strict results remain unchanged. The independent agent's
verifier imports no production helpers, constructs expanded constraints separately,
and agrees on full selected records, all ordered segments, the null strict pairs,
and all six diagnostic records. Boundary checks reject inconsistent repeated masks,
M000/M418, and incorrect double-grid lengths. Two focused production tests pass.

**Primary artifact review.** Agent inspected original Mackay/Vats descriptions,
numbered plates, M77 appendix cross-references, printed transcriptions and sign
lists. DK8489 is FEM CII15, explicitly mapped to2868, with displayed M176,M254,M216.
Its original find description is First Street(11),−19.9feet. Plate CIII repeats it.
Ab473 is explicitly EH C672, connected by M77's stated EH rule to4672; the upper
face has the same leftmost three groups, with a second face printed separately.
Thus both local W525/M254 identifications have primary catalogue bridges. Exact
fine strokes depend on the published normalized transcription; the weak photographs
support object identity/broad arrangement. CISI2/3 alias metadata remain unchecked.
Parent visually inspected both printed lines and the Ab473 metadata crop.

**Failed leads and corrections.** The initial guessed FEM CI15/2855 locator was
wrong; the actual CII15 appendix entry identifies2868. An initial raw Ab473672 split
as Ab4736+72 was considered but never promoted; original Vats proves Ab473+672.
Mackay OCR's FirstStreet(1) was corrected by the original image to(11). Vats PDF198
was Plate XCV and197 a blank verso; correct XCIV is196, with failed renders retained.
Most importantly, original Vats printed33 explicitly connects excavation9015 with
XCIV356 and describes four/three signs, whereas raw H1123 suggests360 and three/two.
Plates356/360 are visibly different. Ref4360 exists, but neither its tempting shape
nor context authenticates9015→360; H1123 is excluded. Its plain/modified-fish mismatch
is not repaired. No transcription or excavation number was silently changed.

**Persistence and integration.** Five original page JPGs are together in data/raw,
registered centrally with URLs, sizes and SHA256. The primary review has44 immutable
file pins, download/crop scripts and render recipes. Added a separate primary audit,
which initially failed because normalized rows do not carry raw_text; corrected it
to reconstruct the source-order numeric string from the retained sequence before
checking the reviewed raw text. This was an implementation schema error, not a
changed research result. The audit now verifies all pins and two anchors, preserves
the excluded case and does not promote the multi-document corpus. Added qualified
M254 context evidence and integrated screen, independent verifier and audit into
the offline pipeline. W525_RESULTS explains the coverage null and semantic limits.
A separate source-exposed W525/W526/W527 context test is underway to examine whether
interchangeability has evidence beyond common editorial numbering.


**Three-form context follow-up.** The agent saved a protocol before computing
W525/W526/W527 counts, then preserved all64 selected rows and56 distinct strings.
W525 has10 rows/6 strings (9 medial,1 final); W5269/7 (all final); W52745/43
(40 final,4 medial,1 initial). Direction categories follow reversed file order,
not newly authenticated direction. There are zero exact whole-string replacements
of W525 by either other form, zero mixed-form rows and zero repeated-form rows.
W525 is exclusively tablet-labelled; the others are mainly seals. The apparent
position contrast therefore cannot be interpreted as a functional distinction.

A transparently post-count protocol amendment examined site×type×length coverage.
Only1 of35 observed strata is shared: Harappa/TAB:B/length3. Its main rows are
H1123 finalW525, H1817 medialW525 and H843 medialW527. H1123 is the sole finalW525;
retrospective omission leaves9 rows/5 strings, all medial. In the shared stratum
only one medial example per side remains, and W554/W195 also differ. There is no
clean one-sign contrast and insufficient coverage to separate positional graphic
variation from different formulas or meanings. Both original and sensitivity
results remain explicit; no allography or values promoted. No new downloads.

Parent independently verified the key counts using a separate script with no
audit imports: direct unequal-position comparisons of selected-versus-all rows,
edge categories computed in original file coordinates, set-based shared strata,
and full stratum member-list agreement. All checks pass. Two focused tests cover
one-position replacement, duplicate retention, reversed indexing and singletons.
Integrated both scripts and a qualified M254 context link; updated report/index
navigation. Full offline pipeline exited0 with200 tests. Because the final
comb-family extensions completed during that run, their final audit/verifier and
index were subsequently rerun, followed by all200 tests, also passing; the exact
follow-up commands/output are in results/w525_final_checks.log.

Source-integrity check verifies271 unique source records (240 downloads,26 web
captures,5 archived responses), including all five new JPGs. Only rawREADME and
mayig_LICENSE sit outside the source registry. The index covers M001–M417 exactly
once, has22 rows with context links, and retains null semantic/phonetic values for
all417. All index-source hashes and44 primary W525 evidence pins verify. Final
local-link and refreshed-manifest verification follows. This turn is progress:
two primary catalogue correspondences, an excluded identity conflict, a diagnosed
corpus-coverage failure, and a context test that limits an allography inference.
The full decipherment remains unresolved; the goal remains active.

Final integrity: all941 local Markdown links resolve. All five new analysis/verifier
input-hash maps are current. Refreshed manifest verifies328 code/document files,
1,536 result files and255 processed-data files, plus the source-registry hash.
This closing log entry was included in a second manifest refresh and recheck.


## 27 September 2026 — Comparable tablets and the second differing sign

**Prior-turn classification: progress.** W525's two local primary correspondences,
the H1123 identity conflict, strict-corpus coverage diagnosis and independent
three-form context check changed the next action. This phase investigates the
remaining shared-stratum pair H1817/H843 rather than assuming two differing
W codes constitute a clean comb-allograph contrast. Full decipherment is still
unresolved and remains the active objective.

**Protocol and source exposure.** Read current saved outputs and raw metadata.
Printing the initial raw rows inadvertently displayed proposed Sanskrit/English
readings and a source cross-reference. These were not used; the saved protocol
explicitly excludes them, and all analytical scripts read only structural strict
rows/feature memberships. The pair had already been selected by literal shared
site/type/length before that exposure. Saved comb_tablet_protocol before counting
W195/W554 outcomes or masked candidates. Both targets were masked separately;
only one M001–M417 per occurrence, consistent if repeated. Existing other-token
memberships, prior pincer candidates and W617 span were required. W525/M254 was
evaluated off/on as an explicitly experimental extension of two local anchors.
Strict M77 and multi-document known-undoubted direction1 locators stayed separate.

**Masked results.** W195 has2 rows/2 strings. Its only strict pair is M735/1060
withM054; H843 supplies separate diagnostic2868/M216 and5326/M054 candidates.
The W525 extension changes none of these results. W554 has10 rows/8 strings.
Strict5 matched rows supply81 incidences, but most come from the duplicated short
W740/W554 string with many alternatives. H133/4261,H680/5099,M1087/1319 are longer
strict matches each suggestingM226. Diagnostic4 rows/26 pairs include duplicate
H1146/H833 matching4370/M226; enablingW525 adds H1817 with2868/M216 and5326/M054,
for5 rows/28 pairs. Neither new target candidate isM226; no global rule is rejected
because corpus coverage and background local conversions are incomplete.

Independent verifier imports no production helpers and expands constraints before
matching. All8 experiments,222 pair incidences,486 ordered alignment segments,
full records and summaries agree. It preserves duplicate accounting: W554 strict81
incidences reduce to27 unique(Wstring,Mstring,candidate)triples; diagnostic26→8
or28→10 with extension. These are compatible contexts, not independent objects.
Two focused tests verify target-only masking, repeated-target agreement, domain
bounds and explicit optionalW525 extension without freeing other positions.

**Adjacent W400 test.** All strict contexts with immediate file-order W400 before
W525/W526/W527 were retained. W525:9 rows/5 distinct strings; W526:0; W527:2 rows/2
strings. None of the7 distinct contexts has a whole-string counterpart deleting
only W400. Independent direct verification agrees. This does not support an
optional-marker claim in this sample, but cannot prove mandatory status, compound
sign identity, word boundaries or grammar.

**M735 primary check.** Parent followed the unique longer-context candidate.
MarshallII printed402/PDF53 row60 explicitly gives C3070,1.25×1.3in,typeB,white
steatite,3ft0 depth. M77appendix818/PDF827 explicitly maps MIC1–560→refs1001–1560,
thus60→1060. Primary text40/PDF51 rightmost glyph agrees with numberedM054 in
primary sign list32/PDF43. Original MarshallIII PlateCV/photo60 on Archiveleaf185
corroborates seven upper groups and a one-horn animal; fine target strokes are
weak. This supports local secondaryW195/M054 through its stated old-publication
identity, not a full CISI2 M735 alias authentication or global conversion. The
original table printsC3070 rather than the secondary's expandedDK-C prefix.
P076 covers W190/W192/W194 andM054/M055 but omitsW195; its non-exhaustiveness is
recorded without rewriting it. All meanings/sounds remain null.

Photo navigation: original volumeIII OCR/XML search for60 failed because plate
OCR is sparse. Existingleaf183 shows19–40; next illustratedleaf185 correctly
contains41–69. One new originalJPG downloaded todata/raw and registered. An initial
M77page42 render reached the codes page, not the sign list; existingprimarypage32
was inspected instead. Reading the page42 image before its confirmed-live render
finished caused an invalid-image error; the same process completed successfully
and was read, without restarting. Parallel workers reused prefixcomb-tablet-m77,
so the single extraction manifest was overwritten by the later149/822 invocation.
All images survived; the parent's exact51/42 invocation/provenance is now separately
recorded in results/m735_m77_extraction.json. Its review/pins explicitly use that
record, leaving the other review's manifest unchanged. Nineteen parent review
file pins verify after this documented correction.

**H843/H1817 primary limits.** Agent exact/variant14307 searches in retained
Vats/M77 OCR found no identity; this is not proof of absence. Candidate5326 primary
appendix823/PDF832 has a blank excavation field and Pu.63:4394–95 source shared
with5327–5329. Printed text138/PDF149 explicitly showsM176,M254,M054; additional
metadata29790 has no second script line. Field-symbol key812/PDF821 and plate
813/PDF822 figure139 link5326 toPu.63:4395 and show a crosshatched reverse. This
matches a secondary motif label but does not supply14307↔5326 orH843↔5326.
Candidate2868 already belongs to the roundDK8489 elephant-impressed object;
sequence compatibility cannot transfer that identity to a prism.

H1817's exactH94-2326/Figure26.06 was not located in accessible original reports.
The1997Harappa report uses different figure numbering/registration examples;
the2010original-authorCISI essay cites a separate1994submitted report but is not
the fullCISI3photographic catalogue. Direct1997PDF retrieval failedHTTP403 with
urllib andcurl; two web-extraction captures from1997/2010were saved and explicitly
registered as captures, not originalPDFdownloads. Screenshot calls supplied no
inspectable image payload, so no web-figure inspection was claimed. The old
corpus-vol-2 Archive lead again identifiesvolume1, not the neededvolume2. Neither
requested artifact acquired an authenticated inscription photograph; pairwise
stroke/comb comparisons remain unresolved. Secondary shape/dimensions also differ
(rectangular small faience versus larger triangular prism), so TAB:B is a broad
label. Agent saved32primary-reviewpins and scripts, all verified.

**H133 independent W554 anchor.** A separate primary review followed the longer
strictM226candidate. OriginalVats printed53/Archiveleaf79 explicitly joins8360
withPlateXCII261, seven pictograms, steatite, TrenchIV StratumI,squareI13/7,2ftdepth.
OCR's B360 was corrected by direct original-page inspection. The cited furnace
is inI13/21, a different square: no workshop/deposit association was promoted.
PlateXCII/PDF192 illustrates261; M77's explicitEHrule maps261→4261. Printed104/
PDF115 second-from-leftglyph matches numberedM226 on34/PDF45. The photograph
supports arrangement but the small terminalhook is weaker than the normalized
drawing. Other six numericMcodes and modernCISIalias were not newly certified.
This supports localW554/M226 on this row, notH1817. One originalpageJPG retained;
20evidencepins verify. Parent inspected the originalmetadata,4261target,numbered
226 and5326blank-fieldcrop. Combined primary audit checks71file-pin incidences
across three reviews (some sources overlap, not71independent witnesses).

**Integration.** Added COMB_TABLET_RESULTS and three detailed primary reviews;
all downloads/captures remain together indata/raw. Central source registry now
includes the two originalpageJPGs and two explicitly typedwebcaptures from this
phase. No failedHTTPresponse withoutretainedbytes is counted as a source download.
Added screen, independent verifier, metadata/search audit and primaryreviewaudit
to the offlinepipeline, and qualifiedM054/M226/M254evidence links. Rawtranscriptions
and featuretables remain unchanged. No W554/W195 merger, H843identity, global
allography, or semantic/phonetic value promoted. Fullpipeline is running; final
integrity checks follow.


Final verification: complete offlinepipeline exited0 with202 tests passing.
Independent computation agrees on all8 experiments,222pair incidences and486
segments; allnewresult input-hash maps are current. Primaryreviewaudit verifies
71file-pin incidences across its three reviews. All275 unique source records
verify (242downloads,28webcaptures,5archivedresponses); onlyrawREADME and
mayig_LICENSE remain outside the registry. All954 localMarkdownlinks resolve.
The all-sign index coversM001–M417 once each, now24rows with qualifiedcontext
links, with allinputhashes verified and all417semantic/phoneticvalues null.
Manifest was refreshed after this entry and allthreehashgroups/source-registry
hash checked. This is progress, not a decipherment: newlocalcorrespondences and
explicitidentity/coverage limits improve the evidence while leaving the original
goal active. The next unresolved source targets are the fullCISI2 H843 entry or
Punjabalbum63identitybridge, and theHARP1994Figure26.06/CISI3 H1817 entry.


## 27 September 2026 — Conversion constraints and recovery of the actual CISI2

**Previous turn: progress.** The second-sign investigation established two local
correspondences and identified specific missing sources for H843 and H1817. This
turn pursued those sources through distinct routes while formalizing what the
reviewed cross-catalogue examples actually permit. The objective remains full
decipherment; none of the following assigns a semantic or phonetic value.

**Finite conversion-model audit.** Saved a source-exposed protocol, then selected
only ten explicit target correspondences from eight existing primary-review files.
No full candidate transcription was silently promoted to a fully certified text.
The ten observations yield eight distinct assertions over W195, W525, W526, W527,
W550, W554, W555 and W617, involving six M inventory members. Tested four models:
locally injective single-token conversion; deterministic single-token conversion
allowing many-to-one mappings; deterministic ordered spans of length one or two;
and a relation permitting multiple such spans per W code.

Core consistency is false/false/true/true. W617→M245,M245 alone contradicts either
single-token model. Different W525/W526/W527 codes sharing M254 additionally
contradict injectivity. The uncertain M897 W550/M222 observation is sensitivity-only:
adding it conflicts with M63 W550/M216 under a deterministic span model, while a
relation can retain both. This is source consistency, not ancient homophony or
proof of different meanings. No majority-vote repair or automatic corpus change
was performed. All minimal singleton/pair witnesses and all417 coverage statuses
are saved; 411 signs are unconstrained by this selected audit, not declared
unevidenced elsewhere. A satisfiable partial table is not a global conversion.

Independent verifier reconstructs the exact targets from source fields and selected
raw metadata without importing the producer. It uses set-based constructions and
exhaustive subset enumeration. All241 checks pass, including184 recursive source
hash/size checks and all417 coverage rows. Minimal contradiction-set counts for
the four models are core6/1/0/0 and sensitivity9/2/1/0. Two tests distinguish span
length, injectivity, deterministic ordered output and duplicate observations.
The local-injectivity test makes no global-surjectivity or full-W-inventory claim.

**Editorial method source review.** A bounded existing method investigation was
finished by the verifier agent before its new task. It visually inspected M77
printed15–17/PDF26–28, sections11.3–11.9. Variant classification and some boundary
choices use distributional evidence; morphology labels are conventional; spacing
has stated exceptions; variable joined/separate forms are normalized as independent
signs; integral-sign boundaries remain provisional. Parent inspected page17.
This warns against reusing normalized contexts as independent proof of the very
segmentation/classification they encode. The author's text1218 frequency argument
was not recomputed, nor was any composite decomposition newly certified. The
note's proposed exact-frame test/threshold is a recommendation, not an executed
experiment or Mahadevan's procedure. No downloads. Six method evidence files
are pinned in catalogue_method_review.json.

**H1817 bounded recovery.** Agent tested19 exact identity, figure, report-title,
author/institution and full-CISI/ISBN/MASI96 query strings, plus public catalogue
routes. Helsinki's institutional CISI3.1 record is bibliography, HARP pages supplied
no1994 report attachment, and Archive returned only1986–1990 reports. Harvard
web retrieval returned403; the prior failed HarappaPDF route was not repeated.
No H94-2326/Figure26.06 or CISI3 H1817 original page was recovered. This is a bounded
negative search, not proof that the source does not exist. Saved two actual
Archive API responses and one explicitly typed web-capture file containing eight
batches, all in data/raw, with eight evidence pins. No target identity promoted.

**Actual CISI2 recovered.** Both source agents independently noticed a distinct
Archive item, corpus-vol-2_202409, rather than the previously rejected corpus-vol-2
which is actually volume1. One agent downloaded the PDF once; the other avoided
duplication. The title was visually authenticated as Shah/Parpola, Collections in
Pakistan, Helsinki1991,486 PDF pages. Retained the35,870,617-byte original PDF,
Archive metadata/search response, companion OCR and page-number JSON. Original
institution/IGNCA searches led to citations/volume1; the Lahore archive catalogue
hit a content-size limit, the Finnish library URL a cache miss, and British Library
photo catalogue leads supplied no exact14307/Pu63 bridge. These failures and three
web-capture files are preserved. OCR was poor; primary identity rests on images.

CISI2 printed331/PDF366 shows H843 A, B, C, F and B+C views. Printed444/PDF479
explicitly gives H843 / Finnish4162 / field14307 / HM269 / AV405; B+C:P859. The
metadata key printed434/PDF469 defines the columns and warns Finnish concordance
numbers can differ from Mahadevan's. It expands HM as Harappa Museum; photo names
were checked in the key. H843↔14307↔Harappa Museum269 is now authenticated.

Agent and parent inspected the three-sign A face, two different crosshatched B/C
faces and triangular end F. The middle comb has stem left and short strokes right
in published orientation; exact tooth count is not asserted. The rightmost glyph
is curved/looped and branched, broadly consistent with M054, but faint topology
prevents a newly certified exact numbered transcription. Both ends remain visible;
no precise physical-completeness grade or missing-stroke reconstruction is inferred.
Comparison with M77 figure139 gives generic crosshatching, not a distinctive
resolvable damaged edge/intersection pattern sufficient for physical identity.
H843↔M775326 and14307↔Pu63:4394–95 therefore remain unresolved. Thirty-four
follow-up evidence pins verify. H1817 remains unavailable, so the original pairwise
graphic test is still incomplete.

**Incidental M735 alias closure.** The basic-data render printed435/PDF470 also
contains M735 with field DK-C3070. Parent inspected the whole page and unretouched
row crop, verified column meanings against the key, and saved a separate five-pin
alias follow-up plus crop script. This independently verifies the modern alias
left unchecked in the preceding review. Finnish1060 is recorded but not used as
a Mahadevan identity bridge; MIC60→M771060 still uses the earlier explicit appendix
rule. Earlier reviews and the ten model constraints remain frozen. A wording
patch initially failed twice because its expected document line had the wrong
capitalization/context; no partial change was applied. The corrected patch clarifies
that the model verifier's old alias limitation describes its frozen input review,
while the new alias evidence is separate.

**Integration.** Registered seven new downloaded files and four typed web-capture
files from the two source searches, all in data/raw. Added model audit/verifier and
source-follow-up audit to the offline pipeline. Added qualified evidence links for
the six constrained M signs and recovered H843/M735 metadata. Updated the living
tablet-results report to supersede the old lack-of-H843-photo statement while
leaving its pinned historical primary review unchanged. README, main report,
hypotheses and all-sign documentation link the new findings. No source family map,
raw transcription, ancient sign count or reading was overwritten. Full pipeline
is running; final integrity checks follow.


Final validation: the full offline pipeline exited0 with204 tests passing. All
new model/verifier/source-audit input hashes are current. The independent model
verifier passes241 checks and184 recursive evidence-pin checks; source follow-up
reviews verify53 pin incidences (34 H843,8 H1817,5 M735 alias,6 method files).
All286 registered source records verify (249 downloads,32 web captures,5 archived
responses). Only rawREADME and mayig_LICENSE are unregistered support files.
All976 local Markdown links resolve. The evidence index covers M001–M417 exactly
once, retains24 rows with qualified context links, and all input hashes verify;
all417 semantic and phonetic values remain null. Manifest refreshed after this
entry and all three hash groups plus the source-registry hash verified.

This turn is progress: authentic CISI2 recovery supplies new object photographs
and closes H843/14307 and M735/DK-C3070 aliases; the selected conversion assumptions
now have explicit contradiction witnesses and independent verification. Full
decipherment is not achieved. The goal remains active. The new volume provides
concrete next work on the earlier H1123/9015/356/360 conflict and other qualified
CISI2 aliases; H1817 and the H843/M775326 bridge remain separately unresolved.

## 2026-09-27 — CISI2 disputed records: M897, M934 and H1123

**Question.** Can the newly recovered authentic CISI2 resolve previously qualified
artifact aliases and fine-sign discrepancies? Parent inspected M897; parallel
agents inspected H1123 and M934, and a second source-exposed reviewer independently
inspected the M897 photographs. All work reused retained sources. No download,
external message or new semantic/phonetic assignment was made.

**H1123: bounded negative with positive coverage evidence.** CISI2 contents
printedIII/PDF6 explicitly covers Harappa H266–275,H356*,H383–1019. The final
Harappa photo page printed351/PDF386 and final basic-data table printed445/PDF480
confirm that endpoint; corrigenda printed447/PDF482 offer no relevant correction.
Agent reopened Vats printed33: excavation9015 explicitly points to XCIV356,
whereas secondary H1123 rows313.1/313.2 concatenate9015360. Separate plate356/360
images are different. No9015→360 or H1123 primary join was promoted. Exact local
OCR searches (H1123,9015,9015360) had zero hits but are not the basis for claiming
coverage. H356* is a different catalogue namespace, not Vats plate356. Twenty-two
pins and reproducible locator/crop code preserve the bounded finding; another
alias for the physical object is not logically excluded. Parent inspected coverage,
end-data and corrigenda crops.

**M897: alias authenticated, fine reading still uncertain.** Resumed the existing
metadata-render session71154 to completion, without restarting it. CISI2
printed436/PDF471 reads M897, Finnish2545, DK9111, MD446, JL589; a:P368.
Parent checked the key printed434/PDF469: the Finnish number is not automatically
a Mahadevan number. Original FEM545=DK9111 and the explicit FEM→M77 appendix
rule remain the basis for M77text2545. MD446 is the published old accession, not
a claim of present-day custody.

OCR had not located M897 reliably. Photo brackets PDF110 and130 gave M837–841
and M973–982; PDF119 narrowed to M889–892. PDF120/printed85 shows labelled
M897A and a; PDF121 shows adjacent M899–906. All non-target renders and invocation
manifests remain preserved with unique prefixes. Larger unretouched crops show
five broad groups and bent crossed-form ends more clearly. Both parent and
independent reviewer find upper line endings still affected by rough edges,
surface/lighting and limited resolution. Neither certifies W550, recodes to W555,
or reconstructs a particular missing diagnostic stroke. Original A as well as
impression a shows the boundary truncating the animal, strengthening physical
fragmentation over the old isolated plate crop. That lower break does not prove
loss at the upper sign. One artifact/two complementary views, not two attestations.
Raw fragment/complete=Y flags, normalized M222, frozen model core and sensitivity
are unchanged. Parent review29 pins; independent review17 pins.

**M934: direct photo support plus a newly visible conflict.** CISI2
printed436/PDF471 explicitly reads M934, Finnish1158, **DM56**, MD50.419/MM464,
JL192; a:P167. Marshall printed403/PDF54 row158 clearly reads **DM50**. Parent
and agent inspected both. Museum50.419 and secondary DM50158 do not resolve the
field-number disagreement. No preferred correction was chosen.

Photo navigation PDF124 reached M923–929; PDF125/printed90 supplies M934A/a.
The labelled photos show the five groups and animal/stand composition, with
strong visual concordance to old MIC158. Direct comparison with L89 impressions
supports the opposite comb stagger, independently of choosing DM50 or56.
There is no gross missing comb corner like L9; every fine stroke and complete
physical condition are not certified. The prior MIC158→M77 appendix rule is
retained without equating Finnish1158 with M77 merely because numbers match.
Twenty-two pins preserve this supplement; historical reviews remain unmodified.

**Execution failures and corrections.** One parent text search used the nonexistent
script name build_sign_evidence_index.py; corrected via rg --files to
build_evidence_index.py. Parent guessed two nonexistent M934 crop filenames
(metadata/pair); inspected the saved crop script and then opened the actual
meta-detail/original/impression filenames. Agent first used system Python without
Pillow; the dependency runtime succeeded. An attempted view of PDF125 before
its render completed failed; agent polled that same process and inspected the
completed image. These issues did not change source readings, restart a live
render or produce invented image data.

**Integration.** Added audit_cisi2_disputes.py to verify90 evidence-pin incidences
and preserve the four reviews' uncertainty dispositions, plus the H1123 locator
script in the offline pipeline. Added qualified context links to existing M216,
M222,M254 index rows. Updated living README/report/hypotheses/all-sign summaries,
including replacing the obsolete M934 “CISI2 unchecked” summary with the explicit
DM56/DM50 conflict. Frozen primary reviews, raw corpora and model protocols remain
unchanged. Audit passed before the full pipeline run. Final validation follows.

Final validation: full offline pipeline exited0, with204 tests passing and the
new90-pin dispute audit passing. All286 registered source records verify
(249downloads,32webcaptures,5archivedresponses); no new raw bytes were acquired.
Only rawREADME and mayig_LICENSE remain unregistered support files.

After the full run, corrected two stale descriptive labels in the catalogue-model
producer/verifier: “M934 alias unverified” now explicitly describes the frozen
input reviews, while the separate new review supplies labelled photographs and
retains the DM56/DM50 conflict. Added the corresponding model-report supplement.
No algorithm, target constraint or model outcome changed. Reran the affected
model audit, independent verifier and evidence-index builder successfully; the
verifier again passed241 checks and184 recursive source pins. No repeat of the
unaffected expensive pipeline was needed for these wording-only changes.

All1015 local Markdown links resolve. The evidence index still covers M001–M417
exactly once, keeps24 rows with qualified context links, and all28 indexed source
hashes verify. New review/model input hashes are current. Every semantic and
phonetic value remains null. Refreshed the manifest after this entry and verified
its three hash groups and source-registry hash.

This phase authenticated M897's modern alias, recovered useful M897/M934 original
views, documented a new M934 excavation-number conflict, and bounded the H1123
search correctly. It did not decipher the script. The goal remains active.

## 2026-09-27 — Recurring roof additions and cross-root contextual transfer

**Prior-turn audit.** The preceding goal turn was progress: it added authenticated
M897 metadata/photographs, a new M934 catalogue conflict and a positive H1123
coverage boundary. This phase moved beyond those local identities to a common
sign-formation hypothesis. Full decipherment remains unachieved.

**Shape-first selection.** An agent inspected the four primary representative
sign-list pages without opening context/count outputs. Initial selection had
seven pairs, including158/159. Closer crops showed an additional central stroke
on159, so that pair was excluded before running the new statistic. Six core pairs
remain:059/065,060/066,089/092,137/138,162/163,333/334. The two fish pairs share one
root. Roof shape is not equated with standalone134, and no token is split.
Flat-topped, rectangular and curved caps were explicitly excluded. Daggers
point to variants not exhaustively inspected. Thirty-one shape-review pins and
reproducible numbered crops preserve both accepted pairs and exclusions. Parent
visually checked all12 endpoint crops.

**Prospective protocol, then counts.** Saved roof_modifier_protocol.json before
running this new statistic; previous general corpus exposure is acknowledged, so
this is not a blind discovery claim. The state of each complete entire frame is
plain-only, roof-only or both. Preserve prefix/suffix, source site/type, length
and position. Unknown sites are not verified same-site comparisons. Compare only
different roots; require one plain/plain and a different roof/roof frame within
the same metadata stratum, with an injective selection of four distinct reference
witnesses. This is a candidate rectangle, not proof of objects/dies or a shared
semantic operator. Metadata-free diagnostics still preserve length/position.
No field joining, loss deletion or late selection of a winning pair.

A parallel design critique identified baseline-frequency bias in signed state
agreement, sampling dependence of mixed masks, possible vacuous shuffles and
unverified site labels. Before counting, the protocol made qualified rectangle
coverage primary and the mask shuffle secondary. It records only preservation of
frame-mask multiplicities and coverage, not token/reference counts or object/
formula dependencies. The narrow shape selection contains five graphic roots
and14 cross-root pair comparisons.

**Results.** Strict1293 records:1 cross-root shared frame, plain/plain,0rectangles.
Broad complete/undoubted2056 records:3 shared frames, one plain/plain, one mixed,
one discordant,0rectangles. Metadata matching changes neither count. The broader
78 one-token records remain in coverage but supply no outside frame. The strict
shared frame M109_ pairs plain fish4171 with plain trident1243/1249/5054; every
site label there is unknown. Broader extra frames are _M176 and _M342, all short
two-token strings. Full frame/reference ledgers and all417 coverage rows saved.
No selected sign value, raw sequence or semantic equation changed.

**Exact diagnostic check.** Producer499 seeded shuffles preserve per-pair mask
counts within source site/type/length/position strata. Independent code imports no
producer helpers, reconstructs every frame/state/reference and all417 coverage
rows, and checks source pins. It enumerates only shared-edge assignments, weighting
unused slots by multinomial completions; four small exhaustive permutation cases
check this marginalization. Despite large global allocation counts, exact score
supports are {1},{1},{0},{-1,0} for strict-stratified,strict-unstratified,broad-
stratified,broad-unstratified respectively. The first three nulls are provably
invariant. The broad-unstratified diagnostic has sampled upper-tail0.478, which
is not a modifier result. No p-value can fill missing rectangle corners.

**Primary M092 coverage.** Primary TableI records092 once (initial). The export's
8018 reads092,099,LOSS. Parent inspected normalized text printed155/PDF166 and
concordance printed321/PDF332: same roofed three strokes, two short strokes and
hatched loss. The latter is the099 concordance group, not a new092 census. The
fixed whole-field loss exclusion is justified for this record; absence from the
complete test does not mean no ancient occurrence or no modifier. Nine pins
retain this coverage review. An attempted filename m77_table1.csv did not exist;
actual retained table review and page729 were inspected instead. No download.

**Primary M176 candidates and omitted sides.** Agent recovered all printed entries
for4407,4493,5444,5477; parent independently viewed complete reference crops and
appendix joins. Four first fields confirmed:138/176 twice,066/176,060/176. Their
other entries are087/328 twice,095/328,and a symbol-only side respectively.
Eight entries (seven script lines plus one symbol-only) remain separate.
5477 original direction2 is distinct from catalogue normalization and agrees with
export; no direction discrepancies. Literal abbreviated metadata is expanded
under the source rule; field-symbol83 is not sign083. EH rule supplies4407/EH407
and4493/EH493; appendix gives5444=3027(2)/Pu35:3863,5477=13592/Pu61:4076. No
unverified excavation join or object/die independence is asserted. Twenty-six
pins preserve the source review; combined primary audit verifies35pins.

**Persistence and validation.** Saved producer, independent verifier, protocol,
shape/source reviews, crop scripts and complete results. Five focused tests cover
loss exclusion, whole-context boundaries, distinct-reference matching, shared-root
exclusion, mixed states, metadata-stratum matching and shuffle conservation.
Independent exact-null oracle has four additional exhaustive cases. Added the
three roof scripts to the offline pipeline and qualified native-M context links
for all12 endpoints; unselected signs retain explicit coverage/null values.
Updated living README/report/hypotheses/all-sign summaries. No new downloaded
bytes, corpus mutation, global conversion or assigned reading. Full pipeline
validation follows.

Final validation: full offline pipeline exited0 with209 tests passing. The
independent roof verifier reproduces every finite frame/state/reference result,
checks all417 coverage rows and verifies41 current source/evidence pins. Its
four exact-null oracle cases pass. Shape review31 pins and the separate primary
field audit35 pins verify. Both producer and primary-audit input hashes are
current, and no source-direction discrepancy was found in the four M176 fields.

All286 registered source records retain valid byte counts/hashes; no new source
was downloaded. All1032 local Markdown links resolve. The consolidated index
contains M001–M417 exactly once, now32 rows with qualified context links, and
all29 indexed source hashes verify. Every semantic and phonetic value remains
null. The manifest was refreshed after this entry and all three hash groups
plus the source-registry hash verified.

This turn is progress: a visually frozen candidate operation received an exact
coverage test, a purported inferential route was proved invariant under its null,
and eight primary object fields plus one damaged rare occurrence were checked.
The evidence does not establish a common roof function or a decipherment. The
full goal remains active. Next useful evidence is original imagery/variants for
these rare roof forms and physical identity checks for the paired tablet entries,
not treating the zero-rectangle result as semantic refutation.

## 2026-09-27 — Roof variants, original artifacts and object disambiguation

**Question.** Does the selected roof difference survive published variants, and
can original photographs independently authenticate the rare roofed candidates?
Continued the active goal with parallel bounded variant and artifact reviews.
All candidate pairs, corpus fields and preceding context endpoints stayed frozen.
Prior hypotheses/counts were known; this was source replication, not a blind test.

**Variant inspection.** Parent rendered M77 PDF794–796,800–801 with unique
roof-variants-locate prefix, inspected relevant pages and made three native
crops. M059 is in the addendum, printed792/PDF801, refs1032/8211: lateral
projections vary. M060 p786/PDF795 refs1177/7025 has four flank strokes versus
four dots. M089 same page refs1003/2573 has upright versus slanted parallel
strokes. All six drawings lack roofs. Agent inspected M137 refs1175/2847,
plain versus ticked X, and M162 refs8075/1361/2934/1539/2648, differing arm
geometry/prong counts, on p787/PDF796. M334 refs2364/1403 has roofed U-like
forms with differing basal stem direction, p790/PDF799. Parent independently
viewed all three non-fish crops and their labels. The initially suggested PDF800
is printed791 beginning336, not334; +9 Appendix offsets differ from +11 in the
representative section. Fifteen drawings in six editorial rows retain their
coarse roof status but do not justify a fixed base drawing, invariant detached
roof, or allography. No roofed partner of every base variant was authenticated.

**K-29 object recovery.** Agent joined M77 8018 to excavation8219/ASI68.1.48
through M77 AppendixV p827/PDF836 and CISI1 p374/PDF410. CISI1 p304/PDF340
original and impression show the roof over three long strokes, two adjacent
shorter surviving strokes and substantial loss. ASI Kalibangan2015 Fig9.29
p469/PDF161 and descriptionp470/PDF162 corroborate8219 and explicitly identify
M-List92. Parent independently viewed the identifier crops, CISI photographs
and excavation figure. CISI7102 is Finnish Concordance, not an M77 identifier;
the source key was checked. Only identity/condition/token columns of secondary
row1903.1 were used, preserving ]000-044+ and incomplete status. P149 supports
W044/M092 locally, not a global conversion or complete transcription equation.
Several publications depict one artifact. Existing loss exclusion remains.
The adjacent stroke lengths cannot be restored at broken edges.

**Roofed cross.** Agent recovered three Vats original text pages into data/raw
(leaves193,134,353), downloaded with persisted script and separate pending
registry; parent verified bytes/hashes and merged all three into data/sources.json.
The earlier explicit M77 EH rule yields4407→EH407. Vats p167/leaf193 explicitly
links407 to1722, squareR24/7,15ft6in; original plateXCV/PDF198 shows roofed X
with comb-like sign and reverse U/two long strokes. Parent viewed both sides
and original metadata. Vats p327/leaf353 calls407 entire and explains the
intentional central concavities. Do not confuse this shape with damage.
Vats counts the reverse as one pictogram while M77 uses two codes; neither
catalogue grouping supplies a numerical interpretation.

5444 is3027(2),Pu35:3863. Vats p108/leaf134 gives EH558=3027, squareM11/21,
12ft,fragment; its plateXCVII/PDF202 shows a small fragment without a secure
complete roof-X reading. Critically, M77 p817/PDF826 paragraphvi explicitly
uses suffixes to disambiguate objects sharing excavation numbers. Parent viewed
the rule and558 source/photo. Rejected automatic3027(2)→558 join. Different
recorded excavation IDs support distinct catalogue entries, but physical
independence and duplication of4407/5444 both remain unresolved. One original
artifact is authenticated from that two-reference target set.

**Failed searches and qualifications.** CISI2 basic-data476–480 English OCR and
selected visual checks yielded no exact1722/3027(2)/Pu35:3863 bridge; CISI1
406–408 likewise. A temptingH780/3863 OCR locator was visually3865 with field
3789 and rejected. Negative search is not proof of source-wide absence. K-29
navigation pages337–339 and Kalibangan163–164 were adjacent entries, not new
witnesses. An initially guessed roof_m092_coverage_review.json was absent;
correct ledger is roof_m092_primary_review.json. Parent lookups also used two
absent guesses, ALL_SIGN_CONCLUSIONS.md and context_audits.json; corrected to
ALL_SIGN_EVIDENCE.md and context_audit_links.json. An early glob preceded agent
file creation and found no ROOF_X review; no data were lost. A tool call emitting
six images exceeded response size, so all relevant images were re-opened in
smaller batches before claiming parent inspection. Full new attempts and render
parameters remain in the four individual source reviews and extraction records.

**Inference and persistence.** Independent critique separates an overstrong
fixed-geometry claim from common roof semantics: the latter is neither proved
nor refuted. Zero qualifying rectangles is a finite corpus result, not an
ancient prohibition; mixed frames, uncertain object independence, source
normalization and other-side differences limit extrapolation. Next productive
work is remaining original-photo replication and independently grouped complete
contexts, not additional shuffles of an uninformative graph. No semantic value
is yet externally anchored. Saved combined report, four evidence ledgers,
inference review, crop/downloader scripts and audit. Added qualified context
links for all12 roof endpoints in the417-sign index. New audit checks105source
pins, crop pixel equality, source-record joins and retained uncertainties;
manual visual judgments remain attributed as such. No new invented readings,
restored signs, raw corpus edits or retrospective selection changes.

Validation in progress: preliminary audit passed105pins and its initial10crop
checks; expanded audit adds the six roof-X crops and inference-document pins.
Full offline pipeline and final manifest checks follow.

Final validation: full offline pipeline exited0;209tests passed. The follow-up
audit verifies105source pins,16exact pixel crops and all3new registered downloads.
A later timing note in the inference critique explicitly distinguishes completed
4407 inspection from prospective4493/5477/exact5444 checks. Reran the affected
audit and index after that documentation edit;8inference revision pins and all
current result-input hashes verify. No computational model or corpus changed.

All289 source records verify bytes and SHA256:252downloads,32web-extraction
captures,5archived responses. The only unregistered raw files are the existing
README and retained license. All1064 local Markdown links resolve. The index
contains M001–M417 exactly once,32rows with qualified context links and30valid
source hashes. Every meaning and phonetic value remains null. The final manifest
covers384code/docs,1725results and289processed files; it was refreshed after
this entry and all groups plus the source-registry hash checked.

Progress this turn is new primary evidence, fifteen inspected variant drawings,
two original artifact authentications and an explicit rejected identity shortcut.
It is not a decipherment. The goal remains active. Next original-photo targets
are4493/EH493,5477/13592/Pu61:4076 and the exact5444/3027(2)/Pu35:3863 bridge;
any later functional test must retain damage, other sides and physical dependence.

## 2026-09-27 — Two fish tablets and a cross-root prediction support gate

**Progress classification and question.** Previous turn was progress: primary
photos, variant drawings and rejected identity shortcut changed the evidence.
Continued the full decipherment goal with two independent original-photo tasks
and a new prospective support design. This step tests whether a roof-state
classifier could be assessed across different bases without repeated-reference
or formula leakage; it does not fit a classifier or assign sign readings.

**4493/EH493 source task.** Agent located the original Vats XCVI493 plate on
retainedPDF200 and Vats tablep349/leaf377 row493. M77's already authenticated
EH numbering rule yields4493→EH493. Exact table gives0.4×0.23in,4–7ft,typeh,
white steatite,MoundF,8650b. The same table assigns8650b to several other
objects; narrativep58 describes a group and cites433. Rejected using either
group identifier as a unique-object key or433photo as493. Both493faces were
retained. Broad capped fish/comb and reverse U/long-stroke cluster compatible;
coarse reproduction does not independently certify four small flank marks or
exactly four reverse strokes. No clear large missing section, but fine damage
and complete-field survival unresolved. Parent viewed both faces, exact row
and headings. Failed flattened-OCR493 match was corrected using retained image,
not treated as source absence.18pins,4crop coordinates, no new downloads.

**5477/13592 source task.** M77 p824/PDF833 gives13592/Pu61:4076. CISI2
p444/PDF479 H-889 exactly13592/HM332/FC4483/photoP1070, with published faces
onp337/PDF372. Parent independently viewed row, M77 entry and both faces.
CISI4483 is Finnish Concordance, P1070 is later photography; neither silently
replaces the historical Pu print. Original Pu61:4076 remains unrecovered, but
later original-object images are exactly joined. PhotoA shows fish/comb/flank
marks, no separately recognizable roof; wear and upper margin make absolute
roof-absence certainty inappropriate. PhotoB ring/cup motifs remain nonscript;
field-symbol83 is notM083. Direction2 and normalizedorder stay distinct. No
sides joined or token reversal. Unrelated Vats excavation4076 rejected as a
photograph-number match.19pins,4crop coordinates, no new downloads. Combined
photo audit verifies37pins and8pixel reproductions; no fine exact new photo
transcription or die-independence claim. Frozen normalized reviews unchanged.

**Prospective support design.** Saved roof_transfer_support_protocol.json before
new grouped counts, after explicitly acknowledged prior roof-coverage exposure.
Independent design agent saw no new outcomes and approved exact fixed-threshold
matching. Clarified metadata null/empty/whitespace and reserved sentinels before
counting. Bundled networkx/scipy unavailable; no package needed: existence of two
vertex-disjoint edges can be checked exactly by enumerating unordered edge pairs,
without maximum-matching claims. Two fish pairs share one root and cannot supply
opposite endpoints across pair index. Group all structurally eligible records
before metadata exclusion, joining equal refs or identical full sequences with
all12selected endpoints replaced by TARGET. Preserve transitive components;
never rebuild after purging heldout-root components. Match pair/site/type/len/pos,
require two component-disjoint opposite-state pairs in test root and in at least
two training roots AFTER purge. Unknown-label matching is a separate sensitivity.
Missing full object/die and image-level authentication remains a separate gate.

**New support results.** Strict1293eligible records,526selected occurrences,
1139totalcomponents,406target-bearing. Broader1978eligible records excludes78
one-token fields from previous2056complete pool;721selected occurrences,
1464totalcomponents,490target-bearing. With known secondary labels only fish
passes the marginal two-pair gate in each corpus. Allowing unknowns adds trident
but no third root. No heldoutfold passes in any of four branches. Strict known
fish components74plain/48roof/6mixed;trident47plain/1roof. Strict unknown
trident100plain/2roof passes;cross andthree-strokes have no eligible roof.
Broad unknown cross7plain/2roof has no matched-stratumedge;basalU has oneplain
component and noedge. Saved all occurrences, component memberships, strata,
edges, exact witnesses and purged IDs. No outcomes used to loosen gates.

**Finite proof and independent verification.** A purge deletes possible edges;
it cannot create a two-disjoint-edge witness. Fewer than three marginally passing
roots therefore implies no declared fold canpass. Independently reconstructed
components using BFS reference/formula adjacency, edges via all opposite-state
occurrence pairs, and every100root support pool across branches/folds. Strict
flags reconstructed from doccount/direction/length/doubt/loss, source refs and
record-ID uniqueness checked;417null-value coverage checked. Review revision
pins checked. Independent code-review agent found no blocking error without
opening corpus outcomes. Persisted exhaustive four-vertex-partition oracle
agrees on all1024simple5vertexgraphs. Nine focused tests additionally cover
triangle/star/path distinctions, mixed-component reuse, cross-pair/position
strata, cross-stratum reuse, transitive unknown-metadata bridges, exclusions,
and marginal support erased by heldoutpurge. No probability/power claim follows.

**Persistence and minor failures.** Added support producer/verifier/protocol,
pre-count design and later code reviews, result ledgers, photo audits and
qualified417indexlinks. Pre-count design filename probes before agent creation
returned absent; waited for saved design before first corpus count. An accidental
word in the draft combined report was corrected before validation. Previous
source/task reviews were not rewritten. All new material derived from retained
raw sources, so source registry remains289records. Full pipeline validation now
running; goal remains active and no semantic/phonetic value established.

Final validation: full pipeline exited0 with218tests passing. Independent
support verifier reconstructs100root pools and four grouping graphs, checks
2906strict flags from source fields, six design/code revision pins, all417null
values and the finite edge-deletion implication. Photo audit verifies37pins
and8exact crop reproductions. Both source-review agents completed; parent
independently inspected the new artifact photos and identifier excerpts.
All result-input and32index source hashes verify; index contains M001–M417
once each, now35rows with qualified context links. No semantic or phonetic
value was introduced. All289source records retain valid byte counts/hashes;
no downloads added. All1081local Markdown links resolve. Final manifest covers
395code/docs,1741results and295processed files, refreshed after this entry and
verified against every file plus the source registry.

This turn is concrete progress: two additional primary object identifications,
qualified photographic checks, an exact grouped-support result and independent
finite verification. No decipherment is established. The goal remains active.
Useful next evidence includes exact5444/Pu35:3863 provenance, better independent
4493/H-889 fine-feature imagery and new complete roofed attestations beyond the
selected native-M export. Retesting the same unsupported three-root design or
loosening its gate after seeing outcomes would not supply that evidence.

## 2026-09-27 — Expanded roof coverage: copper fields, M334 variants and Dholavira24475

**Question and scope.** The prior grouped-support screen cannot support a held-out
root prediction. Sought primary evidence outside that selected flattened export,
without changing frozen gates or treating new source rows as independent objects.
Parallel source reviews covered copper-tablet M138, allW391 candidates, and
Dholavira/Nausharo recovery; parent traced the twoM334 artifacts and integrated
results. Another agent independently reviewed the M334 identity and shape claims.

**Complete enumeration.** Persisted delimiter-aware raw enumeration of W678 (3),
W391 (10),W731 (1),W044 (1), plus M354/W729 (1). Separate native endpoint enumeration
contains14 records: M138: 4, M163: 5, M334: 4, M092: 1. Literal IDs, source condition,
alternatives, doubt and unknown spans retained; translation/language/notes
columns excluded. No catalogue conversion or object joining occurs in that
script. All ten W391 rows are accounted for: four documentary old target joins,
one qualified FEM119/2119 candidate, known 2923 with unrecoverable target, two
unjoined historical candidates and DHR/Ns candidates separately reviewed. K45
field 19360/ASI68.1.51→8054, MIC51/HR4945→1051 and MIC397/VS3227→1397 were checked
against primary records. DK7854/CXXXI37 and M1384 were not merged through shared
strings. Native 2923 initial LOSS and other doubtful tokens remain unchanged.

**Crossed-sign copper tablets.** M77 printed 93/PDF104 gives two complete fields
for 3319 and 3320. Both first fields M287 M319 are absent from the flat export; longer
second fields retain M138. Exact 3319 export is +000-342-067-138+ with NO asterisk,
correcting the initial approximate locator. Appendix DK4067/ASI63.10.271 maps 3319
to CISI M510, DK4069/ASI63.10.270 maps 3320 to M509. CISI1p128/PDF164 photographs
all four faces. CISI A=M77 side2, B=side1. These are two separately catalogued copper
tablets, not four independent samples. Fine roof-cross strokes remain uncertain
in scratched photographs;3319 unknown span not restored. No physical-fracture
inference from transcription loss and no context/depth invented. Agent: 33 pins,
10 crops, no new raw downloads. Parent personally inspected the identity excerpts,
normalized fields and all four faces.

**Roofed basal-U.** M77 Appendix V rules authenticate 1403=MIC403 and 2364=FEM364.
MarshallIIp404row403=D262,2.25×0.6in,typeF,white steatite,depthdash. CISI1 M354 has
D262/NMI15/HU912; its A/a/B/C views are one object. Mackay p380 row364=DK5890,
1.02×1.02×0.26in,typeB,steatite,locus Bet.Bls.1(V)&10,level −11.7 ft. CISI2 M810
repeats DK5890/MD195/JL311/a:P231. Following tiny accession 50.14 remains tentative
and unused. Both target roof/body/basal arrangements are visible. M354's long
extension is oblique/curved, M810's approximately vertical; original Appendix I
p790/PDF799 explicitly labels corresponding M334 variants 1403/2364. W729 at M354 and
W731 at M810 locally correspond to M334. P314 lists W731 but no W729 entry in snapshot.
Neither local comparison yields universal equivalence. M810's missing lower
corner is in animal field; upper inscription broadly preserved. Two existing native
records, no new counts.45 pins/13 exact crops. Independent reviewer verified both
chains, source order, impression-to-impression shape comparison and damage scope;
23 revision pins include supplemental primary variant page. No substantive correction.

**Dholavira and Nausharo.** Exact DHR24475 museum metadata and Bisht 2015 p286 entry119
lead to accession-captioned colour photo. Rightmost upper group visibly has roof
above forked stem. All four apparent groups not independently assigned M IDs; reading
direction and every-stroke completeness not certified. Apparent field extent
retained despite wear/cracks. Primary p247 row8 gives 24475 NM, GSQ25x10x4, stratum6,
A470/D980cm; stage/area/inscription cells blank. Its motif Goat conflicts with museum
unicorn; retained unresolved, not used for sign inference. New graphic witness
beyond five selected native M163 target references, no claim of a globally new artifact or native
M77absence. Ns53/NS91.02.17.01 remains unresolved: exact searches, Jarrige1996
primary article (PDF403), CNRS routes and CISI3.2 catalogue do not yield an exact photo.
33 pins/3 crops; parent independently viewed the full accession page, photo and context table.

**Downloads and failed paths.** All 20 newly retained raw artifacts registered with
URL/bytes/SHA256: two old publication JPEGs plus 18 agent artifacts. Breakdown: 10 download
bodies,2 tool capture JSONs, 8 response/header artifacts. Includes the actual 404 body and empty
timeout header placeholder, expressly no received content. Initial ASI404, Persee403,
archive500 bodies were not read/retained. Slow 127 MB archive PDF was interrupted during
in-memory read; partial buffer unrecoverable, not presented as a retained file. Targeted
report page images subsequently succeeded. Museum HTTP port81 timed out, HTTPS path404.
All retained bytes in data/raw; retained primary reports and corpora reused.

Parent initial Marshall PDF57–59 guess hit p406–408, correct table p404/PDF55; all renders
retained with unique prefixes. Archive page indices lacked reliable printed labels;
visually checked. OCR failed to locate DK5890; used original table. System Python lacked
pypdf; bundled runtime used. Guessed zsh globs failed; rg discovery used. A suspicion that 862 pages
made an old CISI1 extraction inconsistent was unwarranted: new extraction manifest also
reports 862 pages for the actual pinned PDF. The page count does not discredit the source;
exact printed page images were the identity evidence. This corrects the overstated
'inconsistent page count' wording in the first M334 attempt note without rewriting the
independently reviewed revision. Parent integration initially expected 'evidence_files'
 for all reviews; DHR ledger uses 'pins'. Corrected adapter; then 133 pins/26 crops pass.

**Interpretation and persistence.** More complete coverage reveals missing fields,
differently partitioned shape variants and disagreements over damaged readings. They
must not be collapsed into one global W/M dictionary. No previous roof protocol, count,
strict flag or semantic value changed. Added typed registry integration, enumeration,
combinedaudit, source/cropcode, individual reviews, independent review and combined
report; added qualified 417-sign index links. Full pipeline validation pending below. Goal
active; no decipherment or common roof meaning established.

Integration check: the first full pipeline reached the all-sign index after
218 tests and all audits passed, then rejected the new result because it used
new_semantic_values/new_phonetic_values instead of the index contract
established_semantic_values/established_phonetic_values. Corrected those two
result keys to the existing contract; their values remain zero. Reran the new
audit and index first, then the full pipeline. This was a schema integration
failure, not a changed source finding.

Final validation: the corrected full pipeline exited 0 with all 218 tests
passing. The extension audit verifies 133 evidence pins, 26 exact pixel crops
and 23 independently reviewed revision hashes. The source registry now contains
309 artifacts: 262 downloaded bodies, 34 web captures and 13 response/header
artifacts. Every registered byte count and SHA256 matches; the only unregistered
raw-folder files are the pre-existing README and repository license. All 1,100
local Markdown links resolve. The all-sign index contains M001–M417 exactly
once, all semantic/phonetic values null, with 37 rows carrying qualified context
links and all 33 index source hashes verified. Eleven new audit input hashes
also match. The final integration verifier is saved and added after index
construction in the offline pipeline; it was run successfully on the completed
outputs. The manifest is refreshed after this entry.

No decipherment or universal roof operation has been established. The goal
remains active. This phase adds an exact-captioned Dholavira witness, four
recovered copper-tablet fields and two authenticated M334 artifact comparisons,
while preserving the distinction between catalogue coverage, object identity,
photographic legibility and semantic inference.

## 2026-09-27 — DHR24475 comparanda, segmentation limits and external predictions

**Previous turn classification: progress.** It changed authoritative source and
review state with an exact Dholavira photograph, recovered copper fields and
M334 object comparisons. This turn asked whether the Dholavira string supplies
an independently inspectable near-parallel, and what kinds of new evidence
could discriminate meanings rather than merely repeat structural results.

**Pre-count design and implementation.** A separate agent read only the seed row
and header, then froze the DHR24475 context protocol and design. The parent
implemented pure matching helpers and six synthetic tests before running any
corpus outcomes. The tests cover all 81 four-code strings over a three-code
alphabet, unknown/damaged syntax, leading zeros, slash alternatives, and false
matches caused by reversal, insertion or substring matching. The protocol
initially excluded000 only. Before counting, a separate implementation note
conservatively excluded999 too, following the existing parser's documented
unknown/separator treatment. The original protocol hash remains unchanged.
Closed-plus syntax does not establish a complete physical field. No direction
reversal, face concatenation, W-to-M conversion, translation field or Poor-label
exclusion was used. Class overlap and physical-identity uncertainty are explicit.

**Finite outcome.** Scanned all 5,680 raw rows: 552 primary closed-plus singleton
four-code rows, 50 boundary-sensitive rows, 10 slash-sensitive rows, 254 four-cell
unknown/separator cases, and 4,814 other exclusions. Of the latter, 4,811 have a
non-four cell count, two have missing/invalid endpoints and one has malformed
cell/interior-boundary syntax. The only match is seed4196.1 itself. There is no
additional duplicate, no exact-tail initial substitution and no other
one-position substitution. Neither boundary sensitivity nor exhaustive possible
slash alternatives adds a match. There are no additional same-stem companions.
All row decisions and literal metadata are saved. This is a negative result for
one declared source/grammar/transcription, not evidence that no ancient parallel
existed or that a roof modifier has no function.

**Independent reconstruction.** Separate verifier code imports no producer
functions. It checks the frozen protocol and all seven input pins, reconstructs
all 5,680 row decisions, compares 602 literal rows by direct tuple/projection
operations, and expands all ten slash rows into their finite concrete option
sets. All 5,704 checks pass, including complete hit/uncertainty metadata, nine
branch/class count tables, companions and seed treatment. The synthetic tests
exercise helpers; the independent reconstruction additionally covers the actual
runner parser and its source-row decisions. No significance test was proposed.

**Graphic review kept independent of context results.** Another agent inspected
DHR24475's photograph, four overlapping inspection crops and original numbered
M77 representative pages32–35. M163 is the strongest shape candidate. The upper
marks cannot be confidently isolated as a two-stroke unit, so M099/M100 remain
unresolved; an apparent M099 upper-placement preference is expressly conditional
on segmentation. The shaft/wing is compatible with M402 but has weak internal
strokes. Left crossing/terminal details cannot securely distinguish M216 from
nearby M222. No unique ordered M string, exact token boundaries, reflection
convention or reading direction was certified. The four regions are not four
proved tokens. Parent personally inspected all four crops and retained these
limits. Twenty evidence pins and four exact pixel crops verify. No missing
strokes were filled from the stored W string or the absence of comparanda.

**Whole-inventory synthesis.** A third agent reviewed the major current results,
retaining 39 exact file pins and verifying 417 unique IDs with null readings and
13,372 primary occurrences. The report distinguishes exact restricted
contradictions from unidentified numeral, roof, allograph and language claims.
It records the rare tail (264 signs below ten primary occurrences, 112 hapaxes)
and the strict native sequence subset's 332 observed/85 unobserved types. It
also distinguishes the original59-type U-context layer from the corrected
60-type layer; these are not independent counts to add. Two prospective external
predictions are specified: capacity within a fixed vessel class, and bead-craft
association at deposit/phase level with independent controls and unreadable-text
bounds. Neither proposed test is reported as executed or already adequately
supported. Broad internal string scores cannot identify external referents.

**Persistence and attempts.** Saved producer, verifier, protocol, implementation
note, tests, result ledgers, independent graphic review, synthesis and combined
DHR report. README links both new reports. Frozen earlier reports and the all-sign
index meanings remain unchanged. Added a streaming source-fetch helper for future
work: response and HTTP-error bodies are written incrementally to data/raw, with
partial files retained on interruption and typed acquisition records. It was
syntax-checked, not exercised on a live download this turn. This addresses the
previous in-memory PDF retention failure; no new downloads were needed here.
Early file probes occurred before agents saved their outputs; those absent paths
were not treated as terminal agent failure. One zsh glob matched no file and
stopped that invocation; subsequent discovery used rg. Full offline validation
is recorded below after completion.

Final validation: full offline pipeline exited0 with all224 tests passing.
Independent DHR reconstruction passes all5,704 checks with no differences.
Graphic/synthesis integrity checks verify59 evidence/snapshot pins and four
exact pixel crops. All new producer, verifier and combined-audit input hashes
match. The309 registered raw artifacts remain unchanged and fully verified;
all1,147 local Markdown links resolve. The all-sign index still has417 unique
rows, all readings null,37 rows with earlier qualified context links, and33
verified source hashes. No speculative DHR M-code assignment was added to it.
The final manifest contains425 code/doc files,1,807 results and310 processed
files; it is refreshed after this entry and verified file by file.

The active goal remains unresolved. This turn supplies a fully reconstructed
negative comparandum search, stricter graphic uncertainty and an inventory-wide
assessment of what would discriminate semantic hypotheses. The next substantive
step should seek a securely identified external measurement or independently
classified deposit set under one of the stated prediction designs, rather than
loosen the empty DHR comparison or roof support gates after seeing their results.

## 2026-09-27 — Primary vessel heights, contents and capacity-identity corrections

**Question.** Can primary measurements and artifact identities turn the proposed
capacity-per-stroke relation into an external test? Three parallel reviewers
checked H370–372 photographs/identifiers, the actual Fuls table source, and
CISI2 M1374. Parent followed the explicit Vats printed91 footnote to the original
contents table. A second reviewer independently read the split table and context.

**New data and result.** Six Internet Archive JPEG pages (leaves117,277–281,
printed91,251–255) were fetched with the incremental preservation helper, all
HTTP200 and visually inspected. Six serialized header records were retained.
The primary table explicitly gives 1033A height3ft and1033B height2ft10in. They
convert to91.44cm and86.36cm, agreeing with Fuls's public text to0.1cm under the
same excavation numbers. These are height agreements, not measured capacities;
no new complete count-and-volume pair satisfies the prospective test. Original
measurement precision and possible shared archival dependence remain unknown.
Both jars are F/I/M11/16,depth5ft6in,stratumIII, associated with a broken pavement
and drain. Vats says B lay south under the drain and A was west half buried.
The neighboring shaft's dimensions were explicitly excluded as jar measurements.
The first plate locator rendered PlateXXI/PDF54 rather thanXXIII; retained as a
failed locator, then corrected toPDF58/PlateXXIII(a), whose caption names the
pair. No capacity was inferred from the photograph or human figures.

**Contents and extra lead.** Independent readings agree that charred wheat and
slag belong to row3/1033B only; row2/1033A has charcoal and other listed finds.
Rows and dittos were checked across both pages; dotted blank cells were not
silently filled. Bone-ounce fractions are unnecessary and remain qualified.
These are deposition assemblages, not certified original commodities or sign
referents. Vats's funerary interpretation was kept distinct from his observations.
Row18 explicitly identifies inscribed3822, height2ft3in and mouth11in, squareM12/6,
stratumVI, depth15ft9in. Its three shoulder pictograms are not a certified rim
tally; neither internal profile nor fill measurement was recovered. It remains
an external-measurement lead, not a cherry-picked fourth calibration datum.

**Corrections.** Fresh CISI1 metadata confirms H370=12908,H371=1033a,H372=unknown.
The Fuls public-text H372=12908/H370=1033b association remains contradictory.
Primary height agreement cannot resolve it. The CISI4607–4609 column is Finnish
Concordance, not Mahadevan. The attempted equal-number M77 route failed: original
M77 4607 has different multi-field content and4608–09 are skipped in that list;
the Appendix's EH mapping does not bridge FC. Earlier mahadevan_ref fields are
explicitly withdrawn as verified links in the new report, without altering old
frozen evidence. H371's seven upright primitives plus oblique may segment as six
tallies plus an angular sign; the count is not automatically seven. H370's faint
short extra trace and H372's angular/short marks remain uncertain. No grouping
was selected from expected volume. CISI2 M1374 is UPM/MD-138, a photographed rim
fragment; it cannot be joined by the integer alone to Fuls's complete73×69cm pot.
Adjacent whole-vessel photographs are M1372/M1373, not M1374. This identity limit
does not refute Fuls's intended-object volume calculation.

**Unsuccessful access and implementation attempts.** Legitimate publisher links
provided actual contents/abstract PDFs, confirming the article's startpage101,
but no target table images. Two initial files ending.pdf were HTML wrappers,
explicitly typed as such. Full-document link led to login and was not bypassed.
A public Academia landing fetch returned403; its complete error body and headers
remain retained, not source content. An earlier sandbox DNS failure had no body.
No blocked attachment route, purchase or message was attempted. Author/public
institutional searches supplied no alternate table copy in the bounded search.
An HTML parser initially hit a None attribute; guarded and corrected. An absent
pdftotext executable was replaced with bundled pypdf. Font-cache warnings did not
prevent successful readable Poppler output. MD1374 public searches found no exact
capacity-vessel bridge; unrelated exploratory page renders are preserved. An
early parent probe preceded completed agent files and did not indicate failure.
The MD1374 report initially said values remain0; corrected before freezing to
zero assignments and all417 values null, then explicitly repinned.

**Persistence.** All31 new raw artifacts are registered by kind (download,
web-tool capture, response headers/error body), bringing the registry to340.
The streaming helper was exercised successfully, unlike its previous syntax-only
check. Saved four specialist reviews, a combined report, manual structured
findings, exact crop scripts/manifests, conversion script and integrity audit.
The combined report explicitly supersedes overstrong identity/count readings in
earlier capacity evidence while keeping the conditional arithmetic reproducible.
No old frozen pins were silently refreshed, no corpus meanings were assigned,
and no new capacity fit or significance test was run. Final offline validation
is recorded after completion below.

Final validation: the complete offline pipeline exited0; all224 tests pass.
The new audit verifies107 distinct evidence-file pins,25 exact pixel crops and
both height conversions. All340 registered raw artifacts verify (277 downloads,
35 web captures,28 archived response artifacts); all1,170 local Markdown links
resolve. The existing all-sign index retains417 unique IDs, all semantic/phonetic
values null,37 earlier qualified context rows and33 verified source hashes.
Earlier frozen DHR/synthesis checks still pass59 pins and4 crops; no prior
snapshot was silently rewritten. The final manifest is refreshed after this
entry and checked against all recorded files. This is progress in primary
measurement recovery and correction, not completion of the decipherment goal.

## 2026-09-27 — Inscribed jars, full contents-table screen and missing-status bounds

**Prior-turn classification: progress.** Primary vessel heights and identity
corrections changed the next available test. This phase followed explicit
inscribed-vessel leads3822,5919 and10252 while preserving the requirement for
external rather than purely internal semantic evidence. Three parallel agents
reviewed3822's photograph/joins,5919/10252 contents, and their possible text
bridges. One then independently screened the complete right-hand table pages.

**Declared frame and source recovery.** Saved INSCRIBED_JAR_FRAME_DESIGN before
new full-frame table review, explicitly identifying the three known seeds and
7765 comparison as already observed. Selected TableI only, excluding the separate
54-jar group. Parent downloaded right-hand printed259/261/263/265/267/269/271;
reused earlier255 and agent257. All nine pages were personally inspected.
Agent target pages added256/266 and narrative165;264 was a retained wrong locator
covering100–115 rather than116. Initial table keyword screening of retained OCR
returned no hits because it had badly lost the table; this was not a negative
inscription result. Page-number metadata and actual image headings fixed locators.

The declared expected178 came from the narrative. Both complete visual passes
instead find contiguous1–176 on pages255–271, with the final page explicitly
concluded. Unlocated expected177/178 remain a documented source discrepancy;
no synthetic records were created and the separate54 were not added. The source
also gives a broad total230 elsewhere, but arithmetic agreement176+54=230 is not
proof that any particular source number is a printer's error.

**Primary contents and text distinctions.** Jar5919/serial35 is described as
inscribed and napiform on the left-hand table and as crushed in narrative165;
its table squareP23/10 conflicts with narrativeP23/5. Both give depth10ft.
Jar10252/serial116 explicitly has seven pictograms in two lines, F/IV/I12/4,
depth9ft,stratumIV. Neither has recorded dimensions in these cells. Both have
cereal/plant traces in mixed assemblages; that is not original-use or inscription
timing proof. The separate faience object inside10252 explicitly links to
VatsPlateC671 and through the primary M77 AppendixV rule to reference4671.
The M77 text has a lost counterpart and surviving native+089-328+ field. This
is a contained-object text, not the jar's own seven characters. Lipi10252d671
rows212.1/.2 are candidate contained-object locators; the suffixd and exact
lost-field length were not authenticated. Neither jar's own text was recovered.
Exact-number extraction searches, inspected Vats pottery platesCII–CIV and
M77 pottery appendix pages yielded no explicit own-jar bridge; catalogue-wide
absence was not claimed. The row54 contained-seal lead was not pursued beyond
the fixed-frame screen in this phase.

**Correction of previous page reading.** Jar3822's explicit table reference and
photograph link to PlateXXIII(e), not(c). Panel(e)'s inscribed jar and stands in
StratumVI/M12/6 match the table; panel(c) is a different hearth/manger scene.
The prior independent table review had overconfidently read the tiny letterc.
Two new reviewers checked the enlarged original and caption, and the parent
checked the full plate. New reports explicitly supersede that panel letter;
frozen files/pins were not silently changed. The shoulder crop is too weak for
a numbered transcription. H98-3822/H98-3823,13823 and a disordered CISI OCR3823
hit were rejected as substring/column-confusion routes, not assigned to the jar
or stands. No CISI/FC/M77 join for3822 was established.

**Independent complete screen.** Both readers agree on60 cereal-related report
rows:58 direct author cereal/grain/wheat descriptions,30 as apparent former grain
fill and135 as cereal-like sesame impressions. Leaf/root-only147 is separate.
The right-hand table has positive mark/seal reports18/44/54/116/156/165, with
main-container marks only18/116; left-hand description/narrative adds35.
Other positives concern contained goblets, seals or a seal fragment. Row44 says
incised, not necessarily a classified script;165 has four upright marks on a
goblet, not on the containing jar. Row156 does not explicitly describe surviving
writing. Independent reviewer initially read row44 asinscribed and152 astablet;
parent prompted native reinspection, correcting these toincised andtumbler.
These refinements change neither reader's independently derived row sets.

**Mathematical result.** With176 reporting rows,60 cereal-related mentions,
three known inscribed jars(two cereal mentions/one nonmention),173 inscription
statuses remain unestablished. Enumerating6,843 grouped completions gives sharp
reporting-association bounds−58/59 to+60/61. Independent closed-form inequalities
and constructive extremal assignments verify both bounds. Removing the two
qualified cereal descriptions still permits both signs. These concern reports,
not actual grain absence; they demonstrate why even the direction of a proposed
association is unidentified. No significance test, numerical calibration or
semantic assignment was made. The primary context is useful, but cannot turn
M089/M328 or an unknown jar glyph into a grain reading.

**Acquisition and implementation attempts.** Network streams finished normally.
Two parallel agents acquired narrativeleaf191 before coordination arrived, and
agentleaf293 completed before the parent's stop message about its existing copy.
Both body/header pairs are preserved and duplicate hashes explicitly grouped;
they are not independent archaeological evidence. All43 new raw artifacts are
registered:14 fetched images(including2duplicate bodies),14 serialized headers,
and15 clearly typed local renders/crops. The overall registry now has383 artifacts.
The first combined audit compared integer serials to the independent review's
structured row objects and failed; inspecting the schema and comparing their
serial fields corrected this implementation mismatch without altering data.
Recorded exact pixel crops, all-row ledger, specialist reviews, source registries,
producer, closed-form verifier and combined audit are reproducible offline.
The full pipeline and final manifest verification follow below. Goal remains open.

Full-run implementation correction: the first run passed all224 tests, then
the older archive verifier raised a TypeError because local derived-image records
have url:null. Their parent-file provenance is intentionally retained; no fake
network URL was substituted. The verifier now skips non-string URLs before its
specific archive-URL filter, while still requiring exactly four matching archive
files and all their byte/MD5 checks. Its direct check passes. Saved the failed
run as results/inscribed_jar_first_run_failure.log, then started one new full run
after the original process was confirmed exited1. Source claims and observations
were unchanged by this fix.

Final validation: the second complete offline run exited0, with all224 tests
passing and exactly four original primary-archive checks intact. The new combined
audit verifies96 distinct evidence-file pins and31 exact crops. Independent
screening agrees across allnine pages,176 serials and60 cereal-related report
rows; closed-form bounds agree with the6,843 grouped completions. All383 source
records hash/byte-verify and all1,188 local Markdown links resolve. The unchanged
all-sign index still has417 unique IDs, all semantic/phonetic fields null and33
verified source hashes. Earlier frozen review audits continue to pass. The final
manifest is refreshed after this entry and checked file by file. This phase
made progress through a new exact contained-object association, a complete
declared reporting screen and an explicit identification limit; decipherment
remains unachieved and the goal remains active.

## 2026-09-27–28 — Contained-object identities and repeated vessel stamps

**Previous turn: progress.** The fixed table screen supplied five contained-mark
or seal-fragment rows,44/54/116/156/165, and one authenticated contained-object
text bridge. This phase followed every remaining row, without changing that
selection or promoting contextual proximity into identity. Parallel reviewers
handled54,156/165 and the original pottery discussion; parent handled44. A
further independent check examined the repeated-goblet-stamp statement and its
limited logical consequence.

**Row44 and an important register ambiguity.** New original table258 gives
register7856,F/I/M12/7and8,6ft,stratumIII, a large round cracked jar. Row259 says
one contained goblet sherd was incised and another bore a seal impression.
The original narrative91, already retained, also clearly reads7856 but describes
an inscribed goblet fragment inM12/7, compared as similar to PlateCIV73. A literal
7856 OCR search failed because the old extraction mangled the numeral; goblet
and stamp keyword navigation located the passage, then the image supplied the
actual reading. Possible assemblage-level registration, loose reference and
source error remain alternatives. No particular sherd, own-jar text or shared
stamp with73 was inferred. Secondary substring DK7856 identifies a Mohenjo-daro
implement, not this Harappa find. Initial probes for7860/10559 also produced
unrelated substring matches; original pottery pages instead clearly supply10589,
so the weak OCR spelling was not retained as an authenticated identifier.

**Row54 and a qualified candidate.** ContainerXII isD/III/S30/1,3ft6in,stratumII,
large napiform bottom portion. The contained two-sided steatite seal has no
separate number in the table. Narrative189 authenticates a contextual candidate,
J630, and its independent chain to PlateXCVI446,CISIH890(FC3446,HM297), andM774446
via the explicit primary EH rule. Square, depth and stratum match the jar record,
but the narrative is under TrenchII and calls it a scattered find; no containment
statement links it toXII. The trench discrepancy was not repaired by guessing.
Original189 gives six plus four pictograms, correcting OCR's five on the first
side. The candidate's text was not copied into the row54 record.

**Rows156/165.** Original270 supplies a blank register for156,AB/ExtensionPitsI&II,
Q24/18,5ft3in,stratumII. The unicorn-seal fragment's own identifier and surviving
script remain unreported. Row165 is jar7737,F/GreatGranaryArea/I9/5,3ft4in,II.
Three pointed-base goblets are listed; one has four upright incisions. Neither
dimensions nor a separate goblet number, photograph or timing is established.
The description ditto chain reaches the very-fragmentary entry at162; blank
cells do not become zero. A bounded92-file local text screen and Harappa metadata
screen found no eligible exact object bridge. The four returned text locators
were irrelevant/generic. Jar12414/unicorn47 is a different container/location;
grid-only rod2551/dog7071 were explicitly rejected. Three listed goblets do not
prove complete original contents or falsify every interpretation of four marks.

**Pottery production observations.** Retrieved original286–287 after checking
the Archive page map. Neither5919 nor10252 is named there. The source reports
different stamps for21/23/24/46, a shared stamp for53/72/73 and unillustrated
7860/10589, and another single-character stamp for74/76 and unnamed others.
These are source-reported groups, not new vessel identities. Illustration73's
upside-down impression is object-specific. The list of slip-cutting examples
ends85, not OCR86; unrelated stone item599 is not OCR590. Cut-through slip gives
an order between coating and incision, not by itself a post-firing date. The
author's proposed potter/owner authorship and names remain conjectures, kept
separate from the observed surface relation. J97 is explicitly unillustrated.
The weaker7856 similarity-to73 statement was not merged with the shared-stamp
group. Detailed source references and attempts are in the specialist ledgers.

**A narrow identifier constraint.** Parent and independent reviewer visually
verified original91: trough470 inM12/13 held two pointed-base goblets each stamped
with the same seal, citingPlateCII21. No unique field numbers for the individual
goblets follow; the later3262 reference on the page was not assigned to the pair.
Conditional on the report's accuracy, distinct vesselsA/B with equal stamp
designD(A)=D(B) disprove injectivity of that design alone over individual vessels.
This is a historical-report counterexample to a unique-vessel-design claim,
not a decoded name, not a statistical test, and not a modern examination of
both objects. Owner, maker, workshop, batch/class roles or extra distinguishing
marks remain possible. The potter-name suggestion in the source is conjectural.

**Coverage and persistence.** Allfive selected rows are now explicitly followed:
one previously accepted primary contained-text bridge(116) and four unresolved.
Zero new accepted contained-text bridges and zero own-jar texts were recovered;
these limits are machine-readable, not hidden by the new source work. Saved
five reviews plus synthesis, structured records, crop scripts, source integration,
coverage producer and combined audit. Its first direct run passes149 distinct
file pins and16 exact crops. New raw artifacts total14: six downloaded JPEGs,
six serialized header records and two local crop derivatives. The registry now
contains397 artifacts. Initial jar54 sandbox DNS failure produced no body and
is retained as an attempt record; one permitted retry succeeded. Original and
derived bytes retain distinct types. No frozen evidence or sign meaning was
changed. Full offline validation follows; goal remains active and unachieved.

Final validation: the complete offline pipeline exited0 and all224 tests pass.
The new review audit verifies149 distinct evidence-file pins,16 exact crops and
coverage of allfive fixed contained-mark rows. All397 source records retain
matching byte counts and hashes; all1,208 local Markdown links resolve. The
all-sign index remains417 unique rows with semantic/phonetic values null and33
verified source hashes. Earlier frozen audits and the preceding missing-status
proof still pass. The run manifest now records research date2026-09-28; it is
refreshed after this final entry and verified against every recorded file.
The goal remains active: this phase added primary identity constraints and a
limited repeated-stamp counterexample, not a decipherment.

## 2026-09-28 — Chanhudaro deposit frame, conditional contrast and field-record archive

Previous goal turn classification: **progress**. The contained-mark follow-up
persisted a limited repeated-stamp constraint and unresolved object joins. This
phase pursued the other discriminating test in the evidence-gap review: a
fish-family association with independently described bead-production contexts.
The goal remains active and unachieved.

**Design before new grouped outcomes.** Saved CHANHU_DEPOSIT_PROTOCOL.md and
obtained an independent design review. Existing site-wide fish outcomes and
9/D/8/E examples were explicitly already seen. We distinguished documented
production, informative lower-evidence reporting, and unknown; no demand for
perfect archaeological absence, and no conversion of narrative silence to a
negative. Direct deposit, associated building and broad square claims remain
separate. Linked215/286/297 form one potential dependence complex.

**Complete finite illustrated-seal frame.** An independent image reader
transcribed all65 LI1–33/LII1–32 catalogue rows on printed292–293. Every row has
excavation number, locus and signed level;60 have square and5 instead trench.
Six adjacent PlateL entries are outside the core and explicitly retained as
excluded. Original145 confirms unfinished specimens and direct-photo versus
plasticine-impression methods, but not an excavation census. Native rereads
corrected provisional low-resolution2848level and3359square/material readings;
raw source data were never rewritten. Allfinal65 requested fields are readable.

**Metadata-only join and independent reconstruction.** New script joins exact
fieldnumber/suffix and plate/item with compatible class. Of65,55 match,7 have
no candidate,2 have same-plate/different-number conflicts, and1 has secondary
MISC rather than SEAL class. LI26 is3043 (not secondary3817, which belongsLI25);
LII15 is2531 versus secondary2431. Five matchedobjects have7 location/level
field disagreements, including newlycheckedLI12 +7.0versus+7.2 andLI31
+14.9versus+14.1. Every one of74secondarysite rows has phase '-'. Independent
reconstruction reproduces allfullrows and summary; five targeted originals
visually checked independently. Metadata agreement is not authentication of
transcriptions, phase, or untested fields.

The first five-test join suite exposed two parser bugs: word boundaries failed
on the export's concatenated number/Pl and number/sq fields. Replaced these with
explicit letter/digit boundaries and added a bare-number/plate regression case;
allfive nowpass. An independent check subsequently detected a stale result hash
after the register's final annotation update, not a data/count disagreement.
The failed snapshot record is retained; rebuilding against the finalregister
resolves it with zero mismatches. These failures changed no sign data.

**Archaeological screen.** Reviewed the architectural narrative through74 using
bounded OCR locators, adjacent context and original images for substantive new
claims. Saved21 overlapping context records and13 exact crops; these are not21
independent deposits. Newdirectfloor evidence includes court190+10.4, with no
same-locus seal in this65-row frame. Verified tools/rawmaterial contexts and
shell/metal rivals outside9/D; preserved292/293 and253/255 distinctions and
aggregatefootnote mappings rather than guessing one-to-one square/locus pairs.
Corrected OCR drill-head4687 at206 to+6.8; bead-hone3013 at208+9.7 and nodules5178
near443+6.6 verified. Deferred three unverified OCR leads explicitly.

Bath442 is an informative lower-evidence reporting candidate: floor/drain+6.7,
with seals3215/3207 described nearby, not demonstrably on thefloor. Alternative
metalhoard284 is+9.5; nearby seal2390 is separately235+9.9. Seven namedseal
associations are reviewed individually; other58framedobjects remain unsecured,
not bead-negative or falsely claimed exhaustively reassessed. Current strict
supportmatrix has no secured matched phase/deposit/reporting stratum. No strict
craft p-value calculated.

**A weaker conditional calculation, not a substitute for the strict test.**
Before extracting grouped statuses, saved CHANHU_LOCAL_CONTRAST_ASSUMPTIONS.md:
associatedcomplex2285/2428/2529CC versus bathvicinity3215/3207, using alreadyseen
fixed-family andW220 statuses unchanged. This accepts unverified broad-area,
phase and reporting comparability; oneblock pergroup, noholdout or independent
workshopreplication. Productionassociated3 =1positive,1negative,1unknown;
bathvicinity2 =0positive,2negative. Bothfamily andplain contrasts have exact
bounds+1/3to+2/3. The solecertainpositive is passage seal2428;2529CC isnegative,
2285unknown. All5textsignatures differ, not proof of independence.

All32omission subsets were specified before the calculation;21 retainbothgroups
and11 areunavailable (notzeroeffects). Of21,12 havepositive lowerbound and9allow
zero; envelope0to1. Thus the direction is locally positive conditional on allfive
areaassignments, but guaranteed enrichment disappears if the singlecertain
positive association is excluded. No bead-specific effect, word or phonetics
follow. Independent brute-forceunknown-label enumeration verifies66
scenario/profile endpoint checks. Fullsupport failure remains explicit.

**Primary recording method and archive discovery.** Downloaded originalpreface
vi/vii and visually verified spatiallocusnumbers carried throughdifferentlevels,
signedworkingdatum and about5,000fieldcards/finds. These are not5,000seals or a
complete depositinventory. The firstreview correctly recorded archiveunlocated
atthatpoint. A subsequent boundedfive-query officialarchivesearch located Penn
Museumcollection1064, Chanhu-daroPakistanrecords: originalregister/sitelevel
notebooksBox2 and10objectcardboxes5–14 withcataloguedranges1–5457. Thisnewlayer
supersedes the unlocatedstate without rewriting its historicalpin. Individual
cardpresence/content and completeness remainunverified; no publiccardimagelink
identified. RelatedBrownpapers alsohavefieldreports. Pennweb403 and anindexlink
timeout are captured and do notproveunavailability; MFA's currentofficialaccess
notice isretained. Nooutreach occurred. Saved15range-based navigationtargets for
specificpublishedconflicts and test-criticalassociations, withsuffixuncertainty.

**Persistence.** All25newrawartifacts are registered together indata/raw:
9originalpageJPEGs+9serializedheaders,3officialarchive/accessHTMLs+3headers,
and1webtoolcapture. Registrytotal422. A firstregisterpagefetch failedDNS with
nobody; separateapprovedretrysucceeded, bothattemptrecordsretained. Searchlog
explicitly notes initialbatchfullresponse notretained; relevantofficialpages and
laterresponses captured. Raw/derived and source/interpretation types remain
separate. The combinedaudit currently verifies103distinctpins,29exactcrops,
65framerows and66exactboundchecks. Addedproducers,independentreconstruction and
audit toofflinepipeline. All417meanings remain null. Fullvalidation follows.

Final validation: the complete offline pipeline exited 0; all 229 tests pass.
The new combined audit verifies 103 distinct pins, 29 exact crops, all 65
frame rows and 66 independently enumerated bound checks. Independent join
reconstruction has zero mismatches. All 422 registered raw artifacts match
their byte counts and SHA256 hashes; 1,231 local Markdown links resolve.
The all-sign index retains 417 unique rows with null semantic/phonetic values
and 33 verified source hashes. No decipherment is established. The manifest
is refreshed after this entry and verified against every recorded file.

## 2026-09-28 — Primary local graphics and sign-specificity controls

Previous goal turn classification: **progress**. It established the 65-entry
Chanhudaro frame, explicit archaeological eligibility limits, a conditional
five-object contrast and the Penn field-record archive. This turn checked the
physical graphics behind that contrast and whether its statistic uniquely
selects a fish-like code. The full decipherment goal remains active.

**Protocol and independent design.** Saved CHANHU_LOCAL_SPECIFICITY_PROTOCOL.md
before new control outcomes. Kept the five artifacts and area labels unchanged;
used the other 60 objects in the primary frame for background frequency, with
ten unresolved joins unknown for every code. Matched singleton W220 to singleton
controls, excluding declared fish/compound mappings, W221 and placeholders.
Declared exact observed-positive matching, an additional unknown-count match,
and a half-to-twice frequency sensitivity. Independent design review clarified
that a higher upper bound can mean more ignorance, so strength compares lower
bounds. All site-wide target outcomes were already seen: this remains
retrospective and does not repair the failed strict deposit gate.

**Control calculation.** W220 background counts are 2 positive, 34 negative,
24 unknown. Eighty-one eligible non-target codes produce only eight distinct
local profiles. The exact observed-positive set has nine codes, none tying the
target; matching positive and unknown counts leaves six, also without a tie.
The predeclared wider band has 71 codes, including W368 and W790 with identical
[1/3, 2/3] intervals and W717 with [1/3, 1]. No wider-band code has a strictly
larger lower bound. W032/W390 have larger lower bounds only in the unmatched
all-code table, and are not frequency-matched counterexamples.

W368/W790 do NOT equal W220's five-object status profile. They are (P,U,N,N,N)
versus W220's (U,P,N,N,N), with different certain-positive artifacts. Grouping
three complex seals erases that distinction from the interval. No exact target
profile occurs among the 81 controls. Independent full reconstruction reads the
raw CSV without importing producer classifiers and verifies all 4,920 background
and 410 local statuses, sets, profiles, widths and rational bounds. An initial
draft verification sentence accidentally called equal intervals equal profiles;
corrected before final pins. The machine output always preserved the distinction.

The first producer attempt failed before results at a catalogue metadata entry
whose id is default_features, not P plus digits. Added an explicit P-numeric
schema guard and reran successfully. The control universe was not changed in
response to outcomes. A separate check found no W999 placeholder in accepted
frame rows, so the inherited classifier's handling of that unobserved placeholder
does not affect this calculation.

**Additional diagnostics, explicitly post-protocol.** Independent verification
shows all 81 marginal background-count intervals overlap W220's [2,26]. This is
necessary marginal compatibility only, not proof of jointly possible historical
texts, estimated frequencies or a replacement matched set. Omitting the sole
fish-positive 2428 leaves W220 [0,1/2], while W368/W790 retain [1/2,1/2] because
their positive is 2285. Neither multiplicity nor these omission results are
p-values or evidence of semantic equality.

**Primary images and failed visual leads.** Two independent photo tasks covered
all five objects. Exact original catalogue/plate identities authenticate
2428=LII19 and2529CC=LII23. A plain fish-like form is certainly visible on2428,
despite an unclear neighboring text portion;2529CC's displayed band supports
operational family absence with limited confidence in fine-code distinctions.
Both are original published photographs of plasticine impressions. Optional
CISI1/CISI2 label-location attempts did not securely locate C65/C69; those modern
aliases remain secondary, not invented primary-photo joins. Retained locator
renders include the unsuccessful page choices.

CISI1 metadata explicitly joins C17 to3207/LI22 and C22 to2285/LI15, supplying
original photographs plus impressions. C22's original has a substantial missing
upper corner of the inscribed face, partially obscured by the older impression's
rectangular presentation. Its whole original fish status remains unknown. The
review does not claim a missing second face or know why the export author set
complete=N. No specific missing sign was reconstructed.

The photo reviewer initially described small LI14/LI22 forms as fish-like.
Native enlargement and primary sign-list comparison withdrew those suggestions:
CH3215 has an asymmetric bow/limb structure and CH3207 divergent limb/upper
structures, compatible with source-asserted W125/M028 and W100/M008 comparisons.
They are not new members of the fixed fish family or W221. Parent independently
viewed the relevant crops. No broadened family analysis was justified. Visible
field absence does not by itself certify pristine original text edges.

**Post-selection control photographs and separate sensitivities.** The clear
oval/leaf form on C22 supports the graphic associated with W790; its broad
P355 crosswalk does not choose one of M261/M373/M374. The W368-associated shaft
and wing-like remnant crosses the damaged corner; its full diagnostic form is
not independently certain. The frozen catalogue analysis is retained. A separate
photo-conditioned sensitivity changes only that W368 positive to unknown,
reducing its interval to [0,2/3], while W790 keeps [1/3,2/3] under the remaining
source assumptions.

A second, explicitly conditional sensitivity withholds whole-original-text
absence on either bath comparator because image boundaries do not certify all
edges. Either negative becoming unknown changes W220 to [-1/6,2/3]; withholding
both gives [-2/3,2/3]. This is not evidence a missing fish existed. It shows how
much the positive bound depends on the negative classifications. The source
classifications, identities and older evidence layers remain unchanged.

**Persistence and checks.** Saved the protocol, design, complete control table,
independent reconstruction, two primary-photo reviews, crop scripts, sensitivity
producer and synthesis. No downloads were needed; the registered raw collection
remains 422 artifacts together in data/raw. The combined new audit currently
verifies 62 distinct pins, 16 exact crops, all five objects and seven sensitivity
intervals by independent enumeration. Added four new steps to the offline
pipeline. All 417 semantic and phonetic values remain null. Full validation
follows; neither the positive photo nor a tied control establishes a reading.

Final validation: the complete offline pipeline exited 0; all 229 tests pass.
Independent specificity reconstruction verifies 5,330 object/code statuses
with zero mismatches. The combined new audit verifies 62 distinct evidence
pins, 16 exact crops, five physical objects and seven exhaustively checked
sensitivity intervals. All 422 raw source records retain correct byte counts
and hashes; 1,245 local Markdown links resolve. The all-sign index still has
417 unique rows, null semantic/phonetic values and 33 verified source hashes.
The manifest is refreshed after this entry and checked against every recorded
file. The goal remains active; the result is qualified external-context and
graphic evidence, not a decipherment.

## 2026-09-28 — renewed external-anchor discovery and Umma image recovery

**Question and scope.** After the local graphic/specificity phase, sought an
independent object-to-known-referent bridge: named person, measured count or
contents, or parallel known-language text. Three parallel agents and parent
ran four bounded five-query searches, followed by a three-query residue-paper
follow-up. Exact queries, discoveries and access errors are preserved in each
branch's raw web-tool captures and review. These23 targeted queries are not an
exhaustive literature or museum survey. No outreach or request submission.

**Official Chanhudaro records.** Five queries found no public individual card
or independent accession-linked page for the five target objects. The original
CISI1 key p366/PDF402 clarifies that HU means Helsinki photographic provenance,
not a holding museum or accession. Penn L-141-177 is a non-target public record
with field3051 and2558 plus MFA36.0967; both numbers are retained without merging
the excavation objects. Penn direct1064 finding-aid link returned a cache miss,
Possehl finding aid timed out. The earlier located physical archive remains a
valid locator, not inspected fieldcard content.

**New-publication screen.** Five searches found no qualifying new Indus anchor.
Rakhigarhi RGR3's specific S40W10 seal is expressly uninscribed in the recovered
report text. Bahaj item14 has a secure locus but is Brahmi–Kharoshthi. A recently
indexed ASI download proved to be2015 Kalibangan; its bytes equal a retained
older acquisition, so it contributes no new independent evidence. Both copies
and acquisition provenance are kept. Publisher residue page403, Rakhigarhi PDF
cache miss, oversized ASI web-open failure and PDF font warnings are logged in
the branch review; author text and streaming ASI download supplied usable
alternatives. Interpretation-only papers were not counted as new anchors.

**Weight/instrument screen.** Five queries yielded HARP H2000-4496/9880-01 with
identity and single-view photograph but no authenticated inscription/mass pair.
BM120228/1883,1116.1's indexed official record lists8g and an Indus inscription,
but identifies a broken stamp-seal; mass of a seal is not calibration of an
encoded quantity. Direct BM page403 limits primary photograph inspection.
Existing Susa, Dilmun, tool and capacity cases were read and not counted anew.
Raw corpus object-type counts are retained by the new audit; no explicit WEIGHT
label is a catalogue fact, not proof there are no inscribed weights.

**Umma: successful changed access.** Five renewed searches located an indexed
Slovak library holding, ISBN978-80-89704-05-7, callV.237993, with a scan-request
service. Direct catalogue opening returned Internal Error; no request was sent.
A Geneva result is a6July2019 conference programme, not the object report.
Duplicate June2026 Reddit claims are not independent corroboration. The public
Harappa review page now opened and its actual linked figure downloaded HTTP200:
144018bytes, SHA2565a44511b714c5c6d1c1301a3cd925749e5ae2aa5b4da08bcaad163a0e90918c0.
Earlier403 attempts remain in the record. CaptionD points to SAHI p59Fig6.61;
E is older Ashmolean and is not a second view ofD. Parent and independent agent
visually inspectedD. A native162×151crop is saved without transformations.
An oval enclosing strokes and a U-like form are relatively clear, left traces
and the lower figural field are damaged/unclear. Exact field ID, seal versus
impression, script direction, material and full sequence remain unauthenticated.
No rotation, mirroring, restoration or numerical sign transcription was assigned.
The old frozen audit is unchanged; the new layer explicitly updates only its
prior image-access gap. A transient read used a wrong crop-manifest filename;
the actual umma_reproduced_crop_manifest.json was then read and verified.

**Kotada Bhadli targeted continuation.** Three additional searches recovered
an author's full-text extraction and institutional publication record. Online
2November2024, issueDecember2024; excavated2011–12 and selected11 of59 earlier
screened sherds. Table1 gives KB48,61,69,106,136,154,156,167,171,215,225. Figure2
caption identifies61/154; pixels and supplements remain uninspected. No
inscription-to-sample link is documented in inspected methods/table/captions.
These are laboratory/publication IDs without a field-register crosswalk. The
word seal in the methods refers to calcite, not an inscribed sealing. Author
PDF link Internal Error; direct author HTML403 retained with headers, no retry
or bypass. This reduces an earlier full-text gap without declaring sherds
uninscribed. Protein food attribution is insecure; lipid measurement alone
cannot assign a sign's referent.

**Persistence and correction.** Registered23 new raw artifacts together in
data/raw, bringing the registry to445. Saved branch reports/structured ledgers,
Umma crop/persistence scripts, integration and offline audit. The first combined
audit correctly failed because the agent had pinned README before parent added
the new navigation link. Reconstructed the exact old README bytes by removing
that single link, verified the original digest, and saved a historical snapshot.
The frozen review pin stays unchanged; the audit explicitly records its snapshot
resolution instead of silently repinning. The corrected audit verifies61
distinct evidence pins, one exact native crop and eleven sample IDs. All417
semantic and phonetic values remain null. Full pipeline validation follows.

Final validation: the complete offline pipeline exited0; all229 tests pass.
All445 registered raw artifacts retain their recorded sizes and SHA256 values;
1259 local Markdown links resolve. The all-sign index still contains417 unique
entries, null semantic/phonetic values and33 verified source hashes. The new
phase audit verifies61 distinct evidence pins (including the explicitly resolved
historical README snapshot), one native pixel-exact crop and eleven residue
sample IDs. Prior graphic/specificity and archaeological sensitivity audits also
pass unchanged. The final manifest is refreshed after this entry and verified
against every recorded file. No decipherment or new external meaning anchor is
claimed; the research goal remains active.

## 2026-09-28 — conditional calibration proof and original residue supplements

**Prior-turn classification: progress.** The previous turn recovered a new Umma
image, eleven residue sample IDs and an independently checked evidence layer.
This turn read the current authoritative gap review and branch reports before
continuing. Three parallel agents examined new public source routes and the
full-inventory inference problem; parent developed an exact calibration test.
No semantic key was accepted merely because it fit internal distributions.

**Exact new result.** The existing conditional numeral solutions (10,8,6) and
(36,20,4) predict totals A/B of36/61 and112/145. One positive measured quantity
can fit either through an arbitrary positive unit; two commensurate represented
quantities have distinct unit-free B/A ratios61/36 and145/112. Exact error
intervals are disjoint iff403e²−6026e+403>0 for0≤e<1. The critical per-object
error is approximately6.71786805%;5% intervals are disjoint,10% overlap. This
is a prospective mathematical distinction, not a measured calibration or proof
that the proposed field equalities/units are ancient facts. A common unit,
physical referent, sign identities and error bounds still need independent
support. Independent per-object units destroy the distinction. A measurement
may reject both candidates. No claim extends these values to417 signs.

Saved analyze_numeral_calibration_design.py, exact results and five meaningful
feasibility tests: one-point scale ambiguity, proportional candidates, exact
touching boundary, selection/rejection by synthetic observations, invalid inputs.
All five pass. An independent agent imported no producer code, derived totals
from the other equation sides, enumerated four error-corner cases, checked the
integer polynomial and high-precision root, and found zero mismatches. The
all-inventory review preserves28 pins and explicitly rejects a universal
number-of-anchors claim: model restrictions, positivity and integrality matter.
It finds no newly supported historical calibration experiment in current cases;
zero secured deposit strata also still prevent the declared replicated context
test. Null sign fields are an evidence state, not proof of inherent impossibility.

**Umma original-entry search.** Four new exact queries found an official museum
annual-report citation naming the chapter authors and pp54–61, but no p59 object
entry. The Geneva/GoogleBooks/other institutional leads did not yield a primary
object page, material or exact field ID. A draft called GoogleBooks a new record;
parent caught that it was already indexed in the prior capture. Revised the new
review to distinguish first direct inspection from prior discovery, preserving
that capture as an additional pin. Seven pins verify. No old frozen review was
rewritten, no scan request/outreach was sent, and prior denied download routes
were not repeated. Partial or secondary evidence was not promoted to original
report authentication.

**Kotada original publisher source recovery.** Four targeted queries did not
recover2024Figure2 or the2019thesis. Following the explicitly cited2020 paper's
exposed publisher links recovered article HTML, Figure3 chromatograms, Figure4
vessel plate, original DOCX Supplement1 and Supplement2 isotope plot. Initial
sandbox DNS failure had no body; authorized ordinary fetch succeeded. Web-click
cache/internal errors are preserved. The previously blocked2024publisher/author
routes were not revisited or bypassed. Twelve new raw artifacts were retained,
including headers and exact web captures, alongside the Umma capture.

Parent and agent inspected Figure4: six target labels appear as reconstructed
profiles, and KB225 has two small photographic views. KB173 photographs are
outside the eleven-sample cohort. No definite script is identifiable at native
resolution; this is not whole-shard/vessel absence. Profile hatching, painted
bands and modern labels are not sign transcriptions. Two unaltered native crops
were saved and checked pixel-for-pixel. Parent corrected the new report's plate
height typo411to410 to match decoded image and crop metadata; no data changed.

DOCX extraction preserves original XML table rows/cells, not inferred rendered
page addresses. The two tables have61/23rows including headers. Ten of the
2024eleven exact labels occur; KB61 does not, while KB60 occurs separately.
Neither label was corrected or merged. KB106 has aquatic fat and isotope dashes
in S1, but dairy values−19.1/−24.9/−5.8 in S2; the published text/caption also
support an aquatic interpretation/exclusion from isotope analysis. The conflict
is retained unresolved. Exact label overlap plus cited cohort continuity is not
an independent physical-object or field-register crosswalk. Parent's separate
zip/XML extraction reproduces all ten matches, KB61 absence and KB106 conflict.
No inscription-to-residue anchor follows from these tables or limited photos.

**Persistence.** Thirteen new raw artifacts were registered, taking the registry
to458. All downloads/captures remain together in data/raw. New reports, exact
proof, synthetic tests, independent review, source integration, XML extraction
and combined audit are saved. The combined audit verifies59 distinct pins, two
native crops, four independent calibration error cases and ten sample-label
matches. Preliminary reads of not-yet-written or wrongly named review files
returned missing-file errors; completed named artifacts were subsequently read.
All417 meanings/sounds remain null. Full pipeline validation follows.

Final validation: the full offline pipeline exited0. All234 tests pass, including
five new calibration feasibility tests. Independent calculation verifies four
exact error cases and the critical root with zero mismatches; the phase audit
checks59 evidence pins and two pixel-exact crops. All458 registered raw files
retain their byte counts/hashes,1273local Markdown links resolve, and the
417-entry index retains null semantic/phonetic values with33 source hashes
verified. The source findings and exact calibration design are preserved; no
new authenticated represented-quantity pair or reading is asserted. The final
manifest is refreshed after this entry and every recorded file is verified.
The decipherment goal remains active and unmet.

## 2026-09-28 — primary H-904 and cross-object numerical-value sensitivity

**Previous turn: progress.** The exact calibration design and new publisher
residue supplements changed the evidence and next action. This turn inspected
current numerical claims, source rows and old photograph audit before testing
whether the two-equation model's shared value had a defensible graphic basis.
Two agents reviewed primary objects locally; a third made four targeted public
source searches. Parent retained the full objective and did not turn a positive
local shape comparison into a translation or completion claim.

**H-904 primary recovery.** CISI2 printed338/PDF373 explicitly photographs
H-904 A/B; printed444/PDF479 identifies Finnish3477, excavation J213D, museum
field HM434,32.3018 and photoP1213. The primary key establishes Finnish rather
than Mahadevan numbering, HM Harappa Museum and the transferred-accession
convention. Secondary1786.1/.2 match the labelled whole-face patterns; their
raw `J213 (D)477` remains unchanged because the primary row does not authenticate
the appended477. H-904A visibly has two tall strokes and two shorter strokes;
B has three tall strokes and a curved mark with other residual signs. This
confirms a physical example of the screened pattern, not the author figure's
ID3786 identity or an equality of represented quantities.

Uppercase M-331B was compared with uppercase H-904B, using the catalogue's
object/impression convention. Lowercase M-331b reverses curve and stroke order
and was not mistaken for a graphic distinction. The H-904 mark is more angular,
M-331 smoother, but both are single open-left/right-bulging arcs in the object
views. Broad local graphic compatibility is positively supported; fine terminal
topology, complete allography and equal values are not. Parent independently
viewed face and metadata crops. P154 provides a W900/M287 candidate family but
no W899 entry, so no global alias or forced M-331 M287 assignment was added.
OCR failed to find H904/J213; the adjacent known H886–898 page bounded the
successful visual search. Three new uniquely prefixed pages and three native
crops are retained, with no image transformations or downloads.

**H-1923 remains secondary-only.** Original contents/title images establish
CISI1 rangeH1–264,278–382 (1987) and CISI2H266–275,356*,383–1019 (1991).
Secondary H94-2217/Fig28.01 therefore lies outside retained catalogue ranges;
its two-versus-two marks and marker forms were not independently counted.
Local OCR nulls were qualified because two extraction files contain only page
separators. Initial blank leaves and subsequent exact contents/title renders
are retained. The earlier H1817 lead concerns H94-2326/Fig26.06, a different
object; its identities were not transferred. The retained Kenoyer2010 capture
bibliographically cites Harappa Excavations1994 dated30August1994, but actual
report bytes/Fig28.01 are not present. Neither the older1986–90 report listing
nor a failed1997PDF retrieval is the1994report. Primary identity, counts,
orientation and damage stay null. Two exact coverage crops and28pins saved.

**Fuls source search.** Four exact queries located a distinct author deposit
373522958 uploaded31August2023. Indexed text explicitly uses source sign900 in
both ID3786 and M-331 arguments, preserving the proposal's intended shared
variable. Extracted pagination begins15 while bibliography cites57–90; no
unverified offset applied. Figures16/18 remain unavailable. The newly exposed
figure11 image returned404 and download cache miss; the new deposit HTML and
author attachment62075458 both returned403. All received error bodies/headers
and toolcaptures are saved; no repeated denied route, guessed URL repair,
credentials or outreach. Six raw artifacts registered. Captured prose calls
three long strokesSign032, whereas localH904B usesW033 for three andA usesW032
for two. SourceSign14's M-331 referent is also unreconciled. These are literal
coding/text discrepancies, not proof of renumbering or permission to correct
values. Figure pixels or a signary bridge are still required.

**Exact sensitivity result.** Removing only the shared-v constraint gives
3L+vA=2L+2S and vB*L+1=7S+5. Two infinite integer families satisfy even the
stronger digit bounds0<vA,vB<min(L,S),L>=10,S>=8:
(7t+1,4t,t−1,4) for t>=2; (7t+3,6t+2,5t+1,6) for t>=1.
Both polynomial residuals vanish identically, all affine bound margins are
nonnegative/nondecreasing, and L strictly increases. Shared-value intersections
are uniquelyt5→(36,20,4,4) andt1→(10,8,6,6). These are not exhaustive split-value
solutions or proposed ancient keys. The positive local shape comparison makes
shared-form interpretation plausible; it does not prove a constant numerical
value. The author's intended shared model is accurately represented. The earlier
two-candidate ratio/error proof remains valid within that model, not the larger
relaxed class. This identifies a necessary assumption rather than disproving it.

Saved exact coefficient certificates, producer, three new unit tests and
independent review. Independent checking imports no producer and verifies both
symbolic identities, eight bounds per family, unique intersections, saved
examples and source hashes with zero mismatches. The combined audit currently
verifies63 distinct evidence pins and five native crops; no global code aliases
or meanings added. All464raw artifacts remain together in data/raw. Full
pipeline and final manifest validation follow; all417 meanings/sounds stay null.

Final validation: the full offline pipeline exited0 and all237 tests pass.
The new combined audit verifies63 distinct evidence pins, five pixel-exact
crops and both infinite-family certificates; the independent reviewer reports
zero algebra mismatches. All464raw source records retain correct sizes/hashes;
1285local Markdown links resolve. The sign index retains417 unique rows, null
semantic/phonetic values and33 verified source hashes. The H-904 primary
comparison strengthens a local graphic premise, not a reading; H-1923 remains
secondary-only and sourceFigures16/18 remain unseen. The manifest is refreshed
after this entry and checked against every recorded file. Goal active and unmet.

## 2026-09-28 — Convergence requested; primary class distinction resolves an overstrong inference

User requested faster convergence and fewer tokens. Stopped broad new searches and additional agent work after the finite ongoing audit. Saved `docs/CONVERGENCE.md` ranking quantity notation first as a partial candidate, formulaic positional structure as the strongest structural conclusion, and commodity-specific fish readings as weaker. No semantic or phonetic values assigned; no decipherment claimed.

- Primary review of H326/H924 confirms long versus stacked three-mark groups, with H924 clearer. H326's surface/notch limits retained. H924 primary excavation number is unknown; secondary3286 belongs to following H925(1). H326 primary1171 and photoHU564 explain concatenated-looking secondary1171564 without rewriting it.
- Initial photo locators CISI1PDF263 and CISI2PDF375 were non-target pages; corrected to262/374 and retained original attempts. Four native crops persisted. H925 remains unreviewed.
- Exact class/context graph:20 frozen candidate groups,6 eligible,5 pure-class equations. H904 mixed expression excluded only from this ratio graph. All5 inconsistent; omitting still-secondary H1923 gives a=c=1,b=3/2. Merging long/stacked makes it inconsistent again. Three balanced rows repeat one equation. This narrows the constant-conversion criticism; it is not evidence of numerical meaning or global fit. Independent exact Gaussian elimination agrees without producer imports.
- Four H1923 web queries found a1995 catalogue entry for a238-page combined1994/1995 report, not the target original figure. WIS-2217 radiocarbon hit rejected. No original photograph/identifier join, no outreach. Capture stored under data/raw and registered with hash.
- Independent route audit prioritizes completion of this finite audit and acquisition of specified Penn1064 cards/registers. Root log lookup failed then corrected to docs/RESEARCH_LOG.md. Its original log pin is preserved by exact historical snapshot results/research_route_audit_log_input.md; original agent review pins remain unchanged.
- Parent inspected the H924 native photograph crop. A shell wildcard search for a guessed evidence-index filename had no matches; it made no changes.
- Scripts, proofs, independent review and failed-search record retained. New audit added to run_all; targeted verification selected instead of rerunning unchanged broad analyses, in response to usage constraint.

Validation: 3 new graph tests passed; 52 evidence pins and 4 exact pixel crops verified; independent graph check had zero mismatches. All 465 registered raw artifacts verified. Two non-download files are documented by raw/README.md: that local README and extracted mayig_LICENSE. Initial blanket raw-registration assertion therefore failed and was narrowed explicitly. The first manifest verification found macOS changing tests/.DS_Store; manifest now excludes this OS metadata throughout. All417 index rows remain unique with null semantic/phonetic values. Broad pipeline not rerun; previous237-test run is the prior full baseline. Two optional guessed filenames were absent; actual index located via its producer.

## 2026-09-28 — First evidence-impasse continuation after convergence
Re-read convergence validation, independent audit and prioritized route review. Previous turn made progress by completing the finite primary audit; this continuation found no new historical constraint to execute the remaining quantity or production-domain tests. No further fits, downloads, assignments or outreach. Missing independently anchored records are the blocker, not computation. First consecutive impasse turn; full goal remains unmet and active.

Second consecutive evidence-impasse continuation: source-registry hash unchanged and raw directory has no new source files. No new user-provided evidence or outreach authorization. Same quantity/referent and deposit-record gap; no new fits or invented values. Goal remains active, unmet.

Third consecutive evidence-impasse continuation: registry and raw-file inventory unchanged. No independently anchored quantity/referent or additional deposit records supplied; no new authorization for archive outreach. Previous continuation produced no historical progress. Reviewed program remains at the same genuine evidential impasse. Blocked threshold met; requesting blocked goal status, not completion.
Goal tool confirmed blocked status. Research artifacts retained; no decipherment or completion claimed.

## 2026-10-10 — Resume, new excavation sources, then user-directed corpus pivot

Goal resumed after usage reset; prior blocked audit is historical. Two source agents pursued H1923 and a discriminating route. Eight H1923 searches recovered an original Ars Libri catalogue (different entry/page locators and two differing1994-report descriptions), not target photograph. Parent's initial two search responses were not captured; exact queries are recorded in oct10-chanhu-web-capture.json. Subsequent requests/responses are retained there and oct10-chanhu-web-followup.json. Penn direct openings again failed (timeout/403); no access bypass or outreach.

A new search of modern French-led Chanhudaro excavations found a previously unreviewed primary series. Acquired2017Clio dossier, fullDidier article fromauthorHALdeposit,2019–2022 and2023–2024 excavation posters and sevenHALrecords. InitialClio fetch failedsandboxDNS, approvednormalnetworkdownload succeeded. PerséeHTML200 exposedPDFlink; PDF403body retained. PublicauthorrepositoryPDF200 succeeded. Firstattempt atHTMLparsing lackedbs4; stdlibregex used. ClickingwebPDFicon returnediconPNG, notPDF, and was rejected as acquisition. The fullarticle is36PDFpages includingcovermetadata; printed969–1002 conflictswithHALcover947–980, bothretained.

Foursteatiteseals reported, threeillustrated inarticleFig10b; no automaticfour-objectphotographiccount. Cliofragment visuallymatches anarticlefragment; laterposterphotos stronglymatch twoarticleobjects, so laterpublicationdate isnotnewexcavationevidence. Nativeimages and sourcecontext reviewed; damaged/unclear forms are notabsences, tallU-likeforms are notpromotedtofish. See OCT10_CLIO_FRAGMENT_REVIEW, OCT10_DIDIER_SEAL_REVIEW and OCT10_POSTER_SEAL_ADDENDUM. Postersdocument independentbeadcounts but noinscription–quantityjoin: Trench6necklace119beads andmicrobeads mustnotbejoinedto laterTrench4seals. These sources reopen a specific moderncontext route withoutdeciphering anysign.

User then directed stopping artifact-by-artifact audits, committing repository, and choosing verifiedM77corpus orpreprint/outreach, withcomparativescripts as asideproject. Chose verifiedM77corpus asmaintrack and boundedproto-cuneiformcommodity-numeralcomparison alongsideit. Agentsinstructed tostopartifactreviewandfinalizeonlyexistingnotes. No semantic assignments orclaim ofcompleteddecipherment. User's other methodological suggestions (Koberalternations,inventorygrowth,chronology,animal/text) retained forcorpus-backed testing; not all are claimedneworcompleted.

## 2026-10-10 — Whole-page corpus, comparative numerals, independent critique and Git backup

Stopped artifact-by-artifact audits at user direction and chose consecutive-page M77 reconstruction. Initial local checkpoint0a808a2 preserved4066files. User then supplied the empty GitHub repository and requested upstream backup. Converted binary PDFs/images to Git LFS in the unpublished main history because the primary119MB M77 scan exceeds ordinary GitHub limits and binary evidence totals2.6GB. Preserved the original commit on local-pre-lfs-checkpoint. Migration initially exposed pointer files in the working tree; installed local LFS filters/hooks and restored all2083objects from the local store. No source-byte changes intended; source hashes checked afterward. Upload outcome is recorded below when verified.

Primary coverage audit:550 M328-selected/context lines plus9 disjoint keyed recovered lines, with several other selected witnesses; these are not a representative complete corpus. New batch is all29references/33rows on printed39/PDF50. A explicitly saw secondary candidate strings; B performed primary-only transcription after earlier exposure to five pilot references. Frozen reviews preserve these limits. The initial22agreements/11disagreements caused the new assembler to refuse publication as required. Ten image-based adjudications resolve disagreements;1026 position6 remains UNKNOWN with candidatesM347/M352. Released batch:180identified positions,72assigned types,one visible unknown,five loss spans of unknown positive length,nine source-doubtful positions. Complete row coverage is distinct from complete sign identification. Neither copied glyphs nor A/B agreement authenticate the ancient objects. Four multiline/multiside references are not collapsed into export rows;24of25single-line references match secondary strings,one remains uncertain. Native whole-row boxes, metadata inheritance, actualdirection and normalizedRTL serialization retained.

Proto-cuneiform/Proto-Elamite side comparison downloaded two Englund research PDFs, headers and web capture (all five artifacts registered). Visually checked primary numerical graphs. Exact enumeration across three specified proto-cuneiform systems:192orderedpairs,two2/3matches in ŠEfractions,none in selectedintegerS/B. This is not an inventory-wide probability or Indus sign mapping. Proto-Elamite account sums provide a method analogy, not imported values. The source arithmetic520+80+720+60=1380was checked without claiming independent tablet recollation. New sources total29registered artifacts for this phase including two external-model response envelopes; all downloaded bytes remain data/raw.

User requested occasional Claude Code/Fable/Opus second opinions. InstalledCLIhelp explicitly listsfable/opus aliases. Tools-disabled Opus call first failedsandboxauthentication; rawzero-tokenfailure retained. Original prompt had an algebra typo(a=2b), corrected to3a=2b before the successful outside-sandbox call; both prompts retained. Successful model metadata identifiesclaude-opus-5-5. Critique accepted: freeze count-independent eligibility, do not infer equal quantities from shared context, retain H1923 conflict, exclude previously inspected/duplicate objects from holdouts, distinguish M77 fidelity from object verification. Its universal claim about absence of totals and possible mold identity were not accepted as independently established facts. Full response and response-to-critique persisted. No fabricated readings or outreach messages.

Queued corpus-dependent designs: Kober-style joint ending alternations with matched nulls; Good–Turing/Chao and controlled growth comparisons; independently sourced Early/Mature/Late Harappan phases and region; animal/text association controlling site,phase and duplicates. These are not completed analyses. Main next step is consecutivePDF51 onward, not another isolated artifact hunt. All417 semantic/phonetic assignments remain unresolved.

Validation for the new batch: all254unit tests passed; comparative exact graph check passed (3systems/192pairs/2matches); all494registered raw artifacts verified against both byte counts and SHA256 after LFS hydration, zero mismatches. Broad historical analysis pipeline was not rerun. New whole-page assembler and its14tests cover the changed workflow. Run manifest is a current file snapshot with this explicit validation scope, not a claim that every historical analysis was executed today.

GitHub backup succeeded to https://github.com/chinmaymk/indus-script.git, main. Initial LFS migration commit25a63055b0deac10e10acd01659b796cd207b67c uploaded2058unique LFS objects (2.6GB);2083tracked binary paths include repeated content. Corpus/Claude follow-up223069e24e406745d1998b375431295f8c4f4d7c uploaded27additional LFS objects (3.7MB). Both pushes exited0; git ls-remote independently returned223069e24e406745d1998b375431295f8c4f4d7c for refs/heads/main. This final log/manifest update is committed afterward. The original non-LFS checkpoint remains locally recoverable on local-pre-lfs-checkpoint and is not pushed. Source PDFs and all research evidence are retained upstream through LFS, with clone instructions inREADME. Goal remains active and unresolved.

## 2026-10-10 — Goal continuation: second full page and inventory estimators

Previous goal turn classified as progress: committed/pushed source evidence, completed first full-page corpus and external critique. Current authoritative HEAD at start b2d1c5c. Continued user-chosen corpus track rather than restarting artifact audits. Parent visually inventoried printed40/PDF51 as32references1031–1061+1065,33rows including1052's second line. A reviewed with declared secondary exposure; B used primary page/sign list without alternative page51 strings during entry. Both froze before comparison.

Assembler initially rejected B1051UNKNOWNbecause1/1length bounds were absent. B saved a schema-only amended submission pinning the original; glyphs and original bytes were unchanged. Next comparison refused publication with five new disputed rows. Source-image adjudication resolved1033right-tip prongs,1041RTLorder,1045triangular head,1047bow lower branch and1051bifurcated foot/roofed trident. The K-like glyph at1047position1 remainsUNKNOWN{M054,M055}; earlier1026unknown retained. Parent's first intendedM402crop actually showedM403; retained with explanatory filename and correctedcrop. A's row boxes nearbottommayclipreferenceleftedge; fullsource/widebands/Bboxes retain it. Bfollow-up and all nativecrop hashes persisted. Release2 retains original one-page outputs and combines66rows/61refs/349assigned positions/110types,2visibleunknowns,9unknown-lengthloss spans,14source-doubtful positions. This is M77printfidelity only. No populationerrorrate orphysicalduplicate independenceclaimed.

Added user's inventory-size direction using already-audited completeprimaryTableI, not thepartialsequencecorpus. N13372,S417,f1=112,f2=47; basicChao1=550.4468,Good–Turingunseenmass=.00837571044. Rarefaction is finite-catalogue interpolation withoutreplacement; sourceequations visuallychecked. No new signvalue,classifier,confidenceinterval orhistoricalinventoryclaim. Exactsyntheticduplication makesbothunseenestimateszero while relativefrequenciesstayfixed: onlynon-scale-invariance demonstration, not empiricalduplicationbias. Droppingallsingletons is explicitlyanextremehypotheticalscenario,notcorrection. Positionalestimatesretainedseparately; type-labelpermutation preserves all summaries.

Source acquisition: first two discoveryqueryresponses notserialized (queriesretained); subsequentwebresponses captured inraw. Originalets.uvm.eduPDF failedhostnamecertificatevalidation andwebtimeout; noTLSbypass. Workingwww.uvm.edusource downloaded afteroneautomaticapprovalreviewtimeout beforecommandexecution; authorizedretry succeeded. JMLRprimarypaper downloaded normally. BothPDFs,headers,webcapture andFable response (six artifacts) registered alongsideexistingrawdata. Failuremetadataretained. Nooutsiderepositorysourcefolder.

Invoked tools-disabled ClaudeCode aliasfable, returnedmodelclaude-fable-5-1, withsavedself-containedmethodprompt. Arithmeticconfirmed; terminalrarefactionincrementidentity suggested andaddedasindependenttest. Adopteditscaution that syntheticdoublingisnotactualarchaeologicalevidence. Didnotadoptunverifiedclaims abouttypicalscriptinventoryranges orrealduplicatefrequencybias. Fullprompt/responsepreserved; noexternalmodeloutputtreatedashistoricalsource.

Firstchart rendergeneratedmanyfontconfigwarnings but producedviewablePNG. ReplacedunembeddedstandardfontswithbundledVeraTTF andsetReportLabinvariantmode; revisedPDF/PNGvisuallychecked,renderstderrpreserved. No chart confidenceband orchronologicalinterpretation. Numericaltests coverexhaustivesubsets,formulabranches,duplication,domainrejection,monotonicity,labellinginvarianceandthefullTableIterminalincrement. Newstudyresults andsourcehashespersisted. NextmaincorpuspagePDF52; cross-scriptinventorycomparisons,Koberalternations,phase/animalcontrolsremainincomplete. Deciphermentgoalactiveandunmet.

Release2 validation completed: all260tests passed; all500registered raw artifacts match byte counts andSHA256. Embedded-font chart rerender has empty stderr and was visuallychecked. Added an explicit estimand distinction:417is the closedM77codebook size; Chao1 concerns a hypothetical wider consistentlyclassified population, not extra entries in that fixedlist. Currentfullgoalnotachieved. Repositorybackupcommit follows.

## 2026-10-10 — GitHub backup checkpoint for the next page

Verified GitHub main at c97caec988413cb35fde3a8a71f190ab5ab2b320 before backing up the latest saved work. Both independent PDF52/printed41 review submissions are frozen, each covering31references and33rows. Verified all55 embedded source/crop SHA256 pins across the two submissions. Preserved their JSON, extraction metadata, primary renders and diagnostic crops in this checkpoint, with binary evidence stored through Git LFS. These are unadjudicated review submissions; release2 remains the latest verified corpus. Page52 comparison/adjudication and the proposed glyph-matching feasibility pilot are not completed. This checkpoint changes no decipherment claims and runs no new research analysis.

## 2026-10-10 — Goal continuation: third page and terminal-alternation screen

Previous turn is progress: GitHub backup07d9e8a was pushed, including41 new LFS objects; remote main independently matched local HEAD and working tree was clean. Continued user-selected whole-page corpus route. Parent rechecked full printed41/PDF52 coverage against the primary render:1066–1096,31references,33rows including1093's three lines. Both frozen reviews were schema-valid and had32 exact whole-row agreements. Initial assembler run correctly refused publication for1083 position2, A=M054/B=M055. Parent compared primary sign-list054/055 and native1083 pixels; B separately reconsidered its initial055. An interior short stroke cannot be securely separated from edge thickness/pixelation, so custom adjudication retains UNKNOWN{M054,M055}, one position without a source asterisk. Source-normalized RTL order is retained even on1093's symmetric middle line.

Release3 initially assembles99rows/92references,512identified positions/129assigned types,three visibleunknowns,12LOSS spans and20source-doubtful positions. Prior releases and frozen submissions are unchanged. A bounded check of the existing alternative scan is recorded below before finalizing the result. The contemplated glyph-matching pilot was deferred to prioritize corpus adjudication and the user's ending-alternation proposal; no OCR result or accuracy estimate is claimed. First parent crop command used system Python lackingPillow; rerun with the bundled Python succeeded. Nearest-neighbor enlargement was diagnostic only and adds no source information.

For historical-method context, two web queries sought Kober1946 and the institutional archive. Exact responses are retained in data/raw/kober-oct10-web-capture.json and registered. JSTOR499054 exposed only a page shell; the returned UC finding-aid PDF link gave404. No original method paper was acquired, and search snippets are not treated as methodological evidence. The new terminal-pattern computation is our explicitly defined precursor screen inspired by the user's suggestion, not a replication of Kober's full procedure.

The existing alternative scan resolved1083 asM054 M054 M342: both central ovals are empty. Authenticated alternatePDF53/printed41 and native crops were reviewed against primary054/055. A bounded follow-up on the two remaining corpus unknowns found1026position6=M347 (both terminals have three prongs) atalternatePDF51/printed39 and1047position1=M054 (empty oval) atalternatePDF52/printed40. Parent independently inspected all three glyph crops and sign-list exemplars. The final release3 therefore selects A atthese references, assigning515positions/129types, with zero additional visibleUNKNOWN glyphs. TwelveLOSS spans and20source-doubtful positions remain; the latter are included in515. Main-scan-only decisions, frozen reviews and releases1/2 are preserved. The alternative is the same printed edition, not independent ancient object evidence, and no blanket assumption about its accuracy was made.

Implemented the requested precursor terminal-alternation screen with exact nonempty prefixes and one-/two-sign terminal blocks, distinct-sequence support, row multiplicities and within-length atomic-ending permutations. Before examining results, fixed both block lengths,999replicates and seed20261010+k. Initial provisional corpus had74clean rows; after alternative-scan adjudication, reran unchanged parameters on final SHA30008fc9d59c2ae81faa23d0b8ab67dc64d8f4d302588a2190853944fc2031c4. Final76clean rows/75distinct sequences: one-sign split71eligible/71stems; two-sign split67eligible/64stems with3alternative-ending stems. Neither has an ending pair shared by two stems. Every shuffle also has zero four-cycles; this sparse/degenerate baseline is inconclusive, not evidence against morphology. Synthetic root/case and office/product constructions yield identical rectangles, showing why positive structure alone would not decide the language-versus-label question. Full Kober linked-ending/syllabic-grid analysis, word boundaries, phonetic values and meanings remain unestablished.

Review of the new screen added rejection of incomplete manifests and inconsistent token/segment input even after an earlier doubtful token. Eight new tests cover combinatorics, duplicate multiplicity, atomic blocks, slot/length marginals, deterministic shuffling, malformed input and counterexamples. All268unit tests passed; all501registered raw artifacts match byte counts/SHA256. New downloads/captures remain together in data/raw; no original Kober paper was obtained. The full historical analysis pipeline was not rerun. Final assembler checked all review/evidence pins and accepted99rows with no unadjudicated differences. Decipherment remains unresolved; next corpus work is printed42, using both existing scans where useful. This turn makes concrete corpus and methodological progress, not completion of the goal.

## 2026-10-10 — Goal continuation: fourth page and exact test-support proof

Previous turn is progress: release3, alternative-scan resolutions, ending screen and source evidence were committed and pushed as1a88bbe; remote matched local HEAD. Current turn continued the consecutive-page corpus track. Parent independently inventoried printed42/mainPDF53 as1097–1127 except1124, with second lines at1099/1101/1112, giving30references/33rows. Main and alternatePDF54 both authenticate printed42. A disclosed secondary hints; B used primary scans/codebook/sign list without A/secondary/pilot readings during entry and reported no remembered specific page53 reading. Both froze and passed validate_review before comparison. All33 rows agree exactly; no new adjudication was required. Initial build succeeded normally, unlike prior disagreement-rejection runs. Direction2 at1101line2 remains metadata, not a reason to reverse normalized RTL text.

Release4 totals122references/132lines,672assigned positions including24source-doubtful positions,148assigned types,15unknown-lengthLOSS spans,zero additional visibleUNKNOWN glyphs. All132rows are objecttype1; field-symbol counts129code01/2code35/1code00. This is3.69% of printed lines and is not representative or object-photograph verification. Old releases and frozen review bytes remain unchanged. The next source page is printed43/mainPDF54; both existing scans should be used when useful.

At the user's request for occasional ClaudeCode opinions, ran tools-disabled Opus on a saved methodological summary; returned modelclaude-opus-5-5. The first prompt erroneously said all99release3rows were field01 even though the immediately computed profile was96code01/2code35/1code00. Preserved the erroneous prompt/response, then reran a corrected independent prompt. Both response envelopes are in data/raw and registered as AI opinions, not historical evidence. Accepted the warning that fixed whole-line prefixes and preserved slot counts can make the ending statistic structurally impossible. Did not accept newly transcribed pages as automatically untouched holdouts, nor null-event probability as statistical power, nor a proposed preference-injection model as evidence against every dependence alternative. Page53 was already being transcribed; no retrospective preregistration or confirmatory claim was made.

Parent independently derived an exact support criterion before reading the first completed critique: two distinct stems each need at least two slots, plus two ending blocks with two copies each in a shared length stratum or one copy each in two different strata. A separate agent implemented the certificate and sufficiency construction, with five tests including exhaustive enumeration of all allowed permutations across1458 small input cases. The proof relies on allowing shuffled collisions, exactly as the existing null does. Individually feasible rectangle counts are neither a simultaneous maximum nor a probability.

Bothrelease3 and4 have exact zero support for k1/k2 and row/deduplicated-sequence bases. Release4 leaves104cleanrows/103distinct; k1 has98eligible slots but only one repeated stem; k2 has92slots and three repeated stems, but the relevant length3/4 strata have no common ending block and length4 has no repeated ending block. No Monte Carlo rerun onrelease4: every allowed shuffle is already proven to scorezero. This refines the earlier sampled-zero interpretation and gives a stopping rule: skip further shuffles until the same fixed criterion finds support. Positive support would only establish possibility, not power or grammar. No phonetic/semantic assignments follow.

Validation: all273unit tests passed; all503registered raw artifacts match byte counts andSHA256. Release4 assembler verifies all source/review/decision pins and132row coverage; both exact-support outputs match their corpus/script pins. Full historical analysis pipeline not rerun. The bounded proof and corpus work advance the task without claiming decipherment or completion. Research outputs and source opinions are preserved for the next backup commit.


## 2026-10-10 — Compact working context, release 5 and faster-route design

Previous batch was pushed as ebe9a50 and verified upstream. Completed two pages
already underway before the user's faster-route steering: printed 43–44/main
PDF 54–55/alternate 55–56, 63 references and 66 rows. Both frozen reviews agree
on all new rows; no new adjudication. Release 5 totals 185 references/198 lines,
949 assigned positions/173 types, 23 unknown-length LOSS spans and 35 source-doubt
positions; zero additional visible UNKNOWN. Review exposure limits remain explicit.
Source renders, reviews, decisions and comparison are retained. This checks print
fidelity, not ancient readings.

Primary field-code review distinguishes lines, sides and objects: 01 unicorn,
35 uncertain animal, 00 absent motif on that side, 99 damage. Table V associates
across object sides and has unresolved repeated-sign counting semantics, so its
aggregates cannot be casually subtracted or treated as independent replication.
One render was requested before its producer completed; the completed image was
subsequently verified. Release 5 metadata: 186 represented sides, field-code line
counts 193/4/1 for 01/35/00. The exact ending certificate now permits 33 individually
feasible two-sign rectangles but observes zero; one-sign support remains impossible.
No new ending Monte Carlo run or grammar conclusion.

User requested collaboration with Claude on a faster route and explicitly warned
that accumulated context causes repeated work. Added root AGENTS.md, replacing
ACTIVE_STATE.md and a targeted RESEARCH_INDEX.md; condensed README and retained its
old contents under docs/archive (relative links rebased). Agents should read current
state first, retrieve only relevant evidence, and retain one next action/stop rule.
Full history and frozen evidence remain available, without entering every loop.

Restricted read-only Claude Opus repository review succeeded (claude-opus-5-5).
It recommended text–motif association using the existing export ahead of further
transcription. Accepted as prioritization only; rejected semantic/name-versus-office
claims and blind-holdout/independent-Table-V framing. Fable follow-up failed with
zero-token 429 credits_required; raw failure retained, no retry loop. Both captures
registered in data/raw alongside all previous downloads.

Frozen motif protocol v1, then v2 before any new joint counts. Independent review
confirmed the fractional-vector permutation variance, but found unspecified
transfer cutoff and quality filtering; v2 fixes Holm .05, full-group validation
before all-row Good/Fair filtering, and forbids sensitivity rescue. SEAL:S means
only the exact export code. Equal-weight exact text families, whole motif-vector
shuffles within exact length, native sign presence, global maxT, maximum five
frozen candidates, disjoint exact-text site transfer, 9,999 replicates per phase.
Absolute 1e-12 Z tie tolerance fixed before counts. No proposed translation fields
imported. Marginal feasibility audit found 934 standard-strict labelled rows/923
keys in the two-site exact-type subset; actual protocol also permits specified
NR singletons and excludes whole invalid groups, so these are not final sample counts.

Pre-run validation: all 291 unit tests passed, including 15 synthetic motif tests
and three new metadata tests. All 505 registered raw artifacts match byte counts
and SHA256. Prior broad analysis pipeline not rerun. No new sign–motif results have
been inspected at this checkpoint. Further corpus expansion remains deferred.


Before the first real association run, independent code review found a floating-point
edge case: identical fractional motif vectors could acquire tiny positive variance
from mean rounding and enter maxT incorrectly. The synthetic 1/3, 2/3 example
reproduced it. Fixing constant-column centering and adding regression tests precedes
any real results; checkpoint c46a188 preserves the earlier implementation. This is
a numerical correction to the fixed statistic, not an outcome-driven protocol change.


First discovery invocation stopped before calculating any associations: the CSV
reader rejected omitted trailing optional columns on row 2. Inspection of field
counts showed all 5,680 rows contain every whitelisted field through text, while
unselected trailing interpretation fields are variably omitted (35–38 columns).
Adjusted ingestion to require all selected fields and reject excess fields, allowing
only an omitted unselected suffix; added a synthetic regression. No source values,
protocol selection rules or outcomes changed. The failed run produced no result files.


Successful frozen v2 discovery: 716 Mohenjo-daro sequence families, 748 eligible
sign–raw-motif pairs, 9,999 permutations. Maximum Z=3.8298601929646137,
global maxT p=.7609; zero candidates at fixed .01 threshold. Empty candidate file
saved and hashed before any transfer. Per stop rule, no transfer, quality sensitivity,
primary pair checks or altered-feature search followed. Largest Z W455/Rhin is not
promoted to a reading or lead. The result is not a language/name/function conclusion
and has no global power claim. All 294 final unit tests pass (18 motif, three metadata);
505 registered raw artifacts verify. No historical broad pipeline rerun. Context
now records this as closed, preventing repeated rediscovery. Semantic/phonetic
assignments remain entirely unresolved; no outreach sent.


## 2026-10-11 — Concrete Penn archive request, awaiting send authorization

Previous goal turn classified as progress: frozen motif screen closed with no
selected candidates, compact context established, and backup 085b7de verified.
Followed ACTIVE_STATE's one action instead of restarting historical audits.
Prepared a reviewable email and 15-record target appendix for Penn collection 1064.
All identifiers and candidate boxes are unchanged from the existing target ledger;
five initial records follow the existing route audit, with ten further availability
checks retaining conflicts and incomplete cases. Box ranges do not authenticate
individual cards. Requested linked register/context pages and an inventory for
comparison groups, availability and fee information before paid work. No invented
sender affiliation, no decipherment claim, no scan purchase or publication request.

One bounded web call opened the known finding aid and official archive contact page.
The finding aid timed out; retained finding-aid evidence remains the basis for boxes.
The live archive page lists archives@pennmuseum.org. Full returned response, including
the timeout, is saved in data/raw/penn-request-oct10-contact-web-capture.json (the
filename reflects turn start before the date rollover) and registered. No broad
search or new card content. Registry now contains 506 raw artifacts; the newly added
one matches bytes/SHA256, with the previous 505 checked in the preceding batch.

Packet validation checks all seven input/draft hashes and equality to the unchanged
15-target set; result saved. No source-processing code changed or historical tests
rerun. Explicit authorization to send was requested only after the concrete packet
was ready, because developer communication rules require explicit permission to
message outside recipients. No message sent and no sender account selected. This is
the first prepared-packet authorization handoff, not a completed decipherment or a
blocked-goal declaration. Current state now points to the existing packet and pending
approval so a continuation does not recreate it. Cards alone would not establish
replication, quantities or semantic values; the original full goal remains active.


## 2026-10-11 — Repeated dependency verified; goal marked blocked

The request-preparation turn made progress and ended with the first authorization
handoff. The next automatic continuation revalidated the same missing authorization
and source material; it made no research progress and was not a verified live wait.
The third consecutive goal turn again found clean HEAD 988c11c, prepared-not-sent
packet, matching pins, no sender account/authorization and no new raw files. No human
approval appeared between these turns; automatic continuation is not send permission.
The finite local motif route is closed and the reviewed acquisition route needs
external records. No new source or defect justifies reopening completed audits.

Called update_goal(status=blocked); the tool returned blocked. This is an impasse
in the present evidence program, not proof that decipherment is impossible, and the
full original objective remains unmet. No message sent, no payment, no new claimed
sign values. Resume on explicit send approval or supplied relevant records; do not
recreate the packet or re-run old results as a substitute for the missing evidence.
This status persistence is administrative, not scientific progress.


## 2026-10-11 — User declined email outreach

User answered the pending request: “no do not send any emails.” No email had been
sent. Recorded the persistent prohibition in AGENTS.md and replaced the pending
approval instructions in ACTIVE_STATE. The Penn draft and target appendix are
retained as historical research records; they are not a queue to send. Do not ask
for email permission again unless the user explicitly changes the instruction,
and do not route the same outreach through another channel. This reply does not
supply new archaeological evidence or a decipherment and does not authorize a new
research run. No code, raw sources, frozen packet bytes or scientific results changed.


## 2026-10-11 — Public-data resumption and paired-ending design

User explicitly resumed decipherment using public and retained data, no outreach,
lean context, prioritizing a route not already ruled out. No messages or outreach.
Read current state and targeted route/numeral/comparative/foreign-seal summaries;
no full-history ingestion. A bounded read-only agent confirmed exact-context
one-position substitution networks already exist, while the larger retained export
has not had the restricted two-sign ending-rectangle screen. Selected that route:
exact Mohenjo-daro SEAL:S, standard strict parser, whole-artifact validation,
unique complete sequences and nonempty exact stems. Both terminal positions must
differ, with shared ending alternatives on at least two stems. This targets repeated
attachment of intact blocks, not independent-coordinate coupling or a syllabic grid.

Two public discovery queries were captured together in data/raw and registered
(507 registered artifacts total). They exposed public repositories and decipherment
claims but no such claim or external dataset was imported. Existing corpus is enough
for the chosen bounded test; no broad artifact hunt. Claude follow-up was not retried
after the prior provider credits failure.

Protocol v1 frozen before new joint counts. Initial independent review confirmed
its support formula for a collision-permitting null. Parent code/design review then
identified selection incompatibility: deduplicating observed full sequences while
allowing null duplicates does not give the conditional null on unique text types.
Independent reviewer concurred and supplied a concrete counterexample showing that
the former exact maximum is merely an upper bound under uniqueness. Preserved v1;
v2 freezes independent per-length rejection sampling of uniform slot permutations
conditioned on no duplicate edges, 9,999 accepted draws per stratum and a fixed
1,000,000 proposal cap. A missed quota yields computationally_unavailable, no partial
p values or selection. MaxT includes pairs absent in the observed arrangement.
All revisions precede actual new corpus counts. Earlier impossibility proofs in the
larger null space remain valid for the restricted space; positive relaxed support
is not automatically positive simple-graph support. No semantic values assigned.


## 2026-10-11 — Blog draft for chinmay.ai

User requested a blog post about the decipherment attempt for chinmay.ai. Saved
`docs/blog/trying-to-decipher-the-indus-script-with-ai.md` (1,490 words), in the
author's first-person voice. Reviewed only the active state, evidence index and
selected corpus, identifiability, numeral, Claude-review and motif summaries.
The draft distinguishes printed transcription from object verification, internal
structure from semantics, conditional numeral algebra from authenticated equality,
and the frozen motif screen's empty selection from universal absence. It includes
public research links and primary/expert background sources. Verified via GitHub
that the linked research repository is public. No new research run, raw-source
download, outreach or website publication. Concurrent research files were left
in place; the editorial note does not replace the separate active research action.


## 2026-10-11 — Author corrected the blog premise

Author clarified that the project began as a test of whether Astra could decipher
the script autonomously. Astra struggled for roughly two weeks, after which the
author brought in Opus and Sol. Revised the title, opening, research framing,
collaboration section and ending of the existing blog draft around that sequence.
The experiment examples remain project-level findings; no unsupported per-model
attribution, continuous-runtime claim, exact start date or model comparison was
added. Scientific results and linked sources are unchanged. No research run or
website publication.

## 2026-10-11 — Close saved ending test; authenticate five context identities

Resumption inspected ACTIVE_STATE and Git before work. The handoff was stale:
ending v2 had already run and stopped. No process or real experiment was relaunched.
Independent read-only review verified all source/code/protocol pins, seven logical
output hashes and lossless compressed storage, and separately reproduced889
qualifying pairs from635 saved families, each on one preceding string.645 eligible
artifacts; maximum support1; zero candidates/draws; p values null.17 synthetic tests
pass. Closed precisely this predicate, not inflection, language or decipherment.
Saved result report and kept frozen data unchanged. Gzip binary uses Git LFS.

Inherited public metadata batch profiled709 Mackay records; strict normalized field
keys had zero Lipi overlaps. Seven metadata tests pass. Fixed the first five
nonmissing-CISI/field Mohenjo-daro records before primary inspection; read-only
critic confirmed scope. Retained CISI tables explicitly give M584→DK4807,
M1140→DK11340, M592→SD3225, M718→DK5644, M233→DK10799. Labels establish FC in
column2 and excavation number in column3. Appended Lipi values do not all mean the
same reference type; no global suffix parser or namespace merge was inferred.
Three specific fields match Mackay seal-table rows188/209/3. Inspected original
printed375/376/369 pixels: two different rooms with numeric depths and one surface
find. Printed369 separately authenticates SD3225’s narrative locus and depth;
not a seal-table row and not pooled with DK. DK4807 context pixels unresolved.
CISI caveat about possibly wrong excavation numbers retained; no new object
marking or original-use verification. Original strict zero-overlap profile preserved.

Two sandbox source fetches failed DNS without receiving bytes, including an initial
incorrect page-offset lead. Viewing retained printed363 rejected that offset;
chapter PDF45 corresponds to printed369. Authorized network retrieval succeeded
for leaves391/397, with bodies and headers registered by bytes/SHA256/provenance.
Leaf398 was already retained. Failure records remain. No outreach of any kind.
All318 tests then passed. Concurrent blog-chat commits were observed and preserved;
research work neither edited the blog nor reset its commits.

## 2026-10-11 — Frozen metadata locator feasibility; four-object next gate

After the five-record check completed, independently criticized and froze one new
source-based metadata locator rule: literal normalized Mackay field_no+no against
Lipi excavation-idno. The rule is exploratory and unvalidated beyond specific
checks. No sign/readings/translation columns or inferred phase labels enter it.
Reject missing keys, concatenation-boundary collisions, duplicated table fields,
ambiguous artifact keys, inconsistent artifact fields and sites. Repeated Lipi
rows are witnesses. Five adversarial tests pass. One frozen pass produced627
provisional locators from709 rows;82 exclusions.397 have all area/block/house/room
and finite raw depth;393 distinct tuples;4 repeated tuples, each with2 provisional
artifact keys. Complete candidate/exclusion/missing-field ledgers and source pins
retained. Matching numeric room/depth labels is only coverage, not shared deposit,
independence, contemporaneity, semantic interpretation or a significance result.

Next finite pilot fixed to four objects in the first two lexically ordered tuples:
M1178/M1190 and M1746/M1879. Require individual primary identity chains and actual
archaeological context/datum; absent retained CISI coverage stays unresolved, with
no target substitution. No primary pilot or sign analysis auto-launched in this
batch. Claude's previously recorded provider usage-credit failure was not retried;
read-only agent criticism supplied methodological checking, not new source facts.
No phonetic/semantic values established; overall decipherment remains unresolved.

Read-only post-run locator review accepted all counts, projected fields, keys,
witnesses and exclusion reasons against pinned sources. It identified a missing
imported-helper hash in the result; saved a separate audit manifest pinning that
helper and retained the original result unchanged. Four-object pilot identifiers,
field numbers, Mackay rows and input hash are explicitly frozen in a separate
protocol. Source registry verification passed for all522 registered artifacts.


## 2026-10-11 — Frozen token accounting for the blog

Author reported continuing across multiple usage resets and requested exact token
counts. Audited retained local usage metadata at the request timestamp,
2026-10-11T08:23:38.418Z. Selected the two research roots and descendants; excluded
blog/accounting and unrelated grammar chats. Research models total 821,734,966;
including separately attributed automatic review totals 838,914,762. Of the full
total, 810,960,583 are cached input reads and 3,258,652 output tokens including
reasoning. Counts are exact recorded sums, not proof of complete provider billing,
subscription allowance consumption, an exact reset count, or decipherment.

Saved metadata-only source capture in data/raw, registered bytes/SHA256/provenance,
and saved the tally, verification and reproducible script. No message contents,
credentials or account IDs were copied. Removed 17 repeated Claude message blocks.
All 117 nonempty OpenAI histories reconcile per-call and final record counters;
nine older cumulative displays differ and one malformed nonusage line is recorded.
Independent last-cumulative/Claude/envelope sums reproduce the full total; replay
reproduces the report and all 152 original source-prefix hashes verify. First
capture attempt stopped on the malformed nonusage line before saving any output;
parser now records that defect and refuses malformed usage records. Added resets
and a sourced breakdown to the blog, plus docs/RESEARCH_TOKEN_USAGE.md. No scientific
experiment, outreach or website publication. Concurrent research changes preserved.


## 2026-10-11 — Blog context on instructions and engineering discipline

Author requested more context on how the agents were directed, logging and
critiques. Retrieved only relevant log sections and selected human-authored
instructions from the original research rollout; automatic goal continuations
were excluded. Added the original goal prompt, the next-day request to log all
attempts and results, retrospective-log distinction, evidence/code persistence,
later approach critique and compact one-action/stop-rule workflow to the blog.
Expanded the model-collaboration section with the author's occasional-second-
opinion and faster-route requests. Preserved the autonomous-attempt framing,
scientific limits, frozen token counts and current no-outreach rule.

Four historical author prompts captured in data/raw and registered with bytes,
SHA256 and provenance. No model transcripts or full research history imported
into context or copied into the blog. No scientific run or website publication.
Concurrent research state retained; editorial handoff condensed in ACTIVE_STATE.


## 2026-10-11 — Rounded blog numbers and token headline

Author requested human-readable numbers and the token count in the headline,
allowing rounding up. Retitled the post to “840 million tokens trying to decipher
the Indus script.” Converted article token figures to millions/thousands and
simplified the table; roughly 822 million research-model tokens and about
840 million including automatic review. Cache/output distinction remains explicit.
Rounded the motif experiment's shuffle count and p value in prose, linking the
exact result. Frozen usage capture, exact audit, scientific outputs and cutoff
remain unchanged. No new research run or website publication.

## 2026-10-11 — Repository link at the top of the blog

At the author's request, added the public GitHub repository link as the first
line above the headline. No scientific run or website publication.

## 2026-10-11 — Shortened blog for narrative flow

Author requested a substantially shorter, more interesting post. Rebuilt the
draft around the autonomous Astra attempt, logging, the gap between patterns
and readings, a conditional numeral example, later Opus/Sol help, and the outcome.
Removed the usage table, equations, extended corpus details and repeated caveats;
retained rounded model counts, cache context and links to exact evidence.
Repository remains first and the 840 million token headline remains unchanged.
No scientific run or website publication.

## 2026-10-11 — Astra in the blog title

At the author's request, changed the headline to “Asking Astra to decipher the
Indus script: 840 million tokens later.” No scientific run or website publication.


## 2026-10-11 — Four-object context pilot and new Bagasra eligibility gate

User authorized continued exploration with another150m-token budget; active
persistent goal created. Public/retained sources only, no outreach. Four-object
pilot protocol stayed frozen. Parent visually checked CISI II printed438/PDF473
and Mackay printed386/leaf408: M1178→DK7448→FEM559 and M1190→DK7447→FEM558,
both block2/IV/20/−16.5ft. Separate catalogue records, no newly inspected original
markings or explicit shared event. Independent read-only reviewer authenticated
CISI I/II coverage limits: later M1746/M1879 not covered; Mackay printed379/leaf401
pixels absent and OCR corrupt. Both remain unavailable, not disproven. No targets
replaced, sources acquired during pilot, signs scored or significance test.
Manual result script saved four records and13 verified source/output pins;
PUBLIC_CONTEXT_FOUR_OBJECT_PILOT.md records finite stop. OCR-only architecture
leads not promoted to primary pixel observations or use classification.

A bounded internal critic supplied a genuinely unreviewed source: Jamison et al.
2017, Heritage5:1–21, complete seven Bagasra seals. Four discovery queries are
reported in the separate review; original tool response objects were not retained,
so no reconstructed raw capture claimed. Parent repeated one publisher web-open
already timed out in critic's discovery; it also timed out and added no evidence.
Then one authorized direct fetch succeeded HTTP200,21-page PDF,3073754bytes,
SHA256643725ca6e60e99682a921ad2efb51cebcfc387f1658ad1ea0c5224f126517c1.
PDF/headers registered; new protocol froze all seven before acquisition. Rendered
and visually inspected context map7, appendix15 and narrative18. Map includes
seal photographs; no blinding or unseen-holdout claim and no sign transcription.

BSR6719 has Eo11 in map versus El15 in appendix,66cm in both, layer unavailable.
Other six metadata rows agree. BSR7197 probable secondary; BSR7368 sealed gateway
pit without established craft use; BSR2037/8288 near faience/lithic activity but
use relationship explicitly uncertain. Shell/craft observations exist, but no
secured replicated original-use bead versus shell/faience contrast with comparable
phase/recovery. Bhan2005 directly cited primary Antiquity report captured and
registered; six-seal count retained separately from later seven. Exact Sonawane2003
search found request-only original listing; no report acquired/request sent.
Captured search registered. Incidentally located primary black-slipped-jar paper
is a future eligibility lead only, outside this seven-object gate.

Finite stop: test unavailable, zero qualifying deposits under frozen gate. No
semantic rejection, p value, corpus amendment or assigned meaning. Independent
read-only reviewer reproduced metadata conflict and failure, nine evidence pins
verified. Source/output ledgers and bounded reports saved. Initial source-registry
append used nonexistent web_captures key and failed before write; correct existing
web_extraction_captures key then used. An atomic documentation patch failed on an
invalid expected line; corrected patch applied. Existing frozen files preserved.


**Related jar source: pre-experiment criticism.** One author-deposited Ajithprasad
paper opened, four within-source finds, actual52892byte tool capture preserved
and registered (SHA2563ec21ba73e3a561a2a2da5dfba7f976be35547ccbd2de433a629dae47e0c2ed1).
Journal headers2013, index2014, upload2019 kept distinct.210 sherds,12 rims,3 bases,
no complete Bagasra vessel; Table3 height/bodydiameter missing, contents unresolved
and residue attempts unsuccessful. No usable independent capacity-text calibration,
sign scoring, fits or acquired references. Specific result summary saved as
bagasra_jar_source_criticism.json; gate stopped without a new experiment.


**Kanmer source-discovery stop.** Two exact primary-source queries and official
bibliographic/RIHN page reads located2012 report, x+844pages/disc,
ISBN9784902325720, not an authenticated public body. Counts and context frame
remain unknown, not absent.76392byte actual tool capture registered with hash
5977e33451fb1196172e4372644d7bf1d3f300177a238399699fdad578b7195d.
No report/signs acquired or test. One specific unvisited News.html publication
link from official homepage becomes the next bounded source-pointer check; stop
onepage, no query/guessed endpoint extension. This link is newly documented
source evidence, rather than a rerun of the two closed discovery queries.
Research batch ea97805 pushed with5 LFS artifacts/4.5MB; local origin/main agrees.


**Kanmer one-page pointer stop.** Official News.html extraction supplied2009
announcements and photo/news links, not the2012 report body or field/context
register. Captured and registered; no linked photo/sign review or onward crawl.
Source eligibility remains unknown; do not repeat either the two queries or this
page without a specific changed public source. Separate source decision saved.
A specifically newly encountered2025 primary DOI10.1017/rdc.2024.119 is a possible
bounded next-source criticism, not evidence of inscription-associated chronology
or a semantic anchor. No old calibration/deposit model is reopened.


## 2026-10-11 — Bhagatrav single-source criticism

Previous goal turn classified progress: new primary Bagasra source inspected,
closed eligibility gates, conflicts preserved and completed batches backed up;
none was treated as decipherment. Current frozen Bhagatrav check used two exact
source attempts. Web DOI open inaccessible; direct preserved DOI HTTP succeeded200,
1188595bytes, SHA256ebdab4c803b678b7a20e6a46dab7c4d5c855e05cf436eed466bb679f6fe0f0e9,
resolved to Cambridge full article. HTML/headers and original failed tool capture
registered. No extra opens/references. Initial bs4 import unavailable before any
output; standard-library HTMLParser extracted76775 visible characters with
script/style/nav/header/footer excluded. Body context sections selectively read.

Primary Radiocarbon67(1),2025,53–73 dates archaeological materials and iconographic
horn-deity dish, not an identified inscription. No object/event register, known
contents, measured represented quantity or secure comparable original-use deposits.
Medieval lapidary and mixed layer3 cannot become Harappan comparison by pooling.
General Rojdi sherd reference lacks a field ID here. Independent read-only critic
agrees: no qualifying link in this article, not proof of site/region-wide absence.
Finite stop recorded in results/bhagatrav_source_criticism_v1/decision.json, with
five pins. No sign scoring, model, figure review, phonetic/semantic value or
chronological recalculation. Kanungo2021 iconographic pointer not followed and
not enough to reopen. Specific independently described Kuntasi industrial context
and1996 excavation report are a distinct external-context source pointer; inspect
availability/record scope before any new experiment, not generic artifact hunting.


**Kuntasi specific-source discovery.** Bounded independent critic completed two
exact queries/one institutional open. DeccanCollege record123456789/44865 lists
1996 report,x+383pages/PDF,accession132490 and explicit View Book/flipbook links.
Catalogue M.R.Raval differs from prior paper M.H.Raval; neither silently fixed.
Actual30468byte response capture registered with hash
420ba4dc00216fb6dacdd9a79e2f5bd45e1878d1ff27c02929e5c4eaf9db0fec.
No body or signs inspected and no field-level evidence claimed. This concrete
previously unfollowed body pointer meets the predeclared reopening condition,
so a separately frozen one-catalogue/one-linked-body context gate follows. Full
reported inscription/context frame, no replacement, no relaxed proximity rule,
no references or guessed endpoint extension. Authentication/denial ends acquisition.


**User priority change: Yajnadevam validation.** Institutional Kuntasi catalogue
HTTP200,56234bytes,hash1def396c2134dc999aee36624fd64e3f57d2b3cc1c798e07c11fd5ed6b84a6a9,
registered with headers. Explicit View Book/flipbook hrefs parsed without guessing;
body not fetched. User then requested validation of BharathRao/Yajnadevam.
Parked Kuntasi at this exact state under explicit priority change; frozen inputs
survive. New primary candidate-key audit takes precedence; no outreach. Initial
web search discovers author's ScriptDerivation/Lipi repositories and paper mirror.
Earlier retained Lipi corpus is from this author, but no prior named decipherment
assessment found in selective log search. Secondary critiques not adopted as facts.

## 2026-10-11 — Yajnadevam / Bharath Rao validation

User-prioritized candidate audit completed its finite stopping rule. Primary
99-page paper compiled13November2024 acquired from public RareBookSociety mirror,
741788bytes SHA25681c026b78a66a13d1bbc14d9c145bdd5ecabda0ada9b6d14a3ea206a1c68c599.
This is an inspected version, not a claim that no later revision exists. Public
GitHub branch/tree metadata confirm ScriptDerivation commit
5835e8b022106ed105e86c762fd64e1ec9875cce and Lipi commit
fc8813a52e183d19c441631dc26c33a4dccbea39. Lipi equals retained source commit;
existing inscriptions/xlits reused, not counted as independent evidence. All new
HTTP bodies/headers and actual discovery/open tool capture registered. Script,
dictionary preparation,32-group test corpus, auxiliary forms and decoding table
retained. Full dictionary preparation shell script not executed; no MW download.

Two bounded read-only reviewers independently criticized math and code. Paper
pp7–8 rendered and visually inspected: effective330/.7≈471 arithmetic does not
establish uniqueness for a particular corpus or full adjustable rule family.
Optional vowels, phonetic mergers, allograph/conjunct grouping, direction,
segmentation and lexicon augmentation require accounting. No alternative complete
decipherment was generated; rejection is of the asserted proof, not a conclusion
that every value is wrong. Method/conclusion inspected, no frozen withheld
artifact validation identified. Page25 separates intended meaning from its
grammatical accuracy criterion. Later mixed-script/Brahmi comparisons remain
unreplicated; not independently falsified by this bounded assessment.

Original prove.pl conditional substitution ignores an empty prior option set,
allowing subsequent row to restore fresh wildcard matches. Code audited before
execution: only reads dictionary/corpus and prints. Frozen protocol then used
unchanged original003 block and original program with toy dictionary and/ja/jja.
Exactly ONE original Perl invocation. Correct candidate cumulative sets:
{d},empty,empty,empty. Saved stdout ends003-d-bow: two-spaces = j. The original
program therefore returns a candidate inconsistent with earlier constraints.
This establishes unsound intersection semantics, not its incidence on the author's
Sanskrit dictionary or falsity of all proposed readings. Stored earlier values
are not automatically propagated and sign strings are displayed, not constraints.

Our initial driver had a whitespace-only output-observation defect: it expected
one space before = and reported bug_reproduced:false despite saved finalj.
Separate review verifies original pins and interprets existing stdout correctly;
initial result/driver/fixtures remain unchanged, no rerun. Independent reviewer
confirmed both the counterexample and correction. Exact saved output, protocol,
initial result and correcting layer survive for audit.

Specific Table2 overlaps with prior primary name audits reused without reopening
searches: P516366 Nanasa/Samar seal illegible, possible duplicate unresolved;
P525331 cuneiform interpreter seal without Indus counterpart. No independent
Indus/name pair follows. Other Table2 objects and all Table11 mixed-script
artifact identities/dates/readings not exhaustively authenticated; no broad
absence or blanket linguistic disproof claimed.

Decision: claimed validation fails; individual readings unresolved. No semantic
or phonetic key admitted, all417 fields/corpus frozen. No p-value, translation
replication, language sweep, outreach or decipherment announcement.43 source,
control/review/derived pins in decision; separate independent-review summary
preserves scope objections. Report docs/YAJNADEVAM_VALIDATION.md. Source acquisition
and controlled falsification are research progress, not decipherment. Candidate
assessment closes; resume already frozen Kuntasi linked-body gate at parked link,
without repeating its discovery. Claude credit failure has no changed evidence;
no unsupported provider retry or claimed new Claude review.
