# Ending follow-up: primary witnesses, mapping conflict and counterpart tests

**Later follow-up:** [MIC158/DM50 primary inspection](COMB_VARIATION_REVIEW.md)
now supports the M-934 candidate and authenticates its M77text1158 bridge.
The unresolved M-934 references below describe this report’s earlier stage;
CISI2 metadata and global allography still remain unverified.

The comb–crossed-sign ending is a real photographed grouping associated with
modified fish in the selected corpus. Its meaning remains unknown. This follow-up
adds original-image checks, finds a concrete cross-catalogue mapping problem,
and finds no exact deletion pairs supporting an optional-W555 interpretation.
The data do not establish a commodity label, grammatical suffix, word or sound.

## Primary observations and their scope

The [India-volume review](ENDING_PRIMARY_INDIA_REVIEW.md) verifies identities
and selected graphic forms for M-81, L-89, M-133 and L-9. M-81 and L-89 show
the comb–crossed-sign–modified-fish sequence. M-133 has a visibly different
second sign, W550 in the export, followed by modified and plain fish. This is
a photographed positive control outside the exact W527 W555 pair.

L-9 is broken at the comb: original upper right, impression upper left.
Consequently, the export's W526 rather than W527 cannot securely demonstrate
intentional sign variation. Its complete=Y flag also cannot certify the whole
original inscription. The surviving fish-positive observation remains usable.

The [older excavation-report review](ENDING_PRIMARY_PAKISTAN_REVIEW.md)
links FEM photographs60,129,142,583 to the original excavation tables:
DK12110, DK11349, DK11456, DK7402 respectively. Their impressions support
one fish-negative example (60) and three fish-positive examples. Number60's
four-sign text is important: the exact ending does not require a visible fish.
Their proposed CISI aliases M-940, M-1081, M-1351, M-1693 match the secondary
export's field/plate references, but the Pakistan CISI catalogue metadata has
not been checked. These are authenticated FEM objects with qualified CISI joins.
H-459, M-1320, M-833 and M-934 remain without new primary-photo authentication.

These selected photos were located using the existing corpus. They validate
specific surviving shapes; they are not an independently sampled replication.
Mirrored original/impression views represent the same object.

## A checked catalogue bridge: L-89 and M77 text7090

CISI lists L-89 as excavation15337, Finnish6132, LTH SRG1326. Mahadevan's
appendix printed826/PDF835 lists **text7090, excavation15337**. The common
excavation identifier links the objects without equating catalogue numbers.
The primary normalized text is printed151/PDF162. Its five units, read in the
candidate corpus's reading order, are M267 M099 M065 M222 M254. This agrees
with the photograph's spatial order W527 W555 W235 W002 W861 reversed.
The ending comparison specifically supports **W555↔M222 and W527↔M254 on
this artifact**, not a universal one-to-one conversion for every token.

The retained source feature P230 lists W550 and W555 under M216. Mahadevan's
primary sign list separately prints M216 (p33/PDF44) and M222 (p34/PDF45),
with distinct treatments of the open ends of the crossed shape. M222 matches
this ending. Therefore P230 is not an exact, exhaustive conversion table here.
The earlier index link to M216 remains identified as source-family membership;
the new review links M216, M222 and M254 explicitly and flags the conflict.
The source data are not silently rewritten, and W550/W555 are not merged.

Primary normalized lines2060,2129,2142 were also inspected: they show the
comb/M222-like pair, with respectively no fish, modified fish forms, and one
modified fish. Those line observations do not by themselves authenticate an
excavation-number join. A source-exposed census in the candidate M77 export
finds15 rows ending M222 M254. It is retained for future checking, not counted
as15 new independent archaeological witnesses. Only selected lines have been
visually checked. See [mapping evidence](../data/processed/ending_mapping_review.json).

## Counterpart tests

The protocol was saved after the original L51 analysis but before this follow-up's
counterpart counts. The universe has1082 secondary rows: strict, complete-flagged,
complete-preservation, single-row SEAL-type objects with at least two tokens.

For each of nine W527 W555 cases, removing **exactly the second token W555**
produces no complete-string counterpart anywhere in that universe: **0/9**.
This supplies no evidence that W555 is an optional detachable marker. It does
not refute such a function: the corpus is small and incomplete, contexts vary,
and counterpart search requires literal full-string identity.

Two rows place W526 before W555 and have exact W527 substitution counterparts:

| Other first token | Exact W527 counterpart | Result of primary check |
|---|---|---|
| L-9: W526 W555 W235 | M-1351: W527 W555 W235 | L-9 broken at comb; exclude from intact allography evidence |
| M-934: W526 W555 W235 W002 W861 | L-89: W527 W555 W235 W002 W861 | L-89 checked; M-934 still unverified |

After excluding the visually damaged L-9 comparison, one candidate pair remains.
It is a target for primary inspection, not a confirmed allographic equivalence.
Neither pair differs by deletion of W555.

## Retrospective removal of named examples

Removing the paper's named L-51/M-636 examples actually removes only L-51:
damaged M-636 was already outside the eligible universe. The remaining1081
rows contain eight exact-ending cases; seven have fish, all modified forms.
Conditioning on site, literal object type and exact length gives:

| Target | Observed among8 | Conditional expectation | Descriptive upper tail |
|---|---:|---:|---:|
| Fish family | 7 | 3.9125 | 0.0247953 |
| Plain fish W220 | 0 | 1.2143 | 1 |
| U-shaped W705/W706 | 1 | 0.9178 | 0.641097 |
| Fish or U | 7 | 4.2421 | 0.0425493 |

The association survives this particular exclusion. This is retrospective
sensitivity, **not a blind holdout or a semantic significance test**. It does not
remove selection of the ending, fish families or published examples, nor the
grammatical/contextual explanations. The previous same-W527-terminal comparison
remains uninformative about W555's incremental effect because its relevant
strata fix the fish count. A structural association cannot identify its referent.

## Reproduction and next discriminating evidence

Run `python scripts/run_all.py`. The
[audit](../scripts/audit_ending_validation.py) saves every counterpart search,
remaining alternate pair, exact tail and the15-row candidate census in
[ending_validation_audit.json](../results/ending_validation_audit.json).
The [independent verifier](../scripts/verify_ending_independent.py) reconstructs
selection and sequences directly from the raw CSV, checks both pair searches,
and enumerates256 binary outcomes for each eight-stratum exact tail. It agrees
on all comparisons. This is computational verification, not independent decipherment.

Primary review JSONs pin the source pages, crops and review files. Downloads,
including failed source/navigation leads, remain together in `data/raw/` with
URL and hash records in `data/sources.json`.

The strongest next tests are primary authentication of M-934's comb orientation
and a systematic, source-qualified W550/W555↔M216/M222 bridge across all available
shared objects. Semantic progress additionally requires an external referent
that distinguishes a commodity, institution, person or grammatical role. None
of the present photographs provides one. All417 established values remain null.
