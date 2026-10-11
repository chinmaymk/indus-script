# M-735 / MIC60: a local W195–M054 correspondence

Reviewed 27 September 2026, after a source-exposed masked search. The published
catalogue chain supports **W195 → M054 locally on MIC60/C3070**. It assigns no
meaning or sound, and does not authenticate the other W195 occurrence, H-843.

The secondary export labels row3159.1 M-735, excavation `DK-C 3070060`, with seven
source-order tokens `W740 W760 W235 W002 W390 W125 W195`. It labels the surface
Poor and preservation complete. These labels are not new condition assessments.
No proposed Sanskrit or English reading from the export was used.

Marshall, *Mohenjo-daro and the Indus Civilization*, volumeII, printed402/PDF53,
tabulates item60 as **C3070**, size1.25×1.3in, level3ft0 below surface, typeB,
white steatite. The table does not itself print the secondary `DK-` prefix.
VolumeIII, PlateCV, photograph60 (Archive leaf185) displays the numbered object
with seven upper sign groups and a one-horn animal below. The rightmost sign's
fine strokes are weak in this reproduction; no enhancement or reconstruction
was used to invent missing detail.

Mahadevan AppendixV printed818/PDF827 explicitly maps MIC items1–560 to
references1001–1560 respectively. Thus MIC60 maps to1060 by an explicit source
rule. Printed40/PDF51 shows its seven-sign line. The rightmost displayed glyph
has the looped, multi-stroke form numbered **54** in the primary sign list,
printed32/PDF43. It is visibly different from the straight crossed form with a
small terminal hook numbered226 on printed34/PDF45. The normalized first code
in the retained candidate transcription is M054, agreeing with this inspection.

The older object and normalized transcription are securely linked by their
publication numbers. The modern M-735 alias is only secondary here: its CISI2
metadata was not inspected. The local W195 correspondence depends on that
secondary row's stated old publication identity and full compatible seven-token
sequence; it is not a physical autopsy or a blind sign prediction. Photograph60
corroborates broad arrangement, while precise numbered identification rests on
the primary normalized glyph and sign list. No global W195 equivalence is promoted.

The existing P076 feature table lists W190/W192/W194 under candidate M054/M055
but omits W195. It therefore cannot be treated as an exhaustive conversion table.
It remains unmodified. This finding does not show that all those Wells codes
have equal sounds or meanings, and a modern pictorial description is not a reading.

## Reproduction and failed steps

- Original volumeII scan, M77 scan and appendix/sign-list renders were already
  retained. A new original page image, `data/raw/comb_tablet_marshall_leaf185.jpg`,
  is recorded in `data/processed/m735_new_sources.json` with URL, bytes and SHA256.
- The volumeIII OCR has almost no useful text on these plates. Searching its
  XML for literal60 produced no hit. The inspected existing leaf183 contains
  items19–40; the next illustrated leaf185 correctly contains41–69, including60.
- An initial M77 PDF42 render reached the codes page, not the sign list. The
  retained primary sign-list page32/PDF43 was then inspected. The codes page
  remains retained as the failed navigation attempt.
- Viewing that render before its live rendering process completed returned an
  invalid-image error. The same process was polled to successful completion and
  the finished image read; it was not restarted.
- `scripts/render_m735_crops.py` reproduces the unretouched table, transcription,
  numbered sign and photograph crops. Full renders are recorded in
  `results/comb-tablet-mic_extraction.json` and
  `results/m735_m77_extraction.json`. The parallel tablet review reused the
  original prefix and overwrote its single manifest; this separate record preserves
  the exact parent invocation and unchanged51/42 images.

The machine-readable review and evidence hashes are in
`data/processed/m735_primary_review.json`. The screen and this source review are
separate evidence: computation proposed a candidate, while publication references
and displayed primary glyphs support the qualified local correspondence.
