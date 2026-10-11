# Original metal-tool plate audit

Mackay's original **drawings** support the visible graphic groups used in the later three-tool calculation. They do not establish numerical values or a weight interpretation. The **photographs** are a separate, less legible representation; this review does not promote their damaged surfaces into independent confirmation of every stroke.

The [public volume II scan](https://archive.org/details/in.gov.ignca.9954) supplies Plate CXXVI at leaf265 and Plate CXXXI at leaf275 (zero-based Archive leaves). The plate list, printed p.viii/leaf12, explicitly calls CXXVI drawings and CXXXI photographs. Archive metadata dates this volume1937; the paired text volume used for masses is1938. The volume II title-page date was not newly checked.

| Primary drawing | Visible group | Relevant qualification |
|---|---|---|
|CXXVI2, tang conventionally DK7856 |One arch, five upright strokes and four transverse strokes near the lower end of the left depiction |Other complex signs occur above; another inscription is depicted on the opposite face. The transverse group is tilted in the drawing. |
|CXXVI3, small axe DK7855 |Six upright strokes, including one displaced lower at the left |A complex angular sign immediately adjoins the strokes in the same light strip. A staff-like sign and an oval sign are elsewhere on the face. Extracting an isolated `6i` expression is an assumption. |
|CXXVI5, large axe |Seven arches in a vertical column and six upright strokes above |The opposite face has a different complex inscription. Primary catalogue field7535 still conflicts with later DK7835; the secure join is plate/item. |

The small-axe offset stroke is retained, not silently aligned with the other five. On the tang, two stroke orientations are visibly distinct. Neither observation tells us whether their values are equal, unequal, positional, nonnumerical or affected by a larger sign grouping. Local labels `u`, `i`, and `t` describe shapes for comparison with existing equations; they do not identify universal M/W/P signs.

These are counts of **published drawn marks**. The illustrations place signs within light patches on dark object silhouettes and include geometric section views. They are not raw surface photographs. Plate CXXXI photographs show strong corrosion and uneven contrast. Item36 visibly has a column of curved marks, but this scan does not support an independently reliable recount of every target group. Possible visual correspondences CXXXI31→tang,35/36→large-axe faces and37→small axe remain explicitly tentative: this bounded review did not authenticate a printed one-to-one cross-reference. Items38/39 were also inspected without assigning them one of the three target identities.

The original text's group-level reference to CXXXI31,35–39 is not sufficient by itself to make every individual photo join. Nor are a drawing and photograph of one object two independent semantic anchors. The primary7535/later7835 discrepancy is preserved in `metal_original_records.json` and this new ledger; no identification was repaired from shape alone.

This is a source audit after exposure to the proposed counts, **not a blinded test**. It strengthens the documentary basis for those graphic patterns. It does not validate decimal notation, any phonetic reading, a metal weight unit, or the claim that the marks describe the original complete tool's mass.

## Preserved evidence

- `data/processed/metal_plate_audit.json`: item-level observations, uncertainty, source-type evidence, tentative photographic joins and hashes.
- `data/processed/metal_plate_downloads.json`: all8 public downloads, exact URLs, byte counts and SHA256 hashes; total6,083,064bytes. All downloaded files are under `data/raw/`.
- `results/primary_pages/metal-plate-tang.png`, `metal-plate-smallaxe.png`, `metal-plate-largeaxe.png`, `metal-plate-photographs.png`: lossless inspection crops from the downloaded JPGs. No redrawing or sharpening was applied.

| Evidence | SHA256 |
|---|---|
|CXXVI, `data/raw/metal_plate_9954_leaf265.jpg` |`02d3fd1f4dd021a65eddf10b759fa42ab105a70b6320804f5b5471550f80827f` |
|CXXXI, `data/raw/metal_plate_9954_leaf275.jpg` |`217f3c7f6113aef38dcdabd8d3bbbf84f36f743b27194dee8a050d25e71829dc` |
|Plate list p.viii, `data/raw/metal_plate_9954_leaf12.jpg` |`b0dd4982a01886201ffc0adfe9edcccb922d6cda4f60151395853118f67497c6` |

All eight raw hashes and byte counts were checked against the download ledger. The full volume PDF was not downloaded.
