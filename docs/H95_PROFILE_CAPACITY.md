# An independently scaled vessel profile

**A new trace of the published interior gives about 86 litres for vessel 6640-501.**
This corroborates the order of magnitude of Fuls's provisional 88.3-litre estimate
without setting the photograph scale from a numerical reading. It remains a
drawing-based reconstruction, not a direct measurement of liquid capacity.

## Source and identity

J. M. Kenoyer's *The Origin, Context and Function of the Indus Script: Recent
Insights from Harappa* reproduces the profile as Figure7.2, printed156/PDF21.
The [public journal PDF](https://mohenjodarorj.sindhila.org/index.php/journal/article/download/105/81)
is saved in the common raw-data folder with a checksum. Its hosting metadata says
2025; this does not date the excavated object or constitute a new discovery.
The drawing labels H95-2661/6640-501, whereas its caption says H95-2662/6640-501.
The shared excavation identifier permits an explicit link despite that discrepancy.
An earlier Meadow–Kenoyer1997 Figure12.02 table also indexes H95-2661/6640-501;
its public text was inspected, but direct download failed and its image is not
claimed as locally reviewed.

The drawing includes a labelled 0–20cm scale and an interior wall section. It also
shows several classes of marks. Rim and large body graffiti are labelled post-firing;
other body/base marks are labelled as potter's marks. Four rim traces are favored
by visual review, with low native resolution leaving some incision ambiguity.
The [independent inscription review](H95_INSCRIPTION_REVIEW.md) preserves this
uncertainty. **The whole vessel is not inscribed only with strokes.** Fuls's short
Table3 description must not erase the separate body inscription.

## Reproducible integration

The native embedded figure is 696×803 pixels. Its scale bar was digitized as 150px
for 20cm. Thirty samples follow the inner-left wall; the drawn axis has a small tilt,
which is handled by interpolating its horizontal coordinate with height. Rotate the
resulting radius profile, assuming a circular section at each height. For each pair
of linearly interpolated radii r0,r1 separated by height h, the exact segment volume is

```
Vsegment = π h (r0² + r0 r1 + r1²) / 3.
```

Sum the segments, convert cubic centimetres to litres, and stop at the internal
floor. The flat bottom does not require extending the profile to a fictitious tip.
This is exact for the traced piecewise-linear model, not for the ancient vessel.

The [saved trace](../data/processed/h95_profile_trace.json) retains all coordinates
and an initial rough trace superseded after its overlay visibly missed the lower
wall. Corrections followed the inner dark contour at each sampled row; they did
not solve for the previously reported capacity. Because that capacity was already
known, this is explicitly not blind replication.

![Auditable interior trace, axis and labelled scale](../results/h95_profile_overlay.png)

## Result and sensitivity

The corrected profile gives **85.96L**, about **2.7% below** the earlier 88.3L estimate.
The traced interior height is approximately67.5cm; it should not be confused with
the previously reported71cm exterior height. Assuming four equal rim strokes gives
approximately21.5L per stroke. Counting only three would give28.7L per stroke.

Uniform radial shifts of ±3px, a scale-bar length error of ±2px, and an additional
±2% vertical-scale perturbation produce a combined envelope of **78.02–94.66L**.
These are analyst-selected sensitivity scenarios, **not a statistical confidence
interval**. They do not cover unknown restoration errors, non-circular sections,
uneven walls, or every possible distortion in the original drawing. Lower fill levels
reduce the estimated amount; the script records several such scenarios.

Under the four-stroke interpretation, the earlier Harappa calibration of40.35L per
stroke predicts161.4L. That is far above this reconstructed capacity, including the
listed perturbations. Under three strokes it predicts121.1L, also above them.
The mismatch is therefore not explained by the tested tracing perturbations or by
that one counting ambiguity. This conclusion remains conditional on the drawing's
geometry and on treating the strokes as the volume contained at one time.

The result supports testing different unit classes or other quantity functions.
It does not identify which applies, translate the body signs, or establish that the
rim strokes measure capacity at all. Any rule relating the body inscription to a unit
must predict a new vessel before its capacity is used to choose that rule.

## Reproduce

Run `python3 scripts/analyze_h95_profile.py`. Optional `--extract-image` regenerates
the embedded JPEG from the saved PDF using pypdf, then verifies its checksum.
The default analysis needs Pillow; it also emits an SVG overlay and
[machine-readable results](../results/h95_profile_volume.json). Analytical tests
cover cylinders, cones, split frusta, cubic scale dependence and lower fill levels.
