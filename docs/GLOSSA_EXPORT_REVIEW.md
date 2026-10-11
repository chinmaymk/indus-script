# Public Glossa sequence export: provenance and independence

The 3,085-row public export is a **mixed Mayig/Mahadevan reconstruction**, not an identified copy of the README's private Holdat corpus. Its Mayig component exactly reproduces our existing raw Mayig text multiset. Its full Mahadevan component is not adopted as an authoritative corpus. A subsequent [primary check and conservative preparation](M77_CANDIDATE_CORPUS.md) support conditional analysis of a qualified subset.

This audit uses existing local files only. [The script](../scripts/audit_glossa_export.py) reproduces all counts and writes [the detailed ledger](../data/processed/glossa_export_review.json), including input hashes, every repeated-text group, Mayig match witnesses, and all 417 primary-frequency comparisons. Run `python3 scripts/audit_glossa_export.py`. No files were downloaded.

## What the export contains

| `source_system` | `sign_id_scheme` | Rows | Exact unique texts | Repetition excess | Declared signs |
|---|---|---:|---:|---:|---:|
| `mayig-cisi` | `Parpola1982` | 179 | 176 | 3 | 984 |
| `indusscript-m77` | `Mahadevan1977` | 2,906 | 2,289 | 617 | 11,959 |
| Namespace-qualified total | kept separate | 3,085 | 2,465 | 620 | 12,943 |

Exact texts retain all encoded order, `000`, asterisks, and boundary syntax. Repetition excess means rows minus distinct encoded texts **within their declared namespace**; it does not prove duplication of physical objects. There are 867 M77 rows in repeated-text groups and five Mayig rows in repeated-text groups. For example, M77 `+048-342-176+` occurs 37 times. No M-number was equated to a same-numbered Parpola or Wells sign.

The export calls itself an ICIT-format diplomatic sequence reconstruction, version `v1 (2026-05-14)`. Its 56% coverage statistic compares the row count with an ICIT reference scale; this is a claim about scale, not a demonstrated artifact coverage calculation. ICIT-style punctuation does not make its numeric signs Wells/ICIT sign identifiers or authenticate an official ICIT release.

The existing GitHub tree snapshot is untruncated. The local export's Git blob SHA-1 exactly matches `glossa-corpus/indus/exports/indus_icit_format.json` in that snapshot (`40812fc54470d5508b47af5fabcea7ccf044036c`). The tree also lists ingestion scripts, canonical object records and a raw M77 import. Paths alone do not establish those files' contents or prove a row-level derivation: no new files were fetched in this audit.

## Relationship to existing corpora

After changing only Mayig `Pddd` tokens into the export's `+ddd-ddd+` syntax, **all 179 raw Mayig rows match as a multiset**, including multiplicities. No reversals, sign substitutions, sorting, or damage cleanup were needed. All 98 rows in our strictly filtered Mayig corpus are accounted for; the export includes 81 additional raw rows outside that filtered multiset. The Mayig component therefore supplies no independent text observations beyond our stored archive. Matching text does not always identify one object uniquely; the ledger retains all raw matches rather than arbitrarily selecting one.

The [downloaded README](../data/raw/glossa_README.md), section “Corpus Note,” describes Holdat LLC Indus Corpus v3 as **1,670 objects, 7,002 tokens, 390 signs, nine sites**, and says it is not publicly available. The export has different counts and explicitly different source labels. There is no basis to substitute this public reconstruction for the private dataset or claim replication of Holdat-dependent statistics. Possible shared archaeological objects do not establish dataset identity, and cannot be enumerated from this export alone.

All 3,085 exported rows are labeled `seal`. Site is null for all 179 Mayig rows and 1,940 M77 rows. The remaining M77 rows use six site labels: Mohenjo-daro 839, Harappa 110, Chanhu-Daro seven, Sutkagen-Dor six, Lothal three, Kalibangan one. These sparse and uniform metadata fields should not be treated as authenticated context assignments.

## M77 inventory and frequency check

The M77 component has 12,639 token slots: 11,959 named-sign slots and 680 `000` slots. All literal tokens follow `*?ddd`; every nonzero numeric code lies within the primary Table I inventory M001–M417. There are 452 starred tokens across 389 rows. Every row's declared sign count equals its non-`000` token count. This is internal count consistency, not transcription authentication.

For a separate sensitivity tally only, the script combines each `*ddd` with its corresponding `ddd`. The meaning of the asterisk is not established here and the literal forms remain preserved. This tally contains 394 named codes, with 23 primary signs absent. Against the existing primary Table I transcription's 13,372 tokens, **none of the export's per-sign counts exceeds the primary count**, and 226 of 417 totals are exactly equal.

| Sign | Export unstarred | Export starred | Combined sensitivity | Primary Table I |
|---|---:|---:|---:|---:|
| M342 | 1,274 | 48 | 1,322 | 1,395 |
| M099 | 615 | 6 | 621 | 649 |
| M328 | 47 | 2 | 49 | 323 |
| M089 | 183 | 2 | 185 | 314 |

These results are compatible with an incomplete M77-derived transcription. They do not authenticate sign order, row identifiers, orientation, damage readings, or a particular extraction method. Large uneven deficits, such as M328, make this unsuitable as a replacement for full-catalogue frequencies without further source checks. Exact aggregate agreement is not expected for an incompletely recovered corpus with potentially different conventions.

## Identity and next-use limits

All 2,906 M77 `glossa_id` values are unique, with examples `GLI-IND-M77-01001` and `GLI-IND-M77-09905`. They are row identifiers containing M77-like references, but the export does not separately retain an original catalogue reference, excavation number, artifact-side identifier, image link or per-row citation. Their stability across versions and correspondence to physical artifacts remain unverified.

Retain the M77 component as a **provisional candidate for direct comparison with specific primary catalogue entries**. Before analytic use, verify the original-reference mapping and sample literal sign sequences, explain the star convention and frequency deficits, and establish damage, multiline and direction handling. Do not pool it with Mayig, the Wells-labelled corpus, or primary catalogue totals as an independent sample. This review establishes provenance labels and internal consistency; it establishes no deciphered values.

Two concrete follow-up targets already have local primary renders:
`GLI-IND-M77-01066` contains `086-099`, and `GLI-IND-M77-02427` contains
`086-099-086`. The primary reference 1066 drawing shows two short strokes followed
by one long stroke in displayed left-to-right order; reference 2427 shows long,
two short, long. See [the earlier primary review](NUMERAL_PRIMARY_FOLLOWUP.md).
The first segment is compatible with reversing the export for display; the
palindromic second segment does not determine orientation. This is a targeted
partial-pattern consistency check, not authentication of the complete lines,
all exported row IDs, a uniform direction convention or a physical-object bridge.
The full surrounding signs and printed reference labels are the next checks.
