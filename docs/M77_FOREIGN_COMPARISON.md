# Foreign-findspot seals: mixed structural evidence, no translated anchor

The four eligible named-site West Asian seals do not behave uniformly. The Kish
string mostly uses combinations also found in the selected South Asian seals;
the Susa string and two Ur strings contain more unusual combinations. This is
evidence about these transcriptions, not a recovered language or sign meaning.

## Selection fixed before scoring

The [protocol](../data/processed/m77_foreign_comparison_protocol.json) was saved
before the parent inspected the foreign candidate strings or calculated scores.
It was internally prospective, not externally registered or blind. Primary
catalogue review corrected an initial search assumption: the8000-series is
Kalibangan, not foreign. The actual foreign selection contains twelve named-site
references and five whose West Asian provenance is only probable.

Use [the selection ledger](M77_FOREIGN_SELECTION.md) for exact ranges and metadata.
Every foreign reference is retained in the output inventory, including excluded
ones. Quantitative inclusion requires seal object-code1, one export document,
original direction1 or2, at least two tokens and no doubtful sign or unknown span.
The printed/editorial sequence order is already normalized; direction2 is not
reversed again. The Umma sealing, damaged and doubtful rows, and a two-line Ur
object are excluded by these rules. Probable-provenance9901–9905 remain separate.

The domestic reference uses the same filters and primary-reviewed site ranges,
including33 explicit named other-site references. Unknown-provenance9701 is not
silently classified as domestic. This yields1175 source records and1066 distinct
strings. Exact duplicate texts are collapsed. All exact foreign target strings
would be removed globally from training, but none matches a domestic full string.
Archaeologically related copies can remain dependent despite text deduplication.

## Results

Only internal adjacent pairs are scored; there are no invented word boundaries.
The probability model uses fixed add-one smoothing over all417 M codes. Each
domestic control is scored with its own entire unique string removed from training.
Targets are compared with controls of exactly the same length:50 length-eight and
228 length-five strings. The control model therefore has one fewer training string;
this small training-size difference is disclosed, not called perfect matching.

| M77 reference / source findspot | Length | Adjacent pairs unseen in domestic training | Mean transition surprisal, bits | Same-length domestic controls with higher surprisal |
|---|---:|---:|---:|---:|
|9801 / Susa|8|5/7|8.481|0/50|
|9822 / Kish|8|1/7|6.369|34/50|
|9832 / Ur|5|4/4|8.713|8/228|
|9846 / Ur|5|4/4|8.845|2/228|

Higher surprisal means less predictable under this particular model. These are
descriptive reference counts, not p-values, evidence of a named language, or
probabilities that an inscription is linguistic. Six domestic length-five controls
also have every pair unseen after exclusion. Thus even completely unsupported
pairs are not unique to foreign finds. The Kish case also prevents treating every
foreign-findspot string as exceptional under these scores.

Reversed target scores are retained as a direction diagnostic, without selecting
whichever direction fits better. For example,9846 has one attested pair in reverse,
but that does not authorize rewriting the catalogue's direction or normalized text.

## Primary checks and independent archaeological context

The four exported target strings were compared with Mahadevan's printed160/PDF171
and numbered sign forms. Parent review checked all five glyphs of9832 and9846;
the [separate review](M77_FOREIGN_GLYPHS_AGENT.md) checked9801 and9822. The
concordance on printed346/PDF357 additionally supports the short-stroke assignment
M102 in9822. Agreement
with printed drawings is not an artifact autopsy or whole-corpus authentication.

The [artifact review](FOREIGN_ARTIFACT_ANCHORS.md) establishes9801→Louvre SB2425
and9846→British Museum123208. It keeps9832's accession unresolved. Its Gadd1932
item2 must not be confused with Mitchell1986 item2, which describes9846 instead.
The Kish publication warns that finds may have fallen from higher levels; a nearby
cuneiform pommel is a different object, not a bilingual text. The museum questions
whether9846's inscription is an imitation. Consequently shape, production,
chronology, content, names, imitation and transcription remain alternatives to a
language explanation; findspot alone controls none of them.

The [name-anchor review](EXTERNAL_NAME_ANCHORS.md) likewise separates the cuneiform
seal of a Meluhha interpreter from a bilingual inscription. Indus-style manufacture
with cuneiform alone supplies no corresponding Indus sign values. No tested
foreign object independently identifies the owner-name or meaning of its Indus
string. A universal interpretation must explain these objects too, but these
comparisons do not provide the needed translations.

## Reproduce

Run `python3 scripts/analyze_m77_foreign.py`. It writes
[`results/m77_foreign_comparison.json`](../results/m77_foreign_comparison.json),
including every selection decision, target pair count, control score and reversed
diagnostic. The source-selection judgments remain manual inputs.
`tests/test_m77_foreign.py` checks boundary isolation, removal of repeated pairs,
retention of shared training pairs, damage exclusions, probability normalization
and reference ties. Inputs and primary review provenance are fingerprinted.
