# Shared arches: catalogue coverage and a conditional mass bound

The reported masses contradict a shared additive weight model even when the
small axe's unexplained signs may contribute nonnegative amounts. This is a
stronger conditional result than the earlier calculation that treated their
contribution as zero. It establishes no sign meaning or sound.

The [catalogue review](ARCH_EXTENSION_CATALOGUE.md) authenticates all four indexed
occurrences of M315–M318, reconciled against Table I. M315 is seven stacked plain
arches represented by **one catalogue token**. M316–M318 contain additional
elements; they are not established members of a numerical sequence. M317's
occurrence retains a loss span and doubtful direction. Six complete source fields
are retained in [the separate line dataset](../data/processed/arch_extension_primary_lines.jsonl).
Their overlap with earlier reviews is not additional independent evidence.

The small axe (M77 2924, FEM CXXVI.3) has the field
`M108 M342 M001 M375`. The large axe's reverse (2925.2.0, FEM CXXVI.5) has
`M108 M315`. Both fields are clear in the catalogue. M108 is one six-stroke group;
no expansion into six tokens or semantic unit assignment is made. The large
axe's other side remains separate, including its doubtful M098. The unresolved
7535/7835 excavation-number discrepancy remains attached to the plate-based join.

Let S, L and K denote the reported masses of the small axe, large axe and K121
chisel. The tested interpretation requires:

```
S = A + r       r >= 0
L = A + 7u
K = n*u + q     q >= 0, u >= 0, n > 0
```

A is the same contribution of M108 on both axes. The complete selected fields
must encode comparable masses, and M315 must contribute seven equivalent arch
units. K121 must contain at least n of those same units. These are hypotheses,
not observations supplied by the catalogue. In particular, the photographed
K121 marks do not independently establish two identical arches; see the
[retained photographic review](../data/processed/kalibangan_tool_record_review.json).

Since A <= S and u <= K/n, **L <= S + 7K/n**. This needs neither A=6i nor r=0;
increasing a nonnegative r cannot repair a violation. It does not even require
A to be nonnegative. The weaker n=1 case covers the proposed 1u, 2u and u+2i
interpretations only when any remaining contribution is nonnegative.

The original excavation records give S=262.233 g and L=1910.030 g; K=210 g is a
later published surviving-mass report, not a new weighing. Exact arithmetic
preserves those published decimals, not an assertion of zero measurement error.

| Candidate minimum arch units in K121 | Maximum L allowed | Reported L minus maximum |
|---|---:|---:|
| 1, weaker assumption | 1732.233 g | 177.797 g |
| 2, disputed stronger assumption | 997.233 g | 912.797 g |

Both branches contradict the combined premises for the reported surviving
masses. They do not reject numerical uses of arches in general. Negative
residuals, different units or targets, contextual values, multiplication, and
an additional unencoded contribution to L change the tested model.

For hypothetical missing masses dS, dL, dK >= 0, the necessary condition becomes
`dS + (7/n)*dK - dL >= D`, where D is the last column. If both axe masses are
held fixed, the weaker branch needs K at least 235.399571… g, an increase of
25.399571… g; the stronger branch needs 470.799143… g, an increase of
260.799143… g. These are conditional requirements, **not measured losses**.
Without independent damage bounds, freely adjustable original masses do not
identify units. Increasing the large axe's missing mass worsens the inequality.

A parallel [C39 photograph review](C39_GRAPHIC_REVIEW.md) found no secure new
count or weight anchor. `XXUUU` remains Pettersson's plausible proposed reading,
not an independently authenticated complete transcription. The bounded M77
Appendix V lookup gives no C39 mapping and does not prove global omission.

The [protocol](../data/processed/arch_mass_bound_protocol.json) is explicitly
exploratory, selected after source inspection and prior failures. The
[script](../scripts/audit_arch_mass_bound.py) verifies source hashes, exact axe
fields, flags and all four primary count/position profiles before computing the
[results](../results/arch_mass_bound.json). An [independent algebra review](ARCH_MASS_PROOF_REVIEW.md)
confirms the proof and boundary arithmetic. Its script hash identifies the
earlier reviewed revision; the subsequent changes authenticate catalogue inputs
and export fields without changing the reviewed bound function.

The all-sign index retains null semantic and phonetic values for all 417 signs.
This phase narrows a proposed common weight interpretation and improves source
coverage; it is not a decipherment.
