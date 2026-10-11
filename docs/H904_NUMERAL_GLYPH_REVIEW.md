# H-904 and M-331: local curved-sign comparison

28 September 2026. **The original catalogue identifies and photographs H-904, and its curved sign is broadly compatible with the single curved sign on M-331 face B.** Both bend toward the right and open to the left in the published uppercase object views. H-904's outline is more angular. This supplies a positive local graphic comparison; it does not establish a global W899/W900 alias, equal numerical values, a numeral function, or the proposed Figure16 identity.

## Identity recovered without a text-only join

CISI volume2, *Collections in Pakistan* (1991), printed338/PDF373, explicitly labels **H-904 A** and **H-904 B** under the heading for incised tablets without iconography. Its basic-data row, printed444/PDF479, reads:

| Field | Printed entry |
|---|---|
| CISI | H-904 |
| Finnish concordance | 3477 |
| Excavation | J 213 D |
| Museum field | HM 434, 32.3018 |
| Photograph reference | P 1213 |

The column key, printed434/PDF469, defines the second column as Finnish Concordance, not Mahadevan. HM denotes Harappa Museum; italic two-digit-year museum numbers refer to the National Museum of Pakistan accession catalogue after transfer. P denotes photographs by S.M. Ilyas for the corpus project. The exact museum field is retained as printed rather than collapsed into a single unqualified accession number.

The secondary rows **1786.1/1786.2** explicitly name H-904 and give the raw excavation field `J213 (D)477`. The primary row confirms J213 D and the CISI identity. It does **not** print the appended `477` as part of that excavation field, and this review does not guess what that suffix represents. The raw secondary field is unchanged. Finnish3477 is also not a justification for replacing the source article's3786 with another bare integer.

H-904 is therefore now a securely located physical example of the previously screened two-face pattern. The proposed relationship to the article's **Figure16, ID3786** remains a candidate: the article's actual figure has not been inspected in this task. Its arithmetic similarity cannot by itself authenticate that publication identity. The local source row3786.1 still denotes M-1540.

A newly retained author-page text capture, `fuls-numeral-figure-primary-captures.json`, has an additional concrete discrepancy: exposed lines677–678 call the three-long-stroke form Sign032, whereas the local H-904 row assigns **W033** to the three-stroke group and **W032** to two strokes. This is a disagreement between the captured prose and the local coding, not a demonstrated three-versus-two disagreement in the photographs. A prose error, export/version difference or extraction error is not resolved without the actual figure/signary. Matching the number900 across sources likewise cannot alone establish identity. The separate M-331 prose around lines774–778 uses Sign14 in a passage mentioning both five stacked and four short strokes; this review does not force a code reconciliation from that prose.

## Visible marks and coding comparison

H-904 A shows two tall adjacent uprights in the middle-left field and two shorter strokes toward the right, separated by a curved compound form. H-904 B shows a left V-like form, three adjacent tall uprights, a single bent/curved stroke, then further non-stroke signs. These are graphic observations, not counts of represented units. They support the selected stroke groups used in the prior screen without explaining the residual signs or proving any balance between faces.

The retained secondary display-order strings are:

```
1786.1  H-904 A  +740-032-840-002+
1786.2  H-904 B  +700-033-900-645-368-817+
2849.2  M-331 B  +001-899+
```

The H-904 face correspondence is based on the distinctive whole-face patterns in the explicitly labelled photographs. The single bent stroke in B lies between the three uprights and the crossed form; it is the location coded W900 in the secondary row. M-331's corresponding local row codes its curved stroke W899. The latter row-to-face join was already reviewed in `m331_visual_evidence.json`; this task independently reinspects that photographed surface rather than renaming its code.

CISI1 printed84/PDF120 shows **M-331 B** and its impression **M-331 b**. B has a single broad right-bulging curved stroke beside one shorter upright. The impression reverses their left/right order and the curve's opening. CISI1 printedXXIV/PDF28 and CISI2 printedXXV/PDF28 explicitly distinguish uppercase physical faces from lowercase impressions. H-904's published views are uppercase A/B. Comparing H-904 B directly with M-331 capital B therefore avoids manufacturing a mirror difference by mixing an object with an impression.

In these object views, both targets have an open-left, single bent outline, without an obvious interior crossbar. H-904's bend is sharper, approximately chevron-like; M-331's is smoother and more parenthesis-like. Illumination, incised edges, the printed halftone and scan resolution limit the fine terminal comparison. A precise extra basal hook or distinct stroke topology is not securely established in this inspection. The published photographs are not tracings, and their apparent stroke width is not a calibrated ancient feature. No flip, rotation, contrast restoration or reconstructed stroke was used in the new crops.

**Inference:** a shared broad graphic form is plausible and positively supported here. Neither an essential distinction nor complete graphic identity is established by these two surfaces. Even authenticated allography would not independently prove that the sign contributes the same numerical value under two different proposed field rules. Conversely, different modern codes alone do not prove different ancient values.

The secondary feature entry P154 describes a right parenthesis, permits a backward terminal curve, and lists W900 with M287. It lists no W899; the complete feature file contains no W899 entry. This provides a candidate catalogue family for W900, not a primary artifact-level assignment of M287 to M-331 or a globally validated W899↔W900 conversion. No new M77 text identity is inferred from Finnish3477 or shape alone.

## What this changes in the numerical argument

The shared variable v used in the two published equations now has a more concrete **local graphic justification**, but its numerical interpretation, shared value, grouping and alleged equality/total relations remain conditional. It would overstate this review to call the shared-v assumption disproved because of the two export codes. It would equally overstate it to call the shared value proved from a similar curve.

As a separate algebraic sensitivity, independently checked without choosing a reading, splitting the proposed values into vA and vB gives `vA=2S−L` and `vB·L+1=7S+5`. Two infinite positive-integer families obey the minimum-base and digit bounds:

| Parameter range | L | S | vA | vB |
|---|---|---|---|---|
| integer t≥2 | 7t+1 | 4t | t−1 | 4 |
| integer t≥1 | 7t+3 | 6t+2 | 5t+1 | 6 |

Substitution gives respectively `4(7t+1)+1=28t+5` and `6(7t+3)+1=42t+19`, exactly `7S+5`; both also satisfy `0<vA,vB<min(L,S)`, L≥10 and S≥8. The first contains (36,20,4,4) at t=5 and the second (10,8,6,6) at t=1. This proves the importance of fixing the cross-context numerical relation in that model. It does not demonstrate that ancient values actually differed, that the glyphs differed, or that a numerical interpretation was used.

The review script independently reconstructs affine residual and bound coefficients for `results/numeral_identity_sensitivity.json` without importing its producer. Both residuals vanish identically; all eight bound expressions are nonnegative at the stated lower endpoint and nondecreasing thereafter. L increases strictly, proving infinitely many distinct tuples. Solving vA=vB within each family gives only t=5 and t=1 respectively. Saved examples, intersections and input hashes also agree. This is a separate computational validation, not photographic proof or an exhaustive parameterization of every split-value solution.

## Source and artifact limits

The new source result is local: one authenticated H-904 metadata row, its two published faces, and a comparison with the already identified M-331 surface. Fine relief, original reading direction, line segmentation and ancient operations are not established by the displayed orientation. The target curves and neighboring stroke groups are visible, but that does not certify every edge or faint stroke of both inscriptions complete. No capacity or mass is supplied by either catalogue entry inspected here. All semantic and phonetic values remain null.

`scripts/review_h904_numeral_glyph.py` reproduces uniquely prefixed page renders/crops and pins the source PDFs, literal source rows, prior reviews, catalogue features, this report and the inspection images in `data/processed/h904_numeral_glyph_review.json`. The exact crop rectangles and rendering scale are retained. Three PDF pages were newly rendered; existing method/key images were reused. OCR initially failed to locate H-904/J213 in the retained multilingual text; the adjacent known H886–898 page bounded the successful visual search to the next page. No web requests or downloads were made, and no frozen or central file was edited.
