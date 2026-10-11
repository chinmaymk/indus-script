# H-133 / W554: primary catalogue review

Review date: 2026-09-27. The original sources support an **artifact-local correspondence between secondary W554 and Mahadevan M226** on the seven-sign seal labelled H-133 in the secondary export. This does not authenticate H-1817, establish a global mapping, identify a meaning, or assign a sound. The candidate had already been found by the context screen, so this is source-exposed authentication rather than a blind prediction.

## Identity chain

Secondary row 1174.1 is labelled H-133, with raw excavation field `8360261` and source-file text `W740 W554 W220 W415 W798 W060 W692`. The concatenated field is not accepted merely by splitting its digits.

Vats, *Excavations at Harappa*, volume I, printed p53 (Archive leaf79), item1 under the Trench IV Stratum I finds, independently describes a rectangular plano-convex steatite seal with seven pictograms, specifies **Plate XCII261 and No.8360**, and gives square I13/7 and depth 2 feet below surface. The original image reads 8360; the retained OCR misreads its first digit as B. Thus the original passage authenticates 8360↔261.

The paragraph also mentions a furnace in square I13/21. That is a different square from the seal's I13/7; this passage does not establish that the seal was in a furnace, workshop, or shared deposit. No such semantic context is inferred. The relative Stratum I assignment is retained without adopting the secondary absolute/period interpretation.

Vats volume II, Plate XCII (retained PDF page192), independently illustrates the long seven-sign object under261. Mahadevan Appendix V, printed p821/PDF830, explicitly maps EH volume II items1–713 to references4001–4713 respectively. This printed catalogue rule establishes EH261→M77 reference4261. These are an excavation number, a numbered plate item and a text reference, not three independently counted objects.

The modern CISI H-133 entry itself was not separately inspected. The H-133 label remains the export's alias; the authenticated primary bridge concerns its quoted field/plate reference and the corresponding text. No museum accession or modern alias is invented.

## Target sign and photograph

Mahadevan printed p104/PDF115 has a seven-sign line under4261. Its second glyph from the left matches **numbered sign226** on printed p34/PDF45: a triangular left half at a crossing, a straight descending right arm, and an upper right arm ending in a small angular turn. This distinguishes the normalized form being cited from merely treating all crossed/triangular signs as interchangeable.

The secondary W554 is also second from the left in source-file order, or sixth in the reversed seven-token comparison order. The printed M77 line and the Vats photograph share the seven-group arrangement, including the U-shaped leftmost group, the crossed triangular second group, and the intervening and rightmost groups. The photograph is small and locally low contrast around the second sign's fine terminal stroke; its exact hook is less secure than in Mahadevan's normalized drawing. The numbered identification rests on the authenticated printed transcription plus numbered sign list, with the photograph corroborating object and layout. The photograph is not treated as an independent re-transcription of every small stroke.

The secondary candidate M77 sequence is `M150 M123 M053 M171 M059 M226 M342` in normalized right-to-left order. This review specifically checks the M226 target against its numbered sign. It does not claim to have independently assigned the other six numbered codes from the primary sign list. No physical-completeness or all-token certification is added to the raw `slightly chipped` preservation label.

## Attempts, limitations and reproduction

- Located the original metadata with retained Vats OCR, which reads `B360`; verified 8360 directly on downloaded leaf79.
- Verified Plate XCII261 on PDF192, the M77 appendix mapping rule on PDF830, the printed4261 line on PDF115 and numbered226 on PDF45.
- Kept whole-page renders and unretouched detail crops. No image restoration, mirroring, generated reconstruction, or sharpening was used.
- Did not pursue the optional modern CISI alias because the bounded primary reference chain and target sign were already resolved. Its verification status remains explicitly false.
- Downloaded one public original-page JPG into `data/raw/h133_vats_leaf79.jpg`. Pending source registration is `data/processed/h133_w554_new_sources.json`; central registry was not edited by this task.

Render commands, using the installed Python and Poppler binaries:

```sh
"$PYTHON" scripts/inspect_research_pdf.py mahadevan_1977_text.pdf --prefix h133-m77 --pages 115 45 830 --render-only --scale 3600 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/inspect_research_pdf.py vats_1940_plates_9842.pdf --prefix h133-vats --pages 192 --render-only --scale 4200 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/render_h133_w554_crops.py
```

Machine-readable disposition, exact page references, limitations and evidence hashes are in `data/processed/h133_w554_primary_review.json`. The new page URL, byte count and hash are in the pending source file. The review assigns no semantic or phonetic value and does not transfer its target correspondence to another W554 occurrence.
