# DHR-24475: comparison search and graphic limits

**The retained secondary corpus has no additional exact four-code duplicate or one-position substitution neighbor of DHR-24475 under the declared grammar. Its photograph does not independently establish a unique four-M-code transcription.** These are separate results: the first concerns stored strings, the second the legibility and segmentation of an original object image.

## Declared string search

The frozen [design](DHR24475_CONTEXT_DESIGN.md) and [protocol](../data/processed/dhr24475_context_protocol.json) were saved before the first outcome count. The seed is row4196.1, `+391-002-365-550+`. A [pre-count clarification](DHR24475_CONTEXT_IMPLEMENTATION.md) excluded999 alongside000 as an unknown/separator, following the existing corpus parser. The query tests full-length exact duplicates, changes at stored position zero with the remaining three codes fixed, and changes at any single position. It performs no reversal, insertion/deletion, partial-tail search, face concatenation or W-to-M conversion.

|Branch or exclusion|Rows|Additional duplicate|One-position neighbor|
|---|---:|---:|---:|
|Closed-plus, four known singleton codes|552|0|0|
|Four singleton codes with a non-plus boundary|50|0|0|
|Four cells with slash alternatives|10|0 possible|0 possible|
|Four-cell unknown/separator cases|254|Not classified|Not classified|
|Other excluded syntax or length|4,814|Not classified|Not classified|
|Entire scanned source|5,680|Not pooled|Not pooled|

The seed is the only primary duplicate and the only matching row overall. The exact-tail initial-substitution class is a subset of one-position neighbors and is also empty. Counts for these classes must not be added. No same-stem companion supplies another matching field. Distinct raw strings, token tuples, source row indices, literal metadata and all parser dispositions are retained in the [result](../results/dhr24475_context_screen.json). Slash alternatives never become certain readings or multiple attestations.

This rejects only the finite existence claim for that pinned source, grammar and stored transcription. It neither proves absence of an ancient parallel nor tests a common roof meaning. The seed itself has uncertain graphic segmentation, so even a future stored-string match would need independent object and image authentication.

## Photograph and primary sign comparison

The [independent graphic review](DHR24475_GRAPHIC_REVIEW.md) inspected the photo and original numbered sign representatives without context outcomes or translation fields. The roof above a branching stem is the strongest visible feature, compatible with M163. The upper-central marks cannot securely be isolated as a two-stroke unit or assigned between M099 andM100. A shaft/wing group is compatible with M402 but has weak internal detail. The left crossed form cannot securely distinguish M216 from nearby forms such as M222.

The four overlapping inspection crops are not certified token boundaries. No reading direction, reflection convention or ordered M string is supplied by this review. The earlier exact accession identity and broad roof observation remain valid; the more detailed review does not convert them into a complete transcription. No source sign, damaged stroke or corpus flag was repaired.

## Verification and next direction

Six synthetic tests check matching against all81 strings over a three-code alphabet and reject reversed, embedded, different-length, damaged and ambiguous false matches. A separate verifier reconstructs the corpus screen without importing producer functions, including direct expansion of slash alternatives. [Producer](../scripts/screen_dhr24475_contexts.py), [independent verifier](../scripts/verify_dhr24475_contexts.py), [independent results](../results/dhr24475_context_independent.json).

The graphic review pins20 evidence files; the [broader evidence synthesis](DECIPHERMENT_EVIDENCE_GAP_REVIEW.md) pins39 reviewed files and distinguishes narrow contradictions from unidentified meanings. Together they preserve all417 unresolved readings. The synthesis identifies two more discriminating research directions: independently measured capacity predictions within a fixed vessel class, and deposit-level craft associations with genuine comparison contexts and bounds for unreadable inscriptions. Those are proposed tests, not newly demonstrated findings.

No new source download was needed. A new [streaming fetch helper](../scripts/fetch_preserved_source.py) retains response/error bytes incrementally in `data/raw/`, including partial files on interruption, addressing the previous full-PDF retention failure. It is saved for future acquisition and was syntax-checked; no live download was performed with it in this phase.
