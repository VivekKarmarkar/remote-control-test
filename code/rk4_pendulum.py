"""
Core computational engine for the nonlinear pendulum.

Provides:
  - RK4 integrator
  - Pendulum ODE system
  - Period measurement via zero-crossing interpolation
  - Energy computation
"""

import numpy as np


# ── Physical parameters (defaults) ────────────────────────
G_DEFAULT = 9.81   # m/s²
L_DEFAULT = 1.0    # m


def pendulum_ode(state, _t, g=G_DEFAULT, L=L_DEFAULT):
    """Right-hand side of the pendulum ODE system.

    State: [theta, omega]
    Returns: [dtheta/dt, domega/dt]
    """
    theta, omega = state
    return np.array([omega, -(g / L) * np.sin(theta)])


def rk4_step(f, state, t, h, *args, **kwargs):
    """Single 4th-order Runge-Kutta step."""
    k1 = h * f(state, t, *args, **kwargs)
    k2 = h * f(state + k1 / 2, t + h / 2, *args, **kwargs)
    k3 = h * f(state + k2 / 2, t + h / 2, *args, **kwargs)
    k4 = h * f(state + k3, t + h, *args, **kwargs)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def integrate(f, state0, t_span, h, *args, **kwargs):
    """Integrate an ODE system using RK4.

    Returns (t_array, state_array) where state_array has shape (N, dim).
    """
    t_start, t_end = t_span
    t_vals = np.arange(t_start, t_end + h / 2, h)
    states = np.zeros((len(t_vals), len(state0)))
    states[0] = state0

    for i in range(1, len(t_vals)):
        states[i] = rk4_step(f, states[i - 1], t_vals[i - 1], h, *args, **kwargs)

    return t_vals, states


def compute_energy(theta, omega, g=G_DEFAULT, L=L_DEFAULT, m=1.0):
    """Total mechanical energy: E = ½mL²ω² + mgL(1 - cosθ)."""
    return 0.5 * m * L**2 * omega**2 + m * g * L * (1 - np.cos(theta))


def measure_period(t, theta):
    """Measure oscillation period from downward zero-crossings of θ(t).

    Uses linear interpolation between grid points for accuracy.
    Returns the average period, or np.inf if fewer than 2 crossings found.
    """
    crossings = []
    for i in range(1, len(theta)):
        if theta[i - 1] > 0 and theta[i] <= 0:
            # Linear interpolation for crossing time
            t_cross = t[i - 1] + (0 - theta[i - 1]) / (theta[i] - theta[i - 1]) * (t[i] - t[i - 1])
            crossings.append(t_cross)

    if len(crossings) < 2:
        return np.inf

    periods = np.diff(crossings)
    return np.mean(periods)
