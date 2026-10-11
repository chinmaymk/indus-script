# Independent review of metal numeral proofs

Review date: 2026-09-24. This bounded review checked `scripts/audit_metal_numeral_conventions.py`, its five focused tests, the generated JSON, and the convention, weight-anchor, original-record and plate ledgers. It independently recalculated the algebra below and verified all nested file fingerprints in the convention, original-record and plate ledgers. It did not reauthenticate physical objects or independently reread the drawings.

**Result:** the mathematical counterexamples and the conditional rejection using the two axe masses are correct. They do not select an Indus numeral system. One helper output label needs qualification; it does not change the reported archaeological contradictions.

## Checks

1. **Exactly all integer uniform radices R ≥ 8.** Under the explicitly assumed canonical convention, each lower-denomination coefficient must be less than the adjacent ratio. The largest lower coefficients in the proposed expressions are 4 for t, 7 for i and 7 for u. With `(t,i,u,x)=(1,R,R²,R³)`, the condition is therefore exactly `R>7`. The highest x coefficient is not bounded because no higher denomination is assumed. The two K-121 alternatives do not increase those maxima. This proves an infinite family for the chosen arithmetic expressions; it does not establish canonical carrying, uniform ratios, or the proposed segmentation of any inscription.

2. **The pair-bound derivative is correct.** With positive fixed masses M and m,

   `p(R)=(M/m)(R²+5R+4)/(7R²+6R)`

   has derivative

   `p′(R)=−(M/m)(29R²+56R+24)/(7R²+6R)²`.

   It is negative for every positive R. For M=1910 g and m=165 g, `p(8)=1719/682≈2.520528<2.6`; hence every R≥8 satisfies that upper bound. Also `p(R)>M/(7m)=382/231>1`, so the predicted original chisel is heavier than its tang throughout the stated family. The original-chisel bound is hypothetical, and the large axe fixes the scale; this is not an independent mass prediction or an all-object fit.

3. **The earlier t=i result is not contradicted.** The prior decimal failure fixes `i/t=1`. The new uniform decimal model fixes `i/t=10`, while both set `u/i=10`. These are different models. The focused test explicitly checks that the former fails the 2.6 bound and the latter passes. The mixed model `(1,8,80,800)` also correctly satisfies `4t=i/2` while having `u/i=10`; a half-unit premise alone therefore cannot establish a uniform octal system.

4. **Both two-axe contradictions are correct.** For `6i=s=262.233 g` and `7u+6i=M=1910.030 g`,

   `u/i=6(M−s)/(7s)=3295594/611877≈5.386040`.

   The nine-expression canonical model requires `u/i≥8`, implying `M≥62s/6=2709.741 g`. The two axes alone still require integer `u/i≥7`, because six lower units must not reach a carry; this implies `M≥55s/6=2403.8025 g`. Both exceed the reported large-axe mass. No chisel reconstruction is involved. The rejection requires complete extracted expressions, common units and exact encoding of surviving mass. Adjacent signs, other meanings, original mass or unquantified losses change those premises. The published decimal precision is not a measured error interval.

5. **The unrestricted-loss proof is correct.** For finitely many positive quantities q_j and positive surviving masses m_j, choosing `s=max_j(m_j/q_j)` ensures `L_j=sq_j−m_j≥0` for every object. Thus freely selected nonnegative object losses allow every positive unit proposal to reproduce the masses. At least one loss is zero with this minimal scale; if strictly positive losses were required, choosing any larger scale would also work. This is an identifiability argument, not evidence for any loss amounts. The examples explicitly do not impose the chisel geometry bound, so they cannot be described as fits to that bound plus all five masses.

## Helper qualification found during review

In the initially reviewed implementation, `axes_constraint` returns `compatible = large >= minimum_large`. This tests only the necessary lower-ratio bound, not the integer-ratio requirement of canonical carrying. For example, `axes_constraint(6,65.5)` returns true despite the implied `u/i=8.5`. Rename the output to `satisfies_minimum_ratio_bound`, or explicitly check integrality if the output is intended as full compatibility. The actual mass inputs return false even at the weaker bound; their rejection is unaffected. Compatible control examples at exact ratios 7 and 8 are valid but did not expose this distinction.

The numerical utilities also rely on their fixed callers to provide positive units, masses and nonnegative integer counts. They are adequate for the current bounded analysis, but should not be presented as a validated general-purpose inference API without input checks.

## Verification and scope

All five focused tests passed in this review. Independent exact-fraction calculations confirmed the mass ratio, both minimum masses and the four displayed uniform-base pair fits. The infinite-family and derivative claims were checked algebraically rather than inferred from finite numerical examples. Source fingerprints verified, but fingerprint agreement only establishes file identity.

The audit supports the narrow conclusion that these proposed count expressions and the stated mass experiments do not identify a unique base. It establishes no phonetic or semantic values, whole-script coverage, ancient mass-loss estimates, or reason to prefer octal over the surviving countermodels.

## Resolution of the helper finding

The parent corrected `axes_constraint` after this review. It now reports `satisfies_minimum_ratio_bound` and `ratio_is_integer` separately, and requires both for `compatible`. Independent reinspection confirmed the change. The existing axe test now includes `(small,large)=(6,65.5)` and correctly reports a satisfied lower bound, a noninteger ratio and incompatibility. All five focused tests passed again. The original finding above is retained as research history; it is resolved, and the archaeological conclusions are unchanged.
