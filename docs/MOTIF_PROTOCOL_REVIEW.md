# Independent review of the frozen motif fast-route design

Date: 2026-10-10. Scope: read-only mathematical/design review of `data/processed/motif_fast_route_protocol_v1.json` and the named local parser. Reviewed protocol SHA256: `1e2f3d21c3828d09f01be2c6291d5c9ec306654aabf83781c7e826224f375022`. No association counts, raw corpus rows, external data, or implementation outputs were inspected. This is not an implementation certification or evidence for any sign meaning.

## Issues to fix or qualify before interpreting a run

1. **Freeze the transfer decision threshold.** Version 1 gives discovery a maxT cutoff of 0.01, but specifies Holm for transfer without stating a rejection threshold. It also leaves implicit whether the all-condition transfer alone gates support. State the cutoff before examining results. Treat Good/Fair transfer as sensitivity, not a second opportunity to declare transfer if the primary analysis fails; otherwise the two opportunities need a prespecified combined error rule.

2. **Make quality handling deterministic at artifact level.** Group validity must be established from all in-scope rows before quality filtering, so removing an inconvenient row cannot rescue an artifact with inconsistent sequence/site/motif or invalid transcription. If repeated rows for one artifact carry different quality labels, specify which quality rule admits that artifact. Recompute each retained sequence family's motif-proportion vector from retained artifacts, retain the same fixed candidate list, and preserve the original discovery-text exclusion set in the quality sensitivity.

3. **Limit the maxT error claim.** The global test is calibrated under the specified joint within-length exchangeability null. The maxT reference is also a useful multiplicity-adjusted selection rule under that model. Strong familywise control for each true individual pair under arbitrary mixtures of null and non-null pairs would need a subset-pivotality or equivalent argument, which the protocol does not supply. Do not upgrade its exploratory selected pairs to that stronger claim. Holm in transfer needs valid marginal permutation p-values conditional on the fixed selection; prior reuse and archaeological dependence remain explicit limits.

These clarifications need a dated amendment rather than silently changing a frozen file after seeing outcomes.

## The fractional-vector variance formula is correct

In one exact-length stratum, let n be the number of sequence-family slots, m the number with a specified sign, and y the observed proportion of artifacts carrying one raw motif within each family. Let S = sum_i (y_i - mean(y))^2. Under a uniform permutation of the fixed y values, each permuted value has variance S/n and two different positions have covariance -S/[n(n-1)]. Therefore the sum over the m sign-positive positions has variance

`m*S/n - m*(m-1)*S/[n*(n-1)] = m*(n-m)*S/[n*(n-1)]`.

Subtracting the fixed mean term does not change variance. Independent permutations across length strata allow their variances to add. This is precisely the protocol denominator; it works for fractional values as well as binary labels. Strata with fewer than two slots contribute zero, and zero-total-variance pairs cannot be tested with this Z statistic.

The same calculation for two motif columns replaces S with their centered cross-product. Shuffling their entire proportion vectors together preserves that covariance and the simplex constraint; shuffling columns separately would define the wrong null. Sign counts, positive-motif support counts, and the denominator are all invariant under the specified shuffle, so the discovery eligibility mask can and should be fixed before permutation. A null maximum is over the complete eligible discovery pair set, not only the finally selected pairs.

## Selection, duplicates, and transfer constraints

The plus-one Monte Carlo exceedance formula is appropriate when the observed arrangement and independently sampled uniform permitted permutations are exchangeable under the null. Finite Monte Carlo resolution and ties must remain visible. Nonpositive observed Z values cannot qualify for positive-direction selection.

One sequence family per site, with a vector averaged over distinct eligible artifacts, gives each exact text total weight one and retains mixed motifs. It does not make artifacts, dies, family sizes, or styles independent. Permuting those vectors assumes that different family sizes and unmeasured contexts are exchangeable conditional on length; that is a model assumption, not a consequence of deduplication.

The discovery candidate file must be saved before transfer outcomes are computed. Remove every retained discovery exact sequence from transfer, not merely texts containing a selected sign. For the Good/Fair sensitivity, use that same exclusion set rather than rebuilding a smaller discovery set. An untestable candidate remains in the original selected family for Holm with p=1. Use the standard sorted-p step-down adjustment with cumulative maxima and upper bound 1, preserving all selected candidates in the family size.

The protocol's stated conclusion scope is appropriate: a descriptive site-transfer association under these sampling and exchangeability assumptions. Neither successful transfer nor lack of support identifies a sound value, an animal word, a personal name, an office, or a commodity.


## Pre-run resolution

Protocol v2 (SHA256 `9a339d2bd761658d2ed56465cdc6efe635efe6432f13185f063a5dde64a8f1d3`)
resolves all three specification points above before new joint counts, and freezes
an absolute 1e-12 Z tolerance for permutation ties. A separate implementation review
found that constant fractional motif coordinates could gain tiny nonzero variance
through rounding. Both observed and permutation centering now explicitly zero
columns with identical original values within a stratum. Synthetic constant and
mixed-stratum regressions check the mathematical zero case. This corrects numerical
implementation; the stated null and eligibility criterion are unchanged.
