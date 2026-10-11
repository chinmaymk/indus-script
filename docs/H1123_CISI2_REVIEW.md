# H-1123: bounded CISI2 follow-up

Date: 2026-09-27. **The recovered CISI2 cannot supply an H-1123 entry: that identifier is outside the volume's stated and observed Harappa coverage.** The earlier conflict between excavation number9015 and plate items356/360 remains unresolved. No correction, artifact identity, sign correspondence, or semantic value is promoted.

## What the recovered volume actually contains

The retained original scan is `data/raw/h843_identity_CorpusVol2.pdf`, the authenticated1991 *Corpus of Indus Seals and Inscriptions, 2. Collections in Pakistan*. Its contents at printedIII/PDF6 explicitly list Harappa identifiers H-266–275, H-356*, and H-383–1019, on printed253–351.

Two independently inspected endpoints agree with that declared coverage:

| Original page | Observation |
|---|---|
| Printed351/PDF386 | Final Harappa photographic page is labelled H-1018–1019. |
| Printed445/PDF480 | Basic-data table ends the Harappa sequence at H-1019 and then begins Rahman-dheri. |
| Printed447/PDF482 | Corrigenda address other page/figure issues; no H-1123,9015,XCIV356 orXCIV360 correction is supplied there. |

This is positive evidence of the catalogue range, stronger than the negative OCR search alone. It does not prove that no object now called H-1123 was ever photographed under a different alias. No such alias bridge was found or assumed in this bounded inspection. The separate CISI identifier H-356* must not be confused with Vats plate XCIV item356.

## The earlier conflict survives reinspection

The original Vats printed33/Archive leaf59, VIth-stratum item4, was inspected again from the retained full page and its crop. It pairs excavation9015 with plate XCIV item356, J9/3 and depth13feet, describing four pictograms on one side and three on the other. The printed356 is legible; the conflict is not merely a machine OCR substitution.

The retained XCIV plate, PDF196 of the Vats plate volume, separately labels356 and360. Their two-face photographs visibly differ. Item360 has a three-group face and a second face with a U-shaped group and two vertical strokes. Item356 has different, more crowded text on both faces. This independently confirms that one cannot silently treat the plate numbers as interchangeable.

The secondary H-1123 rows313.1/313.2 retain raw identifier `9015360` and texts `+525-550-220+` / `+700-032+`. The resemblance of item360 to that secondary pattern is a locator, not a primary excavation-number join. Earlier Mahadevan4360 evidence belongs to the EH360 branch; no equality between Finnish and Mahadevan reference numbers is used here. Whether Vats's9015/356 statement contains a misprint, whether a later catalogue corrects it, or whether the secondary field/plate concatenation is wrong still requires a specific primary bridge or explicit correction.

## Research log and reproduction

1. Read `W525_PRIMARY_REVIEW.md` and its structured H-1123 exclusion before making new assertions.
2. Searched the retained CISI2 OCR for H-1123 with dash/space variants,9015 with spacing/punctuation variants, and the unsplit9015360 string. All returned zero hits. These negative results are not treated as proof of catalogue absence because the companion OCR is poor.
3. Visually inspected the printed contents, final Harappa photo page, end of the Harappa basic-data table, and corrigenda. The coverage endpoint explains why an H-1123-labelled page cannot be recovered from this volume.
4. Reopened original Vats9015 metadata and separate356/360 photograph crops. The earlier conflict persists; no new interpretation was forced from the second corpus's availability.
5. Stopped the bounded CISI2 search. No new download or request to an institution/person was made. A primary publication actually containing H-1123 or an explicit inventory/correction linking9015 to360 remains necessary.

Renders were made with `scripts/inspect_research_pdf.py`, source `h843_identity_CorpusVol2.pdf`, prefix `h1123-cisi2`, pages6/386/480/482,scale3600. `scripts/audit_h1123_cisi2.py` reproduces the exact failed local locators and unretouched fractional-coordinate crops; its output is `data/processed/h1123_cisi2_locators.json`. `data/processed/h1123_cisi2_review.json` pins the inspected sources, images, scripts and this report. There are no new raw files or pending downloads in this phase, and the central registry and prior review were not edited.
