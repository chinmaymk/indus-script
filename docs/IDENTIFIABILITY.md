# What is proved, and what is not

## A precise limitation on symbol-internal decipherment

Let `S` be a finite sign alphabet and `C` an observed corpus of strings over `S`.
Let `π: S → T` be any bijection onto a set of labels. These labels might be numbers,
syllables, arbitrary strings, or candidate meanings. Relabel every corpus token using
the same bijection.

For any sign tuple `(s1, …, sk)`, its count in `C` equals the count of
`(π(s1), …, π(sk))` in `π(C)`. The correspondence is bijective at every token position.
Consequently:

1. Sign, pair, and higher n-gram frequency distributions are unchanged up to labeling.
2. Entropies, mutual information, and positional-distribution divergence are unchanged.
3. A sequence model whose parameters are permuted in the same way assigns exactly the
   same probability to every corresponding string.
4. Smoothed n-gram models retain this equality when priors and vocabulary sizes are
   also carried through the bijection.

Thus any score based **only on those symbol-internal quantities** cannot choose which
of these label assignments denotes the ancient sounds or meanings. Better predictive
performance demonstrates a better model of sign distribution, not an identified
translation. Even a complete one-to-one key can be perfectly self-consistent and wrong.

This argument does **not** prove that decipherment is impossible. Archaeological
context, bilingual alignments, independently identified quantities, or a restrictive
historically justified language model add information that is absent from the premise.
It also does not show that all linguistic hypotheses are equally good when such
external constraints are supplied. A key must be tested against those constraints.

The result is narrower than claiming all possible decipherments are related by
permutations: many real scripts have ligatures, allographs, polyphony, or homophony.
One unidentifiable subclass is already enough to show that statistical fit alone does
not identify a unique semantic key.

## Executable witness

[`scripts/hypothesis_checks.py`](../scripts/hypothesis_checks.py) renames every observed
sign to an arbitrary label, refits the same bigram model, and compares every sequence
likelihood. The saved witness is
[`results/relabeling_counterexample.json`](../results/relabeling_counterexample.json).
The tests also check relabeling invariance, probability normalization, and known
analytic cases independently of the corpus.

## Why these statistics do not identify writing direction

Reversing every string exchanges the two coordinates of the adjacent-pair
distribution. Since `I(X;Y) = I(Y;X)`, adjacent mutual information is unchanged.
Endpoint Jensen–Shannon divergence is also unchanged because its arguments simply
exchange places. Neither statistic determines which physical edge was read first.

Reading direction needs external evidence or an explicit transcription convention.
The mayig corpus documents left-to-right display order, with right-to-left reading.
The overlap comparison supports the same **display** order for the secondary export.
That comparison does not prove the direction of every object or every line.

## What the empirical tests establish

A permutation-test p-value is conditional on its particular exchangeability null.
Rejecting random order or independent positions is evidence against those nulls. It
does not choose between spoken-language writing, an administrative code, or another
structured notation. The actual weather-icon control provides a concrete example.

The historical conclusions remain empirical and revisable. The algebraic relabeling
result is the proof; the corpus statistics are evidence, not a proof of decipherment.
