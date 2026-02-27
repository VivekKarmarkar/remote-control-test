"""Plot the fractional error of the small-angle approximation sin θ ≈ θ."""

import numpy as np
import matplotlib.pyplot as plt

theta_deg = np.linspace(0.5, 180, 2000)
theta_rad = np.deg2rad(theta_deg)

sin_theta = np.sin(theta_rad)
error_frac = np.abs(theta_rad - sin_theta) / np.abs(sin_theta) * 100  # percent

# ── Main figure ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(theta_deg, error_frac, "b-", linewidth=2)
ax.set_xlabel(r"$\theta$ (degrees)", fontsize=14)
ax.set_ylabel("Relative error  (%)", fontsize=14)
ax.set_title(r"How good is $\sin\theta \approx \theta$?", fontsize=15)
ax.set_xlim(0, 180)
ax.set_ylim(0, 60)
ax.grid(True, alpha=0.3)

# Threshold annotations
thresholds = [(1, "1%"), (5, "5%"), (10, "10%")]
colors = ["#2ecc71", "#f39c12", "#e74c3c"]
for (pct, label), color in zip(thresholds, colors):
    idx = np.argmin(np.abs(error_frac - pct))
    deg_val = theta_deg[idx]
    ax.axvline(deg_val, color=color, linestyle="--", linewidth=1.2, alpha=0.8)
    ax.annotate(
        f"{label} error at {deg_val:.0f}°",
        xy=(deg_val, pct), xytext=(deg_val + 8, pct + 6),
        fontsize=11, color=color, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
    )

# ── Inset: sin(θ) vs θ ───────────────────────────────────
ax_inset = fig.add_axes([0.18, 0.50, 0.35, 0.38])
theta_inset = np.linspace(0, np.pi, 500)
ax_inset.plot(np.rad2deg(theta_inset), np.sin(theta_inset), "b-", linewidth=2, label=r"$\sin\theta$")
ax_inset.plot(np.rad2deg(theta_inset), theta_inset, "r--", linewidth=2, label=r"$\theta$")
ax_inset.fill_between(
    np.rad2deg(theta_inset), np.sin(theta_inset), theta_inset,
    alpha=0.15, color="red",
)
ax_inset.set_xlabel(r"$\theta$ (deg)", fontsize=10)
ax_inset.set_ylabel("Value", fontsize=10)
ax_inset.legend(fontsize=10, loc="upper left")
ax_inset.set_xlim(0, 180)
ax_inset.set_ylim(0, 3.5)
ax_inset.grid(True, alpha=0.3)
ax_inset.set_title(r"$\sin\theta$ vs $\theta$ (radians)", fontsize=10)

plt.tight_layout()
plt.savefig("fig_sin_error.png", dpi=150, bbox_inches="tight")
print("Saved fig_sin_error.png")
