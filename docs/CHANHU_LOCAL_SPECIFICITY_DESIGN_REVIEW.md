# Local specificity stress test: design and finite-information limits

This review precedes inspection of new control-code outcomes. It uses the already reported five-object contrast in `results/chanhu_local_contrast.json` and the existing deposit-results report. All five identities, group assignments and fish statuses are discovery data. Freezing the control calculation now makes it reproducible; it does not make the analysis confirmatory or repair the unverified archaeological comparison.

**The proposed test is useful as a check of whether many other code labels produce the same local association.** It cannot show that any competitor has a meaning, or that fish lacks a domain association. A single positive seal can carry several signs, so several apparently successful labels may describe the same one-object observation.

## Fair comparison and eligibility

1. Keep exactly the five existing source-object groups: associated-complex objects 2285, 2428 and 2529CC; bath-vicinity objects 3215 and 3207. Preserve the exact raw-row membership and previous metadata joins. Never reconstruct identities from a shared code or text.
2. Enumerate all observed literal W codes in the exact predeclared Chanhudaro seal-export cohort, including codes that occur only outside the local objects. Exclude explicit loss/unknown placeholders from candidate identity; retain doubt flags. Define eligibility of grouped source rows and the treatment of bare `SEAL` versus `SEAL:` from the existing cohort rule rather than adjusting it after counts. Do not silently exclude rare, reversed or contrary controls.
3. Use **single W220 versus other single codes** as the primary like-for-like comparison. The fixed fish-family union may be shown beside it, but pooling several forms increases opportunity for occurrence and is not a fair single-code identity test. Do not create outcome-selected competitor unions. Mark which candidate codes belong to the selected family; call the remainder “other codes,” not proven non-fish signs or nonsemantic controls. Excluded compounds may still be visually fish-like.
4. For every code on every object apply the same rule: certainly observed code implies positive even with damage elsewhere; absent only when every required source row passes the existing complete/known/nondoubtful rule; otherwise unknown. Do not treat missing code as absence on an incomplete text. Deduplicate code repetition within an object, not physical objects that happen to repeat a text.
5. Compute the baseline frequency from **certain-positive object counts outside all five local groups**, not token counts, occurrences in the target seal or classifiable-only denominators. Match exact count first; report a separate factor-two band `f220/2 <= fs <= 2*f220`. If the target's outside count is zero, the factor band is degenerate: report that rather than adding an unplanned pseudocount or nearest-neighbor rule. Include the target as a reference, not its own control.
6. Also report outside negative and unknown counts, total objects and the frequency interval `[fs, fs+us]`. Equal observed counts do not guarantee equal underlying prevalence or detection. A complete-text-only outside-frequency sensitivity is defensible if predeclared and applied to every code and W220 on the same objects. It answers a differently selected question; do not use it to replace an unfavorable primary matching set.

The outside sample is a frequency calibration set, not an independent bead-production control. Excluding five objects prevents their local outcome from directly selecting controls by frequency, but text, die, phase and reporting dependence may persist across the site. List overlapping text/die groups when already known; no new identity inference is warranted. Filtering outside controls to favorable archaeological locations would introduce a new, unplanned selection step.

## Define “same” and “stronger” before counting

Order the local status vector as `(2285,2428,2529CC,3215,3207)`. The known W220 and family vector is `(U,P,N,N,N)`, giving conditional difference bounds `[1/3,2/3]`.

Report three different comparisons:

- **Exact observational equivalence:** identical five-object P/N/U vector. Such a code cannot be distinguished from W220 by this particular binary-local observation.
- **Equal interval or lower-bound strength:** identical interval, lower bound equal to 1/3, or lower bound strictly above 1/3. A higher lower bound gives a stronger guaranteed contrast under the same fixed assumptions, not a more credible semantic interpretation.
- **Independent support pattern:** which named objects supply certain positives and how the result changes after omitting 2428. Equal group totals with a different positive seal are not the same object-level evidence pattern.

Do not call a larger upper bound stronger: it can merely represent more unknown text. Do not order overlapping intervals as though they were point estimates. Report the full two endpoints and the statuses. Exact-vector equivalence is the cleanest interpretation of a “competing label”; a lower-bound ranking is a separate descriptive screen.

## Algebraic limit before seeing any new code

Let a and u denote certain positives and unknowns among the three complex seals, and b and v the corresponding counts among the two bath seals. Every candidate has:

`L = a/3 - (b+v)/2 = [2a - 3(b+v)]/6`

`U = (a+u)/3 - b/2`.

To meet or exceed W220's lower bound, `2a - 3(b+v) >= 2`. Therefore:

| Bath positive-or-unknown count b+v | Required complex positives for L >= 1/3 | For L > 1/3 |
|---|---|---|
| 0 | at least 1 | at least 2 |
| 1 | all 3 | all 3 |
| 2 | impossible | impossible |

Thus any certain code on **one** complex object, absent on both bath objects, already reaches a lower bound of 1/3, regardless of whether the other complex objects are absent or unknown. This need not be evidence spread across several production contexts. The exact known fish interval additionally has one complex unknown and one complex negative.

If k distinct eligible codes have vector `(U,P,N,N,N)`, they yield k labels but **one observed vector and one certain-positive object**. The number k cannot exceed the number of distinct certainly observed candidate codes on 2428, but it can be greater than one without adding an independent object or deposit. Removing 2428 yields `(U,N;N,N)` and bounds `[0,1/2]` for every such code. This is an algebraic consequence, not a newly computed corpus result.

There are at most `3^5 = 243` possible complete P/N/U vectors and only `10*6 = 60` possible group-count profiles for groups of three and two, before any source restrictions. Many code identities therefore have intrinsically limited ways to differ on this sample. Counts of matching codes should be accompanied by counts of distinct vectors, distinct positive-object supports and outside-frequency matched candidates. These counts are not independent trials; there is no justified binomial or permutation p-value from their multiplicity alone.

## Coding and interpretation checks

Freeze the exact candidate universe, cohort, placeholder policy, normalization, uncertainty parser, outside-frequency definition, match bands and ranking before the producer runs. Preserve all candidates and exclusion reasons, including zero local positives. Verify W220's five statuses and bounds reproduce the previous result exactly; a failure is a parsing/cohort discrepancy to resolve, not a new scientific finding. Check that group sizes remain three and two for every code and that the outside denominator excludes every row of all five object groups.

Literal W codes are editorial units. Variant splitting and composite coding can divide or combine a graphic concept; no global W→M crosswalk or semantic merger should be introduced to improve rankings. Equal profiles show observational nonuniqueness in this representation, not synonymy or equal ancient function. A lack of equal matched controls would likewise be only finite uniqueness among this candidate set, not proof that fish means beads or gemstones.

The output should lead with the number of outside-frequency controls, their full status vectors, bounds and equivalent-profile classes, followed by the omission of 2428. Keep both archaeological area blocks and their unverified comparability explicit. The test cannot become a true craft-specific or held-out test through frequency matching.

The companion design JSON pins the two inspected inputs and this review. No new control outcome, code-frequency table, identity query or sign-family change was made for this design audit. All 417 semantic and phonetic values remain null.
