# W525: two local catalogue correspondences and a corpus-coverage failure

Completed 27 September 2026. **Two independently identified published objects
support W525 → M254 locally. This identifies a catalogue correspondence, not a
meaning or sound.** Primary documentation and unretouched crops are retained in
the [primary review](W525_PRIMARY_REVIEW.md).

| Secondary label | Authenticated primary chain | Finding |
|---|---|---|
| M-1390 | DK8489 → FEM CII15 → M77 2868 | W400–W525–W550 corresponds locally to displayed M176–M254–M216 |
| H-774 | Ab473 → EH C672 → M77 4672 | Same three-group beginning on the separately printed first face |
| H-1123 | Raw9015360 conflicts with original9015 → XCIV356 | Excluded; plate360 exists but is not authenticated as excavation9015 |

The first two chains use original excavation descriptions, numbered photographs,
and Mahadevan's explicit appendix references. The fine numbered sign identification
comes from the authenticated printed transcription and sign list; the old photographs
support object identity and broad arrangement but cannot independently resolve every
stroke. The modern CISI aliases have not been verified against CISI2/3 metadata.

## What the masked search did and did not find

W525 was the most frequent unmapped non-target sign in the preceding pincer
comparison. The saved protocol selected all ten strict Wells rows containing it,
nine of which belonged to that earlier comparison. Each W525 occurrence could match
one M001–M417 sign, with repeated occurrences required to take the same value within
a candidate pair. Other tokens used the existing family memberships, the previously
declared M216/M222 pincer candidates, and the W617 → M245,M245 span rule. No other
unknown token was allowed to act as a wildcard.

The search returned **zero matches among 1,293 strict M77 rows**. After this null
result, the investigation explicitly expanded to a separate diagnostic set: 526
multi-document records with reported right-to-left direction and no doubtful or
unknown tokens. Their flat arrays supplied six source locators, all with M254 in
the masked position. Five Wells rows point to the same M77 record4672; M-1390 points
to2868. This is six compatibility pairs, not six independent confirmations.

Both authenticated examples were outside the strict corpus because their records
contain multiple documents. Inspection shows one three-sign line plus another
document metadata line for2868, and two separately printed faces for4672. The bulk
extraction's flat arrays cannot be treated as an independently certified face-level
corpus. The original strict null remains recorded; it does not refute W525/M254.
The two reviewed anchors are attached separately and do not silently loosen the
strict corpus filter or establish identities for the other four locator rows.

## Consequences for decipherment

The source family table has W526/W527 under P301 with M254, but does not include
W525. These primary examples expose another missing correspondence in that table.
M254 can therefore collect forms separated into several Wells codes. Treating
either catalogue's sign numbers as ancient semantic distinctions would beg the
question: shared numbering does not prove equal sound or meaning, and separate
numbering does not prove different sound or meaning.

The identical W400–W525–W550 three-group sequence occurs on two identified objects
at different sites, one within a longer text. This supports a recurring sign
sequence in the published transcriptions. It does not identify a word boundary,
owner, commodity, grammatical phrase, or shared issuer. The faience tablet and
elephant impression provide context but no independently labelled referent for
the central sign. All established semantic and phonetic values remain null.

The [candidate-family follow-up](COMB_FAMILY_CONTEXTS.md) finds no exact
W525↔W526/W527 replacement counterparts. W525 occurs mostly medially on tablets,
whereas the other forms occur mostly finally on seals. Only one site/type/length
stratum overlaps; removing the disputed H1123 leaves one medial example on each
side, with another sign also differing. This is too little comparable coverage to
separate positional graphic variation from distinct formulas or meanings.

## Reproduction and limits

- [Protocol](../data/processed/w525_protocol.json) records the initial search and
  explicitly labels the later multi-document diagnostic as post-null.
- [Screen](../scripts/screen_w525.py) retains all ten selected rows and all six
  diagnostic locator records in [its output](../results/w525_screen.json).
- [Independent verifier](../scripts/verify_w525.py) imports no production helper;
  it reconstructs position constraints and compares all full rows, alignments and
  summary fields. [Verification output](../results/w525_independent.json) agrees.
- [Primary audit](../scripts/audit_w525_primary.py) verifies 44 evidence hashes,
  checks the two separately documented joins, preserves the rejected identity,
  and retains the historical M254 position profile with its editorial scope.
  [Audit output](../results/w525_primary_audit.json) is linked into the all-sign index.

The search and source review were source-exposed. These are not held-out
predictions. Incomplete catalogue mappings, uncertain photography and incomplete
face recovery limit the inference. All five new downloads are together in
`data/raw/` and registered with URLs, byte lengths and SHA256 in `data/sources.json`.
Raw transcriptions, source family memberships and primary Table I counts remain
unchanged.
