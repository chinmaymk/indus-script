"""Compare primary-selected West Asian strings with held-out domestic seals.

All inputs remain candidate transcriptions. Scores identify unusual combinations,
not words, meanings, a language, or linguistic encoding.
"""
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
from statistics import median
import hashlib

ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd()
SECURE = ["9801","9811","9821","9822","9832","9833","9834","9842","9845","9846","9851","9852"]
PROBABLE = ["9901","9902","9903","9904","9905"]
# Codebook-defined named South Asian site ranges. Named other sites are supplied
# by the reviewed selection ledger; 9701 (unknown) is never silently domestic.
DOMESTIC_RANGES = [(1001,1905),(2002,2952),(3001,3513),(4001,4905),
                   (5001,5601),(6104,6306),(6402,6405),(7001,7301),(8001,8302)]
NAMED_OTHER = ['9001','9011','9021','9022','9031','9041','9042','9051','9061','9062','9063','9071','9073','9084','9085','9091','9092','9093','9094','9095','9101','9102','9103','9104','9111','9121','9201','9202','9203','9204','9205','9211','9221']

def eligible(row):
    reasons = []
    if row["source_object_code"] != "1": reasons.append("not_seal")
    if row["source_doc_count"] != 1: reasons.append("multiple_export_documents")
    if row["source_direction_code"] not in ("1","2"): reasons.append("other_original_direction")
    if len(row["tokens"]) < 2: reasons.append("fewer_than_two_slots")
    if any(t["doubtful"] for t in row["tokens"]): reasons.append("doubt")
    if any(t["unknown_span"] for t in row["tokens"]): reasons.append("loss")
    return reasons

def sequence(row):
    return tuple(t["sign"] for t in row["tokens"])

def pair_counts(sequences):
    return Counter(pair for seq in sequences for pair in zip(seq,seq[1:]))

def score(seq, counts):
    pairs = list(zip(seq,seq[1:]))
    if not pairs: raise ValueError("Need at least two signs")
    outgoing = Counter()
    for (a,b),n in counts.items():
        if n < 0: raise ValueError("Negative training count")
        outgoing[a] += n
    terms = [-math.log2((counts.get((a,b),0)+1)/(outgoing[a]+417)) for a,b in pairs]
    return {"unseen_pair_fraction":sum(counts.get(p,0)==0 for p in pairs)/len(pairs),
            "mean_transition_surprisal_bits":sum(terms)/len(terms),
            "pairs":[{"left":a,"right":b,"training_count":counts.get((a,b),0)} for a,b in pairs]}

def leave_one_out(seq, counts):
    remaining = counts.copy()
    for pair,n in pair_counts([seq]).items():
        remaining[pair] -= n
        if remaining[pair] < 0: raise ValueError("Cannot exclude an absent sequence")
    return score(seq,remaining)

def compare(value,controls):
    if not controls: return {"count":0,"status":"no_same_length_controls"}
    # Floating equality tolerance is numerical, not an empirical acceptance rule.
    return {"count":len(controls),"median":median(controls),"min":min(controls),"max":max(controls),
            "lower":sum(x<value-1e-12 for x in controls),
            "equal":sum(abs(x-value)<=1e-12 for x in controls),
            "higher":sum(x>value+1e-12 for x in controls)}

def run():
    rows = [json.loads(line) for line in (ROOT/"data/processed/m77_candidate_records.jsonl").read_text().splitlines()]
    byref = {r["source_reference"]:r for r in rows}
    inventory = []
    for ref in SECURE+PROBABLE:
        row = byref.get(ref)
        reasons = ["absent_export"] if row is None else eligible(row)
        inventory.append({"reference":ref,"provenance_group":"named_site" if ref in SECURE else "probable_West_Asia",
                          "filter_reasons":reasons,"sequence":None if row is None else [t["diplomatic"] for t in row["tokens"]],
                          "core_included":ref in SECURE and not reasons})
    targets = [byref[r] for r in SECURE if r in byref and not eligible(byref[r])]
    target_strings = {sequence(r) for r in targets}
    domestic = defaultdict(list)
    for r in rows:
        num = int(r["source_reference"])
        named = any(lo<=num<=hi for lo,hi in DOMESTIC_RANGES) or r["source_reference"] in NAMED_OTHER
        if named and not eligible(r): domestic[sequence(r)].append(r["source_reference"])
    matches = [{"sequence":list(s),"domestic_references":domestic[s]} for s in sorted(target_strings) if s in domestic]
    training = set(domestic)-target_strings
    counts = pair_counts(training)
    controls = defaultdict(list)
    for seq in sorted(training):
        controls[len(seq)].append({"sequence":list(seq),"references":domestic[seq],"scores":leave_one_out(seq,counts)})
    target_results = []
    for row in targets:
        seq = sequence(row)
        values = score(seq,counts)
        target_results.append({"reference":row["source_reference"],"sequence":list(seq),
                               "scores":values,"reversed_diagnostic":score(seq[::-1],counts),
                               "same_length_reference":{key:compare(values[key],[x["scores"][key] for x in controls[len(seq)]])
                                                        for key in ["unseen_pair_fraction","mean_transition_surprisal_bits"]}})
    return {"selection":{"domestic_ranges":DOMESTIC_RANGES,"named_other_references":NAMED_OTHER,
                          "domestic_eligible_records":sum(map(len,domestic.values())),
                          "domestic_unique_before_exclusion":len(domestic),"training_unique":len(training),
                          "target_records":len(targets),"target_unique":len(target_strings)},
            "inventory":inventory,"exact_domestic_matches":matches,"targets":target_results,
            "domestic_leave_one_out_controls":dict(controls),
            "limits":["Foreign findspot does not determine manufacture, owner, language or meaning.",
                      "Candidate transcription and site-selection limitations remain.",
                      "Same-length controls are descriptive, not population p-values.",
                      "Fixed add-one smoothing over417 signs; no boundary terms.",
                      "Reference training has one fewer unique string; differences are not perfectly sample-size matched.",
                      "No script or language decipherment follows from unusual combinations."]}

def main():
    result=run()
    paths=["data/processed/m77_candidate_records.jsonl",
           "data/processed/m77_foreign_comparison_protocol.json",
           "data/processed/m77_foreign_selection_review.json",
           "data/processed/m77_foreign_primary_parent_review.json"]
    result["input_sha256"]={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    selection=json.loads((ROOT/paths[2]).read_text())
    if (selection["selection"]["named_site_references"]!=SECURE or
        selection["selection"]["unknown_probable_WA_references"]!=PROBABLE or
        [(r["lower"],r["upper"]) for r in selection["domestic_reference_ranges"]]!=DOMESTIC_RANGES or
        sorted(selection["other_named_domestic_references"])!=sorted(NAMED_OTHER)):
        raise ValueError("Analysis selection differs from primary-reviewed ledger")
    for source in selection["inputs"]:
        if hashlib.sha256((ROOT/source["path"]).read_bytes()).hexdigest()!=source["sha256"]:
            raise ValueError("Changed selection-review input: "+source["path"])
    review=json.loads((ROOT/paths[-1]).read_text())
    if hashlib.sha256((ROOT/review["source"]).read_bytes()).hexdigest()!=review["source_sha256"]:
        raise ValueError("Changed primary source")
    targets={r["reference"]:r for r in result["targets"]}
    for row in review["rows"]:
        if targets[row["reference"]]["sequence"]!=row["sequence"]:
            raise ValueError("Changed reviewed foreign sequence: "+row["reference"])
    agent_path="data/processed/m77_foreign_glyph_review_agent.json"
    agent_review=json.loads((ROOT/agent_path).read_text())
    result["input_sha256"][agent_path]=hashlib.sha256((ROOT/agent_path).read_bytes()).hexdigest()
    if agent_review["primary_source"]["sha256"]!=review["source_sha256"]:
        raise ValueError("Glyph reviewers used different primary source versions")
    for row in agent_review["rows"]:
        if targets[row["reference"]]["sequence"]!=row["tokens"]:
            raise ValueError("Changed agent-reviewed foreign sequence: "+row["reference"])
    output=ROOT/"results/m77_foreign_comparison.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"selection":result["selection"],"targets":[
        {"reference":r["reference"],"unseen_pair_fraction":r["scores"]["unseen_pair_fraction"],
         "mean_transition_surprisal_bits":r["scores"]["mean_transition_surprisal_bits"]}
        for r in result["targets"]]},indent=2))

if __name__=="__main__":
    main()
