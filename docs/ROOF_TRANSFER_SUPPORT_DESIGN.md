# Pre-count design review: roof transfer support

The proposed procedure is a valid **finite support audit under explicit formula/reference grouping**. It can determine whether a held-out-root comparison has the specified component-disjoint opposite-state witnesses. It cannot establish archaeological independence, a productive roof operation or sign meaning. No new support outcomes, corpus counts or parent implementation were inspected for this review.

The frozen protocol is `data/processed/roof_transfer_support_protocol.json`. It correctly includes grouping before metadata exclusions, purging every component touching the held-out root, and checking at least two training roots **after** that purge. Those conditions are necessary to avoid treating marginal support as usable fold support. The fixed threshold of two disjoint pairs can be checked exactly without a maximum-matching library.

## Units and order of operations

For each corpus branch, first retain complete undoubted fields of length at least two, with the additional existing strict flag in the strict branch. The broad branch remains an explicitly different selection. Preserve source reference, field identity, original tokens and every selected-target position. Separate sides and lines remain separate records, even when the shared reference later places them in one component.

Build the grouping graph over **all structurally eligible records**, before known/unknown metadata scoring filters. Join records with the same source reference or identical full collapsed sequence; collapse all twelve selected endpoint codes to the one literal TARGET marker everywhere in the sequence. Do not collapse only the focal occurrence or only one root. Other sign codes and positions remain intact. Compute transitive connected components, preferably with union-find. This is equivalent to connecting occurrence nodes if all occurrences inherit their record’s component and reference links; record-level construction avoids quadratic duplication.

Component identity must be fixed before making folds. Do not recompute components from the training rows after removing a root: removing a bridge row must not undo a previously established grouping relationship. The full sequence, not a short neighboring window, defines formula equality. Known different objects can still share a formula component; this is conservative leakage control rather than an assertion of common physical identity.

Do not split large components to improve support. Report their size and root composition as limitations. Conversely, references and formula similarity do not identify every shared physical object or die; unmatched duplicates can remain. The protocol’s separate branch construction also means that a bridge record available only in the broad corpus may connect records that remain separate in the strict graph. Thus component-disjoint means disjoint under that branch’s recorded grouping, not disjoint under every known source linkage. Any decision to use one common broader grouping graph for both branches would be a separate, prospectively fixed conservative sensitivity, not a change made after observing gates.

## Metadata and matching strata

The matching key is exactly:

```
(pair_index, site_label_unverified, source_object_code,
 field_length, target_position)
```

Use one fixed position convention. Pair identity prevents M059/M065 and M060/M066 from supplying opposite endpoints of one fish match. Both pairs nevertheless belong to one fish root. Two accepted fish edges may come from different fish pairs, provided each edge stays within its own pair stratum and no component is reused. They count toward one supported root, not two.

In the primary known-label branch, missing site or object metadata excludes an occurrence from scored support, but does not remove it from grouping or from the list of roots touching a component. The unknown-label sensitivity can match a stable unknown sentinel only as a labelled sensitivity. An unknown/unknown match is not a known shared site.

**Pre-count clarification resolved:** the updated protocol strips surrounding whitespace and treats null/empty values plus case-insensitive `<unknown>`, `unknown`, `null`, `none` and `?` as missing. This prevents a sentinel from becoming a known label. The convention was updated before counts; labels must not be inferred or repaired from context. A nonempty secondary site label still lacks archaeological authentication, and numeric object codes must retain their documented source meaning.

No context-token equality beyond these metadata/position conditions is required for an opposite-state match. That is intentional: this gate measures availability of comparable cases for a future prediction task; it is not a repetition of the exact-frame rectangle screen. In fact, records sharing an identical fully collapsed sequence occupy the same component and cannot supply an independent base/roof matched pair here.

## Exact threshold algorithm

For one root and one eligible scoring pool, construct a simple undirected graph whose vertices are the fixed global component IDs. For each matching stratum, collect the components containing at least one base occurrence and those containing at least one roof occurrence. For every base component C and roof component D with C different from D, add the unordered edge {C,D}. Store a concrete pair of occurrence witnesses, the stratum and state orientation.

A component can contain both states, possibly in several strata. Do not discard it automatically, create a self-edge, or treat separate base/roof copies of it as independent vertices. Multiple witness pairs or multiple compatible strata between the same two components form **one edge** for the threshold. Retain all available provenance or choose one deterministic lexicographic witness for display; repeated witnesses do not create additional support.

An exact algorithm for the fixed requirement of two matched pairs is:

```
edges = sorted(unique unordered component edges)
for each unordered pair (e1, e2) of distinct edges:
    if the union of their component endpoints has size four:
        return PASS, e1 and e2 with occurrence witnesses
return FAIL
```

This searches across the union of all strata for the root, so component reuse across strata is excluded. Four distinct endpoints give two valid opposite-state matches and both states automatically. Failure after enumerating every edge pair is an exact finite failure of the threshold. A single greedy matching is insufficient: taking the middle edge of a four-vertex path first would miss a valid pair of outside edges. The enumeration uses at most quadratic comparisons in the number of unique edges and can stop at the first success.

There is no need to compute a maximum matching. Report `has_two_component_disjoint_pairs` and, on success, two witnesses. Do not call a returned pair count2 a maximum or interpret early stopping as proof that no larger matching exists. If a maximum is later required, mixed components make this a general undirected matching problem; a naive bipartite split into base/roof copies can use the same physical component twice. A general-graph maximum matching algorithm or exact component-capacity formulation would then be needed. That extra task is unnecessary for this gate.

Useful synthetic checks, without corpus exposure, are: empty graph; one edge; triangle of mixed components (fail despite three edges); four-vertex path (pass); four-cycle (pass); star (fail); the same unordered edge witnessed in multiple strata (still fail); and a pair of disjoint edges from different strata (pass). Also check that replacing a reference by several duplicate occurrences does not create a second edge.

## Held-out folds and support gates

For each held-out root H, find every precomputed component containing any structurally eligible occurrence of H, including H occurrences excluded from scored support by unknown metadata. Remove **all training occurrences in those components**, irrespective of their root. The scored test pool remains occurrences of H satisfying the branch’s metadata rules.

Run the two-edge threshold on that test pool. Then, for each other root, rerun the same threshold on its remaining training pool after purge. A fold passes the proposed proxy-support gate only if H passes and at least two distinct other roots pass after purge. A declaration that three roots passed their original marginal gates is insufficient: all training support could have been removed by H’s components.

The frozen protocol now states this correctly. Every passing fold therefore has at least three represented roots, counting fish once. State both the per-fold result and the set of supported training roots. If a separate reporting target requires at least three different roots each to be usable as the held-out root, that is an additional condition; it does not follow merely from one passing fold. Do not silently conflate these two summaries.

Within any root’s returned matching, each component is used once globally across strata. The protocol does not require the support witnesses for two different training roots to be disjoint from each other, and the same component can contain both roots. That is not train/test leakage after the required purge, but it limits the number of independent training units. Preserve those links for any future grouped weighting or resampling. Do not describe two supported training roots as two independent archaeological samples.

## Required output and interpretation

Retain corpus and metadata branch identifiers, exact selected endpoints, input hashes, missing-metadata rules, component membership, reference and collapsed-formula link reasons, and the structurally eligible denominator. For each root and fold, report scored base/roof occurrence and component coverage, mixed components, component IDs purged, surviving training roots, and exact threshold outcomes. Passing edges need actual occurrence IDs, references, states, pair indices and matching keys. Failure should identify whether no edges existed or no two disjoint edges existed; it should not imply there were no ancient roofed forms.

Keep three gate layers separate:

1. **Recorded proxy support:** the finite grouping and matching conditions above.
2. **Authenticated source and archaeological support:** image-level roof states, complete fields, and independently established artifact/die links. These are unavailable for the full selected corpus; a positive proxy gate cannot silently promote them to passed.
3. **Future model specification:** fixed features, targets, controls, loss and grouping strategy. No classifier or p-value belongs in this support audit. Under the parent’s stated constraint, fitting must wait for both support and archaeological-independence requirements, not merely a successful proxy match.

The endpoint is deliberately a feasibility check, not a power calculation. Two component-disjoint pairs do not guarantee useful error estimates, representativeness, causal exchangeability, adequate contextual overlap or enough variation for a particular classifier. No significance threshold or semantic conclusion follows from passing it. A failure says that the declared proxy design is unsupported in the selected data, not that roof signs lack a common function.

## Review scope and timing

This note was written before inspecting any new grouped-support outputs. I read the pre-existing `roof_modifier_protocol.json`, the newly frozen `roof_transfer_support_protocol.json`, and the parent’s proposed algorithm and clarifications. I did not inspect the implementation or new corpus support counts, write parent code, fit a model, download data, or modify the frozen protocol. The sentinel clarification was incorporated in the protocol before counts. The fold-level distinction remains a reporting caution, not an outcome-driven revision. The frozen protocol also resolves the initially identified post-purge training-support and metadata-filter-order issues.

## Inspected source pins

- `data/processed/roof_modifier_protocol.json`: SHA256 `09fb3f35c1b52a71a5fd49cf388a4ba689d49360d0b156f04158dc8fc465fb4c`.
- `data/processed/roof_transfer_support_protocol.json`: SHA256 `64246b8448498624e3f166b34709610fdc87d8ac318b3d9e9064bb43ff35ec43`.
