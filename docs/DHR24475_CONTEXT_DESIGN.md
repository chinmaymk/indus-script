# DHR-24475 context screen: frozen design

This is a bounded locator for source photographs, not a test of meaning. The seed is CSV row **4196.1**, excavation label **DHR-24475**, with retained W string `+391-002-365-550+`. The source reports `R/L`, `preservation=complete`, `complete=Y`, and `condition=Poor`; these are independent metadata, not facts inferred from the plus signs. No context-screen outcomes were inspected in preparing this design.

The executable specification is [the protocol](../data/processed/dhr24475_context_protocol.json), SHA-256 `56b5e3b0477baa90297b5397c09c95aba767b02033ad2404ac2d2f11292ab7c5`. Its only corpus source is `data/raw/lipi_inscriptions.csv`, SHA-256 `b8dcb325a2e2cd3cde12ac12e7a418b0348e45713c9ee28aad81b645d2ac5ee4` (1204921 bytes). The attempt log in the protocol records the bounded seed/header check. No downloads or translation columns are needed.

## Fixed comparisons

1. Exact four-code duplicates of `391,002,365,550`, with the seed labelled separately.
2. Full-length exact-tail neighbors `X,002,365,550`, where `X` differs from `391`.
3. All four-code one-position substitutions, recording the changed serialized position. Class 2 is a subset of class 3, so their totals must not be added.

“Initial” means stored slot zero. The screen makes no reversal from the direction label, no W-to-M conversion, no insertion/deletion matching, and no concatenation of fields or faces.

## Parsing and uncertainty

The primary branch requires exactly `+ddd-ddd-ddd-ddd+` (ASCII digits), excluding `000`. Outer whitespace may be trimmed for parsing only; the exact source text remains in the output. This branch means **closed-plus syntax**, not a complete physical inscription. Every condition and preservation label remains visible, including Poor.

A separate boundary sensitivity permits exactly one `+`, `[` or `]` at each endpoint, with at least one non-plus endpoint. A separate slash branch permits four hyphen-delimited cells containing three-digit codes separated by `/`. It preserves the raw alternatives and reports only mechanical compatibility. If each cell has option set S and target token t, minimum distance counts positions with t absent from S; maximum distance counts positions with at least one non-target option. A possible duplicate has minimum distance zero; a possible one-position neighbor has minimum distance <= 1 <= maximum distance. A possible full-tail neighbor needs the target option in every tail cell and a non-target option in the initial cell. None becomes a certain hit or multiple attestations by expansion.

Any eligible four-cell string containing `000` is retained as uncertain, without treating that token as a known sign or wildcard. Other punctuation, malformed cells, missing boundary markers, interior boundaries and other lengths receive explicit exclusion reasons. The protocol does not silently repair them or split multi-field strings.

## Counts and limits

Report source rows and exact ids, distinct raw literal strings, and (separately) literal token tuples. Preserve class overlaps and branch separation. Slash formulas are counted once as raw formulas. Source-row indices guard against duplicate ids. A numeric id stem is only a possible row-family/face key; same-stem companions can be listed separately but are neither concatenated nor counted as matching rows unless they independently match. Textual duplicates are not a basis for merging artifacts. Physical identity and independence remain unresolved.

The finite question is whether this pinned source contains an additional primary four-code exact-tail substitution. A zero result would reject only that restricted existence claim. Any hits would supply photograph locators, not evidence of a shared roof meaning, numeral value or language. A source-selected context screen cannot become independent semantic validation by reporting a count.
