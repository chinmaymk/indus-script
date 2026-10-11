# Capacity-table follow-up: earlier data recovered, visual verification pending

**Wells2015 Table4.1 remains unavailable, but an earlier author-posted paper exposes
relevant dimensions and geometric capacity calculations.** This advances source
recovery; it does not supply a fully checked calibration dataset.

[Fuls2012, *Volumenmaße von Tongefäßen der Induskultur*](https://www.academia.edu/8808307/VOLUMENMA%C3%9FE_VON_TONGEF%C3%84%C3%9FEN_DER_INDUSKULTUR)
reports Wells2009 measurements, each repeated three times, rather than an independent
measurement campaign. Its public extracted text gives the following Table2 values
(manuscript p7):

| Vessel | Sphere, L | Ellipsoid, L | Profile, L |
|---|---:|---:|---:|
| H-372 | 123.6 | 118.8 | approximately121.0 |
| H-371 | 248.7 | 259.1 | 240.6 |
| H-370 | 292.9 | 282.7 | 283.8 |

These are **computed capacities**, not direct fill measurements. Table1 reports
H-371 dimensions85.6/91.4/74/43.5cm and H-37083.6/86.4/85/40cm, in the order maximum
external diameter/external height/internal height/opening diameter. H-372's extracted
row contains61.4,64,33.5; one blank column is unresolved. Do not place that blank
using the expected numerical reading. The paper also gives K-90 a profile-derived
103L using a claimed30cm photographic scale; that scale has not been visually
authenticated here. Its prose and table disagree on the per-stroke value.

A further identifier conflict prevents a clean join: CISI1 printedp372/PDFp408
visually assigns excavation12908 to H-370 and leaves H-372 unknown, whereas the
public Fuls table assigns12908 to H-372 and1033b to H-370. The ledger preserves
both. Extraction error, a source typo, or revised identification remain unresolved;
we have not reassigned capacities to make a numerical relationship fit.

The [machine-readable ledger](../data/processed/capacity_table_followup.json) retains
all cells, source locators, measurement dependencies, access attempts, and original
source leads for H95-2661 and MD-1374. Values are marked as **provisional public-text
transcriptions**. They must not silently replace missing cells in Wells2015 Table4.1.
The available model alternatives should be preserved in any sensitivity calculation;
a favorable model cannot be reported as an independently observed vessel volume.

The legitimate search covered the publisher sample, JSTOR chapters, Perlego, Google
Books, and the author's bibliography/public paper. The
[17-page publisher sample](https://www.archaeopress.com/Archaeopress/DMS/3608E8E0F92C4920AE82709E2A32643F/9781784910464-sample.pdf)
lists Table4.1 but does not contain its page. The author's linked PDF returned
HTTP403; no access-control workaround was attempted. No file was downloaded, so
there is no new raw-file hash or source-manifest entry to register.

The bounded search ends with a useful earlier table and an explicit validation gap.
It establishes neither an absolute numerical value nor a word, unit name, or sign
reading. The existing [quantity-anchor analysis](QUANTITY_ANCHORS.md) remains
conditional on its stated assumptions.

The [subsequent conditional model comparison](CAPACITY_MODELS.md) preserves all
three geometries, reports internal leave-one-pot-out errors, and checks transfer
of the same fitted constant. Original CISI photographs independently corroborate
the three stroke counts; they do not resolve the measurement-table identifier conflict.
