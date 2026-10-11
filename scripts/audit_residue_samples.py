#!/usr/bin/env python3
"""Inspect published residue sample metadata without assigning Indus meanings."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def docx_tables(path):
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    return [[["".join(cell.itertext()) for cell in row.findall("w:tc", NS)]
             for row in table.findall("w:tr", NS)]
            for table in root.findall(".//w:tbl", NS)]


def main():
    review_path = ROOT / 'data/processed/residue_anchor_audit.json'
    review = json.loads(review_path.read_text())
    for evidence in review['evidence_fingerprints']:
        assert hashlib.sha256((ROOT / evidence['path']).read_bytes()).hexdigest() == evidence['sha256'], evidence['path']
    path = ROOT / "data/raw/residue_suryanarayan_data.csv"
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
        fields = reader.fieldnames
    sites = ["ALM", "MSDVII", "MSDI", "LHRI", "KNK", "FRN", "RGR"]
    archaeological = [row for row in rows if row["Site_name"] in sites]
    tables = {str(i): docx_tables(ROOT / f"data/raw/residue_ghosh_2025_si{i}.docx")
              for i in (1, 2, 3)}
    result = {
        "scope": "Published sample metadata and manually documented visual audit; not a decipherment",
        "review_sha256": hashlib.sha256(review_path.read_bytes()).hexdigest(),
        "csv_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "csv_total_rows": len(rows),
        "csv_archaeological_rows": len(archaeological),
        "csv_other_rows": [{"site": r["Site_name"], "sample": r["Sample"]}
                           for r in rows if r not in archaeological],
        "csv_site_counts": dict(Counter(row["Site_name"] for row in rows)),
        "csv_fields": fields,
        "csv_inscription_named_fields": [f for f in fields if any(w in f.lower() for w in
                                                                ("inscri", "graffi", "sign", "glyph"))],
        "csv_not_full_172_sample_inventory": True,
        "ghosh_supplement_tables_literal": tables,
        "ghosh_main_sample_rows": {"karanpura": len(tables["1"][0]) - 1,
                                   "ropar": len(tables["2"][0]) - 1},
        "authenticated_sample_sign_content_joins_established_in_this_audit": 0,
        "caution": "Missing inscription columns do not prove absence of marks; visual findings live in residue_anchor_audit.json. No visual classification is computed here."
    }
    out = ROOT / "results/residue_sample_metadata.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(rows)} CSV rows, {len(archaeological)} archaeological; Ghosh 9+6 table rows; no sign-value assignment")


if __name__ == "__main__":
    main()
