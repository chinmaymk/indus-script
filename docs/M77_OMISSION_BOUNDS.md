# Missing-line evidence and omission bounds for every sign

23 September 2026. The export's low M328 count is a data-coverage problem, not
evidence that Mahadevan's terminal-sign distribution is wrong. Primary concordance
pages show omitted secondary lines ending in M328. The aggregate counts also
place a strong conditional lower bound on the missing terminal occurrences.

**Subsequent recovery:** the [entire M328 concordance block](M77_U_COMPLETE_RECOVERY.md)
is now separately transcribed:323 occurrences in313 lines, exactly reproducing
all four primary positional counts. Its per-reference comparison localizes the
274-occurrence export deficit. The older bounds below still describe the unchanged
export; the recovered lines are a separate primary dataset.

## What is directly established

The [position-count review](M77_POSITION_COUNT_REVIEW.md) verifies that primary
Table I counts **line-relative** positions and includes doubtfully read signs
among legible occurrences. A text containing several sides or lines must therefore
retain those boundaries to reproduce the table. Concordance ordering can use
whole-text context; it must not be mistaken for a direction to concatenate all
lines into a linguistic sentence. Mahadevan states that their continuity/order
is unknown.

The review identifies omitted M328-final secondary lines for texts4373,4702 and
8117 in printed615/PDF626, and texts4428 and4576 in printed581/PDF592. Their
canonical first-sequence records do not contain M328. These are concrete omissions;
no general missing-line rate is estimated from the five selected examples.

Separate primary work [recovers all seven entries of text2405](M77_2405_RECOVERY.md),
preserving their sides, lines, actual directions and lost passages. The public
canonical record contains only its first sequence. The primary images establish
the omitted content without borrowing a reading key from another decipherment.

The [two-line recovery for text1001](M77_1001_RECOVERY.md) adds its omitted
singleton M393. An initial visual confusion with M317 was flagged by the primary
counts and corrected using a clearer image and an independent glyph check.
The rejected identification remains in the correction history, not in current
transcribed tokens. Across both recovered objects there are nine lines, 24
identified sign positions and three unknown spans. Seven of those lines are
absent from the canonical records' single sequences.

The [recovery validator](../scripts/verify_m77_recoveries.py) checks evidence
hashes, side/line keys, first-line matches and primary count compatibility, then
writes a separate [reviewed-line corpus](../data/processed/m77_primary_recovered_lines.jsonl).
It neither overwrites the canonical export nor silently expands the selected
statistical corpus. Image identification remains a documented visual judgment;
passing these checks does not make it infallible.

## Count proof without inventing damaged endpoints

Let a sign have `T` occurrences in the primary table, with `p` in one positional
category. Let `A` named occurrences survive in the export. **Assume** those `A`
occurrences form an injective subset of the primary occurrences of that same
sign. This assumption is compatible with the observed counts but has not been
authenticated for every exported token.

At most `A` of the `p` category occurrences can survive. At most `T−p` surviving
occurrences can come from other categories. It follows that

```
max(0, p − A) ≤ missing occurrences in the category ≤ min(p, T − A)
```

Each endpoint is achievable by allocating surviving occurrences to this category
first or to the other categories first. Thus the bounds are individually sharp.
The category intervals cannot be chosen independently: missing counts across
all four categories must sum to `T−A`.

The [script](../scripts/audit_m77_omissions.py) calculates these bounds for all417
signs. Tests exhaustively enumerate feasible retained allocations for every
four-category population whose category counts range from zero through three.
An impossible subset fails explicitly rather than being clipped into a result.
The [full result](../results/m77_omission_bounds.json) preserves inputs and assumptions.

This calculation does **not** remove `000`, call it one missing sign, or assign
positions to the first surviving glyph after a lost span. No explicit primary
rule for all such damaged-edge cases was recovered. The named-sign total includes
doubtful readings for comparison with the primary table while retaining their
uncertainty in the underlying records.

## Result

| Quantity | Count |
|---|---:|
| Primary named-sign occurrences | 13,372 |
| Export named-sign occurrences, including doubtful | 11,959 |
| Conditional omitted occurrences | 1,413 |
| Sign types with a deficit | 191 |
| Sign types completely absent | 23 |

For M328, `T=323`, `A=49`, and the primary final-position count is `p=274`.
Its **missing final-position count is bounded by225–274**, under the stated
subset assumption. This lower bound holds even if every one of the49 surviving
tokens were terminal. It does not require trusting the export's apparent endpoints.
M328's total deficit274 is about19.4% of all1,413 missing named occurrences.

The further strict filtering leaves14 M328 occurrences, only one of them final.
That selected profile cannot replace the primary distribution. Across all417
signs, no strict-subset positional count exceeds its corresponding primary
count. This is a useful compatibility check, not proof of correct transcription.

M089 and M087 have the next largest total deficits,129 and101 respectively.
Their global counts alone do not force a positive deficit in any one positional
category. The full per-sign intervals preserve that distinction rather than
assuming all missing signs are terminal or occur on the same object type.

## Interpretation and limits

The missing secondary lines and count imbalance can distort inferred functional
classes. A proposed grammar must fit the primary occurrences as well as the
selected digital subset. These findings identify a repairable input problem;
they establish no specific phonetic or semantic value and do not determine the
language.

Not every deficit is attributed to omitted lines: transcription, edition and
counting differences remain possible. An [alternative public scan](M77_ALTERNATIVE_SCAN_REVIEW.md)
also skips printed758–759 at the expected position, so the missing Table IV
object-type rows have not been recovered. A bounded public-source follow-up is
recorded in [the discovery ledger](../data/processed/m77_source_followup.json).
