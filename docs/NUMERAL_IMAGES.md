# Artifact images strengthen one constraint and clarify a face crosswalk

**The H-306 mismatch is visible in a published catalogue photograph and an earlier
normalized transcription.** It is not merely an unverified pair of numbers in a
modern CSV. What remains conditional is the assumption that those faces express
equal quantities using the proposed numerical roles.

## H-306: an identifier chain, not a guessed image match

The [CISI volume 1 scan](https://ignca.gov.in/Asi_data/76884.pdf), edited by Jagat
Pati Joshi and Asko Parpola (1987), supplies the following checks:

| Evidence | Locator | Observation |
|---|---|---|
| H-306 photograph | Printed p.225; PDF p.261 | Two long strokes on A; three beside the plain U on B |
| H-306 catalogue data | Printed p.371; PDF p.407 | Excavation 13270; museum ASI 63.11.183 |
| Mahadevan identifier table | Printed p.824; PDF p.833 | Same identifiers join reference 5474 |
| Mahadevan normalized text | Printed p.144; PDF p.155 | Reference 5474 also gives the two-versus-three pattern |

The Mahadevan source is our existing
[1977 catalogue scan](../data/raw/mahadevan_1977_text.pdf). A reproduction on slide
30 of [Farmer's 2004 presentation](https://safarmer.com/indus/Harvard2004.pdf) first
located the photograph. Its proposed religious meanings are not adopted. Reuse of
one photograph and repeated publication of one object are not independent samples.

The [visual evidence ledger](../data/processed/h306_visual_evidence.json) records
the reviewed pages, source hashes, literal observations, identifiers and limitations.
This is one manual review, not an independent double transcription. Photographic
orientation and the normalized drawing differ; comparing stroke counts does not
require a common left-to-right orientation.

## A constant conversion between units does not rescue the global rule

The original [screen](NUMERAL_SCREEN.md) assumed a common long-stroke value L.
H-306 then requires 3L = 2L, which fails for L > 0. A broader test allows different
positive values in the two marker contexts:

- a: value per long stroke next to W700, including its unit conversion;
- b: value per long stroke next to W840, including its unit conversion.

The recorded H-1923 pair requires 2a = 2b. H-306 requires 3a = 2b.
Subtracting the equations gives a = 0, and then b = 0. Therefore **no positive,
constant pair (a,b)** can satisfy both. Equivalently, the required b/a ratios are
1 and 3/2. This argument does not depend on decimal or octal bases, nor on assigning
stacked strokes a particular multiplier.

H-1923 is still supported here by the secondary transcription, not a newly checked
photograph. The broader result is consequently conditional on that record as well
as the assumed equalities. Object-dependent units, non-additive modifiers, or faces
that do not balance would change the hypothesis. They require evidence and rules;
they cannot be silently introduced to preserve a failed universal rule.

The exact rational constraints are saved under `constant_long_stroke_unit_ratio`
in [the screen results](../results/numeral_pair_screen.json) and reproduced by
[the screen script](../scripts/screen_numeral_pairs.py). Its test retains both the
contradiction and a compatible repeated-pair control.

## M-331: physical faces can now be joined explicitly

CISI p.84 (PDF p.120) photographs the six physical faces. The four inscribed faces
are A, B, D and F. The data row on p.368 (PDF p.404) identifies HR 2240, NMI 155.
The [review ledger](../data/processed/m331_visual_evidence.json) maps the local text
rows to those physical labels:

| Local row | CISI face | Distinguishing pattern |
|---|---|---|
| 2849.1 | A | Two-line text; five grouped strokes and four short strokes |
| 2849.2 | B | Curved sign with one stroke |
| 2849.4 | D | Three short strokes |
| 2849.3 | F | Compound signs with curved flanks |

Thus different row ordinals do not by themselves indicate conflicting faces.
The article's prose ordering appears to be A, B, D, F, whereas the local rows use
A, B, F, D. That article-order join is inferred from the prose; its Figure 18
has still not been checked visually. The catalogue's own convention on p.XXIV
(PDF p.28) distinguishes physical-face capitals from lowercase impressions.

The photographs do not establish that local W899 and the proposal's W900 are
interchangeable throughout the corpus. No such alias is applied. Nor do they prove
that face B is a total or that particular signs take particular place values. The
[conditional algebraic ambiguity](NUMERAL_EQUATIONS.md) remains.

## The scan itself contains a duplicate volume

The downloaded file has 862 PDF pages. Comparing embedded image streams shows that
each of pages 432-862 duplicates the corresponding page 1-431. All 431 comparisons
require nonempty images and match exactly. The second half is another copy of
volume 1, not volume 2, and supplies no additional archaeological evidence.

The [audit script](../scripts/audit_cisi_scan.py), requiring optional `pypdf`, and
[pair-by-pair results](../results/cisi_page_duplicate_audit.json) preserve this
check. Locators above always use the first copy. Rendering and OCR use the existing
[PDF inspection script](../scripts/inspect_research_pdf.py); OCR only locates pages,
and all conclusions above rely on the specified visual checks.

Both new PDF downloads are in `data/raw/`, with URLs, sizes and hashes in
`data/sources.json`. No primary text was changed to fit a numerical candidate.
The investigation has strengthened a constraint and resolved part of an artifact
crosswalk; it has not established meanings for all signs.
