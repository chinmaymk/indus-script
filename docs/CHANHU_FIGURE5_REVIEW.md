# Chanhudaro Figure 5: a descriptive inventory

Reviewed 2026-09-25. Source: Bahata Ansumali Mukhopadhyay, *Bulletin of the IRC* 6 (June 2025), Figure 5, printed p. 13 / PDF p. 19; the numerical claim is on printed p. 12 / PDF p. 18. The [publisher PDF](https://rmrl-site-files.s3.us-east-1.amazonaws.com/PDFFIles/bulletin/bulletin-No-6-June-2025.pdf) is retained as `data/raw/irc_2025_fish_bulletin.pdf`. Source SHA256: `af5f67d803a4c8bdda75c27bf113fd67f32cf2a88a680fc5530e3aa334e86a87`.

**The figure displays eight catalogue IDs in square 9/D, five with the author's orange fish border. Neither its map nor its inscription panel reproduces the prose count of six out of nine.** The five orange IDs are C-10, C-53, C-58, C-65 and C-79. The three others are C-22, C-55 and C-87; the last has the dashed border identified as a tag in the legend. This discrepancy does not establish that a ninth object is absent from the excavation record. It establishes that the published figure does not identify it.

This review transcribes labels and borders. It does not independently classify fish signs, identify commodities, validate findspots or test a decipherment. The figure was already selected and interpreted by the hypothesis's author; it is not a held-out sample. Its caption describes **some** contextualized inscriptions, so it cannot supply an independently complete excavation denominator.

## Complete inventory of panel (c)

“Orange” records the author's fish designation. It is not a reading assigned by this project. C-numbers in the two identifier columns are mutually exclusive.

| Square | Orange IDs | Other IDs | IDs / panels |
|---|---|---|---|
| 9/E | — | C-91, C-66 | 2 / 2 |
| 8/E | C-70, C-62, C-9 | C-76 | 4 / 4 |
| 9/C | C-11 | C-5, C-68, C-75 | 4 / 4 |
| 8/C | C-40 | C-39, C-69, C-56, C-94, C-61, C-30 | 7 / 7 |
| 9/B | — | C-17, C-74 | 2 / 2 |
| 8/F | C-24 | C-18, C-35, C-38 | 4 / 3 |
| 9/D | C-79, C-10, C-65, C-58, C-53 | C-87, C-22, C-55 | 8 / 8 |
| 7/E | C-14 | C-32, C-12 | 3 / 3 |
| 7/C | C-78 | C-19, C-3 | 3 / 3 |
| 7/F | C-8 | C-71 | 2 / 2 |
| 8/B | C-4 | — | 1 / 1 |
| 8/D | C-64 | C-54 | 2 / 2 |
| 6/F | — | C-60 | 1 / 1 |
| 10/F | C-51 | — | 1 / 1 |
| 10/E | — | C-2 | 1 / 1 |
| 10/D | — | C-15 | 1 / 1 |
| 10/C | — | C-20 | 1 / 1 |
| **Total** | **17 IDs** | **30 IDs** | **47 / 46** |

C-35 and C-38 share one inscription panel, with a yellow sign border. C-9 and C-64 have both yellow and orange borders. C-53 and C-58 are separate panels with very similar drawings: two catalogue IDs are not automatically two distinct text types. The map repeats the inscription-panel IDs and the legend repeats C-11 as an example; these repetitions are not additional objects. C-40 shows two inscription lines inside one panel, also not two objects.

The figure is not a seal-only dataset. C-91 is explicitly labelled as a pot, C-39 as a snarling tool, C-40 as a metal implement and C-87 as a tag. C-35/C-38 have tablet-style outlines in the map. The object-shaped C-94 outline is not sufficient here to independently establish its archaeological object class. No unmarked panel has been reclassified from the apparent shape of an individual sign.

Square 9/D still has the largest orange-ID count in this illustration, five versus the next-largest three in 8/E. That descriptive maximum is not a test of an unusual concentration. Exposure, completeness, chronology, object class, duplicate impressions/texts and the comparison population remain unverified. The observed fraction in 9/D is 5/8; 8/E is 3/4, illustrating why the largest count is not automatically the largest proportion. Neither comparison establishes a gemstone meaning.

## Persisted evidence and reproducibility

- `data/processed/chanhu_figure5_inventory.json` stores every panel, its IDs, square, observed border colours, qualifications, source hash and derived-image hashes. Totals are sums of those entries.
- `results/primary_pages/chanhu-figure5-19-large.png` is a 5,000-pixel render of PDF p. 19. Four crops ending `-panels`, `-map`, `-bottom` and `-legend` preserve the inspected details.
- Render command: `pdftoppm -f 19 -singlefile -scale-to 5000 -png data/raw/irc_2025_fish_bulletin.pdf results/primary_pages/chanhu-figure5-19-large`.
- The four crop boxes are fractional coordinates of that 3,601 × 5,000 render, converted with Python `int`: panels `(0.42w, 0.34h, 0.88w, 0.61h)`; map `(0.115w, 0.18h, 0.61w, 0.57h)`; bottom `(0.12w, 0.565h, 0.88w, 0.612h)`; legend `(0.61w, 0.175h, 0.88w, 0.34h)`.

All images are derived locally from the retained PDF. This independent subtask downloaded no new data and did not modify the source registry or main research log.

## Independent computational review, 2026-09-25

Reviewed `scripts/audit_chanhu_fish.py` at SHA256 `56ce5e087038e05c0c09b78df2924ad009ef5f0b200c6d7ecf168c642d61d567` and its generated `results/chanhu_fish_audit.json`. A separate raw-CSV recount used exact site equality, object-ID prefixes, a separate square parser and three-digit token extraction without importing the audited script. No doubtful `*` or `?` text qualifiers occurred in this site subset; damage and unknown-code rules were checked directly. All 72 objects' declared-family and plain-fish statuses matched the result. There were 74 text rows, not 74 independent objects.

| Seal-prefix cohort | 9/D positive / negative / unknown | Other known squares positive / negative / unknown |
|---|---|---|
| Raw secondary locations | 5 / 3 / 1 | 15 / 21 / 9 |
| Selected catalogue location overlays | 5 / 1 / 1 | 15 / 23 / 9 |

The overlays move C-6 and C-74 out of the target; C-57 moves between two comparison squares. This does not make the overlay a fully authenticated excavation dataset. The C-74 assignment remains a sensitivity choice given its conflicting location evidence. “Negative” means absence of the declared code family under the stated completeness rules, not demonstrated absence of every conceivable fish form: W221 and unmapped forms are excluded. C-22 stays unknown. The missing original partial seal CH2558 is not silently added as a negative observation.

The fixed-margin tails were independently recalculated using exact rational arithmetic: raw `0.2486241204335362`, overlay `0.05820271617208656`. These numbers agree arithmetically with the script. They cannot function as confirmatory significance tests: neither exchangeability nor a prospective, complete sample is established. C-53 and C-58 have identical raw text and the same locus 211, creating a concrete dependency concern. The grid restriction does not establish matching chronological phases; secondary phase fields are unspecified. None of the site's symbol fields contains “fish,” so the text-or-symbol sensitivity adds no observations here. Literal `SEAL:` selection excludes C-23, typed `SEAL`, but that record also has unknown square and therefore does not alter the target/comparison counts.

No count or current-input classification bug was found in this bounded review. The code does not establish semantic values, craft specificity, a complete fish inventory, or a homogeneous Harappa-II comparison population.
