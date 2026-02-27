"""
Phase portrait of the nonlinear (large-angle) pendulum.

Equation of motion:  θ'' + (g/L) sin(θ) = 0

Rewritten as a first-order system:
    dθ/dt = ω
    dω/dt = -(g/L) sin(θ)
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
g = 9.81   # gravitational acceleration (m/s²)
L = 1.0    # pendulum length (m)

# --- Phase-space grid ---
theta = np.linspace(-2 * np.pi, 2 * np.pi, 400)
omega = np.linspace(-8, 8, 400)
THETA, OMEGA = np.meshgrid(theta, omega)

# Vector field: the right-hand side of the ODE system
dtheta_dt = OMEGA
domega_dt = -(g / L) * np.sin(THETA)

# Speed magnitude (used for colour mapping)
speed = np.sqrt(dtheta_dt**2 + domega_dt**2)

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 8))

# Streamlines coloured by speed in phase space
strm = ax.streamplot(
    THETA, OMEGA, dtheta_dt, domega_dt,
    color=speed, cmap="coolwarm", density=2.5,
    linewidth=0.7, arrowsize=0.7,
)
fig.colorbar(strm.lines, ax=ax, label="Phase-space speed")

# --- Separatrix ---
# Energy: E = ½L²ω² − gL cos θ
# At the unstable equilibrium (θ=±π, ω=0): E_sep = gL
# So the separatrix satisfies: ω = ±√(2g/L · (1 + cos θ))
theta_sep = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
omega_sep = np.sqrt(2 * g / L * np.maximum(1 + np.cos(theta_sep), 0))

ax.plot(theta_sep, omega_sep, "k--", linewidth=1.8, label="Separatrix")
ax.plot(theta_sep, -omega_sep, "k--", linewidth=1.8)

# --- Equilibrium points ---
for n in range(-2, 3):
    if n % 2 == 0:  # stable: θ = 0, ±2π (hanging down)
        ax.plot(n * np.pi, 0, "o", color="#2ecc71", markersize=9, zorder=5,
                label="Stable eq." if n == 0 else "")
    else:            # unstable: θ = ±π (inverted)
        ax.plot(n * np.pi, 0, "o", color="#e74c3c", markersize=9, zorder=5,
                label="Unstable eq." if n == 1 else "")

# --- Labels & formatting ---
ax.set_xlabel("θ  (rad)", fontsize=14)
ax.set_ylabel("ω  (rad/s)", fontsize=14)
ax.set_title("Phase Portrait — Nonlinear Pendulum  θ″ + (g/L) sin θ = 0",
             fontsize=15, pad=12)
ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
ax.set_xticklabels(["−2π", "−π", "0", "π", "2π"], fontsize=12)
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.set_ylim(-8, 8)
ax.axhline(0, color="k", linewidth=0.4)
ax.axvline(0, color="k", linewidth=0.4)
ax.legend(fontsize=11, loc="upper right")

plt.tight_layout()
plt.savefig("../plots/pendulum_phase_portrait.png", dpi=150, bbox_inches="tight")
print("Saved ../plots/pendulum_phase_portrait.png")
