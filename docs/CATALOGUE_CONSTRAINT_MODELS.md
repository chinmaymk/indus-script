# Which catalogue conversions fit the reviewed examples?

27 September 2026. **A one-to-one conversion between Wells and Mahadevan code
numbers cannot represent the selected reviewed examples. A limited deterministic
span conversion can represent them, but has not been validated globally.** This
concerns modern catalogues; it neither deciphers the script nor rules out any
language or phonetic writing system.

The audit uses ten explicit target correspondences from recent primary reviews,
covering eight Wells codes and six Mahadevan inventory members. It deliberately
does not promote every token in a compatible candidate transcription to a
primary-certified numerical code. The source selection and outcomes were already
known, so this is a formal consistency audit, not a held-out prediction.

| Reviewed Wells code | Local Mahadevan span | Source witnesses |
|---|---|---|
| W195 | M054 | MIC60/C3070/M77 1060 |
| W525 | M254 | DK8489/M77 2868 and Ab473/M77 4672 |
| W526 | M254 | MIC158/DM50/M77 1158 |
| W527 | M254 | L-89/15337/M77 7090 |
| W550 | M216 | M-63/DK8333/M77 3068 |
| W554 | M226 | EH261/8360/M77 4261 |
| W555 | M222 | M-63/DK8333/M77 3068 and L-89/15337/M77 7090 |
| W617 | M245, M245 | M-81/C3133/MIC180/M77 1180 |

These are eight distinct mapping assertions supported by ten selected local
observations. Shared sources and repeated assertions are retained explicitly;
the table is not ten independent confirmations of a global conversion. Some
modern CISI aliases remain unchecked, and several precise numbered assignments
depend on normalized published drawings because the photographs have weak fine
strokes. The original reviews preserve those limits. A subsequent inspection of
the newly recovered CISI2 basic-data page435 independently verifies M-735's
field number DK-C3070; [that narrow update](../data/processed/m735_alias_followup.json)
is separate from these frozen constraints. It does not use equality of the
Finnish and Mahadevan numbers to establish identity.

The later [M934 CISI2 review](M934_CISI2_REVIEW.md) supplies directly labelled
photographs but exposes DM56 in CISI2 versus DM50 in Marshall's seal158 table.
The selected MIC158 constraint above still uses the explicit old-publication
identity and records DM50 as that source's reading. It does not silently identify
the two excavation numbers. The [M897 photo follow-up](M897_CISI2_REVIEW.md)
authenticates its modern alias but leaves the fine crossed-sign discrepancy
unresolved, so the core and sensitivity outcomes below remain unchanged.

## Four models

| Model | Ten core observations | With the uncertain M-897 observation added |
|---|---|---|
| One W token ↔ one M token, injective | Inconsistent | Inconsistent |
| One W token → one M token, many W codes may share an M code | Inconsistent | Inconsistent |
| One W token → a fixed ordered span of one or two M tokens | Consistent on these observations | Inconsistent |
| One W token may correspond to several spans of length one or two | Consistent on these observations | Consistent on these observations |

“Consistent” only means that a table satisfying these selected constraints exists.
It is not a measured error rate or evidence that the table works elsewhere. The
last model can accommodate disagreement by retaining alternatives; that flexibility
does not identify which alternative applies or make it a decipherment.

M-897 is kept outside the core because its secondary W550 versus normalized M222
discrepancy has unresolved fine photographic W550/W555 geometry. Adding it
conflicts with the reviewed W550/M216 observation on M-63. This is a warning about
source consistency and uncertainty, not proof of ancient homophony, variable
spelling, separate meanings, or a defective original inscription. Nothing is
silently corrected or decided by majority vote.

## Short proofs and complete witnesses

1. A single-token conversion preserves token count at each aligned occurrence.
   The reviewed W617 occurrence corresponds to two M245 tokens. That one
   observation violates either single-token model, regardless of the assigned
   names or meanings.
2. An injective conversion requires different W codes to have different images.
   Reviewed W525, W526 and W527 occurrences each correspond to M254. Any two
   different members supply a contradiction to injectivity. Repeated W525
   witnesses do not make this a larger ancient inventory claim.
3. A deterministic span conversion requires every occurrence of a given W code
   to have the same ordered M span. The core table satisfies that condition.
   Adding uncertain W550/M222 alongside W550/M216 violates it. The difference
   is uncertainty in an observation, not a licence to call both meanings true.

The program records every singleton cardinality violation and every conflicting
pair, with source assertion IDs. These are all minimal contradiction witnesses
for the stated models: their restrictions are unary (span length) or binary
(equal W inputs require equal spans; injectivity forbids equal outputs for
different inputs). If none is violated, assigning the observed span to each W
code constructs the finite function; for a relation, retain its set of spans.
Unobserved codes remain unconstrained. No inference is made about a global
bijection over unexamined inventories.

## Implication for the full research goal

Catalogue numbers are editorial units. A decipherment cannot safely treat
agreement or disagreement between those numbers as an ancient distinction
without checking the underlying glyphs and boundaries. The local span model is
a useful candidate representation for future tests, while the different sign
forms and source uncertainties remain available for inspection.

The [primary editorial-method review](COMPOSITION_METHOD_REVIEW.md) reinforces
this limitation. Mahadevan's introduction, printed pp15–17, uses distributional
evidence when classifying variants and deciding some boundaries. It also treats
forms that are sometimes joined and sometimes separate as independent signs in
the normalized texts. Reusing those normalized contexts to prove the same
segmentation risks circularity. The author explicitly leaves integral-sign
boundaries provisional. These inspected statements do not newly verify his
example frequencies or any particular composite decomposition.

This audit constrains only M054, M216, M222, M226, M245 and M254. Its output also
has a row for every M001–M417 identifier, explicitly marking the other 411 as
unconstrained **by this selected audit**, rather than claiming they lack evidence
elsewhere. Every semantic and phonetic value remains null. No global conversion
is applied to the corpus, and raw transcriptions and feature memberships stay
unchanged.

## Reproduction

- [Protocol](../data/processed/catalogue_constraint_protocol.json).
- [Audit script](../scripts/audit_catalogue_constraints.py) and
  [full assertions, witness sets and 417 coverage rows](../results/catalogue_constraint_audit.json).
- The script reads the explicit target fields from the source reviews, verifies
  their evidence hashes, and stores the review paths with every assertion.
- Focused tests distinguish cardinality, injectivity, deterministic order,
  duplicate observations and a multi-valued relation.
- The [independent verifier](../scripts/verify_catalogue_constraints.py) reconstructs
  the targets from named source fields and uses set-based consistency and
  exhaustive subset enumeration. All241 checks,184 source-pin checks and417
  coverage entries agree in [its output](../results/catalogue_constraint_independent.json).

No new downloads are needed for this model audit. The separate source-recovery
follow-ups retain their own evidence and conclusions.

The [H-843 follow-up](H843_IDENTITY_FOLLOWUP.md) recovered the actual CISI2 and
authenticated H-843/14307/Harappa Museum269 plus its inscription photograph.
Its curved rightmost glyph broadly agrees with the M054 candidate, but no new
exact numbered assignment is promoted and its explicit M77 5326 join remains
missing. The [H-1817 search](H1817_IDENTITY_FOLLOWUP.md) remains unresolved.
These later observations do not change the ten frozen model constraints.
