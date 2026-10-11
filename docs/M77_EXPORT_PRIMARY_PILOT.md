# Two complete Mahadevan lines and an unknown-span case checked against print

**Both selected complete sequences agree with their printed normalized lines,
in right-to-left order.** A third check confirms that `000` preserves an unknown
span, which can represent multiple missing signs. Across the three records,
22 exported segments comprise 20 unstarred sign positions, one doubtful sign
position, and one unknown-span marker. This does not validate the full export,
its translations, or the ancient artifact readings independently of Mahadevan's
edition.

The [ledger](../data/processed/m77_export_primary_pilot.json) retains the complete
raw records, source hashes, per-token comparisons and TableI row locators. All
16 distinct base glyph IDs were compared with the supplied numbered PNGs and the
primary sign forms. No Mahadevan-to-Wells conversion is used.

## Reference 1066

The full page explicitly labels **1066**, followed by code **100101**, under
the Mohenjodaro heading: printed p.41/PDF52. Its complete line matches
`GLI-IND-M77-01066`:

```
+210-086-099-389-060-204-108-358-342+
```

Read the [printed detail](../results/primary_pages/numeral-followup-52-detail.png)
from right to left:

| Position from right | M ID | Observed form |
|---|---|---|
| 1 | M210 | Tiered triangle with central vertical divider |
| 2 | M086 | One long stroke |
| 3 | M099 | Two short strokes |
| 4 | M389 | Branched stem inside oval |
| 5 | M060 | Fish-like form with four exterior short ticks |
| 6 | M204 | Tiered triangle without central divider |
| 7 | M108 | Six short strokes in one row |
| 8 | M358 | U with oblique flag-like caps |
| 9 | M342 | U with outward horizontal ticks |

All nine positions are accounted for. The two triangle forms, two U forms, and
long-versus-short stroke distinction agree. The export has null site metadata;
the primary page supplies Mohenjodaro. This observation does not alter the raw
record.

## Reference 2427

The full page explicitly labels **2427**, followed by **100101**, under the same
site heading: printed p.71/PDF82. Its line matches `GLI-IND-M77-02427`:

```
+307-086-099-086-121-391-391-*402+
```

Read the [printed detail](../results/primary_pages/numeral-followup-82-detail.png)
from right to left:

| Position from right | M ID | Observed form |
|---|---|---|
| 1 | M307 | D-like outline crossed by an oblique extending line |
| 2 | M086 | One long stroke |
| 3 | M099 | Two short strokes |
| 4 | M086 | A second separate long stroke |
| 5 | M121 | Twelve short strokes in three rows of four |
| 6 | M391 | Oval with spokes |
| 7 | M391 | Repeated oval with spokes |
| 8 | *M402 | Slanting stem with wedge attachment; doubtful-reading mark |

All eight positions are accounted for. In particular, the four strokes between
M307 and M121 are segmented as long one / short two / long one, agreeing with
the export. M121 is a separate stacked group.

## Reference 1001: an unknown span, not an ordinary zero sign

The [full page](../results/primary_pages/texts-050.png), printed p.39/PDF50,
clearly labels **1001**, followed by **103511**. Its first line matches
`GLI-IND-M77-01001`:

```
+000-067-072-008-342+
```

From right to left, the printed line contains a hatched block, the M067
fish-like form with upper and lower extensions, M072 with an internal diagonal,
the branched anthropomorphic M008, and the ticked U of M342. All four identified
forms agree with the supplied glyphs. The export's `sign_count: 4` thus agrees
with the four identified sign positions; the string contains five segments only
because it also preserves `000`.

The primary Codes page defines the hatched block as an illegible or lost passage
of **one or more signs**. Thus `000` is an unknown-span marker, not M000 and not
one securely counted missing glyph. The original first line had at least five
signs; its exact length is unknown. Removing `000` would invent a known beginning
for the surviving sequence. Excluding this entire line from a strict
complete-sequence analysis is appropriate.

Reference 1001 also has a **second printed line**, beside continuation code 23,
with a separate glyph. This check covers the first line only, and does not
authenticate the record as a complete representation of the whole artifact.

## Orientation and the star are documented conventions

The [Codes page](../results/primary_pages/context-042.png), printed p.31/PDF42,
states that direction code **1** means right-to-left. Each checked line has that final
code digit. Its note4 defines right/left relative to **seal impressions**, not
the reversed physical sealing surface. The export's first token corresponds to
the rightmost printed glyph in each case.

The same Codes page defines the upper-right prefixed asterisk as a **doubtful
sign reading**. The dot-like asterisk beside the leftmost form in 2427 therefore
supports the export's `*402`. It is not an additional sign or a lost-passage
marker. The drawn form is consistent with M402, but its uncertain identification
must remain uncertain: this inspection cannot remove Mahadevan's qualification.

The original two complete-line checks comprise 16 unstarred positions plus one
doubtful position. Adding 1001 supplies four identified positions and an unknown
span. These selected cases support faithful preservation of these primary
sequences and their uncertainty markers, while leaving whole-corpus accuracy
and every proposed semantic or phonetic interpretation unproved.
