# From tool drawings to catalogue sign codes

The recovered reverse of M77 object 2923 supplies an object-specific bridge between three catalogue codes and Pettersson's local graphic notation. It does not establish numerical values or a universal mapping from stroke orientation to units.

The [artifact identity review](BRONZE2923_IDENTITY.md) joins 2923 to Mackay's *Further Excavations at Mohenjo-daro*, plate CXXVI item 2, conventionally DK7856. This is the already studied surviving chisel tang with reported mass 165.343 g. The identification adds a catalogue connection, not an independent ancient object or mass measurement.

M77 printed p85/PDF96 gives side 2, line 0 as the normalized sequence `M387 M015 M104 M106 M312`. Original direction code **4** is retained. The page prints the normalized signs from right to left; the excavation drawing arranges the corresponding groups down the left depiction of the tang. These are not interchangeable layouts.

| M77 token | Group in CXXVI item 2 drawing | Pettersson's object-specific notation | Limit |
|---|---|---|---|
| M104 | Four tilted transverse marks, above the upright group | `4t` | M77 normalizes these as four upright marks. The code does not preserve this original orientation. |
| M106 | Five upright marks, below the transverse group | `5i` | One catalogue token comprises five drawn strokes; it is not five occurrences of an independently identified unit sign. |
| M312 | One arch below the upright group | `1u` | Arch morphology is supported, but value 10, a mass unit, or an arithmetic operator is not established. |
| M387, M015 | Two preceding complex signs on the same face | Omitted from the selected `1u 5i 4t` expression | Retain both codes and their positions. No reading, function or reason to ignore them is proved. |

This alignment uses the authenticated object join, the sequence of the three conspicuous drawn groups, M77's Texts and sign list, and Pettersson 1999 pp98 and 101 (PDF10 and 13). It is stronger than comparing isolated shapes across unrelated objects. It remains an alignment of published representations, not a fresh reading of original incisions. In particular, the upper complex sign in the old plate looks more open than M77's normalized M387; this review retains M77's classification without claiming that every detail of the complex signs is independently confirmed by the low-resolution drawing.

Pettersson's order `u 5i 4t` runs through the selected groups in the opposite order to the normalized tail `M104 M106 M312`. His additive equation discards this ordering distinction. Accordingly, the bridge records a correspondence of groups, not an ancient reading direction or a segmentation rule. His p98 also explicitly considers whether `4t` might instead be `4i`. M77's shared upright normalization cannot decide that question: it would be circular to infer equal values from the normalized appearance and then use that equality to interpret the original orientation difference.

## The other occurrence on a weighed tool

M77 8301 side 2 line 0 is the single token `M106`, with original direction code **3**. The existing primary crosswalk joins excavation number KLB14983 to CISI K-122 and M77 8301. CISI printed p326/PDF362, face B and its enlargement, and the 2020 excavation report figure 12.1d show five approximately parallel strokes. This supports a second object-specific correspondence, **M106 ↔ K-122's `5i`**. The same code in both inscriptions does not prove identical metrological use across objects, sites, materials or dates.

K-122's published 476 g is a reported surviving mass. The separately retrieved museum candidate's 476.70 g remains only a probable descriptive match; it is not substituted for 476 g here. Nor does an unmarked remainder of the photographed surface prove that no marks were lost.

A useful conditional test now becomes expressible directly in catalogue codes. If the sole recorded M106 on K-122 represents its exact present total mass, then its contribution is 476 g. If the same contribution applies additively and nonnegatively inside 2923 side 2, that side must represent at least 476 g, already greater than the tang's surviving 165.343 g. The shortfall is 310.657 g before assigning any positive contribution to M104 or M312. Thus a shared exact-current-total-mass model fails. This does **not** reject quantity notation: unknown original mass, material or site-specific units, nonadditive expressions, lost signs, or an inscription unrelated to whole-object mass all change the premises. M387 and M015 cannot silently be assumed semantically inert.

## Reproducibility and remaining limits

The structured ledger [tool_sign_bridge_review.json](../data/processed/tool_sign_bridge_review.json) preserves both complete normalized fields, residual signs, object-specific group mappings and SHA256 hashes of inspected evidence. Existing files were reused; no downloads or image transformations were needed. Source normalization, drawing and photograph are distinguished, and no universal sign value is assigned.

This bridge does not cover the other face of either object, authenticate every mark on either ancient surface, supply their original masses, or make the earlier metrological models independent evidence. Its main gain is to connect previously separate corpus and tool records while exposing information lost by normalization.
