# M-294 room and hoard context review

Reviewed 2026-09-25. This independent archaeology review tests the room association used in Mukhopadhyay's 2025 IRC bulletin, §3.1 (PDF 14–16). It does not infer a sign meaning. The parent review handles CISI photographs and inscription completeness.

The original report directly associates seal 376 with the jewellery find in Room 8, House VIII, HR Area. The strongest justified description is **a seal in a subsurface jewellery and scrap hoard, plausibly belonging to a goldsmith**. The report does not establish a working jeweller's shop in the room. This is a stronger contextual association than matching objects only by square, but it remains a single assemblage and does not distinguish personal identity, ownership, profession, institution, commodity or administrative message.

## Primary evidence checked

| Source | Image | Observation |
|---|---|---|
| Marshall 1931 I, p.189 | [Archive leaf231](../data/raw/m294_marshall722_leaf231.jpg) | Block 2 is divided into houses V–XIII. Six houses other than V, IX and X are described as Late Period structures incorporating earlier walls. |
| I, p.193 | [leaf235](../data/raw/m294_marshall722_leaf235.jpg) | House VIII measures 54×37 ft externally, about a dozen rooms; none paved. Passage7 from courtyard2 gives access to room8. |
| I, p.194 | [leaf236](../data/raw/m294_marshall722_leaf236.jpg) | Room8 measures8×7 ft internally. Find was immediately beneath its floor. Jewellery, silver vessels, copper vessel with implements, and other items are listed. Fragmentary seal, plateCXII376, is expressly included with the find, along with a chert scraper. Three pictographs are described. |
| II, p.376 (PDF27) | [render](../results/primary_pages/m294-vol2-p376.png) | Seal376 is HR4212e, typeB; upper fabulous animal has elephant trunk, lower register has elephant. Exact original excavation/plate identity is supported. |
| II, p.493 (PDF144) | [render](../results/primary_pages/m294-vol2-p493.png) | Silver vases CXL2 HR4212d and CXL3 HR4212c, depth6 ft below surface. Both contained gold ornaments and stone beads; much gold was scrap. Larger lid upside down. Associated metal vessel and implements explicitly from Room8, HouseVIII, Block2, HR. |
| II, p.522 (PDF173) | [render](../results/primary_pages/m294-vol2-p522.png) | Hoard No.3, jewellery find HR4212a, Room8 HouseVIII Block2 SectionB, depth6 ft below surface. Majority of beads loose in soil with evidence of former cloth wrapping. Original author judges probable goldsmith property because of waste metal and rolled-up ornaments retained for remelting. |

The printed p.194 list is entirely on one page. Page195 begins a continuation about the superficially excavated area **south of House VIII**, including another seal HR5193/306; it is not a second seal from Room8. Page195 was checked by Archive page-linked OCR only; no image obtained. Do not pool this southern-area seal with Room8 or infer exhaustive room inventory from the singular seal reference.

The HouseVIII pottery-kiln reference in p.195–196 vicinity should also not be casually used as goldsmith production evidence: the explicit kiln discussion and courtyard17 on p.193 concern **House VII**. No furnace or floor-based jewellery manufacturing installation is described for Room8 on the reviewed pages.

## Implications and limits

The 2025 paper's room assemblage claim has a real primary foundation. Its stronger wording, that this was undoubtedly a place of making and selling jewellery, exceeds the context actually described. The find was beneath the floor, not reported as an in-use work surface. The original goldsmith attribution is itself explicitly probabilistic, based on recycling stock. Production ownership and retail activity are different claims. The report's inventory supports broken/rolled ornaments and scrap; calling these all unfinished production pieces is not warranted by these pages.

The silver-vessel catalogue reports contents, while the jewellery chapter says most beads were loose in soil. These descriptions allow contents plus external/wrapped material; they should not be flattened into either “everything inside sealed jars” or “everything loose on a shop floor.” The seal is associated with the find, but these passages do not place it inside a specific container. Deliberate hoarding is the original interpretive category; it does not independently prove occupation of the room, the owner of the seal, or the seal's function.

Primary Block2 agrees across I,p189 and II,pp493,522. The secondary CSV entry's Block1, reported by the parent, therefore conflicts with these primary references. Preserve the raw value and record a source-based overlay; do not silently rewrite the export. The depth is below the then-excavated surface, not an absolute elevation. Late Period is the excavation report's phase assignment, not a independently recalculated absolute date.

This review supports retaining M-294 as **goldsmith-associated hoard evidence**, conditional on the independently verified CISI alias. It cannot identify which of the inscription's three signs, if any, encodes profession, gems, ornaments, ownership, tax or a personal name. No semantic/phonetic value is assigned.

## Reproduction and attempts

- Existing volumeII source was reused. Internet Archive title search located volumeI identifier `in.ernet.dli.2015.722`.
- Retained catalogue search, item metadata, OCR TXT, OCR XML and scandata under `data/raw/`. The scandata contains no printed-page labels, so OCR XML page objects were used to map printed194 to leaf236. A supplementary Archive scrape query did not solve pagination; retained as a navigation attempt.
- Downloaded leaf236 first. Parallel downloads for leaves235 and237 failed with connection resets and yielded no saved files. Retrying235 succeeded. Leaf237 was not redownloaded because194 held the substantive find; its OCR remains available. Leaf231 was obtained to confirm Block2 visually.
- Rendered already-retained volumeII PDF pages27,144,173 at scale2600 using bundled `pdftoppm`; inspected all three and the three downloaded volumeI images.
- [Extraction script](../scripts/extract_m294_room_sources.py) persists eight page-linked OCR extracts in [result JSON](../results/m294_room_source_extracts.json). OCR is navigation evidence, not an authoritative transcription.
- Nine new source entries, with byte counts and SHA256, are supplied in [registry merge file](../data/processed/m294_room_new_sources.json). No concurrent edits to central registry were made by this reviewer.
