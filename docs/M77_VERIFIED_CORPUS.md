# M77 corpus: complete-page transcription

## Current release: four consecutive pages

10 October 2026 continuation. [Release4](../data/processed/m77_verified/corpus_v4.json) covers printed39–42/mainPDF50–53: **122 references,132 lines,672 assigned sign positions,148 distinct assigned types,15 unknown-length loss spans and24 source-doubtful positions**. The24 doubtful positions are included in672. There are no additional unidentified visible glyphs, but damaged text and source doubts remain. This covers3.69% of3573 printed lines, not a complete corpus or decipherment.

The fourth page adds1097–1127 except1124, with two lines each at1099,1101 and1112:30 references and33 rows. Parent independently checked this inventory and the continuation metadata against the full main-source page. Both reviewers used the main and alternative scans, authenticated as printed42 at mainPDF53/alternatePDF54. A disclosed secondary hints; B did not consult alternative transcriptions during entry and reported no specific remembered page53 readings. Both froze and validated their own inventories before comparison. All33 rows agree exactly; no new adjudication was needed. This is agreement between AI review passes, not an estimate of ancient-object accuracy.

The source's1101 second-line direction code2 is retained as metadata without reversing the already normalized RTL token order. Current field-symbol codes are129rows code01,2code35 and1code00; all132 rows have object type1. No code-to-animal mapping, date assignment or representative sampling follows from these counts.

```sh
python scripts/build_verified_m77.py \
  --manifest data/processed/m77_verified/page_manifest_v4.json \
  --adjudications data/processed/m77_verified/adjudications_v4.json \
  --candidate-export data/processed/m77_candidate_records.jsonl \
  --comparison results/m77_verified_v4_comparison.json \
  --output data/processed/m77_verified/corpus_v4.json
```

The [exact ending-test support diagnostic](ENDING_SUPPORT_CERTIFICATE.md) remains negative on this release: the specified statistic is zero under every permitted shuffle. This closes further Monte Carlo work at the present support, not the language question. The next consecutive page is printed43/mainPDF54; authenticate the alternate locator independently. Prior releases and their conclusions remain versioned.

## Third release: historical batch record

10 October 2026 continuation. [Release3](../data/processed/m77_verified/corpus_v3.json) covers printed39–41/PDF50–52: **92 references,99 lines,515 assigned sign positions,129 distinct assigned types,zero additional unidentified visible glyphs,12 unknown-length loss spans and20 source-doubtful positions**. The20 source-doubtful positions are included in515, not resolved by that count. This is2.77% of the3573 printed lines. All rows in the manifest are present; this is not a complete Indus corpus or a decipherment.

The third page contains1066–1096, including three lines of1093. Parent independently checked the printed coverage and metadata. The source direction codes on1093's lines are3,5,1; these do not change M77's already normalized right-to-left token order. Both reviews froze before comparison: A disclosed secondary-export exposure, B disclosed earlier exposure to the1066 pilot. These are distinct review passes, not fully blind human readings.

The32 whole-row agreements left one disagreement:1083's second glyph from the right, M054 versus M055. On the main scan, M055's short interior stroke could not be separated reliably from the oval edge and scan pixels; the assembler initially refused publication, then a provisional custom decision retained `UNKNOWN {M054,M055}`. That decision remains in [the main-scan-only snapshot](../data/processed/m77_verified/adjudications_v3_primary_scan_only.json).

The existing alternative scan provided a clearer view of the same printed edition. At alternatePDF53/printed41, both1083 glyphs have empty central ovals, supporting M054. A bounded check of the two earlier unknowns also resolves1026 position6 as M347 (three prongs on both terminals) and1047 position1 as M054 (empty oval). Parent visually checked the native crops against the sign-list forms and accepted B's separately recorded findings. Final release3 uses A's rows at these three references. Original reviews and releases1/2 remain unchanged; no loss span or source-doubt marker was removed. This improves printed-transcription fidelity, not independent archaeological confirmation.

```sh
python scripts/build_verified_m77.py \
  --manifest data/processed/m77_verified/page_manifest_v3.json \
  --adjudications data/processed/m77_verified/adjudications_v3.json \
  --candidate-export data/processed/m77_candidate_records.jsonl \
  --comparison results/m77_verified_v3_comparison.json \
  --output data/processed/m77_verified/corpus_v3.json
```

[Initial comparison](../results/m77_verified_v3_initial_comparison.json), [decisions](../data/processed/m77_verified/adjudications_v3.json), [B initial follow-up](../data/processed/m77_verified/reviewer_b_adjudication_page052.json), [1083 alternative-scan addendum](../data/processed/m77_verified/reviewer_b_adjudication_page052_alt_addendum.json), and [prior-unknown addendum](../data/processed/m77_verified/reviewer_b_alt_prior_unknowns.json) preserve the changing evidence. The next consecutive page is mainPDF53/printed42; authenticate the alternative scan's locator separately. Prior releases remain unchanged.

## Second release: historical batch record

10 October2026 continuation. [Release2](../data/processed/m77_verified/corpus_v2.json) covers printed39–40/PDF50–51: **61 references,66 lines,349 identified sign positions,110 distinct assigned types,two unidentified visible glyphs,nine unknown-length loss spans and14source-doubtful positions**. This is1.85% of the3573 printed lines. Full printed-row coverage does not imply object-photograph verification or decipherment.

The second page adds32references (1031–1061 and1065), with1052 having two lines. Both reviews froze before comparison; A saw secondary candidates, B used primary pages without alternate page51 readings during entry. Five rows disagreed. Four were resolved against primary glyph details/order;1047's first glyph remains UNKNOWN{M054,M055}. The earlier1026 UNKNOWN{M347,M352} remains unresolved. B's original1051 UNKNOWN lacked explicit1/1length bounds, so the assembler rejected it. A separately pinned schema-only amendment added those bounds; the original freeze was preserved. Adjudication then identified1051's formerly unresolved glyph asM163. No silent repair or majority vote was used.

Whole-row boxes in A's second-page review may clip the extreme left reference digits near the bottom; full-page renders, wide bands, B boxes and the independently inventoried row manifest retain reference evidence. Boxes are not a substitute for the pinned full source.

```sh
python scripts/build_verified_m77.py \
  --manifest data/processed/m77_verified/page_manifest_v2.json \
  --adjudications data/processed/m77_verified/adjudications_v2.json \
  --candidate-export data/processed/m77_candidate_records.jsonl \
  --comparison results/m77_verified_v2_comparison.json \
  --output data/processed/m77_verified/corpus_v2.json
```

[Initial unresolved comparison](../results/m77_verified_v2_initial_comparison.json), [decisions](../data/processed/m77_verified/adjudications_v2.json), and [B follow-up](../data/processed/m77_verified/reviewer_b_adjudication_page051.json) remain inspectable. The previous one-page release below is retained unchanged. Next consecutive source page isPDF52.

## First release: historical batch record

10 October 2026. **The first release covers one entire printed page: 29 references and 33 lines.** It is faithful to the reviewed M77 printed transcription, with one glyph identity still unresolved. This is not object-photograph verification, a representative corpus, or a decipherment.

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

At this first release, the next page wasPDF51, now included in release2 above. Source totals are2906 objects,3573 lines,13372 legible occurrences;33/3573 was only0.92% of printed lines. Entire-page coverage prevents cherry-picking legible or interesting rows, but is not random sampling. New transcription does not erase prior exposure to the export or create a fresh held-out test set.

## Tests enabled by a larger verified corpus

These remain queued designs except the explicitly linked inventory calculation:

- **Kober-style alternations:** find recurring stems with coordinated multi-sign ending replacements, then compare the number and replication of rectangular stem/ending paradigms against shuffled controls preserving length, sign frequency, site and object class. Fixed labels can also alternate: evidence for inflection requires additional constraints, not just a shared suffix. Linear B motivates the method; no transfer of its sound values is proposed. Linear A and Rongorongo remain comparative cases to investigate, not validation corpora already analyzed.
- **Inventory estimation:** [Good–Turing, Chao1 and finite-catalogue rarefaction are now calculated](INVENTORY_RICHNESS.md) from the complete primary Table I. Cross-script growth comparisons remain unperformed. Normalization, damage, sample selection and duplicate inscriptions limit interpretation; an estimated inventory alone cannot classify a script as logosyllabic.
- **Chronology and region:** source site and excavation-phase assignments independently. Early Harappan, Mature Harappan and Late Harappan are not interchangeable bins; a secondary level number is not a phase date. Compare within securely dated phases before pooling; keep unknown dates explicit.
- **Text and seal animal:** authenticate the field-symbol codebook and each association, then test conditional dependence with site, phase, object class and duplicate groups controlled. Name and office hypotheses can both produce animal associations. Repeated mold impressions must not inflate sample size.
- **Numeral substitutions:** freeze count-independent inclusion rules and stroke-class definitions. Count all eligible minimal substitutions, including failures, and compare ratios with fixed null models. Such a test measures substitution structure, not equal quantity. The current2/3 conditional ratio has no established external equality anchor.

The [comparative numeral result](COMPARATIVE_NUMERAL_SYSTEMS.md) and [Claude critique response](CLAUDE_SECOND_OPINION.md) explain why metrological interpretation must remain separate. The corpus path was chosen over the preprint/outreach path; no new artifact-search loop was started.
