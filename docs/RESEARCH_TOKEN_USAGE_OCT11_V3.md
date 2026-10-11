# Token milestone check — 11 October 2026, 4:28 a.m. Pacific

At the frozen cutoff **2026-10-11T11:28:53Z**, the combined retained total is
**885,984,491 tokens**, or **about 886 million**, including all research models,
their subagents and automatic review. The billion-token milestone is not reached:
**114,015,509** remain. This is **5,116,232** more than the previous check.

| Model or activity | Exact recorded total |
| --- | ---: |
| Astra and its subagents | 816,968,200 |
| Sol and its subagents | 47,592,150 |
| Opus | 1,391,032 |
| Fable | 9,975 |
| Research models subtotal | 865,961,357 |
| Automatic review | 20,023,134 |
| All recorded research | 885,984,491 |

About **856 million** are cached input reads; about **3.5 million** are output,
including reasoning. Cache and reasoning are already within input and output,
respectively. Counts do not measure dollar cost or subscription-limit units.

The [original counting method](RESEARCH_TOKEN_USAGE.md) is unchanged: two research
roots and their recorded descendants, retained Claude usage and seven separate CLI
envelopes. The blog/accounting chat and unrelated projects remain excluded. All
124 histories with usage reconcile per-response and final cumulative counters.
There are 28 selected histories without usage; no recorded tokens are inferred.

Independent direct-source summation of final cumulative counters, deduplicated
Claude messages and CLI totals reproduces the total. All **161** source-prefix
hashes were verified. Frozen metadata replay exactly reproduces the derived report.
No new Claude usage appears. Exact for retained records; complete billing is not
established. No decipherment claim follows from token volume.

Frozen evidence:

- Capture: `data/raw/research-token-usage-oct11-v3.json`, **2,888,181 bytes**.
- Capture SHA256: `1fb934ccfa9ad911e7306ae9cb4647863a129289ff754ee2910da39d1e290ca8`.
- Report: `results/research_token_usage_oct11_v3.json`.
- Verification: `results/research_token_usage_oct11_v3_verification.json`.

Earlier snapshots remain preserved. The blog uses its original 840-million cutoff;
the billion-token headline is deferred.
