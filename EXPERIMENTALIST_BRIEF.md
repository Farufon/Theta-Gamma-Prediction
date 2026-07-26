# For the Experimentalist: The Protocol

## Thesis

Entangled particles held unmeasured across a gravitational gradient accumulate phase diffusion via a proposed non-unitary stabilization mechanism. After proper-time compensation, this produces a residual CHSH deficit that standard relativistic QM does not predict.

## Epistemic Status, Stated Plainly

Tier one, measured: gravitational time dilation (optical clock experiments), Bell violations (loophole-free tests), and the standard-QM prediction that compensation fully restores correlations.

Tier two, proposed: the non-unitary stabilization mechanism and its saturating signature. That is what this protocol tests.

Nothing below requires accepting any interpretation of quantum mechanics. The protocol is interpretation-neutral; it asks only whether a specific number deviates from a specific bound.

## The Experiment (in principle)

1. Prepare entangled particles (e.g., via Raman beamsplitters in an atom fountain).
2. Separate them vertically: one at height 0, one at height H.
3. Let them evolve unmeasured for time t.
4. Bring the measurement records together.
5. Apply full proper-time compensation (rotate bases to undo deterministic gravitational phase skew).
6. Measure CHSH correlation S.

## Standard QM Prediction

S = 2 root 2, approximately 2.828 (Tsirelson's bound), independent of H and t after compensation.

## Theta-Gamma Prediction

S = 2 root 2 times exp(minus sigma squared over 2)

where sigma squared (t, H) is proportional to (g H / c squared) times f(t):

- g H / c squared is the fractional redshift, a measured quantity from general relativity
- f(t) is a saturation function: linear at small t, plateau at large t, with characteristic timescale tau_sat
- The proportionality constant kappa is a free parameter of the framework

## Expected Magnitude of kappa

The framework's honest position: kappa should be very small. Three lines of reasoning support this expectation.

1. **Existing constraints.** Clean Bell-test results and precision clock comparisons across height differences have not reported anomalous residual decoherence. A large kappa would already have appeared as unexplained noise. It has not, so kappa is already implicitly bounded by the archive.
2. **The pattern of real corrections.** Genuine corrections in physics, the Lamb shift, the anomalous magnetic moment, are typically small refinements to established predictions rather than large deviations.
3. **Everyday stability.** Entanglement does not routinely collapse across mundane gravitational gradients. If it did, quantum technology as practiced would already be in trouble.

The practical consequence: this is a hunt for a small, specific signal, not a dramatic effect. Existing datasets (Micius satellite entanglement distribution, laboratory atom interferometry) may already constrain kappa from above, which would itself be a publishable analysis before any new apparatus is built.

## What to Look For

**If Theta-Gamma is right:**
- S stays near 2.828 for short t
- S drops as t increases
- S levels off at a floor, no longer decreasing
- The floor is lower for larger H
- The approach to the floor has a characteristic saturation timescale tau_sat

**If standard QM is right:**
- S = 2.828 at all t and all H after compensation
- Any deviations trace to experimental error or environmental decoherence, which grows without bound

## The Distinguishing Feature

Saturation. Theta-Gamma predicts a knee. Standard QM predicts a flat line. Environmental decoherence predicts monotonic decay without a floor. These are experimentally separable.

## What Your Data Determines

- **Saturation matching the curve:** kappa is measurable. The framework has its first empirical anchor.
- **S = 2.828 within error:** kappa is bounded toward zero. The framework's central empirical claim is falsified or negligible at your sensitivity. This is a publishable constraint, not a null waste.
- **Unbounded decay:** ordinary decoherence dominates; the framework's effect, if present, is below your floor.

## Accessible Platforms

- **Atom fountains:** 1 m to 10 m separations, existing infrastructure
- **Long-baseline quantum interferometry:** kilometer-class separations, extreme precision
- **Transportable optical clocks:** meters of separation, extreme sensitivity to gravitational frequency shift
- **Archival reanalysis:** existing entanglement-distribution datasets across altitude differences, for an upper bound on kappa at zero new hardware cost

## The Honest Caveat

This is a proposal about time's role, not a competing quantum theory. Standard QM's mathematics is unchanged. The claim is narrower: how that mathematics gets applied across gravitational potentials may require a non-unitary stabilization step, and that step has a signature.

If you run this and find nothing, standard QM's picture of entanglement across gradients is vindicated and kappa carries a new bound. If you find the saturation curve, you have found something that opens a new line of inquiry into time's structure.

## Next Steps

1. Run theta_gamma_sim.py to see the target curve
2. Assess whether existing apparatus reaches the relevant H and t parameter space
3. Consider whether archival data already bounds kappa
4. Design the compensation protocol and the CHSH measurement
5. Measure, then publish the bound or the detection

Contact: Jon Farhat (framework) / Claude, Anthropic (simulation) / Your judgment (experiment)
