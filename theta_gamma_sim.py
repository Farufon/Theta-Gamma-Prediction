"""
THETA-GAMMA DIVERGENT PREDICTION SIMULATION
Jon A. Farhat framework / simulation by Claude, July 2026

THE EXPERIMENT (in principle):
Prepare entangled particle pairs. Hold one at height 0, one at height H,
for unobserved duration t. Bring measurement records together, apply full
proper-time compensation (rotate bases to undo the deterministic
gravitational phase skew), then measure CHSH correlation S.

THE TWO PREDICTIONS:
  Standard relativistic QM:
      The gravitational phase skew is deterministic and unitary.
      After compensation, S returns to Tsirelson's bound, 2*sqrt(2).
      Residual deficit: ZERO (up to ordinary environmental decoherence,
      which is apparatus-dependent and can be engineered down).

  Theta-Gamma:
      Phase stabilization (Theta -> Gamma) is NOT unitary (Farhat,
      "Response to Chalmers", Phase Stabilization, rule four).
      Curvature modulates stabilization tempo. A pair held across a
      gravitational gradient stabilizes at two different tempos, and the
      tempo MISMATCH injects irreversible phase diffusion that no
      compensation can undo.
      After compensation, S = 2*sqrt(2) * exp(-sigma^2/2) < 2*sqrt(2).

THE MODEL:
      sigma^2(t, H) = kappa * (g*H/c^2) * tau_sat * (1 - exp(-t/tau_sat))
      kappa    : dimensionless coupling, THE FREE PARAMETER of the theory.
                 The framework does not yet derive it. Honesty requires
                 saying so: this simulation demonstrates the STRUCTURE and
                 FUNCTIONAL FORM of the divergence, not its magnitude.
      g*H/c^2  : fractional redshift between the two sites (measured physics).
      tau_sat  : saturation timescale. Farhat's Q1 answer: the skew effect
                 saturates once Theta exploration is fully differentiated
                 by the metric. Linear at small t, plateau at large t.

WHAT WOULD FALSIFY WHAT:
      Find S = 2*sqrt(2) restored to experimental precision after
      compensation at large g*H*t product  ->  kappa bounded toward zero,
      Theta-Gamma's non-unitary stabilization is falsified or negligible.
      Find a residual deficit matching the saturation curve  ->  standard
      QM has an anomaly and Theta-Gamma has a measured coupling constant.
"""

import numpy as np

RNG = np.random.default_rng(20260708)

# ---------- physical constants (SI) ----------
G_EARTH = 9.80665          # m/s^2
C_LIGHT = 2.99792458e8     # m/s

# ---------- CHSH machinery ----------
# Singlet state correlation with a relative phase error delta on one arm:
# E(a, b) = -cos(a - b + delta). Optimal CHSH angles give S = 2*sqrt(2)
# when delta = 0. Random Gaussian delta (the irreversible diffusion)
# attenuates the correlation by exp(-sigma^2 / 2) on average.

CHSH_ANGLES = dict(a=0.0, a_prime=np.pi/2, b=np.pi/4, b_prime=-np.pi/4)

def chsh_S(deltas):
    """Monte Carlo CHSH value given an array of per-pair phase errors."""
    a, ap, b, bp = (CHSH_ANGLES[k] for k in ("a", "a_prime", "b", "b_prime"))
    def E(x, y):
        return np.mean(-np.cos(x - y + deltas))
    return abs(E(a, b) + E(a, bp) + E(ap, b) - E(ap, bp))

# ---------- the two models ----------
def sigma2_theta_gamma(t, height, kappa, tau_sat):
    """Irreversible phase variance accumulated across the gradient.
    Linear in redshift fraction, saturating in exposure time."""
    redshift_fraction = G_EARTH * height / C_LIGHT**2
    return kappa * redshift_fraction * tau_sat * (1.0 - np.exp(-t / tau_sat))

def run_experiment(t, height, kappa, tau_sat, n_pairs=200_000):
    """Returns (S_standard, S_theta_gamma) after full compensation."""
    # Standard QM: deterministic skew fully compensated -> delta = 0 exactly.
    S_std = chsh_S(np.zeros(n_pairs))
    # Theta-Gamma: deterministic part compensated, diffusion part cannot be.
    s2 = sigma2_theta_gamma(t, height, kappa, tau_sat)
    deltas = RNG.normal(0.0, np.sqrt(s2), n_pairs)
    S_tg = chsh_S(deltas)
    return S_std, S_tg, s2

# ---------- sweep ----------
def main():
    TSIRELSON = 2 * np.sqrt(2)

    # Free parameters, stated as such. kappa chosen ONLY so the effect is
    # visible on these axes; the theory must eventually derive it.
    kappa   = 1.0e11        # dimensionless coupling (FREE PARAMETER)
    tau_sat = 100.0         # seconds (FREE PARAMETER)

    print(f"Tsirelson bound (both theories at t=0): {TSIRELSON:.6f}")
    print(f"Free parameters: kappa={kappa:.2e}, tau_sat={tau_sat} s")
    print("kappa is NOT derived by the framework. Functional form is the "
          "prediction;\nmagnitude awaits a derivation or a measurement.\n")

    print("=" * 76)
    print("SWEEP 1: exposure time at fixed height H = 1000 m")
    print("=" * 76)
    print(f"{'t (s)':>8} | {'S standard':>11} | {'S Theta-Gamma':>13} | "
          f"{'deficit':>9} | {'sigma^2':>10}")
    for t in [0.1, 1, 3, 10, 30, 100, 300, 1000]:
        S_std, S_tg, s2 = run_experiment(t, 1000.0, kappa, tau_sat)
        print(f"{t:>8.1f} | {S_std:>11.5f} | {S_tg:>13.5f} | "
              f"{S_std - S_tg:>9.5f} | {s2:>10.4e}")

    print()
    print("=" * 76)
    print("SWEEP 2: height at fixed exposure t = 100 s")
    print("=" * 76)
    print(f"{'H (m)':>8} | {'S standard':>11} | {'S Theta-Gamma':>13} | "
          f"{'deficit':>9} | {'sigma^2':>10}")
    for h in [1, 10, 100, 1000, 10_000, 100_000]:
        S_std, S_tg, s2 = run_experiment(100.0, h, kappa, tau_sat)
        print(f"{h:>8.0f} | {S_std:>11.5f} | {S_tg:>13.5f} | "
              f"{S_std - S_tg:>9.5f} | {s2:>10.4e}")

    print()
    print("=" * 76)
    print("THE SIGNATURE, in one sentence")
    print("=" * 76)
    print("Standard QM: after proper-time compensation the CHSH value returns\n"
          "to 2*sqrt(2) regardless of H and t.\n"
          "Theta-Gamma: a residual deficit remains, linear in g*H/c^2,\n"
          "saturating in t with timescale tau_sat, and NO compensation\n"
          "protocol removes it, because stabilization was never unitary.\n\n"
          "That saturation knee is the fingerprint. Ordinary decoherence\n"
          "grows without bound; this plateaus. An experimentalist can tell\n"
          "them apart.")

if __name__ == "__main__":
    main()
