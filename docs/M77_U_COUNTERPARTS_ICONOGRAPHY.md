# Primary counterpart recovery: iconography partition

The ledger `data/processed/m77_u_counterparts_iconography.json` accounts for all **74 references** assigned by the frozen counterpart protocol (5270–8117). It records **76 separate counterpart text lines**, **15 symbol-only metadata entries**, and **75 excluded selected stroke-plus-U fields**. Both selected fields on 5413 are excluded. No selected reference is omitted.

Every retained sequence was checked visually against the primary Texts entry and Mahadevan's numbered sign inventory. The original PDF, complete page renders, inventory renders and enlarged glyph crops have SHA-256 evidence records in the JSON. Primary Texts locators are PDF147–156 (printed136–145) and PDF168 (printed157). These are editorial drawings, not new inspections of artifact photographs. The candidate export was consulted for proposed IDs in a subset of first lines; accepted glyphs required primary-image confirmation, so this is not a blinded transcription.

Each text line retains its own side and line identifier in printed right-to-left normalization. Physical reading direction is not inferred from that convention. The two additional counterpart lines belong to 5471 and 5490:

| Reference | Side | Line | Primary-checked sequence |
| --- | --- | --- | --- |
| 5471 | 1 | 0 | M177 M307 M149 |
| 5471 | 2 | 0 | M076 M343 M224 |
| 5490 | 1 | 0 | M048 M047 M379 M245 M245 |
| 5490 | 2 | 0 | M307 M267 |

The enlarged 5471 crop shows one interior tick in M343. Treating this as the plain jar M342 would create a false match. Other distinctions preserved include M169 versus M162, plain versus internally marked or wrapped fish, lattice-chevron M136, and the adjacent separate curved signs M293/M123 in 5310. Reference 8117 independently reads M076 M342 M176.

Eight lines contain primary hatched loss: 5278, 5319, 5408, 5415, 5420, 5443, 5455 and 5483. Each `LOSS` represents a positive missing span of unknown length; the completely lost first line of 5483 is still represented. Six lines retain eight primary doubt marks: 5317, 5318, 5322, 5408, 5454 and 5495. There are no remaining reviewer-`UNKNOWN` glyphs in this partition. Complete accounting does not make a damaged or doubtful line eligible for a strict exact comparison.

Symbol-only metadata entries are kept outside the glyph strings. On 5471, the selected side3 text itself has an associated symbol code, while side4 is the separate symbol-only entry. Neither is silently concatenated with the two counterpart texts.

Validation checked the exact 74-reference selection, disjointness from all selected field line IDs, valid M001–M417 tokens, separate side/line keys, all evidence hashes, and the counts above. No downloads were required. This recovery supports comparisons of exact positioned counterpart bundles; it supplies no phonetic or semantic readings and does not itself establish that the U fields encode amounts.
