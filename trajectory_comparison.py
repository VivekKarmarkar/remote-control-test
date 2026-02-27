"""Compare SHM analytical solution with nonlinear RK4 solution at multiple amplitudes."""

import numpy as np
import matplotlib.pyplot as plt
from rk4_pendulum import pendulum_ode, integrate, G_DEFAULT, L_DEFAULT

g, L = G_DEFAULT, L_DEFAULT
omega0 = np.sqrt(g / L)
T0 = 2 * np.pi / omega0      # small-angle period
h = 0.001                     # RK4 step size

amplitudes_deg = [10, 90, 170]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)

for ax, theta0_deg in zip(axes, amplitudes_deg):
    theta0 = np.deg2rad(theta0_deg)
    t_end = 3 * T0
    t, states = integrate(pendulum_ode, [theta0, 0.0], (0, t_end), h)
    theta_num = states[:, 0]

    # Analytical SHM solution
    theta_shm = theta0 * np.cos(omega0 * t)

    ax.plot(t, np.rad2deg(theta_shm), "r--", linewidth=1.8, label="Small-angle (SHM)")
    ax.plot(t, np.rad2deg(theta_num), "b-", linewidth=1.8, label="Nonlinear (RK4)")
    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_title(rf"$\theta_0 = {theta0_deg}°$", fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="k", linewidth=0.4)

    # Shade the difference
    ax.fill_between(t, np.rad2deg(theta_shm), np.rad2deg(theta_num),
                     alpha=0.12, color="purple")

axes[0].set_ylabel(r"$\theta$ (degrees)", fontsize=12)
axes[0].legend(fontsize=9, loc="lower left")

fig.suptitle(
    "When does the small-angle approximation fail?",
    fontsize=15, y=1.02,
)
plt.tight_layout()
plt.savefig("fig_trajectory_comparison.png", dpi=150, bbox_inches="tight")
print("Saved fig_trajectory_comparison.png")
