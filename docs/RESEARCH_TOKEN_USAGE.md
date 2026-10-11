# Recorded token usage for the Indus investigation

Latest check: **about 881 million tokens** at 4:00 a.m. Pacific on 11 October.
See [the second audit](RESEARCH_TOKEN_USAGE_OCT11_V2.md). The first audit below is
preserved at its original cutoff, which the blog currently uses.

Audited 11 October 2026 for the author's blog. Frozen cutoff:
**2026-10-11 08:23:38.418 UTC**, or **1:23:38.418 a.m. America/Los_Angeles**.
This is the timestamp of the author's token-accounting request.

**821,734,966 recorded tokens across the research models; 838,914,762 including
automatic review overhead.** Counts cover retained research histories from
22 September through the cutoff, including later model collaboration. They do
not isolate only the initial two-week attempt.

| Model | Input including cache | Cached input reads within input | Output including reasoning | Total |
| --- | ---: | ---: | ---: | ---: |
| gpt-6-astra | 813,809,360 | 793,476,864 | 3,158,840 | 816,968,200 |
| gpt-6.1-sol | 3,347,915 | 3,161,984 | 17,844 | 3,365,759 |
| claude-opus-5-5 | 1,352,535 | 1,050,928 | 38,497 | 1,391,032 |
| claude-fable-5-1 | 6,421 | 535 | 3,554 | 9,975 |
| Research models subtotal | 818,516,231 | 797,690,311 | 3,218,735 | 821,734,966 |
| codex-auto-review | 17,139,879 | 13,270,272 | 39,917 | 17,179,796 |
| Recorded research total | 835,656,110 | 810,960,583 | 3,258,652 | 838,914,762 |

The Astra main chat contributes 394,820,084 tokens; its 44 subagent histories
contribute 422,148,116. Sol has one root and one research subagent. The automatic
review counters belong to separate guardian histories; they are not attributed
to Astra or Sol.

## Scope and counting

Selected the original research root `01a0cb0a-c3d3-7290-a6bb-752a686c8f57`,
the continuation root `01a12a06-ffd2-7371-a682-3309f96488ce`, and their descendants
using recorded parent relationships. This selects 143 histories: 2 roots,
45 research subagents, and 96 automatic reviewers. Of these, 117 have usage
records and 26 have no usage records. Absence contributes no recorded tokens;
it is not a proof that an unrecorded provider call never occurred.

Excluded the blog/accounting chat, its descendants, and the unrelated grammar
chat, even though they used the same repository directory. Included the retained
Claude project message histories and seven saved Oct 10 CLI result envelopes.
Successful CLI sessions and the interactive Claude session have distinct IDs.
Failed zero-token envelopes are preserved and add zero to the recorded tally.

For OpenAI, sum each uniquely identified response's `usage`, not repeatedly
displayed cumulative counters. All 117 nonempty histories reconcile component by
component with their final `token_usage_record.thread_token_usage` at the cutoff.
Nine legacy `event_msg`/SQLite-style counters disagree with these records; the
audit uses the per-response ledger and its matching cumulative record. One malformed
nonusage log line is recorded as a source defect; no malformed usage record was
silently accepted. Source byte-prefix hashes pin live files at capture time.

For Claude, count one usage record per message ID. Removed 17 repeated message
blocks with identical usage. Add the nonoverlapping CLI session aggregates once;
their per-model counters reconcile with the envelope's aggregate usage.

OpenAI input already includes cached input. Claude total input is its uncached
input plus cache creation plus cache reads. Reasoning/thinking tokens are part of
output and are not added again. The normalized combined total is input plus
output. See [OpenAI usage definitions](https://developers.openai.com/api/docs/guides/agents-api/observability)
and [Claude cache definitions](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
In total, 810,960,583 tokens are cache reads; excluding cache reads leaves
27,954,179 tokens. Neither count is a dollar bill, GPU-compute measure, unique-text
count or subscription allowance measure.

These are exact sums of retained recorded usage. Log completeness and provider
billing completeness are not established. The author reports multiple usage
resets; this audit does not claim an exact number of resets. No scientific result
or decipherment claim follows from token volume.

## Frozen evidence and reproduction

- Metadata-only capture: `data/raw/research-token-usage-oct11-v1.json`; no prompts,
  responses, credentials or account IDs were copied into it.
- Capture SHA256: `31e450d4f2c18630520017b65aba80c9fe75609c6aadae3ba155fc2b7747db10`.
- Derived tally: `results/research_token_usage_oct11_v1.json`.
- Script: `scripts/audit_research_token_usage.py`.

```sh
python3 scripts/audit_research_token_usage.py \
  --from-capture data/raw/research-token-usage-oct11-v1.json \
  --report /tmp/indus-token-usage-new-replay.json
```

Use a new output path; the script refuses to overwrite frozen captures or reports.
An independent check sums the last cumulative record from each selected OpenAI
history, unique Claude messages, and CLI envelope totals. It reproduces the
838,914,762 total. A replay from the frozen metadata capture reproduces the full
derived report. Original local source-prefix hashes were independently checked.
