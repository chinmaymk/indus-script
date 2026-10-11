# H-1923 bounded acquisition follow-up

Research date: 2026-10-10. Eight targeted searches recovered no authenticated photograph of H-1923 / H94-2217 or original Figure28.01. This is a bounded acquisition failure, not evidence that the report or image is unavailable everywhere. No numerical or semantic assumption changes.

The new acquisition is the [original Ars Libri catalogue PDF](https://www.arslibri.com/collections/PossehlLibrary1.pdf), dated 13 April 2012. Its printed/PDF p90, entry1212, describes the combined 238-page Harappa1994–1995 preprints. This differs from the prior Scribd capture's entry1276/p94; those older locators must not be transferred to this version. Entry1276 here concerns Moorcroft and Trebeck.

Printed/PDF p76, entry987, describes a bound compilation with two components titled Harappa Excavations1994: one with 34 pages, four tables and 22 plates; another with 40 pages and 23 plates. Their relationship is unresolved. Printed/PDF p35, entry375, lists CISI3.1 within the three-volume set. These are historical bibliographic locators, not report images, current holdings or proof that either version contains Figure28.01.

The eight exact queries and complete tool returns are preserved in `data/raw/oct10-h1923-web-capture.json`. Searches found familiar bibliographies and the already inspected 1997/2010 extracts; their denied downloads were not retried. Unrelated H1923 archive files and Indian excavation reviews were excluded. No full CISI3.1 scan or original report link emerged. This follow-up stops rather than expanding generic searches.

The public catalogue download initially failed DNS resolution without receiving bytes. The authorized retry succeeded with HTTP200; both attempt records remain in `data/processed/`. All new source bytes are in `data/raw/`, including locally serialized response headers. No outreach, purchase or restricted access occurred.

Run `scripts/audit_oct10_h1923_acquisition.py` to verify the catalogue page count and locator text, extract the four relevant pages, and regenerate the typed three-artifact source manifest. The resulting `data/processed/oct10_h1923_acquisition.json` pins seven inputs and retains primary image, report and identity authentication as false. Original report pages remain the necessary acquisition; this catalogue cannot establish the stroke counts or face pairing.
