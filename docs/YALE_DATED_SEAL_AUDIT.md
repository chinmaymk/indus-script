# Yale YBC 5447: a dated Gulf seal impression, not a recovered bilingual

The Yale catalogue directly identifies its seal-impression entry **1090 as YBC 5447**, dated to **Gungunum year 10**. This provides a cuneiform date for the use of that seal design. It does not supply an Indus inscription with a known translation. The entry describes a scene and does not identify an Indus sign sequence or name its owner.

## Primary source and visual audit

Downloaded the complete 514-page scan of Briggs Buchanan, *Early Near Eastern Seals in the Yale Babylonian Collection* (1981), from the [Yale Babylonian Collection](https://babylonian-collection.yale.edu/sites/default/files/files/Buchanan1981.pdf). The local file is `data/raw/yale_buchanan_1981.pdf`. Source and reviewed-image fingerprints are recorded in `data/processed/yale_dated_seal_review.json`; the proposed source-registry entry is `data/processed/yale_dated_downloads.json`.

Visually checked introduction xi/PDF 9, catalogue printed 382/PDF 400, its facing illustrations/PDF 401, and adjacent pages PDF 402–403. The important catalogue/photo pages were also rendered at 3,200 pixels and the illustration page was viewed again. OCR is an aid, not an independent authority for the glyphs.

| Entry | Identification in printed 382 | What the entry establishes |
|---|---|---|
| 1088 | Newell 23 | Separate stamp seal, bull and Indus characters; new impression illustrated. |
| 1089 | NCBS 876 | Separate damaged/worn stamp seal, bird and possible Indus characters. |
| 1090 | YBC 5447 | Stamp impressions on a tablet; dated Gungunum 10; scene described without an Indus inscription. |
| 1091 | NBC 9256 | Separate cylinder with animal scene. |

The section heading and neighboring inscriptions do not make 1090 an inscribed Indus seal. Its illustration labels also matter: **1090a** shows the tablet's left edge, **1090b** a bottom-oblique view, **1090c** a drawing of the impressed design, and **1090d** a comparative drawing of a seal from Failaka. The catalogue explicitly separates the Failaka object; this is not a photograph of the Yale seal die or proof of a die match.

The 1090 scene has two seated figures using drinking tubes, vessels, a central bull head, upper circle and crosshatched squares, and three horizontal marks. The photographs show partial impressions, while the drawing assembles a clearer design. At this reproduction quality I cannot independently collate every fine mark against the photograph. No new M77 sign IDs are assigned. Circle, grid and line motifs alone are insufficient to assert a written sequence.

## What is independently dated

The introduction specifies **1923 BCE under the middle chronology** for Gungunum 10. The regnal year is the cuneiform anchor; converting it to an absolute BCE date depends on chronology. The seal catalogue refers the tablet edition to Hallo, *Assyriological Studies* 16, pp. 199ff., and the seal discussion to Buchanan in that volume pp. 204ff. It also cites Buchanan's 1967 *Archaeology* article, pp. 104ff.

The catalogue's historical discussion uses the dated impression to constrain Gulf seal style. That argument must not be inflated into an independent date for every Indus sign or the entire Indus corpus. Nor does it establish which contracting party applied the stamp, who owned the lost die, or whether any individual motif spelled that person's name.

The amount of goods and personal names belong to the separate tablet-text audit. Even if the same transaction has readable cuneiform names, a semantic bridge additionally needs an authenticated Indus text and an independently justified correspondence. This catalogue supplies neither a sign sequence for 1090 nor such a correspondence.

## Original 1965 seal discussion: motif resemblance is acknowledged

After the catalogue audit, the sibling tablet audit downloaded the original [AS 16 volume](https://oi.uchicago.edu/sites/default/files/uploads/shared/docs/as16.pdf), stored once as `data/raw/gungunum_as16_1965.pdf`. I read extracted Buchanan pp. 204–209 and visually checked printed 204/PDF 224, Plate XVI/PDF 225, and printed 206–207/PDF 228–229. The saved extraction is `data/processed/yale_buchanan_as16_excerpt.txt`.

Buchanan's printed 204 explicitly says drawing C assembles the visible portions of the Yale impressions; its lowest strokes indicate possible seal-edge traces. Drawing D represents a different Failaka seal. His initial comparison is strong resemblance, not a demonstrated match of recovered die and ancient impression. Plate XVI confirms those labels and the visibly different upper motifs: Yale has a circle and grids, while the Failaka comparison has birds and a plant.

The important qualification is on printed 206–207 and footnote 17. Buchanan places both designs in Type III and thinks any Indus signs there generally no longer function as writing, with a possible exception for Gadd 12. He nevertheless explicitly compares the Yale crosshatched squares to Marshall signs **ccxcvi–ccc**. Therefore the defensible result is **no authenticated Indus inscription**, not an assertion that no motif could resemble an Indus sign. The cited resemblance does not identify an M77 sign, demonstrate a text sequence, or establish the meaning of a square motif. His Type III argument and geographic proposals remain historical interpretations, not newly verified facts about the entire Indus corpus.

## Attempts, corrections and reproducibility

- Initial sandbox `curl` failed DNS resolution and produced no source file. The authorized escalated download completed successfully: 25,377,330 bytes.
- `pypdf` extracted the introduction, but the body catalogue is largely image-only. Text search therefore found the introductory reference but missed the actual entry. Page rendering recovered the primary evidence.
- A web search returned a useful indexed transcription of printed 382. A direct web open failed because of the PDF's size; the downloaded original and images were used for conclusions.
- A parent search initially raised an apparent claim that an unmistakable Indus character appeared on the Yale tablet. The parent traced the juxtaposed snippet to Gadd no. 7/IM8028 instead. The claim is not adopted here; it is not in this catalogue entry.
- Original 1967 article was bibliographically located but not recovered in this bounded audit. The original 1965 seal discussion was subsequently read and four relevant pages visually verified as above; the other agent audits its tablet edition. No later claim about an exact Failaka/Yale die match is assumed from the juxtaposed drawings.
- AS 16 rendering printed a nonconformant image-codestream warning but completed successfully. Each of the four rendered pages opened and was reviewed.

Reproduce extraction with `scripts/inspect_research_pdf.py yale_buchanan_1981.pdf --prefix yale-buchanan`. For visual review use that script with `--pages 9 400 401 402 403 --render-only --scale 1600 --pdftoppm PATH_TO_PDFTOPPM`; the `yale-buchanan-detail` run used pages 400–401, scale 3200, and `--tesseract /opt/homebrew/bin/tesseract`.

**Result:** useful independent documentary dating of a Gulf stamp design, but no recovered Indus reading, sound value, name equivalence, or commodity value. All semantic assignments remain unchanged.
