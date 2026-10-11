# BM122187: exact corpus identity, unresolved owner and find context

Audit date: 2026-09-24. **BM122187 = Gadd1932 no.2 = Mahadevan1977 reference9832.** This closes the accession gap recorded in the earlier [foreign artifact audit](FOREIGN_ARTIFACT_ANCHORS.md). It does not supply a translation. BM120573/Gadd1 and BM123208/Gadd16 are different objects.

## Primary joins and inscription

The original [Gadd catalogue](https://ignca.gov.in/Asi_data/33779.pdf), printed pp.6–7 and PlateI no.2 (PDF13,16,14), explicitly identifies museum number122187. The seal is circular, chipped on one side, made of pale steatite with a glazed surface, and has a pierced button boss. Its face has a short-horned bull with lowered head and five inscription characters above it. Gadd considers Indian manufacture possible; this is a stylistic interpretation rather than a workshop provenance.

Mahadevan's AppendixV, printed829/PDF838, lists9832 at Ur with `PBA:18(1932):p.191:No.2`. Here191 identifies the article's opening page; no.2 supplies the object-level link. The primary text drawing at printed160/PDF171 has metadata `100401` and five units. Read in the corpus's normalized right-to-left order, the sequence is:

**M254 M074 M297 M184 M003**

This is the same code sequence established in the existing primary parent review. This audit re-viewed the actual corpus row and bibliography, and the Gadd plate. It did not independently collate every cut on the stone. The plate confirms the broad circular object, bull and upper sign field, but its degraded contrast does not establish every fine allographic feature. No extra character is inserted, and neither the photograph nor its orientation is used to reverse the normalized corpus string. The code values are modern sign identifiers, not a transliteration or reading.

## What the provenance supports

Gadd says the object was obtained at Ur in the1928–29 season and that the precise place of discovery is unknown. The reviewed entry gives no excavation number, locus, building, stratigraphic layer, ancient owner, contents, accompanying named document, or parallel cuneiform inscription. The statement concerns this particular object, not the better contextualized objects elsewhere in the catalogue.

Consequently, PG1847 and its shaft fill must not be imported from BM123208. U.7683 and the cuneiform inscription must not be imported from BM120573. Acquisition in an excavation season is insufficient to establish a secure excavated context, an UrIII date, a merchant's identity, or a particular commodity.

## Museum registration lead and access limits

No accessible current official record for122187 was recovered. A targeted registration search found an indexed copy of the exhibition catalogue *India and the World* describing a circular Harappan seal and impression from Ur as `1929,1017.725`, height2cm and diameter2.5cm. This is a **candidate registration**, not an authenticated bridge to122187: the returned passage does not contain the big number, and its original page/image was not inspected. The corresponding [candidate British Museum URL](https://www.britishmuseum.org/collection/object/W_1929-1017-725) returned403. Exact-number searches did not recover its official indexed entry.

The official indexed record for the neighboring `1929,1017.726` is122188/Gadd4, a fragment. Adjacency of those numbers is useful for locating a lead but does not prove the preceding registration belongs to122187. Registration and excavation-number fields therefore remain null in the authenticated ledger. The exhibition catalogue page and museum register are concrete next sources to check.

## Semantic-anchor test

None of the reviewed evidence independently names this seal's owner or aligns its five signs to a known phrase. Parpola1994 printed132–133/PDF150–151 discusses foreign names as a future test once enough phonetic values have been established. Its named interpreter is a different object, LouvreAO22310. Its nearby round Indus seal is BM120228/Gadd17, and the Kish/Mohenjo-daro pair is another comparison. Their proximity on a printed page cannot label BM122187.

A text-layer search for the exact string122187 across Parpola's book returned no hit; this is a bounded search result, not proof that the object never appears under another label. The relevant pages were rendered and visually checked. General hypotheses about merchants, migration or local names remain hypotheses and do not provide an independently established name for M77 9832.

The defensible addition is therefore one exact museum-to-corpus join with an explicit provenance limitation. All five semantic and phonetic values remain unknown.

## Attempts and reproducibility

1. Read the existing BM120573, foreign-object and primary-corpus reviews before searching. Reused all three source PDFs; downloaded no new original source.
2. Viewed existing GaddPDF13 and16 text pages and the3600-pixel PlateI render. Re-viewed existing M77PDF171 and newly renderedPDF838. Exact page-image hashes are retained in `data/processed/bm122187_review.json`.
3. Searched exact122187, seal, Ur, Mitchell and museum domain combinations. Many hits were unrelated catalogue numbers or modern compilations placing several artifacts together; these were not promoted to evidence of ownership or translation. A current Wikipedia page no longer contained the old museum link, and the older mirror returned cache miss. No museum image was recovered.
4. Tested the candidate registration from search evidence. The official URL returned403. Search results preserve the candidate as unresolved; no access protection was bypassed.
5. Extracted Parpola's relevant text as a navigation aid and renderedPDF150–151. Poppler reported nonfatal font-cache warnings but exited0 and produced readable pages, both viewed. No new name or phonetic correspondence resulted.
6. Retained a bounded web capture with queries, selected paraphrased results and the access failure in `data/raw/bm122187_web_capture.json`; proposed source registration is separate in `data/processed/bm122187_downloads.json` for the parent to merge.

Use the existing renderer to reproduce the two new source checks:

```sh
python scripts/inspect_research_pdf.py mahadevan_1977_text.pdf --prefix bm122187-m77 --pages 838 --render-only --scale 2400 --pdftoppm /path/to/pdftoppm
python scripts/inspect_research_pdf.py umma_old_parpola_1994.pdf --prefix bm122187-parpola --pages 150 151 --render-only --scale 2400 --pdftoppm /path/to/pdftoppm
```

The saved review fingerprints sources and reviewed images separately, specifies which inferences are established or provisional, and keeps semantic anchors null. No canonical corpus data, central report, research log, source registry or manifest was edited by this subtask.
