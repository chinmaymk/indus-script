# Fish signs and the Harappa jewellery assemblage: a counting problem

25 September 2026. **The bead association is real; the published six-type
calculation is not supported by the detailed catalogue and plates.** This audit
establishes no gemstone meaning, pronunciation, language or decipherment.

Mukhopadhyay's June2025 bulletin links fish signs to gemstones and related
commodities. Its Harappa example reports four fish-bearing inscription types
among six in assemblage8650, treating duplicates once. Figure4 represents8650b
with one inscription and labels nine similar tablets. The argument merits
checking because it uses an archaeological association beyond sign sequences.
[Publisher bulletin, pp10–11, Figure4](https://rmrl-site-files.s3.us-east-1.amazonaws.com/PDFFIles/bulletin/bulletin-No-6-June-2025.pdf).

## What the original excavation records establish

Vats's narrative places group8650 in squares H12/21 and I12/1, at4–7ft below
surface. It lists inscribed seals/tablets, many beads and pendants, other small
objects, and two weights of26.3g and4.3g. Careful recovery used knives and sieves
over three months. This supports an association with beads and jewellery-related
materials. The weights are separate objects; no inscription on either weight,
or mass corresponding to a particular text, is established.

The broad narrative discusses a well and fourteen workmen's quarters in
StratumIV. It does not by itself put all these features in one closed deposit or
establish that every inscription recorded a commodity. A catalogue entry for
the related8650q beads repeats the same squares and4–7ft interval but says
**StratumIII**. This internal discrepancy remains unresolved.

Read the original scans: [p58](../data/raw/vats_1940_text_p58_leaf84.jpg),
[p59](../data/raw/vats_1940_text_p59_leaf85.jpg),
[p60](../data/raw/vats_1940_text_p60_leaf86.jpg),
[p435](../data/raw/vats_1940_text_p435_leaf463.jpg).

## A find-group letter is not one inscription type

The detailed catalogue assigns these numbered illustrations to8650b:

| Original plate item | Catalogue page | Find number | Depth |
|---|---:|---|---|
|433,439,458|348|8650b|4–7ft|
|486,488,489,493|349|8650b|4–7ft|

The joins are visible in [p348](../data/raw/vats_1940_text_p348_leaf376.jpg)
and [p349](../data/raw/vats_1940_holdout_leaf377.jpg). The corresponding
[PlateXCVI](../results/primary_pages/gemstone-vats-plate-200.png) shows differing
texts and face arrangements. For a particularly clear comparison,
[433](../results/primary_pages/gemstone-EH433.png) has an animal depiction on
its lower illustrated face, whereas [458](../results/primary_pages/gemstone-EH458.png)
has upright strokes beside a U-shaped form. The upper texts also differ.
[489](../results/primary_pages/gemstone-EH489.png) and
[493](../results/primary_pages/gemstone-EH493.png) supply further differences.
Two agents independently checked the table joins and gross visual distinctions.
These are low-resolution printed photographs, not artifact autopsy or certified
fine sign transcriptions.

Consequently, the nine8650b objects cannot be assumed to share the complete
inscription represented by433. The narrative's wording about identical
pictograms does not override the detailed records. The discrepancy must be
reconciled before accepting the claimed six-type denominator. The8650c narrative
also cites two numbered illustrations,448 and452; their exact equivalence has
not been established here.

An exact, site-restricted join to the retained secondary export finds seven
object groups and twelve rows for the seven8650b plate entries, with seven
different raw multi-line signatures. This corroborates the need to distinguish
objects; it does not authenticate every secondary glyph or establish a corrected
population of types. Proposed translations and phonetic readings are excluded.
[Reproducible audit](../results/gemstone_context_audit.json).

**No replacement fish fraction is asserted.** Early arithmetic gave7/17 physical
objects if the Figure4 classifications and nine-identical-b assumption were
accepted. The newly checked primary evidence contradicts that simplification;
7/17 is retained only as a withdrawn conditional calculation in the research
history. It must not be reported as an observed corrected rate. Seven numbered
illustrations are likewise not a complete corrected denominator.
Reconstructing omitted types could change both numerator and denominator;
this audit does not establish the direction of a corrected association.

## Nearby finds and sign boundaries also matter

Vats lists two nearby tablets under10928a, in I11/15 at5ft7in, one badly broken.
He then lists eight later seals/tablets from the same area. Figure4 includes
seven of those eight and one panel for10928a. The missing entry8154 is explicitly
fragmentary; another included entry10226 is also fragmentary. The three nearby
fish-positive examples are not three successes out of three eligible objects.
We retain every listed entry and unknown status in the
[evidence ledger](../data/processed/gemstone_primary_review.json).

For8650e, Vats explicitly describes a fish on a separate side. The secondary
export stores Fish as an iconographic symbol and only the other two-token text
in its transcription. A text-only fish search would therefore change the
counting boundary. Neither representation automatically decides whether the
fish belongs to writing, iconography or both. A future comparison must state
its classification rule and apply it consistently to cases and controls.

## What remains testable

An association test needs a complete inventory, a fixed fish-family definition,
the same counting unit for cases and controls, and comparable archaeological
contexts classified without looking at their inscriptions. Duplicated tablets,
different object classes, text lengths, damage and deposit-level dependence
must be handled explicitly. A corpus-wide line frequency is not a matched
baseline for deduplicated multi-face types.

Even a robust association would leave several explanations open: commodity,
craft, institution, owner, status or another property correlated with the
setting. Particular sounds and rebus mechanisms require additional independent
constraints. The [method review](GEMSTONE_METHOD_REVIEW.md) supplies test designs
and an illustrative binomial sensitivity calculation, explicitly not an
empirical significance test. No empirical enrichment estimate is made here.

Useful next work is to reconcile the complete8650 object inventory and test
other independently classified contexts. Chanhudaro and Mohenjodaro examples
already used in the2025 argument would be source-exposed corroboration, not
held-out predictions. All417 established semantic and phonetic values remain
null.

## Reproduction and source retention

All downloaded bytes are in `data/raw/`, with URLs, sizes and hashes in
[sources.json](../data/sources.json). The old publisher URL's404 response is
retained as HTML, separately from the recovered50-page bulletin. This is not
the distinct proceedings/SSRN version. The archive page map mislabelsleaf374
as348; visual inspection established it is346 and the correct348 isleaf376.

Run `python scripts/audit_gemstone_context.py` or the full
`python scripts/run_all.py`. Recreate page images and crops with
`python scripts/render_gemstone_evidence.py --pdftoppm /path/to/pdftoppm`.
Crop boxes and resizing are saved in
[gemstone_crop_boxes.json](../data/processed/gemstone_crop_boxes.json).
Enlargement adds no source detail. The audit checks36 evidence-file hashes,
preserves uncertainty and imports no proposed translation columns.
