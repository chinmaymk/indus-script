# Does a recurring roof mark transfer across sign families?

27 September2026. **The selected corpus supplies no qualifying repeated context
pattern for a common roof modifier across different graphic families.** This is
an evidence-coverage result. It does not show that roofed signs lack a common
function, and it does not identify that function or any sign meaning.

The [shape review](ROOF_MODIFIER_SHAPE_REVIEW.md) fixed six candidate pairs before
this new screen's counts: M059/M065 and M060/M066 (one fish root), M089/M092
(three tall strokes), M137/M138 (cross), M162/M163 (trident), M333/M334 (U with
basal projections). The pairs concern primary representative drawings, not every
variant or original inscription. M158/M159 was removed before counting because
another stroke also changes. The added roof is not equated with standalone M134.

## What was tested

A full frame preserves every sign before and after one target position, with at
least one outside sign. Each pair/frame records plain only, roof only, or both.
The primary analysis also matches the source object code, secondary site label,
length and position. Two unknown site labels are explicitly **not a verified
same-site comparison**. Damage or doubt excludes a whole field; surviving pieces
are never joined. Distinct reference IDs remain locators, not certified dies.

We compare pairs from different graphic roots. A qualifying candidate needs a
frame admitting only the plain forms of both pairs, plus a different frame
admitting only their roofed forms, within the same metadata stratum. Four distinct
reference witnesses must be selectable. Such a four-corner pattern would still
require original photographs and independent-object checks; it would not prove
semantic equality. This endpoint and the exclusions were fixed in the
[protocol](../data/processed/roof_modifier_protocol.json), with prior corpus
exposure acknowledged. The [design critique](MODIFIER_TRANSFER_DESIGN_REVIEW.md)
explains why a high count of matching plain states alone would be inadequate.

## Results and denominator

| Corpus / frame rule | Retained records | Cross-root shared frame incidences | Plain/plain | Roof/roof | Mixed | Discordant | Qualifying candidates |
|---|---:|---:|---:|---:|---:|---:|---:|
| Strict, metadata matched | 1,293 | 1 | 1 | 0 | 0 | 0 | 0 |
| Strict, metadata ignored | 1,293 | 1 | 1 | 0 | 0 | 0 | 0 |
| Complete undoubted export, metadata matched | 2,056 | 3 | 1 | 0 | 1 | 1 | 0 |
| Complete undoubted export, metadata ignored | 2,056 | 3 | 1 | 0 | 1 | 1 | 0 |

These are incidences across14 allowed pair comparisons, not independent artifact
counts. The broader selection includes78 one-token records that cannot supply a
nonempty outside frame; those records remain in the coverage denominator but
contribute no tested frame. The strict selection contains none of those78.

The strict metadata-matched pair/frame states show the main support limitation:

| Pair | Plain-only frames | Roof-only frames | Both forms in frame |
|---|---:|---:|---:|
| M059/M065 | 158 | 104 | 0 |
| M060/M066 | 14 | 10 | 0 |
| M089/M092 | 96 | 0 | 0 |
| M137/M138 | 6 | 0 | 0 |
| M162/M163 | 113 | 2 | 0 |
| M333/M334 | 1 | 2 | 0 |

Many individual fish frames do not create cross-family coverage. The M092 case is
especially clear: primary TableI records it once; its8018 field has loss and is
excluded. A [direct primary reinspection](ROOF_M092_COVERAGE_REVIEW.md) confirms
the roofed three strokes, two short strokes and lost span. Zero eligible complete
M092 fields is not zero ancient use or evidence against a modifier.

The sole strict shared frame is `M109 _`: M059 on4171 versus M162 on1243,1249,5054,
all with unknown secondary site labels. Both are plain forms. The broader corpus
adds `_ M176`, with plain/roofed flanked fish versus roofed X, and `_ M342`, with
plain trident versus roofed basal-U. All are two-token contexts. These extra
cases supply neither a roof/roof-only shared frame nor a qualifying pair of
opposite-state frames. The complete witness ledger retains every reference,
including broader unstratified additions.

## Why the shuffle cannot rescue the evidence

The secondary diagnostic assigns plain-only=-1, roof-only=+1 and mixed=0 and
sums products across shared frames. It shuffles masks only within each pair's
site/type/length/position strata. This preserves frame-mask counts and the
coverage graph, **not** token counts, reference multiplicities, object or formula
dependencies. It is a specified artificial null, not a model of ancient scribes.

The independent verifier enumerates assignments on the shared-frame positions,
then counts allocations to unused positions by exact multinomial coefficients.
Four small exhaustive permutation tests check that calculation. Despite enormous
numbers of possible assignments elsewhere, the exact attainable score sets are:

- Strict metadata matched: `{1}`.
- Strict unstratified: `{1}`.
- Complete metadata matched: `{0}`.
- Complete unstratified: `{-1,0}`.

The first three scores are therefore provably invariant under this shuffle;
there is no useful significance test. The last diagnostic's499 seeded draws give
an upper-tail fraction0.478 with the plus-one correction. It is not evidence for
a modifier and is not the primary endpoint. No threshold or relaxed grouping was
chosen after these results to manufacture a positive finding.

## Direct check of the M176 fields

A [primary reinspection](ROOF_M176_PRIMARY_REVIEW.md) confirms all four selected
first fields in the mixed `_ M176` frame, and records their other sides separately:

| Reference | First field | Other entry |
|---|---|---|
| 4407,5444 | M138 M176 (roofed X) | M087 M328 (two long strokes and U) |
| 4493 | M066 M176 (roofed flanked fish) | M095 M328 (four long strokes and U) |
| 5477 | M060 M176 (plain flanked fish) | Symbol-only side, field-symbol83 |

There are seven script lines and one symbol-only entry across four catalogue
references. Reference5477 has original direction2 even though all normalized
strings are printed in the catalogue's standard order. Source direction agrees
with the export for all four. The EH numbering rule authenticates4407/EH407 and
4493/EH493. Appendix rows give5444 excavation3027(2), photoPu35:3863, and5477
excavation13592, photoPu61:4076. The repeated roof-X records are not presumed to
be independent artifacts or dies.

These complete published entries show why sharing one neighbouring sign does
not make the objects otherwise equivalent. The plain-X corner is missing, and
the extra sides differ. No new fields are silently appended to the frozen
one-field screen. Original artifact images and duplication checks remain needed
before a stronger comparison of these objects.

## What follows

A common roof operation remains a visual hypothesis. The current complete-field
export does not demonstrate its repeated contextual transfer between different
bases. The productive next evidence is authenticated roofed examples for the
rare non-fish families and comparisons of complete multi-sided objects; further
frequency fits to the same sparse intersections cannot supply the missing corners.
A shared contextual effect would still need an external anchor to identify a
meaning such as a quantity, category, sound or grammatical function.

The [producer](../scripts/audit_roof_modifier.py),
[independent verifier](../scripts/verify_roof_modifier.py),
[full results](../results/roof_modifier_audit.json) and
[exact verification](../results/roof_modifier_independent.json) are retained.
All417 signs have explicit coverage rows; only12 are endpoints in this selected
shape test. No unselected sign is declared unimportant or unexplained by a future
system. Every semantic and phonetic value remains null.
