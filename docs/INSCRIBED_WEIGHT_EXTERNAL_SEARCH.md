# Bounded external search for inscribed weights and measuring instruments

No new qualifying artifact was authenticated in five targeted searches. The criterion was an actual weight or measuring instrument, an exact museum/excavation identity, an independently recorded mass or capacity, and a photograph establishing ancient Indus signs on that same object. No semantic or phonetic values were assigned; all 417 values remain null.

The searches were completed on 28 September 2026. Full requests and returned text, including unsuccessful page openings, are preserved in `data/raw/inscribed-weight-anchor-web-capture.json`. Search-result snippets are discovery evidence, not a substitute for a recovered original photograph. The broad final query returned unofficial material; unofficial aggregators, Scribd copies, translation proposals and general metrological speculation were not used to establish an anchor.

## Five queries, then stop

|Number|Exact query|Domain constraint|Outcome|
|---|---|---|---|
|1|`"Indus" "inscribed weight" museum`|britishmuseum.org, penn.museum, harappa.com, mfa.org, metmuseum.org|General weights and separate inscriptions; no qualifying same-object record.|
|2|`"Harappa" "weight" "inscription" grams`|harappa.com, asi.nic.in, penn.museum|A concrete HARP agate-weight identity, H2000-4496/9880-01, followed below; other hits conflate adjacent finds or separate figure entries.|
|3|`site:britishmuseum.org/collection/object "Indus" "weight" "inscription"`|Site restriction in query|BM120228 joins inscription and measured mass, but the object is a stamp-seal. The already-reviewed BM134301 foreign duck/goose weight also resurfaced.|
|4|`site:harappa.com "scale" "inscribed" ivory Lothal`|Site restriction in query|Excavation figures with modern scale bars and separately described inscribed objects; no identified inscribed measuring instrument with calibrated value.|
|5|`"Harappan" "inscribed weight" museum -site:harappa.com`|No positive domain constraint|Broad synthesis and foreign-weight leads; no new original excavation or museum record satisfying the artifact-level criteria.|

The web tool returned combined results for each batch, not a per-query attribution. The outcomes summarize the relevant batch leads and are not counts of results assigned unambiguously to individual queries. Following returned sources used page openings and direct retrieval, with no additional search query.

## Exact fresh leads checked

**H2000-4496/9880-01.** The [HARP photograph caption](https://www.harappa.com/slide/spherical-agate-weight-one-side-flattened) identifies a spherical agate weight with a flattened side and describes it as outside the standard Harappan weight system. The caption supplies no mass and reports no inscription. The caption HTML and its directly linked original JPEG were downloaded successfully and retained. The small single photograph shows a rounded translucent stone and pale surface flecks; it does not authenticate a readable ancient Indus inscription. No statement about all unseen surfaces follows. The modern photographic scale is not an ancient measuring instrument or an independently recorded mass. The author's proposed international-trade explanation is not adopted as a sign interpretation. This closes a concrete fresh lead at the published-record level, while leaving unphotographed surfaces and unpublished measurements unknown.

**BM120228 / 1883,1116.1.** The [official British Museum record](https://www.britishmuseum.org/collection/object/W_1883-1116-1?selectedImageId=272276001), as returned by the search index, describes a circular steatite stamp-seal bearing an Indus inscription above a bull and records a mass of **8 g**. It gives Babylon as findspot and reports the domed reverse broken. This is an exact object-level mass/inscription lead, but its type is explicitly a **stamp-seal**, not a weight or measuring instrument. The indexed record supplies no independent reason to equate the inscription with its present mass, and damage prevents casually treating the measurement as original intact mass. Direct opening returned HTTP 403, so neither the live page nor its photograph was authenticated in this follow-up. The indexed metadata are preserved as an excluded lead, not a new metrological anchor. No repeated access or restriction bypass was attempted.

**Other concrete but ineligible hits.** The excavators' [1999 Harappa report](https://www.harappa.com/sites/default/files/pdf/Kenoyer1999_Harappa%20New%20Discoveries%20on%20its%20origins%20and%20growt.pdf), in the search extract, lists limestone weight H98-3827/8447-1 as figure item 7 and pottery inscriptions separately as items 8–10. Their adjacency supplies no same-object join. The HARP plan listing a sealing, elephant seal, inscribed sherds and limestone weight likewise describes different finds. These were not downloaded or advanced to primary photograph review after failing the elementary identity criterion.

## Previously known cases and access limits

The reviewed starting files were `WEIGHT_ANCHORS.md`, `INSCRIBED_WEIGHT_SEARCH.md`, `DILMUN_WEIGHT_ANCHORS.md`, `TOOL_SIGN_MASS_RESULTS.md` and `CAPACITY_CONTEXT_RESULTS.md`. The Susa stroke-marked weights, Ur/Bahrain objects, uninscribed excavation weights, measured metal tools, incomplete vessel dimensions and unsecured capacity fits remain prior work; none is counted as a discovery here. The newly surfaced official BM134301 record is the same foreign duck/goose object already excluded. Its direct page opening also returned 403. No claim about its historical marks is needed for this result.

The search did not yield multiple same-class qualifying instruments, a calibration curve or a sign-value test. It does not establish that such objects never existed or that no museum holds one. Search indexing, record completeness, image resolution, single-view photography and inaccessible pages limit the result. The absence of a `WEIGHT` label in the secondary corpus is not used as evidence of archaeological absence. A future exception would need a new exact artifact record satisfying the criteria above; another measured uninscribed weight or a nearby seal would not resolve the gap.

## Reproducibility and research log

`scripts/persist_inscribed_weight_external_search.py` writes `data/processed/inscribed_weight_external_search.json`, checking the five-query limit and the exact downloaded HARP identity, and pins this report, the prior reviews, source captures, fetch ledgers and script. `data/processed/inscribed_weight_anchor_new_sources.json` is a separate pending manifest. All five new raw artifacts—caption HTML, original JPEG, two locally serialized HTTP-header records and one web-tool capture—are together in `data/raw/` under the requested prefix. The capture includes both 403 failures; the tool did not expose their response bodies, so no original error-body bytes are claimed. No central registry or frozen prior review was edited.
