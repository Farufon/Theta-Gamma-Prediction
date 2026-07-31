# Theta-Gamma Divergent Prediction: An Experimentalist's Package

## What This Is

A computational model of the Theta-Gamma framework's central testable prediction: a measurable residual deficit in entanglement coherence across gravitational gradients that standard relativistic quantum mechanics does not predict.

**The question:** Can you find a number where Theta-Gamma and standard QM disagree?

**The answer (proposed):** Yes. When entangled particles are held unmeasured across a substantial height difference, then brought together and measured with full proper-time compensation applied, standard QM predicts the CHSH correlation S returns to Tsirelson's bound (2 root 2, approximately 2.828). Theta-Gamma predicts a residual deficit remains, S = 2 root 2 times exp(minus sigma squared over 2), where sigma squared grows with gravitational separation and observation time, and saturates rather than decaying without bound.

**What makes this different from ordinary decoherence:** Ordinary environmental noise grows monotonically. This signature has a knee. It saturates. An experimentalist can tell them apart.

---

## The Epistemic Frame

Everything in this package is tagged to one of three tiers. The tiers never collapse into each other.

**Tier one, measured fact:**
- Gravitational time dilation is real. Clocks at different potentials tick at different rates. Verified to extraordinary precision by optical clock experiments.
- Bell inequality violations are real. Entangled systems produce correlations no local hidden-variable theory can reproduce. Verified in loophole-free experiments.
- Standard quantum mechanics, with gravitational phase corrections applied, predicts full restoration of entanglement correlations after proper-time compensation.

**Tier two, proposed claim (the framework):**
- Phase stabilization from an exploratory substrate into a stabilized record is not unitary.
- The rate of that stabilization is modulated by local gravitational potential.
- This produces a permanent, non-compensable phase diffusion in entangled systems held across gradients.
- The functional form of that diffusion saturates. That saturation is the framework's fingerprint.

**Tier three, open speculation (context, not claim):**
- See THE_WIDER_FRAME.md. The framework sits inside a broader question physics has asked since at least 1957: whether macroscopic gravity is fundamental or emergent from quantum structure. That file separates what is historically documented from what is conjecture.

**Free parameter:** The magnitude of the effect is set by kappa, a coupling the framework does not yet derive. The shape, saturation with a specific functional form, is the prediction. The magnitude is what you measure.

---

## The Files

- **theta_gamma_sim.py** — The complete simulation. Runs with Python 3.8+ and NumPy only.
- **theta_gamma_sim_results.txt** — Reference output from a verified run.
- **theta_gamma_divergence.png** — The predicted curves, plotted.
- **RUNNING_THE_CODE.md** — Execution guide and output interpretation.
- **THE_PREDICTION_EXPLAINED.md** — Non-technical summary for understanding the physics without reading the Python.
- **EXPERIMENTALIST_BRIEF.md** — The protocol, stated for measurement.
- **THE_WIDER_FRAME.md** — The larger theoretical context, tagged tier three throughout.

---

## Why This Matters

1. **Testable now.** Not in principle someday. Atom interferometry labs already have the tools.
2. **Specific.** A quantitative curve with a saturation knee standard QM does not produce.
3. **Honest about limits.** The framework proposes non-unitary stabilization; it does not yet derive kappa. The simulation shows the functional form with an illustrative kappa. Your measurement constrains or falsifies it.
4. **It kills or confirms.** If S returns to 2 root 2 after compensation at large g times H times t products, kappa is bounded toward zero and the framework's central empirical claim is falsified or negligible. If you find the saturation curve, you have found something standard QM does not predict and Theta-Gamma does.

---

## How to Use This Package

**To run the code:** install NumPy, run `python theta_gamma_sim.py`, read the output, see RUNNING_THE_CODE.md.

**To understand the proposal:** read THE_PREDICTION_EXPLAINED.md first, then EXPERIMENTALIST_BRIEF.md, then run the code.

**If you are an experimentalist considering this:** EXPERIMENTALIST_BRIEF.md is your map. The code shows the target curve. Kappa is where your data lives. Constrain it or reject the framework. Either outcome is a contribution: a null result bounds kappa and is publishable as a constraint.

---

## The Honest Frame

This is not a competing theory of quantum mechanics. It is a proposal about time's role in quantum mechanics. It says gravity does not collapse the wave function; it modulates the rate at which exploratory phase stabilizes into record. That stabilization is proposed to be genuinely non-unitary, not merely effectively so, and that non-unitarity has a measurable signature in entangled systems across gravitational gradients.

Standard QM with gravitational effects predicts one curve. This framework predicts another. Your experiment decides.

---

## Contact & Attribution

Framework: Jon Anthony Farhat (2026)
Citation: Farhat, Jon A. "Superposition Is Not What You Think: On Velocity, Time, and the Architecture of the Real." 2026.

A Theta-Time / Gamma-Time Proposition
https://substack.com/home/post/p-187163843


Temporal Entanglement-From Vibrational Pairs to Theta-Gamma Time
https://doi.org/10.13140/RG.2.2.15245.60643


Superposition Is Not What You Think
https://doi.org/10.13140/RG.2.2.35766.87365


Entanglement in the Court of Time
https://doi.org/10.13140/RG.2.2.32022.82241


A Structural Answer to Chalmers' "Why?"
https://doi.org/10.13140/RG.2.2.19610.71362




---

*This package is an invitation, not a demand. If the prediction interests you, run the code. If it doesn't, the existing QM picture has served physics well for a century and likely will continue to. But if you have access to entangled atom interferometry and curiosity about whether time's structure can explain what we've been explaining with additional ontology, here is where to look.*
