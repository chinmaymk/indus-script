# Independent Chanhudaro metadata-join review

The declared frame contains **65 illustrated catalogue entries: LI.1–33 and LII.1–32**. Original printed pp.292–293 visibly delimit these sections; material above LI and below LII belongs to other plate sections. Completeness here means the declared illustrated frame, not all excavated seal objects.

`scripts/verify_chanhu_deposit_joins.py` reconstructs the joins independently from the primary register and metadata columns of the raw CSV, without importing the producer or its helpers. It compares every complete output row, candidate list, selected object, provenance discrepancy and summary field. It checks input hashes and prohibits reuse of a selected secondary object. No inscription strings, symbols, family outcomes or translations are inspected.

The current reconstruction agrees: **55 unique number+suffix+plate+seal-class matches, seven entries with no metadata candidate, two plate/number conflicts and one secondary-class conflict**. The secondary frame contains 72 grouped objects in 74 rows. Five matched primary rows have seven recorded square/locus/elevation disagreements. Every secondary phase field is unspecified. All 65 primary rows remain present, including the ten without an accepted match.

## Independent original-image checks

| Primary entry | Visually verified original | Secondary conflict and handling |
|---|---|---|
| LI.12 | CH3493, level +7.0 ft | +7.2 ft in secondary row81.1; match retained with explicit elevation disagreement |
| LI.31 | CH1293, level +14.9 ft | +14.1 ft in row59.1; explicit elevation disagreement |
| LI.26 | CH3043, level +7.3 ft | Row83.1 instead says CH3817; plate-only candidate rejected. The original preceding LI.25 is CH3817. |
| LII.15 | CH2531, level +9.6 ft | Row63.1 says CH2431; plate-only candidate rejected |
| LI.4 | CH518, level +0.8 ft, under the seal-amulet heading | Row115.1 matches number and plate but is labelled MISC; retained as an explicit class conflict with no automatic type conversion |

The row12 and row31 readings are clear on enlarged native crops. The row26 distinction is particularly important: a bare-number join to CH3817 would conflate different plate entries. The producer's exact plate requirement prevents that. Alphabetic suffixes remain part of the identity key, including 3485a versus 3485b, 2594h and 2529cc; differently suffixed records are not pooled.

## Logic and limits

I found no silent false join or count loss under the stated rules in the current files. Every accepted object's grouped rows must agree on number/suffix, plate/item and seal-class eligibility. Number-only, plate-only and wrong-class candidates remain diagnostic alternatives; they are not promoted to identity.

This conservative metadata result does not prove that the primary catalogue's printed numbers are historically error-free, or that the secondary transcription represents the authenticated object's surviving field. LI.4's primary section heading supplies a reason to review its secondary MISC classification later, but overriding that class would require an explicit new layer. The present rejection is faithful to the frozen eligibility rule.

The provenance-disagreement list checks only mutually known square, locus and elevation values. An empty list does not certify missing values, trench, mound, cutting, phase or depositional episode. The current register has a locus for every entry; the producer's conversion of a future null locus to the literal string “None” would need attention if that invariant changes. It does not affect this run.

The machine report `results/chanhu_deposit_join_independent.json` pins the exact register, producer output, script and original images reviewed, and stores the targeted source checks and crops. Those hashes define this review even if a later register revision occurs. This is a computational and selected-source verification, not a second visual transcription of all 65 rows. No semantic or phonetic values were assigned; all 417 values remain null.

The first verification detected a stale producer snapshot after the register reviewer added three explanatory note arrays. No join decision, source reading, discrepancy or count changed. The attempt is retained in `data/processed/chanhu_deposit_join_verification_attempts.json`. After the parent refreshed the producer output against the final register, the full independent verification passed with zero mismatches.
