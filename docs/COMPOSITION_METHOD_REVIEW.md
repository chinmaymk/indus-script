# Composite-sign criteria and a bounded substitution test

Mahadevan’s criteria can support a test of graphical or distributional equivalence, but context substitution alone does not identify linguistic meaning. A further limitation is circularity: his sign boundaries already use distributional evidence, and his normalized texts erase some joined-versus-separated variation.

## Retained primary passages

Source: I. Mahadevan (1977), *The Indus Script: Texts, Concordance and Tables*, retained as `data/raw/mahadevan_1977_text.pdf`. Printed pp15–17 correspond to PDF26–28; all three pages were rendered and visually inspected for this review.

- **p15, sections11.3–11.4:** sequence membership helps distinguish script signs from isolated motifs. Variant classification uses visual similarity, positional and functional characteristics, and gradual or numerous graphic differences. Doubtful variants remain separate signs. These are operational classification criteria, not deciphered values.
- **p16, section11.5:** morphological categories are explicitly conventional; their labels do not establish what objects the signs represent.
- **p16, section11.6:** spacing is the ordinary boundary criterion. Exceptions include closely grouped strokes consistently occurring together; bracketed signs with modifications present on both sides in undamaged instances; and mirror-reflected compounds. The bilateral-bracket requirement is a concrete falsifiable graphical criterion. A clear undamaged unilateral occurrence would challenge its application to that candidate.
- **pp16–17, section11.7:** repeated instances of the same sign count separately. Where signs sometimes join and sometimes remain separate on originals, Mahadevan consistently treats them as independent signs. Consequently, his normalized tokens may preserve neither the physical joining nor the distinction a new ligature test seeks to measure.
- **p17, section11.8:** alternative segmentations of text1218 are evaluated using pairwise frequencies. Mahadevan favors a three-sign segmentation because the competing pairings lack ordinary attestation, with a doubtful exception in2124. This is the author’s argument, not a fresh verification of those counts.
- **p17, section11.9:** integral-sign boundaries are provisional conventions. Possible plural readings and suffix readings are discussed as interpretations, while exceptional ligatures in1332 and5067 do not change his choice to tokenize those signs independently. A catalogue token is therefore not automatically a word, morpheme, phonetic unit, or semantic atom.

## Narrow test to specify before inspecting counts

Choose one visually documented candidate composite C and its proposed components A and B. Fix their catalogue identifiers and the admissible component order from independent image inspection before examining contexts. Do not search many decompositions and report only the best. If graphic evidence leaves order unresolved, retain AB and BA as separate, explicitly corrected comparisons rather than selecting the winning order afterward.

Define one occurrence as one complete, sufficiently legible inscription field on one physical object. Use one occurrence per independent object or die family in the primary analysis; repeat photographs, casts, duplicate catalogue entries and concordance listings are not independent observations. Keep side and line boundaries. Do not join across damage, lost spans, uncertain signs or unrelated sides. Audit the original image for every candidate match, because M77 normalization alone cannot establish a physical ligature.

The proposed primary test is **exact two-sided frame substitution**: identify complete fields `L C R` and `L A B R` whose entire flanking sequences L and R agree. Exclude the uninformative case where both flanks are empty; require at least one explicit flanking sign. Preserve field boundaries, normalized reading order and original image orientation as separate records. Define the numerator as independent matched frames and report every unmatched occurrence as well. Use looser one-neighbor contexts only as a separately labelled exploratory analysis.

A narrow operational positive criterion can be fixed in advance: at least two independent matched frames, occurring on at least two independent object/die families, with the graphical segmentation verified in each witness. This threshold is a reproducibility safeguard, not a statistical significance guarantee. Test whether the candidate has more exact-frame matches than predeclared frequency-, length-, site- and object-type-matched control decompositions; account for every candidate/order tested. Sparse strata should be reported as untestable rather than pooled until a result appears. A held-out object group or source collection is preferable where the same corpus helped define the candidate.

The falsifiable claim is limited: **this proposed decomposition exhibits the preregistered repeated substitution pattern in the available eligible corpus**. Zero or one verified frame fails that operational criterion. It does not disprove that C is graphically composite, because a ligature can have restricted distribution and the corpus is small. Conversely, repeated matches support distributional interchangeability under those constraints, not semantic identity. Contrasting distributions or well-attested incompatible flanks weaken an unrestricted substitution model; a universal claim would need its allowed contexts stated in advance.

## What a positive result would and would not separate

Shape alone can establish a candidate graphical composition. Exact-frame substitution adds evidence that a composite and a sequence occupy equivalent inscriptional positions. With physical joining verified, repeated substitution could support an optional joining convention or abbreviated spelling. It can also arise from alternatives that share a slot, formulaic texts, numerical alternatives, or catalogue normalization. These competing explanations remain until independently discriminating evidence is found.

No context statistic by itself decides whether A and B denote words, sounds, names, numbers, classifiers or nonlinguistic categories. Nor does it establish that the meaning of C is an arithmetic or semantic sum of A and B. Independent anchors, productive predictions on unseen objects, and source-level validation remain necessary. The same distributional evidence used to establish M77 boundaries cannot be counted again as independent validation of those boundaries.

## Attempts, provenance and limits

1. Searched the retained OCR for ligature, composite, compound, combination and basic-sign terms. Hits concentrated in introduction sections11.3–11.9; unrelated animal-motif and frequency-table hits were not treated as composition criteria.
2. Read OCR around lines1540–1815 to locate the passage. OCR corrupted the sign diagrams, so it served only as navigation.
3. Rendered PDF26–28 at scale3000 with the existing `scripts/inspect_research_pdf.py`, prefix `composition-method`, and visually read the complete pages. Outputs are `results/primary_pages/composition-method-26.png`, `-27.png`, `-28.png`, with invocation metadata in `results/composition-method_extraction.json`.
4. No downloads, context counts, decomposition screening, new sign-number assignments, or M316/M317 shape audit were performed. The proposed test and threshold are this review’s recommendations, not Mahadevan’s procedure or an achieved result.

This is a bounded methodology review. The actual examples, all variants and the complete sign list were not re-audited; the p17 frequency argument was not recomputed. The note should not be cited as a primary authentication of any particular composite-to-component mapping.
