# Metal-tool weight anchors: Pettersson 1999

The paper supplies genuine reported physical weights, but **does not establish any sign's numerical value from them**. Its two-object fits depend on disputed readings, preservation and the intended meaning of the inscription. A seemingly successful fit for K-122 additionally supplies missing signs and an assumed original mass. The reconstructed Mohenjo-daro calculation contains an algebra error not listed in the accessible official errata text.

The publisher's original 20-page PDF is saved as `data/raw/pettersson_1999_indus_numerals_metal_tools.pdf`. The [official record](https://insa.ndl.gov.in/items/049524a4-8d7a-478e-928d-c44bf4e90523/full) links this [publisher PDF](https://insa.nic.in/writereaddata/UpLoadedFiles/IJHS/Vol34_2_1_JSPettersson.pdf). The author institution's [errata PDF](https://kau.diva-portal.org/smash/get/diva2%3A593951/ERRATA01.pdf) timed out on two direct attempts. Its official indexed text is preserved in `data/raw/pettersson_1999_errata_web_capture.json`, explicitly **not PDF bytes or a visual verification**. Download URLs, hashes, byte counts and failures are in `data/processed/pettersson_1999_downloads.json`; the central registry was not edited.

## The nine-object inventory

The following factual cells were visually checked on printed page 101 (PDF 13). These expressions use **Pettersson's local u/i/t/x notation**; the text numbers are Finnish-corpus references. They are not automatically M77 sign IDs or M328 readings.

| Object | Paper's expression | Finnish text | Reported surviving mass | Qualification |
| --- | --- | --- | --- | --- |
| C-39 | 2x 3u (?) | 5083 | unavailable | Ingot; x as numeral uncertain |
| C-40 | 3u 5(?) i | 5075 | unavailable | Broken axe; expression crosses another inscription |
| DK-7800 | 4i 4t | blank | unavailable | Knife; condition and shape poor |
| DK-7857 | 7i 4t | blank | unavailable | Possible spearhead; very thin and damaged |
| DK-7855 | 6i | blank | 262 g | Other signs nearby; first stroke lower |
| DK-7856 | 1u 5i 4t | 2796 | 165 g in table; 165.343 g on p98 | Surviving tang, not whole chisel |
| DK-7835 | 7u 6i | 2798 | 1910 g in table; 1910.030 g on p98 | Axe affected by corrosion/cleaning |
| K-121 | 1u (or ???) | 7080 | 210 g | Multiple readings considered |
| K-122 | 5i | 7081 | 476 g | Corrosion; additional lost signs possible but unproved |

Thus only five of the nine have masses in this table. Printed p91 explicitly says Mackay did not give C-39 or C-40 weights. The table's **<430 g** for DK-7856 is an estimated whole-chisel mass, not a sixth measurement. The structured ledger `data/processed/metal_tool_weight_anchors.json` preserves these distinctions, every alternative equation, exact decimal strings, strict inequality, and page-image hashes.

## Kalibangan: physical observation versus fitted interpretation

Printed p92 (PDF 4) acknowledges the 210 g and 476 g weights as supplied by B. M. Pande through Asko Parpola. They are independent observations in the limited sense of reported surviving object weights. The paper does not supply balance records, uncertainty estimates or a measurement of the original mass.

Reading K-121B as 2u and K-122B as 5i gives `u=105 g, i=95.2 g`; reading the former as 1u gives `u=210 g`. The first line of p93 prints **125 g**, corrected to **105 g** in the official indexed errata. Reinterpreting the ambiguous K-121B sign as two strokes instead gives `u+2i=210`, hence `u=19.6 g`. Changing the axe's original mass to an assumed 500 g yields `i=100 g,u=10 g` (pp93–94). The attractive 10:1 ratio therefore depends on both a changed reading and an unmeasured original mass.

Section 4, pp96–97, explores adding lost signs to K-122. For example, proposed `3u5i`, with `u=137 g,i=13.7 g`, totals 479.5 g, but the three u signs are supplied by the model. Proposed `1u8i`, with `u=274 g,i=27.4 g`, totals 493.2 g and supplies one u plus three additional strokes. Pettersson explicitly cautions that the fit benefits from uncertain original mass and extra assumed numerals. It cannot serve as independent validation of the supplied signs or values. Page 95 separately explains why two equations in two unknowns provide a solution rather than confirmation, and calls for further objects.

## Mohenjo-daro: a restricted contradiction and an arithmetic correction

Printed p98 (PDF 10) reports tang **165.343 g** and axe **1910.030 g**, then rounds them to 165 and 1910 for calculation. With the visible expressions, the rounded equations are:

```
u + 5i + 4t = 165
7u + 6i     = 1910
```

Multiplying the first by seven and subtracting the second gives `29i+28t=-755`. With the precise reported masses it gives `29i+28t=-752.629`. Consequently, nonnegative additive values cannot encode both **surviving** masses under these expressions. This is a useful conditional exclusion, not a refutation of every weight-related interpretation: the chisel is broken, and p97 says the objects were corroded together and lost material in chemical separation. Pre-treatment aggregate mass was apparently not recorded.

The author next compares chisel shapes and proposes original chisel mass below `2.6×165=429 g` (p99, PDF 11); the table rounds this to <430 g. This estimate uses other tools' proportions and approximate thickness, not an intact measurement of this chisel. The printed equations are:

```
u + 5i + 4t < 429
7u + 6i     = 1910
```

Exact elimination gives **`29i+28t<1093`**, or **`i+(28/29)t<1093/29`**. Page 99 instead prints `i+(4/29)t<37.69`, omitting the factor seven on the t contribution. Page 100 consequently reports `i<33.13 g` for `t=i`; the correct bound under the printed equations is **`i<1093/57≈19.1754 g`**, with **`u>4872/19≈256.4211 g`**. The primary expression, printed result and independent correction all remain separate in the ledger. This error does not establish a different numeral system.

## What the evidence supports

The masses can rule out specified models and constrain conditional parameter ranges. They do not identify inscription meanings without independently fixed readings, boundaries, arithmetic conventions and original-mass assumptions. The proposed octal interpretation is an internal-pattern argument; on p102 the author says a small t fraction cannot be tested by these weight equations because preservation uncertainty is too large. His alternative that 4t is a nonnumerical mark is also retained on pp101–102.

This audit visually checked the downloaded paper's pp91–102. It did not reweigh the original tools or independently reread the cited CISI photographs and excavation tables. No existing corpus transcription or semantic reading was promoted.
