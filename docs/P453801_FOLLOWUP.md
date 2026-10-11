# P453801: the recovered drawing does not supply an Indus name anchor

**The exact published handcopy labels the seal “Seal illegible” and draws no
readable seal signs.** This resolves the immediate source-search question: the
available drawing cannot calibrate an Indus sign sequence against the tablet's
named recipients. It does not prove the actual seal was non-Indus or that another
image could never improve its reading.

## What was recovered

The source chain is CDLI P453801 → BDTNS192941 → Owen, *Nisaba*15/2 no.371.
The BDTNS catalogue credits the linked handcopy to Owen and CDL Press. Both parent
and image reviewer inspected the retained825×1700 JPEG. It depicts two cuneiform
tablet faces, with the explicit unread-seal legend below them; no separate seal
motif or character sequence is supplied. This is a published handcopy, not a
new photograph or autopsy. [Image search and source credit](P453801_IMAGE_SEARCH.md),
[retained handcopy](../data/raw/bdtns_192941_owen_handcopy.jpg).

The current CDLI page itself displays a no-image placeholder. Its linked
P533185/S999999 is explicitly a dummy composite record for unidentified seals.
It is not an independently identified shared physical seal, even when another
tablet links to it. The Sumerian language label for the tablet does not establish
the unread seal's script. No hypothetical Indus sequence was reconstructed from
these missing fields.

## Names and record identity require version control

The2015 CDLI revision2249158 transcribes obverse2 as `na-na-za` (Nanaza).
The current revision2289564 instead has `na-na-sa3` (Nanasa). The catalogue history
dates the later revision to2017-06-25. The old and current exports are saved
separately, and the script reports every line change without treating both
spellings as free alternatives for a name-matching exercise.

P516366 is a separate CDLI record for CUSAS40/2 no.1582. Its current obverse largely
agrees with P453801; the reverse year-name differs in damage annotations and wording.
BDTNS explicitly reports a **probable same-text identification**, attributed to
Sigrist and Ozaki, while warning that the year names appear different. CDLI gives
Šū-Suen year6; BDTNS gives year8 and a boat-related formula. This review preserves
the conflict rather than independently adjudicating the cuneiform year sign.

Therefore neither “definitely two independent tablets” nor “securely the same
physical artifact” is warranted from these records alone. The shared dummy seal
identifier does not resolve the ambiguity. Recipients of oil need not be the
person whose seal authorized its distribution. [Detailed identity review](P453801_IDENTITY.md).

## Reproducible checks

`python3 scripts/audit_p453801_anchor.py` reads the pinned JSON, ATF and HTML.
It checks object IDs and agreement between JSON-embedded and separately exported
ATF, reports differences by face and line, preserves damage and spelling, extracts
image links, and excludes explicitly generic seal records from shared-ID evidence.
The result is [the audit JSON](../results/p453801_anchor_audit.json). The four
focused tests cover unread-seal separation, preservation of doubtful spellings,
dummy-seal joins and repeated line numbers on different faces.

These program checks validate extraction and accounting, not ancient readings.
The handcopy review, possible duplication and conflicting dates remain explicitly
sourced human assessments. All downloads are in `data/raw/`, with source URLs,
byte counts and SHA256 hashes in `data/sources.json`.

## Consequence for decipherment

No known Indus inscription can currently be aligned with Nanasa/Nanaza, Samar or
Ali'aḫī through this specific tablet. The lead is **unresolved at the seal-reading
step**, not a successful bilingual and not evidence against linguistic writing.
A sharper photograph or a separately identified repeat impression would be needed
before testing any phonetic key here. Further name-based work must also freeze
which attested spelling and independently justified owner/role linkage it uses.
