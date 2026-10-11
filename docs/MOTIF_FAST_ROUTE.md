# Frozen motif screen: no selected lead

10 October 2026. The bounded experiment suggested by Claude Opus selected **zero
sign–motif pairs**. It is closed under the recorded design; do not rerun with new
bins, motifs, features or thresholds merely to obtain a signal.

| Result | Value |
|---|---:|
| Discovery site | Mohenjo-daro |
| Distinct eligible text families | 716 |
| Eligible native-sign/raw-motif pairs | 748 |
| Permutations | 9,999 |
| Largest observed Z | 3.829860 |
| Global maxT permutation p | 0.7609 |
| Candidates passing frozen maxT p ≤ 0.01 | 0 |

The largest Z belongs to native W455 / raw `Rhin`, with sign support 12 and
positive-motif support 13 families; its adjusted p is 0.7609. This is a diagnostic
of the stopped screen, not a selected candidate or a proposed rhinoceros reading.
No Harappa transfer, Good/Fair sensitivity or primary glyph-pair checks were run,
because selection was empty. The [stop record](../results/motif_fast_route_v2/stop.json)
prevents accidentally restarting these downstream phases.

The design uses exact exported `SEAL:S`, validates grouped artifacts before
selection, gives each exact complete sequence per site weight one, and retains
fractional raw-motif vectors when identical texts occur on differently labelled
objects. Presence-only native W features are tested by whole-vector shuffles within
exact length. No proposed translations were imported. All rows were previously
available: this is exploratory reused-data analysis, not a blind historical test.

This does not establish absence of motif information, support the name hypothesis,
reject language, or assign any sound/meaning. Unrecorded phase, style, provenance
and die dependence remain limitations; no justified alternative or global power
calculation was supplied. It only supplies no selected lead under this fixed design.

- [Protocol v2](../data/processed/motif_fast_route_protocol_v2.json), frozen SHA256
  `9a339d2bd761658d2ed56465cdc6efe635efe6432f13185f063a5dde64a8f1d3`
- [Mathematical review and pre-run corrections](MOTIF_PROTOCOL_REVIEW.md)
- [Full discovery output and input/code hashes](../results/motif_fast_route_v2/discovery.json)
- [Frozen empty selection](../results/motif_fast_route_v2/candidates.json), SHA256
  `3e4c7af250f63dfe44166e3b5e4a480afa5a335562d7a8b37bbeebbf3b752cfe`
- [Claude collaboration and rejected interpretations](CLAUDE_SECOND_OPINION.md)

Reproduction uses the bundled Python with NumPy and a **new** output directory;
existing phase files deliberately refuse overwrite:

```sh
python scripts/analyze_motif_fast_route.py discovery --output-dir results/motif_reproduction
```

Do not run this command as routine agent-loop startup. Existing results suffice.
The initial invocation failed before association calculation because optional
unselected CSV suffix fields were missing; ingestion was corrected and tested.
A separate constant-fraction centering defect was fixed using synthetic data before
the first invocation. The successful run used the unchanged v2 protocol. All 294
unit tests pass, including 18 motif tests; all 505 registered raw files verify.
