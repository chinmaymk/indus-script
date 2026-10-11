# Token milestone check — 11 October 2026

Frozen cutoff: **2026-10-11 11:00:28 UTC**, or **4:00:28 a.m. Pacific time**.

**About 881 million recorded research tokens including automatic review.**
The billion-token milestone has not been reached. The exact retained total is
**880,868,259**: an increase of **41,953,497** since the first audit, leaving
**119,131,741** to reach one billion. Research models alone total **860,949,268**.

| Model or activity | Input including cache | Cached reads within input | Output including reasoning | Total |
| --- | ---: | ---: | ---: | ---: |
| Astra (gpt-6-astra), including subagents | 813,809,360 | 793,476,864 | 3,158,840 | 816,968,200 |
| Sol (gpt-6.1-sol), including subagents | 42,355,321 | 40,981,632 | 224,740 | 42,580,061 |
| Opus (claude-opus-5-5) | 1,352,535 | 1,050,928 | 38,497 | 1,391,032 |
| Fable (claude-fable-5-1) | 6,421 | 535 | 3,554 | 9,975 |
| Research models subtotal | 857,523,637 | 835,509,959 | 3,425,631 | 860,949,268 |
| Automatic review | 19,874,376 | 15,756,800 | 44,615 | 19,918,991 |
| Recorded research total | 877,398,013 | 851,266,759 | 3,470,246 | 880,868,259 |

About **851 million** are cached input reads; about **3.5 million** are output,
including reasoning. Cache reads are already within input, and reasoning is
already within output. Neither is added a second time. These counts are not
subscription-limit units, dollar cost, or distinct text generated.

## Scope and verification

Same research roots and exclusions as the [first audit](RESEARCH_TOKEN_USAGE.md):
the original and continuation research chats and recorded descendants, retained
Claude project usage, and the seven nonoverlapping Oct 10 CLI envelopes. The blog
and accounting chat and unrelated projects remain excluded. Thread inventory
confirms the same two research roots. No new Claude usage appears in this update.

Selected 151 Codex histories: two roots, 48 research subagents and 101 automatic
reviewers. Of these, 123 have usage records and 28 have none. All nonempty histories
reconcile per-response usage with the final recorded cumulative usage at the cutoff.
The same malformed nonusage line remains recorded; no usage record was skipped.
Eleven legacy counters disagree, so the matching response/cumulative ledger is used.

An independent check read the final cumulative counters directly from each frozen
source prefix, deduplicated Claude message IDs and counted the separate CLI totals
once. It reproduced **880,868,259**. All 160 source-prefix hashes were verified, and
a replay of the metadata capture reproduced the complete derived report.

Exact for the retained records; missing calls or complete provider billing cannot
be established. More usage does not establish decipherment.

## Frozen evidence

- Metadata-only capture: `data/raw/research-token-usage-oct11-v2.json`.
- Capture: 2,868,772 bytes; SHA256
  `92800c1a468323c21cba713e1c899830c33092c8e3ac2c566416e48a14e2f3a5`.
- Derived report: `results/research_token_usage_oct11_v2.json`.
- Verification: `results/research_token_usage_oct11_v2_verification.json`.
- Unchanged script: `scripts/audit_research_token_usage.py`.

```sh
python3 scripts/audit_research_token_usage.py \
  --from-capture data/raw/research-token-usage-oct11-v2.json \
  --report /tmp/indus-token-usage-new-replay.json
```

Use a new output path. Earlier captures and reports remain frozen. The blog still
uses its earlier 840-million cutoff; the planned billion-token headline is deferred.
