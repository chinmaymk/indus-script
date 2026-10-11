# Independent review of the arch mass bound

The bound is a valid necessary consequence of the stated additive model. Its numerical deficits are correct. It tests a conjunction of assumptions and does not establish numerical or phonetic sign values.

## Algebra

Let S be the small-axe mass, L the large-axe mass, and K the chisel mass. The proposal assumes a common contribution A for the selected shared group, an arch-unit contribution u, and nonnegative residuals r and q:

```
S = A + r,  r >= 0
L = A + 7u
K = n*u + q,  q >= 0, u >= 0, n > 0
```

From the first equation, A <= S. From the third, u <= K/n. Substituting both upper bounds into the second gives:

```
L <= S + 7K/n
D = L - S - 7K/n <= 0
```

Thus a strictly positive D contradicts the combined premises. No separate assumption that A equals six times a stroke value, or that r is zero, is needed. Allowing r >= 0 makes this a weaker and more permissive test than equating the complete small-axe field with A: a positive residual reduces A and cannot rescue an excessive L. No premise A >= 0 is needed for this necessary inequality.

The n=1 branch covers a candidate containing at least one common u: a sole u, two u units, or u plus other nonnegative contributions. It does not cover arbitrary signed, multiplicative, contextual or nonadditive readings. The n=2 branch specifically needs at least two equivalent units. Catalogue normalization as a double-arch sign cannot independently supply that semantic premise.

## Arithmetic

The inspected input ledgers store the literals as strings: S=`262.233`, L=`1910.030`, K=`210`. Fraction-based arithmetic preserves these published decimals exactly; this does not imply that the physical measurements have zero uncertainty.

| Minimum units n | Maximum L allowed (g) | Deficit D (g) | Minimum added K alone (g) | Required total K with axes fixed (g) |
|---|---:|---:|---:|---:|
| 1 | 1732.233 | 177.797 | 25.399571… | 235.399571… |
| 2 | 997.233 | 912.797 | 260.799143… | 470.799143… |

These exact deficits are 177797/1000 and 912797/1000. The added-K thresholds are 177797/7000 and 912797/3500. With K and L held fixed, the required added S is respectively 177.797 g or 912.797 g.

## Missing-mass extension

For hypothetical nonnegative losses dS, dL and dK, replace each reported mass by its corrected mass. The same necessary bound is:

```
L + dL <= S + dS + (7/n)*(K + dK)
dS + (7/n)*dK - dL >= D
```

The proposed sign on dL is correct. Increasing the original large-axe mass worsens the discrepancy; increasing either comparison mass may reduce it. These are conditional requirements, not observed damage corrections or fitted original weights. The one-object thresholds assume the other two corrections are exactly zero. They supply no measurement of actual missing material and no evidence that the premise applies to original rather than surviving mass.

## Implementation review and validation

Inspected `arch_mass_bound_protocol.json`, `audit_arch_mass_bound.py` and `test_arch_mass_bound.py`. The `bound` function uses exact Fractions, tests strictly positive inputs, computes D with the correct sign, and clamps required added masses at zero when there is no deficit. Its equality boundary is correctly treated as no contradiction. The minimum total K expression is a nonnegative lower bound; when L <= S, a zero bound does not assert that the actual positive chisel mass is zero.

The two existing unit tests pass. They check the equality boundary, an incompatible positive deficit, the stated numerical deficits, and the repaired n=1 boundary. Independent direct Fraction calculations reproduce both branches and both added-K thresholds. No additional tests or changes were required. This review does not certify all external record joins or independently remeasure the artifacts. At the inspected script revision, a comment still reserves exact field authentication for a forthcoming catalogue join; that provenance task remains distinct from this completed algebra check.

## Interpretation limits

The bound assumes that the selected complete fields encode comparable masses, the shared group has the same contribution, seven arches compose additively, and all residual contributions are nonnegative. It also assumes no additional unencoded component in L. Failure of any one premise can remove the contradiction. The test was chosen after prior inspections and model failures, so it is exploratory rather than a preregistered or independent semantic prediction. Broken objects, disputed K121 segmentation, uncertain historical masses, alternate quantity targets and contextual sign values remain relevant. The defensible conclusion is conditional inconsistency with reported surviving masses, not a decipherment or proof that arch signs cannot be numerical.

## Inspected revision pins

- `data/processed/arch_mass_bound_protocol.json`: SHA256 `97d01b5861743c2a8eb06d50b619b9c5aca45c05c73fdb58abb2f69d14064cad`.
- `scripts/audit_arch_mass_bound.py`: SHA256 `51c7ec8c594cbbf0813b2ae4151b163c0d45a60cd6ebc1756b38c7117b305381`.
- `tests/test_arch_mass_bound.py`: SHA256 `555444cbec54df77fd48ad669b4b5830a1fb9185db62891003b15472ad0cf4b6`.
