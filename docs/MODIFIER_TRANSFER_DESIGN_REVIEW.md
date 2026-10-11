# Review of a recurring roof-mark test

This review recommends **cross-root rectangle coverage as the primary finite result**, with the proposed signed agreement score and its shuffle distribution treated as secondary diagnostics. A rectangle can establish a repeated contextual analogy in this export. It cannot establish a productive ancient modifier, identical contextual effects, or meaning. This is a design review made after earlier corpus exploration, before reading any new roof-screen outcomes; no corpus counts were recomputed here.

## What is new, and what has already been tested

The [family analysis](SIGN_FAMILIES.md) already found 63 exact one-position family/frame instances across 23 catalogue families and evaluated prediction of variants within known families. Its folds joined shared artifacts and family-collapsed identical strings into connected groups. That is an important precedent for avoiding near-duplicate leakage, but it did not test whether one graphic addition transfers across different base shapes.

The [composite expansion screen](COMPOSITE_EXPANSION_RESULTS.md) enumerated one-token versus two-token whole-frame substitutions, including generic alternatives. The [repetition screen](REPETITION_EXPANSION.md) compared repeated signs with stroke-plus-sign alternatives. Their concrete counterexamples show why occupying the same slot does not imply equivalent content. Repeating those searches with a new label would not answer the cross-base question.

The primary inventory analysis already compared M059/M065 positional profiles. It did not test transfer to other roots. The [composition method review](COMPOSITION_METHOD_REVIEW.md) records that M77 classification used distribution as well as shape, and sometimes regularized joined/separate writing. Consequently, recurrence in normalized M codes is partly dependent on modern editorial choices.

## Freeze the graphic hypothesis first

The prospective protocol currently proposes six pairs: M059/M065, M060/M066, M089/M092, M137/M138, M162/M163 and M333/M334. The first two belong to one fish root and must never count as evidence of transfer between different roots. Excluding M158/M159 because another stroke also changes is the right kind of shape-based restriction. Do not select or restore pairs because their context scores are favorable.

For every retained pair, preserve primary sign-list crops, a description of all changed strokes, uncertainty about attachment/placement, and an explicit root label. Similar roof outlines do not authenticate identity with standalone M134. Detached carets, enclosing arches, crossbars and caps should not be pooled merely because a verbal description calls them roofs. Primary object images are needed to show that the operation is ancient rather than a property of standardized drawings.

There are three separate claims:

1. A visually comparable addition recurs on different bases: a graphic claim.
2. Its presence has a comparable relationship to context across bases: a distributional claim.
3. The addition contributes the same sound or meaning: an interpretation requiring independent anchors.

Each later claim needs additional evidence. Even perfectly shared conditional distributions would not prove the third.

## A finite, falsifiable coverage algorithm

Use the existing strict native-M selection without repairs or new W/M joins. An eligible record has a single source document, right-to-left source direction, at least two tokens, and no doubtful reading or unknown span. These are source selection flags, not certification that the object is complete or the transcription correct.

For each occurrence of either member of each frozen pair:

1. Retain the source reference, full raw M sequence, target position, exact prefix and suffix, source object code and companion `site_label_unverified`.
2. Form an exact frame `L [target] R`, with at least one external token. Deduplicate state presence within pair/frame while preserving every supporting reference. Do not turn repeated tokens or duplicate strings into independent evidence.
3. In the primary descriptive stratum require equal site label, object code, field length and position. Mark missing-site strata explicitly as **unknown site**, not an authenticated shared locality. Full-frame unstratified results remain diagnostic.
4. Record each pair/frame state as plain only, roof only, or both. Retain every mixed frame, every absent frame and every pair with zero coverage. “Only” means observed only in this selected export; it is not an assertion of ancient prohibition.
5. For each pair of different roots, intersect their exact frames. An eligible rectangle consists of one shared plain/plain frame and a different shared roof/roof frame, in the same metadata/length/position stratum, with an injective assignment of four source references to its four cells.
6. Save all four witness sets and one deterministic injective assignment. Report failed assignments separately. Count eligible root-pair/stratum coverage and eligible rectangles; also provide a component-deduplicated summary after linking known shared artifacts/dies and overlapping witnesses. Unknown links remain unknown.

The principal question is whether **any eligible opposite-state rectangle exists**, and which independently reviewed roots and objects support it. The primary numerical summary should be the number of cross-root comparisons with eligible support, not the total number of overlapping rectangles. Overlapping rectangles are a witness catalogue, not independent replications. A zero result falsifies the narrow claim that this particular selected export supplies this particular exact analogy; it does not falsify graphic composition or all forms of productivity.

For a stronger productivity claim, require transfer across a third root and independent formula/object components. The current two-root rectangle screen is not a held-out prediction: it deliberately reuses shared frames. Do not describe its success as generalization to unseen contexts.

## Signed scores, generic substitutions and the proposed null

With `c = -1` for plain only, `+1` for roof only and `0` for both, the sum of products `c_i c_j` is transparent but insufficient alone. Both pairs can be mostly plain and achieve a positive score without any shared roof contrast. Always show plain concordance, roof concordance, discordance and mixed states separately. Frequent pairs have more opportunities to become mixed; zero is not a calibrated effect size or neutral archaeological observation.

The proposed per-pair mask shuffle, within site/type/length/position strata, preserves the observed frame-coverage graph and counts of the three masks. It **does not preserve per-state reference multiplicity, shared-object dependence, or formula-family dependence**. Its exchangeability premise must remain explicit. Its p-value concerns the signed score, not the number of eligible rectangles or the truth of a semantic operator.

Before interpreting a null distribution, report for each stratum its size and mask multiplicities, the exact number of distinct allocations `n! / product(n_state!)`, and whether movable positions touch a shared-frame comparison. All-identical masks, singleton strata or movement confined to unshared frames can leave the statistic constant. A degenerate null supplies no test. With only 499 seeded draws, the resolution is limited; additional simulation cannot cure a vacuous or historically unsupported null. A nondegenerate conditional result still is not an archaeological sampling p-value.

Two useful finite controls can be predeclared without claiming random sampling:

- **Orientation sensitivity:** reverse plain/roof labels for whole shape roots and enumerate every resulting orientation. Keep both fish pairs together. This shows whether the observed graphic orientation aligns better than arbitrary directions of pair contrasts; global reversal has the same score and is not an independent configuration.
- **Generic substitution controls:** enumerate a frozen set of alternative pairings among the selected endpoints, excluding shared endpoints, and apply the same frame/rectangle procedure. Preserve support, state marginals and comparable strata in reporting; do not call an unmatched rare alternative a fair negative control. If no comparable controls exist, report that limitation. These are descriptive controls unless an exchangeability model is separately defended.

Existing ordinary substitution witnesses already refute the rule “same slot implies same meaning.” A roof statistic must exceed that logical standard, not merely rediscover substitution.

## What a later prediction test would require

If coverage is sufficient, freeze a context-only classifier on other roots and test roof/plain prediction on a held-out root. The target code must never be a feature. Use a small fixed feature set, such as immediate neighbor M codes and boundaries, and a fixed smoothing rule. Compare against a metadata-only baseline using root-balanced conditional pairwise log loss between plain and roof occurrences within shared metadata strata; this avoids scoring success from the held-out root's unknown base frequency alone. Use deterministic matching of independent groups, not every possible pair of occurrences.

Training and testing must not share known artifacts/dies or whole texts made identical by collapsing the candidate target families. For this stricter test, collapse all target bases to a common placeholder when identifying potential formula leakage across roots. Remove or hold together the resulting connected components; do not split a giant component to improve fold balance. Require at least three eligible roots, both states and multiple independent groups per state in every held-out root, with all support gates fixed before outcomes. If those conditions fail, report **not estimable**. Positive performance would support a specified contextual regularity; failure would reject that prediction model, not every possible modifier.

This predictive extension is deliberately distinct from the finite rectangle screen. No model has been fitted or evaluated in this review.

## Can strict native M support site/type holdouts?

`data/processed/m77_candidate_strict.jsonl` has `source_object_code`, `source_doc_count`, `source_direction_code`, reference and sequence. It has no site field and no complete independently authenticated physical-object/die key.

`data/processed/m77_candidate_records.jsonl` supplies `site_label_unverified` through the same source-reference join. In `scripts/prepare_m77_candidate.py`, it is copied from the secondary source's `site_name`; it is not recovered from checked excavation metadata. The object code uses primary code definitions (for example 1 seal, 2 sealing, 3 miniature tablet), but applying the label to every record is still conditional on the secondary transcription.

Therefore a **source-labelled object-type holdout is technically possible**, subject to unmeasured support and object linkage. A **secondary-site sensitivity split is technically possible** after an exact reference join, preserving null values. An authenticated archaeological site holdout is not currently supported by this schema alone. Combining site/type/length/position can make every cross-state comparison disappear; that is a coverage limit, not justification to loosen matching after observing the result. Aggregate primary site counts cannot reconstruct the missing joint inscription-level metadata.

This review used only existing local methods, protocols, scripts and schemas. It introduces no counts, identity corrections, semantic values or phonetic values.
