"""Snapshot support and independently check conditional calibration, without fitting."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text())

def pin(path):
    p = ROOT / path
    return {"path": path, "bytes": p.stat().st_size,
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}

def main():
    index = read("results/sign_evidence_417.json")
    assert {r["sign"] for r in index["signs"]} == {f"M{i:03d}" for i in range(1,418)}
    assert len(index["signs"]) == 417
    assert all(r["semantic_value"] is None and r["phonetic_value"] is None for r in index["signs"])
    primary = read("results/primary_inventory_findings.json")
    inventory = {k: primary[k] for k in ["tokens", "hapax_signs", "signs_with_fewer_than_10_occurrences", "tokens_top_67"]}
    assert inventory == {"tokens": 13372, "hapax_signs": 112, "signs_with_fewer_than_10_occurrences": 264, "tokens_top_67": 10769}
    assert index["summary"]["M_rows_observed_in_candidate_M77_strict"] == 332
    support = read("results/chanhu_deposit_support.json")["summary"]
    assert support["framed_objects"] == 65 and support["strict_matched_strata"] == 0
    assert support["reviewed_named_seal_associations"] == 7
    assert support["reviewed_association_tiers"]["no_secured_deposit_join_in_current_review"] == 58
    capacity = read("results/capacity_context_measurements.json")
    assert capacity["new_complete_external_test_pairs"] == 0
    assert capacity["new_direct_fill_measurements"] == 0
    external = read("data/processed/inscribed_weight_external_search.json")
    assert external["queries_executed"] == 5
    assert external["qualifying_new_inscribed_weight_or_instrument_anchors"] == 0
    roof = read("results/roof_transfer_support.json")
    roof_folds = {k: v["summary"]["held_out_roots_passing_proxy_gate"] for k,v in roof["results"].items()}
    assert all(not x for x in roof_folds.values())
    spec = read("results/chanhu_local_specificity.json")
    assert spec["target"]["background"]["counts"] == {"positive":2,"negative":34,"unknown":24}
    control_counts = {k:v["n_codes"] for k,v in spec["control_set_summaries"].items()}
    assert control_counts["same_observed_positive_count"] == 9
    assert control_counts["half_to_twice_observed_positive_count"] == 71

    # Independent bounded-error derivation: each corner is a possible pair of
    # represented-to-observed multipliers; enumerate their observed B/A ratios.
    calibration = read("results/numeral_calibration_design.json")
    eq = read("results/numeral_equation_audit.json")
    expected = []
    for c in eq["after_conditional_digit_bounds"]:
        a = 2*c["L"] + 2*c["S"]
        b = 7*c["S"] + 5
        expected.append({"candidate":c,"A":a,"B":b,"B_over_A":str(F(b,a))})
    assert calibration["candidates"] == expected
    ratios = [F(row["B"],row["A"]) for row in expected]
    assert ratios == [F(61,36), F(145,112)]
    R = max(ratios)/min(ratios)
    assert R == F(1708,1305)
    assert calibration["ratio_of_candidate_ratios"] == str(R)
    checks = []
    for row in calibration["error_sensitivity"]:
        e = F(row["per_object_error"])
        intervals = []
        for r in ratios:
            corners = [r*a/b for a in (1-e,1+e) for b in (1-e,1+e)]
            intervals.append((min(corners),max(corners)))
        assert row["ratio_intervals"] == [[str(a),str(b)] for a,b in intervals]
        separated = intervals[1][1] < intervals[0][0]
        polynomial = 403*e*e - 6026*e + 403
        assert separated == (polynomial > 0) == row["strictly_disjoint"]
        assert str(polynomial/1305) == row["exact_separation_certificate"]
        checks.append({"error":str(e),"polynomial":str(polynomial),"disjoint":separated})
    with localcontext() as ctx:
        ctx.prec = 60
        critical = (Decimal(6026)-(Decimal(6026)**2-4*403*403).sqrt())/(2*403)
    assert abs(float(critical)-calibration["critical_error_approximation"]) < 1e-14
    assert calibration["single_hypothetical_total"]["candidate_units"] == [str(F(100,row["A"])) for row in expected]
    checked_source_hashes = {}
    for path, digest in calibration["input_sha256"].items():
        checked_source_hashes[path] = pin(path)["sha256"] == digest
    assert all(checked_source_hashes.values())
    paths = [
        "docs/ALL_INVENTORY_NEXT_TEST_REVIEW.md", "docs/IDENTIFIABILITY.md",
        "docs/DECIPHERMENT_EVIDENCE_GAP_REVIEW.md", "docs/ALL_SIGN_EVIDENCE.md",
        "docs/CHANHU_DEPOSIT_RESULTS.md", "docs/CHANHU_LOCAL_GRAPHICS_AND_SPECIFICITY.md",
        "docs/CAPACITY_CONTEXT_RESULTS.md", "docs/METAL_NUMERAL_IDENTIFIABILITY.md",
        "docs/INSCRIBED_WEIGHT_EXTERNAL_SEARCH.md", "docs/NUMERAL_EQUATIONS.md",
        "docs/REPEATED_GOBLET_STAMP_REVIEW.md", "docs/HIND_LEG_HYPOTHESIS.md",
        "results/sign_evidence_417.json", "results/primary_inventory_findings.json",
        "results/chanhu_deposit_support.json", "results/chanhu_local_specificity.json",
        "results/chanhu_photo_sensitivity.json", "results/roof_transfer_support.json",
        "results/capacity_context_measurements.json", "results/numeral_equation_audit.json",
        "data/processed/inscribed_weight_external_search.json",
        "results/numeral_calibration_design.json", "scripts/analyze_numeral_calibration_design.py",
        "tests/test_numeral_calibration_design.py", str(Path(__file__).resolve().relative_to(ROOT)),
        *calibration["input_sha256"],
    ]
    result = {
        "date":"2026-09-28", "scope":"Local independent inferential review and exact calibration validation; no new fit or historical measurement.",
        "inventory":{"rows":417,"null_semantic_values":417,"null_phonetic_values":417,
                     "candidate_sequence_signs":332,"candidate_sequence_unobserved_signs":85,**inventory},
        "deposit_support":support,"control_counts":control_counts,"roof_passing_folds":roof_folds,
        "new_capacity_fill_measurements":0,"new_capacity_external_test_pairs":0,
        "new_weight_search_queries":5,"new_weight_anchor_count":0,
        "zero_pair_scope":"Reviewed cases only; not an exhaustive global claim.",
        "priorities":[
            {"rank":1,"test":"Unit-free commensurate quantity ratio between two existing numerical candidates",
             "mathematics_executable":True,"historical_test_available_in_reviewed_data":False,
             "missing":"Two secure represented quantities with shared units, authenticated fields and bounded nuisance errors"},
            {"rank":2,"test":"Replicated bead-domain prediction across independently classified deposits",
             "historical_test_available_in_reviewed_data":False,
             "missing":"Secured matched archaeological strata and independent complex replication"},
        ],
        "calibration_independent_validation":{"producer_imported":False,"candidate_totals":expected,
            "ratio_of_ratios":str(R),"polynomial_coefficients_descending":[403,-6026,403],
            "error_cases":checks,"critical_relative_error_decimal":str(critical),
            "input_hash_checks":checked_source_hashes,"mismatches":0,
            "limits":"Conditional arithmetic only; no new measured anchor or sign value."},
        "model_class_cautions":[
            "Null evidence fields do not prove inherent impossibility.",
            "No model-independent external-anchor count.",
            "For known-label bijections only, k anchors leave (417-k)! keys.",
            "Additive rank-nullity needs unrestricted or interior-feasible values for a continuum; boundary and integer restrictions matter.",
            "One anchor can identify a local value without identifying the full inventory.",
        ],
        "new_fits":0,"downloads":0,"established_semantic_values":0,"established_phonetic_values":0,
        "evidence_files":[pin(p) for p in sorted(set(paths))],
    }
    output = ROOT/"data/processed/all_inventory_next_test_review.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    assert all(pin(p["path"]) == p for p in result["evidence_files"])
    print(json.dumps({"output":str(output.relative_to(ROOT)),"pins":len(result["evidence_files"]),
        "independent_calibration_mismatches":0,"new_historical_anchors":0}))

if __name__ == "__main__":
    main()
