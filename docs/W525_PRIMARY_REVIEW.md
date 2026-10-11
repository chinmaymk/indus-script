# W525 primary-source review

Review date: 2026-09-26. Source-exposed inspection of retained printed pages and photographs, not physical autopsy or a blind prediction. This review supports **local W525 → Mahadevan M254 correspondence on two identified published objects**. It assigns no meaning, sound, numeral, or global equivalence rule. The modern CISI aliases are taken from the secondary export; no CISI volume 2/3 entry was independently inspected here.

## M-1390 / DK8489 / FEM CII15 / M77 2868

Secondary `lipi_inscriptions.csv` row 3684.1 is labelled M-1390, raw excavation `DK8489102.15`, and text `+400-525-550+`. The primary report independently resolves the concatenation: Mackay, *Further Excavations at Mohenjo-daro*, printed p363, states No.15 (DK8489), pottery, diameter 1.1 inches, thickness 0.25 inch, First Street (11), level −19.9 feet. The paragraph describes a square seal impression with an elephant and three signs above it, and a deeply incised winged figure on the reverse. Its subsequent paragraph explicitly relates Plate CIII items8–15 to the preceding descriptions under CI/CII. The report's interpretive suggestion about the reverse figure is not adopted.

Plate CII labels the object 15a/b and shows the elephant impression and reverse. Plate CIII independently reproduces both faces under15. These agree in round outline, elephant composition, three upper sign positions, and distinctive reverse figure. The old reproduction is weak around the middle sign; it does not independently settle every stroke or exclude wear. No restoration, reflection, contrast enhancement, or generated reconstruction was used.

Mahadevan Appendix V printed p818/PDF827 explicitly maps FEM CII item15 to reference2868. This is distinct from FEM CI item15, which maps to2855. On printed p84/PDF95, reference2868 has one three-sign line above an additional document metadata line. The printed glyphs from left to right are **M176, M254, M216**, checked against the numbered sign list at printed pp33–34/PDF44–45. This is the same spatial sequence as secondary W400–W525–W550. The normalized right-to-left sequence is M216–M254–M176. The second metadata line is not a second three-sign inscription and is not concatenated.

M254 in the numbered sign list consists of two uprights joined by three crossbars, with the left upright projecting above and the right below in the displayed orientation. This provides an explicit numbered identification for the central sign. The photographs corroborate the published object and broad three-sign placement; the exact numbered glyph identification rests on the authenticated Mahadevan transcription and sign list, not on imagined detail in the low-contrast photograph.

## H-774 / Ab473 / EH C672 / M77 4672

Secondary rows1666.1/1666.2 are labelled H-774, raw excavation `Ab473672`, with two six-unit faces. Vats, *Excavations at Harappa*, printed p23 (Archive leaf49), explicitly identifies Ab473 as a tiny rectangular faience sealing inscribed on both sides and gives Plate C672. The surrounding sentence associates the find with Stratum II in extension Ab. This verifies Ab473 +672 rather than guessing a split as Ab4736 +72. The secondary depth of −4 feet is not independently established by this paragraph.

Vats Plate C/PDF208 shows two faces together under672. On the upper photograph the leftmost E-like group, adjacent central stepped/ladder-like group, crossed group, and remaining strokes and signs are broadly compatible with the six-unit text. Fine stroke confidence is limited by the small, worn-looking photographic reproduction. This review does not newly certify the secondary preservation label `complete` or every token on either face.

Mahadevan Appendix V printed p821/PDF830 explicitly maps EH volumeII items1–713 to refs4001–4713 respectively. This authenticates EH672 →4672 through a catalogue rule. On printed p126/PDF137 the upper line under4672 has six groups; its leftmost three glyphs are **M176, M254, M216**, matching the W400–W525–W550 beginning of secondary row1666.1. The second six-sign face is separately printed below. It must not be collapsed with the first. This is a second artifact-local W525→M254 anchor at a different site, and a useful directly inspected face boundary even though the bulk extracted multi-document record remains outside the strict computational corpus.

## H-1123 / raw9015360: unresolved identity conflict

Secondary rows313.1/313.2 label H-1123, raw excavation `9015360`, texts `+525-550-220+` and `+700-032+`, with J9/3, −13feet, Stratum VI. Original Vats printed p33/Archive leaf59, item4 of the VIth-stratum list, explicitly says **No9015, Plate XCIV356**, a rectangular faience sealing with four pictograms on one side and three on the other, J9/3, depth13feet. The printed number is356, not an OCR-only confusion.

Plate XCIV/PDF196 separately illustrates356 and360. Their faces visibly differ. Number360 has a three-group upper face and a U-shaped form with two strokes below, broadly compatible with the secondary two-face pattern. Mahadevan printed p109/PDF120 ref4360 likewise has a three-sign line beginning in displayed order with M254 and M216, followed by a fish-shaped sign; another U-plus-two-stroke line follows. Under the explicit EH rule,4360 corresponds to EH360. This confirms the existence of the tempting plate360 locator but **does not connect excavation9015 to360**.

Consequently H-1123 is not counted as an authenticated same-object anchor. A primary misprint, later catalogue correction, or erroneous secondary concatenation is possible; the available evidence does not choose among them. The secondary plain-fish coding is also not forced onto Mahadevan's modified fish drawing. No field number, plate reference, or W220 value is silently corrected.

## Attempts, results, and reproducibility

- Located DK8489 using existing Mackay OCR, then verified the original p363 image and both CII/CIII illustrations. Corrected preliminary OCR-based locus `(1)` to visually verified `(11)`.
- Verified the appendix bridge to2868 and directly inspected its printed line and numbered M254, M176, M216 signs. Candidate extracted codes were source locators, not primary evidence or blind tests.
- Initial Vats PDF198 navigation reached Plate XCV; PDF197 was a blank verso with show-through. Both failed-navigation renders remain retained. Correct Plate XCIV is PDF196.
- Verified the9015→356 statement in the actual page and compared the separate356/360 photographs; result was an unresolved identity conflict rather than an accepted anchor.
- Extended to optional H774 after the initial identity conflict. Verified original Ab473→C672 metadata, paired photographs, the EH appendix rule, and the separated upper/lower4672 text lines.
- All five newly downloaded page JPGs are together in `data/raw/`; exact Archive URLs, byte lengths and hashes are in `data/processed/w525_new_sources.json`. Central source registry was not changed by this review.
- `scripts/download_w525_sources.py` retains downloads and pending provenance. `scripts/render_w525_crops.py` produces unretouched fractional-coordinate crops. Full PDF renders use `scripts/inspect_research_pdf.py`; extraction manifests record raw PDF hashes, page numbers and scale. Visual inspection occurred after rendering; the generic manifest's automatic-verification warning remains correct.

Render recipes (with `PYTHON` and `PDFTOPPM` set to the installed runtime binaries):

```sh
"$PYTHON" scripts/inspect_research_pdf.py mahadevan_1977_text.pdf --prefix w525-m77 --pages 95 --render-only --scale 4000 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/inspect_research_pdf.py mahadevan_1977_text.pdf --prefix w525-m77-h --pages 120 137 830 --render-only --scale 3500 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/inspect_research_pdf.py vats_1940_plates_9842.pdf --prefix w525-vats-xciv --pages 196 --render-only --scale 4200 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/inspect_research_pdf.py vats_1940_plates_9842.pdf --prefix w525-vats-c --pages 208 --render-only --scale 4200 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/render_w525_crops.py
```

Machine-readable disposition and immutable evidence hashes: `data/processed/w525_primary_review.json`. This review leaves all semantic and phonetic values null and does not promote the unreviewed W525 occurrences, other modern tablet aliases, or the entire M254 family.
