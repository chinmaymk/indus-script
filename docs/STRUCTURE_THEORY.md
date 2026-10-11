# How much preceding context helps predict a sign?

**Two preceding signs provide a small predictive improvement over one in this
particular model; the evidence for additional first-sign memory is weak.** Most of
the apparent improvement from adding the first sign can be reproduced by merely
sharpening the shorter-context model. These results constrain predictive models,
not words, sounds, grammatical categories, or language identity.

This is a new exploratory analysis of the existing strict secondary corpus. Its
[protocol](../data/processed/structure_theory_protocol.json) was saved before these
outcomes were inspected, but after exposure to the project's earlier structural
results. A subsequent [calibration diagnostic](../data/processed/structure_theory_calibration_diagnostic.json)
was added after inspecting the initial results; that timing is preserved explicitly.
No additional data were downloaded.

## Models and evaluation

Each model predicts the exact next W identifier, conditional on known inscription
length and file-order position. All 998 possible W001–W998 identifiers retain
positive probability; no sign merger or reading is supplied.

The hierarchy starts with half-count-smoothed sign frequencies, then adds these
successive contextual count tables:

1. Exact length and position.
2. Previous sign, exact length and position.
3. Previous two signs, exact length and position.
4. First sign, previous two signs, exact length and position.

For every layer, with a contextual count c(x), support N, and preceding-layer
prediction p(x), the prediction is `(c(x) + alpha*p(x))/(N + alpha)`. All counts
come from training folds. An unseen context backs off exactly, with no fabricated
count. The headline alpha is 20; 5 and 100 are reported without selecting a winner.
The models are normalized distributions over the full declared inventory.

All comparisons of the last three layers use the **same 3,206 held-out tokens at
zero-based position 3 or later**. Thus the first sign is neither the target nor
one of its preceding two signs. Those tokens belong to 1,240 distinct texts,
1,124 connected groups, and 370 observed W target types. A secondary result for
the two-versus-one comparison also includes position 2, totaling 4,793 tokens.
This is not a test of every sign in every position; short texts and early tokens
cannot provide the required context.

The 2,914 strict rows yield 1,848 distinct texts in 1,564 components. Existing
transitive grouping joins the same artifact and exact whole text, and each
component stays in one of five deterministic folds. Four folds train and one is
scored, without hyperparameter tuning. Every distinct text is counted once.
Near-duplicates, workshop relations and unidentified artifact aliases may remain
across folds. Deduplication also changes the ancient frequency distribution.

A sensitivity analysis partitions every contextual key by the complete set of
site/type pairs recorded for that distinct text. This controls those observed
labels within the model at a cost in sparse support. It is not causal adjustment,
and the multi-site/type set representation is not a claim of identical provenance.

Intervals are 1,000 connected-group bootstrap resamples of fixed predictions.
They do not include refitting, transcription error, model-selection uncertainty,
or full archaeological sampling uncertainty. These exploratory intervals are not
formal conditional-independence or Markov-order tests.

## Results

Positive gain means the longer-context model has lower held-out log loss, in bits
per predicted sign. Common eligible positions are used throughout this table.

| Alpha | Two preceding signs over one | First sign beyond preceding two |
|---|---:|---:|
| 5 | −0.01709 [−0.02796, −0.00633] | −0.02946 [−0.03489, −0.02402] |
| 20 | 0.02290 [0.01570, 0.03054] | 0.00218 [−0.00095, 0.00575] |
| 100 | 0.02406 [0.01950, 0.02906] | 0.00834 [0.00609, 0.01107] |

At alpha 20, two-sign context improves in all five test folds, with average loss
falling from 6.85770 to 6.83480 bits. Giving each component equal weight reduces
the gain to 0.01294; excluding the largest component gives 0.02314. Restricting
contexts additionally by site/type gives gain 0.01178 [0.00700, 0.01748]. Using all
positions eligible for two-sign context gives 0.02660 [0.01753, 0.03569].

However, alpha 5 reverses the aggregate advantage. The extra context is therefore
not uniformly beneficial across reasonable smoothing choices. Its positive
performance at stronger smoothing supports retaining some short combinations as
predictive features, without establishing a uniquely correct segmentation into
words or units.

## Why sharpening matters

Adding a count layer can change calibration even when its extra sign supplies no
new target composition. The post-result diagnostic replaces a child context's
empirical distribution with the empirical distribution of its parent, while
keeping the child support N and alpha fixed:

```
p_control(x) = (N_child * c_parent(x)/N_parent + alpha*p_parent(x))
               / (N_child + alpha)
```

When no parent context is observed, the control backs off to the parent prediction.
This control cannot differentiate target compositions using the added sign. Its
support count can still depend on that sign, so it is only a specific calibration
comparison, not an exhaustive independence null.

At alpha 20, the actual two-sign model improves on this sharpening control by
only **0.00734** bits [0.00362, 0.01121], rather than the original 0.02290. With
site/type keys, the residual gain is 0.00271 [0.00070, 0.00491]. This leaves a small
context-specific advantage under these modeling choices.

The first-sign model's gain over its own sharpening control is **0.000237** bits
[−0.000570, 0.001084]. All three alpha choices have intervals spanning zero for
this contrast; the site/type sensitivity does too. Consequently the original
first-sign gains do not provide a convincing additional remote-dependency finding.
Failure to find one is not proof that long-range dependencies are absent: the
chosen keys are sparse, and other representations or better data may recover them.

## Controls and counterexamples

At alpha 20, the same procedure applied to nonlinguistic weather icons gives a
two-context gain of **0.03435** bits, and 0.03139 over the sharpening control.
Thus even a positive longer-context finding does not identify linguistic writing.
The control is not matched to the Indus inventory or archaeological sampling and
cannot establish which corpus has more language-like structure.

Three reproducible synthetic generators use eight symbols, length eight, 6,000
rows, 80% prescribed transitions and otherwise uniform random draws. Exact texts
are deduplicated and grouped as in the source analysis; the reported measurements
therefore concern their deduplicated outputs, not their original sampling law.

| Generator | Two-over-one gain | First-over-two gain |
|---|---:|---:|
| Next sign depends on previous one | −0.01095 | −0.06789 |
| Next sign depends on previous two | 1.25427 | −0.00569 |
| From position 3, next sign also depends on first sign | −0.06498 | 0.52149 |

These controls show the method can recover large planted dependencies and does
not automatically reward more context. They do not measure power for subtle
Indus effects with its larger inventory, shorter texts, missing data, and source
uncertainty. The remote-memory generator is itself an explicit nonlinguistic
construction with a strong long-range effect.

## Reproduction and retained evidence

Run `python3 scripts/analyze_structure_theory.py`. The
[script](../scripts/analyze_structure_theory.py) writes the
[complete summary](../results/structure_theory.json) and twelve token-level ledgers
named `results/structure_theory_{dataset}_{alpha}.csv`. Each score retains source
IDs, artifact IDs, connected group, fold, full literal sequence, position, target,
metadata and all model/control losses. In particular,
[the headline Indus ledger](../results/structure_theory_indus_20.csv) exposes every
contributing prediction.

Five [unit tests](../tests/test_structure_theory.py) check target/future exclusion,
probability normalization including unseen contexts, transitive duplicate/artifact
grouping, exact backoff and deterministic controls. The source transcriptions are
not authenticated by these software tests.

The defensible new constraint is modest: a model using only individual sign slots
or isolated adjacent pairs leaves some recoverable combination information, but
this analysis does not support assigning lexical boundaries or specific distant
syntax. All candidate readings still require independent semantic anchors.
