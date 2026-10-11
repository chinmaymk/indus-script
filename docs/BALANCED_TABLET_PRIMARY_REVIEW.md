# Balanced tablet examples: different stroke arrangements

28 September 2026. **H-326 and H-924 support three grouped/stacked marks beside the W840-coded form and three long side-by-side uprights beside the W700-coded form. They do not show the same graphic class on both faces.** Equality of their represented quantities remains hypothetical. Consequently these examples alone cannot equate stacked and long marks within every context or reproduce the H-306 contradiction without an additional class-value assumption.

Two physical examples were selected from the previously exposed balanced cases. H-925 was not added as a third photographic validation. The shared pattern was already known from the secondary export, so this is primary corroboration, not a blinded prediction.

## Exact primary locators and identity qualifications

| Object | Photograph | Basic-data row | Printed identifiers |
|---|---|---|---|
| H-326 | CISI1 printed226/PDF262, A and B | printed372/PDF408 | Finnish3564; excavation1171; ASI63.11.79; photographHU564 |
| H-924 | CISI2 printed339/PDF374, A and B | printed444/PDF479 | Finnish4096; excavation `???`; HM296; photographP1104 |

The secondary H-326 rows1348.1/1348.2 have raw excavation field `1171564`. The primary source separately prints1171 as excavation number and HU564 as photograph reference. This makes the concatenated-looking secondary field intelligible, but the raw field is preserved rather than silently rewritten or assumed to be a genuine excavation number1171564.

More materially, the secondary H-924 rows1804.1/1804.2 give excavation3286, while **the primary H-924 row leaves excavation unknown**. The immediately following H-925(1) row gives3286. That adjacent entry cannot authenticate H-924's excavation identity. The explicit H-924 label still securely joins its two displayed faces to its own catalogue record, so the graphic observation does not depend on accepting3286. Finnish numbers are a separate concordance namespace and are not automatic M77 identifiers.

## Marks, contexts and residual signs

Both catalogues classify the objects as incised tablets. Capital A/B labels denote object faces; lowercase labels elsewhere denote impressions. New crops preserve the published orientation, without mirroring, rotation, restoration or contrast manipulation.

**H-924 is the clearer pattern witness.** A shows a left U-like form with upper cross-strokes, a central curved compound form, and three upright marks to its right arranged at two levels: two upper marks and one lower mark. B shows a plain U-like form followed in the displayed order by three long, approximately parallel, side-by-side uprights. This is a visible arrangement difference, not a numerical value difference inferred from modern code numbers. The earlier secondary strings place W840 at the central compound and W700 at the plain U. These are local positional correspondences; this review does not establish global sign aliases.

**H-326 shows the same broad contrast**, with three long side-by-side uprights on B and the three-mark staggered/stacked group to the right of the compound on A. The shorter group's precise stroke endpoints and the left B marker are less clear than on H-924. The object has a conspicuous central notch/loss and an uneven surface, so the export's completeness label must not be treated as a physical certification. No missing stroke is reconstructed, and no claim is made that every part of either face is intact. The pattern is compatible with the retained three-mark transcription; H-924 supplies the stronger independent visual evidence for its arrangement.

The literal source records, in file/display order, are the same for these two objects:

```
A: +740-840-013+
B: +700-033+
```

W013 is the export's three-mark stacked group; W033 is its three-long-upright group. A also includes **W740 as a residual sign**, in addition to the W840 context marker. B has no extra residual token in this parser. Leaving W740 outside the numerical flank does not establish that it is irrelevant to what A communicates. Neither count-three visual grouping proves “three units,” and the two faces are not independently documented as equal quantities.

## Exact class-specific consequence, conditional on equality

Write a for contribution per long stroke in the W700 context, b for contribution per long stroke in the W840 context, and c for contribution per stacked stroke in the W840 context. The proposed equality on each balanced example gives **3a=3c**, hence a=c. H-306's separately reviewed three-long versus two-long pattern instead gives **3a=2b**. Both can hold positively: choose a=c=1 and b=3/2. The implied c/b=2/3 is a consequence of these assumptions, not an established Indus conversion.

If one additionally imposes c=b, the two equations contradict positive a. Thus a universal merger of graphic classes is consequential. If the still-secondary H-1923 equality2a=2b is retained, that also contradicts H-306 regardless of c. Removing H-1923 for a sensitivity calculation does not show its transcription is wrong. Nor does it make the whole remaining dataset primary-validated: H-925 was not inspected as a third object here, and H-326's fine-surface limitations remain explicit.

An independent exact linear-system check of `results/numeral_class_constraints.json` uses no producer imports. From the frozen eligible fields it reconstructs five pure-class equations among twenty candidate groups/six eligible groups; H-904's mixed expression is excluded from the ratio graph. All five equations are inconsistent with positivity. Removing H-1923 yields the normalized solution above. Imposing c=b restores inconsistency. The H-326/H-924/H-925 rows repeat one ratio constraint, not three independent numerical relations; after removing H-1923 there are only two distinct equation patterns. The verifier pins the frozen eligibility selection rather than claiming to independently revalidate all twenty corpus filters or photographs.

Compatibility of a more flexible class/context model is not confirmation of a reading. The numerical assumption that the faces balance, the marker meanings, W740's role, segmentation and the applicability of a common rule across objects all remain open. This review supplies photographs, identity corrections and a precise limit on a previous inference. No semantic or phonetic value is assigned.

## Reproduction and attempts

`scripts/review_balanced_tablets.py` recreates native crops and writes `data/processed/balanced_tablet_primary_review.json` with source hashes, raw rows, count confidence, metadata conflicts and the independent matrix check. Its optional `--render` recreates the five newly rendered pages at4800 pixels on the long edge. The initial CISI1p227/PDF263 locator contained H329–334 and was rejected; the preceding page supplied H326. Initial CISI2p340/PDF375 contained H927–942 and was rejected; the preceding page supplied H924. The inspected non-target CISI2 page remains retained under the same prefix. No new source was downloaded, no central file was edited, and no third physical example was promoted.
