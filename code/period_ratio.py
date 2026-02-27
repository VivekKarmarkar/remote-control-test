"""Plot the period ratio T(θ₀)/T₀ comparing SHM, exact elliptic integral, and RK4."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk
from rk4_pendulum import pendulum_ode, integrate, measure_period, G_DEFAULT, L_DEFAULT

g, L = G_DEFAULT, L_DEFAULT
omega0 = np.sqrt(g / L)
T0 = 2 * np.pi / omega0

# ── Exact elliptic integral curve ─────────────────────────
theta0_exact = np.linspace(0.5, 179.5, 1000)
theta0_rad = np.deg2rad(theta0_exact)
k = np.sin(theta0_rad / 2)
T_exact = 4 / omega0 * ellipk(k**2)   # ellipk takes m = k²
ratio_exact = T_exact / T0

# ── Quadratic approximation ──────────────────────────────
ratio_approx = 1 + theta0_rad**2 / 16

# ── RK4 numerical measurement ────────────────────────────
theta0_sample = np.arange(5, 176, 10)
ratio_numerical = []
for deg in theta0_sample:
    rad = np.deg2rad(deg)
    # Integrate for many periods
    t_end = max(20 * T0, 50)
    t, states = integrate(pendulum_ode, [rad, 0.0], (0, t_end), 0.001)
    T_measured = measure_period(t, states[:, 0])
    ratio_numerical.append(T_measured / T0)

ratio_numerical = np.array(ratio_numerical)

# ── Plot ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(theta0_exact, ratio_exact, "b-", linewidth=2.2, label="Exact (elliptic integral)")
ax.plot(theta0_exact, ratio_approx, "g--", linewidth=1.8,
        label=r"Approximation: $1 + \theta_0^2/16$")
ax.plot(theta0_sample, ratio_numerical, "ro", markersize=6, label="RK4 numerical measurement",
        zorder=5)

# Horizontal reference
ax.axhline(1.0, color="k", linewidth=0.5, linestyle=":")

# Annotations at key amplitudes
for deg, label_y in [(30, 1.02), (90, 1.18), (150, 1.76)]:
    idx = np.argmin(np.abs(theta0_exact - deg))
    r = ratio_exact[idx]
    pct = (r - 1) * 100
    ax.annotate(
        f"{deg}°: +{pct:.1f}%",
        xy=(deg, r), xytext=(deg + 8, r + 0.08),
        fontsize=10, fontweight="bold",
        arrowprops=dict(arrowstyle="->", lw=1.2),
    )

ax.set_xlabel(r"Initial amplitude $\theta_0$ (degrees)", fontsize=14)
ax.set_ylabel(r"Period ratio $T(\theta_0) / T_0$", fontsize=14)
ax.set_title("Period depends on amplitude: the failure of isochronism", fontsize=15)
ax.set_xlim(0, 180)
ax.set_ylim(0.95, 3.5)
ax.legend(fontsize=11, loc="upper left")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("../plots/fig_period_ratio.png", dpi=150, bbox_inches="tight")
print("Saved ../plots/fig_period_ratio.png")
