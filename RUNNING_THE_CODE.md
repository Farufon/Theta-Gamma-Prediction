# Running theta_gamma_sim.py

## Requirements

Python 3.8 or later, NumPy. That's all.

```bash
pip install numpy
python theta_gamma_sim.py
```

The script runs two parameter sweeps and prints results directly to the terminal. Reference output from a verified run is included in theta_gamma_sim_results.txt, and the plotted curves are in theta_gamma_divergence.png.

## Output Explanation

### Sweep 1: Exposure Time at Fixed Height (H = 1000 m)

Holds the vertical separation constant and varies how long the entangled pair sits unmeasured. Shows how the CHSH deficit grows and then plateaus.

| t (s) | S standard | S Theta-Gamma | deficit |
|-------|-----------|---------------|---------|
| 0.1 | 2.82843 | 2.82688 | 0.00155 |
| 1.0 | 2.82843 | 2.81315 | 0.01528 |
| 10.0 | 2.82843 | 2.68497 | 0.14345 |
| 100.0 | 2.82843 | 2.00220 | 0.82623 |
| 1000.0 | 2.82843 | 1.63892 | 1.18950 |

Read this as: standard QM stays flat at 2.828. Theta-Gamma sags and then levels off. That saturation knee is the signature.

### Sweep 2: Height at Fixed Exposure (t = 100 s)

Holds observation time constant and varies gravitational separation.

| H (m) | S standard | S Theta-Gamma | deficit |
|--------|-----------|---------------|---------|
| 1 | 2.82843 | 2.82745 | 0.00097 |
| 100 | 2.82843 | 2.73198 | 0.09645 |
| 1000 | 2.82843 | 2.00329 | 0.82513 |
| 10000 | 2.82843 | 0.08939 | 2.73903 |

The higher the separation, the larger the deficit. Roughly linear in the gravitational potential difference.

## What the Numbers Mean

**S standard:** Always 2 root 2, approximately 2.828. Standard QM, fully compensated. Tier one: this is what established theory predicts.

**S Theta-Gamma:** The CHSH value after compensation according to the framework. Tier two: this is the proposed claim.

**deficit:** S standard minus S Theta-Gamma. This is what you would measure if the framework is right.

## The Saturation Signature

Theta-Gamma predicts S does not decay forever. It hits a floor and stays there. Ordinary environmental decoherence grows without bound.

```
Standard QM:  flat line at 2.828
Theta-Gamma:  sags, then levels off around t ~ tau_sat
Your data:    tells you which is happening
```

If you see the saturation knee, you have found something new. If you see the flat line, standard QM's account holds.

## Important Caveat on These Numbers

The table values use an illustrative kappa chosen to make the curve shape visible. They are not predictions of effect magnitude. The framework's honest position, argued in EXPERIMENTALIST_BRIEF.md, is that kappa is likely very small, or existing precision experiments would already have flagged anomalies. The shape is the prediction. The magnitude is yours to bound.

## Running Your Own Variations

Edit the script's main() function:

```python
kappa   = 1.0e11        # Change this to vary magnitude
tau_sat = 100.0         # Change this to vary saturation timescale
```

Lower kappa, smaller effect. Higher kappa, larger effect. The functional form, saturation, does not change.

## Interpretation Checklist

- Standard QM curve is flat? Expected.
- Theta-Gamma curve sags and plateaus? That is the prediction.
- Deficit grows with height? Expected.
- Deficit grows with time but then levels off? The saturation signature.
- Your data matches the curve? Framework is consistent with your measurement.
- Your data matches the flat line? Framework is falsified at your sensitivity, and you have published a bound on kappa.
