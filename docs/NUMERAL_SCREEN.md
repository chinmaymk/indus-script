# Corpus coverage of a proposed numerical equality

**A narrow numerical rule fits five of twenty candidate objects, but those five
contain only three distinct text pairs.** The remaining fifteen are outside the
strict parser's scope, not successful readings. Allowing the opposite direction
label admits one additional object whose two-versus-three strokes contradict the
rule for every positive long-stroke value. A subsequent photograph and catalogue
check corroborates its two-versus-three stroke pattern. The counterexample remains
conditional on the proposed numerical roles and equality between faces.

## What was tested

The [previous algebra](NUMERAL_EQUATIONS.md) left two candidates, `(L,S,v)=(10,8,6)`
and `(36,20,4)`, under its stated base bounds. We now test a fixed, local extension
of the two-face interpretation in Figure 16 of
[Fuls (2020)](https://www.academia.edu/41952485/Ancient_Writing_and_Modern_Technologies_Structural_Analysis_of_Numerical_Indus_Inscriptions).
It is **not** an implementation of the author's complete, context-dependent
numerical proposal. The protocol was written after an exploratory scan; there is
no preregistration or held-out validation claim.

Every group containing literal W700 and W840 enters the denominator. Groups use
the local identifier prefix, with consistent CISI identifiers required. The rule
requires each marker exactly once on different faces. Both faces must pass the
existing complete, unambiguous, single-line, R/L transcription filters.

For each marker, collect maximal contiguous runs of recognized candidate numerals
on both flanks. Do not skip intervening signs. The recognized classes are W031–039
(long strokes), W001–007 (short strokes), W012–019 (stacked strokes), and W900.
Long and stacked stroke counts multiply L; short stroke counts multiply S; W900
contributes v. Add the two flanks, then compare the sums across faces. Other signs
are retained explicitly as **uninterpreted residuals**. Neither their meaning nor
their irrelevance to quantity has been established.

The [protocol](../data/processed/numeral_screen_protocol.json),
[complete machine-readable results](../results/numeral_pair_screen.json), and
[44 literal source rows](../results/numeral_pair_source_rows.csv) preserve every
candidate, failed quality check, extracted run, coefficient and residual sign.
No proposed translations are imported. No additional data were downloaded.

## Results, including denominators

| Object | Extracted equality required by main rule | Result |
|---|---|---|
| H-1923 | 2L = 2L | Identity; no value constraint |
| H-326, H-924, H-925 | 3L = 3L | One repeated text pair; no value constraint |
| H-904 | 3L + v = 2L + 2S | Both candidates satisfy the same existing equation |
| H-306, direction sensitivity only | 3L = 2L | Fails for every L > 0 |

Strict selection admits **5/20 objects (25%)**, with three distinct complete text
pairs. Both candidates balance all five. Four of those equalities are identities;
the fifth reproduces the equation already used in candidate construction. Thus the
screen adds no numerical constraint distinguishing the two candidates. Five fits
must not be presented as five independent predictions of the numerical key.

The fifteen excluded objects comprise seven with damaged or otherwise incomplete
marker faces, six without a recognized adjacent numeral at W840, one with repeated
W700, and H-306 with an L/R-labelled face. Exact overlapping exclusion reasons are
saved. Stopping at an unrecognized sign does not show that sign is nonnumerical.
H-771, for example, has W032 separated from W840 by W257; the parser cannot simply
jump over W257 to manufacture a numerical expression.

H-904's local rows are 1786.1 and 1786.2, with excavation identifier `J213 (D)477`.
Their numerical pattern matches the paper's example labelled 3786. This is a
**proposed crosswalk**, stronger than joining bare integers but still requiring
artifact-image verification. The original local 3786.1 identifies M-1540. Neither
record is renamed. H-904 also contains W740, W645, W368 and W817, which this screen
does not explain.

## Two sensitivity checks

**Direction.** Flanking addition is unchanged when a complete sequence is reversed.
Allowing L/R as well as R/L, without relaxing completeness or other filters,
therefore gives a useful check. H-306 then enters, raising eligibility to 6/20.
Both candidates balance five and fail one. Its residual is exactly L, so changing
bases cannot fix it while keeping the rule and L positive. Transcription errors,
different relations between faces, and omitted contextual distinctions are possible;
none has been demonstrated. Direction alone is not an arithmetic explanation.
See the later [image audit](NUMERAL_IMAGES.md) for corroboration of the stroke counts.

**Stacked-stroke scale.** Assigning each stacked stroke one instead of L makes all
three copies of the H-326 pattern fail for both candidates, leaving 2/5 strict
matches. The main model's treatment of W013 is therefore consequential, not a
meaning obtained automatically from its three visible strokes. This experiment
does not rule out context-specific positional notation; it shows why those rules
must be specified and independently tested.

## Consequence for the decipherment

The universal claim that these two markers always label equal quantities under
this fixed additive rule is unsupported. Its direction-expanded version has a
literal counterexample, and the strict fits provide no new identification of the
base values. A conditional numerical interpretation remains plausible for a
subset of inscriptions. Extending it to all signs would require additional rules
and independent evidence; adding an exception for each mismatch would not supply
that evidence.

Reproduce with `python3 scripts/screen_numeral_pairs.py`. The
[tests](../tests/test_numeral_screen.py) check that the parser retains the
counterexample and ambiguity, does not skip intervening signs, and never admits
damaged text through the direction sensitivity.
