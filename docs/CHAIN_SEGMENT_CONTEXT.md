# Context of the surviving multi-sign chain

The segments in the verified chain 2463→2302→4084 recur elsewhere, but they do
not have uniquely established word boundaries. In particular, the three-sign
segment combines two more common overlapping pairs, and the two-sign segment
occurs within a longer repeated four-sign prefix. These observations support
reusable textual material while leaving its linguistic and administrative roles
unresolved.

This is an exploratory follow-up to [the consistency test](CONSISTENT_CHAIN_RESULTS.md),
using the same 1,175 filtered domestic candidate seal records and 1,066 distinct
complete strings. The example was selected from this corpus. Removing its three
complete strings is a sensitivity check, **not an independent validation set**.

## Recurrence and alternative boundaries

| Exact segment | Distinct complete strings | Object references | Strings after excluding the three selected texts |
|---|---:|---:|---:|
|M391 M099 M387|4|4|2|
|M102 M287|9|9|7|
|M391 M099|49|50|47|
|M099 M387|19|20|17|
|M102 M287 M329 M343|2|2|1|

Repeated complete texts are collapsed before counting. Each result also preserves
every occurrence position, reference list and all 417 possible immediate neighbors.
Different complete strings are not automatically independent archaeological events.

The three-sign segment occurs initially in 1088, 1126 and 2302, and after M343 in 2463.
Thus the additional complete examples 1088/1126 supply recurrence outside the chain.
However, the pair M391 M099 also appears in 47 other complete strings after excluding
the example, and M099 M387 in 17. Their overlap at M099 permits several hypotheses:
the three signs could form a unit, could combine smaller units, or could span a
boundary. Frequency does not choose among these possibilities. The fixed frame
M391–X–M387 also occurs with X=M123 in 3091; this is a catalogue-sign substitution,
not evidence that M123 means the same thing as M099 or represents another number.

The four-sign prefix M102 M287 M329 M343 is shared by 2084 and 4084. The chain cuts
4084 after the first two signs. The longer recurrence shows a competing segment
to investigate, without proving that its internal boundary is absent. Conversely,
the two-sign segment also occurs in other positions, so the longer prefix is not
a universal obligatory continuation of it.

Eight further records containing one of the two target sequences fail the
unchanged whole-record filter: 1275, 1454, 2564, 2659, 3010, 4634, 4696, 5119. The output
retains their damage, doubtful-reading and multiple-export-document reasons.
For example, 2659 has a doubtful M102 and is not a clean short-form counterpart.
No damaged context was silently trimmed to produce an extra complete name.

## A quantity-like alternative remains conditional

The catalogue forms M102 and M106 contain three and five strokes respectively.
The sequences M102 M287 M342 and M106 M287 M342 occur in 4 and 5 distinct complete
strings (4 and 7 object references). The former appears finally in all 4 strings;
the latter is final in 4 and followed by M001 in one. It is therefore reasonable
to keep a possible variable stroke group plus recurring sign as an alternative
to a personal-name segmentation.

That is a hypothesis about a subset of contexts. M287 also has non-stroke
predecessors and occurs initially in 3 eligible strings. The data do not establish
that M287 always requires a preceding numeral. Nor do they identify any stroke's
arithmetic value, a counted object, a unit, or what relation the final M342 encodes.
The three- and five-stroke descriptions are visual counts, not validated readings
of the inscriptions as quantities 3 and 5. Existing numerical hypotheses remain
subject to their separate [anchor and counterexample audits](QUANTITY_ANCHORS.md).
The later [exact-context test](STROKE_SUBSTITUTION_RESULTS.md) finds three shared
M102/M106 frames elsewhere, but none before M287 M342 with every other sign held
fixed. Its verified four-sign frame supports a stroke-family hypothesis while
leaving numerical values unassigned.

## Evidence and reproduction

The original three chain inscriptions were already checked against the printed
catalogue. The associated [object-identity investigation](CHAIN_ARTIFACT_IDENTITIES.md)
separately traces their excavation/publication identifiers; equal sign sequences
or catalogue integers alone are not used to join artifacts. The three objects are
two Mohenjodaro seals (DK7722 and DK3463) and Harappa find474. Their published
contexts do not establish a contemporary group or an order of generations.
The runtime audit also verifies the artifact review's 30 evidence fingerprints.

Three additional complete rows are now checked in the primary catalogue:
1088 (printed 41/PDF52), 1126 (42/53), and 2084 (60/71). All have metadata 100101,
with no continuation, doubtful-reading or loss marker on these rows. Their full
candidate sequences match the drawings and labelled signlist. The
[primary review](../data/processed/chain_segment_primary_review.json) pins 12 files,
including full pages, row crops and the signlist. Thus recurrence and the longer
prefix are verified in these printed examples, while their interpretation remains
open. None of the analytical boundaries is a printed word divider.

Run `python3 scripts/audit_chain_segments.py` after the consistency audit. It saves
[chain_segment_audit.json](../results/chain_segment_audit.json), including complete
matching strings, excluded records, position counts, neighbor counts and input
fingerprints. It assigns no meaning or sound. Additional primary-page checks of
the recurrence examples are recorded separately in the review ledger.
