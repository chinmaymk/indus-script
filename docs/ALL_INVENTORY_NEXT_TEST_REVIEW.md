# Which next test could distinguish readings?

28 September 2026. **I found no new historical reading-discrimination test that the retained independent anchors presently support.** Existing data do support finite rejection of particular rules, and they support a sharper design for distinguishing the two surviving conditional numerical candidates. That design has different predicted outcomes but currently lacks the required measured referents. No random fit, additional entropy calculation or semantic assignment was performed in this review.

This is a conclusion about the reviewed evidence and specified model classes, not a proof that meanings are structurally impossible to recover. “All 417 values remain null” records what is established; it is not itself an identifiability theorem.

## What is available now

| Evidence layer | Exact retained support | Consequence for a reading test |
|---|---|---|
| All-sign index and primary Table I | 417 rows, 13,372 occurrences; 264 signs below ten occurrences, 112 singletons; strict candidate native-M sequences observe 332 signs and leave 85 unobserved | Broad distributional coverage, with a large rare tail. These are not 417 externally constrained meanings. |
| Conditional numeral equations | Four positive integer solutions; two survive the stated minimum-base screen: (L,S,v)=(10,8,6) and (36,20,4) | A finite competition exists. The alleged field equalities, segmentation, units and value of source sign900 remain assumptions. |
| Tool measurements | Nine proposed expressions and five reported surviving masses in the earlier model; independent cleaning/loss amounts unavailable | Current-mass models have already been rejected under specific assumptions. Arbitrary per-object losses can fit any positive proposed quantities, so another free-loss fit cannot discriminate. |
| Capacity follow-up | Two confirmed heights, 1033A=91.44cm and 1033B=86.36cm; zero new directly measured fill volumes and zero new complete external test pairs | Heights are measurements, not calibrated contents or capacities. Alias/count conflicts prevent treating the selected old fit as new validation. |
| New weight/instrument search | Five queries; zero new qualifying inscribed weights or measuring instruments | H2000-4496/9880-01 lacks reported mass/verified inscription. BM120228's indexed 8g belongs to a damaged stamp-seal, with no basis for equating its text to that mass. |
| Chanhudaro deposit frame | 65 illustrated entries, 55 accepted metadata joins; seven named associations reviewed, 58 explicitly unsecured; zero secured matched strata | Cannot execute the declared phase/deposit test. Zero secured strata does not mean every context was exhausted or lacked production. |
| Weaker local Chanhudaro contrast | Five objects in two area blocks; W220 bounds +1/3 to +2/3, based on one certain positive; nine exact-frequency controls do not tie; among 71 wider controls W368/W790 tie the interval, not the object profile | This conditional result is real but does not uniquely select fish, gemstone or an occupation. The W790 graphic survives photograph review. With either comparison absence withheld, target bounds include zero. |
| Roof transfer | Zero passing held-out-root folds in each saved support analysis | There is no supported transfer test to fit. Adding shuffles or a classifier would not supply the missing comparisons. |

These counts come from the pinned results listed in the companion JSON. The current index contains exactly 417 null semantic and 417 null phonetic fields. The strict sequence sample's 85 unobserved signs still have primary catalogue evidence; they are not signs without attestations.

The earlier exact terminal-marker counterexamples, the repeated goblet-stamp counterexample to a unique vessel identifier, the tool-mass contradictions, catalogue span/collision witnesses and the roof coverage audit already answer narrower questions. They should not be repackaged as new experiments. In particular, a same stamp on two goblets rules out only the stamp design alone being an injective identifier of individual physical vessels; it permits a maker, owner, batch or class identifier.

## Identification is relative to a declared model

Let an admissible model include a reading key K and nuisance assumptions θ: segmentation, allography, field relationships, quantity referent, error/loss, units, archaeological joins and sampling. A sign's value is identified only if its projection has the same value in **every** model compatible with the observations and independently justified restrictions. Rejecting one tuple (K,θ) does not establish another K, and allowing θ to change freely after each failure removes falsifiability.

The relabelling proof in `IDENTIFIABILITY.md` concerns internal scores in a model class closed under relabelling. If each emission/context parameter is relabelled along with the key, internal likelihoods remain unchanged. A fixed independently justified lexical or contextual constraint can break that symmetry. It is therefore wrong to assert that every model or every conceivable decipherment is equally good. It is also wrong to assume a visually evocative sign already has a fixed lexical value: that supplies the desired interpretation as an assumption.

There is **no model-independent minimum number of external anchors** needed for 417 signs. Two illustrative cases make the distinction precise:

- In a deliberately simple bijection onto a known set of 417 distinct labels, with no other restrictions, k distinct fixed sign-label pairs leave `(417−k)!` compatible keys. At least two unanchored signs can still exchange labels. At k=416 the final label is forced, so “417 independent anchors are always necessary” is false. With homophony, polyphony or an unknown label universe even this counting model does not apply.
- In a fixed additive numerical model `Xv=y`, independent equations constrain combinations of values. For unrestricted real values the solution set has dimension `417−rank(X)` when consistent. The same local continuum follows under positivity if a feasible solution lies strictly inside the allowed region. Boundary inequalities or integer restrictions can instead make a rank-deficient system unique, so rank alone must not be promoted to a universal impossibility proof. Unknown physical unit introduces scale ambiguity, and unknown object-specific loss can introduce much more. No authenticated all-inventory matrix of represented quantities exists here to compute this rank.

One real semantic anchor would identify something in an appropriate model; it would not leave literally every value unidentified. Conversely, many context observations with no fixed relationship between sign and referent need not identify even one lexical value. Useful evidence is constraint quality and propagation within a defensible model, not just the number of photographs, catalogue rows or contexts collected.

## Priority 1: a unit-free quantity ratio between the existing candidates

This is a new, finite discriminating design derived from the existing alternatives, not another search for a convenient fit. Under the frozen proposed equations, candidate (10,8,6) gives total A=36 and total B=61; candidate (36,20,4) gives A=112 and B=145. A single independently measured positive quantity cannot choose between these if each candidate may fit one unknown common unit: choose its unit to match that one observation.

Two **commensurate represented quantities**, however, predict different ratios B/A: **61/36** versus **145/112**. Neither arbitrary-unit choice changes a ratio. Thus a second independent quantity with a nonproportional prediction is the minimal extra observation for this particular two-candidate, one-scale comparison. It is not a general minimum for decipherment, nor a claim that any two measured objects suffice.

For a shared worst-case relative error bound `0≤e<1` on each quantity, require the represented quantity `q_j` to lie in the observed measurement interval `m_j[1−e,1+e]`, allowing errors independently within these bounds. A candidate ratio r permits the observed ratio interval

```
[ r(1−e)/(1+e), r(1+e)/(1−e) ].
```

Since 61/36 is larger than 145/112, the intervals are disjoint exactly when

```
((1+e)/(1−e))² < (61/36)/(145/112).
```

Equality gives touching intervals, not guaranteed separation. Common multiplicative calibration cancels; treating it as independently varying on both objects is conservative. Overlap means some outcomes are ambiguous, not that every outcome is. A measured ratio may also reject both candidates. This is bounded-error geometry, not a p-value.

An independent exact check of the new `results/numeral_calibration_design.json`, without importing its producer, gives ratio-of-ratios **1708/1305**, hence polynomial **403e²−6026e+403>0**. The smaller root is approximately **6.71786805%**. At 5% per quantity the candidate intervals are `[1159/756,427/228]` and `[2755/2352,435/304]`; they are strictly disjoint. At 10% they overlap. The pinning script verifies all four saved error cases using corner ratios, the displayed threshold using high-precision decimal arithmetic, the hypothetical single-total units and the producer's source hashes. These checks validate the conditional mathematics, not the unmeasured physical assumptions. The saved zero available pair count applies to the reviewed cases, not an exhaustive global inventory.

**Eligibility before measurement:** authenticate the inscription/field and its reading alternatives; independently justify which measured attribute it represents; establish shared units and comparable referents; freeze damage and uncertainty bounds; retain every alternative segmentation and join. If admissible alternatives produce overlapping unions of prediction intervals, report that residual ambiguity rather than selecting the favorable transcription. For these exact A/B examples, neither secure measured contents nor a common-unit artifact pair is established. We therefore have an executable algebraic separation calculation, but **no historical calibration experiment to run now**. The five-query weight search and zero new capacity test pairs do not satisfy this gate.

## Priority 2: a replicated external domain prediction, with lexical claims kept separate

The Chanhudaro program remains the closest finite archaeological test because it has a 65-object frame and a fixed fish indicator. A useful next outcome would be sign enrichment in independently classified bead-production deposits that repeats across more than one production complex, under declared phase/reporting comparability and unknown-text bounds. The rival prediction is generic concentration of many equally common signs in artifact-rich or workshop contexts. A successful contrast would constrain a domain association, not uniquely translate “gemstone.”

No new counting is justified by the present strict support ledger: there are zero secured matched strata. The already-executed five-object local comparison and all-code specificity screen are discovery evidence; adding signs or changing the family would not supply replication. The physically catalogued field-card archive is a concrete route to deposit resolution, but the individual cards are not present in the retained data. This priority is **currently unavailable**, not failed. An eventual comparison may use explicitly probabilistic archaeological classifications and sensitivity bounds; it need not demand perfectly proven ancient absence. It must nonetheless distinguish nonreporting from a comparable observation opportunity and model the dependence within one complex.

No third fit is recommended merely to fill an experimental queue. The existing hind-leg proposal has eight candidate occurrences but no independently identified neighboring word that fixes a predicted reading; fitting flexible later lexica to those neighbors would add choices, not an external test. Roof support is empty under the declared transfer gate. These are explicit stopping conditions for current local computation, while the numerical ratio design provides a concrete target for genuinely discriminating evidence.

## Persistence

`scripts/pin_all_inventory_next_test_review.py` checks the quoted current support fields and all 417 null values, records the already saved conditional candidates, and writes `data/processed/all_inventory_next_test_review.json` with source hashes. It does not fit a model, alter counts, download data or modify the shared index. The mutable README is intentionally not pinned. This review is a new snapshot; prior frozen reports remain unchanged.
