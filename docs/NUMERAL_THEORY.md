# A fixed class order cannot cover every contiguous tally run

**The literal corpus contradicts a universal fixed-order numeral-field grammar.**
This is a test of an explicit extension made here: every contiguous tally-like run
is one numerical field whose graphic classes have a fixed order. It is not a test
of all numeral systems, nor a claim that a published proposal requires this rule.
Order-free addition, multiple adjacent fields, and context-dependent sign roles
remain alternatives. None acquires a verified numerical meaning from this test.

**Primary follow-up:** [three normalized catalogue drawings](NUMERAL_PRIMARY_FOLLOWUP.md)
now corroborate both orders and a returning long–short–long pattern. M-160 also has
a checked seal/impression photograph. Two proposed CISI crosswalks remain incomplete;
the observations can instead be cited directly under their Mahadevan text references.

## Protocol and denominator

The [protocol](../data/processed/numeral_theory_protocol.json) was saved after an
exploratory listing of runs. It is not preregistered or a held-out prediction.
The main classes are inherited from the [two-marker screen](NUMERAL_SCREEN.md):
long W031–W039, short W001–W007, and operationally stacked W012–W019. This inherited
classification is not a new visual authentication. W900, W020, W025–W029, modified
signs, and every other code remain unassigned. They break runs; no intervening sign
is skipped. The test assigns no stroke magnitude or numerical value.

Of 2,691 source rows containing a literal member, 1,719 pass the existing complete,
unambiguous, single-line R/L filters and 972 are excluded. Completeness here is the
source's transcription flag, not necessarily undamaged physical preservation.
Every failure and every retained run is saved. There are 1,904 runs, including 208
with at least two signs. Removing repeated full texts gives 1,221 runs, of which
186 contain multiple signs. These are the informative denominator below; one-sign
runs necessarily fit every class order. There are 59 distinct multi-sign patterns.

A conservative sensitivity restricts long to W031–W035 and stacked to W012–W013,
whose graphic descriptions are explicit in the saved catalogue features. W014–W019
then become run boundaries rather than silently reassigned short strokes. A separate
direction sensitivity admits L/R-labelled texts by removing only that exclusion;
it never repairs damage or reverses a row. All orders are enumerated, so a uniform
reversal of every text cannot remove the contradiction.

## Exhaustive order comparison

Repeated occurrences of the same class are permitted. Test all six orders of
three distinct classes, then both orders when stacked shares either long or short
rank. The table reports the **fewest** failures across all orders in each family,
with counts deduplicated by full text and run position. Choosing the best order on
these data is deliberately favorable to the hypothesis, not predictive validation.

| Model | All eligible | Fair/Good/Fine | Good/Fine |
|---|---:|---:|---:|
| Three distinct classes | 26/186 | 22/149 | 12/89 |
| Stacked shares long rank | 23/186 | 19/149 | 11/89 |
| Stacked shares short rank | 31/186 | 25/149 | 15/89 |

The best distinct-class order is stacked, long, short in source-file order. The
best two-rank order is long, short. No tested order fits all rows. With artifact,
full text and position deduplicated instead, the corresponding all-condition
failures are 27/206, 24/206 and 32/206. These are descriptive counts, not independent
sampling trials or estimated error probabilities. The condition filters trim spaces
and compare exact labels without treating Fair as Good. Among the 1,719 eligible
rows, source labels are Good 582, Fine 52, Fair 578, Poor 503 (including two with
trailing spaces), `?` 3, and `-` 1. Thus the condition selections contain 1,212
rows for Fair/Good/Fine and 634 for Good/Fine, before run extraction and deduplication.

The conservative membership sensitivity still has at least 24/153 failures for
three classes and 23/153 when stacked shares long rank. Restricting that conservative
sample to Good/Fine leaves 12/77 and 11/77 respectively. Adding L/R records also
preserves failure. Thus poor-condition records, a handful of inherited graphic
assignments, duplicate export rows, and the R/L-only screen do not individually
explain the universal mismatch. Source transcription errors remain possible.

## Explicit witnesses and what they prove

Two Good-condition Mohenjo-daro stamp-seal records contain the same pair of codes
in opposite orders:

| Artifact; local row | Literal full text |
|---|---|
| M-160; 2686.1 | `+151-243-031-002-820-741+` |
| M-678; 3116.1 | `+740-752-006-503-236-806-002-031-502+` |

Both have source type SEAL:S and direction R/L. Their W031–W002 and W002–W031 runs
require opposite ranks if both are single ordered fields. Site and recorded object
type alone cannot resolve this pair. These are **secondary transcription witnesses**;
no new photograph check authenticates either code sequence. The machine-readable
result finds reversed pairs within site/type automatically and retains their IDs.

Fair-condition M-1745 (2393.1) contains `+368-821-055-031-002-031-892+`.
Its long–short–long run fails either strict rank order even considered alone.
A changed orientation cannot fix a return to the starting class. It could instead
be multiple fields, or contain a nonnumerical use of a stroke sign; neither reading
is established by the failure.

For a fixed rank order, a boundary is necessary at every adjacent rank descent.
Cutting at all such descents makes every remaining segment monotone, proving that
the number of descents is the exact minimum number of additional boundaries.
The script saves that number for every order. These are conditional mathematical
bounds, **not recovered ancient word or numeral boundaries**. Tests compare the
calculation with exhaustive partitions of every three-class sequence through length
five.

As a surviving countermodel, addition of fixed per-sign values is invariant under
permutation. Hypothetically taking W031 as 10 and W002 as 16 assigns both opposite
pairs 26 and the returning triple 36. This only demonstrates why an order failure
does not refute addition or identify actual values. Any other additive assignments
are equally unaffected by reordering; no independent contents count was supplied.

## Saved work and consequence

Run `python3 scripts/audit_numeral_theory.py`. The
[script](../scripts/audit_numeral_theory.py),
[full audit](../results/numeral_theory_audit.json),
[208 multi-sign run witnesses](../results/numeral_theory_runs.csv), and
[five tests](../tests/test_numeral_theory.py) preserve the evidence and calculation.
The existing pinned corpus was used; no new data were downloaded.

A numerical decipherment must specify which adjacent strokes belong to the same
field and whether their order carries value. A single global fixed order cannot be
assumed from their tally-like appearance. This constrains one grammar choice;
it does not establish or rule out numerical uses of these signs elsewhere, and
it assigns no meaning to the remaining inventory.
