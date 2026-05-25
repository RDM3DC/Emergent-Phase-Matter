# Emergent Phase Matter (EPM)

**Standalone White Paper**  
**Canonical Core Arm:** 08  
**Date:** 2026-05-25  
**Status:** Draft scaffold

---

## Abstract

Emergent Phase Matter (EPM) studies stable structures that can emerge from adaptive phase-memory geometry. The framework begins after adaptive conductance, curvature, phase, and memory have been coupled through ARP/AIN, Adaptive-π Geometry, Curve Memory, Phase-Lift, ACFN, and PMT.

EPM does not claim the discovery of confirmed new particles or matter. It defines a computational and mathematical layer for persistent structures such as phase knots, memory vortices, adaptive solitons, and geometry-locked islands.

---

## 1. Core Idea

The guiding formula is:

```text
stable structure = adaptation + curvature + phase + memory + topology
```

A structure becomes matter-like when it has:

1. localization
2. persistence
3. resistance to perturbation
4. identity through time
5. a conserved or quasi-conserved topological marker

---

## 2. Effective Field

Let `Φ(x,t)` represent an emergent phase-memory structure:

```text
Φ(x,t) = A(x,t) exp(iθ_R(x,t))
```

where:

- `A` is amplitude or density
- `θ_R` is resolved phase
- `M` is memory density
- `κ` is curvature

This field is not assumed to be quantum mechanical. It is an effective field for tracking stable adaptive structures.

---

## 3. Stability Condition

A minimal stability condition is:

```text
δE_adaptive / δΦ = 0
```

subject to:

```text
W ≠ 0
```

where `W` is a winding, closure, parity, or topological marker.

Interpretation:

```text
the structure survives because its phase-memory loop cannot easily unwind.
```

---

## 4. Prototype Energy

A first adaptive energy functional is:

```text
E = ∫ [a|∇Φ|² + bV(κ,M)|Φ|² + c|Φ|⁴ + d|∇θ|²] dx
```

with:

```text
V(κ,M) = V₀ + uκ − vM
```

Interpretation:

- `|∇Φ|²` penalizes sharp boundaries
- `V(κ,M)` encodes adaptive geometry-memory potential
- `|Φ|⁴` creates nonlinear saturation
- `|∇θ|²` tracks phase strain

---

## 5. Topological Closure

A phase-memory structure can persist when phase returns consistently around a loop:

```text
∮ ∇θ_R · dl = 2πₐ W
```

where:

- `θ_R` is resolved phase
- `πₐ` is adaptive phase-period field
- `W` is winding

This connects EPM to Phase-Lift and Adaptive-π Geometry.

---

## 6. Classes of EPM Structures

### Phase Knots

Closed phase-memory loops with nonzero winding.

### Memory Vortices

Localized circulating memory structures where repeated phase transport reinforces a core.

### Adaptive Solitons

Localized packets stabilized by a balance between spreading, curvature, and memory feedback.

### Geometry-Locked Islands

Regions where curvature and memory form a local trap for phase transport.

---

## 7. Persistence Metrics

Possible diagnostics:

```text
T_persist  → lifetime
W          → winding/topology marker
∫M dx      → memory mass
C_phase    → phase coherence
R_eff      → localization radius
```

A first heuristic persistence score:

```text
S_EPM = T_persist · |W| · C_phase / R_eff
```

This is a simulation metric, not a fundamental constant.

---

## 8. Minimal Simulation Target

A toy EPM simulation should begin with `Φ`, `θ`, `M`, and `κ`:

```text
Φ_t = D∇²Φ − ∂V_eff(Φ,κ,M,θ)/∂Φ
```

Track regions where:

```text
|Φ| remains localized
M remains high
W remains nonzero
```

Expected visible behavior:

```text
persistent phase-memory structures
```

---

## 9. Canonical Claim

EPM does not claim confirmed new matter.

The canonical claim is:

```text
EPM defines a framework for stable emergent structures in adaptive phase-memory geometry.
```

---

## 10. Next Work

- Build toy 1D and 2D simulations
- Define winding diagnostics
- Test memory-vortex formation
- Couple EPM to PMT phase transport
- Couple EPM to ACFN curvature fields
- Explore AdaptiveCAD primitives based on stable phase-memory geometry
