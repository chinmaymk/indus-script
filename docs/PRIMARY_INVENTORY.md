# Direct evidence for all 417 signs

## What changed

We obtained an archived scan of Iravatham Mahadevan's *The Indus Script: Texts,
Concordance and Tables* (Archaeological Survey of India, 1977), together with its
archive-generated OCR. Table I, printed pp. 717–723 (PDF pp. 728–734), records the
frequency and position of every sign in the 417-sign inventory.

This closes a specific gap: **every supplied M sign now has a direct historical
frequency/position profile**, including signs with no reliable Wells correspondence.
The profiles do not depend on the secondary transcription's proposed translations or
the external M/P/W crosswalk. They do not, however, supply sounds or meanings.

Downloads remain together in `data/raw/`. The source scan is
[`mahadevan_1977_text.pdf`](../data/raw/mahadevan_1977_text.pdf).
The [archive record](https://archive.org/details/TheIndusScript.TextConcordanceAndTablesIravathanMahadevan)
and exact companion URLs are recorded in `data/sources.json`.

## Transcription and validation

The extraction follows OCR word coordinates, the five numerical columns, and the
printed sign order. We visually inspected all seven table pages alongside the extracted
values and corrected **112 cells**, retaining the original OCR in a cell-level ledger.
A further 116 cells involved normalization such as `i` to `1`, reviewed in that page
pass. This was one visual review pass, not two independent transcriptions.

The transcribed values satisfy multiple separately printed constraints:

| Check | Recovered | Printed |
|---|---:|---:|
| Sign rows | 417 | 417 |
| Solitary occurrences | 190 | 190 |
| Initial occurrences | 3,010 | 3,010 |
| Medial occurrences | 7,196 | 7,196 |
| Final occurrences | 2,976 | 2,976 |
| All occurrences | 13,372 | 13,372 |
| Signs occurring exactly once | 112 | 112 |

Every individual row adds up. All seven frequency bands in the introduction, printed
p. 17, match both their sign counts and token totals. The separately printed counts
of sign types observed in solitary/initial/medial/final positions also match:
88/290/286/173. Aggregate agreement is a valuable error check, not a proof that an
error could not cancel another error.

Reproducible artifacts:

- [417-row primary table](../data/processed/mahadevan_1977_table_i.csv)
- [Original OCR and corrections for every cell](../results/primary_table_cells.csv)
- [Explicit correction decisions](../data/processed/primary_table_corrections.json)
- [Visual review record](../data/processed/primary_table_visual_review.json)
- [Aggregate audit](../results/primary_table_audit.json)
- [Primary sign profiles](../results/primary_sign_profiles_417.csv)

Run `python3 scripts/extract_primary_table.py` followed by
`python3 scripts/analyze_primary_inventory.py`. The second script refuses to use a
table with unresolved rows or failed aggregate checks. Neither script infers missing
cell values from the totals.

`python scripts/verify_primary_source.py` additionally checks the four book files
against the archive metadata's file sizes and MD5 checksums; all four agree. The
source manifest separately pins SHA-256. `scripts/render_primary_pages.py` reproduces
the table renders with Poppler; `--pages 50 --prefix texts` reproduces the pilot's
source page.

## Constraints that a reading must explain

**The jar family has sharply different positional behavior.** M342 is final in
971/1,395 occurrences (69.6%). M343, whose shape adds one inner stroke, is final in
5/177 (2.8%) and medial in 152/177 (85.9%). M344 and M345, with further inner strokes,
have respectively 2/35 and 2/51 final occurrences. This argues against treating the
forms as freely interchangeable without accounting for context. It does not yet
distinguish different functions from context-conditioned allography, regional or
object-type variation, or other confounds.

The subsequent [context-bound analysis](CONTEXT_BOUNDS.md) narrows this uncertainty:
different site mixtures alone cannot account for the jar contrast under shared
empirical within-site rates. At Mohenjodaro, M342's final rate must exceed M343's
by at least 39.70 percentage points, from the two marginal tables alone. Other
contextual and allographic explanations remain open.

**“Jar sign = end of every line” fails directly in the primary catalogue.** M342
has 1 initial and 420 medial occurrences: 421 counteroccurrences to a strict line-end
restriction. Three solitary occurrences are not counterexamples, since a standalone
sign occupies the whole line. A phrase-final or suffix hypothesis remains possible;
the table does not mark phrase boundaries or establish grammatical values.

**Two-stroke forms require more care than a blanket “2” reading.** Tall-stroke M087
is initial in 147/365 and medial in 199/365 occurrences. Short, top-aligned M099 is
initial in only 2/649 and medial in 625/649 (96.3%). Their visible stroke count is the
same, but their positional profiles differ. Quantity, grammatical, classificatory,
and phonetic interpretations therefore need separate tests. Mahadevan himself discusses
possible grammatical uses of superscript strokes in the introduction; that is a
hypothesis to evaluate rather than an accepted translation.

**Other useful structural anchors exist.** M176 is final in 316/355 occurrences;
M211 in 184/227; and M328 in 274/323. In contrast, M267 is initial in 298/376.
These provide concrete constraints for candidate grammars and corpus restoration,
without assigning an arbitrary word to any of them.

**Rare signs remain a serious limit.** 264/417 signs have fewer than ten occurrences
in this catalogue, including 112 singletons. The most frequent 67 signs account for
10,769/13,372 occurrences (80.53%). A key that reads only common formulae might cover
many tokens while explaining much less of the sign inventory. Both denominators are
needed when evaluating a claimed decipherment.

## Position and sampling cautions

These are Mahadevan's reading-order positions **within a line**, with solitary
occurrences separately counted. The secondary export profiles use file/display order
and a deduplicated, filtered selection of whole texts. The denominators and units are
different; do not add the corpora together or interpret count differences as errors.

The atlas includes a coarse descriptive label for each primary profile. Signs with
fewer than ten occurrences are labeled rare. Otherwise a 60% threshold flags
solitary/initial/final-heavy use and an 80% threshold flags medial-heavy use; other
signs remain mixed. These arbitrary screening thresholds are transparent conveniences,
not discovered grammatical categories or confidence levels. Exact counts take priority.

## Next evidence to pursue

The archived book also contains the full printed texts and pairwise tables. A checked
machine-readable transcription could connect these all-sign positional constraints to
actual sequences while avoiding the provisional M/W mapping. That requires recognizing
the printed glyphs, preserving damage and line boundaries, and independently checking
the transcription against source images. The present step does not claim that work
has already been done, or that the script has been deciphered.

## First sequence witnesses

A [four-line pilot](../results/primary_text_pilot.html) now records texts 1002, 1004,
1014 and 1022 on printed p. 39. The three undamaged, non-doubtful lines contain 19
sign tokens; the fourth retains a damage span of unknown length and a source-doubtful
M373. This deliberately selected sample is not a representative corpus or an OCR
accuracy evaluation. Glyphs were compared with the printed sign list; it remains
a single transcription pass.

Text 1004 supplies a direct visual witness for the internal-jar counterexample:
in reading order it is `M059 M127 M245 M342 M075 M245 M245`. M342 is fourth of
seven signs. Texts 1014 and 1022 share the reading-order opening `M267 M099` and
end with M342, but have different intervening sequences. These examples constrain
segmentation hypotheses without deciding whether the units are words, names,
quantities or nonlinguistic categories.

The book's introduction, section 13.2 (printed p. 20), establishes an important
transcription rule: **the editor prints every line right to left**, regardless of
its original direction, and normalizes graphic variants and asymmetric sign
orientation. The pilot therefore preserves printed order and stores reading order
separately. Asterisk markers and hatched damage are editorial notation. Neither may
be turned into ordinary signs or silently discarded. Original variant shapes and
writing directions need the supplementary lists or artifact photographs.

The input is [primary_text_pilot.json](../data/processed/primary_text_pilot.json);
`python scripts/audit_primary_pilot.py` regenerates crops, the review page and the
structured witness report. The small pilot is kept separate from all corpus-level
statistics.
