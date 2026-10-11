# Relation-marker placement: all-sign extension

Allowing M001 to stand at the end of a text still produces no exact chain in the
filtered domestic candidate corpus. The 36 eligible final-marker strings admit
131 alternative cuts into two bundles; none supplies a matching right-to-left
bundle across two different strings. This does not rule out a kinship use: related
people need not both appear in this sample, and these literal templates exclude
many possible spelling and grammatical constructions.

This extends the [internal-marker audit](PATRONYMIC_TEST_DESIGN.md), motivated by
its observation that M001 is usually final in the selected seal texts. It is an
exploratory test, not an accepted reading of M001. The source proposal concerns
human-like signs and variants; only the plain M001 identity has been matched here.
No variants are merged. All 417 individual codes receive the same three-template
screen as descriptive controls.

## Observations

The corpus selection is unchanged: 1,175 eligible seal records, collapsed to
1,066 complete candidate strings. These are secondary transcriptions with selected
primary checks, not an independently reread complete archaeological corpus.

| M001 placement | Form | Eligible strings | Alternative parses | Distinct ordered chain pairs |
|---|---|---:|---:|---:|
| Prefix | D A B | 0 | 0 | 0 |
| Internal | A D B | 5 | 5 | 0 |
| Suffix | A B D | 36 | 131 | 0 |

M77 reference 1288, candidate `M028 M001`, accounts for the remaining one of the
earlier 37 final-marker strings: its body cannot split into two nonempty bundles.
All 36 eligible suffix strings have more than one possible boundary. Their full
tokens, references and every cut are retained in the result's
`target_M001_eligible_parses` field. None of those cuts is authenticated as a word
boundary. The five internal splits reproduce the earlier result.

| Template, all 417 codes | Codes with eligible strings | Codes with matches | Parse matches | Distinct ordered string pairs, summed over codes |
|---|---:|---:|---:|---:|
| Prefix | 186 | 16 | 130 | 129 |
| Internal | 229 | 6 | 10 | 10 |
| Suffix | 99 | 13 | 1,002 | 1,002 |

These totals have unequal opportunities and dependent hypotheses. They are not
p-values or semantic confidence scores. For example, M342 supplies 894 of the
suffix pairs, but also 393 eligible strings and 1,395 alternative parses. Ranking
those raw counts would conflate frequency, position and boundary opportunities.
No control marker is assigned a kinship meaning.

## Method and proof limits

Every string must contain exactly one tested marker and at least two other
signs. An internal marker fixes the two entire flanks. A prefix or suffix marker
permits every cut of the remaining contiguous body into two nonempty bundles.
The entire right bundle must equal the entire left bundle of a different full
string with the same marker and template. Duplicate full strings share reference
lists and cannot match themselves through alternative cuts. Mixed placement,
multisign markers, omitted signs, variants and approximate matches are excluded.

For terminal templates, this is precisely a proper suffix–prefix overlap of the
two bodies. Multiple overlap lengths can make one ordered pair match repeatedly;
the output reports both counts. A single segmentation of the whole corpus is
not chosen. Two pairwise matches can require contradictory boundaries in their
shared middle inscription, so combining them into an apparent multigeneration
family would be unjustified.

The [three-string extension](CONSISTENT_CHAIN_RESULTS.md) now quantifies that
problem:1,152 of1,483 composed paths have no consistent middle split. The331
survivors remain structural candidates, with one multi-sign example checked
against the primary catalogue; no kinship or reading is established.

The [independent method review](TERMINAL_RELATION_METHOD_REVIEW.md) proves the
overlap equivalence, reversal symmetry and corrected marginal formula. Reversing
every inscription exchanges prefix/suffix templates and reverses the chain order
without changing counts. These statistics therefore do not infer reading or
descent direction. A simple non-kinship two-field classification system produces
`q^3 - q` exact distinct-string chains over q field labels, demonstrating that
even forced boundaries and many matches do not identify genealogies.

## Reproduction

Run `python3 scripts/audit_relation_templates.py` after the candidate corpus and
internal-marker audit have been generated, or use `python3 scripts/run_all.py`.
The script is integrated immediately after the internal-marker audit and saves
all 1,251 code/template rows, witnesses, target parses and input fingerprints in
[relation_template_audit.json](../results/relation_template_audit.json).

Six tests in [test_relation_templates.py](../tests/test_relation_templates.py)
guard full-bundle matching, same-string exclusion, repeated markers, minimum
length, reversal, distinct pair counting and agreement with an independently
specified suffix–prefix overlap oracle over all binary bodies of length two
through four. All six passed. Independent code review found no defect in the
invoked per-marker/per-template workflow. No downloaded source or corpus
transcription was changed for this extension. All sign meanings remain unknown.
