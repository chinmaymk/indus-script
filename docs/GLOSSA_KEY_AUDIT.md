# Audit of a public 2026 candidate reading key

23 September 2026. This is a test of particular public artifacts, not a judgment
about their author, every version of the proposal, or the Dravidian hypothesis.

The inspected key cannot currently supply established readings for our 417 symbols.
Several of its stated sign identifications contradict the primary Mahadevan forms,
and its coexisting releases do not define one consistent key. These are concrete
problems upstream of scoring proposed sounds against a dictionary.

## Frozen scope and provenance

The repository snapshot is
[BitConcepts/glossa-lab at 40812fc54470d5508b47af5fabcea7ccf044036c](https://github.com/BitConcepts/glossa-lab/tree/40812fc54470d5508b47af5fabcea7ccf044036c).
We retain the advertised `research/indus/anchor_table.json` and the distinct
`backend/reports/INDUS_FINAL_ANCHORS.json`. Neither replaces the other silently.
The pinned tree also contains multiple manuscripts with different coverage claims;
the [methodology review](GLOSSA_METHODOLOGY_REVIEW.md) records those separately.
The README-linked unversioned preprint PDF returned HTTP404; the differently named
v4 PDF was available and archived. No claim depends on a nonexistent local download.

All downloads are in `data/raw/`; URLs, sizes and SHA256 hashes are in
`data/sources.json`. Downloaded scripts were inspected as text and never executed.
Our own [audit script](../scripts/audit_glossa_key.py) regenerates
[the count audit](../results/glossa_key_audit.json) and
[a comparison row for every supplied sign](../results/glossa_candidate_comparison_417.json).

## Inventory coverage is not correctness

| Recomputed quantity | Advertised research key | Backend key at the same commit |
|---|---:|---:|
| All entries | 397 | 287 |
| Entries within M001–M417 | 397 | 286 |
| Supplied M signs absent | 20 | 131 |
| HIGH | 75 | 166 |
| MEDIUM | 86 | 109 |
| LOW | 236 | 8 |
| CANDIDATE | 0 | 4 |

The backend additionally contains `H003`, which is not one of the supplied
Mahadevan identifiers. It is retained as an out-of-inventory entry, not renumbered.
Confidence labels above belong to the proposal; they are not our confidence ratings.
The two keys share 286 identifiers; 115 have different reading strings. A change
may reflect spelling or substantive reassignment: this count does not distinguish
them or measure errors. Several embedded summary counters disagree with actual
entries. The script retains both and computes from entries rather than stale totals.

The research key's `total=161` correctly denotes its HIGH+MEDIUM entries, not all
397 entries; that distinction is not a defect. Its missing signs are M083, M084,
M085, M095, M096, M097, M098, M173, M191, M196, M205, M225, M234, M306, M317,
M352, M358, M366, M372 and M417. A claim to have addressed this particular supplied
inventory therefore still needs explicit treatment of those forms.

Using nominal M identifiers alone, its HIGH+MEDIUM subset covers 9,226 of the
13,372 occurrences in primary Table I. The backend subset covers 10,924. These are
inventory intersections, **not translation accuracies**, and cannot authenticate
the namespace or correct proposed sounds. They have different denominators from
the proposal's Holdat token-coverage figures and do not refute those figures.

## Primary identity checks

Five deliberately selected checks are documented in the
[independent visual review](GLOSSA_SIGN_IDENTITY_REVIEW.md), with exact table-page,
half and row locators, source hashes and supplied glyph comparisons.

| Sign | Claimed identification or basis | Observed primary form |
|---|---|---|
| M012 | Single stroke / numeral one | Branched figure with paired loop forms |
| M047 | Plain fish | Bent/forked stem ending in a small enclosure |
| M059 | Numeral seven | Plain fish-like oval, appendages and forked tail |
| M099 | Jar/vessel | Two short parallel bars |
| M328 | Man/person | Plain U-shaped form |

All five original basis strings remain in the backend key. The M099 crosswalk
also calls it a bow/archer, conflicting with the key's vessel description and
the primary form. This is not fixed by keeping numerically equal M and P labels.

The distinction between shape and assigned meaning matters. The M059 source says
“Numeral 7”; it does **not** explicitly say that it is seven visible strokes.
Its fish-like shape supplies no tally-count support for seven, but an arbitrary
conventional numeral value cannot be disproved by that shape. The same limitation
applies to phonetic rebus readings: wrong pictorial premises invalidate the cited
support, not every conceivable assignment of the proposed sound. Five selected
checks cannot estimate an error rate for all 397 or 287 entries.

## What survives, and what would change the conclusion

The [static validation review](GLOSSA_METHODOLOGY_REVIEW.md) also finds an
uppercase-only uniform comparator applied to case-preserved reading initials,
artificial bigrams between inscriptions, and an incorrect conditional-entropy
marginal. Its entropy formula gives −1 bit for two copies of `[a,b]`, where the
correct conditional entropy is zero. These are reproducible mathematical/code
findings; they do not require running the downloaded program or reconstructing
its private corpus. The source's own Meluhhan-name tests report no discriminative
matches. No successful independently grounded phonetic prediction emerged here.

A positional class may be real without establishing a particular Dravidian suffix.
A fish-shaped pictogram may be identified without identifying the spoken word for
fish, a homophone for star, or the language. Dictionary compatibility and readable
phrases require controls for the freedom used in choosing the key. The separate
[2026 specificity review](NONSPECIFICITY_2026_REVIEW.md) examines a relevant
methodological critique, but supplies no new semantic anchor itself.

The public [sequence export](GLOSSA_EXPORT_REVIEW.md) must likewise be audited by
source and namespace; its filename does not establish an independent ICIT corpus.
Its M77-labeled records may be useful for future primary checks, subject to
recovering object identities and transcription conventions.

To reconsider this key, first freeze one corrected version, authenticate its
M/P/W crosswalk against printed glyphs and objects, and state exactly which readings
were chosen using each dataset. Then test predictions about independently known
content on untouched objects, with all alternatives and exceptions specified in
advance. Nothing in this audit licenses replacing unresolved values with guesses.
All 417 established phonetic and semantic fields remain null in the comparison
and in the main evidence index.
