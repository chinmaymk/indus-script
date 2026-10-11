# Artifact identities of the surviving multi-sign chain

The three catalogue strings belong to **two Mohenjodaro seals and one Harappa seal**. They do not form an excavated three-object group. Primary excavation tables now supply field numbers and find contexts; none identifies an owner or a family relationship.

| M77 reference | Authenticated original identity | Published context |
|---|---|---|
|2463|Mackay, *Further Excavations at Mohenjo-daro* (FEM), seal463 = DK7722|Table p383: steatite, typeB; block10, houseII, room26; level −13.6ft; 1.1×1.1×0.35in|
|2302|FEM seal302 = DK3463; also CISI1 M-384|Table p378: steatite, typeF; between blocks3 and4; level −10.2ft; 1.14×0.5×0.35in|
|4084|Vats, *Excavations at Harappa* (EH), seal84 = find474|Table p338: blue steatite, typea, moundF; 7ft3in below surface; 1.1×1.1in|

These mappings do not depend on matching bare integers. Mahadevan1977 appendixV, printed816/PDF825, explicitly keys refs2002–2704 to FEM items2–704 and refs4001–4713 to EH items1–713. Printed818/PDF827 repeats the FEM range. The actual source tables were then read visually. The book's final appendix has a different PDF offset from the earlier Texts section; the retained PDF829 image is printed820, not818.

## Harappa photograph and context

Vats's plateLXXXVIII (PDF184 in the retained plates volume) actually labels photograph84. It shows the unicorn and an upper inscription consistent with the normalized M77 drawing; it has no printed word divider at the analytical split. This is a published photographic view, not a new autopsy or an independent sign-by-sign palaeographic edition.

Vats p38 (Internet Archive leaf64) places find474/plateLXXXVIII84 within the account of **StratumIII**, beside a31ft east–west wall in the centre of the trench, described at squaresK8/5 andJ8/25. It mentions two unicorn seals, find272 andfind474, found on either side of that wall. The wording does **not** assign a separate exact square or side to474, and the companion is not either of the Mohenjodaro chain members. The table independently places474 in moundF. A numbered stratum from this excavation is not itself an absolute date or a genealogical generation.

## Additional photograph of the middle object

CISI1, printed368/PDF404, explicitly lists **M-384 — DK3463 — ASI63.10.187**, with photo references HU842 and HU71/87. This excavation-number match, the M77-to-FEM mapping, and the matching inscription jointly support M77 2302 = CISI M-384. CISI printed95/PDF131 supplies the original/impression pair M-384A/a. The elongated seal has no animal field. The photographs visibly preserve the six-sign composition, with wear around the wheel-form end; the normalized sequence is inherited from the separately verified M77 ledger, not re-deciphered here.

CISI's second data column is its Finnish Concordance reference, as the catalogue explanation says, not a general Mahadevan crosswalk. Its coincident2302 value was not used to equate namespaces. No CISI identifiers or museum accessions were authenticated for2463 or4084 in this bounded search.

## What follows, and what does not

The chain links inscriptions on different artifact forms and across two sites. The two Mohenjodaro pieces have different published loci and levels. Their −13.6ft and −10.2ft measurements cannot establish chronological succession without the relevant stratigraphic relations and depositional assessment; the Harappa depth has a separate site datum. The three records therefore provide no independent parent–child sequence, personal-name values, contemporaneity, or relationship direction. They remain compatible with many repeated-label interpretations, including non-personal ones.

## Attempts and reproducibility

The search reused M77, Vats plates, CISI1, and the existing OCR/page-number metadata. Six source page JPGs were downloaded to `data/raw/`; their URLs, sizes and hashes are in `chain_artifact_identity_downloads.json`. Two were wrong initial table-page selections: Mackay p376 (leaf398) and Vats p339 (leaf365); they are retained and explicitly excluded from target-field claims. Vats PDF100 was an initial locator miss (plateXLVI); PDF184 is the correct seal plate. M77 PDF829/832 and CISI402/403/405/406 were inspected but did not supply additional target identities. CISI photo132 was rendered but not needed or visually authenticated.

All accepted evidence and crop coordinates are pinned in `chain_artifact_identity_review.json`. Existing `scripts/inspect_research_pdf.py` reproduces the PDF renders with recorded scales, prefixes and page lists. The ledger's crop boxes reproduce the unaltered details with Pillow. No global corpus records or semantic/phonetic values were changed.
