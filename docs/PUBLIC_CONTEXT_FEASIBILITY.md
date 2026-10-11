# Public excavation-table feasibility

11 October 2026. **The new public Mackay table has contextual coverage, but no
strict field-number join to the retained Lipi export succeeds.** This leaves no
eligible inscription–locus–depth records for analysis under the stated identity
rule. It does not show that the objects are different or that contextual analysis
is impossible.

The parent acquired pinned metadata tables from `epachayan/indus-script` under
`data/raw/public-context-oct11-*`. The data dictionary describes AI-assisted
transcription from Mackay 1938 and Marshall 1931; its reported checking did not
independently verify Mackay field numbers or depths. Those quality statements are
source claims, not validations performed here. The retained dictionary and Mackay
build script were inspected; **no external script was executed**.

| Metadata coverage | Count |
|---|---:|
| Mackay rows / distinct seal-number keys | 709 / 709 |
| Mackay rows with some block, house, room or street | 705 |
| Mackay rows with finite numeric raw depth | 705 |
| Mackay rows with both some locus and numeric raw depth | 703 |
| Mackay distinct field keys / duplicated field keys | 695 / 13 |
| Lipi Mohenjo-daro rows / distinct nonmissing field keys | 1,923 / 1,716 |
| Exact normalized field-key overlaps | 0 |
| Eligible joins, including locus-plus-depth joins | 0 |
| Marshall rows / distinct plate-number keys | 560 / 560 |
| Narrative findspot rows / distinct seal-number keys | 130 / 127 |

Normalization only uppercases and removes whitespace. It retains prefixes,
punctuation, suffixes and leading zeroes. A proposed join requires one table row
per normalized field key and one Lipi artifact key. Repeated Lipi rows for the same
artifact are retained as witnesses. A further conservative rule excludes artifact
keys carrying conflicting nonmissing field keys. The complete unmatched and
conflicting records remain in the machine-readable result.

Raw examples illustrate the unresolved key format without asserting identity:
Mackay fields include `DK 10436`, `DK 10323`, `DK 10799`; Lipi's first Mohenjo-daro
fields include `DK4807779`, `DK11340188`, `SD 3225749`, `DK5644209`, `DK107993`,
and `DK12403LVII:41`. Some Lipi strings appear to contain concatenated metadata,
but no stripping, inferred boundary, numbers-only matching or prefix repair was
attempted. All Lipi processing projects immediately onto `id`, `cisi`, `site` and
`excavation-idno`; no signs, texts, translations or proposed readings were used.

`phase_estimate` is computed from depth thresholds, with an SD adjustment of
+2.2 feet. It is not independently excavated phase evidence, and its labels
`Early`/`Late I` are not Early/Late Harappan periods. Raw Mackay depths retain
their area-specific conventions; Marshall depths are below modern surface.
Neither depths nor derived phase labels were pooled across those datums. The
narrative findspots are not independent replication of Mackay's table.

**Decision:** this screen supplies no joined sample and no significance test.
The public table may justify a bounded verification of its primary transcription,
but applying it to Lipi requires an independently justified identifier mapping
first. No outgoing contact, semantic claim, independence claim, or broad artifact
search follows from this result.

Reproduce with `python3 scripts/profile_public_context_tables.py`. The
[result](../results/public_context_feasibility.json) pins source bytes and hashes
and retains metadata exclusions. Seven tests in
`tests/test_public_context_tables.py` cover ambiguous and repeated keys, prefixes,
suffixes, leading zeroes, missing fields, preserved unmatched records and numeric
depth eligibility. Run them with
`python3 -m unittest discover -s tests -p test_public_context_tables.py -v`.
