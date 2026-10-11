# Stroke forms in exact inscription frames

**M102 and M106 genuinely share some complete inscription contexts, but the
specific M287 M342 ending does not supply a clean one-sign counterpart in the
unchanged sample.** The stronger positive evidence is a four-sign frame containing
three strokes, four strokes, and two arrangements of five strokes at its variable
position. That makes a related stroke family a reasonable hypothesis to test.
It does not establish what the strokes count, their arithmetic values, or a sound.

## Exact contexts, including alternatives

The analysis uses the same 1,175 eligible domestic seal references and 1,066
complete strings as the preceding chain study. It replaces exactly one position
with a wildcard, retaining both inscription boundaries and every other sign.
Repeated copies preserve their reference lists but count as one complete string.
All 417 possible replacements receive explicit result rows, including zeros.

| Complete frame | All observed occupants of the variable position | Occupants |
|---|---|---:|
| ? M015 | M025, M069, M086, M102, M104, M106, M326, M387, M389 | 9 |
| ? M169 | M100, M102, M104, M106, M107, M112 | 6 |
| M267 M099 ? M162 | M102, M104, M106, M107 | 4 |

These are all three frames shared by M102 and M106 in this sample. Only the last
survives a minimum full-text length of three or four. The first frame's nine
occupants show why a single common neighbor cannot define a numerical class.
None of these lists is claimed to exhaust the ancient allowable inventory.

The longer frame has M102 in references 1091, 2080, 2180, 2354, 4126 and 6214;
M104 in 1143 and 1229; M106 in 1131; and M107 in 1157. The printed catalogue rows
1091, 1143, 1131 and 1157 have now been visually checked, alongside the labelled
signlist. They match the candidate transcription with metadata 100101 and no
loss, doubtful sign, or continuation on those rows.

M102 has three strokes, M104 four, M106 five in one row, and M107 five arranged
three above two. The last two are **kept as different catalogue signs**. Their
matching context and equal visual stroke counts motivate testing possible
allography or numerical equivalence; they do not establish either. Shape counts
are observations, while numerical values are still hypotheses.

## Why the curve ending is a weaker comparison

| Sign immediately before M287 M342 | Distinct complete strings | References | Occurrences with the anchor at the end |
|---|---:|---:|---:|
| M102 | 4 | 4 | 4 |
| M106 | 5 | 7 | 4 |
| M373 | 5 | 5 | 4 |

M373 is included by the same exact-context search, without assigning it a stroke
count or meaning. The two-sign anchor also has to be distinguished from M287 by
itself, which had a broader predecessor inventory in the earlier audit. M104
and M107 occur in 27 and 4 complete strings respectively, but neither appears
immediately before this anchor. This finite sample does not establish that
they were prohibited there or that all stroke forms had identical distributions.

No M102/M106 pair before M287 M342 has the rest of its inscription identical.
For example, 2302 has M391 M099 **M387 M102** M287 M342, whereas 4134 has
M391 M099 **M106** M287 M342. The difference includes an extra M387; treating this
as a controlled one-sign substitution would erase evidence. Reference 2254 also
continues after the anchor with M001, verified in the printed row.

The apparent solus M102 counterpart at 2659 is explicitly doubtful in the source
transcription. Direct inspection of printed page 78/PDF89 confirms the doubt
mark, with metadata 103501; this is not an export-only uncertainty. It stays
outside the strict sample. Missing exact counterparts
do not disprove numerical use: uncertainty, sample restrictions and sparse
survival could conceal them. Conversely, silently accepting a doubtful sign
because it completes the expected pattern would overstate the evidence.

## What can reasonably be concluded

The precise four-sign frame supports a common structural role for this small
set of stroke forms. A number-bearing slot is a plausible interpretation to
investigate, especially given the systematic graphic variation. The present
evidence cannot choose it over category labels, phonetic alternatives, lexical
alternatives or other roles. Even a confirmed numerical function would leave
the neighboring signs, units and values to be independently established.

The non-identification is constructive: replace the four variable signs by four
arbitrary distinct category labels while keeping all strings and reference lists.
Every exact-context observation remains true without any quantity assignment.
Thus these observations alone cannot logically force numerical readings. The
same argument does not prove a nonnumerical reading; both remain underdetermined.
All 417 semantic and phonetic fields remain null.

## Reproduction and checks

The [protocol](../data/processed/stroke_substitution_protocol.json) was saved after
initial exploration and claims no preregistration or independent holdout. Run
`python scripts/audit_stroke_substitution.py` after the
[independent verifier](../scripts/verify_stroke_substitutions_independent.py).
The [result](../results/stroke_substitution_audit.json) retains every target-bearing
full frame, all its occupants, every anchor occurrence, excluded candidates and
all 417 comparison rows. It verifies primary evidence fingerprints and agrees
with a separate exhaustive Hamming-distance algorithm on all shared frames and
occupant reference lists.

The independent algorithm examines 83,691 same-length unordered string pairs,
finding 681 one-position substitutions across all signs and exactly three for
M102/M106. Four regression tests cover changed prefixes, reference duplication,
medial versus final anchors, and agreement with an exhaustive synthetic oracle.
See the [method review](STROKE_SUBSTITUTION_METHOD_REVIEW.md) and
[primary review](STROKE_CURVE_PRIMARY.md) for the independent work and source locators.
No new raw data were required.

The [subsequent five-stroke audit](FIVE_STROKE_CONTEXT_RESULTS.md) tests M106/M107
against long-stroke M096, recovers six omitted primary occurrences and separately
identifies the photographed multi-sided object containing the sixth M107 example.
