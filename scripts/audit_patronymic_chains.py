"""Literal internal-delimiter chains; no meanings or name boundaries inferred.

The domestic corpus is secondary candidate transcription, not full autopsy.
M001 is a visually matched plain human sign, NOT an established patronymic.
"""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

from analyze_m77_foreign import (DOMESTIC_RANGES, NAMED_OTHER, PROBABLE,
                                 SECURE, eligible, sequence)

ROOT = Path(__file__).resolve().parents[1]


def split_edges(strings, delimiter):
    """Keep exact full flanks only, requiring one internal marker occurrence."""
    edges = []
    for seq, references in sorted(strings.items()):
        if seq.count(delimiter) != 1:
            continue
        i = seq.index(delimiter)
        if i == 0 or i == len(seq) - 1:
            continue
        edges.append({"left": list(seq[:i]), "right": list(seq[i+1:]),
                      "sequence": list(seq), "references": sorted(references)})
    return edges


def exact_chains(edges):
    """Two distinct full strings with matching nonempty, entire middle bundle."""
    return [{"first": a, "second": b, "shared_bundle": a["right"]}
            for i, a in enumerate(edges) for j, b in enumerate(edges)
            if i != j and a["right"] == b["left"]]


def marginal_walk_count(edges):
    """Includes self-edge walks; invariant to rewiring with fixed marginals."""
    left = Counter(tuple(e["left"]) for e in edges)
    right = Counter(tuple(e["right"]) for e in edges)
    return sum(left[k] * right[k] for k in left.keys() | right.keys())


def inventory(strings, delimiter):
    positions = Counter()
    bearing = []
    for seq, refs in sorted(strings.items()):
        if delimiter not in seq:
            continue
        n = seq.count(delimiter)
        category = ("repeated_marker" if n > 1 else
                    "initial" if seq[0] == delimiter else
                    "final" if seq[-1] == delimiter else "internal")
        positions[category] += 1
        bearing.append({"sequence": list(seq), "references": sorted(refs),
                        "marker_count": n, "category": category})
    edges = split_edges(strings, delimiter)
    chains = exact_chains(edges)
    return {"delimiter": delimiter, "bearing_unique_strings": len(bearing),
            "bearing_records": sum(len(x["references"]) for x in bearing),
            "position_categories": dict(positions), "bearing_strings": bearing,
            "eligible_edges": edges, "distinct_string_chains": chains,
            "chain_count": len(chains),
            "walk_count_including_self": marginal_walk_count(edges)}


def main():
    path = ROOT / "data/processed/m77_candidate_records.jsonl"
    rows = [json.loads(x) for x in path.read_text().splitlines()]
    domestic = defaultdict(list)
    foreign = defaultdict(list)
    probable = defaultdict(list)
    marker_inventory = []
    for row in rows:
        ref = row["source_reference"]
        if ref in SECURE + PROBABLE:
            marker_inventory.append({"reference": ref,
                                     "diplomatic": row["diplomatic"],
                                     "group": "named_site" if ref in SECURE else "probable",
                                     "exclusions": eligible(row)})
        if eligible(row):
            continue
        n = int(ref)
        if any(lo <= n <= hi for lo, hi in DOMESTIC_RANGES) or ref in NAMED_OTHER:
            domestic[sequence(row)].append(ref)
        if ref in SECURE:
            foreign[sequence(row)].append(ref)
        if ref in PROBABLE:
            probable[sequence(row)].append(ref)
    controls = [inventory(domestic, f"M{i:03d}") for i in range(1, 418)]
    primary_path = ROOT / 'data/processed/patronymic_primary_pair_review.json'
    primary = json.loads(primary_path.read_text())
    for p, expected in primary['input_sha256'].items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == expected, p
    for verified in primary['rows']:
        candidates = [r for r in rows if r['source_reference'] == verified['reference']]
        assert len(candidates) == 1
        assert list(sequence(candidates[0])) == verified['tokens']
        assert not eligible(candidates[0])
    primary_edges = split_edges({tuple(r['tokens']): [r['reference']]
                                for r in primary['rows']}, 'M017')
    assert len(exact_chains(primary_edges)) == 1
    result = {
        "status": "Exploratory literal-chain feasibility audit, not a patronymic reading",
        "protocol": {
            "target": "M001, matched visually to plain human glyph in Vidale Fig5 and M77 sign list",
            "twins_mapping": None,
            "family_variants": "Unresolved; no variants merged",
            "parse": "A D B, exactly one D and both complete nonempty flanks",
            "match": "A D B followed by B D C, two distinct complete strings",
            "deduplication": "Identical entire strings collapsed; all references retained",
            "order": "Existing normalized candidate order, no further reversal",
            "controls": "All 417 single-code delimiters scanned descriptively; not independent tests or p-values",
            "scope_exclusions": ["Prefix/suffix marker parses", "Multiple markers", "Ligatures/allographs",
                                 "Damaged or doubtful lines", "Unverified line splitting", "Phonetic variation"]},
        "samples": {"domestic_records": sum(map(len, domestic.values())),
                    "domestic_unique": len(domestic), "named_foreign_unique": len(foreign),
                    "probable_foreign_unique": len(probable)},
        "foreign_inventory": marker_inventory,
        "main": inventory(domestic, "M001"),
        "named_foreign_main": inventory(foreign, "M001"),
        "probable_foreign_main": inventory(probable, "M001"),
        "primary_verified_control_pair": primary['abstract_pattern'],
        "primary_review_sha256": hashlib.sha256(primary_path.read_bytes()).hexdigest(),
        "delimiter_controls": controls,
        "control_summary": {
            "delimiters_with_edges": sum(bool(x["eligible_edges"]) for x in controls),
            "delimiters_with_distinct_chains": sum(bool(x["chain_count"]) for x in controls),
            "total_delimiter_chain_pairs": sum(x["chain_count"] for x in controls)},
        "input_sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()}}
    for p in ["scripts/analyze_m77_foreign.py", "data/processed/m77_foreign_selection_review.json",
              "data/raw/hybrid_vidale_2005.pdf", "data/raw/mahadevan_1977_text.pdf",
              "results/primary_pages/hybrid-pat-vidale-10.png",
              "results/primary_pages/hybrid-pat-vidale-11.png",
              "results/primary_pages/hybrid-pat-m77-43.png",
              "results/primary_pages/hybrid-pat-m77-171.png"]:
        result["input_sha256"][p] = hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
    (ROOT / "results/patronymic_chain_audit.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"samples": result["samples"], "main": {k: result["main"][k] for k in
          ["bearing_unique_strings", "bearing_records", "position_categories", "chain_count"]},
                      "controls": result["control_summary"]}, indent=2))


if __name__ == "__main__":
    main()
