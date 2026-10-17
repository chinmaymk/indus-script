# Recorded research token usage on 17 October 2026

Frozen cutoff: **2026-10-17T21:43:12Z**, or **2:43:12 p.m. Pacific**.

**891,375,845 recorded tokens**, about **891 million**, across all research models,
their subagents and automatic review. Research models alone total **870,856,336**.
This is **3,191,165** more than the last audit. **108,624,155** remain to one billion.

| Model or activity | Input including cache | Cached reads within input | Output including reasoning | Total |
| --- | ---: | ---: | ---: | ---: |
| Astra and its subagents | 813,809,360 | 793,476,864 | 3,158,840 | 816,968,200 |
| Sol and its subagents | 52,203,969 | 50,566,656 | 283,160 | 52,487,129 |
| Opus | 1,352,535 | 1,050,928 | 38,497 | 1,391,032 |
| Fable | 6,421 | 535 | 3,554 | 9,975 |
| Research models subtotal | 867,372,285 | 845,094,983 | 3,484,051 | 870,856,336 |
| Automatic review | 20,473,709 | 16,285,184 | 45,800 | 20,519,509 |
| All recorded research | 887,845,994 | 861,380,167 | 3,529,851 | 891,375,845 |

About **861 million** are cached input reads; about **3.5 million** are output,
including reasoning. Cache reads are already within input, and reasoning is within
output. Counts do not measure subscription-limit units, dollar cost or unique text.

## Preserving earlier recorded usage

Only 32 of the earlier 152 selected Codex histories remain in the current local
capture. Counting today's files alone gives **503,858,796**, which omits previously
recorded usage. Missing local histories are not a reduction in tokens consumed.

The cumulative ledger therefore unions the pinned October 11 capture with the
October 17 capture by provider and response/message ID. It removes **4,064**
overlapping records, rejects conflicting counters/model/thread identities and
preserves the usage of the **120** histories absent from today's capture. Every
one of the 124 histories with usage reconciles the union against a cumulative
counter preserved in one of the source captures. The remaining 28 have no recorded
usage. Earlier original source files are partly absent; their availability and
hashes are not asserted anew.

The original scope is unchanged: two research roots and their recorded descendants,
Claude project usage and seven nonoverlapping CLI envelopes. Blog/accounting and
unrelated projects are excluded. No additional research root or new Claude usage
was found. Exact sums apply to retained records; complete provider billing is not
established. Token volume supplies no decipherment evidence.

## Evidence and reproduction

- Earlier frozen capture: `data/raw/research-token-usage-oct11-v4.json`, SHA256
  `4115cba928aec7d9323e5304de99afe3c832194a101861df0955670a56b6c647`.
- Current local metadata capture: `data/raw/research-token-usage-oct17-v1.json`,
  1,524,381 bytes; SHA256
  `428a8dd372ab740cbf16b595f5dc56fbaeda3dd564ed0aa75302c3a5b9bd2aee`.
- Current-files-only report: `results/research_token_usage_oct17_v1.json`.
- Combined cumulative report: `results/research_token_usage_oct17_v2.json`.
- Verification: `results/research_token_usage_oct17_v2_verification.json`.

```sh
python3 scripts/audit_research_token_usage.py \
  --from-capture data/raw/research-token-usage-oct17-v1.json \
  --baseline-capture data/raw/research-token-usage-oct11-v4.json \
  --report /tmp/indus-token-usage-oct17-replay.json
```

Use a new output path. All earlier captures and reports remain frozen. Independent
aggregation of the saved cumulative counters and unique Claude records reproduces
**891,375,845**. Checks confirm idempotence, rejection of conflicting usage/thread
identities, unchanged replay of the earlier single-capture report and exact replay
of the combined report.
