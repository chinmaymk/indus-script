# Glossa manuscript and validation review

The reviewed release supplies proposed Dravidian readings, but does not establish an independently verified phonetic anchor or successful external reading prediction. Its assignment counts, internal fit and agreement with earlier conjectures must not be presented as decipherment accuracy. Static inspection also finds material defects in the advertised validation tests.

This bounded review concerns commit `40812fc54470d5508b47af5fabcea7ccf044036c`. No downloaded code was executed and no new data were downloaded. Exact input URLs, byte counts, SHA-256 hashes, findings and source locators are preserved in [the machine-readable review](../data/processed/glossa_methodology_review.json). Sources remain in `data/raw/`. The private Holdat corpus prevents an exact historical rerun here.

## Coexisting versions are different claims

| Pinned manuscript | Its claimed scope | Necessary qualification |
|---|---|---|
| `glossa_preprint_v4.pdf`, May 2026 revised June 2026 | 161 HIGH+MEDIUM assignments; 90.96% token coverage | Explicitly assignment coverage, not verified phonetic transcription |
| `glossa_preprint_current.md`, header calls itself v3 | 605 readings; 100% coverage; 413 described as independently confirmed and 192 inferred | Also calls all 605 HIGH; expanded assignments rely on ICIT and cognate-based promotion |
| `glossa_preprint_v3.md`, audited narrative | 400 HIGH readings, 185 Holdat-attested; 92.8% coverage | Retracts 605/100% and grammar conformance; explicitly acknowledges anchor circularity |

These artifacts coexist at one commit. Filenames do not identify a single latest scientific result. The [audit corrections](../data/raw/glossa_AUDIT_CORRECTIONS.json) acknowledge mass assignment of `kur` and then `kol` to 205 signs. The reported 91.8% grammar result was retracted because shuffled readings obtained 94.2%. This candid correction is valuable; it does not validate the remaining tests.

The saved release report describes a 400-HIGH state, whereas the pinned backend file contains 166 HIGH entries with readings. The audit and release report also disagree on Holdat-attested counts (208 versus 185) and Parpola agreement (50% versus 80%). Revision or postprocessing may explain these differences, but the states cannot be pooled. Several saved summary fields are not emitted by the pinned script's `anchor_summary()` function. Parent's separate key audit covers exact accounting.

## Material static findings

The relevant [validation script](../data/raw/glossa_release_validation.py) was read, not run.

1. **The advertised language baseline is invalid.** Lines 62–88 extract the first case-preserved character of each proposed reading and count whether each adjacent pair exists as a language-model key. The calculated probabilities are unused. The uniform comparison contains uppercase ASCII A–Z pairs; the reviewed current HIGH readings have no uppercase ASCII initials. Its zero support therefore reflects an alphabet mismatch. Even a case-matched uniform model with full support would yield 100% under this membership score: it is not a likelihood comparison. The historical 400-HIGH state is not reconstructed here. The header promises five-way discrimination, but this function compares only Dravidian and uniform.

2. **Inscription boundaries are crossed.** `test1` scores `flat_tokens`, which concatenates objects without separators (lines 39–50, 56, 82–91). Assigned final and initial signs on unrelated objects become scored bigrams. The M77 function likewise scores a flat returned stream; its helper's boundary treatment was not inspected, so the same defect there remains conditional.

3. **The reported conditional entropy uses the wrong marginal.** Lines 211–227 delete unassigned readings, creating artificial adjacency across gaps, then calculate joint bigram entropy minus entropy of all retained tokens. Correct `H(Y|X)` subtracts the entropy of the first endpoints of the very same bigram sample. For two copies of `[a,b]`, the only bigram is `(a,b)`: joint entropy is 0, all-token entropy is 1, and the script's formula gives **−1 bit**, whereas the correct conditional entropy is **0**. This proves a formula error without executing the source or accessing Holdat. The magnitude and direction of the historical score error are not calculated here. Full slash-separated reading strings are also categorical labels, not resolved phonological transcripts.

4. **Phonological coverage is hardcoded.** Lines 259–273 fix six missing initials and return `(25−6)/25 = 76%`, regardless of the observed initial inventory. The report simultaneously says `attested=25`, lists six missing and concludes 19/25. This is not a computed coverage test against a specified phoneme inventory.

5. **Prior agreement is not correctness.** The Parpola comparison uses a hardcoded 20-entry key, checks any slash alternative after diacritic removal, and accepts three-character partial matches. It lacks per-entry primary-source mappings and is not independent where Parpola proposals already informed assignments. Although described as HIGH-only, it accesses all anchor entries. The uniqueness statistic is the fraction of inscriptions whose complete sign sequence occurs once; it supplies no phonetic ground truth.

## What is, and is not, held out

The current manuscript says ICIT was tested blind with readings established solely from Holdat (line 214), but describes ICIT integration and promotion of new signs (lines 96, 223, 374). It says Elamite cognates were unused in derivation (line 260), yet describes cognate injection during promotion (line 96). A frozen, dated sign-level partition would be needed to resolve those dependencies. Two exports also need an artifact-overlap audit before being called independent corpora.

The same manuscript acknowledges that its 83.7% consistency comes from anchored simulated annealing and that unconstrained optimization did not discriminate language families (line 400). Compatibility of Dravidian-derived assignments with a Dravidian model does not independently identify their language. Tamil-Brahmi name resemblance likewise needs a documented separation from lexicon/model construction. Agreement with or disagreement from another proposed decipherment is not validation or falsification of a language absent a correct reference key.

The v4 PDF contains a more directly grounded external test: §§3.26 and 3.28 compare proposed readings with attested Meluhhan personal names. **It reports no strong match for six names and no discriminative match for the expanded 25-name test.** Broad fuzzy matches arose from common short readings. These are negative results, not successful name decipherments. No successful prospective prediction with independently known reading was identified in this bounded set.

## Sign identities and remaining limits

Both v4 and the current Markdown retain M047 as fish/P47, M059 as seven strokes, M099 as vessel/jar and M328 as man. M012 was not found in the three manuscript texts; absence does not establish correction. Parent's [primary glyph review](../data/processed/glossa_sign_identity_review.json) checks these claims against catalogue imagery and records conflicts. This review does not duplicate that visual work. A wrong pictorial identification undermines its proposed iconographic basis, without logically disproving every possible conventional sound assignment to the glyph.

The conclusion is limited: the reviewed evidence cannot establish the proposed key, and several cited metrics need correction before interpretation. It is not a proof that the underlying language was non-Dravidian or that every proposed reading is false. No exhaustive review of every dictionary, cognate or repository phase was performed.
