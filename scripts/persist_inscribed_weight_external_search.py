"""Pin a five-query external-anchor search; no value inference or central mutation."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def pin(path):
    source = ROOT / path
    return {"path": path, "bytes": source.stat().st_size,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}

def main():
    capture_path = "data/raw/inscribed-weight-anchor-web-capture.json"
    capture = json.loads((ROOT / capture_path).read_text())
    queries = [q for call in capture["calls"]
               for q in call["request"].get("search_query", [])]
    assert len(queries) == 5
    assert capture["queries_executed"] == 5
    html = (ROOT / "data/raw/inscribed-weight-anchor-h2000-4496.html").read_text()
    assert "H2000-4496/9880-01" in html
    assert "https://www.harappa.com/sites/default/files/slides/68_2.jpg" in html
    entries, ledgers = [], []
    for filename, kind in [
        ("inscribed-weight-anchor-h2000-4496.html", "excavation_project_photograph_caption_HTML"),
        ("inscribed-weight-anchor-h2000-4496.jpg", "original_linked_excavation_project_single_view_JPEG"),
    ]:
        ledger = "data/processed/fetch_" + filename.replace(".", "_") + ".json"
        record = json.loads((ROOT / ledger).read_text())
        assert record["response_complete"] and record["http_status"] == 200
        assert record["sha256"] == pin(record["path"])["sha256"]
        ledgers.append(pin(ledger))
        for obj, typ in [(record, kind), (record["header_artifact"], "locally_serialized_HTTP_response_headers")]:
            entries.append({**pin(obj["path"]), "kind": typ, "url": record["url"],
                            "resolved_url": record["resolved_url"], "http_status": 200,
                            "response_complete": True})
    entries.append({**pin(capture_path), "kind": "locally_serialized_web_tool_requests_responses_and_errors_not_original_HTTP_bodies", "refetchable": False})
    manifest = "data/processed/inscribed_weight_anchor_new_sources.json"
    (ROOT / manifest).write_text(json.dumps({"status": "pending_parent_integration", "sources": entries,
        "retrieval_ledgers": ledgers, "search_tool_error_bodies_exposed": False}, indent=2) + "\n")
    result = {
        "date": "2026-09-28", "scope": "bounded new external search, not exhaustive museum inventory",
        "queries_executed": len(queries), "maximum_queries": 5, "queries": queries,
        "batch_result_attribution": "Combined results do not identify an exclusive query for each result.",
        "qualifying_new_inscribed_weight_or_instrument_anchors": 0,
        "new_same_class_measured_inscribed_instrument_series": 0,
        "candidates": [
            {"artifact_id": "H2000-4496/9880-01", "type": "spherical agate weight with flattened side",
             "identity_in_downloaded_primary_caption": True, "photograph_inspected": True,
             "independently_recorded_mass_g": None, "ancient_Indus_signs_authenticated": False,
             "all_faces_inspected": False, "reason_not_anchor": "No mass stated and no inscription authenticated in the one shown view; unseen surfaces unknown."},
            {"artifact_id": "BM120228 / 1883,1116.1", "type": "stamp-seal",
             "indexed_official_record_mass_g": 8, "source_reports_Indus_inscription": True,
             "measurement_authenticated_against_live_page_or_original_photo": False,
             "photograph_inspected": False, "direct_page_open_status": 403,
             "reported_condition": "top of domed reverse broken", "reported_findspot": "Babylon",
             "instrument_function_authenticated": False,
             "reason_not_anchor": "A measured inscribed seal is not an independently identified weight or measure; damage and inscription-value relation unresolved."},
            {"artifact_id": "H98-3827/8447-1", "type": "limestone cubical weight",
             "evidence_level": "search extract of excavators' report, no downloaded original/photo inspection",
             "reason_not_anchor": "Weight figure item7 differs from inscribed pottery items8–10; adjacency is no same-object join."},
        ],
        "previously_reviewed_not_new": ["Susa stroke-marked weights", "Ur and Bahrain weights", "BM134301 / 1963,0715.1", "metal tool masses", "prior vessel dimensions and capacity fits"],
        "failed_accesses": [
            {"url": "https://www.britishmuseum.org/collection/object/W_1883-1116-1?selectedImageId=272276001", "via": "web.open", "status": 403, "response_body_exposed": False},
            {"url": "https://www.britishmuseum.org/collection/object/W_1963-0715-1?selectedImageId=949886003", "via": "web.open", "status": 403, "response_body_exposed": False},
        ],
        "no_outreach": True, "no_access_bypass": True, "negative_result_is_not_nonexistence": True,
        "no_values_assigned": True, "all_417_values_remain_null": True,
        "established_semantic_values": 0, "established_phonetic_values": 0,
        "new_raw_artifact_count": len(entries), "new_raw_bytes": sum(e["bytes"] for e in entries),
    }
    paths = [e["path"] for e in entries] + [e["path"] for e in ledgers] + [manifest,
        "docs/INSCRIBED_WEIGHT_EXTERNAL_SEARCH.md", "docs/WEIGHT_ANCHORS.md",
        "docs/INSCRIBED_WEIGHT_SEARCH.md", "docs/DILMUN_WEIGHT_ANCHORS.md",
        "docs/TOOL_SIGN_MASS_RESULTS.md", "docs/CAPACITY_CONTEXT_RESULTS.md",
        str(Path(__file__).resolve().relative_to(ROOT))]
    result["evidence_files"] = [pin(p) for p in sorted(set(paths))]
    output = ROOT / "data/processed/inscribed_weight_external_search.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    assert all(pin(p["path"]) == p for p in result["evidence_files"])
    print(json.dumps({"output": str(output.relative_to(ROOT)), "queries": 5,
                      "new_qualifying_anchors": 0, "raw_artifacts": len(entries),
                      "pins": len(result["evidence_files"])}))

if __name__ == "__main__":
    main()
