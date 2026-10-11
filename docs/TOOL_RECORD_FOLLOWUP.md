# Tool photographs and original records

The follow-up authenticates the two Kalibangan artifact identities and five
visible strokes on the axe, while exposing unresolved readings and a Mohenjo-daro
catalogue-number conflict. The new evidence improves the inputs to numerical
tests; it supplies no demonstrated numerical or phonetic sign value.

## Kalibangan: exact catalogue joins

| Object | Excavation ID | Finnish text | Mahadevan reference | Primary photographs |
| --- | --- | --- | --- | --- |
| K-121, chisel | KLB2 16948 | 7080 | 8302 | CISI1 p.325; 2020 report Fig.12.2 |
| K-122, axe | KLB 14983 | 7081 | 8301 | CISI1 p.326; 2020 report Fig.12.1 |

These are object/text identifiers, not sign numbers. The [CISI1 catalogue](https://ignca.gov.in/Asi_data/76884.pdf)
on printed p.374 (PDF410) joins K-121/122 to the excavation numbers and Finnish
texts. Mahadevan's appendix printed p.828 (PDF837) independently joins the same
excavation numbers to references8302/8301. The official
[2020 excavation report](https://asi.nic.in/pdf/Excavation-at-Kalibangan-Part-II-min-1-compressed_compressed.pdf),
printed pp.768–771 (PDF70–73), supplies these numbers, photographs, dimensions
and late Period II contexts. The reviewed entries give no masses.

K-122B has five visible parallel strokes in the enlarged photographs. This
supports the visible count used by the weight hypothesis. It does not establish
that the count labels the whole object's mass, or that damaged areas never
carried additional marks.

K-121B shows an irregular bent upper form and a lower arch, rather than two clean
identical U shapes. The marks appear highlighted in the photographs; neither
their original unaltered contours nor an allographic equivalence is established.
Mahadevan's normalized B drawing instead shows two stacked arcs. Consequently,
the alternative readings 2u, 1u, and u+2i remain interpretive choices. The later
photographs do not select a numerical equation. The 1987 and2020 publications
show the same objects and matching highlighted forms; they are not two ancient
samples, and independent photographic exposures have not been demonstrated.

## Museum masses: useful candidates, incomplete identity joins

The official NMMA indexed records describe an inscribed
[chisel, GM-KAM-RJ-1391408](https://nmma.nic.in/nmma/antiqDetail.do?object=39&refId=1391408)
at210.59g and an inscribed
[axe, GM-KAM-RJ-1391390](https://nmma.nic.in/nmma/antiqDetail.do?object=39&refId=1391390)
at476.70g. Their forms, approximate dimensions and marks make them probable
matches to K-121 andK-122. However, the retrieved text omits the old excavation
numbers; direct pages timed out, and museum photographs were not inspected.
The association therefore remains provisional. A separate catalogue publication
also does not prove a separate reweighing: no weighing date or protocol was found.

As a sensitivity calculation only, substituting these candidate masses into
Pettersson's three alternative readings gives:

| Assumed chisel expression, with axe=5i | u (g) | i (g) | u/i |
| --- | ---: | ---: | ---: |
| 2u | 105.295 | 95.34 | 1.10442 |
| 1u, excluding the other mark | 210.59 | 95.34 | 2.20883 |
| u+2i | 19.91 | 95.34 | 0.20883 |

These remain two-object calibrations, not independent confirmation. Additional
decimal places do not resolve the reading ambiguity or establish weighing accuracy.
The historical210/476g model remains separately reproducible.

## Mohenjo-daro: corrected source precision and unresolved field number

The [original Mackay audit](METAL_ORIGINAL_RECORDS.md) joins the masses of Plate
CXXVI items2,3,5 on printed p.454 to the catalogue rows on p.489. The small axe
is **262.233g**, later rounded to262g. The large axe's primary field number is
**7535**, while Pettersson prints **7835**. The plate/item join is secure;
the field-number disagreement is not silently resolved. No original plate
photograph has yet authenticated the proposed numerical groups in this follow-up.

The original reports chemical separation of corroded tools and substantial weight
loss. Its suggested original chisel length above15in is a reconstruction, not a
measured complete tool. Dividing by surviving length5.22in gives a length ratio
above2.874; varying cross-sections prevent treating that as a mass ratio. The
later2.6 upper mass factor remains an added hypothesis. Imperial/metric printing
also warrants caution: a small printed ounce fraction is unclear or inconsistent
with the metric counterpart. The audit retains the literal metric observations
without claiming milligram measurement precision or silently repairing the source.

Using all three primary metric masses with the same proposed expressions gives
the chisel lower bound **453.92707g**, or at least **2.74537** times the tang mass
when t≥0. This still exceeds the assumed2.6 factor. It strengthens source
traceability, not the factual status of the reconstruction or the sign readings.

## Saved evidence and remaining test

The [Kalibangan ledger](../data/processed/kalibangan_tool_record_review.json)
preserves exact joins, visible observations, provisional museum matches, failures
and15 source/image fingerprints. The
[original-record ledger](../data/processed/metal_original_records.json) preserves
the Mohenjo-daro measurements and uncertainties.
[`audit_tool_record_followup.py`](../scripts/audit_tool_record_followup.py) verifies
the evidence hashes and produces
[`tool_record_followup.json`](../results/tool_record_followup.json) with exact
rational calculations. It runs in the offline pipeline. All downloaded originals
and web captures remain in `data/raw/`.

The subsequent [Mohenjo-daro plate audit](METAL_PLATE_AUDIT.md) authenticates the
published drawing counts while preserving the field-number conflict and the
small-axe segmentation caveat. The [numeral-convention tests](METAL_NUMERAL_IDENTIFIABILITY.md)
then compare explicit rules across all nine proposed expressions. Independent
damage restrictions and reliable sign grouping remain necessary for a decisive
weight test. No established value has been added to the417-sign index.
