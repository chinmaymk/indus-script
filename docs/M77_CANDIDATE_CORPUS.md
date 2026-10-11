# Recovered M77 transcription: checked examples and conditional analysis

23 September 2026. The public object records provide a useful source-labeled
Mahadevan transcription, but not a complete, independently authenticated edition.
We preserve its defects and uncertainty, select a conservative subset, and keep
all resulting claims conditional on the transcription. No sound or meaning is
established by this work.

## What the primary images establish

The [complete-line pilot](M77_EXPORT_PRIMARY_PILOT.md) checks references 1066 and
2427 against the printed catalogue, including every encoded glyph: 17 positions,
16 unstarred and one doubtfully read M402. Both arrays follow the printed line
from right to left. The `*402` qualifier agrees with Mahadevan's uncertainty; it
is neither another sign nor a confidently identified M402.

A further check of reference1001 authenticates four identified signs and one
`000` segment matching the printed hatched loss marker. The primary codebook
defines this as **one or more lost/illegible signs**, not a one-sign gap. This
record represents only the first of two displayed lines.

The [primary codebook review](M77_CODEBOOK_REVIEW.md) gives a stronger multiline
witness: reference2405 has seven printed entries across six sides, but the public
record retains just the first sequence. All six signs in that first sequence
match the primary drawing. Thus row count equal to the catalogue's 2,906 texts
does not imply recovery of its 3,573 lines. The canonical field `doc_count=7`
matches that example, but its general definition and extraction process remain
unverified.

The same primary pages establish object and direction codes. Every printed line
is normalized to right-to-left even when metadata records another actual direction.
Consequently, the metadata must not trigger blind reversal of arrays. Primary
object codes distinguish seals, sealings, miniature tablets, pottery graffiti,
copper tablets, bronze implements, ivory/bone rods and miscellaneous objects.
The export's blanket `artifact_type="seal"` conflicts with this richer metadata.

These checks concern selected records, not a random sample or a population
transcription accuracy estimate. The [ingestion review](M77_INGESTION_REVIEW.md)
distinguishes the whole-book OCR, a separate rank-mapped flat file, the supplementary
Firestore helper and the canonical object export. Their coexistence does not
establish a reproducible derivation chain. The helper's star-as-additional-sign
interpretation conflicts with the checked primary convention; we do not run it.

## Reproducible preparation

Our [fresh parser](../scripts/prepare_m77_candidate.py) joins all 2,906 M77 objects
to their exported records by explicit identifier and checks raw-token, diplomatic,
canonical-token and sign-count consistency. It preserves every literal token,
source reference, uncertainty flag, code and exclusion reason in
[`m77_candidate_records.jsonl`](../data/processed/m77_candidate_records.jsonl).
The raw record never disappears just because it is excluded from analysis.

The strict candidate subset requires `doc_count=1`, actual direction code1, at
least two token slots, and no doubtful or unknown-span marker. No sign is deleted
inside a retained line, so there is no invented adjacency across damage. This is
a conservative eligibility rule, not proof that every retained record is complete.

| Quantity | Count |
|---|---:|
| Source M77 records | 2,906 |
| Eligible candidate rows | 1,293 |
| Tokens in eligible rows | 6,132 |
| M signs represented | 332 |
| Distinct complete encoded texts | 1,141 |
| Tokens after whole-text deduplication | 5,625 |
| Supplied signs absent from the eligible subset | 85 |

Overlapping exclusion reasons are 880 multiple-document records, 617 containing
unknown spans, 389 containing doubtful readings, 393 with another direction code,
and 84 with fewer than two token slots. These counts cannot be added to get a
unique excluded-row count. Eligible rows include 1,155 seals, 65 sealings, 30
pottery graffiti, 16 ivory/bone rods, 14 miniature tablets, six copper tablets,
six miscellaneous objects and one bronze implement, according to primary code
definitions applied to source-supplied metadata.

Every supplied M sign has a [conditional profile](../results/m77_candidate_profiles_417.json),
including zeros, primary catalogue totals and unresolved readings. The same
qualified counts appear separately from primary evidence in the
[417-sign index](../results/sign_evidence_417.json). No M/P/W correspondence is
inferred from numerical equality. No proposed reading columns are imported.

## Structural results and selection limits

The [analysis script](../scripts/analyze_m77_candidate.py) deduplicates whole texts,
keeps boundaries, and compares adjacency with 499 permutations preserving each
length/position marginal. It uses the previously tested statistical functions.

| Candidate dataset | Distinct texts | Observed adjacent MI | Position-preserving null mean | Upper-tail permutation p |
|---|---:|---:|---:|---:|
| All eligible objects | 1,141 | 3.169 bits | 1.989 bits | 0.002 |
| Seal code1 only | 1,053 | 3.176 bits | 2.009 bits | 0.002 |

The remaining dependence is consistent with a structured sign system and cannot
be explained by these positional marginals alone. It does not identify a language,
phonetic key or semantic categories. The minimum attainable p here is 0.002, not
a claim of an exactly measured population probability. The source M77 and Wells
datasets may describe the same objects; this is a transcription-based replication,
not independent archaeological evidence.

Selection materially changes some sign profiles. In the primary inventory M328
is final in 274 of323 occurrences. In the eligible secondary subset it occurs
only14 times: ten initial, three medial and one final. The full public export
contains only49 M328 occurrences even with doubtful forms included. This warns
against using the selected subset to redefine that sign's general role. It does
not refute the primary distribution or prove a particular reason for every
missing occurrence.

The direct M-number stream also contains both adjacent orders of selected stroke
forms: M086→M099 on five eligible records and M099→M086 on seven. The complete
witness ledger is in [the results](../results/m77_candidate_structure.json).
Reference1066 supplies a checked example of the first; reference2286 has an
earlier primary check of the opposite displayed order in the
[numeral investigation](NUMERAL_PRIMARY_FOLLOWUP.md). These runs do not establish
numerical values or that the strokes share one numerical field. They preserve
concrete tests for any future rule that imposes a universal ordering.

## Next discriminating work

Recover the missing side/line records or transcribe them directly, starting with
the authenticated multiline examples and signs most underrepresented in the
export. Check additional preselected primary lines across sites, object types,
direction codes and rare signs. Only then expand the strict subset or use it to
evaluate detailed linguistic readings. Structural prediction and verified meaning
remain distinct requirements of decipherment.

The subsequent [complete M328 recovery](M77_U_COMPLETE_RECOVERY.md) now supplies
all323 published occurrences on313 lines, with uncertainties and repeated indexed
sightings preserved. Its positional totals exactly match Table I. These reviewed
lines form a sign-selected recovery separate from the general strict candidate
subset; they establish no sound or meaning and cannot be treated as an unbiased
new language-test sample.
