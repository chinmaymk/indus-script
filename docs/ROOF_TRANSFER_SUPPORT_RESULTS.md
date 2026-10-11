# Roof transfer: support limits and two further tablet photographs

27 September 2026. **The selected corpus cannot support the declared test of roof-state prediction across graphic roots.** This is a feasibility result, not evidence that the roof lacks a common function. Separately, original photographs now support the broad fish-and-comb arrangements on two more identified tablets, with important limits on fine stroke readings.

## A prediction test needs independent comparisons

The earlier exact-frame screen found no qualifying cross-root rectangle. This follow-up asks a different question: are there enough comparable cases to train on two graphic roots and test on a third? The [protocol](../data/processed/roof_transfer_support_protocol.json) and [independent design review](ROOF_TRANSFER_SUPPORT_DESIGN.md) were fixed before the new grouped-support counts, with earlier corpus coverage already known.

Each branch groups whole records transitively by equal reference or identical full text after replacing all twelve selected sign endpoints with one TARGET. Every occurrence inherits that component. Grouping happens before excluding missing metadata; it is not rebuilt after a held-out root is removed. These are reference/formula components, not authenticated independent objects or dies.

Within each root, a matched pair needs opposite roof states in different components and the same sign pair, secondary site label, object code, field length and target position. The two fish pairs cannot supply opposite ends of one match. A root passes only if two such matches can use four distinct components. Mixed-state components can supply either state, but cannot be used twice. An exact edge-pair search finds a witness or exhausts the finite possibilities; it does not claim a maximum matching.

For each held-out root, all components touching it are removed from training. The test root must pass and at least two other roots must still pass after that removal. Any later archaeological interpretation would also need image-level authentication and physical object/die links, which the full corpus does not provide. No classifier, accuracy estimate or p-value was fitted here.

| Corpus and metadata branch | Eligible records | Target occurrences before metadata exclusion | Reference/formula components with targets | Roots passing marginal two-pair gate | Usable held-out roots |
|---|---:|---:|---:|---|---:|
| Strict, known secondary labels | 1,293 | 526 | 406 | Fish | 0 |
| Strict, unknown labels allowed | 1,293 | 526 | 406 | Fish, trident | 0 |
| Broader complete export, known secondary labels | 1,978 | 721 | 490 | Fish | 0 |
| Broader complete export, unknown labels allowed | 1,978 | 721 | 490 | Fish, trident | 0 |

The broader denominator excludes 78 one-token records from the earlier 2,056 complete-field pool because there is no outside context. Known-label means nonmissing after the frozen normalization rule; it does not mean independently authenticated archaeological provenance. Unknown/unknown matches are shown only in the sensitivity branch.

In the strict known-label branch, fish has 74 plain-bearing and 48 roof-bearing components, with six containing both states; trident has 47 plain-bearing and only one roof-bearing component. Basal U has no plain occurrence in that branch, and cross and three-strokes have no roofed occurrence. In the strict unknown-label sensitivity, trident reaches two roof-bearing components and passes. Basal U still has only one plain component; cross and three-strokes still lack eligible roofed fields. In the broader unknown-label branch, cross has roofed records, but no opposite-state edge within the fixed matching strata. All failed roots and all actual edge witnesses are retained in the result.

**Finite proof of the fold limit.** Removing training occurrences can only delete edges from a root's support graph. It cannot create two disjoint edges in a root that failed before removal. Therefore, if fewer than three roots pass marginally, no fold can have a passing test root plus two passing training roots. Every branch has only one or two marginally passing roots. The implementation also recomputes each post-purge pool directly; the independent verifier reconstructs all 100 root pools. The conclusion concerns this declared design and selected corpus, not all possible statistical questions.

## Original photographs: what is now checked

The four `_ M176` catalogue witnesses now have the following source status:

| M77 reference | Object evidence | Photographic disposition |
|---|---|---|
| 4407 | EH407, excavation1722; reviewed previously | Broad roofed cross/comb and U/two-long-strokes reverse; intentional notches, source calls the object entire. |
| 5444 | 3027(2), Pu35:3863 | Exact original photograph remains unresolved. Unsuffixed3027/EH558 cannot be substituted. |
| 4493 | EH493, find group8650b; both Vats plate faces recovered | Broad capped fish/comb and U/long-stroke cluster compatible. Four fine fish-side marks and exactly four reverse strokes are not independently certified from the coarse photograph. |
| 5477 | 13592 → CISI H-889, HM332; both faces recovered | Flanked fish/comb with no separately recognizable roof; wear and narrow upper margin limit categorical roof-absence certainty. Reverse shows ring/cup-like motifs, retained as the separate nonscript field. |

The [EH493 review](ROOF_FISH_4493_REVIEW.md) authenticates the exact Vats table row, including 0.4 × 0.23 inches, depth 4–7 feet, white steatite, type h and Mound F. Its 8650b identifier is shared among several illustrated objects. It is an assemblage key, not a unique artifact key; neither shared number nor similar text authorizes merging those objects.

The [H-889 review](ROOF_FISH_5477_REVIEW.md) uses excavation13592 in both primary catalogues. CISI's4483 is Finnish Concordance, and P1070 is a later photographic source, not the historical Pu61:4076 print. That historical print remains unrecovered. M77 source direction2 stays distinct from its normalized token order. The reverse's field-symbol83 is not script signM083.

Both photo reviews retain broad compatibility while declining to certify fine features that the reproduction cannot resolve. This is not an independently exact new transcription of either full field. Their different reverse fields also prevent treating the tablets as semantically controlled minimal pairs. No missing strokes are reconstructed, no catalogue token is changed, and no sign value is assigned.

## Reproduction and next evidence

The [support producer](../scripts/audit_roof_transfer_support.py) saves complete component membership, selected occurrences, matching strata, edges, witnesses, purged components and all417 coverage rows in [the result](../results/roof_transfer_support.json). The [independent verifier](../scripts/verify_roof_transfer_support.py) uses breadth-first graph traversal and all opposite-state occurrence pairs rather than importing producer helpers; its [output](../results/roof_transfer_support_independent.json) records the finite checks. Focused tests cover transitive leakage, mixed components, cross-stratum reuse, metadata sentinels, damage and failure after training-component purge. The [independent code review](ROOF_TRANSFER_SUPPORT_CODE_REVIEW.md) also records the exhaustive 1,024-graph oracle.

The [photograph audit](../scripts/audit_roof_fish_photos.py) verifies 37 evidence pins and eight exact crops across the [4493 ledger](../data/processed/roof_fish_4493_review.json) and [5477 ledger](../data/processed/roof_fish_5477_review.json). Hash and pixel equality checks protect provenance; they do not mechanically prove visual interpretations. No new downloads were needed.

Additional independently identified attestations are needed to make the declared transfer design feasible; merely increasing shuffle or classifier runs cannot supply them. The exact5444 photograph and better reproductions of the fine fish features remain useful source targets. None of these source improvements alone would identify a semantic operator. All417 meanings and phonetic values remain undetermined, and the decipherment goal remains open.
