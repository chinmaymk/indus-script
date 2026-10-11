# Exact stem–ending alternation screen

The verified release 3 produces **zero shared ending-pair rectangles** for terminal blocks of either one or two signs. This is a sparse descriptive result, not evidence against language or morphology. There are no repeated eligible stems at the one-sign boundary; only three stems have alternative two-sign endings, and none shares the same ending pair with another stem.

“Kober-style” describes the user's historical inspiration for seeking repeated alternations. This operational screen is our own narrow precursor. It works on whole printed lines without established word boundaries; it does not implement linked penultimate/final alternations or infer a syllabic value grid. It is not a replication of Kober's full procedure or assumptions: an original method paper has not been acquired. No historical claim here depends on search snippets.

## Data and definition

Input: `data/processed/m77_verified/corpus_v3.json`, SHA256 `30008fc9d59c2ae81faa23d0b8ab67dc64d8f4d302588a2190853944fc2031c4`. These are 99 reviewed printed rows on PDF pages 50–52, not a representative sample of the Indus corpus. Verification concerns M77's printed transcription, not object photographs. Earlier structure work (`analyze_structure_theory.py`) tested predictive context; modifier audits used predefined plain/roof sign pairs. Neither establishes morphological readings. This screen instead searches exact terminal-block alternations without sign-family pooling.

Whole rows containing source doubt, `UNKNOWN`, `LOSS`, or reviewer uncertainty are excluded. That leaves 76 clean rows and 75 distinct sequences. Exclusion reasons overlap: 12 rows contain loss and 18 source doubt; 23 rows are excluded in total. The final corpus has no remaining unknown/reviewer-uncertain signs. Short complete rows remain in clean coverage but cannot supply a nonempty stem for every ending length.

For each ending length *k* = 1 or 2, split the stored token sequence exactly into a nonempty preceding stem and its last *k* tokens. No line concatenation, reversal, internal deletion, allograph merging or numerical-family grouping is performed. The source already uses normalized right-to-left token order. “Ending” means the end of that stored order; its status as a historical reading ending or grammatical suffix is an assumption, not a discovery. Actual source direction codes remain in corpus metadata (clean rows: 70 code1, 5 code3, 1 code5).

A stem and ending are connected when their concatenation is attested. A pair of different endings supported by *s* distinct stems contributes *s(s−1)/2* bipartite four-cycles. Thus a rectangle requires all four distinct sequences `AX`, `AY`, `BX`, `BY`, with different exact stems A/B and different exact blocks X/Y. Repeated copies of `AX` cannot supply `BY`.

The JSON preserves every edge, its source row keys and its row count. Unique-sequence support counts each edge once. A separate row-witness count multiplies the four edge multiplicities for each rectangle; it does not measure independent objects, dies or archaeological contexts.

## Fixed screen results

| Terminal block | Eligible rows / unique sequences | Exact stems | Stems with multiple endings | Ending pairs shared by ≥2 stems | Four-cycles |
|---|---:|---:|---:|---:|---:|
| One sign | 71 / 71 | 71 | 0 | 0 | 0 |
| Two signs | 67 / 67 | 64 | 3 | 0 | 0 |

The three two-sign alternations are:

| Exact preceding stem | Ending block A | Ending block B |
|---|---|---|
| M028 | M180 M402 | M400 M404 |
| M267 M099 | M102 M162 | M124 M342 |
| M391 M099 | M104 M162 | M289 M342 |

These pairs do not repeat across stems. The distinct M102/M104 and M124/M289 identifiers are retained; treating them as equivalent after seeing this table would change the question.

## Conditional permutations and limitations

The two ending lengths and permutation rules were fixed before running the release 3 analysis. After an alternate primary scan resolved three initially uncertain glyphs, the same parameters were rerun on the final source hash above; two additional rows passed the clean filter. The provisional run also had zero rectangles. All counts reported here use the final corpus. For each length, run 999 shuffles using Python's deterministic `random.Random`, base seed 20261010 plus the ending length. Hold each stem slot fixed and permute entire ending blocks only among sequences of the same total length. This preserves full sequence lengths, stems/slot multiplicities, and within-length ending-block counts. It does not preserve stem–ending associations, object dependencies or metadata strata.

Two baselines are reported: one slot per row, and one slot per distinct input sequence. The latter can acquire duplicate full sequences through shuffled collisions; it does **not** preserve distinct output count. In this sample all duplicate clean sequences are too short for either split, so eligible row and distinct-sequence baselines coincide.

All 999 scores are zero for every baseline and both ending lengths. Raw `score ≥ observed` is therefore 999/999; raw `score > observed` is 0/999. This is an uninformative, constant sampled score distribution, not a significance finding. For one-sign endings, unique stem slots make any rectangle structurally impossible under this shuffle. Two-sign support is also very sparse. The script saves all replicate scores and explicitly labels the exceedances exploratory; no corrected significance or multiple-testing claim is made.

The examples deliberately generate the same rectangle from an invented root–case grammar and from fixed office–product labels. Both have one four-cycle. Structural alternation alone cannot decide between these accounts, establish a word boundary, or assign sound or meaning. Absence of whole-line exact-prefix rectangles cannot reject morphology with changing stem forms or internal word boundaries. Excluding uncertain/damaged rows also changes the sample. The result supports continued accumulation of reviewed consecutive pages, not relaxed sign matching selected to obtain a positive result.

## Reproduction

```sh
python3 scripts/analyze_kober_alternations.py \
  --corpus data/processed/m77_verified/corpus_v3.json \
  --output results/kober_alternations_v3.json
python3 -m unittest discover -s tests -p test_kober_alternations.py -v
```

The result pins the corpus and analysis-script SHA256 hashes. Eight tests check missing-corner rejection, duplicate row multiplicity, cycle counting, atomic two-sign blocks, exact stems, short-row exclusion, permutation marginals/reproducibility, uncertainty exclusions, malformed/incomplete input rejection, and the grammar/fixed-label counterexample. No external data is needed to reproduce the numerical screen.
