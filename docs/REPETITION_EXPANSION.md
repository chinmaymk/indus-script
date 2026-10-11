# Repeated signs versus stroke-plus-sign constructions

**One primary-checked pair fits this pattern inside an otherwise identical inscription. The same context also admits other replacements, so semantic equivalence is not established.** This constrains a partial numerical hypothesis without supplying a deciphered sign.

Parpola proposes that triple U can be an alternative to three strokes followed by U, interpreting the strokes as a numeral attribute. That motivates the broader formal comparison `prefix A…A suffix` versus `prefix stroke(n) A suffix`, where A repeats n times. We test the opposite marker order and every other possible replacement sign too. The author's U interpretation remains a hypothesis. [Parpola2008, printed116](https://www.harappa.com/sites/default/files/pdf/indus-writing.pdf); a [bounded web extraction](../data/raw/parpola_2008_repetition_web_capture.json) is retained because direct PDF download returned403.

## Primary fish-shaped comparison

Four complete, undoubted lines share prefix **M267 M099** and suffix **M211**:

| Reference | Intervening pair | Graphic observation | Primary page |
|---|---|---|---|
|4232|M059 M059|Two plain fish-shaped signs|Printed103 / PDF114|
|1551|M087 M059|Two long strokes, then plain fish|Printed55 / PDF66|
|1019|M104 M059|Four short strokes, then plain fish|Printed39 / PDF50|
|2523|M065 M059|Modified fish, then plain fish|Printed74 / PDF85|

Normalized sequences and metadata were visually checked in [PDF114](../results/primary_pages/repetition-pilot-114.png), [PDF66](../results/primary_pages/repetition-pilot-66.png), [PDF50](../results/primary_pages/repetition-pilot-50.png), and [PDF85](../results/primary_pages/repetition-pilot-85.png). All four are coded as seals with one line and original RTL direction. Reference4232 is under Harappa with field-symbol03;1551 is under Mohenjodaro with field-symbol35. The other two have field-symbol01. Archaeological contexts and motifs are therefore not demonstrated equivalent.

The4232/1551 pair is compatible with replacing two copies of a sign by a two-stroke marker plus that sign. Ordinary substitution within a grammatical or classificatory position also permits different meanings. The1019 and2523 alternatives make this ambiguity explicit. **Do not equate two long strokes with four short strokes merely because both occur here**, or infer that M059 literally means fish from its shape.

## Systematic screen

Native M codes are used without a Wells crosswalk. Whole rows containing doubt or loss are excluded; damage is never removed to join surviving tokens. A maximal four-sign run is counted once, not as three overlapping pairs.

| Subset | Records / distinct strings | Repeated-sign runs | Any replacement matches | Graphic-count matches | Matches with outside context |
|---|---:|---:|---:|---:|---:|
|Complete, undoubted exported strings|2,056 /1,520|102 across27 target signs|29|4|1|
|Strict candidate subset|1,293 /1,141|75 across23 target signs|3|1|1|

Tested run lengths are2–4. Graphic candidates remain distinct: long M087/M089/M095 for two/three/four; short M099 and M100 for two, M102 for three, M104 for four. M099/M100 differ in placement and are not merged. These are graphic multiplicities, not assigned values. Both marker orders were searched; all four selected matches put the marker before the target in normalized order.

The other three matches have **empty surrounding contexts**: three M162 versus M102 M162; four M162 versus M104 M162; and two M104 versus M100 M104. The last comparison involves stroke groups on both sides of the proposed rewrite.

Repeated M162 strings appear on2949 and2950, [printed86 / PDF97](../results/primary_pages/repetition-rods-97.png). The primary metadata identifies ivory/bone rods, symmetric arrangement, and additional symbol-only sides. Stroke-plus-M162 counterparts are secondary-corpus candidates on other object types; no archaeological equivalence was authenticated. Both repeated-rod cases disappear under strict filtering. Empty frames supply little contextual specificity, and these matches establish neither multiplication nor units.

All417 codes have coverage rows in the [results](../results/repetition_expansion_audit.json), including zero observed runs and null meanings. Zeros concern the selected export. Triple-U lines occur in the separate primary pilot but are omitted from the one-sequence export here; their remaining unidentified surrounding glyphs are not guessed. This screen therefore does not test or refute every proposed U equivalence.

## Interpretation and limits

The exact fish pair is a lead for a compositional notation involving repetition and stroke groups. It remains an ordinary shared-context substitution until an external constraint establishes equivalence. No sound, word, value or language follows from it.

The matched U tablets give complementary evidence: one main text accompanies several auxiliary stroke counts. The [external-anchor review](M77_U_EXTERNAL_ANCHORS.md) found no independently represented amount in its examined sources. The [alternative-model review](M77_U_ALTERNATIVES.md) shows that collapsing repeated identical pairs preserves the two/three/four variation. Production categories, dates and conditioned variants still need independently measured context. These constraints can coexist in a structured-label hypothesis without selecting a unique semantic interpretation.

## Correction and reproduction

This audit caught a prose error: **M104 has four short strokes, not five long strokes.** The U-pilot generator, review and generated ledger were corrected. No pilot row contained M104; the141-group U analysis and matched-tablet findings are unchanged. Four-long M095 remains distinct.

Run `python3 scripts/audit_repetition_expansion.py` or `python3 scripts/run_all.py`. The [script](../scripts/audit_repetition_expansion.py), [five validity tests](../tests/test_repetition_expansion.py), and [primary ledger](../data/processed/m77_repetition_primary_review.json) preserve rules, all replacements, exclusions, six checked lines and source hashes. Tests cover boundaries, maximal runs, exact contexts, alternatives, order and duplicate-string handling. They validate computation, not ancient semantic equality.
