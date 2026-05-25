"""
Minimal Emergent Phase Matter (EPM) simulation.

This is a dependency-free 1D toy model for an emergent phase-memory
structure field:

    Phi(x,t) = A(x,t) * exp(i theta_R(x,t))

The update is a simple reaction-diffusion style prototype:

    dPhi/dt = D laplacian(Phi) - V_eff(kappa, M) Phi - c |Phi|^2 Phi
    dM/dt   = xi |Phi|^2 - rho M

where:

    V_eff(kappa, M) = V0 + u*kappa - v*M

This is not a physical proof of new matter. It is a computational toy for
exploring stable phase-memory structures, localization, memory mass, and
winding-like phase persistence.

Run:
    python examples/minimal_epm_sim.py
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass


ComplexField = list[complex]
ScalarField = list[float]


@dataclass(frozen=True)
class EPMParameters:
    n: int = 256
    length: float = 1.0
    steps: int = 2500
    dt: float = 0.0008
    diffusion: float = 0.002
    nonlinear_saturation: float = 0.7
    memory_write: float = 1.2
    memory_decay: float = 0.06
    v0: float = 0.3
    curvature_coupling: float = 0.4
    memory_coupling: float = 0.9
    initial_winding: int = 2


def periodic_laplacian_complex(values: ComplexField, dx: float) -> ComplexField:
    n = len(values)
    return [
        (values[(i + 1) % n] - 2.0 * values[i] + values[(i - 1) % n]) / (dx * dx)
        for i in range(n)
    ]


def periodic_laplacian_scalar(values: ScalarField, dx: float) -> ScalarField:
    n = len(values)
    return [
        (values[(i + 1) % n] - 2.0 * values[i] + values[(i - 1) % n]) / (dx * dx)
        for i in range(n)
    ]


def initialize_phi(params: EPMParameters) -> tuple[list[float], ComplexField, ScalarField, ScalarField]:
    n = params.n
    x = [params.length * i / n for i in range(n)]

    # A localized amplitude bump with a phase winding around the periodic domain.
    phi: ComplexField = []
    memory: ScalarField = []
    kappa: ScalarField = []

    for xi in x:
        bump = math.exp(-((xi - 0.5) ** 2) / 0.006)
        background = 0.08
        amplitude = background + 0.95 * bump
        phase = 2.0 * math.pi * params.initial_winding * xi / params.length
        phi.append(amplitude * cmath.exp(1j * phase))

        # Memory and curvature start near the same region, so the first test has
        # a geometry-memory trap where a stable object can try to persist.
        memory.append(0.4 * bump)
        kappa.append(0.5 * math.exp(-((xi - 0.52) ** 2) / 0.012))

    return x, phi, memory, kappa


def phase_winding(phi: ComplexField) -> float:
    """Estimate total winding around the 1D periodic domain."""
    if not phi:
        return 0.0

    phases = [math.atan2(z.imag, z.real) for z in phi]
    total = 0.0
    for i in range(1, len(phases)):
        delta = phases[i] - phases[i - 1]
        while delta > math.pi:
            delta -= 2.0 * math.pi
        while delta < -math.pi:
            delta += 2.0 * math.pi
        total += delta

    # Closing segment.
    delta = phases[0] - phases[-1]
    while delta > math.pi:
        delta -= 2.0 * math.pi
    while delta < -math.pi:
        delta += 2.0 * math.pi
    total += delta

    return total / (2.0 * math.pi)


def localization_radius(x: list[float], phi: ComplexField) -> float:
    """Return a simple amplitude-weighted radius around the amplitude center."""
    weights = [abs(z) ** 2 for z in phi]
    total = sum(weights)
    if total <= 1e-12:
        return float("inf")

    center = sum(xi * wi for xi, wi in zip(x, weights)) / total
    variance = sum(wi * (xi - center) ** 2 for xi, wi in zip(x, weights)) / total
    return math.sqrt(max(variance, 0.0))


def run_simulation(params: EPMParameters | None = None) -> dict[str, float]:
    p = params or EPMParameters()
    x, phi, memory, kappa = initialize_phi(p)
    dx = p.length / p.n

    for _ in range(p.steps):
        lap_phi = periodic_laplacian_complex(phi, dx)
        # Smooth curvature slightly so the trap can spread rather than remain fixed.
        lap_kappa = periodic_laplacian_scalar(kappa, dx)

        next_phi: ComplexField = []
        next_memory: ScalarField = []
        next_kappa: ScalarField = []

        for i, z in enumerate(phi):
            amplitude2 = abs(z) ** 2
            v_eff = p.v0 + p.curvature_coupling * kappa[i] - p.memory_coupling * memory[i]

            # Toy EPM evolution: diffusion + adaptive potential + saturation.
            dz = (
                p.diffusion * lap_phi[i]
                - v_eff * z
                - p.nonlinear_saturation * amplitude2 * z
            )
            z_next = z + p.dt * dz
            next_phi.append(z_next)

            dm = p.memory_write * amplitude2 - p.memory_decay * memory[i]
            next_memory.append(max(0.0, memory[i] + p.dt * dm))

            # A tiny curvature relaxation/smoothing proxy.
            dk = 0.0004 * lap_kappa[i] - 0.01 * kappa[i] + 0.004 * amplitude2
            next_kappa.append(kappa[i] + p.dt * dk)

        phi = next_phi
        memory = next_memory
        kappa = next_kappa

    amp = [abs(z) for z in phi]
    memory_mass = sum(memory) * dx
    winding = phase_winding(phi)
    radius = localization_radius(x, phi)
    phase_coherence = abs(sum(phi)) / max(sum(amp), 1e-12)
    persistence_score = (abs(winding) + 1.0) * phase_coherence / max(radius, 1e-9)

    return {
        "amplitude_min": min(amp),
        "amplitude_max": max(amp),
        "amplitude_mean": sum(amp) / len(amp),
        "memory_mass": memory_mass,
        "winding_estimate": winding,
        "localization_radius": radius,
        "phase_coherence": phase_coherence,
        "persistence_score": persistence_score,
    }


if __name__ == "__main__":
    metrics = run_simulation()
    print("Minimal EPM simulation complete")
    for key, value in metrics.items():
        print(f"{key}: {value:.6f}")
