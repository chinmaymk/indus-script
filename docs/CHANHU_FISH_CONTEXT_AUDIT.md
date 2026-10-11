# Chanhudaro fish signs: a local pattern with unresolved context

25 September 2026. **Fish-family signs are frequent in the available Square
9/D seal texts, but the current evidence does not establish a gemstone meaning.**
Checking original catalogues changes the comparison, and the reported bead
workshop crosses the spatial and chronological boundaries used in a simple
square-level count. No phonetic value or language is identified.

## What can be reproduced

The 2025 bulletin reports six fish-bearing seals among nine from 9/D. Its
Figure5 actually labels eight objects there, five with orange fish borders.
One of the eight is a clay tag, C-87. Both the figure's map and its inscription
panels give the same eight identifiers. This internal discrepancy remains
unreconciled; it does not prove that no additional object existed.
[Bulletin, pp12–13](https://rmrl-site-files.s3.us-east-1.amazonaws.com/PDFFIles/bulletin/bulletin-No-6-June-2025.pdf).

The independent [figure inventory](CHANHU_FIGURE5_REVIEW.md) records 47 catalogue
identifiers, 46 drawing panels and 17 orange designations across 17 squares.
It preserves shared panels, similar texts, tags, pottery and metal implements.
These are the author's visual classifications, not an independently complete
excavation corpus. The caption explicitly describes an illustrative selection.

For a separate, reproducible comparison, the retained secondary export supplies
72 Chanhudaro object groups in 74 rows. We fixed the same fish-family mapping
used in the earlier crab audit before counting this export: catalogue P050,
P051 and P056–P064. A sensitivity uses plain W220 alone. The mapping is a
defined graphic subset, **not every possible fish-like sign**. In particular,
unmapped W221 and excluded compounds must not be interpreted as non-fish meanings.

Each source object group is counted once. A certain observed member of the
selected family remains positive despite damage elsewhere. A missing,
doubtful or incomplete text without a certain member remains unknown.
"Absent" below means absent from the selected family under those rules.

| Seal cohort | Objects | Selected-family present | Absent | Unknown |
|---|---:|---:|---:|---:|
|9/D, unmodified secondary locations|9|5|3|1|
|Other known squares, same source|45|15|21|9|
|9/D, three selected catalogue-location overlays|7|5|1|1|
|Other known squares, same overlays|47|15|23|9|

The overlaid 9/D group is C-10, C-22, C-53, C-55, C-58, C-65 and C-79.
C-22 is unknown under the source's incomplete-text flag; C-55 lacks the selected
family. C-53 and C-58 have identical raw texts, so five positive objects are
not five independent text types. Counting all object classes adds the
fish-negative C-87 tag to 9/D, giving five positives, two negatives and one
unknown among eight groups. Adding unknown original texts to either side gives
bounds rather than a single assumed rate.

After the overlays, 8/E has three positive seals among four, all classifiable.
Thus the highest displayed *number* in 9/D is not uniquely the highest
*fraction*. Plain W220 gives only two certain positives in 9/D, with three
unknowns among seven. Sign-family choice matters.

[All rows, exclusions, square counts and sensitivities](../results/chanhu_fish_audit.json).

## Why the original catalogues change the count

These are separate overlays; the downloaded source is unchanged.

| Secondary ID / excavation number | Exact original entry | Difference or limitation |
|---|---|---|
|C-6 / CH4852|LII.5, p293: Cutting, 9/F, locus469, −2.8ft|Secondary export says9/D. Narrative p15 confirms the Cutting find and level.|
|C-74 / CH3215|LI.14, p292: 9/B, locus283, +6.9ft|Secondary says9/D; the bulletin says9/B. A different object at locus283 is listed under9/D onp57, so this remains a catalogue-based sensitivity, not a final plan-resolved attribution.|
|C-57 / CH3811|LII.29, p293: Cutting, 9/F, locus468, +3.8ft|Secondary 8/C, locus289, +8.6ft matches a different catalogue object, CH3492/LII.32. The cause is not inferred.|

Original scans: [p292](../data/raw/chanhu_context_leaf312.jpg),
[p293](../data/raw/chanhu_context_leaf313.jpg),
[p15](../data/raw/chanhu_context_leaf35.jpg).

The same catalogue contains an additional 9/D seal fragment, CH2558/LII.12,
locus106, +8.8ft. Its [photograph](../data/raw/chanhu_context_leaf417.jpg) shows
the lower animal-bearing part, without an established surviving inscription.
It is not a synthetic fish-negative text, and is kept outside the secondary
transcription comparison. This shows why a count of excavated seal objects
differs from a count of surviving texts.

The remaining background locations and transcriptions have not all received
equivalent primary verification. These selective overlays therefore improve
specific records without validating an entire statistical control population.
The secondary phase fields are unspecified. Restricting the comparison to the
mapped grid does not establish that its objects belong to the same occupation.

## The archaeological comparison is not "workshop versus non-workshop"

Original production evidence supports room215 and associated areas as places
of beadworking. It does not make every 9/D object part of one floor deposit:

- CH2285, the C-22 candidate, is reported in room215 at+10.4ft.
- CH2428, C-65, comes from adjacent passage286, catalogue level+9.7ft.
- CH2529CC, C-69, is in associated courtyard297 at+10.4ft, but in square8/C.
- CH2297, C-10, has a primary discrepancy: narrativep46 puts it slightly below
  beads at+6.8ft, while the catalogue gives+10.0ft.

Room215 and locus287 contain records at several elevations. Other activities,
including shellworking and metalworking, occurred in associated spaces. The
report's furnace interpretation also contains explicit uncertainty.
The [independent archaeological review](CHANHU_WORKSHOP_CONTEXT_REVIEW.md)
separates those observations and interpretations.

Most decisively for controls, originalp52 explicitly reports beadworking in
8/C, 9/C, 9/D and9/F, as well as elsewhere. A retrospective coarse sensitivity
combining those four named squares yields eight positive, nine negative and
three unknown seal groups among20. Other known squares yield12 positive,
15 negative and7 unknown among34. Those other squares are **unclassified**, not
verified absence-of-beadworking controls. This comparison was added after
inspection and cannot establish either a craft association or its absence.
It shows that the local9/D pattern does not automatically extend to every
archaeologically documented beadworking square.

## Statistical and semantic limits

The script retains fixed-margin upper-tail calculations for the classifiable
secondary tables: approximately0.249 before overlays and0.058 after, for seals
in9/D versus all other known squares. These are descriptive, source-exposed
calculations, **not confirmatory p-values**: the target was selected in the
published argument, unknown texts are excluded from those particular tables,
duplicate texts and deposits create dependence, and the controls are not
verified non-workshops. They neither prove nor disprove gemstone semantics.
The actual counts and uncertainty bounds take precedence over these numbers.

The useful surviving hypothesis is that some fish-family signs could be
associated with particular activities, people or institutions in these areas.
Discriminating those possibilities requires independently classified deposits,
complete provenance and a prediction more specific than spatial proximity.
The present findings do not choose a commodity name, a craft label, an owner's
name, a language or a pronunciation. All417 established sign readings remain null.

## Reproduction

Run `python scripts/audit_chanhu_fish.py` or `python scripts/run_all.py`.
The [protocol](../data/processed/chanhu_fish_protocol.json) distinguishes the
initial fixed rules from the later exploratory square grouping. The
[primary ledger](../data/processed/chanhu_primary_review.json) pins source and
image hashes and preserves every selected location discrepancy. Downloads are
retained together in `data/raw/` and registered in `data/sources.json`.
