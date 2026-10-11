# Independent review: M102/M106 substitutions

The candidate transcription supports **three exact complete-string substitution frames** for M102 and M106. None is immediately followed by M287 M342. This establishes overlapping distribution under the stated filters; it does not establish the values “three” and “five,” a counting unit, or an expression for a measured commodity.

This review independently uses exhaustive pairwise Hamming distance, rather than the parent audit's planned mask index. The sample and definitions are the existing eligible domestic seal sample: 1,175 reference records, deduplicated to 1,066 complete sign strings. The verifier spells out the eligibility conditions and checks their equality with the existing filter. Domestic ranges and named references are shared inputs, so this is an independent algorithmic check of the result, not independent archaeological evidence.

## Exact pairs

| Complete frame | M102 references | M106 references |
|---|---|---|
| ? M015 | 2368, 2497, 2514, 5063, 5093 | 2113, 2382, 7040 |
| ? M169 | 1411, 8024 | 1422, 1441, 2215, 2525, 8058 |
| M267 M099 ? M162 | 1091, 2080, 2180, 2354, 4126, 6214 | 1131 |

The algorithm compares all **83,691 unordered same-length pairs**, yielding **681 pairs at Hamming distance one** across all sign substitutions. Exactly three involve M102/M106. Different reference multiplicities do not increase the three-frame count. The 22 listed references do not establish 22 independent producers or uses.

## Controls in the same complete frames

| Frame | All observed occupants of ? | Distinct occupants |
|---|---|---:|
| ? M015 | M025, M069, M086, M102, M104, M106, M326, M387, M389 | 9 |
| ? M169 | M100, M102, M104, M106, M107, M112 | 6 |
| M267 M099 ? M162 | M102, M104, M106, M107 | 4 |

All occupants and their reference lists are retained in the JSON result. The first frame is especially permissive: sharing it is not a property unique to M102/M106. The narrower third frame makes a common functional category plausible, but sample restriction and low counts prevent treating its four observed occupants as the complete allowable inventory. These are whole-string frames, so no proposed word boundary is necessary to count them. A complete-frame substitution still does not guarantee a single morpheme, independent word, or numeral.

## The curve-terminal comparison is weaker

There are four unique strings containing M102 M287 M342, all final, and five containing M106 M287 M342, four final. The M106 sequences have seven references because the solus three-sign sequence has three references. The nonfinal occurrence is reference 2254, M106 M287 M342 M001.

The strict sample has **no exact complete-string M102/M106 counterpart followed by M287 M342**. For example, reference 2302 is M391 M099 **M387 M102** M287 M342, whereas 4134 is M391 M099 **M106** M287 M342: an additional M387 is present in the former. They are not a controlled one-sign substitution. Shared short endings show recurrent local context, but their different preceding material permits many alternative segmentations and functions.

The absence is filter-conditional. Reference **2659**, diplomatically `+*102-287-342+`, would superficially supply the solus M102 counterpart of M106 M287 M342 at references 1460, 2381, and 4618. Its M102 identification is explicitly doubtful, so the unchanged eligibility rules exclude it. Ignoring that doubt would transform an uncertain reading into purported support for the hypothesis being tested. This review records the exclusion rather than silently promoting it. Reference 4520 also contains the M106 solus sequence but is excluded as a non-seal record with multiple exported documents; adding another M106 reference would not resolve the doubtful M102 counterpart. The verifier does not inspect the original glyph; a separate primary review is needed to determine whether the doubt can be resolved.

## What the evidence permits

The exact substitutions strengthen the statement that M102 and M106 share some combinatorial environments. If primary sign drawings establish three and five strokes respectively, this geometric correspondence makes a numeral-family hypothesis reasonable to investigate. It remains a hypothesis: the stroke counts could instead distinguish categorical values, phonetic signs, lexical signs, or other functions. Common frames alone cannot choose among these alternatives or decide whether some catalogue distinctions are allographic.

A simple nonnumeric counterinterpretation assigns the varying signs arbitrary category labels A, B, C, and D. The same exact strings and substitution counts result. The corpus comparison contains no external observation forcing A to mean 3 or B to mean 5. Conversely, the absence of a strict M287 M342 pair does not disprove quantities: sparse sampling, selection, and the unresolved reading at 2659 can all remove an expected pair. No hypothesis receives a numerical probability or significance claim here.

Evidence that would change this conclusion includes an independently authenticated quantity or total, a secure correspondence with counted objects or metrology, or a predeclared numerical rule that successfully predicts external examples. Assigning sound values would additionally require an independent linguistic anchor. The present computation supplies none of those anchors; all 417 semantic and phonetic fields remain unassigned.

## Reproduction and scope

Run `python scripts/verify_stroke_substitutions_independent.py` from the repository root. It writes [the complete independent result](../results/stroke_substitution_independent_review.json); the saved [console output](../results/stroke_substitution_independent_summary.txt) records the executed run. The result includes SHA256 values for the candidate corpus, shared filter definitions, and verifier itself. No downloads were needed.

This review is exploratory, uses the same corpus in which the hypothesis was noticed, and supplies no held-out confirmation. It verifies transcription-level counts and controls. It does not authenticate the 22 reference readings from photographs, infer artifact contemporaneity, determine owners, or assign meanings.
