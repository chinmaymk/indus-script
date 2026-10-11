# A variable stroke-plus-U field, with primary counterexamples

**The same main inscription occurs beside two, three and four long strokes followed by plain U.** This is direct evidence of variation in an auxiliary field. It supports investigating a quantity-like function, but does not establish numbers, units, words or sounds.

The comparison recovers information lost from a digital export that usually retains only one sequence per catalogue reference. All new evidence comes from the already downloaded Mahadevan 1977 volume. Nothing new was downloaded.

**Later artifact check:** the [exact bridge](M77_U_ARTIFACT_BRIDGE.md) now supplies
original Vats photographs and excavation descriptions for the three-tablet group.
Those later downloads are separate from this initial nine-page recovery. All
three are steatite, but shape, nominal size and find context differ. Their recorded
dimensions do not establish represented amounts.

## The strongest matched comparison

All three references have exactly the same normalized side1 text, **M048 M342 M176**. Their other sides differ:

| Reference | Side2, normalized reading order | Visible long strokes | Primary Texts locator |
|---|---|---:|---|
| 4548 | M087 M328 | 2 | Printed119 / PDF130 |
| 4509 | M089 M328 | 3 | Printed117 / PDF128 |
| 4508 | M095 M328 | 4 | Printed117 / PDF128 |

The original printed metadata is `310001` for side1 and `20001` for side2 in all three cases. The primary codebook decodes these as miniature tablets, two separately displayed sides, one line per side, and original right-to-left direction on both sides. Thus this particular contrast does not arise merely by mixing catalogue object types or original writing directions. The primary forms and metadata were independently checked by two reviewers; the parent also checked the full-page images.

See the [original4508/4509 detail](../results/primary_pages/m77-u-counterexample-4508-4509-detail.png), [fullPDF128](../results/primary_pages/m77-u-counterexample-128.png), and [fullPDF130 containing4548](../results/primary_pages/m77-u-counterexample-130.png). These are catalogue drawings, not new photographs or autopsies of the ancient objects. Distinct catalogue references do not by themselves prove independent manufacture, molds, findspots or transactions.

Two more normalized main patterns have primary checked two-versus-three-stroke contrasts:

| Main pattern | Two-stroke reference | Three-stroke reference |
|---|---|---|
| M391 M099 M040 | 4665, PDF578 | 4601, PDF583 |
| M175 M176 M211 M176 | 5270, PDF578 | 4684, PDF584 |

The first main pattern includes **short** double strokes M099; they are not equated with the **long** strokes M087 in the auxiliary field. The second pair has different recorded original main-line directions in the secondary export; the primary catalogue normalizes both to RTL. Only the first three-tablet comparison above has its original direction and object codes independently rechecked here.

Additional references repeat the M048 M342 M176 contrast:5464 has two strokes, while4387 and several others have three. Conversely,4373 and4702 repeat both their main text and the same three-stroke-plus-U field. That pair provides no quantity contrast. Repetitions are retained without counting them as independent archaeological confirmations.

## Bounded recovery and exclusions

Three parallel reviews transcribed every indexed M328 group on **PDF576–584 / printed565–573**. This is a contiguous nine-page pilot within a larger concordance section, not a complete recovery of all323 primary occurrences. Concordance sorting deliberately groups similar neighboring signs, so its proportions cannot estimate corpus prevalence.

- 141 indexed groups;145 U instances within those indexed lines because two longer lines contain repeated U.
- 110 undoubted, complete, exactly two-sign stroke-plus-U lines:1 with one long stroke,70 with two,39 with three.
- Five lines contain physical loss,12 contain a primary doubtful reading, and four retain reviewer-unidentified glyphs. These categories overlap.
- The4508 four-stroke example is a separately selected original-Texts supplement and is **outside** the141-group denominator.

Physical loss (`LOSS`), doubtful readings (`*Mddd`) and an unidentified visible form (`UNKNOWN`) remain different states. The pilot includes longer lines rather than trimming them into apparent two-sign fields. Actual direction codes are not copied from a different side. The parent ledger retains one long prefix as candidate rather than wholly authenticated; its checked terminal stroke-plus-U is not admitted as an exact two-sign line.

The digital export already contains the exact indexed two-sign line for six pilot references—4364,4459,4515,4660,4671,5483. This shows why **“one sequence per object” does not always mean “first side.”** Other primary lines can be omitted even when a surviving secondary line is preserved. No automatic blanket omission label is applied to every side2 line.

## What a general U hypothesis must explain

The [counterexample review](M77_U_COUNTEREXAMPLES.md) authenticates uses outside the simple field:

- 4401 has U alone on side2; three strokes occur separately on side1. This contradicts a mandatory **same-line** stroke predecessor, but remains compatible with an object-level quantity association.
- 4231 and6109 begin with M328 M307;8202 begins M328 M053 M342.
- 1532 has M095 M328 M002 M012, placing U medially.
- 1206 ends M329 M212 M328: plain U follows a non-stroke sign. M329 is a different, modified form.
- Pilot4452 has M095 M059 M328: four long strokes are separated from U by a fish-shaped sign. Pilot5303 has M167 M087 M328, an additional preceding sign.

The working interpretation must allow U outside an isolated stroke-plus-U field. Calling every U a quantity-field terminator would require additional rules, with explicit tests. These observations do not decide whether its broader function is lexical, phonetic, classificatory, metrological or something else.

## Exact conclusion and remaining ambiguity

Let `m` be the main normalized string and `c` the auxiliary graphic stroke count. A model asserting a single-valued rule `c = f(m)` cannot reproduce the matched two/three/four observations: one identical argument would require three different outputs. This is an exact contradiction for that narrow deterministic model, conditional on the catalogue's readings and object associations.

It does **not** prove a quantity interpretation. A quantity model using labels2/3/4 and a category model using labelsA/B/C can represent exactly the same observed paired records. Their fitted distributions remain identical under the label bijection. A context-dependent allograph model or a model conditioned on additional object information also survives this particular test. No independent amount, arithmetic relation or word meaning fixes the labels.

The reasonable conclusion is therefore **a recurring auxiliary field with multiple graphic states, compatible with quantity notation**. It is stronger than merely noticing tally-like shapes. It still supplies no established sign reading and does not extend a numerical interpretation to every sign in the inventory. The next discriminating evidence would associate these exact objects or equivalent securely matched cases with independently known quantities, units, batch categories, or arithmetic constraints. Tablet dimensions alone would not establish the represented quantity.

## Reproduction and retained evidence

- [Combined analysis script](../scripts/analyze_m77_u_fields.py) and [four validity tests](../tests/test_m77_u_fields.py).
- [Generated results](../results/m77_u_field_analysis.json) and [normalized141-group ledger](../data/processed/m77_u_pilot_normalized.jsonl).
- [Primary matched-context review and countermodels](../data/processed/m77_u_paired_context_review.json).
- [Numeral review](M77_U_PILOT_NUMERALS.md), [structure review](M77_U_PILOT_STRUCTURE.md), and [parent48-row ledger](../data/processed/m77_u_pilot_parent.json).

Run `python3 scripts/analyze_m77_u_fields.py`, or the complete offline `python3 scripts/run_all.py`. Source and reviewed-image SHA-256 fingerprints are checked before analysis. Manual primary transcription remains an explicit input; software validation does not make it infallible.
