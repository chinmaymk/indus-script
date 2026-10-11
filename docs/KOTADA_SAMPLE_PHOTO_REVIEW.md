# Kotada sample photographs: limited visual coverage, no inscription anchor

This bounded follow-up recovered original publisher images and supplementary sample tables from the [2020 Scientific Reports paper](https://www.nature.com/articles/s41598-020-72963-y), published 30 September 2020. **No authenticated inscription-to-residue join was recovered.** Actual photo views of KB225 were inspected; definite script is not identifiable at the supplied image resolution. That is not evidence that the entire sherd or its original vessel lacked inscriptions. The 2024 Figure 2 pixels remain unseen.

The earlier [follow-up](KOTADA_BHADLI_ANCHOR_FOLLOWUP.md) established that the 2024 paper selected eleven samples from earlier lipid work and explicitly cited 2019/2020. Its Table 1 names KB48, KB61, KB69, KB106, KB136, KB154, KB156, KB167, KB171, KB215 and KB225; its Figure 2 caption names KB61 and KB154. Matching labels in the explicitly cited predecessor study support publication-sample continuity, but do not furnish an excavation-register crosswalk, all-face documentation or independent physical-object identity. The 2020 methods describe collection during 2011–12 and 2012–13; the earlier reviewed 2024 passage described 2011–12. These source-specific descriptions remain separate.

## Image inspection

The publisher's [Figure 4 image](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-020-72963-y/MediaObjects/41598_2020_72963_Fig4_HTML.png), retained as `data/raw/kotada-sample-photo-2020-fig4.png`, is a 685 × 410 pixel plate. Most entries are reconstructed vessel profiles, with a legend distinguishing wares. They are not documentary photographs of entire surfaces. Six target IDs appear as profiles: KB69, KB106, KB156, KB167, KB171 and KB215. KB225 has two small photographic views with a profile; KB173 also has photo views but is outside the eleven-sample target set. KB48, KB61, KB136 and KB154 are not depicted in this plate.

No definite script is identifiable in the displayed KB225 or KB173 photo views. The photographic areas occupy only small parts of this already small plate; neither all surfaces nor missing vessel portions are recorded. Painted bands, section outlines, profile hatching and modern labels cannot be treated as ancient signs. No sign sequence was transcribed and no absence label was assigned. Native crops, without enlargement, are `results/primary_pages/kotada-sample-photo-kb225.png` and `kotada-sample-photo-kb173.png`; their coordinates and source hash are in the review JSON.

The [Figure 3 image](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-020-72963-y/MediaObjects/41598_2020_72963_Fig3_HTML.png) contains chromatograms, not sherd photos. [Supplement 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-020-72963-y/MediaObjects/41598_2020_72963_MOESM2_ESM.jpg) is an isotope scatterplot, also not surface photography. Neither supplies a new inscription reading.

## Exact sample-table evidence and disagreements

The original [Supplement 1 DOCX](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-020-72963-y/MediaObjects/41598_2020_72963_MOESM1_ESM.docx) is retained unchanged. Its two tables have 61 and 23 XML rows respectively, including headers; its ZIP contains no embedded media. The extraction script preserves target cells, paragraph boundaries and one-based XML table/row addresses. These are XML locations, not rendered page numbers. Ten of the eleven 2024 sample labels occur in S1.

- **KB61:** no exact entry occurs in S1 or S2. KB60 occurs separately (S1 XML row 19; S2 row 2). The 2024 Table 1 and Figure 2 caption say KB61. This review does not substitute KB60, infer a typo, or merge physical samples.
- **KB106:** S1 XML row 31 records aquatic fat and dashes for isotope values. S2 XML row 3 instead gives −19.1, −24.9 and −5.8‰ with a dairy classification. Figure 3b's caption names KB106 as possible aquatic fat, while the discussion says the one aquatic sample was excluded from isotope analysis. These are conflicting published entries; the review preserves both without selecting values or inventing a corrected label. The supplementary scatterplot does not resolve this identity conflict.

Sample-to-analysis continuity is therefore partly traceable, but an inscription inventory and sample-to-field-object bridge remain missing. Chemical classifications, profile drawings and unmarked-looking small views do not identify a sign's referent.

## Bounded attempts and reproducibility

Exactly four targeted searches were used, all retained in `data/raw/kotada-sample-photo-search.json`:

1. `"Kotada Bhadli" "KB-61" "KB-154"`
2. `"Assessing the applicability of protein residues" filetype:pdf -site:researchgate.net -site:sciencedirect.com`
3. `"10.1016/j.qeh.2024.100038" supplement OR pdf -site:researchgate.net -site:sciencedirect.com`
4. `Chakraborty 2019 Subsistence Based Economy Kachchh thesis Toronto repository`

No 2024 photo file or 2019 thesis file was recovered through those searches. Subsequent navigation followed the explicitly cited 2020 DOI and exposed publisher links. Web-tool figure and supplement clicks produced cache/internal errors; the supposed S1 anchor led back to the article. The complete retained publisher HTML then exposed actual CDN image and supplementary-file URLs, whose ordinary HTTP downloads succeeded. A first sandbox fetch failed at DNS without receiving a body; its metadata is retained separately from the successful authorized network fetch. This was not a retry of a publisher denial: the earlier blocked 2024 ScienceDirect and ResearchGate routes were not revisited or bypassed. No author was contacted.

All downloaded bodies, response headers and tool captures are together under `data/raw/kotada-sample-photo-*`. `data/processed/kotada_sample_photo_new_sources.json` lists 12 new raw artifacts with byte lengths, SHA256, URLs and source kinds. The detailed review at `data/processed/kotada_sample_photo_review.json` includes all eleven sample records, table cells, source conflicts, failure records and crop pins. Reproduce local extraction and crops with `scripts/build_kotada_sample_photo_review.py` using Python with Pillow. The script performs no network calls and verified all raw-source and crop pins. Earlier frozen reviews and central files were not edited.
