# What the evidence now constrains, and what would change the conclusion

27 September 2026. This is a bounded synthesis of the saved research, not a new corpus analysis or a review of proposed translations. **The best-supported account is a structured system with conventional positions, recurring local combinations, variable auxiliary fields and graphic contrasts that modern catalogues normalize differently.** That account applies to the available evidence without pretending that it assigns a function to every sign. It does not yet identify language, phonetic values, referents, word boundaries or a common meaning for modifiers.

The decisive gap is not simply the absence of a bilingual. Most positive results constrain **which signs occur together**, whereas the competing readings differ in **what those combinations refer to**. A useful next test must make a prediction about an independently measured attribute or archaeological context that was not used to select its sign examples. More repetitions of the existing entropies, matching strings or selected photographs cannot bridge that gap.

## Coverage of the whole 417-sign inventory

The current [evidence index](../results/sign_evidence_417.json) has exactly one row for each M001–M417; every semantic and phonetic field is null. The [primary findings](../results/primary_inventory_findings.json) cover **13,372 tabulated occurrences**, without requiring a Wells crosswalk. However, **264 signs have fewer than ten primary occurrences and 112 occur once**. The 67 most frequent signs account for 10,769 occurrences. An all-sign key would therefore require a way to constrain the large rare tail beyond fitting familiar formulae.

Different evidence layers have different coverage and cannot be added as independent attestations:

| Layer | Current finite coverage | What it supplies |
|---|---:|---|
| Primary Table I | 417 signs | Global frequency and position constraints in that historical catalogue |
| Strict candidate native-M sequences | 332 observed signs; 85 unobserved | Conditional sequence evidence, with documented omitted lines |
| Candidate W-substitution paths | 300 M rows linked; 181 with at least one connected W candidate | Mapping-qualified contexts, not 181 individually authenticated allographs |
| Supported candidate graphic families | 20 source families; paths to 31 M rows | Limited variant prediction; not 31 proven mergers or distinctions |
| Corrected U-field plus counterpart recovery | 1,515 assigned tokens across 143 types | Selected, reviewed line/side contexts; not representative coverage of all types |

The [family audit](../results/sign_family_audit.json), [counterpart audit](../results/m77_u_counterparts.json) and index preserve the relevant denominators. The original U recovery has 59 identified context types; the index's later corrected context layer currently reports 60. These are versioned evidence layers, not counts to combine. Likewise, 112 primary M hapaxes must not be confused with the report's 214 deduplicated secondary W hapaxes.

## Strongest positive constraints

**Order is informative beyond position alone.** In the strict deduplicated W sample, adjacent mutual information is 3.196 bits versus a 2.114-bit mean under the declared length-and-position-preserving null; none of 499 draws reaches it. More substantively, the grouped held-out bigram loss is **5.934 bits/sign**, compared with **6.792** for position and **7.085** for frequency. Exact duplicate strings and connected artifact records stay together. Cross-site checks retain an advantage. This constrains a successful model of the notation, while the weather-icon controls show that the result does not identify spoken-language writing. [Permutation results](../results/permutation_tests.json), [prediction results](../results/predictive_tests.json), [model limits](STRUCTURE_THEORY.md).

**Some graphic contrasts have real distributional consequences.** Primary M342/M343 final-position differences cannot be explained solely by different site mixtures with shared empirical within-site rates; the Mohenjodaro contrast is at least **39.70 percentage points**. Related marginal bounds hold for selected fish and stroke contrasts. This is stronger than visual resemblance alone and requires no guessed joint table. It does not rule out position-conditioned allography, chronology, joint site/type confounding or modifiers. [Exact bounds](CONTEXT_BOUNDS.md), [saved audit](../results/primary_context_audit.json).

**The stroke-plus-U field can vary while a main text stays fixed.** The primary recovery accounts for all **323 M328 occurrences on 313 lines** and reproduces the four printed positional totals. Twelve exact counterpart groups retain variable stroke counts with object class and side/line layout held fixed; four span two, three and four strokes. Literal copying alone cannot remove this variation. A variable quantity field is a useful hypothesis, but a separately varying categorical field also fits. The physically identified selected tablets differ in shape, dimensions and find contexts, so these are not experimentally controlled transactions. [Recovery](../results/m77_u_recovery_audit.json), [counterparts](../results/m77_u_counterparts.json), [alternative models](M77_U_ALTERNATIVES.md).

**One modern token is not invariably one ancient graphic unit.** M81 locally has W617 corresponding to two M245 tokens; reviewed W525/W526/W527 contexts share M254; M63 carries both locally differentiated crossed forms. A future reading must account for these distinctions and normalizations rather than inherit a one-to-one conversion. These are concrete constraints on representation, not established ligatures, synonymy or phonetic equivalence. [Catalogue constraint models](CATALOGUE_CONSTRAINT_MODELS.md), [finite audit](../results/catalogue_constraint_audit.json).

**External contexts are informative but currently nonunique.** Storage/closure impressions, selected craft associations and the three-pot capacity fit make administrative or quantity-related uses worth testing. None selects a unique word. The strongest capacity fit uses three selected pots and about **40–42 litres per stroke** across geometry choices; the same unit fails to transfer to other published vessel rows. A physical dimension is an independent measurement, but the claim that it is the inscription's represented quantity is still an assumption. [Capacity audit](../results/capacity_model_audit.json), [Chanhudaro context audit](CHANHU_FISH_CONTEXT_AUDIT.md).

## Contradiction is narrower than failure to decipher

| Hypothesis or inference | Present status and exact scope |
|---|---|
| Every complete M342-bearing line ends with M342 | Contradicted in primary Table I: 1 initial and 420 medial occurrences. Three solus occurrences are not counterexamples. |
| M328 is universally terminal | Contradicted by the complete concordance: 19 initial, 29 medial, 274 final and 1 solus occurrence. A frequent auxiliary-field role survives. |
| Different site mixtures alone reproduce the selected primary position contrasts | Incompatible with the empirical marginal totals under the declared shared-rate model. This is not a claim that equal population probabilities are mathematically impossible. |
| Every contiguous tally-like run is one field with one global graphic-class order | Contradicted in the literal screen: the best of six orders fails 26/186 runs; selected primary examples retain reversed class order. Multiple fields or additive unordered notation survive. |
| Exact tablet length equals `(stroke count+3)/16` inch | Refuted by the frozen EH405/4405 check: predicted 3/8 inch versus 0.6 in the table and 5/8 in the linked narrative. This is not a refutation of quantity notation. |
| M106 has one fixed nonnegative additive *mass contribution* equal to K-122's whole surviving 476g, also within the chisel's surviving total | Inconsistent with the 165.343g chisel. A proposed 2.6-times original-mass cap also fails. Different units, referents or unconstrained lost mass change the premises; the number five itself is not disproved. |
| One-token W→M conversion represents all reviewed local correspondences | Contradicted by the authenticated two-token W617 span; injectivity additionally fails on the comb forms. This concerns editorial coding, not the language. |
| Significant sequence structure proves language, or a fully relabelled key identifies ancient meanings | The inference fails: weather icons supply a concrete structure control, and bijective relabelling preserves the declared internal scores exactly. |

Sources: [primary findings](../results/primary_inventory_findings.json), [U recovery](../results/m77_u_recovery_audit.json), [parallel-theory results](PARALLEL_THEORIES.md), [length holdout](M77_U_LENGTH_HOLDOUT.md), [mass proof](TOOL_SIGN_MASS_RESULTS.md), [catalogue audit](../results/catalogue_constraint_audit.json), [identifiability proof](IDENTIFIABILITY.md).

The following instead remain **unidentified or underpowered**, not contradicted:

- A numeral/quantity interpretation in specified contexts. Conditional numeral equations retain two screened integer solutions, **(10,8,6)** and **(36,20,4)**, and arithmetic notation does not authenticate the hypothesized equality between fields. [Exact equation audit](../results/numeral_equation_audit.json).
- A productive roof modifier. The fixed cross-root screen finds zero rectangles, but the follow-up support audit has **zero usable held-out-root folds**. Missing counterfactual contexts prevent the test; zero rectangles are not evidence that the modifier has no function. Extra shuffles cannot create coverage. [Roof audit](../results/roof_modifier_audit.json), [independent range proof](../results/roof_modifier_independent.json), [support audit](../results/roof_transfer_support.json).
- Position-conditioned allography versus distinct sign identity. Neighbor prediction adds only 0.0217 bits/token over the family metadata baseline, is weighting-sensitive and divides the twenty supported families evenly between gains and losses. Predictable contexts can occur under either explanation. [Family results](SIGN_FAMILIES.md).
- Long-range dependency, personal names, kinship, commodity names, a particular language or a rebus reading. Absence of a successful alignment or a strong first-sign residual is not evidence of absence. Conversely, exact chains and shared frames do not establish segmentation, kinship or semantic equivalence. [Structure calibration](STRUCTURE_THEORY.md), [current synthesis](REPORT.md).

The unrestricted statements “this sign denotes some category” or “every failure uses another unit” can accommodate almost anything. They are not positively supported merely because they have not been contradicted. A research hypothesis needs a finite rule for when its category, unit or operation applies.

## Two discriminating next tests

These are designs, not executed results or claims that adequate new samples already exist. Previously inspected objects must remain marked discovery data.

### 1. A prospective within-class capacity prediction

**Question:** within a declared vessel class, do independently counted rim strokes predict independently reconstructed usable capacity beyond vessel class, phase and manufacturing batch?

Freeze a finite inventory of all inscribed storage-vessel profiles in one excavation report or museum collection, selected from its artifact register **without inspecting the strokes**. Include damaged/unscaled cases as excluded or uncertain records, rather than silently dropping poor fits. An image reviewer, masked to counts, traces internal profiles and independently calibrated scale; a second reviewer, masked to dimensions, counts strokes with uncertainty and records placement. Match or stratify vessel class, site/phase and sign placement before inspecting volume/count association. Do not mix the already incompatible general vessel pool and fit a rescue unit after seeing it.

Prespecify two comparisons: the existing **40–42 L/stroke** range as an out-of-sample transfer prediction for a genuinely matched class; and a within-class one-parameter proportional model fitted only to training production groups, compared with a class-only capacity baseline on held-out groups. Freeze the physical reconstruction/error rule before counting. Report every prediction interval and residual; require the rank/ratio relation to survive alternative plausible counts and scales. If independent batches cannot be established, report that support failure instead of an independence-based p-value.

Successful proportional prediction on new groups would constrain a specific quantity-like use, while still leaving container capacity versus actual contents unresolved. Reliable within-class rank reversals or systematic held-out failure would contradict the fixed proportional-capacity rule. An arbitrary category model does not predict either outcome without additional assumptions. This goes beyond the existing selected three-pot fit and the failed tablet-length rule; it is not another fit to H-370/H-371/H-372. [Existing capacity evidence](CAPACITY_MODELS.md), [scale-independent follow-up](H95_PROFILE_CAPACITY.md).

### 2. A deposit-level test of the proposed fish/craft association

**Question:** does the frozen graphic fish-family indicator predict independently documented bead production, rather than just one selected square or a generally artifact-rich context?

Use the finite Chanhudaro excavation register as the development frame. Before inspecting sign strings, classify **room/locus plus elevation/phase**, not whole grid squares, from drill waste, unfinished beads, blanks and documented working surfaces. Distinguish positive, demonstrably comparable negative, and unknown contexts; absence from a narrative is not a negative. Record shellworking, metalworking and deposit richness as rival explanatory variables. All seal finds in eligible deposits enter the inventory, including fragments whose text is unknown. Freeze the already declared P050/P051/P056–P064 family indicator and plain-W220 sensitivity; do not add forms because they improve the result.

Estimate the association within matched phase/deposit classes, with exact inscription, artifact and verified die/mold duplicates grouped; whole deposits are the sampling units. Keep already reviewed 9/D and 8/E as discovery examples. Predict a second independently classified deposit set or excavation sector before unmasking its signs. Report identified-set bounds placing unreadable inscriptions on either side, and do not call a result decisive if those bounds reverse it. Compare bead-specific prediction against the same procedure for shell/metal production and non-fish signs matched on frequency; the latter controls generic workshop concentration.

A reproducible bead-specific held-out association would support a restricted activity/domain relationship and narrow future meanings. Failure would reject the frozen enrichment prediction, while not disproving all occupational uses. Neither outcome alone would translate fish as “gemstone,” distinguish worker from institution, or establish a homophone. If no defensible negative deposits or held-out set exist, the outcome is **test unavailable**, not confirmation by proximity. This addresses the actual weakness of the existing 9/D comparison rather than repeating its square-level count. [Current finite ledger](../results/chanhu_fish_audit.json), [archaeological review](CHANHU_FISH_CONTEXT_AUDIT.md).

Both tests add an external prediction. Broad relabelling, another flexible segmentation search or more roof-state classifier runs on the current empty support design would not. The preserved sign distinctions and all 417 unresolved values remain unchanged.

## Snapshot and reproducibility

The companion `data/processed/decipherment_evidence_gap_review.json` records the reviewed file hashes, exact inventory checks and the two proposed tests. `scripts/pin_decipherment_evidence_gap_review.py` verifies the 417 unique IDs, null values and primary totals and refreshes that snapshot explicitly. This review introduces no downloads, no new ancient readings and no changes to central reports, corpora or counts. File hashes establish what was reviewed; they do not independently authenticate every underlying archaeological interpretation.
