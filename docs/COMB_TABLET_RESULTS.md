# Testing the other sign in the comparable tablet pair

27 September 2026. **Published records support local W195/M054 and W554/M226
correspondences on two other inscriptions. The requested H-1817/H-843 tablet
comparison remains unresolved.**
It cannot presently demonstrate either comb interchangeability or an identical
formula. No meaning or sound has been established.

**Later source update, 27 September:** the full CISI2 was recovered and its
[H-843 entry verified](H843_IDENTITY_FOLLOWUP.md): H-843 is excavation14307,
Harappa Museum269, with published views of its inscribed and crosshatched faces.
The explicit join to M77 5326 is still missing. The
[H-1817 follow-up](H1817_IDENTITY_FOLLOWUP.md) did not recover its original figure.
The earlier failed-search review below remains a dated record of that phase;
its statement that no H-843 photograph was available has been superseded.
The newly inspected CISI2 data also independently confirm the M-735/DK-C3070
alias; the old MIC60→M77 1060 bridge still rests on the explicit appendix rule.

## Why this pair was investigated

The preceding [comb-family context test](COMB_FAMILY_CONTEXTS.md) left only
H-1817 and H-843 in the same site/type/length stratum after excluding disputed
H-1123. Their source-order texts are `W400 W525 W554` and `W400 W527 W195`.
Two codes differ. Before interpreting the comb change, this phase independently
investigated the other change, W554/W195, and the original artifact identities.

The secondary object descriptions also differ: H-1817 is a small rectangular
faience tablet, H-843 a larger prism with triangular section. Their shared
`TAB:B` label does not establish identical physical form or function. These
descriptions remain secondary and cannot substitute for original photographs.

## Primary evidence and unresolved joins

| Case | Evidence | Supported scope |
|---|---|---|
| M-735 / MIC60 | Marshall table60=C3070; explicit M77 appendix rule60→1060; printed rightmost glyph numberedM054 | Local W195/M054 correspondence, qualified by the secondary row's old-publication identity; CISI2 alias not separately checked |
| H-133 / EH261 | Original field8360, seven-sign steatite seal; EH261→M774261; printed second-from-left glyph numberedM226 | Local W554/M226 correspondence on this inscription; no transfer of identity to H-1817 |
| H-843 candidate5326 | Printed M176–M254–M054, crosshatched reverse photograph and sourcePu.63:4394–95; excavation field blank | Useful locator; no14307↔5326 or H-843↔5326 identity bridge |
| H-1817 | Exact fieldH94-2326/Figure26.06 not found in the accessible reports | Original graphic comparison unresolved |

The [M-735 review](M735_W195_PRIMARY_REVIEW.md) retains the table, photograph,
explicit appendix conversion and numbered-sign inspection. The old photograph
supports the arrangement but has weak fine target strokes; exact numbered
identification rests on the normalized primary transcription. The
[H-133 review](H133_W554_PRIMARY_REVIEW.md) documents the second local anchor.
The [tablet source review](COMB_TABLET_PRIMARY_REVIEW.md) preserves the failed
searches and the precise missing joins, without promoting a matching text to
an artifact identification.

The existing feature table omits W195 from the M054/M055 family. Its W554/M226
membership is supported locally, but neither observation validates an exhaustive
global conversion. In particular, replacing W554 with W195 to force the tablet
strings to agree would require additional evidence. Different normalized forms
also do not by themselves prove different sounds or meanings.

## Source-exposed masked search

The protocol was saved after seeing the tablet strings but before target counts
and candidate searches. Each target was masked separately to one M001–M417 sign;
all repeated occurrences had to agree within a candidate pair. Other tokens
required existing memberships, prior pincer candidates, and the declared doubled
grid span. W525/M254 was evaluated both disabled and enabled as an explicitly
experimental extension from two local anchors. No other unmapped code could
act as a wildcard.

| Target and pool | W525 extension | Matched / selected rows | Candidate pair incidences |
|---|---|---:|---:|
| W195, strict | disabled or enabled | 1 / 2 | 1 |
| W195, multi-document locators | disabled or enabled | 1 / 2 | 2 |
| W554, strict | disabled or enabled | 5 / 10 | 81 |
| W554, multi-document locators | disabled | 4 / 10 | 26 |
| W554, multi-document locators | enabled | 5 / 10 | 28 |

The single strict W195 pair is M-735/1060 with M054. H-843 supplies the two
diagnostic locators2868/M216 and5326/M054. Ref2868 is already authenticated as
the round DK8489 elephant-impressed object, so its identity cannot be transferred
to the prism-labelled H-843. The second locator has the promising crosshatched
reverse but the missing excavation bridge described above.

Most W554 pair incidences come from the repeated short `W740 W554` string:
one background position leaves many candidate values. The81 strict pair incidences
reduce to27 distinct (W string, M string, masked candidate) triples, still not
independent archaeological confirmations. The longer strict H-133/4261,
H-680/5099 and M-1087/1319 contexts each suggest M226; H-133 was then checked
against primary sources. Two repeated longer tablet rows H-1146/H-833 point to
the same diagnostic4370/M226 context. All cases, failures and alternatives remain
in the output, without selecting only the expected matches.

With the experimental W525 extension, H-1817 adds the same2868/M216 and5326/M054
locators, neither M226. This does not refute W554/M226: the old comparison corpus
need not contain this modern-catalogued tablet or its exact formula, and the
other local conversions have not been validated globally. It establishes no
H-1817 identity or new W554 value.

## Adjacency and deletion test

In source-file order, W400 immediately precedes W525 in nine rows representing
five distinct strings, and W527 in two rows/two strings. No such W526 adjacency
occurs. None of these seven strings has an exact counterpart obtained by deleting
only that W400 and retaining every other token. This supplies no direct support
for treating W400 as an optional marker in these contexts. Absence from this
limited corpus does not prove that it is mandatory, part of a compound sign,
a word boundary, or a grammatical unit.

## Saved work and checks

- [Protocol](../data/processed/comb_tablet_protocol.json) and
  [screen](../scripts/screen_comb_tablets.py) retain all selected rows, candidates,
  alignments and exact deletion contexts in [the output](../results/comb_tablet_screen.json).
- The [independent verifier](../scripts/verify_comb_tablets.py) imports no production
  helpers. All eight experiments,222 pair incidences,486 segments and deletion
  records agree. It reports duplicate context accounting separately.
- [Primary review audit](../scripts/audit_comb_tablet_review.py) checks evidence
  hashes and keeps local source correspondences separate from unjoined tablet
  candidates. These are research checks, not tests of ancient meanings.
- Downloaded originals and explicitly labelled web-extraction captures are
  together in `data/raw/`, registered with provenance and hashes. Failed HTTP403
  retrievals did not produce original PDF files and are not counted as downloads.

All analyses are source exposed. Earlier proposed translations were accidentally
displayed during the first raw metadata inspection; they were excluded from the
protocol, all analytical inputs, candidate selection and conclusions. Original
transcriptions and family tables remain unchanged. All417 established semantic
and phonetic values remain null.
