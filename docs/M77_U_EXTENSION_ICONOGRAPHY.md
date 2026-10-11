# Independent M328 extension: PDF 588–590

Reviewed 2026-09-23 from Mahadevan's 1977 primary concordance. PDF pages **588, 589 and 590 are printed pages 577, 578 and 579**, respectively. Every page's index glyph remains the plain U, M328; no section boundary occurs within this assignment.

The [structured ledger](../data/processed/m77_u_extension_iconography.json) records **50 indexed lines**: 16 on printed 577, 18 on 578 and 16 on 579. All 50 reference/side/line keys are distinct within this tranche. Each target contains exactly one M328. Ten are longer sequences; forty are stroke-group-plus-U lines. The index position is stored as a zero-based token index. Contextual lines on other sides were not transcribed into this dataset.

| Printed page | Indexed references, in page order |
|---|---|
| 577 | 4672, 4351, 4344, 5254, 4356, 4497, 5474, 4445, 5222, 5223, 5286, 5335, 4689, 4345, 5337, 4375 |
| 578 | 4549, 4525, 4520, 4670, 4511, 4593, 4350, 4512, 4564, 5452, 4473, 4686, 4502, 5436, 1532, 2815, 3224, 3230 |
| 579 | 4678, 4470, 4485, 4571, 5497, 4577, 4579, 4484, 5271, 4493, 4501, 4503, 5406, 5292, 4476, 4508 |

All codes are `20` (side 2, line 0), except 1532 `00` and 2815/3224/3230 `10`. Arrays follow right-to-left reading of the printed concordance, so the first-read sign is first. This normalization is not evidence of the actual direction on each object.

The longer target sequences, checked against the primary numbered sign list, are:

| Reference/code | Full normalized tokens |
|---|---|
| 4672/20, 4351/20, 4344/20, 5254/20 | M177 M197 M192 M341 M089 M328 |
| 4356/20 | *M336 M267 M341 M089 M328 |
| 1532/00 | M095 M328 M002 M012 |
| 2815/10, 3224/10, 3230/10 | M045 M095 M328 M002 M176 |
| 4485/20 | M267 M402 M149 M095 M328 |

M341 has the divided sloping base and curved right edge; it should not be silently replaced by angular M191. M336 has an internal pendant terminating in a loop. M045 lacks the extra fringe of M046. These identifications use primary sign-list morphology, not a candidate export.

Three indexed lines carry primary doubt: **4356 on M336, 4525 on M328, and 4476 on M095**. Their tokens retain `*`. The remaining short targets on printed 577 and the first fourteen on 578 use M089 (three long strokes); the last four on 578 and targets on 579 use M095 (four long strokes). At 4525 the hatching belongs to contextual side 10, while the indexed side 20 is M089 *M328. It is not legitimate to carry the other side's missing span into this target.

There are **zero LOSS and zero reviewer UNKNOWN tokens** in the indexed targets. The schema nevertheless distinguishes a primary missing span (`LOSS`, one or more signs, not a fixed single token) from an unidentified visible glyph (`UNKNOWN`). Primary doubt is independent of either. Full-sequence checking does not erase the source's doubt marks.

The ledger gives bytes and SHA-256 for the source PDF, all three full-page renders, five inspected detail crops and four numbered sign-list renders. Local renders use prefix `results/primary_pages/u-extension-iconography-`; no data was downloaded. Counts, unique keys, indexed U positions and evidence hashes were checked locally. Physical artifact images were not reexamined in this task.
