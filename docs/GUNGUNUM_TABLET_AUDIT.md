# YBC 5447: a dated mercantile tablet, not an Indus bilingual

Audit date: 2026-09-24. The exact tablet is **YBC 5447**, published by William W. Hallo in *Assyriological Studies* 16 (1965), pp. 199–203, with Buchanan's seal discussion pp. 204–209. The modern [ARCHIBAB record T24413](https://archibab.fr/texte/24413) explicitly links it to **CDLI P306518**. This last identifier is verified as an outgoing catalogue link; the CDLI object page itself could not be retrieved. Buchanan's 1981 catalogue 1090 is audited independently in the companion Yale seal report.

The primary publication is saved as [AS16](../data/raw/gungunum_as16_1965.pdf), downloaded through the [publisher's current page](https://isac.uchicago.edu/publications/studies-honor-benno-landsberger-his-birthday). Printed pp. 200–203 correspond to PDF pages 220–223. All four were rendered and visually inspected; p. 201 is the labeled tablet handcopy. This is checking the printed edition and drawing, not a new cuneiform collation of the original artifact.

## People and their roles

| Person | Primary reading / role | Connection to seal |
|---|---|---|
| Luma'a | `Lú-má-a-a`; consignor / silent partner | No explicit seal-owner statement |
| Hatin-Ibanum | `Ha-tin-ᵈI-ba-nu-u[m]`; active partner receiving goods | Hallo p. 202 infers that the impressions probably belong to the obligated partner |
| Apkallum | `Ap-ka-lu-um`; father of Hatin-Ibanum | Patronymic in the cuneiform tablet, not in a paired Indus inscription |
| Ur-Shulpa'e | `Ur-ᵈšul-pa-è`; seer, witness | Witness role only |
| Erishti-ili | Partly restored name `[E-r]i-iš-ti-ì-lí`; fishermen's foreman, witness | Witness role only; beginning restored by available space |

The original names are transcriptions in Hallo's edition. His divine determinative in Hatin-Ibanum is not the syllable *il*. Later alternative analyses must not be silently substituted into the original transcription. Hallo pp. 202 and n. 32 discusses etymological uncertainties; these do not establish the speaker's ethnicity or language, much less an Indus sound value.

The contract concerns **4 talents of wool, 2 GUR wheat, and 2 GUR sesame**. Hallo prints his tentative identification of the wool grade with a question mark. His receipt predicate is editorially supplied, the clearance term begins with restored `[t]`, and the last year-name signs are restored/emended. The text obligates the recipient to provide clearance after the journey. The two witnesses and legal structure support Hallo's interpretation of a partnership being established. No conversion to modern mass or volume is used here.

## What this establishes—and what remains inference

The tablet's year name dates it to **Gungunum year 10**, conventionally 1923 BCE in Hallo's stated middle chronology. The edition has month II, **day 20**. ARCHIBAB's live header and Charpin's 2020 table p. 50 instead give **day 2**, while ARCHIBAB's own transliteration line 14 has `U₄ 20.KAM`. The conflict is retained; the visible primary edition supports day 20. No claim of an independent corrected day-2 collation is justified.

Hallo explicitly reasons from typical sealing practice to Hatin-Ibanum as the likely seal owner. A name on the tablet is therefore a **role-based owner hypothesis**, not an independently labeled owner on the seal. His proposed Ur provenance is likewise based on textual parallels and chronology; the current database's Ur fields do not transform it into an excavated findspot. Gulf destination is an interpretation of the commodities and seal style, not an explicit place name in this contract.

ARCHIBAB calls the impressions **uninscribed** (*anépigraphes*) and compares their style with Failaka seals. This provides a direct catalogue reason against treating this tablet as a bilingual Indus–cuneiform text. A drinking scene or other emblem cannot be assigned one of the tablet's names or commodities merely because it appears on the same artifact. No Indus sign sequence is authenticated here, and **zero semantic or phonetic values are assigned**.

ARCHIBAB's wording refers to two impressions; Buchanan 1981 describes impressions on several surfaces. These statements may differ in counting scope. Neither the phrase nor the plural is proof of two distinct seal dies. The other agent's seal-image audit preserves the fuller impression count and Failaka comparison.

## Retrieval and research log

1. Searched Gungunum, Buchanan 1090 and YBC 5447. Yale's indexed catalogue concordance associated 1090 with 5447. Exact CDLI searches initially found no record; this negative search was not treated as nonexistence.
2. Located the primary AS16 volume. Initial sandbox curl failed DNS. Authorized network retry succeeded but returned publisher HTML, not a PDF. Renamed that actual response `gungunum_as16_redirect.html`, retained it, and followed the PDF link embedded in it. The current S3-hosted publisher PDF downloaded successfully (45,022,472 bytes).
3. Extracted relevant pages and visually inspected PDF 220–223. Confirmed recipient, patronymic, witnesses, restoration marks, quantities, and explicit owner-inference wording. Shared source and page references with the parent and the Yale-seal agent.
4. Search found Charpin's ARCHIBAB4 (2020) table p. 50, which points to T24413. Downloaded the volume (15,455,227 bytes) and inspected p. 50 image. Confirmed the day-2 entry and exact record pointer. An initial extraction loop overwrote its excerpt with the last matching page; replaced it with an explicit multi-page extraction (50,57,347,348,549). The original source was unaffected.
5. Web reader could not open T24413; curl returned a 1,476-byte JavaScript application shell. Opened the public record through computer-use UI successfully, without login. Saved a clearly labeled bounded transcription/paraphrase in `gungunum_archibab_ui_capture.json`, retaining query and resolved URLs. The UI supplies museum number, CDLI link, full transliteration, editorial history, and the uninscribed-seal note. This capture is not represented as original HTML or a full page export.
6. Following the CDLI link did not navigate the current tab. A new-tab attempt failed with an in-app browser visibility limitation; direct navigation then timed out. Web opening of `https://cdli.earth/P306518` also failed, and a 30-second curl timed out with zero bytes. No CDLI HTML/image is claimed or registered. The P-number remains verified through ARCHIBAB's explicit link only.
7. USC's indexed Non-alphabetic Cuneiform Texts list supplied an additional lead, ISF_TXT_01101, with the matching Hatin-Ibanum/Luma'a summary. Its museum-number join was not verified; no additional identity is asserted from it.

All five files acquired or captured by this task are in `data/raw/`. Proposed registration, exact SHA256 hashes, source fingerprints and reviewed images are in [download records](../data/processed/gungunum_downloads.json) and [structured review](../data/processed/gungunum_tablet_review.json). No central corpus or sign interpretation was changed.
