# Complete M328 concordance recovery

The primary catalogue's entire M328 block has now been transcribed at the indexed
line level: **323 occurrences in313 distinct lines across310 catalogue references**.
The reconstructed positional counts exactly reproduce Table I: **one solus,
19 initial,29 medial and274 final**. The previously selected export's apparent
initial-position preference cannot represent this sign's catalogue-wide behavior.

This is a recovery of published inscriptions, not a semantic decipherment.
Unidentified neighboring glyphs, primary doubt and physical loss remain explicit.
No sound, word or numerical value has been established.

## Scope and independent checks

M328 begins partway through printed564/PDF575 and ends partway through
printed584/PDF595, before M329. The earlier nine-page pilot supplies141 indexed
sightings. New reviews add17 at the opening boundary,48 on PDF585–587,50 on
PDF588–590, and67 on PDF591–595. Every R-column sighting has an object reference,
side, line and indexed token position. Context lines belonging to another indexed
sign are excluded from this inventory.

Several lines occur more than once because they contain repeated U signs. They
must be merged by reference/side/line, retaining separate indexed positions. For
example,4653/20 appears three times on PDF594 but is one line with three U signs.
References1623 and2847 each contribute distinct first- and third-side lines;
5413 contributes sides2 and3. The program refuses conflicting line transcriptions
or duplicate indexed positions. After merging, every recorded U token has its own
indexed sighting, and all323 expected occurrences are accounted for.

The review did not select or modify lines to force the total. Page boundaries and
R-column positions determine inclusion. Aggregate agreement is a strong coverage
check; it does not prove that every neighboring glyph has been identified correctly.

Primary-image reviews: [boundary](M77_U_EXTENSION_BOUNDARY.md),
[PDF585–587](M77_U_EXTENSION_STRUCTURE.md),
[PDF588–590](M77_U_EXTENSION_ICONOGRAPHY.md), and the parent's
[67-sighting ledger](../data/processed/m77_u_extension_parent.json).
The [promotion review](M77_U_PROMOTION_REVIEW.md) audits how the old pilot can be
used, and [independent crosschecks](../data/processed/m77_u_extension_crosscheck.json)
verify difficult glyphs and repeated-U alignments.

## Counts and retained uncertainty

| Measurement | Result |
|---|---:|
| Indexed M328 occurrences, including source doubt | 323 |
| Distinct reviewed lines | 313 |
| Distinct catalogue references, not proven independent artifacts | 310 |
| Lines containing primary doubt | 21 |
| Lines containing primary loss | 11 |
| Lines with a reviewer-unidentified visible glyph | 10 |
| Fully identified, undoubted, loss-free lines | 274 |
| Identified sign tokens, all types including primary doubt | 752 |
| Identified sign types | 59 |

The three uncertainty categories overlap. `UNKNOWN` is a visible glyph whose
inventory identity remains unresolved; `*UNKNOWN` also retains the source's doubt
mark. `LOSS` represents a positive passage of unknown extent. Neither kind is
deleted to make new adjacencies. Printed RTL normalization is retained; actual
writing direction is not inferred from concordance layout. Sides and lines are
never joined into a hypothetical sentence.

All positions count printed glyph slots and positive loss spans. This produces
Table I's exact M328 distribution. Restricting to loss-free lines instead gives
one solus,17 initial,26 medial and268 final occurrences. The agreement supports
this treatment for these M328 cases; it does not independently establish every
damage-counting convention across the full417-sign catalogue.

Two image-based corrections were required. Reference2208's fish-like glyph is
M070, distinguished from the initial M059 reading by an inner vertical stroke.
Reference4309/22 has M141, distinguished from the initial M149 guess by straight
inner vertical strokes. The export comparison prompted reinspection, but the
corrections were made against enlarged primary images and the numbered sign list.
Previous choices and evidence remain in the review history.

The earlier4316 prefix had partly come from the candidate export. A new independent
primary review confirms the visible sequence as
`M267 M099 M086 M336 UNKNOWN M089 M328`; the carrying-person glyph cannot safely be
distinguished among nearby inventory forms at the available resolution. This
replaces that candidate-derived identification in the new corpus, without changing
the historical pilot ledger. [Correction evidence](../data/processed/m77_u_4316_primary_review.json).

## What was missing from the export

All49 exported M328 occurrences lie on references included in this recovery.
There are45 export records containing U;41 match an entire reviewed line exactly,
accounting for45 exported U tokens. The remaining four records differ only at
reviewer-unidentified neighboring glyphs:1165,2169,2188 and4316. They are retained
as unresolved whole-line comparisons rather than silently filled from the export.
An exact string match alone does not identify a side or line where those fields
are absent from the export.

For265 reviewed references, the exported string has no M328 at all. Their reviewed
primary lines contain268 M328 occurrences. Summing the nonnegative per-reference
difference between reviewed and exported U counts gives274 missing occurrences,
conditional on correct reference identity and injective exported U tokens.
The new recovery localizes the entire aggregate deficit rather than merely
bounding it from Table I. It does not overwrite the original export or enlarge
the general strict statistical sample with a sign-selected dataset.

## Constraints on a reading

M328 is final in274/323 catalogue occurrences, about84.8%. It is also initial,
medial and solitary, so an unconditional terminal-only rule fails. Among the
fully identified, undoubted lines,227 consist exactly of a long-stroke group
followed by U:

| Visible long-stroke count | Exact two-sign lines |
|---|---:|
| One | 1 |
| Two | 70 |
| Three | 107 |
| Four | 49 |

These are graphic counts. Their interpretation as quantities or particular units
still lacks an independent anchor. The pattern supports a recurring short field;
the full inventory also requires uses outside that field. Any proposed M328
meaning must account for the other86 lines, doubt/loss, repeated-U strings and
the nonterminal positions without inventing a separate exception for each case.
Catalogue references can duplicate molds or related objects, so these counts are
not independent statistical trials.

## Persisted outputs and reproduction

- [Recovered313-line corpus](../data/processed/m77_u_recovered_lines.jsonl)
- [Counts, source hashes and per-reference export comparisons](../results/m77_u_recovery_audit.json)
- [Recovery and validation script](../scripts/recover_m77_u_concordance.py)
- [Parent transcription packaging script](../scripts/build_m77_u_extension_parent.py)
- [Tests for duplicate counting, boundaries and uncertainty](../tests/test_m77_u_recovery.py)

Run `python3 scripts/run_all.py`. The full417-sign evidence index now includes a
separate count of identified occurrences in these reviewed U-bearing contexts.
Zeros mean not identified in this selected context corpus, not absent from Indus
writing. Semantic and phonetic fields remain unresolved. All work in this phase
used already saved sources; no new downloads were needed.


## Later glyph correction

The [counterpart recovery](M77_U_COUNTERPARTS.md) exposed one neighboring-sign
error in the historical U corpus:3234/10 ends in M283, not M280. Primary glyphs and
the sign's own index onPDF544–545 confirm this. All U counts, positions and object
class results remain unchanged. The corrected current transcription is in
`data/processed/m77_primary_reviewed_contexts.jsonl`; the original stage output
retains its historical reading and the correction ledger preserves both versions.
