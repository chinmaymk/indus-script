# Bounded coupled-ending protocol review

11 October 2026. Read-only mathematical review before new corpus counts. Reviewed
`data/processed/coupled_endings_protocol_v1.json`, SHA256
`108e09e93f7fd09c8bc547b953fd5d11b25b2bd3f8553f696bd1484bdc6549cd`.
No corpus fit, observed statistic, or permutation result was inspected. This
reviews the protocol, not its separately developed implementation.

**Superseded initial assessment:** the first review found no blocker within the
stated collision-permitting model. Before any real corpus counts, the parent
identified that deduplication makes this model incompatible with the selected
sample's guaranteed uniqueness. The correction below replaces that assessment:
v1's support proof is correct for its mathematical model, but its proposed p
values are not inferentially calibrated for the deduplicated sample. V2 repairs
this issue. The initial model-specific reasoning remains below as a record.

## Exact support certificate

Fix distinct endings A and B and a total-length stratum. Let R be the number of
distinct stems with at least two slots, and let nA/nB be the respective ending
frequencies. A supported stem needs two slots and one copy of each ending, so its
maximum count cannot exceed `min(R, nA, nB)`.

This bound is attainable: choose that many eligible stems, assign A and B once
to each, then assign all remaining endings arbitrarily to the remaining slots.
There are no residual restrictions under this null; duplicate resulting texts
are expressly allowed. Distinct total lengths cannot contain the same exact
stem when ending width is fixed at two, so these separately attainable maxima
add across strata. This proves the formula. It does not provide a simultaneous
maximum over different ending pairs, nor a probability or power calculation.
It would not remain a proof under a collision-free permutation null.

The support calculation must range over all pairs of available ending types
whose two coordinates both differ, including pairs never observed together on
a stem. A pair absent from the observed configuration may form under a shuffle.

## Permutations and selection

Uniform shuffling of intact ending copies among fixed slots preserves the stated
marginals. Collapsing collisions for the statistic is consistent with the support
proof. Each replicate's maximum must include every eligible pair it forms,
including pairs absent in the observed configuration; an empty maximum is zero.
The `+1` Monte Carlo p formula handles finite simulation and ties conservatively
under the stipulated joint exchangeability null. This is not strong pairwise
familywise control under arbitrary configurations of true and false pair nulls;
the protocol correctly disclaims that claim.

The no-observed-support early stop is a candidate-selection decision. It must
leave p values uncomputed, and cannot establish general absence of alternation.
Sampled-constant null maxima do not prove exact degeneracy or low/high power.

## Novelty and inference limits

This is a restricted two-sign rectangle statistic on a larger retained native-W
export subset. The previous `KOBER_ALTERNATIONS.md` screen tested one-/two-sign
rectangles on a small reviewed M77 slice. The completed single-position
`audit_substitution_network.py` does not enumerate these simultaneous two-position
changes. The new subset and coordinate restriction make this a specific unused
screen; it is not a reconstruction of Kober's full historical method.

Shuffling intact ending blocks **conditions on their internal penultimate/final
association**. Thus the test asks whether already-observed two-sign alternatives
share exact preceding stems unusually often. It does not compare coupled changes
against independent changes in the two terminal positions. Even a positive result
cannot by itself supply a syllabic grid, grammatical inflection, word boundaries,
or any phonetic/semantic reading.

Exact Mohenjo-daro and `SEAL:S` export codes avoid deliberately pooling sites and
type codes. They do not remove chronology, provenance, style, die, or cataloguing
dependencies, and `SEAL:S` is not an authenticated synonym for every stamp seal.
Duplicate-sequence suppression limits copy inflation without proving independence.
Primary checks can authenticate transcription witnesses, not independent
replication or historical exchangeability. Results remain exploratory reused-data
constraints under the frozen selection and stopping rules.

## Pre-run correction: condition on unique texts

Reviewed amendment `data/processed/coupled_endings_protocol_v2.json`, SHA256
`6715ace6c35f320279dd869998aa9425d9d8a58216b3ff1b3e7e642e1356cfbd`.
Neither this correction nor the initial review inspected real coupled-ending
counts. V2 supersedes v1 before the experiment.

Selecting one distinct full sequence guarantees a simple bipartite graph: no
stem can have two identical ending edges. V1 shuffles could create duplicates,
so its reference distribution does not condition on a property guaranteed by
selection. Merely stating unconditional exchangeability would not repair this
sample-space mismatch. V1 maxima could describe a hypothetical reference model,
but their p values would not calibrate the intended distinct-text null.

V2 samples each exact-length stratum separately. It proposes uniformly shuffled
ending copies among labelled stem slots and rejects the entire proposal if any
stem receives the same ending twice. Accepted draws therefore follow the uniform
conditional distribution given simplicity. For any simple graph with the fixed
stem degrees and ending frequencies, the number of corresponding slot assignments
is the same product of stem-degree factorials. If ending copies are individually
labelled, a further product of ending-frequency factorials is also constant.
Consequently the sampler is uniform over admissible simple graphs, rather than
weighting graphs according to how many repeated edges they contain.

Independent strata factor under this conditional null; combining the same-index
accepted draws gives independent full-corpus null replicates. A fixed acceptance
quota of 9,999 and fixed cap of 1,000,000 proposals per stratum are sound finite
stopping rules. Conditional on meeting the quota, the accepted values still have
the intended distribution: the acceptance times depend on acceptance indicators,
not on which admissible configurations were drawn. If any stratum misses its
quota, V2 correctly requires `computationally_unavailable`, null p values, and no
selected candidates. Partial accepted draws must not be used for inference.

The old support formula is now only an upper bound. For example, take four stems,
each with two slots, and three distinct ending types with frequencies A=2, B=2,
C=4; choose A/B differing in both coordinates. Simplicity forces C onto every
stem, leaving only one slot per stem. No stem can contain both A and B, although
`min(4, 2, 2)=2`. Thus the collision-relaxed construction is not generally
attainable under V2. An upper bound below two still proves insufficient support;
an observed qualifying pair itself proves feasibility but neither significance
nor power.

**Revised decision:** no mathematical blocker identified in V2's conditional
sampling design. Implementation still needs independent verification of rejection,
quotas, all-pair maxima, and cap-failure handling. Historical exchangeability and
interpretive limits remain assumptions and limitations, as stated above.
