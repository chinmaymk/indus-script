# M77 corpus: complete-page transcription, first batch

10 October 2026. **The current release covers one entire printed page: 29 references and 33 lines.** It is faithful to the reviewed M77 printed transcription, with one glyph identity still unresolved. This is not object-photograph verification, a representative corpus, or a decipherment.

The main research direction is now consecutive-page corpus construction. The earlier 550 reviewed contexts were selected around M328 and its counterparts. Nine other explicitly keyed recovered lines and several selected witnesses do not make those data a complete, unbiased corpus. They remain preserved separately; this batch does not automatically upgrade them.

## Released coverage

Source: Mahadevan1977, printed39/PDF50, existing `data/raw/mahadevan_1977_text.pdf`. References1001–1030 excluding1009, which is absent from this printed page. References1001,1012,1016 each have two lines;1018 has two sides. The manifest lists every expected row independently of both transcription submissions.

| Measure | Count |
|---|---:|
| References / displayed rows | 29 / 33 |
| Identified sign positions | 180 |
| Distinct assigned M77 sign IDs | 72 |
| Visible sign with unresolved identity | 1 |
| Unknown-length loss spans | 5 |
| Source-doubtful sign positions | 9 |
| Initial whole-row A/B agreements / disagreements | 22 / 11 |

The one unresolved glyph is position6 in normalized right-to-left sequence1026: candidates M347/M352. It is stored as `UNKNOWN`, not either candidate. The uncertainty concerns the left terminal's shape. It is not a source asterisk, a lost passage, or evidence that either candidate is absent. No sounds or meanings are assigned.

A `LOSS` span has minimum1 and unknown maximum sign count. A visible unidentified glyph occupies one position. Source doubt is separate from reviewer uncertainty. All printed lines already run right-to-left; actual direction is retained as its own code and never triggers another reversal. This matters at1018: the secondary export has the second side's sequence but a direction field matching the first side. A one-row-per-reference representation loses this distinction.

## Review and adjudication

[Reviewer A](../data/processed/m77_verified/reviewer_a_page050.json) saw the secondary strings before checking primary images; it is not blind. [Reviewer B](../data/processed/m77_verified/reviewer_b_page050.json) did not consult secondary strings during transcription, but had previously seen five pilot references on this page. Both froze their submissions before token comparison. These are two AI-assisted reviews, not independent human epigraphists; their agreement is no population error-rate estimate.

The [initial comparison](../results/m77_verified_initial_comparison.json) records11 disagreements. The assembler correctly refused publication at that stage. [Adjudication](../data/processed/m77_verified/adjudications_page050.json) resolved ten against source images and retained the1026 ambiguity. Reviewer B's [separate follow-up](../data/processed/m77_verified/reviewer_b_adjudication_page050.json) explains several corrected identifications and one serialization error. Original submissions were not rewritten to create agreement.

The released [corpus](../data/processed/m77_verified/corpus.json) therefore has all33 rows and zero *unadjudicated rows*, but **not zero uncertain glyphs**. Ten adjudications select A; one uses a custom unknown-bearing sequence. Primary source, render, review and decision files are hash-pinned. Whole-row bounding boxes allow inspection; they are not per-glyph segmentation.

For the25 single-line references,24 agree exactly with the secondary candidate tokens and one differs because we refuse to choose between M347/M352. Four multiline/multiside references are reported separately rather than compared as if the export covered every line. This selected-page comparison is not an accuracy estimate for the whole export.

## Reproduce and extend

```sh
python scripts/build_verified_m77.py \
  --manifest data/processed/m77_verified/page_manifest.json \
  --adjudications data/processed/m77_verified/adjudications_page050.json \
  --candidate-export data/processed/m77_candidate_records.jsonl \
  --comparison results/m77_verified_comparison.json \
  --output data/processed/m77_verified/corpus.json
python -m unittest discover -s tests -p 'test_verified_m77.py'
```

Without `--adjudications`, the first command writes differences and refuses to publish a complete corpus. Tests cover lost continuations, duplicate keys, metadata inheritance, unknown-length loss, uncertain glyphs and candidate schema conversion. Source bytes must be present through Git LFS, not just pointer files.

Next add consecutive PDF51 onward using the same frozen-review protocol. Source totals are2906 objects,3573 lines,13372 legible occurrences;33/3573 is only0.92% of printed lines. Entire-page coverage prevents cherry-picking legible or interesting rows, but is not random sampling. New transcription does not erase prior exposure to the export or create a fresh held-out test set.

## Tests enabled by a larger verified corpus

These are queued designs, not completed results:

- **Kober-style alternations:** find recurring stems with coordinated multi-sign ending replacements, then compare the number and replication of rectangular stem/ending paradigms against shuffled controls preserving length, sign frequency, site and object class. Fixed labels can also alternate: evidence for inflection requires additional constraints, not just a shared suffix. Linear B motivates the method; no transfer of its sound values is proposed. Linear A and Rongorongo remain comparative cases to investigate, not validation corpora already analyzed.
- **Inventory estimation:** report singleton/doubleton counts, Good–Turing missing mass and Chao-type richness estimates with their sampling assumptions; compare growth at matched sample sizes and tokenization conventions. Normalized M77 types, damage, finite corpus selection and unequal sign frequencies limit interpretation. An estimated sign inventory alone cannot classify a script as logosyllabic.
- **Chronology and region:** source site and excavation-phase assignments independently. Early Harappan, Mature Harappan and Late Harappan are not interchangeable bins; a secondary level number is not a phase date. Compare within securely dated phases before pooling; keep unknown dates explicit.
- **Text and seal animal:** authenticate the field-symbol codebook and each association, then test conditional dependence with site, phase, object class and duplicate groups controlled. Name and office hypotheses can both produce animal associations. Repeated mold impressions must not inflate sample size.
- **Numeral substitutions:** freeze count-independent inclusion rules and stroke-class definitions. Count all eligible minimal substitutions, including failures, and compare ratios with fixed null models. Such a test measures substitution structure, not equal quantity. The current2/3 conditional ratio has no established external equality anchor.

The [comparative numeral result](COMPARATIVE_NUMERAL_SYSTEMS.md) and [Claude critique response](CLAUDE_SECOND_OPINION.md) explain why metrological interpretation must remain separate. The corpus path was chosen over the preprint/outreach path; no new artifact-search loop was started.
