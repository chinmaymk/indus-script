# Mahadevan 2405: recovery of all seven displayed entries

All seven entries of text **2405 (FEM 405)** are recoverable as normalized printed sequences, except for two explicitly hatched passages. They contain **19 identified sign positions, representing 18 distinct Mahadevan sign IDs**, plus **two unknown spans**. Each span represents one or more signs; the full text therefore has at least 21 signs, with no exact total recoverable here.

The source is `data/raw/mahadevan_1977_text.pdf`, SHA-256 `6dcdd074a0174e5fab149590fbbf82342711d345764e9763f8e5e92c81cf7f99`. The specimen on printed p.20 / PDF p.31, §13.3, was compared with the ordinary text entry on printed p.70 / PDF p.81. All seven entries agree between those reproductions. Existing renders are `results/primary_pages/m77-codebook-31.png` and `results/primary_pages/numeral-followup-81.png`.

## Recovered entries

Sequences below run in **normalized printed reading order, rightmost glyph first**. All IDs are Mahadevan IDs; there is no Wells or Parpola conversion. `000` is our serialization of a hatched unknown span, not a sign ID and not a count of one missing sign.

| Display entry | Side | Line code | Original direction code | Recovered sequence | Identified positions | Unknown spans |
|---|---:|---:|---|---|---:|---:|
| 1 | 1 | 0: only line | 1: right to left | `293-123-343-065-294-342` | 6 | 0 |
| 2 | 2 | 1: first line | 2: left to right | `391-089-137-253` | 4 | 0 |
| 3 | 2 | 2: second line | 1: right to left | `409-094-409-000` | 3 | 1 |
| 4 | 3 | 0: only line | 1: right to left | `319-032-162` | 3 | 0 |
| 5 | 4 | 0: only line | 1: right to left | `403-231` | 2 | 0 |
| 6 | 5 | 0: only line | 3: only sign in line | `408` | 1 | 0 |
| 7 | 6 | 0: only line | 9: doubtful | `000` | 0 | 1 |

The object type is code 1, seal. Field-symbol code `01`, unicorn, applies to side 1; the other sides have `00`, nil. Seven displayed entries belong to six sides because side 2 has two lines. The side-6 entry is wholly illegible. The codebook explicitly says it is retained because other lines of the same text are legible.

The ordinary text page prints metadata as `110101`, `20012`, `21`, `30001`, `40001`, `50003`, `60009`, using inherited fields. Expanded metadata is respectively `110101`, `120012`, `120021`, `130001`, `140001`, `150003`, `160009`. The JSON stores both the displayed forms and expanded fields.

## Identity and direction checks

Each identified position was compared with the supplied numbered PNG and Table I, using its printed order to locate the Mahadevan sign. The JSON records the primary page, half and row for every position, the distinguishing morphology, and glyph hashes. The close alternatives were checked explicitly:

- Entry 3 has **M094**, one upright stroke and two slanting strokes. M093 instead has two upright strokes and one slant.
- Entry 4 has **M032**, the anthropomorphic form with a plain attached U. The added internal upright of M034 is absent.
- Both paired-oval forms in entry 3 have a central downward stem, **M409**. The singleton on side 5 lacks this stem, **M408**.
- Entry 2 has three long strokes, **M089**, rather than a short-stroke triad.
- Entry 1 distinguishes **M343**, with an extra internal upright in the U form, from final **M342**, without that upright.

No doubtful-sign asterisk is observed beside the 19 readable positions. This is a statement about the normalized print, not certainty from inspecting the artifacts.

Section 13.2(ii) on the same primary page says all lines are copied uniformly **right to left**, regardless of the original direction, or the direction on seal impressions. Consequently, the side-2 first line remains `391-089-137-253` in normalized reading order even though its original direction code is 2. Reversing this sequence again would undo the source's normalization. Codes 3 and 9 are preserved as “only sign” and “doubtful”; neither is silently converted into an original physical direction.

Section 13.2(iii) also says the source normalizes sign forms and the orientations of asymmetric signs. This recovery does not preserve original graphical variants. The note below the specimen defines hatching as a lost or illegible passage with **one or more signs**. Both such spans remain unresolved; `000` must not be counted as a single ancient sign, deleted, or used to create an adjacency across damage.

## Export coverage and limits

The literal `GLI-IND-M77-02405` record in `data/raw/glossa_icit_export.json` contains only `+293-123-343-065-294-342+`, with `sign_count: 6`. That is an exact match to entry 1. The six additional displayed entries contain 13 readable positions and two unknown spans. This ledger is a separate manual recovery, not an assertion that those additional lines are present in the raw export.

Five entries are complete normalized lines, one is partially readable, and one is wholly illegible. Keep side and line boundaries: concatenating all seven entries would create unsupported adjacencies. No phonetic, numeric or semantic values follow from these shape identifications. No artifact photograph was inspected in this bounded recovery.

The machine-readable evidence is `data/processed/m77_2405_recovered_lines.json`. Validation checked all seven entries, the 19 identified positions, 18 distinct IDs, two unknown spans, metadata expansions and the exact first-line export match. No canonical export, strict dataset, source registry or shared analysis file was changed, and no download was made.
