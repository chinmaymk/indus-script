# Chanhudaro public-records follow-up

28 September 2026. Five targeted search queries were issued and searching then stopped. No publicly readable fieldcard or independently maintained accession-linked record for **CH2428, CH2285, CH2529CC, CH3215 or CH3207** was located in this bounded pass. This is a search outcome, not evidence that records do not exist or cannot be digitized. No person was contacted, request submitted, account used or restriction bypassed.

## Identifier clarification

The original CISI1 key, printed p366/PDF402, defines **HU** as Helsinki University, Department of Asian and African Studies, and identifies photographs taken by Eija Lahdenperä for the CISI project. Column 4 supplies the holding museum and registration number; column 5 supplies photograph sources. Accordingly, **HU817** for C17/CH3207 and **HU804** for C22/CH2285 are photographic-source identifiers, not evidence the objects are held in a museum called HU. Their ASI entries, **63.12.29** and **63.12.16**, remain distinct museum-registration identifiers. This clarification was verified from the retained primary key crops and PDF, with no new download.

## Sources actually found

Penn's official collections website contains an independently maintained object page for **L-141-177**, a Chanhudaro seal, with an MFA number **36.0967** and two field numbers, **3051 and 2558**, under the same “Other Number” heading. It cites both Mackay LI.24 and LII.12. None of the five target field numbers is listed. This demonstrates a public museum record beyond a finding aid, but does not resolve a target's deposition. The dual field-number association is preserved as written, not treated as proof that the two excavation objects are identical. No underlying card, acquisition-document image, locus or elevation was supplied by the readable page. [Official Penn object record](https://collections.penn.museum/collections/object/329820).

The live Penn archive index again lists collection **1064, Chanhu-daro Pakistan records**. Its linked direct finding-aid URL is `https://collections.penn.museum/collections/archives/findingaid/552839`; following that link produced a web-tool cache-miss error. A separate search result for the Gregory L. Possehl papers mentioned Chanhudaro object/seal material, but opening its finding-aid page timed out. These are navigation failures, not evidence of unavailable physical records or missing archival contents. [Official archive index](https://collections.penn.museum/collections/archives/).

The earlier [Penn 1064 finding aid](https://findingaids.library.upenn.edu/records/UPENN_MUSEUM_PU-MU.1064) remains the concrete holding locator documented in `CHANHU_FIELDCARD_ARCHIVE_SEARCH.md`. This follow-up did not inspect individual cards or supersede that review. A broad Penn collection result for a cart wheel and an unrelated Ur record containing “field card” were rejected as target matches. Indian museum search results likewise returned unrelated objects and administrative/educational pages. No applicable MFA object result was returned in the fifth-query batch; this does not establish an exhaustive MFA catalogue search.

## Exact search log

1. `("Chanhu-daro" OR Chanhudaro) ("2428" OR "2285" OR "2529" OR "3215" OR "3207")`, restricted to `penn.museum`, `collections.mfa.org`, `harappa.com`, `nationalmuseumindia.gov.in`, `asi.nic.in`. The first whitelist inadvertently included the non-museum site `harappa.com`; no result from that domain was opened or used. No relevant exact-number object record was returned.
2. `("63.12.16" OR "63.12.29") seal`, restricted to `asi.nic.in`, `nationalmuseumindia.gov.in`, `indianculture.gov.in`, `museumsofindia.gov.in`. Returned unrelated government/museum results; no authenticated target accession record.
3. `("Chanhu-daro" OR Chanhudaro) ("object card" OR "field card" OR "register") digitized`, restricted to `penn.museum`, `library.upenn.edu`, `archives.upenn.edu`, `collections.mfa.org`. No target card content located. An Ur flute page's discussion of a field card was unrelated.
4. `Chanhudaro`, restricted to `collections.mfa.org`. No relevant MFA object returned in the retained batch response.
5. `"Chanhu" seal`, restricted to `collections.penn.museum`. Located the unrelated-but-relevant-to-method L-141-177 object page, archive index and other navigation results described above.

Queries 1–3 and 4–5 were batched; the full returned results are retained, rather than claiming an exact per-query result allocation where the tool did not label it. After these five queries only the three directly relevant official URLs and the archive-index link were opened; no further search was performed.

## Preservation and limits

`data/raw/chanhu-public-records-web-capture.json` preserves the complete returned search/open/click tool responses and exact submitted queries. It is explicitly a **serialized web-tool capture**, not original website HTML or an HTTP-body download. The separate `data/processed/chanhu_public_records_new_sources.json` manifests that distinction and the source URLs. The main review JSON pins this capture, the earlier archive review and the primary CISI key sources.

No target identity, fieldcard content, depositional bridge, sign assignment or statistical result changes. The remaining concrete research need is the individual card/register/site-level evidence already located archivally, not a new interpretation of a photograph identifier.
