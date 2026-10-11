# Vessel capacities: a conditional positive result and its limits

**The selected three-pot group supports a local count–size hypothesis. It does not
establish a universal unit or decipher a word.** This is conditional on the earlier
Fuls table recovered as public text, whose layout and conflicting excavation
identifiers still require authentication. See the [source recovery](CAPACITY_TABLE_FOLLOWUP.md).

## What the photographs establish

The saved CISI1 photographs show seven strokes on H-370 (printed233/PDF269),
six plus a U-shaped sign on H-371, and three plus a U-shaped sign on H-372
(printed234/PDF270). Their catalogue identities were checked on printed372/PDF408.
These observations corroborate the stroke counts, not the capacities. The catalogue
and Fuls extracted table disagree on excavation numbers; no values were reassigned.

K-90's photograph (printed319/PDF355) shows two rim strokes and a separate body
inscription. A black/white bar appears below the whole-vessel image, but its length
is not numerically labelled on that page. The claimed 30cm scale is still unresolved.
The [visual ledger](../data/processed/capacity_primary_review.json) records all locators.

## Conditional calculations

For each geometry separately, fit V = u n by minimizing squared volume residuals,
where n is the visible stroke count. This assumes proportionality and a zero
intercept; larger counts receive greater influence on u. Also fit on two pots and
predict the third. The three geometries reuse the same vessels and measurements.

| Geometry | Fitted litres/stroke | Individual litres/stroke, range | Largest absolute leave-one-pot-out error |
|---|---:|---:|---:|
| Sphere | 41.63 | 41.20–41.84 | 1.16% |
| Ellipsoid | 41.38 | 39.60–43.18 | 6.76% |
| Profile | 40.35 | 40.10–40.54 | 1.02% |

This is a positive association within three selected objects, under every listed
geometry. The profile model is particularly close; choosing it does not make the
capacity directly measured. The ellipsoid alternative is less uniform. These
ranges summarize differences among pots under each geometric model, not measurement
confidence intervals.

For transparency, the script enumerates all six permutations of the three counts
against each fixed volume vector. The published pairing ranks first in each case.
This is descriptive: the objects and hypothesis were already selected, so no valid
discovery significance level follows. Internal leave-one-out does not undo that
selection or supply new archaeological evidence.

## Applying the same constant to other reported objects

Freeze the profile fit at 40.353 litres/stroke without refitting to each object:

| Object | Assumed strokes | Reported modeled capacity | Prediction | Prediction error |
|---|---:|---:|---:|---:|
| H95-2661 | 4 | 88.3 L | 161.4 L | +82.8% |
| MD-1374 | 6 | 138.84 L | 242.1 L | +74.4% |
| K-90 | 2 | 103.0 L | 80.7 L | −21.6% |

All three geometry calibrations show the same direction of mismatch. MD-1374's
six counts combine three vertical and three slanted strokes, whose equal value is
an assumption. MD-1374's original scaled profile has not been checked here.
The [bounded primary-source search](MD1374_SOURCE_FOLLOWUP.md) records that access
gap and an unverified catalogue-number lead; no similarly numbered corpus row was
silently substituted for the cited vessel.
A [subsequent H95-2661 profile trace](H95_PROFILE_CAPACITY.md) from the excavator's
published drawing gives about86L and preserves uncertainty in the rim count.
It also confirms a separate body inscription; this is not a tally-only vessel.
K-90 additionally depends on the unresolved photographic scale and is not
a decisive counterexample. These objects were already discussed in the source;
this is a transfer check, not a blind prediction on newly discovered artifacts.

The source itself considers multiple units. Thus the mismatches constrain the
extension of this particular constant; they do not refute quantity notation,
different units, different commodities, or counts unrelated to capacity. Those
alternatives need independently identified conditions to predict which rule applies.
Choosing a separate unit after seeing each volume would fit without explaining it.

## Consequences for decipherment

The reasonable partial conclusion is that repeated strokes on these selected pots
may record an amount related to size. Capacity, contents, batch size and intended
load remain distinct possibilities. The analysis cannot identify the U-shaped sign,
a commodity, unit name, language or sound. Multiplying every proposed numerical
value by a constant while dividing the inferred unit by the same constant leaves
the fit unchanged; the [scale proof](QUANTITY_ANCHORS.md) still applies.

The next discriminating evidence is a checked measurement table joined by secure
artifact identifiers, followed by independently scaled vessels with comparable
stroke forms and a rule for unit classes fixed before their capacities are inspected.

## Reproduction

- [Calculation script](../scripts/analyze_capacity_models.py)
- [All fits, errors, permutations and transfer predictions](../results/capacity_model_audit.json)
- [Source cells and retrieval limitations](../data/processed/capacity_table_followup.json)
- [Tests guarding scale invariance and held-out leakage](../tests/test_capacity_models.py)

Run `python3 scripts/analyze_capacity_models.py`, or the full offline pipeline.
Inputs are explicitly provisional; no source values are inferred from the fit.
