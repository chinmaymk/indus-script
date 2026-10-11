# A frozen tablet-length prediction fails on heldout objects

**The exact rule `length = (stroke count + 3)/16 inches` fails outside its selected training trio.** All five predetermined candidates were retained and their primary tabular dimensions recovered. None matches the exact formula. The clearest counterexample is M77 **4405 / EH405**: three long strokes predict **3/8 inch**, while Vats records **0.6 inch** in the table and **5/8 inch** in the narrative linked by excavation number2355. The failure does not depend on the damaged or doubtful candidates.

This is a test of physical tablet length, not of represented quantity. Failure does not refute every numerical interpretation of the strokes or U.

## Protocol and observation order

The parent froze [the protocol](../data/processed/m77_u_length_prediction_protocol.json) after noticing an exact fit in three selected examples,4548/4509/4508. This was prospective relative to the targeted holdout dimension lookup, but was not an externally registered or blinded study.

Before searching Vats for any holdout dimension, this reviewer inspected M77 printed115/PDF126. Reference4476 has the same main text and a **doubtfully read four-long-stroke group**, `*M095 M328`, on side2. Its conditional prediction7/16 inch was saved at **2026-09-23 18:13:27 UTC**, with the frozen protocol hash, in [the preread record](../data/processed/m77_u_length_4476_preread.json). The primary doubt star was not discarded. Main direction is1, auxiliary direction2; displayed M77 drawings are normalized RTL.

The other four counts came from the frozen protocol. No slope, intercept, tolerance or subset was changed after dimension lookup.

## All five results

| M77 / EH item | Long strokes | Fixed prediction, inches | Vats table size, inches | Narrative length, inches | Qualification |
|---|---:|---:|---|---|---|
|4403 /403|3|3/8|0.55 ×0.3|11/20|Explicitly fragmentary|
|4405 /405|3|3/8|0.6 ×0.3|5/8|Oval; no fragmentary condition stated in linked narrative|
|4476 /476|4, doubtful|7/16|0.4 ×0.3|Not recovered|Broken in photograph; conditional count|
|4516 /516|4|7/16|0.55 ×0.3|Not recovered|Two rectangular faces pictured|
|4543 /543|3|3/8|0.4 ×0.3|7/16|Narrative says “similar to543”; exact find-number bridge retained with this caveat|

All five table rows explicitly place the material/color under **white steatite**. The table links403→F8102,405→F2355,516→G262 and543→F1261;476 has no find number or area recorded. The last narrative describes burnt steatite. These entries were transcribed directly from page images, not accepted from OCR.

The M77-to-EH bridge is explicit in AppendixV printed821/PDF830:4001–4713 correspond to EHII items1–713. Numbered photographs were checked on plateXCV/PDF198, XCVI/PDF200 and XCVII/PDF202. The dimension table is VatsI printed347,349–350, held in raw image leaves373,377–378. Table entries headed “similar to” were not substituted for exact numbered items.

For4405, the exact table find2355 joins the narrative on printed109, item6. That narrative calls it similar to its item2 but explicitly supplies2355,5/8 ×5/16 inch, squareM10/20 and depth15ft3in. The bridge depends on the find number, not on visual similarity. Its **5/8 versus3/8** difference also falsifies the prediction when narrative fractions are used consistently.

## Source precision and damage

The source itself has alternative dimension representations, including the training objects:

| Training EH item | Previously read narrative | Newly inspected table |
|---|---|---|
|508|7/16 ×1/4|0.45 ×0.28|
|509|3/8 ×1/4|0.4 ×0.25|
|548|5/16 ×1/4|Diameter0.3|

These records are preserved without silently treating their decimals as exact conversions of the fractions. Small residuals alone may reflect historical measurement or rounding conventions; the rule asserted exact nominal lengths. The large4405 discrepancy survives either representation. No new physical precision, confidence interval or acceptable tolerance is inferred.

4403's fragmentary status is explicit on printed72, item6;4476 is visibly broken and its count is starred by Mahadevan. Both remain in the fixed inventory with separate limitations. Their dimensions cannot be treated as original complete-object sizes. The decisive4405 case requires neither of them. Halftone photographs do not substitute for an autopsy or establish a common mold.

## Reproduction and downloads

Run `python3 scripts/check_m77_u_length_holdout.py`. The script checks the frozen protocol hash, fixed candidate membership, exact rational predictions, download hashes and all residuals; it performs no fitting. It writes [the full ledger](../data/processed/m77_u_length_holdout.json). Source-reading judgments remain manual inputs.

Eight public Archive.org page JPGs were saved only under `data/raw/`. [The download registry](../data/processed/m77_u_length_holdout_downloads.json) gives every exact URL, byte count and SHA-256 for parent registration. Leaves374 and376 were retained although their pages do not contain target rows: archive page metadata near this section is unreliable, so printed page numbers were checked visually. No broad additional volume was downloaded.

The tested size formula is rejected. The underlying same-main-text variation remains evidence for a variable auxiliary field; it still does not identify quantities, units, denominations or phonetic readings.
