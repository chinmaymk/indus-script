# Do copper-tablet associations transfer to other objects?

**Two source-level counterexamples oppose a strong, context-independent
“this sign/text identifies the object's pictured motif” rule.** They do not refute
an animal-word reading in general. A word meaning an animal need not describe the
picture on its object, and an ancient text need not be a caption at all.

**Follow-up:** a [published H-598 photograph](ICONOGRAPHY_PHOTO_FOLLOWUP.md) now
confirms the compound glyph and single-horn animal on the same impression face.
The exact W777 variant and copper donor remain source-dependent. The initial
locator-only account below is retained as the history of that first check.

This test follows the [copper bridge audit](COPPER_BRIDGES.md), but searches outside
its discovery domain. It uses the same pinned transcription export, so it is a
new calculation over different objects, not independent archaeological evidence.
No additional source was downloaded.

## Fixed operational claim and method

For each of the seven bridge singleton codes, collect its literal copper motif
labels. Then search all eligible non-copper objects for that code, even inside a
longer inscription. In a separate test, search for the **entire exact bridge text**
and compare its recorded motif labels. This second test does not require deciding
which particular sign might encode an animal name.

The strong transfer rule predicts that the new object's recorded label belongs
to the discovery set. We test a closed set of **source labels**, retaining `Rhin`,
`Anth`, `Bull1:W`, etc. as annotations, without assigning their ancient meanings.
This is intentionally stronger than generic lexical meaning, and even stronger
than a copper-specific naming convention. The latter two remain possible.

The [script](../scripts/audit_iconography_theory.py) imports no source translations.
It applies the existing strict literal parser, allowing `NR` only for a singleton.
It neither reverses sequences nor merges variants. Targets exclude `TAB:C` and
all discovery artifacts. Duplicate artifact/text/label/type rows count once.
Missing motif labels are untested cases. All candidate occurrences, discovery
bridges and rejection counts are saved in the
[audit](../results/iconography_theory_audit.json).

The [protocol](../data/processed/iconography_theory_protocol.json) was written
after the two witnesses were found. This is exploratory counterexample search,
not preregistered prediction, a random test sample, or a significance test.

## Results and coverage

From 5,680 input rows, 3,275 meet the parser rules including the singleton exception.
Deduplication leaves 3,252 artifact/text/label/type observations. There are 3,060
eligible observations outside the copper domain, of which 1,597 have motif labels.
Only **two distinct objects** match either kind of candidate:

| Test | Copper association | Outside-copper witness | Result |
|---|---|---|---|
| Presence of W777 | `Anth`, `Buff`, `Goat:8`, `Othr` | H-598, row 1541.2, `SEAL:S`, Good; `Bull1:W` | Label outside discovery set |
| Exact W740 W615 W503 | `Rhin` | M-1803, row 2320.1, `SEAL:S`, Good; `Bull1:I` | Label outside discovery set |

H-598's literal seven-token text is:

```
W740 W639 W240 W002 W435 W255 W777
```

The exact-text match on M-1803 is a particularly direct obstacle to treating the
whole copper text as a universal caption identifying only the `Rhin` motif. It is
also compatible with text and motif serving different functions or with labels
being inconsistently assigned. Those alternatives require evidence; this test
does not choose among them.

The coverage denominator matters. Of the seven singleton candidates, **six have
no eligible non-copper occurrence at all**. Of five distinct complete bridge
texts, **four have no eligible non-copper occurrence**. Thus W753's hare-name
proposal receives no outside-domain test here; its lack of a counterexample is
not a confirmation. The full [coverage table](../results/iconography_theory_coverage.csv)
includes these zero-coverage candidates.

Requiring Good or Fair condition everywhere leaves 2,030 deduplicated observations,
including 1,936 outside copper and 1,065 labelled ones. Rebuilding the discovery
set leaves W777/W780/W782 connected only with `Anth`. H-598 still supplies the
W777 → `Bull1:W` transfer mismatch. The `Rhin` discovery bridge disappears because
its motif-bearing source row is Poor; consequently M-1803 is no longer a testable
transfer, even though M-1803 itself is Good. A quality flag is not visual proof.

## Primary-source locator check

H-598 is outside the Harappa artifact range in the downloaded CISI volume.
The export gives excavation number **13751**. Mahadevan's appendix, printed p.822
(PDF831), independently lists excavation 13751 under reference **5073**. His text
drawing for reference 5073 appears on printed p.131 (PDF142), with a seven-group
line and a complex horned/U-shaped glyph at its right. Both pages were rendered
and visually inspected; their locators and source hash are in the
[visual ledger](../data/processed/iconography_theory_visual_review.json).

This check corroborates an object locator and finds an earlier drawn text. It
does **not** authenticate an artifact photograph, the `Bull1:W` label, or the exact
W777 code assignment. No W-to-M sign identity is inferred from the drawing. Neither
H-598 nor M-1803 had received photographic verification at this initial stage.
The later follow-up confirms the H-598 same-face pairing, while its exact W-code
equivalence and the M-1803 photograph remain unresolved.
The export also repeats motif annotations across some multi-sided artifacts;
the initial scan therefore made only an object-level association. The new H-598
photograph supports a same-face observation for that object alone.

## Consequence for decipherment

A viable reading should explain these transfer cases rather than infer meanings
solely from copper reverse substitutions. A literal name shared across unrelated
pictures, an institutional emblem, a category marker, and a phonetic usage could
all accommodate a mismatch. None is established here. The useful result is a
specific falsifiable constraint and two source objects to verify next, while
retaining the many candidates this corpus cannot test.

Run `python scripts/audit_iconography_theory.py` to reproduce the audit and
`python -m unittest discover -s tests -p test_iconography_theory.py` for the four
focused tests. They check matching, target exclusion, duplicates and parser
behavior; passing them does not verify the archaeological annotations.
