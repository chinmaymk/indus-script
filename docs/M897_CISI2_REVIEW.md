# M-897: recovered original and impression

Date: 2026-09-27. **CISI2 now independently verifies M-897 = DK9111 and supplies a larger original-seal photograph plus an impression.** This closes the modern-alias gap in the earlier review. It does not, by itself, settle the fine distinction between the secondary W550 transcription and the M222 normalized drawing.

## Identity and sources

The authenticated *Corpus of Indus Seals and Inscriptions, 2: Collections in Pakistan* (1991), printed436/PDF471, explicitly lists M-897, Finnish2545, excavation **DK9111**, museum **MD446**, and photographs **JL589; a: P368**. The key at printed434/PDF469 defines MD as Mohenjo-daro Museum's old accession numbering, JL as Jyrki Lahtinen, and P as S. M. Ilyas's photographs for the CISI project. Thus MD446 is a published historical accession, not a newly checked present-day custody claim.

The [metadata crop](../results/primary_pages/m897-cisi2-metadata.png) preserves the row and parts of its neighbours. The [full photographic page](../results/primary_pages/m897-cisi2-photo-120.png), printed85/PDF120, explicitly labels the two views M-897 A and M-897 a. The labels, excavation row and column key provide the join; text resemblance is not the sole identity criterion.

Earlier original excavation evidence already links **FEM545 = DK9111**. Mahadevan's explicit FEM2–704 → 2002–2704 appendix rule supplies **FEM545 → M77 text2545**. That remains the M77 identity basis. Equality of Finnish2545 and M77 text2545 is not substituted for the explicit rule: CISI2's key warns that the numbering systems can differ. The historical reviews remain unchanged and are superseded only on the specific newly inspected fields.

## Direct photographic observations

The [original](../results/primary_pages/m897-cisi2-original.png) and [impression](../results/primary_pages/m897-cisi2-impression.png) show the same five broad groups in opposite spatial order: an enclosure with an internal mark, two strokes, a capped fish-like form, a crossed form, and a comb-like form. Opposite spatial order is expected for seal and impression; it is not a new inference about reading direction. These are two views of one artifact.

The crossed form and its bent ends are appreciably clearer than in the small FEM plate. Surface texture, lighting and worn/irregular upper edges nevertheless affect the fine line ends near the comb and top border. The photograph supports a comparison with the normalized M222 drawing, but the parent review does not independently certify an exact W555 reassignment or reconstruct a stroke that is no longer securely visible. Nor does it certify the raw W550 as a distinct intact ancient form. The earlier normalized M77 line still explicitly depicts M222; that is a claim about a catalogue transcription.

Both new views show the lower boundary intersecting the animal motif, with only the head/neck area remaining below the inscription. This strengthens the reading of the object as a fragment over the old isolated impression cutout alone. It does not locate a break that specifically removed the diagnostic stroke of the crossed sign. No reverse or side view of M-897 appears on this page, and no physical autopsy or exact condition grade is claimed. The raw preservation=`fragment` and complete=`Y` fields remain separate and unchanged.

## Consequence for the model comparison

The [earlier sensitivity analysis](PINCER_MAPPING_SENSITIVITY.md) keeps the M-897 raw W550 versus normalized M222 pair separate from the better-supported local W550/M216 and W555/M222 core. The new source strengthens artifact identity and improves the image evidence; it is not permission to silently recode the secondary corpus or remove the exception so a preferred rule fits. The frozen [catalogue constraint audit](CATALOGUE_CONSTRAINT_MODELS.md) and its counts remain unchanged. No global sign equivalence, meaning or sound is established.

## Attempts and reproduction

The retained CISI2 OCR did not produce a useful M897/9111 locator. The contents identified the Mohenjo-daro photo section. PDF110 showed M837–841 and PDF130 showed M973–982; PDF119 narrowed the location to M889–892. Rendering PDF120 and121 found M897 on120, while121 is the adjacent M899–906 page. These non-target renders are retained as part of the search record.

`inspect_research_pdf.py` rendered metadata471 at scale4000 (prefix `m897-cisi2-meta`), locator110/130 at1800 (`m897-cisi2-locate`), locator119 at2400 (`m897-cisi2-narrow`), and photo120/121 at4400 (`m897-cisi2-photo`). [The crop script](../scripts/render_m897_cisi2_crops.py) records fractional coordinates and performs no line restoration, sharpening or contrast manipulation. No new download was needed: all work reuses the retained CISI2 PDF in `data/raw/`. A separate source-exposed independent visual review accompanies this report; neither review is a blind validation test.
