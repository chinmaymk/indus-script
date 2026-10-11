# Independent review of the pipe and chain figures

Reviewed 2026-09-25. This review checks the graphical premises of IRC Bulletin 6 (June 2025), §4.2 and §7. It does not assign a reading or meaning to any sign. The reproducible inventory and byte/hash evidence pins are in [pipes_figure_review.json](../data/processed/pipes_figure_review.json).

## Figure 7: the denominator and named examples

Figure 7 is PDF page 25, printed page 19; the numerical claim is on PDF page 24, printed page 18. I rendered the page at 4,000 pixels and inspected a crop of panel A. It contains **13 rows but 12 distinct CISI labels**, in this order:

K-20, M-636, H-155, H-446, M-268, Krs-1, M-1765, M-1783, M-324, M-324, H-656, M-99, M-46.

The two M-324 rows each depict the same two-sign pattern. The retained secondary corpus also has two M-324 records, 2842.1 and 2842.2, with the same string and excavation number. The figure therefore does not independently establish 13 different seals. It does establish 13 displayed rows. There are nine displayed inscriptions with more than two known signs; the duplicated label is among the short rows and does not change that nine-row subset.

H-656 is illustrated with a shaded missing segment after its two preserved signs. The secondary row is explicitly `text length=2+?`, `complete=?`, `preservation=fragment`. It should not be treated as an originally two-sign text that had no opportunity to contain another sign. M-636 and M-1783 likewise show missing/uncertain parts. Their observed positive signs can be counted, but missing parts cannot provide secure absences.

The four named positive examples can be aligned safely to secondary sign codes:

| Figure label | Visible candidate type | Secondary codes supporting this limited identification |
|---|---|---|
| M-46 | plain and modified fish forms | W220, W235, W240 |
| M-636 | plain and modified fish forms | W220, W235 |
| M-1765 | U glyph with internal stroke ending in a small circle | W705 |
| Krs-1 | corresponding U glyph with adjacent vertical strokes | W706 |

These are labels for the author's proposed categories. They do not establish fish = gemstone or U = gold. The §4.1 illustration on PDF page 22 explicitly identifies the two U-based diagrams as the author's precious-metal candidates. The provisional catalogue groups W704–W707 in P316/M336, but this review confirms only the pictured W705/W706 examples; it does not license pooling all P316 variants automatically.

An initial correspondence inference based on the shared W480 in M-1765 and Krs-1 was **wrong and withdrawn before final analysis**. W480 is their common plain caret, also present in M-268, not the author's gold candidate. Consequently an apparent fifth positive M-268, and any W480-based statistics, do not test the paper's stated gold-or-fish association. Parent analyst was immediately notified of this correction.

## Chain variants and the Kalibangan seal

The catalogue's P353 family bridges W215/W216 to M415/M417. The original Mahadevan sign list, printed page 35 (PDF page 46), visually distinguishes M415 as three stacked plain loops and M417 as three stacked loops crossed by an axial vertical line. I inspected the retained rendering. This is a family-level bridge, not proof of exact variant equivalence for every secondary record.

In Figure 7A the K-20 example has a clearly crossed three-loop chain, as does the seal photograph in panel B. The caption identifies **KLB-1, ZE10, early Period II, ASI Reg. 18902**. Its secondary row is 1895.1, `+151-216+`. This seal is a separate object and context from the later ZA8 pipes; it cannot independently identify their contents.

## Figure 9: the archaeological photos

Figure 9 is PDF page 37, printed page 31. Panel A shows the two pipes joined, fish-marked segment above chain-marked segment. Panel B shows the fish pipe on the left and chain pipe on the right, separately. There are no per-pipe registration-number labels in the figure. The pipe photos are credited to the 2020 excavation report Figure 20.4.

The fish outline is visible, as is an irregular three-loop chain. The clean diagram printed alongside the interpretation is a normalized sign drawing; it is not itself a photograph of the incised strokes. In particular, the text's description of an internal stroke in only the middle oval should not be silently upgraded to a full-axis M417 rendering. The original report's quoted “cf. M-List Nos. 415 and 417” is an appropriately qualified comparison.

The preceding page's quotation of the 2015 report assigns fish to registration 21582 and chain to 21583, in that order. The retained secondary corpus instead associates K-447/5351.1, a plain W220 fish, with `KLB1 21583`; K-446/5350.1 is `+215+` and has no excavation number. This is an unresolved registration discrepancy. Figure 9 alone cannot settle it. The primary excavation review must take precedence over a forced corpus alias.

The archaeological photos do not show beads, bead sticks, end closures, or a secured transport package. Such uses are hypotheses introduced by the article, not photographed contents. Figure 10 is explicitly presented as AI-generated schematic material and is not independent archaeological evidence. An incised sign, a possible telescoping joint, and recovery out of installation position do not uniquely distinguish storage, drainage, repair stock, reuse, or other marking functions.

## Reproduction and limits

Rendering uses the existing `scripts/inspect_research_pdf.py`, with source `irc_2025_fish_bulletin.pdf`, prefixes `pipes-figure-bulletin` (pages 25 and 37, scale 4000) and `pipes-gold-bulletin` (pages 22–24, scale 3200). The panel-A crop uses pixel box `(530, 1860, 1135, 2710)` from the 2881×4000 page image. System Python lacked Pillow; the crop succeeded with the bundled dependency Python. This failed attempt and the W480 correction are retained in the JSON review log.

No new external download was required. All numerical and alias comparisons used only whitelisted corpus fields, never its proposed translation fields. Glyph depiction, corpus code alignment, archaeological function, and semantic decipherment remain separate levels of evidence. The duplicate figure row and unknown original text lengths warrant corrections to denominator language, while the four selected fish/U co-occurrences remain observable. Their frequency alone does not identify a commodity or language.

## Independent numerical verification

A second computation in `scripts/verify_pipe_chain_independent.py` reads only the raw CSV, existing strict corpus, and catalogue family definitions before comparing to the finished audit output. It does not import or read `audit_pipe_chain.py`. It groups raw object IDs before selecting single-row, strict, complete-preservation seals with more than two tokens, producing **931 objects**, including six chain-bearing objects. It independently reconstructs the strata by site, literal object type, and exact token length. Each of the six informative strata has one chain-bearing object, allowing direct enumeration of all **64 binary outcome patterns** with exact rational arithmetic rather than reuse of the production convolution algorithm.

All stratum margins, observations, expected values, null probabilities, and exact upper tails match, for all four targets and both object and deduplicated-text universes. Deduplication by site, literal type, and whole sign sequence yields **918 text types**, still six chain-bearing texts. These are descriptive comparisons under a selected conditional exchangeability model; the verification does not validate a semantic interpretation.

| Target | Observed among 6 chain objects | Object upper tail | Deduplicated-text upper tail |
|---|---:|---:|---:|
| Selected fish family | 1 | 6857/6930 | 755/763 |
| Plain W220 | 1 | 17893/28875 | 106429/171675 |
| U candidates W705/W706 | 2 | 5377/8250 | 42637/65400 |
| Fish family or U candidates | 3 | 7864093/8316000 | 649573/686700 |

The union expectation is **4.0312193362**, with object upper tail **0.9456581289**. Its positive count is lower than the matched conditional expectation. This sample does not establish enrichment, let alone the proposed gemstone/bead meanings. The small six-object sample, incomplete excluded objects, singleton Khirsara stratum, and retrospective category correction remain limitations.

The review also caught stale protocol text naming W480 in the targets list after candidate codes had been corrected. The parent analyst was notified to correct that metadata before final output. Initial inspection used the incorrect filename `lipi_strict.json`; the existing `.jsonl` input was then located and used. No data or results arose from that failed read. Saved numerical evidence: [pipe_chain_independent_verification.json](../results/pipe_chain_independent_verification.json).
