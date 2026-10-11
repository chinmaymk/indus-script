# L-51: an unidentified motif and a real ending–fish association

The seal's identity and four-sign inscription are supported by the catalogues.
Its proposed necklace motif remains an analogy. Separately, the exact ending
shown on L-51 has a strong association with modified fish signs in the selected
complete-text sample. This is a useful structural constraint, but does not
identify gemstones, a jewellers' guild, a tax category or a pronunciation.

## Artifact identity and context

The [original report review](L51_PRIMARY_CONTEXT_REVIEW.md) verifies Rao's
terracotta seal11358, plateCLIX C5, phaseIV, SRG2/C25, from a pit sealed by layer2,
at depth1ft. Its reverse button is broken. The cited passages do not identify
jewellery, beadworking or a jeweller in that pit. A sealed pit is not automatically
a workshop occupation deposit. No absolute date is inferred here.

The [CISI metadata](../results/primary_pages/l51-review-metadata.png) connects
L-51 to excavation11358, Finnish6037, LTH SRG1264 and photoHU1019. The museum
accession is distinct from the excavation's SRG2/C25 location. Finnish6037 is
not silently treated as a Mahadevan text number.

The [visual review](L51_VISUAL_REVIEW.md) distinguishes what is visible from
what it might depict. The upper motif has a transverse element, rounded repeated
elements in rows and a fringe of elongated projections. The four large signs
below it form a separate text. The seal and impression are mirrored; the 2025
bulletin repeats the CISI impression in the same orientation, rather than
providing a second independent view of the original motif.

Rao cautiously compares the motif to a seed drill, without a diagnostic comparison
on the cited pages. CISI calls the object unidentified. The bulletin compares it
to ancient and modern necklaces. The modern example is the closer overall row-and-
fringe analogy; the depicted ancient necklace chiefly resembles its pendants.
Neither comparison uniquely identifies the motif. The reproduced necklace's
original stringing and context are not independently authenticated by that figure.
The original Rao plate is too degraded to resolve the finer details.

Even a secure necklace identification would leave the text–image relationship
open: emblem, ownership, commodity, office and ritual associations would still
need distinguishing evidence. It is not an independently labelled translation.

## What the more-than-80% claim can mean

Independent review confirms that the bulletin's inline glyph depicts the exact
pair represented in the export as **W527 W555**, not W555 with every possible
ending. The same pair is explicitly terminal in its M-636 example. In reported
right-to-left reading, the raw file prefix corresponds to that ending.
L-51's raw string is `W527 W555 W231 W235`.

The [protocol](../data/processed/l51_protocol.json) preceded new counts, after
the named examples and claim were seen. The author does not supply executable
boundaries for the proposed core informational segment or an explicit denominator.
Our [audit](../scripts/audit_l51.py) therefore counts target signs anywhere in
the remaining text as a transparent proxy. It does not claim an exact replication
of unspecified segmentation.

Fourteen raw seal rows have the exact file prefix. Eleven certainly contain a
selected fish-family member; two lack one under the source's completeness flag;
one has unknown text. The U candidates W705/W706 add no additional positive:
the one U-bearing example already contains a modified fish.

- All14 records:11/14 observed positives, or78.6%; allowing the unknown gives
  an upper bound of12/14, or85.7%.
- Excluding the one source-flag unknown:11/13, or84.6%. This is one possible
  denominator that yields more than80%, not proof of the author's count rule.
- M-821 has only the two ending signs and is physically fragmentary despite
  complete=Y. Treating that negative as unknown gives11 positive, one negative
  and two unknown; the conditional known-only fraction becomes11/12.

Four other seal rows contain the pair internally or after other/unknown material:
H-21, M-1917, M-1053 and M-1293. They remain separately listed rather than silently
becoming whole-text ending cases. Original completeness of M-821 has not been
independently resolved by this audit.

## Comparison with other complete seal texts

The primary comparison selects single-row secondary object groups from the
existing strict corpus, complete preservation, seal types, and length≥2.
It contains1082 records and nine exact-ending cases. Site, literal object type
and exact text length define fixed-margin strata.

| Target | Observed among9 | Matched expectation | Descriptive upper tail |
|---|---:|---:|---:|
| Selected fish family | 8 | 4.163 | .00786 |
| Plain W220 | 0 | 1.214 | 1 |
| U candidates W705/W706 | 1 | .918 | .641 |
| Fish or U | 8 | 4.492 | .0140 |

The fish-family association is therefore stronger than a high unadjusted percentage
alone. The eight positives contain modified forms: W235 on five records, W231 on
three, W240 on two, and W233 on one, with overlap. They do not establish plain-fish
W220 equivalence. Deduplicating entire texts within site/type leaves1049 records
and nearly the same result: fish upper tail .00715, union .0131.

A narrower comparison asks what W555 contributes beyond W527 itself. Restricting
the universe to W527-initial texts leaves27 records. Seven of the nine active
site/type/length strata contain only the ending case. The two remaining strata
each have one additional control, M-833 or M-133, and both already contain fish.
Consequently the union count is fixed at8 under these margins: expectation8,
upper tail1. This comparison is **uninformative about the incremental role of
W555**; it is not evidence that W555 has no role.

These are selected, exploratory comparisons. Exact tails describe the specified
exchangeability model, not a probability of a decipherment being correct. Selection,
position-dependent grammar, unverified transcriptions, chronology and archaeological
context remain limitations. The independent verifier separately reconstructs all
12 target-by-universe comparisons and enumerates512 binary outcomes per comparison
using exact rational arithmetic; all margins and fractions agree.

## Result and integration

Retain the exact ending's modified-fish association as a structural observation
that future readings should explain. Keep its incremental components and the
motif's referent unresolved. Neither visual resemblance nor co-occurrence supplies
an independent commodity meaning.

The [complete result](../results/l51_audit.json),
[independent check](../results/l51_independent_verification.json), primary pages,
protocol and reviews are persisted. Recent M-294, pipe-chain and L-51 audits are
also linked into the417-sign evidence index through explicitly conditional
catalogue paths. Ambiguous M/W mappings remain ambiguous; all established
semantic and phonetic values remain null.
