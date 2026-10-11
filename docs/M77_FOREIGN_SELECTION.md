# Selecting Mahadevan's West Asian finds

**Use the catalogue's 17 explicitly listed West Asian references, separating 12 named-site attributions from five unknown-provenance objects described only as probably West Asian.** These are source attributions of findspots, not evidence of manufacture abroad or a foreign language. The original excavation reports behind the catalogue citations were not independently reviewed here.

The definition is explicit in M77 printed 31/PDF 42, note 6: WA denotes Harappan inscribed objects found in West Asia. Printed30/PDF 41 assigns 9801–9905 to that section. Exact membership and site labels were visually checked in Appendix V9b, printed 829/PDF 838. The entire corresponding Texts block is printed 160/PDF 171; Introduction printed 6/PDF 17 independently separates named sites from unknown provenance.

| Source-attributed site | Exact M77 references |
|---|---|
|Susa|9801|
|Djoka (Umma)|9811|
|Kish|9821,9822|
|Ur|9832,9833,9834,9842,9845,9846|
|Telloh|9851,9852|
|Unknown provenance, probably West Asia|9901,9902,9903,9904,9905|

Do not generate missing catalogue numbers within ranges. Do not call named-site entries securely excavated merely because M77 names a site: this review authenticates catalogue attribution and bibliography, not recovery history.

## Object, side and direction codes

All 17 entries have side 0, the only inscribed side. Sixteen are object 1 (seals); 9811 alone is object 2 (sealing). All have line 0 (only line) except 9845, whose only side contains lines 1 and 2.

| References | Primary direction |
|---|---|
|9801,9903,9905|2: left to right|
|9834|9: doubtful due to damage or illegibility|
|Other entries' first or only lines|1: right to left|
|9845 second line|3: a single sign in the line|

Directions refer to seal impressions and originals of other objects. M77 displays normalized RTL lines irrespective of the actual direction code. Reversing an exported sequence merely because its metadata says 2 would be unwarranted.

The candidate export matches object and first-or-only-line direction codes for all 17. Canonical site labels are null, so missing labels cannot select this group. The primary 9845 entry has two lines with different direction codes, whereas its canonical row has one array, direction 1 and doc_count 2. Do not silently omit or concatenate the additional line.

Current strict filtering retains 9811,9822,9832,9846 among named-site attributions and 9901,9904 among probable WA. This is a damaged/doubtful/multiline/direction-filtered subset, not the complete foreign section. Sign IDs were not all reauthenticated in this metadata review.

## Domestic comparison selection

The authenticated primary ranges are 1001–1905,2002–2952,3001–3513 for Mohenjodaro; 4001–4905 and 5001–5601 for Harappa; 6104–6306 and 6402–6405 for Chanhudaro; 7001–7301 for Lothal; and **8001–8302 for Kalibangan**. The 8000 series is not foreign.

Appendix V9a, printed 828/PDF 837, supplies 33 named domestic Other Sites entries:
9001,9011,9021,9022,9031,9041,9042,9051,9061,9062,9063,9071,9073,9084,9085,9091,9092,9093,9094,9095,9101,9102,9103,9104,9111,9121,9201,9202,9203,9204,9205,9211,9221.

The broader 9001–9701 Other Sites codebook range contains **9701, unknown provenance**, described in the introduction as probably from the Indian subcontinent. Keep it separate from both named domestic sites and WA. Apply ranges only to existing records, not every integer between endpoints. The ledger includes the explicit 33-reference site map.

## Limits and evidence

This is a selection from Mahadevan's 1977 corpus of Harappan inscriptions, not all inscribed objects excavated abroad or an exhaustive Gulf corpus. Findspot, manufacturing place, language, writer identity, date and exchange function remain separate questions.

[The review ledger](../data/processed/m77_foreign_selection_review.json) retains all 17 references, primary citations and metadata, candidate filtering status, domestic selection and source fingerprints. No downloads occurred. Existing codebook images were inspected. PDF 17,171,837,838 were rendered to memory for visual review because disk writes failed; the source PDF and exact page locators permit reproduction without new image files.
