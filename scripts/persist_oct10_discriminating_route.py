"""Persist the bounded October 10 acquisition audit; no semantic assignment."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def pin(path):
    p = ROOT / path
    b = p.read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def main():
    api_paths = ["data/raw/oct10-route-hal-api-network.json", "data/raw/oct10-route-hal-api-additional.json"]
    records = {}
    for path in api_paths:
        for row in json.loads((ROOT / path).read_text())["response"]["docs"]:
            records[row["halId_s"]] = row
    assert set(records) == {"hal-05691442", "halshs-05523662", "hal-04869704", "hal-05434452", "halshs-02978545", "halshs-04365872", "halshs-05431314"}
    pdfs = {"13": "data/raw/oct10-route-chanhu-2023-2024-poster.pdf", "11": "data/raw/oct10-route-chanhu-2019-2022-poster.pdf"}
    texts = {}
    for key, path in pdfs.items():
        r = PdfReader(ROOT / path)
        assert len(r.pages) == 2
        texts[key] = r.pages[1].extract_text()
    assert all(t in texts["13"] for t in ["119", "12-15,000", "7151", "1037", "few seals"])
    assert all(t in texts["11"] for t in ["6,500", "80,000", "ste", "seals"])
    image = PdfReader(ROOT / pdfs["11"]).pages[1].images[14]
    assert image.name == "I22.jpg" and image.image.size == (537, 311)
    assert (ROOT / "results/oct10_route_poster11_seals.jpg").read_bytes() == image.data
    signs = json.loads((ROOT / "results/sign_evidence_417.json").read_text())["signs"]
    assert len(signs) == 417 and len({x["sign"] for x in signs}) == 417
    assert all(x["semantic_value"] is None and x["phonetic_value"] is None for x in signs)
    sources = []
    for meta_path in sorted((ROOT / "data/processed").glob("fetch_oct10-route-*.json")):
        meta = json.loads(meta_path.read_text())
        for key in ["path", "header_artifact"]:
            if key not in meta:
                continue
            path = meta[key] if key == "path" else meta[key]["path"]
            row = pin(path)
            row.update(url=meta["url"], research_date="2026-10-10", kind="locally_serialized_HTTP_response_headers" if key == "header_artifact" else "original_public_PDF" if path.endswith(".pdf") else "original_public_API_JSON", original_document_bytes=key == "path")
            sources.append(row)
    capture = pin("data/raw/oct10-route-web-capture.json")
    capture.update(url=None, source_urls=["https://arscan.parisnanterre.fr/membre/aurore-didier/"], research_date="2026-10-10", kind="web_tool_capture_not_original_document", original_document_bytes=False, refetchable=False)
    sources.append(capture)
    assert len(sources) == 9 and len({x["path"] for x in sources}) == 9
    (ROOT / "data/processed/oct10_route_new_sources.json").write_text(json.dumps({"sources": sources}, indent=2)+"\n")
    reports = ["CONVERGENCE", "RESEARCH_ROUTE_AUDIT", "ALL_INVENTORY_NEXT_TEST_REVIEW", "QUANTITY_ANCHORS", "SEALING_FUNCTION_ANCHORS", "EXTERNAL_NAME_ANCHORS", "HYBRID_SEAL_SEMANTICS", "DATED_DOCUMENT_BRIDGE", "INSCRIBED_WEIGHT_SEARCH", "DILMUN_WEIGHT_ANCHORS", "WEIGHT_ANCHORS", "NUMERAL_IDENTITY_SENSITIVITY", "CONSISTENT_CHAIN_RESULTS", "P453801_FOLLOWUP", "MELUHHA_NAME_POOL", "OCT10_DISCRIMINATING_ROUTE"]
    evidence = [pin("docs/"+x+".md") for x in reports]
    evidence += [pin(str(p.relative_to(ROOT))) for p in sorted((ROOT / "results").glob("oct10_route_*")) if p.is_file()]
    evidence += [pin("results/sign_evidence_417.json"), pin("scripts/persist_oct10_discriminating_route.py")]
    out = {"date_local": "2026-10-10", "conclusion": "New primary acquisition; no established sign-to-deposit or sign-to-count alignment yet", "initial_local_audit": "No new test among previously retained routes; revised after parent supplied unreviewed MAFBI sources", "search_queries": 4, "HAL_records": records, "poster11_seal_photo": {"source_pdf": pdfs["11"], "pdf_page": 2, "image_name": "I22.jpg", "dimensions": [537, 311], "depicted_faces": 2, "authenticated_independent_new_artifact_count": None, "object_ids": None, "specific_deposit_joins": None, "codes_assigned": [], "note": "Parent comparing prior 2017 image; avoid duplicate specimen counting"}, "poster13_counts": {"necklace_beads": 119, "microbeads_interval": [12000, 15000], "workshop_chips": 7151, "preforms_and_beads": 1037, "authenticated_Indus_count_text_pair": False}, "inventory": {"rows": 417, "semantic_null": 417, "phonetic_null": 417}, "new_raw_artifacts": sources, "evidence": evidence, "outreach": False}
    (ROOT / "data/processed/oct10_discriminating_route.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"raw_artifacts": len(sources), "evidence_pins": len(evidence), "HAL_records": len(records), "signs_null": len(signs)}))

if __name__ == "__main__":
    main()
