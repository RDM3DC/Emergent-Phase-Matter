# EPM Notation

Canonical notation for Emergent Phase Matter.

---

## Core Variables

| Symbol | Meaning |
|---|---|
| `Φ` | emergent phase-memory structure field |
| `A` | amplitude / density field |
| `θ_R` | resolved phase |
| `θ` | phase field |
| `M` | memory density |
| `κ` | curvature field |
| `W` | winding / topological marker |
| `πₐ` | adaptive phase-period field |

---

## Stability Conditions

```text
δE_adaptive / δΦ = 0
```

```text
W ≠ 0
```

---

## Effective Field Form

```text
Φ(x,t) = A(x,t) exp(iθ_R(x,t))
```

---

## Energy Functional Prototype

```text
E = ∫ [a|∇Φ|² + bV(κ,M)|Φ|² + c|Φ|⁴ + d|∇θ|²] dx
```

```text
V(κ,M) = V₀ + uκ − vM
```

---

## Topological Closure

```text
∮ ∇θ_R · dl = 2πₐ W
```

---

## Persistence Score

```text
S_EPM = T_persist · |W| · C_phase / R_eff
```

This is a heuristic simulation metric, not a fundamental constant.
