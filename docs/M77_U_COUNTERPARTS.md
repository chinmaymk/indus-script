# What varies when the accompanying inscription stays the same?

**Twelve exact counterpart groups have different auxiliary stroke counts even
with object type and side/line layout held fixed.** Four groups span two, three
and four long strokes. This broadens the earlier three matched-context examples
into an exhaustive check of the226 catalogue references bearing227 clear
stroke-plus-M328 fields.

The result supports a recurring field whose graphic state can vary independently
of the included counterpart text. Quantity notation remains plausible. Category
labels remain compatible too; these data do not identify a numerical value, unit,
word, sound or language.

## Coverage and comparison

Primary review accounts for **237 other text-bearing lines** and28 symbol-only
entries on all226 selected references. Each side and line is retained separately;
no text is concatenated across surfaces. All selected fields are excluded from
their own counterpart bundles, including both fields on5413. “Counterpart” means
other textual entries on the same reference, not an inferred universal main side.

The counterpart transcriptions contain763 assigned glyph tokens across121 M sign
types. Twenty-six lines contain physical loss and23 contain primary doubt; five
lines have both. No reviewer-unidentified glyph remains in this newly checked
selection after close glyph comparisons. This does not reconstruct missing text
or remove primary uncertainty. The older U-bearing corpus still retains UNKNOWNs.

After excluding any reference with an incomplete, damaged or doubtful counterpart
bundle, **183 references with184 fields** remain:74 sealing references and109
miniature-tablet references. These form110 distinct counterpart/type/layout groups.
Twelve groups vary in stroke state; they contain64 catalogue references. Repeated
references, molds, casts and identical text types are not established independent
archaeological observations.

| Object class | Identical side1 counterpart, normalized order | Observed long-stroke counts | References in group |
|---|---|---|---:|
| Sealing | M136 M193 M342 | 2,3 | 2 |
| Sealing | M150 M123 M067 M244 M342 | 3,4 | 2 |
| Sealing | M175 M176 M211 M176 | 2,3 | 2 |
| Sealing | M391 M099 M040 | 2,3 | 2 |
| Miniature tablet | M048 M193 M342 M176 | 2,4 | 2 |
| Miniature tablet | M048 M342 M176 | 2,3,4 | 31 |
| Miniature tablet | M067 M244 M149 M342 | 2,3 | 4 |
| Miniature tablet | M072 M211 | 2,3,4 | 3 |
| Miniature tablet | M072 M216 M254 | 2,3 | 3 |
| Miniature tablet | M103 M403 M342 | 2,3,4 | 6 |
| Miniature tablet | M119 M087 M342 M176 | 2,3 | 3 |
| Miniature tablet | M287 M402 | 2,3,4 | 4 |

Every variable group in this table has its selected field on side2/line0. The
complete results retain side/line positions for all other groups too. For the
largest group, two references have two strokes,19 have three, and10 have four.
The second three-state group, `[M072 M211]`, is witnessed by4551(two),5496(three)
and4428(four). The one-stroke field remains in the complete census; its damaged
and doubtful counterpart at4491 excludes it from clean exact-context inference.

All226 candidate export strings match at least one newly assembled primary line.
That checks these strings against catalogue drawings; it does not establish which
side an export represents when equal strings repeat. Candidate strings suggested
some glyph IDs during review, so this is not a blind transcription-accuracy study.
The reviewers explicitly retained the primary printed damage and doubt.

## A finite-data proof and its limit

Let `x` be the complete positioned counterpart bundle, object class and selected
field layout. Let `y` be the tuple of auxiliary graphic stroke counts on that
reference. A deterministic model `y = f(x)` must give the same output to identical
inputs. Any group with two observed outputs contradicts that model on at least
one reference, conditional on the catalogue's object associations and readings.

If the observed output counts in one group are `n1,…,nk`, a single-valued map can
fit at most `max(n1,…,nk)` of its records. Its minimum exception count is therefore
`sum(n1,…,nk) − max(n1,…,nk)`. Summing over the110 eligible groups gives **27
reference exceptions**:4 on sealings and23 on miniature tablets. The audit retains
every witness rather than treating that number as a population error estimate.
It does not prove that a model with additional context, scribal variation or
latent categories is impossible.

Relabeling the graphic states2/3/4 as categoriesA/B/C preserves all these paired
observations. Thus the contradiction does not distinguish quantity from category,
let alone determine ancient pronunciations. A quantity reading needs an independent
amount, arithmetic relation or metrological anchor. The earlier physical-size
holdout did not supply such an anchor. Original direction, chronology, manufacture
and excavation context are not held fixed in every new group.

## Corrections exposed by the larger dataset

The new audit compares70 previously recorded counterpart observations:57 match,
nine resolve earlier UNKNOWNs, and four change earlier assigned glyphs. Independent
second reviews support the substantive changes:

- 4359/10: M178 → **M402**; a flag on one stem, not an A-like form.
- 4370/10: M216 → **M226**; only the upper branch terminal bends.
- 5323/10: M060 → **M071**; an internal straight stroke is visible in the wrapped fish.
- 5410/10: M178 → **M402**; the same stem/flag distinction.

Four carrying-person promotions were independently checked. M012 lacks the detached
inner-leg stroke that distinguishes M013; explanatory notes that reversed this
feature were corrected without changing accepted token IDs. All nine contexts
from the earlier dedicated paired-context review match the new readings.

A further combined-corpus check exposed a mistake in the earlier U recovery:
three apparent M280 occurrences exceeded its primary total of two. Primary glyph
inspection and the sign's own concordance resolve it. **3234/10 ends in M283**,
with an extra right-edge enclosed cell and oblique internal stroke. The M280
index onPDF544 lists5325/20 and4468/10; the M283 block spansPDF544–545 and includes
3234/10. The leading UNKNOWN on3234 remains unknown. No M328 count, position or
selected field changes.

The [correction ledger](../data/processed/m77_u_3234_primary_review.json) preserves
the former string, hashes and new evidence. Historical stage outputs remain
reproducible with their old reading; the **current corrected combined corpus** is
[data/processed/m77_primary_reviewed_contexts.jsonl](../data/processed/m77_primary_reviewed_contexts.jsonl).
It contains550 distinct reviewed lines,1515 assigned tokens and143 observed sign
types. All assigned counts respect the full primary marginal totals. The143 types
have contextual evidence here; the other274 of417 are not covered by this selected
corpus. Nothing in this coverage count constitutes a deciphered sign.

## Reproduction and evidence

Run `python3 scripts/run_all.py`, or the counterpart audit after its preceding
recovery and object-type stages. The [script](../scripts/analyze_m77_u_counterparts.py)
checks exact reference coverage, field exclusion, duplicate IDs, input/image
hashes, historical correction targets and primary count bounds. Six targeted
tests protect the inference and join rules. Results include every group, excluded
reference, comparison and witness in
[results/m77_u_counterparts.json](../results/m77_u_counterparts.json).

Primary reviews: [first76 references](M77_U_COUNTERPARTS_STRUCTURE.md),
[middle76](M77_U_COUNTERPARTS_NUMERALS.md), [last74](M77_U_COUNTERPARTS_ICONOGRAPHY.md).
The saved [protocol](../data/processed/m77_u_counterpart_protocol.json) acknowledges
prior matched examples and fixes the exhaustive selection. No raw downloads were
added. This remains a sign-selected historical catalogue census, not an unbiased
sample of all Indus inscriptions or a key for all417 signs.
