# External material retained for the Indus investigation

Audited 17 October 2026 against `data/sources.json` and actual local file bytes.

**About 1.2 GB of distinct downloaded content**, including **58 PDF files** and
**138 image files**, plus tables, code, text and other retained responses. The blog
rounds these to nearly 60 PDFs and roughly 140 images. GB means one billion bytes.

| Measure | Files | Bytes |
| --- | ---: | ---: |
| Registered direct HTTP(S) download files | 368 | 1,231,177,647 |
| Distinct contents after SHA256 deduplication | 363 | 1,205,244,771 |
| Distinct PDF files | 58 | 828,531,907 |
| Distinct images | 138 | 288,998,589 |
| Other distinct download files | 167 | 87,714,275 |
| Separately saved web/search extraction captures | 81 | 3,533,575 |
| Separately archived HTTP responses and metadata | 113 | 182,902 |

The direct-download counts select entries in the registry's `downloads` section
with HTTP(S) source URLs, excluding explicitly local renders/crops. Each selected
file's actual byte count and SHA256 matches its registered values. Five duplicate
content groups account for the difference between 368 retained files and 363
distinct contents. PDF/image formats are identified by their file headers.

These are retained file bytes, not measured network transfer. PDF files can be
complete books or papers, excerpts or frontmatter; counts are not independent
publications or evidence units. Other downloads include landing/error responses.
The user-supplied starting dataset, locally rendered pages/crops, AI review
responses, token-accounting captures and derived experiments are excluded. Archive
contents are not added again after counting their downloaded container files.
Web/search captures and archived HTTP records are listed separately and are not
added to the 1.2 GB headline. No new source was downloaded for this audit.

Frozen per-file inventory: `results/research_data_collection_oct17_v1.json`,
including the registry hash, source URLs, file hashes, formats and exclusions.

```sh
python3 scripts/audit_research_data_collection.py \
  --report /tmp/indus-data-collection-new-audit.json
```

Use a new output path. A future inventory reflects the then-current registry;
the saved report preserves this audit's file-level evidence and exact counts.
