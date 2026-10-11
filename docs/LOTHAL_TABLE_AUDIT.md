# Lothal Table 1: complete row audit

Date: 2026-09-24. Source: Dennys Frenez and Maurizio Tosi (2005), *The Lothal sealings*, Table 1, printed pp. 93-94, PDF pages 31-32 of [the archived paper](/Users/chinmaymk/github/indus-script/data/raw/sealing_frenez_tosi_2005.pdf). The caption is on printed p. 92; context discussion is on pp. 71-72.

All **93 rows, L-124 through L-216**, were manually transcribed from full-page rendered images. Each impression count and the occupied context/type cell was visually inspected. No table cell required a guessed value. Printed question marks are retained as the authors' unknown *discovery contexts*, not uncertainty about our transcription. Superscript W1/W2 are stored without superscripts; the outside-context symbol is stored as the letter O.

The [row ledger](/Users/chinmaymk/github/indus-script/data/processed/lothal_sealing_table.json) preserves source locators and hashes of the PDF and the two inspected page renders. The [audit script](/Users/chinmaymk/github/indus-script/scripts/audit_lothal_table.py) verifies these hashes, contiguous IDs and basic row invariants before producing [computed totals](/Users/chinmaymk/github/indus-script/results/lothal_sealing_table_audit.json). The source classifications have not been reauthenticated by examining the clay objects.

## Context discrepancy

| Context | Table rows | Prose count | Evidentiary status |
|---|---:|---:|---|
| W | 35 | 35 | Ascribed by Rao to warehouse cluster |
| W1 | 18 | 18 | Authors' inference from seals also occurring in W |
| W2 | 11 | 11 | General SRG3 area, without recurrent seals |
| O | 10 | 11 | Ascribed to outside contexts |
| ? | 19 | 17 | Indeterminate discovery context |
| Total | **93** | **92** | Prose also states an overall total of 93 |

The prose's W2 count is computed as 64 minus 53, not separately printed. W/W1/W2 total **64** in both table and prose. The remaining table rows number 29, partitioned 10 outside and 19 unknown; the prose gives 11 plus 17 = 28. We do not change a row to repair this inconsistency or infer which prose/table classification was intended. The explicit outside rows are L-141, L-145, L-146, L-150, L-174, L-205, L-208, L-210, L-215 and L-216.

W1 must not be used as independent evidence that recurring seals belong to the warehouse: that recurrence is the stated reason for assigning W1. Results preserve both W-only and W/W1/W2 summaries.

## Counts by published type

| Published type | All 93 | W only | W + W1 + W2 |
|---|---:|---:|---:|
| Pegs-on-wall | 9 | 3 | 8 |
| Structures | 10 | 4 | 8 |
| Lockers | 9 | 2 | 4 |
| Parallel canes | 5 | 1 | 3 |
| Wooden boxes | 15 | 14 | 14 |
| Pottery | 21 | 6 | 16 |
| Leather sacks | 2 | 1 | 1 |
| On wicker | 1 | 0 | 0 |
| On single rope | 1 | 0 | 0 |
| On woven straw | 1 | 1 | 1 |
| Other types | 1 | 0 | 0 |
| Undiagnostic | 18 | 3 | 9 |

These are categories of inferred fastening devices or surviving reverse traces. They do not all name the same ontological level: for example a straw trace is not itself an identified cargo. The ledger retains the published column label rather than collapsing categories.

The table reports **133 seal impressions**: 62 objects with one, 25 with two, four with three, one with four and one with five. Thus **31/93 objects have multiple impressions**. W alone comprises 35 objects and 45 impressions, including six objects with multiple impressions. W/W1/W2 comprises 64 objects and 87 impressions, including 19 with multiple impressions. These counts are neither numbers of script signs nor numbers of independent seal matrices; repeated impressions can come from the same seal.

The prose on printed p. 82 instead gives **130 impressions: 63 on objects with one impression and 67 on objects with multiple impressions**. Table 1 totals **133 = 62 + 71**, so its corresponding differences are +3 total impressions, -1 single-impression object and +4 impressions on multiple-impression objects. There are 31 multiple-impression objects in the table; the prose's 63 single objects out of 93 would imply 30. The source disagreement remains unresolved. An impression can repeat the same seal, so these totals cannot be repaired by silently equating impressions with distinct matrices.

## Targeted cautions for further joins

- Table 1 places **L-124 under "on woven straw"**, even when prose discusses it as a probable pottery-related sealing. The broad vessel interpretation must remain separately attributed; do not replace its table field with pottery.
- Table 1 places **L-193 and L-198 under "structures"**. Prose discussion that associates them with lockers is a separate characterization, not grounds to silently move the rows.
- L-125 is under wooden boxes; L-126 is under leather sacks. These are published identifications, not independently measured contents.
- **L-174 has one impression in Table 1, but printed p. 80 explicitly reports two impressions of the same geometric seal.** The ledger retains the table's one and records the prose's two separately. Replacing only this cell would increase the table total to 134 and therefore would not reconcile it with the prose total of 130.
- **L-209 is W2 in Table 1 but described as not contextualized on printed p. 82.** This may reflect different levels of spatial precision, because W2 only identifies the general SRG3 area. It is not established that the prose meant no area assignment whatsoever; no forced reconciliation is made.
- No ancient owner, commodity, sound or sign meaning follows from these context/type/count fields alone.

## Reproduction and attempt record

The first rendering command incorrectly supplied `data/raw/` to a helper that requires a plain source filename; it exited with argument validation status 2 and produced no table render. Retrying with `sealing_frenez_tosi_2005.pdf` succeeded. Pages 31 and 32 were rendered at maximum dimension 3400 pixels and visually reviewed. Text extraction was not trusted for column alignment because it interleaves the cells.

A later independent parent review agreed with the table's outside/unknown counts and impression counts. The subtask then visually inspected the parent's `sealing-text-18.png` and `sealing-text-20.png` renders (printed pp. 80 and 82), confirming the additional prose comparisons above. Both render hashes are now included in the row ledger's evidence files; no original table cell was changed.

```sh
FONTCONFIG_FILE=/opt/homebrew/etc/fonts/fonts.conf /Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/inspect_research_pdf.py sealing_frenez_tosi_2005.pdf --prefix lothal-table --pages 31 32 --render-only --scale 3400 --pdftoppm /Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm
/Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/audit_lothal_table.py
```

No new data was downloaded for this subtask. The script's assertions and hash checks passed; its counts are a reproducible audit of the manual transcription, not automated verification that every original artifact has been interpreted correctly.
