# A catalogue token boundary explains some unmatched texts

On the independently authenticated M-81/MIC180 object, the Wells export uses
one W617 token for the doubled-grid form, while Mahadevan's normalized text1180
uses two adjacent M245 tokens. Allowing this specific correspondence recovers
five previously unmatched pincer-context rows. This is a catalogue-encoding
result, not a word division, numerical interpretation or decipherment.

The [primary review](DOUBLE_GRID_PRIMARY_REVIEW.md) establishes the shared
object through **C3133**, independently recorded in the CISI M-81 metadata and
Marshall's table for seal180. Mahadevan's explicit appendix rule connects
MIC180 to reference1180. The similarly numbered Finnish entry is not used as
proof. Primary photos show the doubled grid, and the normalized M77 line shows
two separate grid tokens. The complete candidate sequences are:

- Wells source-file order: W527 W555 W240 W002 **W617** W070 — six tokens.
- M77 candidate reading order: M155 **M245 M245** M099 M067 M222 M254 — seven tokens.

The sequences are in opposite catalogue orders. This comparison changes neither
source transcription. It must not be used to infer that the form meant “two,”
that two written words were present, or that M245 has an established meaning.

## Restricted experiment

The protocol was fixed after inspecting the M-81 discrepancy and before the
new counts. It allows only W617→[M245,M245]. Other positions keep the prior
source-family candidate sets, including the explicitly hypothesized M216/M222
alternatives for W550/W555. There are no arbitrary insertions, deletions,
wildcards, further splits or merges. The source's P268 entry covers W615 with
M241/M245 alternatives but does not cover W617; it is retained unchanged.
The new correspondence is separately declared and remains source-qualified.

Every compatible candidate retains the original Wells position, the one or two
M77 positions it consumes, its justification and the full source rows. A
two-grid segment cannot consume one or three M245 tokens; separate occurrences
keep separate boundaries. Matching text still does not establish object identity.

| Selection | Before: rows with candidates / selected | After: rows with candidates / selected | Candidate pairs after |
|---|---:|---:|---:|
| Prior pincer selection | 36/93 | 41/93 | 66 |
| All strict W617-bearing rows | Not previously screened as this selection | 22/59 | 38 |

All55 prior pincer pairs are preserved. Eleven new pairs concern five rows:

| Source label | Candidate M77 references | Caveat |
|---|---|---|
| H-1767 | 1542,2346,4133 | Source slightly chipped |
| H-49 | 1542,2346,4133 | Candidate matches only |
| M-401 | 1542,2346,4133 | Candidate matches only |
| M-81 | 1180 | Primary object bridge independently authenticated |
| M-980 | 2317 | Source fragment flag |

The first three rows have identical Wells strings W617 W550 W003. Their nine
pairs are a three-by-three context match, not nine new objects or nine independent
confirmations. The five newly matched rows represent only **three distinct
Wells strings**. Different site labels and repeating formulae make identity
inference from these matches particularly unsafe.

Two W617-bearing rows in the original pincer selection, H-1951 and M-1080,
remain unmatched. Overall52 of93 pincer rows and37 of59 W617 rows still have
no candidate. This experiment only shows that a token-boundary difference
explains some earlier failures. It does not explain every missing mapping or
validate the complete W617 inventory. M-81 is the selected motivating example,
so recovering it is a consistency check, not a successful blind prediction.

## Consequences for the investigation

Raw token counts from the two catalogues are not automatically commensurable.
Some apparently different text lengths reflect editorial inventory choices.
Preserve both granularities before comparing frequencies, positions, compounds
or proposed translations. The existing M77 Table I remains an account of M77
units; it is not changed to force agreement with Wells counts.

This supplies a useful limited cross-catalogue rule and more targets for primary
review. It supplies no external referent and no established phonetic or semantic
value. A global conversion needs additional authenticated shared objects,
especially unmatched W617 examples and cases with different grid shapes.

## Reproduction

Run `python scripts/run_all.py`. The
[screen](../scripts/screen_double_grid.py) and
[protocol](../data/processed/double_grid_protocol.json) produce
[all rows and candidate alignments](../results/double_grid_screen.json).
Two tests enforce exact grid consumption and distinct boundaries for repeated
compounds. The independent verifier constructs constrained token slots without
importing the production alignment helper, then compares all candidate pairs.
Primary images, identity evidence and hashes are retained separately from these
computational matches. All downloaded originals remain together in `data/raw/`.
