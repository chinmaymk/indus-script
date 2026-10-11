# Independent visual review of L-51

The inspected photographs support a patterned object with pendant-like projections above a separate four-sign text. A bead necklace is a possible visual interpretation. The photographs do not make that identity certain, nor establish that the text names the pictured object or its material. No semantic or phonetic value follows from this comparison.

## Identity and source navigation

CISI volume 1, printed p249 / PDF285, labels the object L-51 and supplies A (original), a (impression), B (back), and C/D (edges). The page heading includes **unidentified object**. Correct metadata is printed p372 / PDF408: L-51; Finnish number6037; excavation number11358; museum LTH SRG1264; photograph HU1019. The first attempted metadata page, PDF409 / p373, covers L99–266 and is retained as a navigation failure, not evidence for L51. Secondary export row2020.1 gives11358(S058), plateCLIX-C5 and the four-code transcription527–555–231–235.

The [primary image](../results/primary_pages/l51-cisi-285.png) and [metadata row](../results/primary_pages/l51-review-metadata.png) were visually checked. The bulletin's Figure7C label “SRG2,C25” must not be silently equated with the CISI museum accession SRG1264; its contextual interpretation belongs to the separate excavation review.

## Observable features and limits

- The original and impression are horizontally mirrored. The motif remains above the inscription in both. The comb-like sign is original-right / impression-left; the roof-marked fish-like sign is original-left / impression-right. Figure7C reproduces the impression in this same orientation; it does not supply an independent new image or a separate line drawing of the motif.
- The upper motif has a long transverse element with upturned or curved ends, repeated small rounded elements arranged in rows, and a lower fringe of elongated tapering projections. Its repeated organization is visible in both original and impression. Individual boundaries and exact counts are not sufficiently secure at this reproduction quality to promote a bead or pendant inventory.
- The four large lower signs are spatially distinct from the upper motif. The two fish-like forms and two other forms are compatible with the secondary527–555–231–235 sequence in impression display order. Fine sign-variant identity is not independently established by this photograph alone.
- The pictured seal face has a roughly complete rectangular outline, without the major missing corner seen on neighboring L49/L50. Surface texture, wear, relief and reproduction blur obscure details. This is not physical autopsy or a declaration that every original cut survives.
- The Mohenjodaro necklace photograph reproduced in Figure7C has a curved strand and a cluster of pointed dangling components. That offers a shape analogy for the projections. It does not show the same full arrangement of repeated rows as L51, and the figure alone does not independently authenticate the necklace's original stringing or archaeological context.
- The modern necklace on a display bust has several bead rows and a lower fringe. It provides the stronger overall visual analogy, but it is selected modern comparative material, not independent evidence of the ancient motif's referent.

A necklace, a schematic implement, or another repeated-component object cannot be discriminated solely by the selected resemblance. This review does not rank those alternatives quantitatively; doing so would require a defined comparison set and diagnostic features. Even independently establishing a necklace would leave ownership, emblem, commodity, ritual and other text/image relations unresolved. The proposed guild and lapidary-license interpretations are further assumptions.

## Exact scope of the published frequency claim

At the bottom of bulletin printed p19 / PDF25, the inline graphic attached to the claim of **more than80%** contains **both** the comb-like sign and the crossed/triangular sign, matching the provisional secondary codes **W527+W555**. It is not a graphic of W555 alone. The surrounding prose describes a pre-phrase-final sign and a phrase-final combination somewhat awkwardly, but the illustrated pair is explicit. The next clause displays W555 alone when assigning the proposed specialized applicability.

At the top of printed p20 / PDF26, the M-636 illustration and discussion repeat the **same pair** as a terminal sequence. Thus the closest computable reading is seals bearing this particular pair at the displayed ending; a broader W555-plus-any-ending family would be a separately labelled sensitivity analysis. With the secondary display convention and reported right-to-left reading, displayed prefix527–555 corresponds to a reading-order ending. Do not reverse the raw strings silently.

The outcome named by the author is a disjunction: proposed precious-metal sign **or** fish signs in what the author calls the core informational segment. Neither the segment boundaries nor an executable complete corpus denominator are supplied in this paragraph. A whole-text co-occurrence count can test a transparent operational proxy, but should not be labelled an exact replication of unspecified segmentation. A positive percentage also needs an appropriate comparison group before it supports specific semantic association.

## Reproducibility

[Structured review](../data/processed/l51_visual_review.json) records source and image hashes. [Crop script](../scripts/render_l51_review_crops.py) regenerates the five unenhanced crops from retained rendered pages using proportional boxes converted to integer pixels. The images are research evidence excerpts; no restoration or invented strokes were applied. No downloaded files were added by this review.

## Independent numerical check

A second implementation, [verify_l51_independent.py](../scripts/verify_l51_independent.py), reconstructs tokens directly from the raw CSV, uses only strict-subset membership from the processed file, and imports no production audit code. It selects the requested single-row complete seals, deduplicates independently, and explicitly enumerates512 binary outcomes across nine active strata. Production code was available during review, so this is an independent implementation, not a blinded analysis or independent transcription.

[Verification output](../results/l51_independent_verification.json) matches all12 combinations of four targets and three universes:1082 objects,1049 deduplicated text types, and27 objects beginning withW527. Each of the nine strata contains one exposed object. The main fish result is8 observed versus4.162526697 expected, with exact descriptive upper tail649523/82608768. Fish-or-U is8 versus4.492064099, tail19278467/1376812800. Among the same-W527 universe, fish-or-U remains8 observed and8 expected, tail1. Only two nonexposed controls occur in the active matched strata, and both contain the selected union. That comparison has very limited power to distinguish whatW555 adds beyondW527.

The raw illustrated-pair inventory has14 rows:11 positive,2 negative and1 unknown under the source complete-text flag rule. Eleven of fourteen is78.6%; removing the unknown gives11/13,84.6%. The latter denominator is an analyst choice, not an explicitly stated denominator in the paper. M-821 contributes a negative under this rule because its text is flagged complete, but its physical preservation is fragmentary. A conservative preservation sensitivity treats that absence as unknown:11 positive,1 negative,2 unknown; known-only11/12. This does not repair or confirm the published percentage. Primary inspection would be needed to distinguish a complete two-sign text on a broken seal from a truncated inscription. Matched-universe results already exclude this object and do not change.
