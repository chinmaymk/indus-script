# Working context

Start with `docs/ACTIVE_STATE.md`, then `git status --short`. Do not load the full
research log, all reports, or past model responses into the working context.
Use `docs/RESEARCH_INDEX.md` to open only the evidence needed for the current decision.

The full goal remains decipherment of the Indus script. No phonetic or semantic
key is established. Do not equate more transcription, tests, or documentation with
decipherment. User priority: work with Claude Code on a faster discriminating route.

## Loop discipline

- Keep one primary next action, its expected evidence, and a finite stopping rule
  in ACTIVE_STATE. Finish or falsify it before opening another broad route.
- Do not repeat closed searches, parameter sweeps, or artifact audits without a
  specific new source or a documented defect. Existing results remain evidence.
- A newly transcribed page is not automatically unseen or an independent holdout.
- Inspect live state before restarting any process. Poll a confirmed live handle;
  do not relaunch because output is quiet or a tool observation times out.
- Preserve frozen inputs and earlier releases. Distinguish uncertainty from loss,
  source doubt, and a missing observation. Never invent readings to complete coverage.
- Update ACTIVE_STATE at handoff, replacing stale operational notes rather than
  appending history. Put attempts/results/failures in `docs/RESEARCH_LOG.md`.
- Keep ACTIVE_STATE about one screen (target ≤650 words); do not copy long tables,
  agent transcripts, raw tool output, or full historical conclusions into it.

## Persistence and collaboration

All downloaded/captured source material belongs in `data/raw/`, registered with
bytes, SHA256 and provenance in `data/sources.json`. Derived results belong in
`data/processed/` or `results/`. User permits subagents and requests occasional
Claude Code collaboration. Prefer bounded read-only criticism before a new experiment.

GitHub backup is authorized: `origin/main`, https://github.com/chinmaymk/indus-script.git.
Keep Git LFS for source binaries; commit and push completed batches, then verify.
No archive outreach has been authorized; prepare concrete drafts before requesting
permission to send. Never mark the overall goal complete on structural evidence alone.
