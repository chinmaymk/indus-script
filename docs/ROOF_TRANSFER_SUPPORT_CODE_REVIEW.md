# Independent roof-transfer support code review

No blocking algorithm error was found in the inspected implementation. The nine focused tests pass, including the independently added exhaustive oracle. An independent exhaustive oracle agrees with the two-edge threshold on all1,024 simple graphs on five vertices, and all returned witnesses have four distinct valid endpoints. Additional synthetic examples confirm a positive three-root path and the known-label versus unknown-allowed branch distinction.

This is an implementation review of the frozen support design. No new corpus support output was opened, no classifier or accuracy estimate was computed, and no semantic hypothesis was added. The pre-count design document was preserved unchanged; this later code review has its own pins.

## Checked implementation properties

- `grouped_occurrences` filters doubt/loss, strict status where requested and field length before constructing the reference/formula graph. All eligible records participate, including target-free records and records with unknown metadata. Collapse uses every endpoint of every selected pair, not just the focal root. Union-find retains transitive connections.
- Component IDs are fixed before occurrences are scored. Every target position inherits the record’s component. Metadata filters do not alter the graph, and held-out folds do not reconstruct components after removing bridge records.
- `root_support` matches exact pair, normalized secondary site label, object code, length and position. It does not cross the two fish pairs within an edge. Missing metadata is excluded in the primary scoring branch only.
- An edge joins different components with opposite states in one compatible stratum. Parallel witnesses collapse to one unordered edge. A mixed component can occur in either role, but the two-edge threshold prevents self-pairing and component reuse across strata.
- `two_disjoint_edges` exhaustively enumerates unique unordered edge pairs and accepts only disjoint endpoint sets. It is an exact threshold check, not a greedy algorithm or a maximum-matching claim. Witness selection is deterministic.
- `analyze` bans every component touching the held-out root, including occurrences excluded from known-label scoring. It recomputes each remaining training root’s support after purge, then requires the held-out root and at least two training roots to pass. The two fish pairs count once through their shared root label.
- Metadata normalization strips whitespace and recognizes the protocol’s case-insensitive missing sentinels. The output explicitly denies complete artifact/die keys and states that prediction was not run. No fitting path exists in the inspected script.

These conclusions assume the existing record schema supplies unique record IDs, valid token fields and stable nonmissing source references. The script is not a general-purpose validator for arbitrary malformed external data. Hashes authenticate inspected revisions, not archaeological identity. Branch-specific grouping and unknown physical links remain the limits described in `ROOF_TRANSFER_SUPPORT_DESIGN.md`.

## Validation performed

Ran:

```
python3 -m unittest discover -s tests -p test_roof_transfer_support.py
```

All nine tests passed. The previously existing eight cases include metadata sentinels, triangle/star/path graphs, mixed-state components, pair/position stratum separation, cross-stratum component reuse, transitive grouping through missing metadata, damage/strict exclusions, and marginal support disappearing after the held-out purge.

The independent threshold oracle is now persisted as `test_exhaustive_threshold_against_four_vertex_partition_oracle` in `tests/test_roof_transfer_support.py`, with the parent authorizing this test-file addition. It uses a different enumeration: choose four vertices, enumerate the three perfect pairings of those four, and check whether either pairing’s two edges are present. This was compared against the producer for every edge subset on five vertices. The following reproduces that bounded check without reading a corpus:

```python
import itertools, sys
sys.path.insert(0, 'scripts')
from audit_roof_transfer_support import two_disjoint_edges
vertices = tuple('abcde')
possible = list(itertools.combinations(vertices, 2))
for mask in range(1 << len(possible)):
    edges = {e for i, e in enumerate(possible) if mask >> i & 1}
    expected = False
    for a, b, c, d in itertools.combinations(vertices, 4):
        for first, second in [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]:
            if first in edges and second in edges:
                expected = True
    found = two_disjoint_edges(edges)
    assert bool(found) == expected
    if found:
        assert len(set(found[0] + found[1])) == 4
        assert all(tuple(e) in edges for e in found)
```

A second synthetic check constructed three roots, each with two base and two roof records. Every record had a unique reference and unique second context token, while sharing known site, object type, length and target position. All three held-out folds passed. Replacing all site labels with whitespace-padded uppercase `<UNKNOWN>` made every known-label fold fail while all three unknown-allowed folds still passed. This verifies the positive path and missing-label branch separation; it does not inspect or predict real corpus support.

## Remaining inferential limits

Passing this code audit does not make a proxy component an independent object or die. A passing fold would establish only the frozen finite support condition. It would not establish adequate sample size for a classifier, statistical power, archaeological exchangeability, or common roof semantics. Separate training roots may share components with each other; the implementation correctly removes training/test component overlap, while future group-aware weighting would still be needed within training. No such model is authorized by this review.

## Inspected revision pins

- `data/processed/roof_transfer_support_protocol.json`: SHA256 `64246b8448498624e3f166b34709610fdc87d8ac318b3d9e9064bb43ff35ec43`.
- `docs/ROOF_TRANSFER_SUPPORT_DESIGN.md`: SHA256 `630ba61ce044e449fc0f71ba2d6134db84ef2a63539a1c3cf17f9536394f456a`.
- `scripts/audit_roof_transfer_support.py`: SHA256 `181b1ee75bfe6e4d70c2220ce646e8ef330c1e7f028b592e87a0d8a42ac6705f`.
- `tests/test_roof_transfer_support.py`: SHA256 `944b2daa807fb61bcf1f04871abfb403b2d2d2ec79f583596aa90454f35af19d`.
