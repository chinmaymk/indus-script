# A crossed inscription and the limits of a linear reading

C-40's photographed layout supports a vertical group crossing the height of the
main inscription. It does not establish that the group is a separate quantity
message. The catalogue combines its three arches into one M314 token and its
five short strokes into one M106 token. Treating those codes as an ordinary
adjacent pair loses physical layout; expanding them into eight unit tokens
would add an unproved segmentation.

The [catalogue audit](C40_CATALOGUE_REVIEW.md) authenticates both sides of
M77 6306 and its source join to Mackay plate LXXIV1. The [original excavation
audit](C40_ORIGINAL_REVIEW.md) joins that plate to CH2596A. CISI's printed
metadata joins CH2596A to C-40, Finnish reference5075, accession ASI74.1.76.
These are successive documentary joins, not identities inferred from resemblance.

![Photographed crossed group on side A](../results/primary_pages/c40-photo-A-detail.png)

The retained photograph shows five upright marks above a column of three
downward-opening arches. The column extends above and below neighboring signs.
This inspection followed exposure to the proposed reading. Surface damage,
photographic preparation and the neighboring staff-like mark limit independent
stroke interpretation. No order of engraving or ancient reading direction can
be determined from the crossing alone. The [photographic ledger](../data/processed/c40_photo_review.json)
keeps these observations separate from normalized token assignments.

## Two fields, not one concatenated inscription

| Side | Catalogue field in normalized order | Source qualification |
|---|---|---|
| A /1 | M109 M059 M367 M380 M314 M106 M018 M162 | No printed doubt or loss |
| B /2 | *M129 M287 M086 M065 M067 M403 M087 M342 | M129 explicitly doubtful |

Both fields have eight tokens. Side B was absent from the secondary export and
is now saved in a [separate primary line dataset](../data/processed/c40_primary_lines.jsonl).
The remaining glyphs on either side are not supplied with invented meanings to
make `3u 5i` a complete translation.

The primary concordance also accounts for all five indexed occurrences of the
selected codes M312, M313 and M314, matching their positional totals2,2,1.
This is not the whole family of arch-like signs. M312 and M313 share a `? M102`
context in4802/4804, but the M312 reading is doubtful. There is no fully clear
substitution pair among these five fields. Graphic one/two/three-arch grouping
therefore does not establish numerical values1/2/3 or arithmetic composition.

## A source-motivated sequence test gave no supporting recurrence

Before checking other strings, the protocol selected removal of M314/M106 as
one hypothetical projection of the main text. It also specified all seven
contiguous two-token deletions as comparison cases. No deletion is accepted as
the ancient reading. The entire discovery object6306 was excluded from matches.

The comparison contains2055 nonempty secondary records without doubt or unknown
tokens, representing1519 distinct strings. It includes644 multi-document records
and all object/direction categories; it is a broad candidate sample, not an
authenticated complete corpus or representative linguistic sample.

Neither the source-motivated six-token projection nor any comparison deletion
has an exact match or a match differing at only one token. The original eight-token
string has no other exact match either. Thus this test provides no recurrence
evidence favoring the proposed segmentation. Absence of repetition does not
refute it: a real inscription need not recur, and the export is incomplete.
The result does not justify choosing a different deletion or relaxing the match
criterion until a favorable comparison appears.

## Excavation context does not validate the proposed number

Mackay already proposed35 or36, depending on whether an adjacent mark belongs to
the human figure's staff. He suggested an inventory count conditionally. The
original record supplies no independently established number of possessions
belonging to this inscription's owner and no numerical mass for the axe.

C-40 belongs to pan2596 in courtyard297 at+9.3ft. Ingot C-39 is catalogued as
CH2529H in a different group on the same courtyard floor, at+10.4ft. The report's
37-piece count belongs to group2529 and cannot validate the axe's proposed35/36.
The report also mentions an ingot in pan2596, leaving an unresolved detail against
the exact illustrated-ingot record. Neither shared courtyard nor a tempting
nearby count establishes a quantity anchor. Exact records and caveats are in the
original-source review; no mass was reconstructed from dimensions.

## Reproduction

Run `python scripts/audit_c40_layout.py`. It verifies source fingerprints,
reconciles the selected arch occurrences to Table I, preserves source doubt,
writes primary line records and performs the fixed deletion comparison.
[Protocol](../data/processed/c40_layout_protocol.json) and
[results](../results/c40_layout_audit.json) retain the exploratory scope.
A test guards against matching the discovery object back to itself or accepting
doubtful records as clear evidence.

All417 evidence-index rows retain unresolved semantic and phonetic values.
Sixteen codes receive qualified C-40 field links, and the three selected arch
codes receive their reviewed occurrence records. These annotations provide
source coverage, not additional independent objects or deciphered signs.
