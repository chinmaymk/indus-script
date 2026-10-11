# Alternative Mahadevan scan: missing Table IV pages

The alternative scan does **not** recover printed pages 758–759 in the expected Table IV sequence. Direct visual review shows printed page 757 immediately followed by printed page 760. Therefore M328 and M342–M345 were not transcribed, and their object-type totals remain unverified by this scan.

The source is `data/raw/mahadevan_alternative_scan.pdf`, Internet Archive item `masi77indusscripttextsconcordancestablesiravathammahadevan_410_D`. Its cover identifies Mahadevan's 1977 ASI Memoir 77; the PDF contains 843 pages. The cover has extractable text, but the four table pages inspected have no extracted text. Page identification and table titles below were read from rendered images, not inferred from a fixed page offset.

| PDF page (one-based) | Printed page | Visually confirmed content |
|---|---|---|
| 768 | 756 | Table IV continuation, object-type count columns |
| 769 | 757 | Table IV: Distribution of Signs by Object Types |
| 770 | 760 | Table V: Distribution of Signs by Field Symbols |
| 771 | 761 | Table V continuation |

The Table IV headers on printed 757 read `SIGN`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `9`, `TOT`, repeated for the two page columns. Table V uses `SIGN`, `FS`, `FR` blocks. Thus page 770 is a different table; its numbers cannot substitute for the missing object-type counts.

Evidence images are `results/m77-alternative-768.png` through `results/m77-alternative-771.png`. [The evidence ledger](../data/processed/m77_alternative_scan_review.json) records the source URL, PDF and archive-metadata hashes, byte count, rendered-image hashes and per-row unresolved status. Poppler rendered the images; stderr was redirected to avoid font-configuration log noise.

This is a bounded negative result for the expected page neighborhood, not an exhaustive visual search for displaced pages elsewhere in the 843-page file. Different Internet Archive item identifiers do not establish that the underlying scans are independent. No secondary counts or guessed totals were substituted for the missing primary rows.
