# Yajnadevam / Bharath Rao: bounded decipherment validation

Reviewed 11 October 2026 at the user's request. **The inspected work does not
establish a decipherment.** Its uniqueness argument is insufficient, and a
controlled execution reproduces an unsound intersection in the author's program.
This rejects the claimed validation, not every proposed sign value or Sanskrit
as a possible language. No ancient sound or meaning is admitted into our corpus.

## Sources and scope

Primary sources are the author's 99-page *A cryptanalytic decipherment of the
Indus script*, compiled 13 November 2024, and the public author repositories.
The paper was downloaded from the [Rare Book Society mirror](https://rarebooksocietyofindia.org/book_archive/A_cryptanalytic_decipherment_of_the_Indu.pdf).
This assessment is version-specific; the mirror is not proof of the newest
possible revision. [ScriptDerivation](https://github.com/yajnadevam/ScriptDerivation/tree/5835e8b022106ed105e86c762fd64e1ec9875cce)
was pinned at commit `5835e8b022106ed105e86c762fd64e1ec9875cce`;
[Lipi](https://github.com/yajnadevam/lipi/tree/fc8813a52e183d19c441631dc26c33a4dccbea39)
at `fc8813a52e183d19c441631dc26c33a4dccbea39`. The latter equals the previously
retained Lipi commit; its existing inscriptions and transliterations are reused.
Their prior acquisition does not make them independent validation data.

The finite assessment covered the mathematical proof, derivation method and code,
reported external checks, and one frozen program control. Independent read-only
reviewers criticized the proof and code before execution and verified the saved
counterexample afterward. Social-media criticism was not accepted as evidence.
No outreach, real Sanskrit dictionary download, full translation replication,
alternative-language fit or new archaeological experiment was performed.

## 1. The length threshold is not a uniqueness proof

Paper pp7–8, section2.4.2, computes an effective alphabet of 330 signs and divides
by redundancy0.7 to obtain about471. Page93 then treats reading beyond that
threshold as sufficient proof. The author also removes ligatures from the count
and adds37 to represent phonetic alternatives. The formula pages were rendered
and visually checked, not inferred from defective glyph OCR.

Our mathematical objection is to the inference, not the arithmetic. A unicity
estimate depends on a specified cipher/key ensemble and language model. It does
not prove zero remaining uncertainty for every particular string of that length.
For example, repeating one inscription to arbitrary length cannot resolve values
of signs it never contains. Length is not itself a certificate that every key
degree of freedom has been constrained.

More importantly, the implemented search has choices beyond a fixed assignment
of one symbol to one phoneme. Optional vowels, sound mergers, grouping of signs,
conjunct handling, direction, segmentation and dictionary augmentation all alter
the candidate space. The numerical adjustment is not a derivation of the entropy
of that complete rule system. Reading selected texts under adjustable rules cannot
be substituted for a uniqueness proof under a different fixed model.

This criticism does not show that two complete Sanskrit decipherments exist.
It shows why the cited calculation cannot certify that only one exists, or that
the proposed one is historically correct. Fixing the program defect below would
not repair this mathematical gap.

## 2. Original program can restore an eliminated candidate

The audited [original Perl program](../data/raw/yajnadevam-prove-oct11.pl) only
substitutes previous options when that set is nonempty. It replaces the set after
each row. If a row leaves zero matches, the following row returns to the original
wildcard, instead of preserving the empty cumulative intersection. Stored values
from earlier groups are printed but not automatically propagated into later
groups. Earlier phonetic assignments are embedded manually in the regex input;
the displayed CISI identifiers and sign strings are not independently decoded.

Before execution we froze the [control protocol](../data/processed/yajnadevam_intersection_control_protocol_v1.json).
We used the exact original `003-d-bow` block and unchanged original program, with
the toy dictionary `and`, `ja`, `jja`. These are algorithmic fixtures, not claimed
Sanskrit words. There was exactly one author-program invocation.

| Original constraint | Candidates from fixture | Correct cumulative set |
|---|---|---|
| C-80: `an(..?)` | `d` | `d` |
| H-1919: `(..?)an` | empty | empty |
| M-1637: `(..?)a` | `j`, `jj` | empty |
| H-1545: `(..?)\1a` | `j` | empty |

The [saved original stdout](../results/yajnadevam_validation_v1/intersection_control/stdout.txt)
nevertheless ends with `003-d-bow:  = j`. Row2 eliminated all candidates; rows3–4
restored and narrowed a fresh set. The returned `j` does not satisfy the earlier
constraints. This is a concrete counterexample to the program's interpretation
as a cumulative-intersection proof.

Our initial output parser expected one space before `=` and incorrectly recorded
that the prediction was not reproduced. The output actually has two spaces. The
[separate observation review](../results/yajnadevam_validation_v1/intersection_control/observation_review.json)
corrects that measurement using saved stdout and verifies all original pins.
The initial result, fixture, program and output are preserved unchanged. No rerun
or adjustment to the author's code/regexes was made. A second read-only reviewer
verified the sets and correction independently.

The toy control establishes an algorithm defect. It does not measure its frequency
with the author's augmented Sanskrit dictionary or show that every printed sign
assignment is wrong. The supplied corpus has32 derivation groups; neither it nor
this control is an automatic full-corpus decoder or a validation of all417 signs.

## 3. The checked external comparisons do not validate the key

Paper Table2 compares cuneiform names with proposed Sanskrit equivalents.
Existing primary audits can be reused for specific overlapping objects:

| Candidate object | Retained independent evidence | Consequence |
|---|---|---|
| P516366, Nanasa/Samar | Catalogue seal illegible; possible duplication with P453801 unresolved | No readable Indus string independently assigned either name |
| P525331 / Louvre AO22310, Shu-ilishu | Cuneiform interpreter seal; no Indus counterpart supplied | Occupation and proposed name resemblance do not align Indus phonemes |

See [name-pool audit](MELUHHA_NAME_POOL.md),
[P453801/P516366 follow-up](P453801_FOLLOWUP.md), and
[external-anchor review](EXTERNAL_NAME_ANCHORS.md). No repeated search was needed.
These exclusions apply to the inspected objects, not to every item in Table2.
That table provides language-hypothesis comparisons rather than independently
attributed matching Indus spellings.

Table11's seven later mixed-script readings and the proposed Brahmi correspondences
were inspected as claims. We did not independently authenticate every artifact,
date, glyph correspondence or translation. They cannot be reported as either
replicated confirmations or individually falsified readings in this assessment.
Similarity of shapes alone also leaves the proposed correspondence as a hypothesis.

## 4. Corpus readability is not independent success

The paper describes adding forms after dictionary dead ends and using grammar or
theme for sparse signs (pp15–16). It also leaves intended inscription meaning
outside its stated accuracy criterion (p25). We did not identify a frozen decoder,
genuinely withheld artifact set and independent scoring procedure in the inspected
method/conclusion. Long inscriptions presented during fitting are not automatically
a holdout. Every manual adaptation needs accounting before an independent score
can distinguish recovery from fitting.

A further test would require a complete fixed decoder including all exceptions,
an independently controlled lexicon/grammar, an explicit failure policy, and
predictions on independently attributed material. Such a test could support or
contradict particular readings. Running more adjustable dictionary matches now
would not resolve the identified validation gaps.

## Decision and persistence

Finite stopping rule reached. Classify this as **candidate validation failed;
individual readings unresolved**. No established key, semantic anchor, statistical
p-value or decipherment announcement follows. This assessment does not claim an
exhaustive linguistic disproof. The overall research goal remains active.

The [decision record](../results/yajnadevam_validation_v1/decision.json) pins sources,
control and reviews. Downloaded bodies and headers remain in `data/raw/` and are
registered with bytes, SHA256 and provenance in `data/sources.json`. Derived text,
page renders and execution records remain in `results/yajnadevam_validation_v1/`.
The original intersection run is closed: reopen only for a changed pinned author
version or a documented defect, not to repeat this counterexample.
