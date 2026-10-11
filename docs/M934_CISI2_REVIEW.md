# M-934 in CISI2: photographs recovered, field-number conflict retained

The newly available CISI2 original and impression **confirm M-934's five-sign composition and reversed-comb comparison with L-89**. They also expose an unresolved field-number discrepancy: **CISI2 prints DM56; Marshall's original seal158 table prints DM50**. Both readings are clear in their respective scans. This follow-up does not decide which is correct or silently repair either source.

## Exact CISI2 entry

CISI2, *Collections in Pakistan* (1991), printed p436/PDF471, row M-934 gives:

| Field | Reading |
|---|---|
| CISI label | M-934 |
| Finnish concordance number | 1158 |
| Excavation number | **DM56** |
| Museum/accession entries | MD50.419; MM464 |
| Photograph sources | JL192; impression a: P167 |

The metadata key at printed p434/PDF469 identifies column2 as the Finnish concordance, column3 as excavation data, column4 as museum/accession data, and column5 as photograph provenance. It explicitly cautions that many Finnish numbers agree with Mahadevan's but many differ; therefore the printed1158 is not automatically promoted to a Mahadevan number. The prior separate MIC158→M77 1158 bridge remains based on the authenticated Mahadevan appendix rule in `docs/COMB_VARIATION_REVIEW.md`.

Museum accession50.419 is a separate field and cannot resolve whether the excavation number is50 or56. No explanatory correction accompanies DM56 in this row. The general key discusses excavation-number problems but does not choose a resolution for this object.

## Compare the original report

The retained original Marshall volumeII, printed p403/PDF54, row158 unmistakably reads **DM50**, with the already recorded dimensions0.95×0.95in, depth4ft7in, typeB and white steatite. Its zero is not a six. This reinspection therefore confirms the old review's literal table reading; the earlier review had correctly marked the CISI2 alias as unchecked.

The secondary export's `DM50158` follows the older number50, but that export is not an independent authority for adjudicating the discrepancy. Possible explanations include a typographical error, a catalogue correction, or an excavation-label problem. The inspected sources do not distinguish them. The field-number conflict must remain attached to any combined object record.

## Original and impression photographs

CISI2 printed p90/PDF125 labels two new views **M-934 A** and **M-934 a**. They show the square animal-bearing seal and its impression. In impression order, the five groups are the staggered comb, crossed angular form, capped fish, two short strokes, and internally marked diamond. The animal, its neck ornament and the stand beneath the text also agree in layout with the previously inspected Marshall seal158 impression. This is strong visual concordance between the old illustration and the directly labelled CISI2 object; it is not merely a string-based join.

The new original and impression agree after their expected reflection. Compared in impression orientation with the retained CISI1 L-89 pair, M-934's comb has the opposite stagger arrangement while the other groups retain their relative sequence. No conspicuous missing comb-bearing corner like L-9's is visible in these reproductions. The coarse scan and surface wear still prevent physical autopsy or every-stroke certification. M-934 is square with animal/stand; L-89 is rectangular and text-only, so they remain distinct objects rather than mirrored views of one artifact.

Thus the **directly labelled M-934 photograph now supports the prior graphic comparison**, even though the excavation field is unresolved. Do not describe the modern catalogue as confirming “M-934 = DM50” without qualification. Equally, the field-number conflict does not erase the separately observable orientation contrast. Neither shared context nor image similarity establishes equal sound, meaning, or free interchangeability.

## Attempts and retained evidence

- Read the frozen M934 and comb-variation reports and their machine-readable dispositions before inspecting the new source; none was overwritten.
- Rendered CISI2 metadata PDF471 separately at scale5000 and checked the original Marshall table crop/full page directly: DM56 versus DM50.
- Inspected the CISI2 metadata key to distinguish Finnish, excavation, museum and photograph-source columns.
- Photo navigation PDF124 reached M923–929 (printed89); PDF125 reached M930–937 (printed90) and the target pair. Both full renders are retained.
- A crop attempt with system Python failed because Pillow was unavailable; rerunning with the installed dependency runtime succeeded. An image read while the PDF125 render was incomplete failed; after the same running render finished, the completed image was inspected. No process was restarted or image reconstructed.
- Reinspected the retained old MIC158 impression and the L-89 original/impression crop. All new crops are unretouched and carry distinct `m934-cisi2-` filenames.
- No downloads were needed; the authentic full CISI2 PDF is already in `data/raw/h843_identity_CorpusVol2.pdf`.

Reproduction:

```sh
"$PYTHON" scripts/inspect_research_pdf.py h843_identity_CorpusVol2.pdf --prefix m934-cisi2-meta --pages 471 --render-only --scale 5000 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/inspect_research_pdf.py h843_identity_CorpusVol2.pdf --prefix m934-cisi2-photo --pages 124 125 --render-only --scale 3800 --pdftoppm "$PDFTOPPM"
"$PYTHON" scripts/render_m934_cisi2_crops.py
```

Exact source dispositions and immutable evidence hashes are in `data/processed/m934_cisi2_review.json`. This supplement preserves the older reports as historical evidence, makes the conflict explicit, and assigns no semantic or phonetic value.
