# Physical use of Lothal sealings and the limits of a commodity reading

The backs of clay sealings provide evidence independent of their inscriptions:
they preserve impressions of cords and surfaces. The recovered study supports
closure and storage uses for some inscribed stamps. It does not identify their
contents, a numeral value, an official's name or a commodity word.

The primary source is Frenez and Tosi (2005),
[author-deposited chapter](https://doi.org/10.5281/zenodo.5514283), printed pp.65–103.
Its physical reexamination and photographs are more direct evidence than later
semantic proposals. We retain its interpretations as interpretations, including
uncertain material identifications and reconstructed findspots.

## A repeated stamp crosses physical contexts

The source's most recurrent stamp reportedly occurs sixteen times. Its prose
lists ten sealing objects across several closure types; our ledger preserves that
selected list rather than inventing the remaining six impression records. Different
impressions on one object must also be kept distinct from different objects.

| Selected item | Source interpretation | Qualification |
|---|---|---|
|L-124|Small vessel with woven-straw closure|The table classifies the contacted surface as woven straw; the vessel is inferred.|
|L-125|Wooden surface, probably a box|A less likely pottery-shoulder alternative is explicitly discussed.|
|L-126|Leather bag or sack|Soft unwoven pleats are observed; the leather identification is tentative.|
|L-195, L-197|Vessel closures|Recurrent stamp occurs with other impressions.|
|L-189, L-190|Grating-like structures|Contents unknown.|
|L-206|Peg-on-wall closure|Not a measured quantity or a known commodity.|
|L-193, L-198|Frames or lockers in the prose|The table uses the broader category “structures.”|

The source reports the stamp identity. This review does not independently
reidentify its damaged signs or assign M/W codes. Parent visual inspection covered
the relevant prose and Figures6–7, including the labeled reverse photographs.

For a deliberately restrictive hypothesis—one fixed stamp text is an exact,
exclusive label for the contacted container category—the possible category sets
must share a member. Under the listed interpretations they do not. The saved
script checks this condition and its sensitivity to uncertainty. For L-124/125/126
alone the sets are `{pottery}`, `{wood,pottery}`, `{leather_bag}`. Their intersection
is empty; making the uncertain leather classification wholly unknown restores the
possible common label `pottery`.

This is a **conditional restriction**, not an established ancient classification.
It depends on stamp identity, container reconstruction and the exclusive-label
premise. It does not exclude one commodity in different containers, one custodian
handling different goods, an institution, authorization or a mixed inscription.
Nor does a full-stamp constraint establish a value for any individual sign.

## Stable impressions and additional marks

L-161–172 are reported as twelve impressions of one elephant stamp with four signs,
associated with polished wooden surfaces. Additional fingernail impressions vary;
the source reports up to six and no preserved tallies on L-165/L-170, while allowing
loss through breakage. Figure6 shows the distinction between the stamped image
and ancillary marks. We do not supply a new complete tally transcription.

That combination is compatible with a stable identifier plus separately added
information. The added marks might concern quantities, events, location or handling;
their cause remains disputed. The containers and contents have not survived as
independently counted units. Twelve sealings could represent repeated closure of
one box, several boxes or other event groupings. Treating them as twelve known
transactions, twelve different boxes or twelve independent semantic anchors would
add evidence that is not present.

## Context cannot validate the inference that created it

The source codes distinguish recorded warehouse context W, context W1 inferred
from recurring stamp identity, and W2 assigned from the broader SRG3 area. W1 can
be useful for reconstruction, but testing stamp-to-warehouse association on those
same assignments would reuse the conclusion as evidence. Analyses must show
W-only results separately and retain unknown findspots.

The [complete table audit](LOTHAL_TABLE_AUDIT.md) recovers all93 printed rows and
records disagreements with the prose. Its row-level counts are reproducible;
they are not corrections to the excavated objects themselves. No undocumented
choice of the prose or table is allowed to improve a semantic hypothesis.

## What changes in the working account

The physical traces make storage, closure and repeated-use contexts concrete for
this assemblage. A short-label or authorization account must permit the same
stamp in different contexts and preserve separately added information. This is
stronger contextual grounding than sequence statistics alone, but it still cannot
select between names, authorities, goods and regulations. It also does not decide
whether any such information was encoded linguistically.

The next useful bridge would join a particular inscription to independently
identified contents or an independently known quantity, while allowing for reuse,
mixed residues and sampling uncertainty. The parallel
[residue-source audit](RESIDUE_ANCHOR_AUDIT.md) checks whether published laboratory
sample records provide such a join.

## Preserved analysis

The [review ledger](../data/processed/sealing_function_review.json) separates
observations, source hypotheses, analytical domains and unknown values.
[`audit_sealing_function_anchors.py`](../scripts/audit_sealing_function_anchors.py)
verifies its evidence hashes and writes
[`sealing_function_anchors.json`](../results/sealing_function_anchors.json).
Three tests ensure that missing observations are not treated as contradictions,
that alternative classifications propagate, and that empty domains are rejected
as data errors. These checks validate the restricted calculation, not a reading.

All downloaded originals remain in `data/raw/`; renderings and provenance are
retained. No semantic or phonetic value has been assigned to any of the417 signs.
