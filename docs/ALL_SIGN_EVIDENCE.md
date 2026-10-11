# Consolidated evidence for all 417 supplied signs

The [machine-readable index](../results/sign_evidence_417.json) combines direct
Mahadevan positional counts, provisional catalogue correspondence, sign-family
test coverage, copper-tablet associations, exact substitution evidence, and
qualified profiles from a recovered secondary M77 transcription.
A [compact CSV](../results/sign_evidence_417.csv)
is available for inspection. Every M001–M417 appears exactly once. This is an
evidence index, not a translation key; all sounds and meanings remain undetermined.

Twenty rows now have conditional catalogue paths to the recent
[M-294 hoard](M294_HOARD_AUDIT.md), [pipe/chain](PIPE_CHAIN_AUDIT.md), and
[L-51 motif/ending](L51_MOTIF_AUDIT.md) audits. These links distinguish verified
find associations and structural patterns from unverified object meanings.
They preserve every M candidate and W family member; a comparison target need
not occur on the named artifact. The positive modified-fish association with
the L-51 ending is therefore not silently converted into individual M–W
identities or gemstone readings. Source hashes link the index to all three audits.

The direct primary profiles cover 13,372 occurrences in the printed table. They do
not depend on a W-number mapping. Family and copper results do depend on source
cross-references, and are stored separately. A supported family result is not
automatically a result about each individual M variant.

Six M rows have **conditional catalogue paths** to tested copper singleton codes:

| M row | Source P entry | Copper W candidate | Scope |
|---|---|---|---|
| M050 | P043 | W341 | P entry includes eight W forms; no individual-form identity established |
| M346 | P329 | W749 | Provisional source correspondence |
| M355 | P337 | W753 | Provisional source correspondence |
| M362 | P118 | W777, W782 | Same three-M/three-W catalogue group |
| M363 | P118 | W777, W782 | Same three-M/three-W catalogue group |
| M364 | P118 | W777, W782 | Same three-M/three-W catalogue group |

The last three rows do **not** establish six individually identified M–W pairs.
The JSON retains every M and W member in the source entry to make that ambiguity
inspectable. W780 and W781 also have copper associations but no M correspondence
in this catalogue; the index reports them separately instead of silently losing
them. None of these associations establishes an ancient sign meaning.

The separate [hind-leg reading audit](HIND_LEG_HYPOTHESIS.md) examines a published
phonetic proposal for W278/W279. Those codes also lack direct P/M entries in the
pinned catalogue. M084 is a visually plausible family candidate, but the catalogue
formally links it only to W280. The proposal and its eight occurrences are retained
outside the per-M assignments; neither a new alias nor a phonetic value is silently
propagated into this index.

The [capacity follow-up](CAPACITY_MODELS.md) records physical stroke counts on
three photographed vessels and conditional volume fits. It assigns no new M–W
aliases, absolute numeral values or meaning to the accompanying U-shaped sign;
these results therefore remain separate from per-M semantic assignments.
The [new H95 profile trace](H95_PROFILE_CAPACITY.md) supplies a drawing-based
capacity with explicitly uncertain rim counting and separate body marks. It does
not authorize any additional sign-code identity or meaning in this index.

Each link retains both the complete-condition and Good/Fair-only motif labels.
The latter are source condition annotations, not an independent photographic
authentication. Motif labels also remain literal source categories. See
[the copper audit](COPPER_BRIDGES.md) for individual witness objects and limitations.

The [builder](../scripts/build_evidence_index.py) rejects missing or duplicate M
rows in the joined indexes and records hashes of all input files. Tests
check that ambiguous memberships survive the join and unmapped W candidates remain
visible. The underlying [sign atlas](../results/sign_atlas.html) supplies images;
[primary profiles](PRIMARY_INVENTORY.md), [family tests](SIGN_FAMILIES.md), and
[source provenance](SOURCES.md) explain each evidence layer.

The [substitution audit](SUBSTITUTION_NETWORK.md) covers all575 W codes in the
strict subset. Candidate paths reach300 M entries:181 have at least one candidate
with a connection, and119 link only to isolated codes. The remaining117 M entries
have no such observed-W path, while170 W codes lack an M link in this catalogue.
Every conditional link retains full P-entry membership; all sounds and meanings
remain unresolved. Counts of links must not be read as decipherment coverage.

The [recovered M77 candidate corpus](M77_CANDIDATE_CORPUS.md) adds sequence
profiles without requiring a Wells crosswalk. Its strict subset represents332
M signs; the other85 retain explicit zero coverage. These are secondary counts
in `candidate_M77_sequence_profile`, separate from `primary_M77`. Selected
lines have been checked against images, but multiline loss and a large M328
selection effect prevent treating this as an authenticated replacement for the
primary catalogue. No source confidence label or reading is promoted during the
join; the established semantic and phonetic fields remain null for all417 signs.

The [omission audit](M77_OMISSION_BOUNDS.md) supplies an additional per-sign
constraint table for all417 entries. Its positional-loss intervals are conditional
on the export being a subset of the primary occurrences; that assumption is not
upgraded into a verified source identity. Five primary M328-final secondary-line
examples directly demonstrate omissions. Recovered complete objects remain in a
separate line-preserving evidence file rather than being silently pooled with
unreviewed source records.

The [primary U-field comparison](M77_U_FIELDS.md) adds selected, directly checked
relationships among M087, M089, M095 and M328: the same main text can accompany
two, three or four long strokes plus U. This evidence remains separate from the
all-sign join. It establishes a graphic contrast, while amounts, units
and meanings remain unresolved. U's non-stroke and nonfinal contexts are retained
as constraints on any future general interpretation.

The separate [repetition screen](REPETITION_EXPANSION.md) supplies all417 coverage
rows. One nonempty exact frame supports a candidate repeated-sign versus
stroke-plus-sign alternation, but two other replacements occupy that frame.
These comparisons do not assign equal meanings or numerical values and are not
silently joined into the evidence index.

The [complete M328 recovery](M77_U_COMPLETE_RECOVERY.md) now adds a distinct
`primary_reviewed_U_contexts` field to every sign row. It counts752 identified
tokens spanning59 M codes in313 reviewed lines, including primary doubt and
excluding reviewer-unidentified glyphs. These are counts in U-bearing contexts,
not global sign frequencies. M328's323 occurrences and four positional totals
match the primary catalogue exactly. Missing export lines remain in a separate
corpus with side/line keys; no sound or meaning was added to any sign.


The [complete stroke-U counterpart audit](M77_U_COUNTERPARTS.md) adds a separate
primary counterpart-context count to every sign row. Its763 assigned tokens span
121 types. Together with the corrected M328-bearing lines, the deduplicated
combined corpus contains1515 tokens across143 types. These selected contexts do
not assign meanings to those143 signs or cover the other274 signs. The index's
M328-context counts incorporate the later3234 correction M280→M283; the original
stage corpus remains preserved as historical evidence. Source profiles must not
be added blindly if future versions introduce overlapping lines.


The [tool-orientation audit](STROKE_ORIENTATION_RESULTS.md) adds object-level
source comparisons to M104 and M110. Every row has an
`object_specific_orientation_reviews` list; other signs have empty lists. These
reviews preserve knife2928's two orientations and the corrected comparison
of spearhead2926 with a tilted-row description without inventing token order, a numerical unit or new values.


The [C-40 source review](C40_LAYOUT_RESULTS.md) adds `primary_c40_fields` to every
row, nonempty for16codes across two separate eight-token fields. Doubt remains
on the reverse's M129. The three selected codes M312/M313/M314 also receive
`selected_arch_primary_occurrences`, totaling five indexed occurrences. These
are source annotations, not new global frequency counts; they overlap other
reviews and must not be summed as independent attestations. All values remain
unresolved, and M314 is not replaced by three M312 tokens.

The [arch extension](ARCH_MASS_RESULTS.md) adds `arch_extension_primary_fields`
to every row and `arch_extension_selected_occurrences` for the four selected
M315–M318 codes. Fields retain doubt, loss and direction separately; M317's
initial position is catalogue-normalized despite doubtful original direction.
These source annotations overlap existing reviews and are not independent
corpus counts. M315 remains one seven-arch catalogue token. No mass model is
promoted to an established semantic value.

The [composite expansion screen](COMPOSITE_EXPANSION_RESULTS.md) adds
`one_to_two_context_screen` profiles to all417 rows. They count exact one-token
versus adjacent two-token replacements in the selected secondary export, with
strict-candidate sensitivity. A match is not an established graphic ligature or
semantic equation; zeros do not imply lack of meaning. The separately verified
primary witness lines remain source-qualified rather than silently changing the
candidate corpus or its global counts.


The [ending primary validation](ENDING_VALIDATION.md) extends conditional context
links directly to M216, M222 and M254. L-89's checked excavation-number bridge
supports M222 where source feature P230 lists M216 for W555. Direct review links
have `via_P: null`; the original family memberships remain separately visible.
This adds M222 to the linked rows and prevents a conditional catalogue family
from being mistaken for an exact conversion. It does not merge codes or assign
any of the417 signs a semantic or phonetic value.


The [M-63 primary comparison](PINCER_PRIMARY_REVIEW.md) verifies both crossed
forms on a single seal via DK8333, supporting local W550/M216 and W555/M222
correspondences. The same object rules out site/object differences as the sole
source of that graphic contrast, but positional allography and separate sign
identity remain unresolved. New direct review links preserve both M signs;
source P230 membership is not overwritten. The full context screen's55 matches
are candidate pairs, not independently identified artifacts or translations.


The [comb follow-up](COMB_VARIATION_REVIEW.md) authenticates Marshall158=DM50
and its explicit catalogue link to Mahadevan1158. Its impression supports a
reversed comb with the same following sequence as L-89, without the gross
corner loss seen on L-9. This strengthens a candidate orientation variant,
while leaving allography, sound and meaning unresolved. The later [CISI2 review](M934_CISI2_REVIEW.md) independently recovers the
labelled M-934 photographs, but finds a field-number conflict: CISI2 DM56 versus
Marshall DM50. The graphic comparison remains supported; the excavation number
is unresolved. Direct M254 context links preserve these levels of certainty.


The [M-897 sensitivity](PINCER_MAPPING_SENSITIVITY.md) authenticates FEM545=DK9111
and its normalized M77text2545, while leaving the photograph's fine W550/W555
reading unresolved. The local split fits35 of36 candidate-bearing rows; M897
is the exception. All27 candidate-bearing source-complete rows fit, but45 other
source-complete rows have no candidate and even the matched subset includes
known damaged L9. These are retrospective compatibility counts, not global
conversion accuracy. Raw transcriptions and all established values remain unchanged.


The [doubled-grid comparison](DOUBLE_GRID_RESULTS.md) authenticates M81=C3133=
MIC180=M77text1180 through primary catalogue links. One W617 token corresponds
locally to two adjacent M245 tokens, so the same inscription has six Wells units
and seven M77 units. Allowing only this declared span conversion recovers five
previously unmatched pincer rows, representing three distinct strings; repeated
contexts are not new object identities. M245 receives a direct qualified review
link. Neither raw inventory is rewritten, and no ancient word boundary, numeral
or meaning is inferred from the different token counts.


The [W525 investigation](W525_RESULTS.md) authenticates local W525/M254
correspondence on DK8489 (FEM CII15/M77 2868) and Ab473 (EH672/M77 4672).
Both are excluded from the strict extracted corpus because of multiple documents,
so zero strict masked-search matches do not refute the correspondence. Six
separate diagnostic pairs supply only two M77 locators; they are not six independent
anchors. H1123 is excluded because original9015 points to356, not the secondary
record's apparent360. The qualified M254 evidence link preserves these distinctions;
no global allography, semantic or phonetic value is established.


The [three-form context comparison](COMB_FAMILY_CONTEXTS.md) finds no exact
W525/W526 or W525/W527 substitution counterparts in the strict corpus. W525 is
mostly medial on tablets; W526/W527 mostly final on seals. Only one shared
site/type/length stratum exists, with one medial example per side after excluding
the identity-conflicted H1123. The other tokens also differ. Positional graphic
variation remains possible, and the coverage cannot establish a functional or
semantic distinction between forms grouped under M254.


The [tablet follow-up](COMB_TABLET_RESULTS.md) checks the second difference in
the sparse H1817/H843 comparison. Other primary inscriptions support local
W195/M054 (MIC60/C3070/M77 1060) and W554/M226 (EH261/8360/M77 4261).
The actual tablet pair remains unjoined: candidate5326 has the expected three-sign
text and crosshatched reverse but no14307 identity bridge, while H1817's exact
figure was not obtained. The two differing codes cannot simply be merged to
force an allograph comparison. No exact W400-deletion counterparts occur in the
seven distinct adjacent-comb contexts. These results constrain particular
conversions and optional-marker claims without identifying meanings or sounds.


The [catalogue-model audit](CATALOGUE_CONSTRAINT_MODELS.md) formalizes ten
selected local target correspondences. Single-token conversion fails on W617's
two-M245 span, and injectivity also fails where W525/W526/W527 share M254.
An ordered-span model fits these eight distinct mappings but is not globally
validated; uncertain M897 remains a separate conflicting sensitivity case.
Primary editorial-method passages show why normalized tokens should not be
assumed to preserve physical joining or independently validate their own boundaries.

The [new CISI2 recovery](H843_IDENTITY_FOLLOWUP.md) now authenticates H-843 as
excavation14307, Harappa Museum269, and provides its inscription, crosshatched
faces and triangular section. Its explicit M77 5326 join remains unresolved.
The same volume independently verifies the M-735/DK-C3070 alias. The
[H-1817 source search](H1817_IDENTITY_FOLLOWUP.md) remains unresolved; none of
these updates assigns a sound or meaning.


The [M-897 CISI2 follow-up](M897_CISI2_REVIEW.md) closes its DK9111 alias and
recovers the original plus impression. These show a fragmentary object, but do
not establish loss of a particular diagnostic stroke or settle W550/W555. The
raw/model sensitivity remains unchanged. [M-934's new photographs](M934_CISI2_REVIEW.md)
support the comb-orientation comparison while exposing DM56 versus DM50 in the
catalogues. [H-1123](H1123_CISI2_REVIEW.md) lies outside CISI2's stated Harappa
coverage; its 9015/356/360 conflict survives reinspection. These source checks
improve provenance without promoting any of the417 sign meanings or sounds.


The [roof-modifier test](ROOF_MODIFIER_RESULTS.md) fixes six representative
base/roof pairs across five graphic roots. No qualifying cross-root context
rectangle occurs in1,293 strict or2,056 broader complete-field records. The strict
screen has only one shared frame, with both plain forms and unknown site labels.
An independent exact calculation proves three proposed shuffle diagnostics have
constant scores despite many movable masks elsewhere. This is sparse evidence,
not rejection of a common modifier. M092's sole primary occurrence has loss;
its absence from complete fields is a coverage limit. No roof meaning, standalone
M134 decomposition, or semantic/phonetic value is assigned.


The [roof variant and artifact follow-up](ROOF_VARIANT_ARTIFACT_RESULTS.md) checks
15 Appendix drawings across six targeted rows. Broad roof status is retained in
these drawings, but fish side marks, trident prongs and basal geometry vary.
Original photographs authenticate K-29/M77 8018's roofed strokes and EH407/4407's
roofed cross. K-29 has substantial field loss; EH407's notches are intentional.
The original photo of5444/3027(2) remains unjoined: the catalogue suffix explicitly
disambiguates objects, so EH558/3027 cannot be substituted. These findings do not
supply a complete cross-root rectangle or a common roof meaning. All417 semantic
and phonetic values remain undetermined.


The [roof prediction support audit](ROOF_TRANSFER_SUPPORT_RESULTS.md) groups
references and full formulas before matching opposite states and withholding a
graphic root. Only fish passes with known secondary labels; allowing unknown
labels also admits trident. No fold has the declared three-root support, so no
classifier is fitted. An independent graph/occurrence reconstruction checks the
finite result. Original EH493 and H-889 photographs now have exact source joins;
fine fish-side details remain qualified, and8650b is a shared find group rather
than a unique artifact. No meaning or sound is assigned.
