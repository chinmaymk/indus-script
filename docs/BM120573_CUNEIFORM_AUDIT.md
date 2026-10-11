# BM120573: a hybrid seal without a translated Indus counterpart

Audit date: 2026-09-24. Object: **BM120573 = 1928,1009.56 = U.7683 = Gadd1932 no.1**. Do not merge it with BM122187 (Gadd no.2), BM123208 (Gadd no.16), or either Umma object.

The original catalogue establishes a cuneiform inscription on an Indus-style seal, but does **not** establish its meaning or the language of its text. It supplies no sign-by-sign translation of Indus writing. A name remains a possibility; neither a name nor an occupation, commodity, title, or religious formula can currently be used as an authenticated semantic label for this object.

## Sources and direct inspection

- **Gadd1932, printed pp.5–6, PlateI no.1:** downloaded the complete 44-page scan from [IGNCA](https://ignca.gov.in/Asi_data/33779.pdf), stored as `data/raw/hybrid_bm_gadd_1932.pdf`. Printed pp.5–6 are PDF12–13; PlateI is PDF14. All three were visually read. The plate was inspected at 1800 and 3600-pixel full-page render scale. Raw source and review-image fingerprints are in the accompanying JSON.
- **British Museum:** reused the previously archived indexed catalogue response in `data/raw/external_name_anchors_web_capture.json`, response containing `turn144search1`. This identifies the [official record](https://www.britishmuseum.org/collection/object/W_1928-1009-56), accession, dimensions, and Diqdiqqah surface provenance. New web opens and a direct public HTTP request returned403, so this audit does not claim a freshly retrieved museum image or current full catalogue.
- **Parpola1994, printed p.131, Fig.8.3:** reused `data/raw/umma_old_parpola_1994.pdf`, PDF149. Read the page and figure visually at 2600-pixel render scale. This is the author's own interpretive discussion, not an independent discovery of a translation. No duplicate source download was made.

## What Gadd actually reports

Printed p.5 identifies BM120573 explicitly. It describes grey steatite, a lengthwise-perforated ridge on the back, and a lowered-head short-horned bull. A narrow band crosses its back. There is no preserved manger in front; a horizontal divider separates the animal from the inscription. The plate corroborates a rectangular seal back with a pierced projecting ridge and an associated impression containing the animal and the upper sign field. The image is degraded; precise wedge identity and a fourth sign cannot be independently resolved from this reproduction. The modern museum number visible on the reverse is not part of the ancient inscription.

Gadd's printed p.6 gives the following alternatives, explicitly acknowledging wear and cuneiform polyphony:

| Position | Gadd1932 reading | Status in the source |
|---|---|---|
| 1 | SAG(K) or KA | Doubtful choice |
| 2 | KU or possibly LU | Doubtful choice |
| 3 | ŠI | Described as almost certain by Gadd, not freshly established here |
| 4 | Unknown, possibly absent | Almost obliterated if it existed |

The provisional phonetic rendering is **sak-ku-ši--**, retaining possible loss at the end. This is a conjectural reading of cuneiform, not an Indus decipherment. Gadd does not recognize a Sumerian or Akkadian name and explicitly declines to speculate about the word's meaning. He considers local manufacture at Ur or another area under both Indus and Sumerian influence, preferring the latter. These are origin interpretations, not excavated workshop evidence.

The catalogue proposes a pre-Sargonic date from epigraphy, using its historical chronology of before2500BC. Gadd also states the find circumstances give no date. The archived museum record gives circa2500BC and Diqdiqqah surface. Neither is an independent stratified dating anchor; this audit does not convert Gadd's1932 chronological number into a modern absolute terminus.

## Later alternatives and a transcription correction

Parpola's actual printed p.131 gives, in order of likelihood, **šak or ka; ku or ma; ši or ba**. It does **not** list LU in that passage. Some online retellings merge Gadd's LU with Parpola's MA and replace ši by zi; those merged forms must not be attributed verbatim to either original.

Parpola leaves the meaning obscure and offers a foreign name or an unusual Sumerian name as possibilities. Examples include **ka / inim-dab₅-ba**, interpreted as a mouth being seized or inability to speak properly, and **sag-ma-BA**, compared with a personal name sag-ma. These examples do not identify a documented owner of this seal. They demonstrate remaining ambiguity, including a possible Sumerian interpretation contrary to Gadd's inability to recognize one. No candidate is adopted as the inscription's semantic value.

The Fig.8.3 caption labels impression and reverse, but the images show the modern accession-marked seal back at left and the sign-bearing impression at right. Visual features and accession lettering take precedence over assuming the caption's (a)/(b) ordering. Both this reproduction and Gadd's PlateI appear to reproduce closely corresponding views; they are not two independent ancient impressions or two independently readable texts.

## Test of the proposed semantic anchor

The required inference would be: readable cuneiform phrase → known seal meaning → corresponding Indus text → values of matching Indus signs. This object fails at both the first and third links. Its phrase is unresolved, and there is no accompanying Indus inscription identified as a translation. The bull motif cannot supply that missing textual correspondence. A speculative rebus such as an animal-name homophone plus a speculative cuneiform restoration compounds unknowns instead of providing independent support.

The supported contextual conclusion is narrower but useful: **Indus-related seal form and animal imagery can accompany cuneiform writing.** Consequently, iconographic affinity alone cannot decide a seal's script, text language, owner's language or ethnicity, or whether its inscription labels an animal/commodity. This constrains any universal theory that equates those categories automatically. It does not rule out personal names, commodity labels, or administrative functions in the authentic Indus corpus.

No Mahadevan/Wells sequence is assigned to BM120573 here. No Indus semantic or phonetic value is added.

## Attempts, limitations, and reproducibility

1. Searched the existing corpus and review files before requesting sources. Gadd's full PDF was absent; the museum indexed response and Parpola book were already available.
2. New museum web opens returned403. Direct `curl --fail` also returned403, leaving no new museum HTML file. No access protection was bypassed.
3. IGNCA web open timed out; a normal direct authorized download succeeded, producing a valid44-page PDF. `pypdf` found no useful text layer; this failure is retained as `data/processed/hybrid_bm_gadd_1932_text.txt` (page markers only).
4. Used `scripts/inspect_research_pdf.py` with Poppler/Tesseract to find the inserted plates and text pages. Exploratory renders included irrelevant blank/end pages. They are not treated as reviewed evidence. The explicitly reviewed relevant pages are PDF12,13,14 and ParpolaPDF149. GaddPDF15 and39–43 were viewed only to locate plates/establish irrelevance.
5. Visually corrected OCR's SI to **ŠI** and its flattened transliteration to **sak-ku-ši--**. OCR is a navigation aid; the page image is the authority. No attempt to trace lost wedges or restore the unknown fourth sign was made.
6. Parpola render emitted font-cache write warnings but exited0 and produced a readable page, which was viewed. The accompanying JSON fingerprints the actual reviewed image.

Reproduce the key source renders with the existing helper (supply your Poppler path):

```sh
python scripts/inspect_research_pdf.py hybrid_bm_gadd_1932.pdf --prefix hybrid-bm-gadd-review --pages 12 13 14 --render-only --scale 3600 --pdftoppm /path/to/pdftoppm
python scripts/inspect_research_pdf.py umma_old_parpola_1994.pdf --prefix hybrid-bm-parpola --pages 149 --render-only --scale 2600 --pdftoppm /path/to/pdftoppm
```
