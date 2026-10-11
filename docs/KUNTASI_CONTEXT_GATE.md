# Kuntasi institutional source gate

Completed 11 October 2026. **The linked institutional file does not supply the
excavation report body, so the context test remains unavailable.** This is a source
coverage result, not evidence that the full report lacks inscriptions or suitable
contexts, and not a failed phonetic/semantic prediction.

The frozen [protocol](../data/processed/kuntasi_context_gate_protocol_v1.json)
selected the independently documented inscribed-artifact context frame in the
1996 report. A catalogue advertised x+383 pages and linked a public viewer.
The catalogue HTML had been retained before the user's Yajnadevam priority change.
This continuation resumed at that exact link without repeating discovery.

The View Book response is an HTML wrapper. Its iframe explicitly identifies
`/jspui/bitstream/123456789/44865/1/132490.pdf`. We recorded that link resolution
before acquisition and made one attempt at this precise payload. A read-only
critic agreed that resolving the wrapper to its explicit payload fits the single
linked-body bound; it is not a guessed endpoint. No viewer assets, alternatives,
references, authentication attempt or retry were requested.

The HTTP200 payload is a complete **three-page PDF**, 2,642,737 bytes,
SHA256 `4bd0be7e32be5a4ff8b622c870c86326d9c558a2079a98229667ef0c5f40571d`.
All three pages were rendered and visually inspected:

| PDF page | Observed material |
|---|---|
| 1 | Front cover: *Kuntasi: A Harappan Emporium on West Coast*; 1996 |
| 2 | Library flyleaf with donation stamp |
| 3 | Back cover |

The cover reads M.K.Dhavalikar, **M.R.Raval**, Y.M.Chitalwala. It resolves the
initials for this edition in favor of M.R.; the earlier citing article's M.H.
remains a recorded discrepancy. The file's completeness as an HTTP response
must not be confused with completeness of the advertised book.

No inscription inventory, object identifiers, working-floor/deposit associations,
quantity observations or manufacturing contrasts can be extracted from these
pages. Artifact counts and eligibility denominators remain **unknown**, not zero.
No signs were transcribed, tested or assigned values. A publisher's emblem on the
cover is not being promoted into an archaeological inscription record.

Independent criticism confirms the three-page count, cover identification and
absence of a report body in this retained file. The acquisition stopping rule is
reached. Reopen only on a specific newly available public report body or identified
context register, not another fetch of this same file or speculative path changes.

See [decision and pins](../results/kuntasi_context_gate_v1/decision.json),
[explicit payload resolution](../data/processed/kuntasi_explicit_payload_resolution_v1.json),
and [cover render](../results/kuntasi_context_gate_v1/retained-pdf-page-1.png).
Original bytes, viewer wrapper and response headers are retained in `data/raw/`
and registered in `data/sources.json`; renders and observations are derived results.
The overall decipherment goal remains unresolved.
