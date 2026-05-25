# EPM Proof and Solution Package

**Repository:** Emergent-Phase-Matter  
**Canonical Core Arm:** 08  
**Date:** 2026-05-25  
**Status:** Mathematical working draft

---

## 0. Purpose

This document turns Emergent Phase Matter (EPM) from a concept into a proof program.

The goal is not to prove that nature contains new matter. The goal is to prove what can be proven inside the EPM model:

1. the toy equations are mathematically well-posed under reasonable assumptions,
2. memory remains nonnegative,
3. the EPM energy decreases for frozen memory/curvature gradient flow,
4. stable nonzero structures exist in reduced models,
5. winding/topological identity is protected unless the field vanishes or the branch structure breaks,
6. adaptive conservation accounting can be attached to EPM observables.

---

## 1. Minimal EPM Model

Let `Ω` be a bounded spatial domain. The main EPM field is a complex field

```text
Φ(x,t) = A(x,t) exp(i θ_R(x,t))
```

with memory `M(x,t)` and curvature proxy `κ(x,t)`.

A minimal EPM energy is

```text
E[Φ; κ, M] = ∫Ω [ a |∇Φ|²/2 + r(x,t)|Φ|²/2 + c |Φ|⁴/4 ] dx
```

where

```text
r(x,t) = V0 + uκ(x,t) − vM(x,t)
```

and constants satisfy

```text
a > 0, c > 0, V0,u,v ≥ 0.
```

The simplest gradient-flow dynamics are

```text
∂Φ/∂t = a ΔΦ − r(x,t)Φ − c|Φ|²Φ
```

with memory law

```text
∂M/∂t = ξ|Φ|² − ρM
```

where

```text
ξ ≥ 0, ρ > 0.
```

---

## 2. Theorem: Memory Positivity

### Statement

If

```text
M(x,0) ≥ 0
```

and

```text
∂M/∂t = ξ|Φ|² − ρM
```

with `ξ ≥ 0`, `ρ > 0`, then

```text
M(x,t) ≥ 0
```

for all `t ≥ 0`.

### Proof

For each fixed `x`, the memory equation is a linear ODE:

```text
dM/dt + ρM = ξ|Φ|².
```

Using an integrating factor:

```text
M(t) = e^{-ρt}M(0) + ∫0^t e^{-ρ(t-s)} ξ|Φ(s)|² ds.
```

Both terms are nonnegative because `M(0) ≥ 0`, `ξ ≥ 0`, and `|Φ|² ≥ 0`.

Therefore:

```text
M(t) ≥ 0.
```

QED.

---

## 3. Theorem: Memory Boundedness Under Bounded Field Amplitude

### Statement

If

```text
|Φ(x,t)|² ≤ B
```

for all `x,t`, then

```text
M(x,t) ≤ e^{-ρt}M(x,0) + (ξB/ρ)(1 − e^{-ρt}).
```

In particular,

```text
limsup_{t→∞} M(x,t) ≤ ξB/ρ.
```

### Proof

From the exact memory solution:

```text
M(t) = e^{-ρt}M(0) + ∫0^t e^{-ρ(t-s)} ξ|Φ(s)|² ds.
```

Using `|Φ|² ≤ B`,

```text
M(t) ≤ e^{-ρt}M(0) + ξB∫0^t e^{-ρ(t-s)} ds.
```

The integral equals `(1 − e^{-ρt})/ρ`, so

```text
M(t) ≤ e^{-ρt}M(0) + (ξB/ρ)(1 − e^{-ρt}).
```

QED.

---

## 4. Theorem: Energy Descent for Frozen Memory and Curvature

### Statement

Assume `M` and `κ` are frozen in time, so `r(x)` is fixed. Let

```text
∂Φ/∂t = − δE/δΦ*
```

with

```text
E[Φ] = ∫Ω [ a |∇Φ|²/2 + r(x)|Φ|²/2 + c |Φ|⁴/4 ] dx.
```

Then

```text
dE/dt = −∫Ω |∂Φ/∂t|² dx ≤ 0.
```

### Proof

The variational derivative is

```text
δE/δΦ* = −aΔΦ + r(x)Φ + c|Φ|²Φ.
```

The gradient flow is therefore

```text
∂Φ/∂t = aΔΦ − r(x)Φ − c|Φ|²Φ = −δE/δΦ*.
```

Taking the time derivative of the energy along the flow gives

```text
dE/dt = Re ∫Ω (δE/δΦ*) (∂Φ*/∂t) dx.
```

Since `∂Φ/∂t = −δE/δΦ*`,

```text
dE/dt = −∫Ω |∂Φ/∂t|² dx ≤ 0.
```

QED.

### Interpretation

For fixed memory and curvature, EPM relaxes downhill in adaptive energy. Stable structures are energy minima or metastable local minima.

---

## 5. Theorem: Local Uniform Equilibria

Ignore spatial gradients and take `r` constant. Then EPM reduces to

```text
dΦ/dt = −rΦ − c|Φ|²Φ.
```

Writing `A = |Φ|`,

```text
dA/dt = −rA − cA³.
```

### Equilibria

The equilibria are

```text
A = 0
```

and, if `r < 0`,

```text
A² = −r/c.
```

### Stability

For amplitude squared `X = A²`,

```text
dX/dt = −2rX − 2cX² = 2X(−r − cX).
```

If `r > 0`, then `X=0` is stable.

If `r < 0`, then `X=0` is unstable and

```text
X* = −r/c
```

is stable.

### Interpretation

Where the adaptive potential is positive, the EPM field dies away.

Where memory and curvature make the effective coefficient negative,

```text
r(x) = V0 + uκ − vM < 0,
```

nonzero structure can exist.

This is the first solved EPM emergence condition:

```text
vM > V0 + uκ.
```

---

## 6. Solved 0D Memory-Coupled EPM Model

A more complete zero-dimensional EPM toy model is

```text
dA/dt = (s0 + vM − cA²)A
```

```text
dM/dt = ξA² − ρM
```

where `A ≥ 0` is amplitude and `M ≥ 0` is memory.

Let

```text
X = A².
```

Then

```text
dX/dt = 2(s0 + vM − cX)X
```

```text
dM/dt = ξX − ρM.
```

### Equilibria

There is always the zero equilibrium:

```text
(X,M) = (0,0).
```

A nonzero equilibrium satisfies

```text
M* = ξX*/ρ
```

and

```text
s0 + vM* − cX* = 0.
```

Therefore

```text
X* = s0 / (c − vξ/ρ)
```

```text
M* = (ξ/ρ) X*.
```

### Existence Condition

A positive nonzero equilibrium exists when

```text
X* > 0.
```

The physically stable case is

```text
s0 > 0
```

and

```text
cρ > vξ.
```

Then

```text
X* = s0/(c − vξ/ρ) > 0.
```

### Stability Proof

The Jacobian of the `(X,M)` system is

```text
J = [[ 2(s0 + vM − 2cX), 2vX ],
     [ ξ,                 −ρ  ]].
```

At the nonzero equilibrium, `s0 + vM* − cX* = 0`, so

```text
J* = [[ −2cX*, 2vX* ],
      [ ξ,     −ρ   ]].
```

The trace is

```text
tr(J*) = −2cX* − ρ < 0.
```

The determinant is

```text
det(J*) = 2X*(cρ − vξ).
```

Thus the nonzero equilibrium is linearly stable when

```text
cρ > vξ.
```

QED.

### Interpretation

Stable EPM emergence in this reduced model requires:

1. positive base growth/trapping `s0 > 0`,
2. nonlinear saturation strong enough to dominate runaway memory feedback:

```text
cρ > vξ.
```

This is the second solved EPM condition.

---

## 7. Theorem: Winding Is Topologically Protected

### Statement

Let `Γ` be a closed loop and suppose

```text
Φ(x,t) ≠ 0
```

on `Γ` for all `t` in an interval. Define the phase map

```text
Φ/|Φ| : Γ → S¹.
```

The winding number

```text
W = (1/2π) ∮Γ ∇arg(Φ) · dl
```

is an integer and is constant in time as long as `Φ` never vanishes on `Γ`.

### Proof

Because `Φ ≠ 0` on `Γ`, the normalized field

```text
u = Φ/|Φ|
```

is a continuous map from the loop `Γ ≅ S¹` to the unit circle `S¹`.

Such maps are classified by an integer degree. Continuous deformation of the map cannot change its degree unless continuity fails or the map leaves `S¹`.

The map leaves `S¹` only when `Φ = 0` somewhere on the loop, because then `Φ/|Φ|` is undefined.

Therefore `W` is constant under all continuous nonzero deformations.

QED.

### EPM Meaning

An EPM object can only change its topological identity if:

- the field amplitude collapses to zero somewhere critical,
- the branch/phase structure tears,
- or the loop boundary changes.

This is the core topological persistence result.

---

## 8. Adaptive-π Version of Winding

When using Adaptive-π, define a normalized phase coordinate `ψ` by

```text
ψ = θ_R / πₐ
```

or, more generally, by the local phase-period convention of the model.

The protected winding should be computed from the circle-valued normalized phase, not from a raw unnormalized scalar if the period varies over space.

A safe canonical statement is:

```text
W = degree(exp(iψ)).
```

Then `W` is integer-valued and topologically protected whenever `exp(iψ)` is continuous and nonzero on the loop.

---

## 9. EPM Persistence Score

A simulation diagnostic can be defined as

```text
S_EPM = T_persist · |W| · C_phase / R_eff.
```

Where:

- `T_persist` is lifetime,
- `W` is topological winding,
- `C_phase` is phase coherence,
- `R_eff` is localization radius.

This is not a fundamental constant. It is a ranking/diagnostic metric for simulations.

A structure scores high when it:

1. lives long,
2. has nonzero topology,
3. maintains phase coherence,
4. remains localized.

---

## 10. ACST Accounting for EPM

Define memory charge:

```text
Q_M(t) = ∫Ω M(x,t) dx.
```

Using

```text
∂M/∂t = ξ|Φ|² − ρM,
```

we get

```text
dQ_M/dt = ξ∫Ω |Φ|² dx − ρQ_M.
```

This is an adaptive conservation law of ACST form:

```text
dC_A/dt = input − decay + memory feedback.
```

For EPM, the memory charge is not exactly conserved, but it is exactly accounted for.

---

## 11. What Is Solved So Far

### Proven

- memory positivity,
- memory boundedness under bounded amplitude,
- energy descent for frozen memory/curvature gradient flow,
- local equilibrium condition,
- stable 0D memory-coupled equilibrium condition,
- topological winding protection,
- ACST memory-charge accounting.

### Solved conditions

Nonzero local EPM structure can exist when

```text
vM > V0 + uκ.
```

Stable reduced EPM emergence exists when

```text
s0 > 0
```

and

```text
cρ > vξ.
```

Topology persists when

```text
Φ ≠ 0 on the enclosing loop.
```

Memory remains nonnegative when

```text
M(0) ≥ 0, ξ ≥ 0, ρ > 0.
```

---

## 12. What Is Still Open

The full coupled PDE system

```text
Φ, M, κ, θ_R, G
```

is not completely solved in closed form.

Open questions include:

1. global existence for the full five-field system,
2. stable localized objects in 2D and 3D,
3. bifurcation thresholds for memory-vortex formation,
4. rigorous Adaptive-π winding under variable period fields,
5. numerical stability bounds for explicit solvers,
6. classification of EPM object types.

---

## 13. Next Theorem Targets

1. Prove global boundedness for the coupled `Φ-M` system under `cρ > vξ`.
2. Prove existence of localized minimizers in a bounded trap where `r(x)<0` inside and `r(x)>0` outside.
3. Prove winding conservation on discrete grids using plaquette phase sums.
4. Prove persistence-score monotonicity under restricted classes of perturbation.
5. Couple EPM to PMT and prove phase-memory channels can seed EPM structures.

---

## 14. Summary

The strongest current EPM result is:

```text
EPM structures can be stable when memory/geometry creates a negative effective potential, nonlinear saturation prevents runaway growth, and nonzero winding protects identity.
```

In compact form:

```text
r(x,t) = V0 + uκ − vM
```

```text
r < 0 creates structure
```

```text
cρ > vξ prevents runaway
```

```text
W ≠ 0 protects topology
```

That is the first solved mathematical core of Emergent Phase Matter.
