# Conditional three-object check of the metal-tool weights

**The three objects cannot all fit the author's reconstructed-chisel bound with nonnegative t while the stated masses and readings are held fixed.** This is a conditional consistency check, not identification of numeral values or a rejection of every possible weight interpretation.

Inputs are the primary table on Pettersson 1999 p101 (PDF 13), the precise surviving weights on p98 (PDF 10), and the reconstruction on p99 (PDF 11), preserved in `data/processed/metal_tool_weight_anchors.json`. The equations are:

```
DK-7855: 6i = 262 g
DK-7835: 7u + 6i = 1910 g
DK-7856 original chisel: M = u + 5i + 4t, with t >= 0
Author's rounded-mass reconstruction: M < 2.6 * 165 g = 429 g
```

The first two equations determine:

```
i = 262/6 = 131/3 g
u = (1910 - 262)/7 = 1648/7 g
M = 1648/7 + 655/3 + 4t = 9529/21 + 4t g
```

Thus `M >= 9529/21 = 453.7619047619 g`, with equality only when t=0. This exceeds 429 g by `520/21 = 24.7619047619 g`. Satisfying the strict reconstruction would instead require `t < -130/21 g`, which contradicts t>=0.

Writing p as original-chisel mass divided by surviving-tang mass, and keeping the axe equation fixed at the requested **1910 g**, gives:

| Surviving tang mass | Minimum p, at t=0 | Consequence |
| --- | --- | --- |
| 165 g, author's rounded equation | 9529/3465 = 2.7500721501 | Above 2.6 |
| 165.343 g, precise reported tang mass | 9529000/3472203 = 2.7443671928 | Above 2.6 |

For completeness, replacing **both** rounded values by the precise reported axe 1910.030 g and tang 165.343 g gives `u=164803/700 g`, `M>=952909/2100=453.7661904762 g`, and `p>=9529090/3472203=2.7443931130`. The corresponding cap `2.6*165.343=429.8918 g` is still too low. This sensitivity calculation changes the explicitly identified precision convention; it is not a repair of the primary rounded equations.

The original 262 g and 1910 g observations are the calibration inputs; the reconstructed chisel supplies the third conditional constraint. It adds an overdetermining test that the two-object fit lacked. At least one of the shared-value assumption, exact current-mass equations, sign readings, additive arithmetic, nonnegative t, or the reconstruction bound must change to achieve a fit.

The archaeological limitations matter: p101 questions whether DK-7855's six strokes form a separate numerical expression because other signs are nearby and one stroke sits lower. The objects suffered corrosion and chemical cleaning; the original chisel is incomplete, and the 2.6 bound is a comparative reconstruction rather than an original measured mass. These facts prevent turning this arithmetic inconsistency into an unconditional semantic conclusion.

All fractions above were independently calculated with Python's standard-library `fractions.Fraction`, retaining decimal inputs as strings. No source readings, ledger entries, or shared scripts were changed. No downloads were needed.

Reproduce the primary rounded calculation and the tang-precision comparison:

```python
from fractions import Fraction as F

i = F(262, 6)
u = (F(1910) - 6*i) / 7
minimum_mass = u + 5*i
assert (i, u, minimum_mass) == (F(131, 3), F(1648, 7), F(9529, 21))
assert minimum_mass > F("2.6") * 165
for tang in [F(165), F("165.343")]:
    print(minimum_mass / tang, float(minimum_mass / tang))
```
