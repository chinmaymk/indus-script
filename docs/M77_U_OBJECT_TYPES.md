# M328 placement and primary object type

All **310 M328-bearing catalogue references** now have object classifications
checked directly against Mahadevan's primary *Texts*. Joined to the complete
recovered concordance, these cover313 lines and323 M328 occurrences. None of the
310 primary type digits disagrees with the secondary export. This verifies that
particular metadata field for this selected set; it does not validate every
exported sequence or every corpus record.

The distribution supplies a new constraint: **the common final placement of M328
is concentrated in sealings and miniature tablets**. The short stroke-plus-M328
format is also confined to those classes in this recovered historical corpus.
Object association does not identify a word, sound or numerical value. A census
selected for M328 cannot estimate its prevalence among all seals or other classes.

## Complete distribution

Counts refer to catalogue references, distinct reference/side/line entries, and
individual sign occurrences respectively. They must not be interchanged.

| Primary object class | References | Lines | U occurrences | Solitary | Initial | Medial | Final |
|---|---:|---:|---:|---:|---:|---:|---:|
| Seal | 16 | 16 | 19 | 0 | 11 | 5 | 3 |
| Sealing | 131 | 133 | 140 | 0 | 5 | 18 | 117 |
| Miniature tablet | 159 | 160 | 160 | 1 | 2 | 3 | 154 |
| Pottery graffiti | 1 | 1 | 1 | 0 | 1 | 0 | 0 |
| Copper tablet | 2 | 2 | 2 | 0 | 0 | 2 | 0 |
| Ivory/bone rod | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| **Total** | **310** | **313** | **323** | **1** | **19** | **29** | **274** |

Thus final-position shares are3/19 on seals,117/140 on sealings and154/160 on
miniature tablets. No M328 occurrence was recovered in the bronze-implement or
miscellaneous classes. This is absence in the M77 M328 census, not an assertion
about all Indus inscriptions discovered since1977.

The pattern persists after restricting to fully identified, undoubted, loss-free
lines: final counts are1/13 U on seals,108/120 on sealings and138/143 on miniature
tablets. Those figures cover10,117 and143 lines, respectively. The complete
sensitivity tables, including exclusion of loss alone, are in the
[machine-readable results](../results/m77_u_object_types.json).

## Exact short fields and counterexamples

The227 clear exact two-sign `[long-stroke sign, M328]` lines split as follows.
Stroke counts describe the glyphs; treating them as numerical values remains a
hypothesis.

| Class | One stroke M086 | Two M087 | Three M089 | Four M095 | Total |
|---|---:|---:|---:|---:|---:|
| Sealing | 0 | 36 | 48 | 9 | 93 |
| Miniature tablet | 1 | 34 | 59 | 40 | 134 |

These227 lines represent only **four distinct strings**, with three shared across
both classes. All227 occur on numbered side2 or3: sealings91/2 and miniature
tablets125/9 respectively. The134 miniature-tablet fields represent133 references,
because5413 contributes two. This supports a repeated auxiliary-side format; side
number alone does not establish its function. Repetition is evidence of a standardized format; it is not227
independent demonstrations of a meaning. Catalogue records may represent related
impressions, molds or repeated text types.

Length alone does not force final placement. Among clear two-sign lines, seals
4231 and6109 carry `[M328 M307]`. Sealings4363 and5250, and miniature tablet5484,
carry `[M328 M059]`. Six sealing lines instead carry `[M345 M328]`, where M345 is a
jar-like form with three internal ticks. These observations show that both the
neighboring sign and object context need consideration. They do not isolate an
object-type effect with the string or site held constant.

A universal terminal-only interpretation fails. Even a separate terminal-only
rule for miniature tablets fails on six observed U occurrences: one solitary,
two initial and three medial. After excluding all doubt, loss and reviewer
unknowns, five nonfinal/solitary occurrences remain. Every such witness is
listed with its complete recovered sequence in the results JSON. A candidate
meaning must account for these uses, repeated U signs and the longer strings,
not merely fit the majority short field.

A defensible working hypothesis is that M328 participates in a recurring short
field that can combine with stroke groups, with other constructions also in use.
Possible quantity, category, unit, name and linguistic analyses remain open.
Neither the catalogue label “sealing” nor final position proves an administrative
transaction, traded commodity, grammatical suffix or particular language.

## Evidence and reproducibility

Object codes were read from numerical column5 of the primary *Texts*, independently
of candidate metadata. The first metadata string has six digits in this order:
object type, side, two field-symbol digits, line, direction. Later entries can omit
the object digit. Such five-digit strings must not be parsed as new object types.
First-line side, line and direction identify that displayed entry only; direction
is not propagated onto the M328-bearing side. Printed normalized sequences are
kept in their existing reading order.

Four manual ledgers partition the target references, with exact metadata, page
locators and hashed evidence images:

- [61 references below4400](M77_U_TYPES_STRUCTURE.md)
- [142 references4400–4999](M77_U_TYPES_NUMERALS.md)
- [100 references5000–5999](M77_U_TYPES_ICONOGRAPHY.md)
- [Seven references at6000 or above](M77_U_TYPES_PARENT.md)

The [analysis protocol](../data/processed/m77_u_type_protocol.json) explicitly
records that an exploratory candidate cross-tabulation preceded primary review.
This was not a preregistered discovery, and no independent-trial significance
test is reported. The missing original Table IV pages remain missing: the present
M328 distribution was reconstructed from underlying *Texts* entries.

Run `python3 scripts/analyze_m77_u_object_types.py` after the concordance recovery,
or run the complete offline pipeline. The script validates exact reference
coverage, rejects duplicates and malformed full metadata, verifies image hashes,
and keeps unverified types unknown. It writes the
[joined line corpus](../data/processed/m77_u_typed_lines.jsonl),
[normalized review ledger](../data/processed/m77_u_primary_types.jsonl) and results.
All sources used were already downloaded; this phase added no raw downloads.


## Later glyph correction

The [counterpart recovery](M77_U_COUNTERPARTS.md) exposed one neighboring-sign
error in the historical U corpus:3234/10 ends in M283, not M280. Primary glyphs and
the sign's own index onPDF544–545 confirm this. All U counts, positions and object
class results remain unchanged. The corrected current transcription is in
`data/processed/m77_primary_reviewed_contexts.jsonl`; the original stage output
retains its historical reading and the correction ledger preserves both versions.
