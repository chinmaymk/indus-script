# Token milestone check — 11 October 2026, 4:38 a.m. Pacific

Frozen cutoff: **2026-10-11T11:38:22Z**. Combined retained usage is **about 888 million
tokens**, exactly **888,184,680**, across all research models, subagents and
automatic reviews. Up **2,200,189** since the previous check;
**111,815,320** remain to reach one billion.

| Model or activity | Exact recorded total |
| --- | ---: |
| Astra and its subagents | 816,968,200 |
| Sol and its subagents | 49,759,247 |
| Opus | 1,391,032 |
| Fable | 9,975 |
| Automatic review | 20,056,226 |
| All recorded research | 888,184,680 |

Research models alone account for **868,128,454**.
The combined total includes about **858 million cached input reads** and
**3.5 million output tokens**, including reasoning. Cache and reasoning are
already within input and output; they are not added again. Counts are not
subscription-limit units or dollar cost.

The [original counting method](RESEARCH_TOKEN_USAGE.md) is unchanged. All
**124** histories with usage reconcile per-response totals
with final cumulative records. Blog/accounting and unrelated projects remain
excluded. No new Claude usage appears. Exact for retained records; complete
provider billing cannot be established. No decipherment claim follows from usage.

- Metadata-only capture: `data/raw/research-token-usage-oct11-v4.json`; **2,896,224 bytes**.
- Capture SHA256: `4115cba928aec7d9323e5304de99afe3c832194a101861df0955670a56b6c647`.
- Derived report: `results/research_token_usage_oct11_v4.json`.
- Unchanged script: `scripts/audit_research_token_usage.py`.

Earlier snapshots remain frozen. Blog retains its original 840-million cutoff;
the billion-token headline remains deferred.
