# Sign families: contextual information without invented readings

**The source catalogue's sign families do not justify automatically merging their
members.** Some variants have reproducible context associations, but the overall
predictive gain is small and sensitive to smoothing and weighting. Conversely,
failure to predict a rare variant does not prove that it is equivalent to another.
No allograph set, meaning, or sound is established by this analysis.

An *allograph* is a different written form of the same underlying sign. Both
contextual allographs and genuinely different signs can have predictable contexts.
This is why distributional similarity alone cannot decide the question.

## Coverage of the whole inventory

The pinned feature catalogue has **76 entries linking multiple Wells identifiers**.
They are treated as candidate families, not accepted equivalence classes. All
original inscription identifiers are retained. Nine families have only one member
observed in the strict transcription subset. Twenty meet the descriptive support
gate: at least twenty occurrences, including at least two variants with five or
more occurrences each. This gate is not a statistical significance threshold.

The [417-row evidence index](../results/sign_family_index_417.csv) covers every
supplied Mahadevan sign, retaining its direct primary-catalogue profile:

| M-index coverage | Rows |
|---|---:|
| Linked to a source family meeting the support gate | 31 |
| Linked to a source family with insufficient support | 73 |
| No multi-W family asserted by the source mapping | 313 |
| Total | 417 |

These are **mapping-coverage counts**, not 31 independently identified M signs.
Some source entries link several M signs and several W signs without identifying
each correspondence. The family-level result cannot be assigned uniquely to every
member of that many-to-many mapping. All 417 meanings and sounds remain explicitly
undetermined; absence of a tested family does not erase other positional evidence.

## What the model is allowed to know

The prediction task is deliberately limited: given the source family, predict
which exact W member occurs at a position. It does not predict the family, a word,
or a language. The three models add information in this order:

1. Frequency of each member within its family.
2. Site, object type, exact inscription length, and file-order position class.
3. The immediately neighboring signs, with candidate-family members represented
   by temporary family labels.

The input contains 2,914 strict rows, reduced to 2,898 distinct
artifact/sequence/site/type units. All source IDs remain in the
[grouping ledger](../results/family_group_folds.csv). Repeated artifacts and texts
that become identical after family substitutions are joined transitively into
1,497 connected groups. Each group belongs to just one test fold. Thus a text
differing from a training text only in a proposed family variant is not counted
as a new test example. This is stricter than merely separating literal duplicates.

There are five folds with 1,197, 406, 443, 403 and 449 units. One connected group
contains 834 units; the resulting imbalance is reported rather than broken apart
to manufacture independent samples. The twenty supported families contribute
2,283 predicted tokens in 925 groups. Predictions for the other families are also
saved, but are not promoted into the supported-family aggregate.

For family member x, a half-count prior gives

```
p0(x) = (n_family,x + 0.5) / (N_family + 0.5 K)
pM(x) = (n_metadata,x + alpha p0(x)) / (N_metadata + alpha)
pN(x) = (n_neighbors,x + alpha pM(x)) / (N_neighbors + alpha)
```

K is the number of catalogue members. Counts use training folds only. Each
expression sums to one over those members, including unseen variants. The local
context model pools across metadata and smooths toward its metadata prediction;
this is a predictive baseline comparison, not complete control of confounding.
Neither the target variant nor its raw code appears in its context features.

## Results and their sensitivity

At the specified headline smoothing strength of twenty, average test loss is
1.293 bits per token for family frequency, 1.237 for metadata, and 1.216 with
neighbors. Lower loss means better prediction. The added neighbor information
therefore improves prediction by only **0.0217 bits per token** on this task.

| Smoothing strength | Neighbor gain over metadata | Component bootstrap 95% interval |
|---|---:|---:|
| 5 | 0.0145 | -0.0287 to 0.0622 |
| 20, specified headline | 0.0217 | 0.0002 to 0.0421 |
| 100 | 0.0105 | 0.0032 to 0.0165 |

These intervals resample connected groups with fixed predictions and fixed family
selection. They do not account for all source error, model selection, or unknown
scribal/chronological dependencies. They are not family-specific significance
tests or evidence that any candidate grouping is an allograph set.

After inspecting group sizes, an additional weighting check was added. The largest
selected group contributes 275 target tokens. Excluding it reduces the headline
gain to 0.0110 bits; giving each component equal weight reduces it to 0.0062 bits.
At strength five, both alternatives make the gain negative. Training is unchanged
in this check. The modest aggregate advantage is therefore not uniformly robust
across these choices.

At strength twenty, ten supported families gain and ten lose predictive accuracy
when neighbors are added. Three have positive gains in all five folds: P004
(source description: burden-carrying figure), P230 (pincer-like form), and P364
(tree-decorated leaf). These are **exploratory image-review priorities**, selected
after seeing results, not three proven distinctions. For comparison, P186 loses
0.249 bits per token and P316 loses 0.030; failures remain in the
[complete 76-family summary](../results/sign_family_summary.csv).

## Exact substitutions constrain possible roles

Across all candidate families, 23 have at least one exact one-position substitution
frame, totaling 63 family/frame instances. These witnesses show that variants can
occur with identical surrounding text. For example:

```
W740 W176 W233 W803
W740 W176 W233 W806
```

Both are present in the transcription and differ only in a P364 member. This is
substitution compatibility, not synonymy. A list of different people's names can
also occupy an identical grammatical frame. Five family/text instances contain
different members together; co-occurrence likewise does not by itself disprove
contextual allography. Every witness is retained in the
[full audit](../results/sign_family_audit.json).

One post-analysis photograph check illustrates the source limit. The first pair
above occurs on K-62 and M-503. Both were located in the downloaded CISI volume 1,
on printed pp.310 and 126 (PDF pp.346 and 162). K-62's original and impression are
clear, but the M-503 reproduction is too degraded to authenticate the fine W803/W806
distinction confidently. The source itself labels M-503's condition Poor despite
complete preservation. The [visual review ledger](../data/processed/sign_family_visual_review.json)
therefore records **insufficient verification**, not a confirmed primary minimal
pair. Neither source code was changed. A clearer photograph or independent drawing
is needed before treating this witness as an authenticated graphic contrast.

## Consequences for an account of all signs

A reasonable whole-system account must preserve the observed distinctions until
there is evidence for specific mergers. Some context-sensitive variation could
belong to one underlying sign; some could encode distinct content or modifiers.
The current analysis cannot partition the inventory reliably between those cases.
The supported statement is that the inventory combines graphic similarity with
uneven contextual differentiation. A rule equating every similar form, or assigning
each one an unrelated word, would outrun the evidence.

The study of allographs is a recognized research problem; see the public abstract
of [Daggumati and Revesz (2021)](https://digitalcommons.unl.edu/mechengfacpub/563/).
Their proposed mergers are not imported, and this is not a replication of their
method. No additional file was downloaded for this analysis.

Reproduce with `python3 scripts/analyze_sign_families.py`. The
[protocol](../data/processed/sign_family_protocol.json) states the exploratory
status, the [script](../scripts/analyze_sign_families.py) implements the models,
and the [tests](../tests/test_sign_families.py) check leakage grouping, normalization,
target exclusion, ambiguity handling and duplicate-frame counting. The
[token-level predictions](../results/family_token_predictions.csv) retain every
held-out score for all three smoothing strengths. The full offline pipeline runs
this analysis automatically.
