# Existing export: motif-route feasibility

A bounded local metadata audit supports a fast exploratory analysis of this secondary export. It does **not** establish a physical-object census or validate motif semantics. No sign–motif joint counts, feature choices, association tests, or new downloads were made.

Source: `data/raw/lipi_inscriptions.csv`, SHA256 `b8dcb325a2e2cd3cde12ac12e7a418b0348e45713c9ee28aad81b645d2ac5ee4`; 5,680 rows. Code hashes, complete raw-label histograms, scope definitions, exclusion counts, and two duplicate/multirow examples are in [the machine-readable audit](../data/processed/motif_fast_route_feasibility.json). Sanskrit, translation, and proposed phonetic columns were not used.

The exact site strings are `Harappa` (2,717 raw rows) and `Mohenjo-daro` (1,923). They supply 4,640 rows across all types. The following are separate **raw type-code scopes**, not a selected final sample:

| Raw type code, both sites | Raw rows | Standard strict rows | Strict rows with known motif | Provisional keys with known motif |
|---|---:|---:|---:|---:|
| `SEAL:S` | 1418 | 956 | 934 | 923 |
| `SEAL:R` | 303 | 189 | 6 | 3 |
| `SEAL:C` | 7 | 2 | 2 | 2 |
| `SEAL:CY` | 4 | 2 | 0 | 0 |
| `SEAL:L` | 1 | 0 | 0 | 0 |
| `SEAL` | 59 | 9 | 0 | 0 |

An authoritative type-code dictionary was not located in this bounded local inspection. The export's own shape marginals associate `SEAL:S` with `square` in 1,739/1,777 rows globally (also two rectangular, 35 missing, one `sqaure`); `SEAL:R` predominantly with cuboid/rectangular forms; `SEAL:C` with circular forms; and every `SEAL:CY` with cylindrical. Thus `SEAL:S` is not a justified synonym for **all stamp seals**. `SEAL:C` must not be mistaken for the cylindrical code. Bare `SEAL` and `SEAL:L` remain separate. The union of every `SEAL`-prefix code is reported only for coverage, including `SEAL:CY`; no stamp-seal eligibility rule was chosen here.

For exact `SEAL:S`, the 934 strict labelled rows represent 923 provisional keys: Harappa 184 rows/181 keys, Mohenjo-daro 750 rows/742 keys. The same strict subset also contains five `-` and 17 `None` labels, which remain unlabelled. Its literal motif marginals, including those missing values, are:

`-` 5; `Anth` 1; `Buff` 9; `Bull` 1; `Bull1` 88; `Bull1:I` 61; `Bull1:II` 6; `Bull1:J` 131; `Bull1:L` 35; `Bull1:O` 1; `Bull1:S` 120; `Bull1:T` 5; `Bull1:U` 20; `Bull1:V` 4; `Bull1:W` 285; `Bull1:X` 8; `Bull2` 1; `Bult` 1; `Comp` 1; `CompBull` 5; `Elep` 24; `Gaur` 53; `Gavi` 2; `Goat:3` 2; `Goat:6` 1; `Htgr` 1; `Mult` 5; `None` 17; `Othr` 3; `Rhin` 14; `Scene` 2; `T-A-T` 1; `T-M-T` 3; `Tigr` 8; `Zebu` 32

These labels are opaque strings. Do not silently rename `Bull1`, combine its colon suffixes, interpret `None` as photograph-confirmed absence, or convert `Othr`, `Mult`, and `Scene` into particular animals. The current missing set is `{'', '-', '--', '?', 'None', 'Unknown'}`. Existing scripts technically treat every other label as available, not necessarily animal-specific.

Standard strict means `scripts/prepare_corpora.py::parse_lipi` applied to the original CSV row. It requires the complete literal syntax `+ddd-ddd-...+`, excludes codes `000` and `999`, requires `complete.strip() == 'Y'` and `dir..strip().upper() == 'R/L'`, rejects classes `2L` and `3L`, and checks declared sign count only when raw `signs.isdigit()`. It does not filter `condition` or `preservation`; raw text is not trimmed. Returned tokens use namespace `Wells_ICIT_as_exported` (`Wnnn`), in source-file order, without reversing or authenticating archaeological reading direction. No M77 mapping is implied.

For two-site `SEAL:S`, rejection-reason counts overlap: malformed/non-simple text 308; unknown/separator token 98; incomplete metadata 359; direction 127; multiline class 35; count mismatch 98. Its 956 strict rows include condition labels `Good` 416, `Fair` 264, `Fine` 36, `Poor` 239, and lowercase `good` 1. They include 60 `preservation=fragment` rows despite `complete=Y`; inscription completeness and physical-object preservation are different fields. No quality cutoff was chosen. Complete condition/preservation marginals are retained in the JSON.

The existing `audit_iconography_theory.py` is a different exploratory copper-bridge transfer test. Its `parse_record` first receives stripped fields and changes `NR` to `R/L` for raw strings of length five; the strict parser still checks syntax. That rule produces 985, not 956, two-site `SEAL:S` rows (all types globally: 3,275 versus 2,914). Do not silently mix these parsers. Its deduplication unit is `(artifact, sequence, symbol, type)`, so distinct texts on one object remain multiple rows; its published transfer counts are not independent stamp-seal association evidence.

One “object” currently means a provisional key: stripped `cisi`, unless absent, otherwise `lipi_id:` plus the integer portion before the decimal in `id`. `prepare_corpora.main` has a slightly narrower absent-CISI set than the iconography audit, but that difference affects zero current rows. All 5,680 row IDs are unique. The 4,695 provisional keys include 620 fallback keys; 902 keys have multiple rows. No key spans multiple integer roots, sites, or types; no integer root spans multiple keys. These clean bookkeeping relationships do not prove independence of physical objects, impressions, molds, or duplicate catalogue entries.

Across the full export, no key has conflicting known motif strings, and no key mixes known and absent motif labels. This may reflect object-level metadata repeated on every row. It cannot establish that a motif is on the same face as a particular text. All multirow face/line claims need that limitation retained. A decimal suffix is a row distinction, not an authenticated face identifier.

Within two-site `SEAL:S`, 1,418 raw rows form 1,383 provisional keys; 23 keys have multiple rows. Twenty-one have different raw texts. After strict parsing, 956 rows form 942 keys; 13 are multirow, including 11 with distinct strict texts and two with repeated text/motif. For example, H-102 rows `1168.1` and `1168.2` have different texts but the same raw motif `Bull1:W`; H-597 rows `1540.1` and `1540.2` repeat both text and `Bull1:J`. The JSON preserves both examples without treating either as an extra independent object. Identical text on **different** keys was not collapsed. Observed-row versus declared-side discrepancies are retained as descriptive counts, not called errors: missing uninscribed faces and strict filtering can both change row coverage.

The executable route is therefore available at the secondary-export level, once its exact type eligibility, opaque motif grouping policy, parser variant, and multirow-object handling are fixed explicitly. Keep all rows of a provisional key in one statistical unit or dependence block; do not infer side-specific motif placement or concatenate separate fields as a single inscription. No sign features or statistical model were selected by this audit.

Reproduction uses Python `csv.DictReader`, the pinned parser functions, and `Counter`/grouping only: evaluate empty parser-reason lists, retain raw metadata values, group with the explicit key rule, and count whole-text equality/difference within keys. The JSON records each scope and the ordered steps. Required existing paths are the CSV, `scripts/prepare_corpora.py`, `scripts/audit_copper_bridges.py`, `scripts/audit_iconography_theory.py`, and provenance `data/sources.json`. Neither the translation columns nor the existing transfer-test outcome is an input to this feasibility conclusion.
