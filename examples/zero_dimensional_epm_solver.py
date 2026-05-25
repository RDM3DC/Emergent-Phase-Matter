"""
Zero-dimensional Emergent Phase Matter (EPM) solver.

This solves the reduced amplitude-memory system from the proof package:

    dX/dt = 2(s0 + v*M - c*X)X
    dM/dt = xi*X - rho*M

where X = |Phi|^2 >= 0.

The nonzero equilibrium is:

    X* = s0 / (c - v*xi/rho)
    M* = (xi/rho) X*

when:

    s0 > 0 and c*rho > v*xi.

Run:
    python examples/zero_dimensional_epm_solver.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ZeroDEPMParameters:
    s0: float = 0.25
    v: float = 0.4
    c: float = 1.0
    xi: float = 0.5
    rho: float = 0.8
    dt: float = 0.002
    steps: int = 10000
    initial_x: float = 0.05
    initial_memory: float = 0.0


def equilibrium(params: ZeroDEPMParameters) -> dict[str, float | bool]:
    denom = params.c - params.v * params.xi / params.rho
    exists = params.s0 > 0.0 and params.c * params.rho > params.v * params.xi
    if not exists or abs(denom) < 1e-12:
        return {"exists": False, "X_star": 0.0, "M_star": 0.0}

    x_star = params.s0 / denom
    m_star = (params.xi / params.rho) * x_star
    return {"exists": True, "X_star": x_star, "M_star": m_star}


def stability_condition(params: ZeroDEPMParameters) -> dict[str, float | bool]:
    margin = params.c * params.rho - params.v * params.xi
    return {
        "stable_nonzero_possible": params.s0 > 0.0 and margin > 0.0,
        "stability_margin_c_rho_minus_v_xi": margin,
    }


def run_solver(params: ZeroDEPMParameters | None = None) -> dict[str, float | bool]:
    p = params or ZeroDEPMParameters()
    x = max(0.0, p.initial_x)
    m = max(0.0, p.initial_memory)

    max_x = x
    max_m = m

    for _ in range(p.steps):
        dx = 2.0 * (p.s0 + p.v * m - p.c * x) * x
        dm = p.xi * x - p.rho * m

        x = max(0.0, x + p.dt * dx)
        m = max(0.0, m + p.dt * dm)

        max_x = max(max_x, x)
        max_m = max(max_m, m)

    eq = equilibrium(p)
    stable = stability_condition(p)

    x_star = float(eq["X_star"])
    m_star = float(eq["M_star"])
    distance_to_equilibrium = ((x - x_star) ** 2 + (m - m_star) ** 2) ** 0.5

    return {
        **eq,
        **stable,
        "final_X": x,
        "final_M": m,
        "max_X": max_x,
        "max_M": max_m,
        "distance_to_equilibrium": distance_to_equilibrium,
    }


if __name__ == "__main__":
    result = run_solver()
    print("Zero-dimensional EPM solver complete")
    for key, value in result.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value:.8f}")
