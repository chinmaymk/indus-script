# Exact support of the ending-rectangle shuffle

Date: 2026-10-10. **Release 5 has zero observed rectangles, but two-sign rectangles are now possible under the specified shuffle.** One-sign rectangles remain impossible. This update changes the support diagnosis; it establishes neither statistical power nor a significant or linguistic result. Further ending-screen exploration is deferred for the finite motif-transfer route.

## Current release 5

The [release-5 certificate](../results/ending_support_v5.json) uses 198 corpus rows, of which 154 are clean and 153 have distinct sequences. Both starting bases have 146 eligible slots at k=1 and 137 at k=2. At k=1 only one stem has multiple slots, so no rectangle is possible. At k=2 seven stems have multiple slots, and the certificate finds 33 individually feasible stem-pair/ending-pair combinations in each basis. All observed four-cycle counts remain zero. The 33 are possible individual rectangles, not observed examples, a maximum simultaneous score, independent witnesses, or a probability.

For a concrete k=2 support witness, stems `M267 M099` and `M391 M099` can both receive endings `M104 M162` and `M124 M342`: each ending has at least two copies in their common total-length-4 stratum. The certificate asserts that a permitted reassignment can realize those four edges; it does not assert that the corpus attests the rectangle. No new Monte Carlo analysis was run for this documentation update.

## Historical releases 3 and 4

On verified M77 release 3, **every permitted permutation has zero four-cycles**, for both ending lengths and both starting bases. Running more shuffles cannot change that historical result. This is a limitation of the statistic conditional on the observed marginals, not evidence against language or inflection.

The input is the final `data/processed/m77_verified/corpus_v3.json`, filtered by `clean_rows` in `scripts/analyze_kober_alternations.py`. Of 99 printed lines, 76 are clean and 75 have distinct sequences. Doubt, visible unidentified signs, loss, and reviewer uncertainty are excluded. Stored normalized order is retained. The result includes SHA256 pins for the corpus and both scripts.

## Exact criterion and proof

Fix an ending length k, either one or two signs. Every eligible sequence has a nonempty exact stem s and an atomic ending block e. Write n(s) for its number of fixed slots and C(L,e) for the multiplicity of ending e among input slots of total length L. A stem's length fixes its unique total-length stratum L(s) = length(s) + k.

A rectangle consists of two distinct stems s and t, and two distinct endings a and b, with all four combinations present. Such a rectangle occurs in at least one permitted shuffle **if and only if** some pair s,t satisfies n(s) >= 2 and n(t) >= 2, together with one of these conditions:

- If L(s) = L(t) = L, at least two distinct endings have C(L,e) >= 2.
- If L(s) differs from L(t), the two strata share at least two distinct ending blocks with positive multiplicity in each.

Necessity follows directly from the four required edges: each stem needs two slots; each ending needs two copies in the shared stratum or one copy in each separate stratum. For sufficiency, assign one a and one b to two slots of each stem. The stated inequalities ensure no ending multiplicity is exceeded. In each stratum, the unassigned slots and unused ending copies have equal totals, so fill those slots by any bijection with the remaining ending copies. The shuffle imposes no other restriction, and collisions are permitted. This constructs a valid permutation containing the rectangle.

The argument covers both repeated row slots and the deduplicated starting-sequence basis. Deduplication happens before shuffling; it is not a ban on repeated output sequences. A ban on output collisions or additional artifact/metadata constraints would define a different null and require a different proof.

The script enumerates all pairs of stems with two or more slots. For each it records eligible endings, the number of feasible distinct ending pairs, and one witness ending pair when available. The sum counts individually feasible rectangles. It is **not** a maximum simultaneous score, a probability, or a number of distinct shuffles. A positive certificate says only that some shuffle can contain a rectangle; it does not establish variability or useful statistical power.

## Release 3 result

| Ending length | Starting basis | Eligible slots | Stems with at least two slots | Rectangle possible in any shuffle |
| --- | --- | ---: | ---: | --- |
| 1 | Rows | 71 | 0 | No |
| 1 | Distinct input sequences | 71 | 0 | No |
| 2 | Rows | 67 | 3 | No |
| 2 | Distinct input sequences | 67 | 3 | No |

For k=2, the repeated stems are `M028` (total length 3), `M267 M099` (length 4), and `M391 M099` (length 4), each with two slots. The length-3 and length-4 strata share no complete two-sign ending block. The length-4 stratum has no ending block with two copies. Thus all three candidate stem pairs fail the necessary-and-sufficient criterion. The two starting bases give the same eligible slots because the one duplicated clean sequence is too short to enter either screen.

The previous Monte Carlo outcome is therefore exactly determined by preserved marginals for release 3. An exceedance fraction of 1 here cannot rank a morphological explanation against a label explanation. Additional corpus pages can alter these marginals and should be checked anew, without treating a newly feasible rectangle as a decipherment.

## Reproduction and validation

Release4 extends the corpus to132 rows,104 clean rows and103 distinct clean sequences. The exact conclusion is unchanged. At k=1 there are98 eligible slots and only one stem with two slots (`M267 M099 M124`), so no pair of eligible stems exists. At k=2 there are92 slots and the same three repeated stems as release3; `M267 M099` now has three slots. The length3/4 strata still share no two-sign ending block, and the length4 stratum still has no repeated ending block. All four certificates therefore force zero, with no additional random shuffles needed. [Release4 result](../results/ending_support_v4.json) pins the new corpus and the same scripts.

Operational stopping rule for this exact screen: check support before running more shuffles. While the certificate is negative, skip Monte Carlo significance calculations. Additional consecutive corpus pages can be checked without changing the ending lengths or grouping signs after seeing the data. A positive certificate would only reopen the question of whether the statistic varies and has useful power; it would not validate a linguistic interpretation or justify a significance claim by itself.

Run from the repository root:

```sh
python3 scripts/ending_support_certificate.py \
  --corpus data/processed/m77_verified/corpus_v3.json \
  --output results/ending_support_v3.json
python3 scripts/ending_support_certificate.py \
  --corpus data/processed/m77_verified/corpus_v4.json \
  --output results/ending_support_v4.json
python3 scripts/ending_support_certificate.py \
  --corpus data/processed/m77_verified/corpus_v5.json \
  --output results/ending_support_v5.json
python3 -m unittest discover -s tests -p test_ending_support_certificate.py
```

The five tests include exhaustive finite enumeration of every distinct allowed within-length permutation for all three-ending assignments over five small stem-slot arrangements (1,458 input cases across k=1 and k=2). These cover shared and different lengths, repeated slots, singleton stems, insufficient ending multiplicity, and deduplicated starting inputs. Further cases check distinct-ending thresholds, atomic two-sign blocks, empty input, and invalid ending lengths. The independent enumerator evaluates the actual existing rectangle statistic on every permitted result and compares existence to the certificate. All five tests passed.

No external data were downloaded. Results and proof address only exact whole-line stem/end matches under this specified shuffle; they do not establish word boundaries, historical grammar, sign sounds, sign meanings, or an Indus reading.


## 11 October: distinction from a uniqueness-conditioned null

The proof above remains exact for its declared collision-permitting shuffle.
The later [paired-ending review](COUPLED_ENDINGS_REVIEW.md) identifies a different
inferential requirement when observed texts are deduplicated: conditioning the null
on unique stem–ending edges. Impossibility under the larger collision-permitting
space also proves impossibility under that restricted space; the release-3/4 zero
support conclusions therefore persist. Conversely, release 5's 33 individually
feasible rectangles in the larger space do not prove attainability in the restricted
space. No prior observed count changes, and no prior shuffle is rerun here.
