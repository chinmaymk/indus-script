# M-897 candidate: original identity verified, fine crossed-sign reading unresolved

FEM seal545 is **DK9111** according to the original excavation table. Its old
impression shows a comb-like sign, a crossed/diamond-like form, a capped fish,
two strokes and a final oval enclosure. This is broadly compatible with the
secondary M-897 string, but the small, blurred reproduction does not securely
resolve the fine W550-versus-W555 distinction. A damaged W555 interpretation
is not established, and cannot be excluded by this image alone. Keep the raw
transcription visible and its uncertainty separate; do not silently recode it.

## Original identity and context

The new [catalogue page](../data/raw/m897_mackay_leaf408.jpg) is Mackay's
*Further Excavations at Mohenjo-daro*, printed386, Archive leaf408. The
personally checked row545 gives:

- Field number **DK9111**.
- TypeB, steatite (ditto to the material heading at540).
- Dimensions **0.95×0.82×0.29 inches**.
- Block8, HouseII, Room18; level **−16.2ft**.

The dimensions and context are not inferred by splitting the export field
`DK9111545`. The original row explicitly associates545 with9111. The
[retained original plate](../data/raw/ending_fem_plates_leaf207.jpg), XCVII,
labels its corresponding image545; the plate header identifies DKarea,Gsection,
“Impressions of seals. Lower levels.” These two original sources provide the
field-number/image bridge. They do not identify a commodity, workshop, guild,
or precise absolute date.

The export's CISI labelM-897 (row3302.1) and combined excavation string agree
with that bridge, but CISI2's own metadata, museum registration, original-seal
photograph, and a primary Mahadevan text alias were not newly verified here.
FEM545 is a seal number, not a sign number.

## What the impression supports and leaves unresolved

The [crop](../results/primary_pages/m897-fem545.png) retains the printed545.
Its five broad groups are compatible with `W527 W550 W235 W002 W817` in
left-to-right printed-image order. The fish-shaped third group with a cap is
visible and provides a positive fish observation independent of the crossed
sign's finer identification.

The second form has diagonal strokes and a diamond-like outline. The old
impression is much less clear than the modern CISI1 views of M-133 and L-89
used for comparison. Some line endings merge into the dark ground; the cutout
and light/contrast boundaries are not reliable proof that an additional short
stroke was absent from the original. I therefore do **not** certify the
fine distinction as an independently authenticated W550. Conversely, the image
does not demonstrate a break exactly removing a W555 diagnostic stroke, so
there is no evidential basis for automatically replacing W550 with W555/M222.

The export itself records preservation=`fragment`, while complete=`Y` refers
to its textual assessment. Those flags must remain distinct. The plate presents
only an old impression cutout; its apparent edges and missing lower animal
portion cannot safely distinguish physical breakage from the illustration's
cropping. No original-seal or reverse view was inspected to resolve that issue.
The catalogue gives measured dimensions without declaring the inscription
complete. Thus neither complete=Y nor the table dimensions settle the damaged-
sign question.

For the parent's exact-context screen, this is an **uncertain fine-sign witness**:
retain it in a transparent raw transcription analysis, and report a preservation
sensitivity excluding fragmentary objects. If the contextual preference disappears
on exclusion, this object alone cannot restore it through the indistinct plate.
The parent performs that computational test; no new counts are asserted here.

Image order is spatial, not a newly proved direction of reading. No semantic,
phonetic or allographic equivalence is established.

## Reproduction and research log

One source was downloaded into `data/raw/`:
`m897_mackay_leaf408.jpg`, from the exact Archive image endpoint retained in
[`m897_new_sources.json`](../data/processed/m897_new_sources.json), with byte
length and SHA256. Existing FEMleaf207 was reused. No central registry was
modified by this subtask.

[`render_m897_crops.py`](../scripts/render_m897_crops.py) records fractional
coordinates for the unretouched545 plate and table crops. Both resulting crops
were visually checked. The independent India review's M-133 and L-89 crops were
inspected for comparison but did not overcome this image's resolution limit.

Initial local filename search found no existing Mackay leaf408; OCR searches
for9111/545 did not provide a dependable table-row transcription. The direct
page download succeeded on the first page guess and visually supplied the
identity. The plate's small size prevented a stronger fine-sign conclusion;
no image enhancement or invented line restoration was used.
