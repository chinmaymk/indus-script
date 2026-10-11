# What geography can and cannot explain

The primary catalogue's site counts rule out a specific explanation of the jar
family's positional contrast: **different mixtures of the seven recorded sites,
with identical empirical position rates within each site, cannot reproduce the
observed difference**. There must be a within-site difference as well.

This is an exact statement about the tabulated occurrences, conditional on correct
transcription and the catalogue's classifications. It does not identify meanings,
establish causation, or claim a population-level significance test.

## Source evidence

We manually transcribed the eight signs in the five shape comparisons previously
recorded in `results/primary_shape_contrasts.csv`. Table III supplies their site
counts. Table IV supplies object-type counts for the fish and stroke comparisons.
The result is 12 rows, each of which adds to its printed total and agrees with the
same sign's total in Table I. These are sign occurrences, including repetitions,
not independent objects.

- [Context counts, source pages, row locations and review provenance](../data/processed/primary_context_subset.json)
- [Exact-rational analysis script](../scripts/analyze_context_bounds.py)
- [Mixture bounds](../results/primary_context_bounds.csv)
- [Within-context bounds](../results/primary_within_context_bounds.csv)
- [Audit and source limitations](../results/primary_context_audit.json)

The source is Mahadevan 1977, Tables I, III and IV. Site codes are defined on printed
p. 31; object codes on p. 30. The numerical context rows were visually inspected
on printed pp. 746, 747, 751, 753 and 754. This is a single transcription pass,
not independent double entry. Summation checks supplement the visual evidence.

## The mixture bound

For signs A and B, let `p[c]` and `q[c]` be their respective proportions of
occurrences in context c. Suppose an event, such as final position, has the same
empirical rate `r[c]` for both signs within every context. Each rate lies in [0,1].
The difference in their overall event rates is then

```
sum_c (p[c] - q[c]) * r[c].
```

Its absolute value is at most

```
TV(p,q) = (1/2) * sum_c |p[c] - q[c]|.
```

To prove this, write `d[c] = p[c]-q[c]`. Since both distributions sum to one,
the positive d terms sum to TV and the negative terms sum to −TV. Multiplication
by any r in [0,1] cannot increase either extreme. Equality is attainable by
assigning rate 1 to positive terms and 0 to negative terms, or the reverse.

For a shared full distribution of positions `K[position|c]`, the same argument
gives the stronger categorical contraction inequality:

```
TV(pK, qK)
 = (1/2) * sum_position |sum_c (p[c]-q[c]) * K[position|c]|
 <= (1/2) * sum_c |p[c]-q[c]| * sum_position K[position|c]
 = TV(p,q).
```

No joint position-by-context table is imputed. A violation of this necessary
condition means no shared empirical context rates can exactly fit the two
marginals. Passing the bound would be inconclusive, not proof of such a model.

## Results

All differences below are absolute percentage-point differences. Each row tests
the named context variable separately.

| Signs | Position event | Observed gap | Maximum from site mix alone | Maximum from object-type mix alone |
|---|---|---:|---:|---:|
| M342 / M343 | Final | 66.78 | 12.16 | Missing source rows |
| M342 / M344 | Final | 63.89 | 19.08 | Missing source rows |
| M342 / M345 | Final | 65.68 | 11.40 | Missing source rows |
| M087 / M099 | Initial | 39.97 | 23.99 | 28.19 |
| M059 / M065 | Initial | 26.20 | 10.17 | 8.96 |

Every available comparison exceeds the mixture bound. The script also checks the
whole four-category position distribution and reaches the same incompatibility
in all seven comparisons. The numbers strengthen the case for preserving these
graphic distinctions when testing candidate readings. They do not establish that
each form has a different word value: context-conditioned allography, modifiers,
and other functions remain possible.

## A guaranteed contrast within Mohenjodaro

An even more direct result follows from the marginal totals. If an inventory has
N occurrences, F final occurrences and N_c occurrences in a particular site, the
number F_c that are both final and in that site must satisfy

```
max(0, F + N_c - N) <= F_c <= min(F, N_c).
```

The upper bound follows because the intersection cannot exceed either set. The
lower bound follows because at most `N-N_c` final occurrences can lie outside the
site. These bounds are sharp for the two given margins; both extremes can be
realized by a valid allocation. Bounds for different sites should not be treated
as independent allocations that can all attain their extremes simultaneously.

For M342, N=1,395, F=971 and N_MD=766. Therefore at least 342 final occurrences
must be at Mohenjodaro, giving a final rate of at least **342/766 = 44.65%**.

For M343, N=177, F=5 and N_MD=101. At most five can be final at Mohenjodaro,
giving a final rate of at most **5/101 = 4.95%**.

Thus the M342 final rate exceeds the M343 final rate at Mohenjodaro by at least
**39.70 percentage points**, whatever the unobserved joint table is. The corresponding
minimum differences against M344 and M345 are 36.31 and 38.59 points.

This is a within-site positional difference in the historical catalogue. It is
not an estimate obtained by assuming independence or filling in missing cells.

## What remains unresolved

Site and object type have been tested **separately**. They could still explain
patterns jointly through their association, even when neither does so alone.
For example, let A occur in binary contexts (0,0) and (1,1), and B in (0,1) and
(1,0), with equal weights. Each individual context variable has identical
marginals for A and B. Yet the common rule “event occurs when the two context
values are equal” separates A and B perfectly. The tests preserve this example
to prevent interpreting separate marginal bounds as joint adjustment.

Chronology, object subtypes, line length, neighboring signs and editorial decisions
are also uncontrolled. Position-conditioned allographs are compatible with the
findings. A stochastic model with equal underlying probabilities is not literally
impossible merely because finite observed rates differ; no sampling p-value is
claimed here. Repeated inscriptions would require special care for such inference.

The text PDF has a specific scan gap: PDF p. 768 is printed p. 757, and PDF p. 769
is printed p. 760. Printed pp. 758–759, which would supply the remaining Table IV
rows including the jar family, are absent there. The two adjacent rendered pages
are retained as evidence. We have not filled those missing counts from another
table or called them zero. This also means a constant printed-page/PDF-page
offset must not be assumed across the entire book.

Next discriminating work is to recover the missing source pages and obtain
joint site × object × position counts from checked inscription-level records.
Semantic or phonetic values still require independent anchors beyond these
distributional constraints.

A subsequent [secondary-corpus replication](JOINT_CONTEXT.md) now compares joint
site × type × length strata. The W740/W741 and W220/W235 contrasts persist across
deduplication choices, conditional on the secondary transcription and crosswalk.
This is additional evidence, not a recovered primary joint table. The W002 reverse
mapping is ambiguous between M099 and M100, and rare jar variants lack broad support.

Run `python scripts/analyze_context_bounds.py`. The tests exhaust all event/context
set intersections in a small population, check the mixture bound against its
extreme allocations, and verify the source totals and Mohenjodaro arithmetic.
