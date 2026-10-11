# Primary checks of stroke substitutions and curve-ending strings

Reviewed 24 September 2026. Ten complete rows in Mahadevan (1977) agree with the candidate export. Four establish an exact substitution in the complete frame `M267 M099 X M162`: the varying glyph has three, four, or five short strokes, with two arrangements for five. This is stronger distributional evidence than the shared local ending `X M287 M342`, but it supplies no numerical, semantic, or phonetic value by itself.

The parent analysis selected these examples after searching the corpus. They are exploratory checks, not an independent validation sample. [Machine-readable review](../data/processed/stroke_curve_primary_review.json) pins 29 evidence files, including the original PDF, page renders, detail crops, and the export against which each transcription was checked. A further doubtful row is kept separate below.

| Reference | Printed page / PDF page | Complete normalized sequence | Printed metadata |
|---|---|---|---|
| 1091 | 41 / 52 | M267 M099 **M102** M162 | 100101 |
| 1131 | 43 / 54 | M267 M099 **M106** M162 | 100101 |
| 1143 | 43 / 54 | M267 M099 **M104** M162 | 100101 |
| 1157 | 43 / 54 | M267 M099 **M107** M162 | 100101 |
| 1092 | 41 / 52 | M028 M162 M343 M106 M287 M342 | 100101 |
| 1460 | 53 / 64 | M106 M287 M342 | 100001 |
| 2097 | 61 / 72 | M204 M245 M102 M287 M342 | 100001 |
| 2254 | 65 / 76 | M106 M287 M342 M001 | 100101 |
| 4134 | 101 / 112 | M391 M099 M106 M287 M342 | 100101 |
| 4239 | 104 / 115 | M089 M106 M287 M342 | 100601 |

All ten have no visible loss hatching, doubtful-sign mark, or continuation in their printed rows. The sequences above follow Mahadevan's normalized right-to-left glyph order, written as code sequences in reading order. The full pages were inspected to check row boundaries and continuation; the detail crops were then inspected at larger effective scale. Metadata is preserved literally rather than conflated with the glyphs or interpreted as a reading.

The labelled signlist, printed pages 32–35 / PDF pages 43–46, was also viewed. It distinguishes M102's three short strokes from M089's longer three strokes. M104 has four short strokes; M106 has five in one row; M107 has three above two. These graphic counts do **not** establish the ancient values “three,” “four,” or “five,” or prove M106 and M107 interchangeable everywhere.

Two limitations matter for the current hypothesis. Row 2254 has M001 after M342, so the latter is not necessarily the terminal sign. Row 4239 has two different stroke groups, M089 followed by M106, before the curve. The six curve-ending examples do not supply a complete-inscription M102/M106 minimal pair. The authenticated substitution frame is `M267 M099 X M162`, which has a different ending.

Follow-up row **2659**, printed page 78 / PDF page 89, is the potential three-sign counterpart `*M102 M287 M342`, with metadata `103501`. The primary page visibly marks M102 doubtful. The codebook, printed page 31 / PDF page 42, explicitly identifies the upper-right asterisk as a doubtful reading. This confirms that the uncertainty originates in the catalogue rather than only the export. The normalized three-stroke drawing does not resolve the original uncertainty. The row remains excluded from clear substitution evidence.

![2659 with catalogue doubt mark at M102](../results/primary_pages/stroke-curve-2659-detail.png)

Selected primary details:

![1091: three-stroke substitution](../results/primary_pages/stroke-curve-1091-detail.png)
![1131: five-stroke substitution](../results/primary_pages/stroke-curve-1131-detail.png)
![1143: four-stroke substitution](../results/primary_pages/stroke-curve-1143-detail.png)
![1157: three-plus-two stroke arrangement](../results/primary_pages/stroke-curve-1157-detail.png)

Reproduction uses the retained original [Mahadevan PDF](../data/raw/mahadevan_1977_text.pdf) and the existing rendering script:

```sh
FONTCONFIG_FILE=/opt/homebrew/etc/fonts/fonts.conf \
  /Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  scripts/inspect_research_pdf.py mahadevan_1977_text.pdf \
  --prefix stroke-curve --pages 52 64 72 76 112 115 --render-only --scale 3000 \
  --pdftoppm /Users/chinmaymk/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm
```

The additional render used the same command with `--prefix stroke-curve-doubt --pages 89`. PDF page 54, the four signlist images, and codebook PDF page 42 were reused from earlier renders and actually viewed in this review. To reproduce the detail crops, use [the saved page names and crop boxes](../results/stroke_curve_crop_recipe.json):

```python
import json
from pathlib import Path
from PIL import Image
base = Path("results/primary_pages")
recipe = json.loads(Path("results/stroke_curve_crop_recipe.json").read_text())
for reference, (page_name, box) in recipe.items():
    Image.open(base / page_name).crop(box).save(
        base / f"stroke-curve-{reference}-detail.png")
```

OCR located the original six requested rows but missed exact matches for 1091, 1131, 1143 and 1157. Direct page inspection resolved these locators. The first crop of 4134 clipped glyph tops; its box was enlarged and the final image rechecked. No new downloads were needed. This review authenticates published normalized drawings, not the original seals; it does not establish an artifact's date, owner, contents, or language.
