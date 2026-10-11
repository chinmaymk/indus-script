# Recovery and original-report review of four Pakistan-held candidates

Four older Mackay impressions are now located and checked personally against
printed excavation tables. They support the fish-negative four-sign reading of
FEM60 and fish-bearing readings of FEM129,142,583 at the broad shape-class
level. The CISI Pakistan volume has not been authenticated in this recovery.
The correspondence to CISI labels below still depends on the secondary export's
excavation/plate identifiers, checked for consistency with these original sources.
No semantic or phonetic values are assigned.

## Download provenance recovered after interruption

The previous reviewer stopped before recording thirteen downloaded files. The
recovery script reconstructed twelve image URLs from the retained Archive item
metadata and leaf-number filenames, downloaded them again, and confirmed exact
byte equality to every retained JPEG. SHA256, byte lengths, URLs and recovery
method are in [`ending_pakistan_new_sources.json`](../data/processed/ending_pakistan_new_sources.json).

The thirteenth file, `ending_cisi2_metadata.json`, embeds Archive identifier
`corpus-vol-2`, but its description/title and listed PDF identify **Volume1**.
It is a failed Pakistan-volume lead. Its endpoint URL was inferred from that
embedded identifier and is explicitly marked as not byte-reverified because the
metadata endpoint is dynamic. It must not be cited as a verified Volume2 source.
No additional unique downloaded files were created during this recovery.

## Personally verified identities

| FEM number | Plate / image leaf | Text table printed page / leaf | Field number | Original table details | Secondary candidate |
|---|---|---|---|---|---|
| 60 | LXXXIV /181 | 371 /393 | DK12110 | B; steatite; 0.82×0.82×0.28in; block19, house—, room9; −4.7ft | M-940, row2243.1 |
| 129 | LXXXV /183 | 373 /395 | DK11349 | B; steatite; 1.2×1.2×0.3in; block16, houseII, room15; −6.8ft | M-1081, row3455.1 |
| 142 | LXXXV /183 | 374 /396 | DK11456 | D; steatite; 1.35×0.56×0.4in; between blocks14&15; −7.1ft | M-1351, row3652.1 |
| 583 | XCVII /207 | 387 /409 | DK7402 | B; steatite; 1.25×1.25×0.4in; block3, houseIII, room38; −17.4ft | M-1693, row2359.1 |

The number for60 is **12110**, not1211. Export strings such as `DK1211060`
combine field and FEM numbers; they are not single field identifiers. None of
these field numbers is automatically a Mahadevan text number.

The plates explicitly say “Impressions of seals.” LXXXIV/LXXXV are labelled
DK area,G section,upper levels; XCVII is lower levels. These broad headers and
the table levels are not converted into precise dates, workshops or commodities.
Only the old impressions are reviewed here: there is no newly authenticated
CISI original/impression pairing or museum registration for these four objects.

## Personally verified shape observations

- **60:** Four groups are visible: comb-like sign, crossed/angular sign,
  two short strokes, then a leaf/oval enclosure with interior mark. This is
  compatible with the export's `W527 W555 W002 W817`. No fish silhouette
  is visible in these four positions. The illustrated square face appears to
  have no gross missing text-bearing corner. This supports a photographed
  fish-negative candidate for the exact ending; it is not proof that every
  conceivable original sign is perfectly preserved.
- **129:** A longer single row above the animal includes the initial comb/crossed
  group, a large group of short strokes, and two successive fish-like forms
  before the remaining right-hand shapes. This is broadly compatible with
  `W527 W555 W055 W233 W235 W741 W831 W518`. Two fish-family shapes
  are visible, but the reproduction does not justify independent certification
  of every fine allographic distinction or every internal token boundary.
  The illustrated square outline lacks a conspicuous major missing corner.
- **142:** A rectangular impression shows three main forms: comb, crossed/angular
  sign, and a fish with a cap above it. This is compatible with
  `W527 W555 W235`; its fish-positive classification is directly supported.
  The impression's comb teeth are on its left. The plate cutout is rectangular
  and does not show L-9's conspicuous corner loss, although an impression alone
  is weaker evidence of the physical seal's edge preservation than an original
  photograph. Do not use this to repair L-9's lost comb or declare the two
  inscriptions identical from raw codes alone.
- **583:** The comb/crossed beginning, following strokes, U-like form, capped fish,
  short strokes and final leaf/oval are visible in that order. This is compatible
  with `W527 W555 W033 W706 W235 W002 W817`, including a clear positive
  fish observation and a U-like component. The square illustrated face does
  not show a gross missing text-bearing corner. This is not a matched-pair
  translation with60: the strings differ by several intervening forms.

All ordering statements are left-to-right order in the printed impression.
Treating the pair as an ending follows the corpus's reported reading direction;
this review does not independently prove that direction.

## Remaining gaps and retained failed leads

The raw images at FEM leaves179 (LXXXIII,numbers1–52) and205
(XCVI,numbers488–537) do not contain the four target seal numbers. They were
personally inspected and retained as navigation attempts. Mackay leaf410 is
printed388,numbers599–630, so is not the583 table. Leaf375 and394 are retained
from the interrupted investigation but not interpreted here. The interrupted
reviewer's Mahadevan renders are outside this recovery review; the parent
analysis handles them separately.

M-636, M-821, M-833, M-934 and any other Pakistan targets have **not** received
primary original/impression authentication in this document. Source labels,
decipherment claims or bare corpus strings do not close those gaps.

Crops are reproducible with
[`render_ending_pakistan_crops.py`](../scripts/render_ending_pakistan_crops.py).
The full pages retain captions, numbers and spatial context. The evidence
manifest [`ending_pakistan_review.json`](../data/processed/ending_pakistan_review.json)
records hashes and distinguishes original FEM identity checks from provisional
CISI aliases. No central source registry was modified by this recovery.
