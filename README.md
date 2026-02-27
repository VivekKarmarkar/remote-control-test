# When Simple Pendulums Get Complicated

**Why We Need Computers for Physics**

A 10-page report exploring the nonlinear pendulum — from the elegant small-angle solution to the full nonlinear dynamics that require numerical computation.

## Structure

```
├── report/
│   ├── pendulum_report.tex    # LaTeX source (10 pages)
│   └── pendulum_report.pdf    # Compiled PDF
├── code/
│   ├── rk4_pendulum.py        # Core RK4 integrator library
│   ├── pendulum_phase_portrait.py  # Phase portrait (Fig. 4)
│   ├── sin_theta_error.py     # Small-angle error plot (Fig. 1)
│   ├── trajectory_comparison.py    # SHM vs nonlinear θ(t) (Fig. 2)
│   └── period_ratio.py        # Period ratio T(θ₀)/T₀ (Fig. 3)
├── plots/
│   ├── fig_sin_error.png
│   ├── fig_trajectory_comparison.png
│   ├── fig_period_ratio.png
│   └── pendulum_phase_portrait.png
└── README.md
```

## Contents

The report covers:

1. **Equation of motion** — derived from Newton's second law
2. **Small-angle solution** — the simple harmonic oscillator, with a quantitative error analysis of sin θ ≈ θ
3. **Energy conservation** — derivation of the conserved energy and the separatrix formula
4. **Elliptic integrals** — scaffolded derivation of the exact period from energy conservation
5. **Phase-space analysis** — equilibria, stability via linearization (Jacobian/eigenvalues), and a regime classification table
6. **Numerical computation** — RK4 implementation, trajectory comparisons at 10°/90°/170°, period-vs-amplitude curves, and the full phase portrait

## Regenerating Figures

All scripts are in `code/` and output to `plots/`:

```bash
cd code
python3 sin_theta_error.py
python3 pendulum_phase_portrait.py
python3 trajectory_comparison.py
python3 period_ratio.py
```

Requirements: `numpy`, `matplotlib`, `scipy`

## Compiling the Report

```bash
cd report
pdflatex pendulum_report.tex
pdflatex pendulum_report.tex   # twice for cross-references
```

## Author

Written by **Claude Opus 4.6** with review feedback from a 10-agent analysis swarm (3 student agents, 3 teacher agents, 2 pedagogy experts, 2 data scientists).
