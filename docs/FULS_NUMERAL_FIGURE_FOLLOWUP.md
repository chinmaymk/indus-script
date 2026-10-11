# Fuls numerical figures: text attribution confirmed, pixels unresolved

**Figures 16 and 18 were not recovered as inspectable images in this four-query follow-up.** A newly located [author deposit](https://www.researchgate.net/publication/373522958_Ancient_Writing_and_Modern_Technologies_-_Structural_Analysis_of_Numerical_Indus_Inscriptions) repeats the two arguments using source sign 900, but does not resolve the source-to-artifact or signary joins. The established conditional algebra remains conditional.

The deposit identifies the work as a January 2020 conference contribution and says that Andreas Fuls uploaded this copy on 31 August 2023. Its extracted pagination begins at 15; the author's [bibliography](https://www.epigraphica.de/indus/menueindus.htm) cites *Studies on Indus Script* (2020), pp.57–90. The difference is recorded, not silently reconciled by a page offset. No original PDF pagination was visually checked.

## What the text supports

The new deposit describes the sign list as an extension of Wells's system. In its extracted p.26, sign 900 is the proposed numeral associated with repeated forms 904, 914 and 908. On extracted p.30, the two-face argument explicitly assigns sign 900 to source object ID3786. On extracted p.32, the M-331 discussion assigns the same source label to Side 2. This confirms common nomenclature in the author's arguments, not independently established graphic identity or meaning. The inspected text does not identify ID3786 as H-904. Figure 16 and Figure 18 pixels remain unavailable.

Specific evidence locators in the retained web capture are: sign-list convention, extraction lines152–160; sign900 discussion, lines546–563; ID3786 and Formula2, lines675–688; M-331 and Side2, lines769–806. These line numbers belong to the captured web rendering, not manuscript lines. Its accessible Figure11 landing page calls the illustration an example of sign900, but its image also failed. Its URL says `fig5` while the page heading identifies article Figure11; a platform image index must not be substituted for article figure numbering.

## What remains unverified

The earlier [M-331 visual ledger](../data/processed/m331_visual_evidence.json) joins physical CISI face B to local row2849.2, containing a curved sign and stroke. That review did not inspect Fuls's Figure18. The [equation ledger](../data/processed/numeral_equation_claims.json) deliberately preserves the mismatch between local W899 and source900. This follow-up does not alter that policy: author nomenclature alone does not authorize W899=900, H904=ID3786, or equality of the two physical curved forms. It also does not authenticate a total, positional multiplication, or a common value across the objects. No new photograph was examined and no alias was added.

The next necessary evidence is the actual source illustrations or a documented source-ID/physical-artifact crosswalk, alongside a signary defining the two codes. Until then the precise result is **same author label in both arguments; graphic and artifact joins unresolved**.

## Bounded attempts

The four exact queries, with returned results, are retained in `data/raw/fuls-numeral-figure-search.json`:

1. `"Fuls" "Structural Analysis of Numerical Indus Inscriptions" pdf`
2. `"Ancient Writing and Modern Technologies" Fuls 2020 publisher`
3. `site:epigraphica.de Fuls 2020 Indus numerical`
4. `"Fuls" "Numerical Indus" "900"`

The new RG deposit differs from the formerly attempted deposit361812318. Its public indexed text opened, but its PDF button failed in the web reader. An ordinary archival fetch of the newly found page returned HTTP403; the complete error body and response headers were retained. The exposed sign900 figure landing page opened, but its image link resolved to a 404 and its download link gave a cache miss. Neither URL was repaired or guessed.

The author's public Academia profile exposed attachment62075458. That previously unrecorded attachment link produced a web cache miss and an ordinary fetch returned HTTP403, again retained. Neither denied route was retried or bypassed. The author's bibliography supplied a citation but no PDF link for this work. No ICIT login, registration, outreach or alternate credentials were attempted. Four searches were sufficient to exhaust this bounded attempt; failure does not establish that no public copy exists.

All new source captures and error bodies remain under `data/raw/fuls-numeral-figure-*`. The review JSON distinguishes text inspected from pixels unseen, retains exact failures and pins earlier evidence. `data/processed/fuls_numeral_figure_new_sources.json` contains the six-artifact typed source manifest. The files whose names end in `.pdf.partial` and `.html.partial` are complete HTTP403 error bodies, not article contents. Existing reviews, equations and central files were unchanged.
