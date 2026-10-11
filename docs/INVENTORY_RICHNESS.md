# Inventory richness: what the rare signs support

10 October2026. **The audited primary M77 counts give a basic Chao1 diagnostic of550.45 sign types and Good–Turing unseen token mass of0.84%. These do not establish the true historical inventory or identify a logosyllabic script.** They are plug-in calculations under sampling assumptions not established for this archaeological catalogue.

| Primary Table I quantity | Value |
|---|---:|
| Sign occurrences N | 13,372 |
| Observed normalized sign types S | 417 |
| Types occurring once f1 | 112 |
| Types occurring twice f2 | 47 |
| Good–Turing unseen token mass f1/N | 0.00837571 |
| Chao1 inferred unseen types f1²/(2f2) | 133.4468 |
| Chao1 total S+f1²/(2f2) | 550.4468 |

Input is the existing primary [Table I transcription](../data/processed/mahadevan_1977_table_i.csv), validated again against all printed totals and frequency bands. This uses all417 catalogued signs, not the partial sequence corpus or a converted W-code inventory.

## Methods and interpretation

Good–Turing estimates the probability mass of unobserved classes, not their count. The primary statistical paper defines its model using independent identically distributed samples. [Drukh & Mansour2005, §1.1–1.3](https://jmlr.org/papers/volume6/drukh05a/drukh05a.pdf).

Chao1 is a lower-bound richness estimator under its sampling model, not a guaranteed statement that at least550 signs existed. For f2>0 we use S+f1²/(2f2); the source's f2=0 fallback is S+f1(f1−1)/2. Finite-sample rarefaction computes the expected number of observed types in a smaller random subset without replacement. [Gotelli & Chao2013, pp199–200, equations2 and7](https://www.uvm.edu/~ngotelli/manuscriptpdfs/Gotelli_Chao_Encyclopedia_2013.pdf). Both equation pages were visually checked; downloads and headers are retained in data/raw.

A small unseen *mass* can coexist with many unseen *types*, if each has very small probability. The two headline figures are therefore not contradictory. Neither quantity assigns a sound or meaning.

If the target is the closed M77 codebook, its size is417 by definition. The Chao1 calculation instead concerns a hypothetical larger population that could yield additional, consistently classified signs. It does not imply hidden entries in the existing codebook.

## Sensitivity and checks

112/417=26.86% of the observed classes are singletons. These classes drive the entire Chao1 gap of133.45. A singleton may be a genuinely rare sign, a normalization decision, or a reading problem; frequencies alone do not distinguish those explanations. Removing every singleton is an extreme hypothetical recoding/error scenario, not a proposed correction: it leaves305types/13,260tokens and makes the inferred unseen gap zero.

Copying every token once synthetically leaves417 types and identical relative frequencies but gives f1=0 and f2=112; Chao1 then returns417 and Good–Turing returns zero. This is only an illustration of non-invariance to count duplication, **not evidence about the actual extent or direction of archaeological duplication bias**. The informative future comparison is to recount an independently grouped, deduplicated corpus. Aggregate Table I counts cannot reconstruct those groups.

A permutation of all sign labels leaves every reported statistic unchanged. Thus these summaries cannot by themselves distinguish any proposed mapping of the417 signs to sounds or meanings. Positional strata are also saved, but their differing sample sizes, overlapping inventories and different conditional populations prevent treating their estimates as additive totals or a ranking.

The [rarefaction figure](../results/inventory_rarefaction.pdf) and [numerical curve](../results/inventory_rarefaction.csv) describe random token subsets of the existing catalogue. The curve ends at417 because all catalogued occurrences are then included. It is not chronological growth, an extrapolation to future finds, or a comparison with another script. No archaeological confidence band is asserted.

![M77 finite-catalogue rarefaction](../results/inventory_rarefaction.png)

Independent checks include exhaustive enumeration of all subsets of a toy population, boundary checks, monotonicity, and the exact identity S(N)−S(N−1)=f1/N at the full primary sample size. The latter was suggested by a tools-disabled Claude Fable second opinion and then tested directly.

## External second opinion

Requested CLI alias `fable` resolved to `claude-fable-5-1`. [Prompt](../results/claude_code/oct10_inventory_review_prompt.txt) and [full response](../data/raw/inventory-oct10-claude-fable.json) are retained. Fable confirmed the arithmetic, recommended the terminal-increment check and stressed the limited interpretation of synthetic duplication. These points were incorporated. Its suggestions that real duplication probably spares singleton classes and that this inventory lies between typical syllabic and logographic sizes were **not adopted as verified facts**: neither was demonstrated from matched data in that review. Its request for equal-size positional comparisons is treated as a sampling-design caution, not a theorem that asymptotic estimators can never be compared at unequal sample sizes. Model agreement is not independent historical evidence.

## Reproduction and next inference

```sh
python -m pip install 'reportlab>=4,<5'
python scripts/analyze_inventory_richness.py
python -m unittest discover -s tests -p 'test_inventory_richness.py'
```

The script uses standard-library arithmetic and ReportLab for the chart. It writes [machine-readable results](../results/inventory_richness.json), source hashes, the complete frequency spectrum, rarefaction CSV and an embedded-font PDF. No random seed or fitted base is used. Tests reject extrapolation beyond the observed token count.

To test a script-type hypothesis, acquire known-script frequency data with explicit tokenization, normalization and sampling units; match sample sizes or coverage and quantify uncertainty. A syllabary with variants, a mixed writing system and a restricted nonlinguistic repertoire can overlap in observed inventory statistics. No such comparator analysis is claimed here. Continue the verified M77 corpus so that duplicate, region, object and phase effects can eventually be examined instead of assumed away.
