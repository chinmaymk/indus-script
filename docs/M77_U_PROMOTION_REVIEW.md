# Review of primary M328 line promotion

The pilot can support a **separate, uncertainty-preserving reviewed line corpus**. It should not overwrite the one-string export or become a representative sample of Indus texts. Five high-risk primary examples were checked; their indexed side/line labels and uncertainty transcription are supported. No existing source or script was modified.

The 141 indexed rows represent 141 distinct reference/side/line keys and 145 M328 instances. Adding the 83 stored context lines yields 224 unique keys, with two further M328 instances in context lines. These counts describe the existing ledger, not independent artifacts or exhaustive coverage. By current flags, 119 indexed lines are fully checked and free of loss, doubt and reviewer-unknown glyphs; 4316 explicitly retains a candidate-derived prefix and must stay outside this tier.

| Primary example | Verified detail | Promotion consequence |
|---|---|---|
| 1623, PDF576 / printed565 | Side1 line0 has three adjacent U signs; side3 matches the exported string | Three occurrences are one line; export is not assumed to be the first side |
| 4487, PDF576 / printed565 | Side2 line0 has a visible unidentified composite before U, without hatching | UNKNOWN is identification uncertainty, not physical loss |
| 4546, PDF576 / printed565 | Indexed line has LOSS; context has LOSS, *UNKNOWN, M342 | Preserve reviewer uncertainty and primary doubt separately |
| 4660, PDF582 / printed571 | Side1 is loss-only; side2 is M089 M328 and matches export | Do not mark every auxiliary line as omitted |
| 1527, PDF583 / printed572 | Labels11/12 are side1 lines1/2; second line matches export | Preserve line2 and starred M097; do not read12 as side2 |

2847 and 2604, immediately adjacent to the selected examples, display matching strings under distinct references. This does not authorize merging the references into a single line or asserting they are independent artifacts.

## Normalizer issues to handle in the new corpus

The existing normalizer defaults whole-sequence review to true for 93 rows whose source ledgers lack that explicit flag. Their ledger protocols do describe primary visual transcription, so this is a provenance limitation rather than evidence of fabricated review. The new corpus should record the actual supporting ledger statement instead of extending an unconditional default to new inputs.

The normalizer omits the source's complete-line flag and detailed notes. Preserve both: physical completeness is not complete identification. Its exact UNKNOWN test also would miss *UNKNOWN if applied to the real 4546 context row; strip the doubt prefix for classifying the token base, retaining doubt separately. No currently indexed *UNKNOWN row is missed.

4316 correctly retains full_sequence_primary_checked=false. Its source ledger states that only the terminal M089 M328 was independently checked and the prefix came from the candidate. Do not promote that full string as authenticated.

## Safe identities and missingness

Use namespace/reference/side/line as the line key and append token position for occurrence identity. A repeated concordance observation of one object-line is one line; preserve all locators. Conflicting strings require review. Equal strings on distinct lines stay distinct.

Compare the export without assigning it a side in advance. Report an exact uncertainty-aware match, a definite mismatch, or an unresolved comparison. Matching a string does not uniquely locate it if several primary lines share that string. A mismatch establishes that the complete line is not the exported string; it does not establish that all its signs are new. Preserve overlap and selected-line ambiguity separately.

Keep LOSS, UNKNOWN and starred signs in the diplomatic corpus. Use only whole-line reviewed, fully identified and undoubted rows for a strict tier. Never create adjacency across loss or reviewer-unknown slots. Partial verified segments may be analyzed under an explicitly partial protocol.

The [review ledger](../data/processed/m77_u_promotion_review.json) supplies source fingerprints, exact observations and rules. Existing images only were inspected; no downloads occurred.
