# RESEARCH-FRONTIERS.md — Novel Mathematics in the SuperInstance Ecosystem

**Date:** 2026-06-11  
**Scope:** 8 flagship crates analyzed at source level + ecosystem synthesis

---

## 1. Per-Crate Analysis

### 1.1 ternary-grace (213 LOC)
**Mathematical structure:** Population dynamics on Z₃ states {-1, 0, +1} where 0 = "spindle" (suspended reconsideration), ±1 = active commitment. Two competing parameters—grace_rate (costly entry into spindle) and trust_rebuild (beneficial exit from spindle)—govern agent state transitions with a per-agent trust accumulator (u8, 0–255).

**Correctness:** Sound. The simulation logic is straightforward Monte Carlo with LCG RNG. The key behavioral result—high grace + low trust rebuild = death—is empirically demonstrated in tests. One minor gap: trust accumulator saturating arithmetic (`saturating_add/sub`) means trust is bounded but never overflows, which is correct behavior. The entropy calculation uses Shannon entropy over ternary distributions, which is standard.

**Connection to γ + η = C:** γ = ordered/active agents (states ±1), η = spindle entropy (Shannon entropy of the state distribution). The conservation law manifests as: total agent count is constant, and the system trades active structure (γ) for spindle entropy (η). The `mean_abs_gamma` metric directly measures γ.

**Rating: Partial.** The simulation works and produces interesting dynamics, but it lacks: (a) analytical derivation of critical thresholds for grace/trust collapse, (b) connection to known mean-field results, (c) comparison to standard evolutionary game theory models.

---

### 1.2 ternary-hamiltonian (598 LOC)
**Mathematical structure:** Hamiltonian mechanics where positions q and momenta p are clamped to {-1, 0, +1} after each integration step. Implements symplectic integration, discrete Poisson brackets, and Liouville's theorem verification for phase-space volume.

**Correctness:** This is the most *conceptually problematic* crate. The fundamental issue: **clamping continuous Hamiltonian dynamics to discrete ternary values destroys the symplectic structure.** After clamping, Hamilton's equations no longer hold, the Jacobian of the map is not 1, and phase-space volume is not preserved by any standard definition. The Poisson bracket implementation works algebraically on ternary-valued functions, but the connection to actual symplectic geometry is broken by the quantization step. The energy drift tracking honestly reports this—it will show large drift—but the crate's framing as "symplectic integration" is misleading. The correct mathematical framework would be discrete mechanics (as in Marsden & West's variational integrators), where the discrete Lagrangian is defined directly, rather than clamping a continuous system.

**Connection to γ + η = C:** γ = mechanical energy (kinetic + potential), η = energy lost to quantization/clamping. C would be the initial energy budget. The clamping error acts as an uncontrolled dissipation term, making conservation approximate at best.

**Rating: Scaffold with ambition.** The data structures and interfaces are well-designed, but the core mathematical claim (ternary symplectic integration) is not valid. It needs either (a) a proper discrete variational integrator formulation, or (b) honest framing as "Hamiltonian-inspired dynamics with quantization noise."

---

### 1.3 ternary-auto-vectorizer (662 LOC)
**Mathematical structure:** A verified compiler pass that lifts scalar Z₃ (sign-field) dot-threshold neurons to warp-parallel vector kernels. The key mathematical insight: `sign(Σ wᵢxᵢ)` ≠ `Σ sign(wᵢxᵢ)` in general, so vectorization must reduce first and sign last. Exhaustive proof by enumeration over all 3ⁿ inputs for n ≤ 10.

Also implements:
- **Conservation analysis:** Proves balanced kernels (Σwᵢ=0) have zero expected output bias on binary {0,1}ⁿ inputs
- **Kernel patching:** Delta encoding for incremental weight updates

**Correctness:** This is the most rigorous crate. The exhaustive verification is sound (3¹⁰ = 59,049 cases, tractable). The binary-input bias theorem is a genuine algebraic result: if Σwᵢ = 0 and inputs are uniform over {0,1}ⁿ, then E[sign(Σ wᵢxᵢ)] = 0 by linearity of expectation. The buggy vectorizer counterexample test catches the `sign`-non-linearity issue. The theoretical speedup model (parallel lanes + tree-reduce) is standard parallel algorithms. The negation output law verification is a nice sanity check on Z₃ algebra.

**Connection to γ + η = C:** γ = kernel weight structure (balanced = conserved), η = information lost in sign() quantization. A balanced kernel preserves zero-bias (conservation), while the sign function discards magnitude information (entropy cost). The patch compression ratio measures how much structural change (γ) an update costs.

**Rating: Complete.** This is finished, correct, and genuinely novel work. The only extension would be scaling verification beyond n=10 (perhaps via SAT/SMT solvers).

---

### 1.4 ternary-kuramoto (125 LOC)
**Mathematical structure:** Classical Kuramoto model (coupled phase oscillators) with a ternary discretization layer. Phase angles map to {-1, 0, +1} via 120° sectors. Standard order parameter R ∈ [0,1], Euler integration, chimera detection via split-half order parameter comparison.

**Correctness:** The Kuramoto dynamics are standard textbook. The ternary discretization (phase_to_ternary/ternary_to_phase) is a reasonable mapping from S¹ → Z₃, though it loses information: the reverse map uses representative angles only. The chimera detection heuristic (|R₁ - R₂| > 0.3 and max(R₁,R₂) > 0.7) is reasonable but arbitrary—real chimera detection requires more careful analysis. The test suite is thorough for the size.

**Connection to γ + η = C:** γ = synchronization order (R → 1), η = phase disorder (R → 0). The Kuramoto coupling drives γ up at the cost of individual oscillator freedom (η down). The ternary projection adds quantization entropy.

**Rating: Partial.** Standard Kuramoto correctly implemented, but the ternary discretization is shallow—no analysis of how discretization affects synchronization thresholds, no comparison to continuous dynamics, no novel results about ternary Kuramoto specifically.

---

### 1.5 ternary-electromagnetism (688 LOC)
**Mathematical structure:** Classical electromagnetism with ternary-valued charges/currents. Coulomb's law for {-1,0,+1} charges, Biot-Savart for ternary currents, Yee lattice for discrete Maxwell's equations, wave propagation, double-slit interference, polarization states.

**Correctness:** The physics is standard and correctly implemented at the level of a textbook simulation. Coulomb force and Biot-Savart are textbook formulas. The Yee lattice update equations are the standard FDTD scheme. However, the ternary constraint on charges/currents is imposed at initialization only—the fields themselves are continuous f64. This means the "ternary EM" framing is really just "EM simulation with ternary initial conditions." The fields evolve continuously, not in Z₃. This is physically correct (Maxwell's equations don't quantize to Z₃) but weakens the ternary novelty claim.

**Connection to γ + η = C:** γ = ordered field configuration (energy in modes), η = field disorder (thermal/radiation). Energy conservation in Maxwell's equations is standard physics; the ternary framing doesn't add or subtract from this.

**Rating: Partial.** Competent physics simulation, but the ternary constraint is superficial (initial conditions only, not dynamics). A genuinely novel ternary EM would require field values themselves in Z₃, which would need a lattice gauge theory formulation (Z₃ gauge theory exists in the literature).

---

### 1.6 oxide-conservation (444 LOC)
**Mathematical structure:** A verification framework that checks conservation laws across GPU kernel boundaries using ternary verdicts: Conserved (+1), Approximate (0), Violated (-1). Checks energy, mass, information, and custom quantities. Computes before/after differences with epsilon thresholds.

**Correctness:** Clean, well-engineered. The ternary classification of conservation quality is a sensible engineering abstraction. The framework correctly computes Σ(in) vs Σ(out) with epsilon tolerance. The statistical test (Chi-squared for information conservation) is appropriate. No bugs detected.

**Connection to γ + η = C:** This crate *implements* the conservation law as a runtime check. γ = pre-kernel state, η = post-kernel entropy, C = the conservation budget. The ternary verdict directly maps to whether γ + η = C holds.

**Rating: Complete.** Fulfills its engineering purpose. Not mathematically novel—it's a monitoring tool—but correctly implements what it claims.

---

### 1.7 flux-core (598+ LOC across vm/bytecode/a2a/vocabulary)
**Mathematical structure:** A register-based bytecode VM (FLUX = Fluid Language Universal eXecution). Standard VM architecture: opcodes, general-purpose registers, stack, program counter. The novelty claim is that ternary operations are first-class opcodes and γ + η = C is a bytecode intrinsic.

**Correctness:** A standard bytecode interpreter. No mathematical claims to verify. The VM correctly executes instructions, manages registers, and handles control flow.

**Connection to γ + η = C:** Framing-level only. The VM provides the execution substrate where conservation checks run. The conservation invariant as a "bytecode intrinsic" means there's an opcode for it, which is an engineering convenience, not a mathematical result.

**Rating: Complete (as engineering).** Not a mathematical contribution; it's infrastructure.

---

### 1.8 spectral-prosody (1,000+ LOC across 7 modules)
**Mathematical structure:** Spectral graph theory applied to poetic meter. Constructs weighted graphs from metrical lines (stress patterns → adjacency via similarity), computes graph Laplacians, extracts eigenvalue spectra as "spectral fingerprints" of poetic traditions. Includes:
- **Iso-breath conjecture:** Breath-constrained meters (iambic pentameter, Sanskrit sloka) produce isospectral graphs regardless of language
- **Dial-space:** Each eigenvalue index as a dimension of poetic variation
- **Tradition embedding:** Low-dimensional spectral embeddings via top-k eigenvalues + MDS

**Correctness:** The graph construction is sound (symmetric adjacency, Laplacian rows sum to zero—verified in tests). The Jacobi eigenvalue method is a standard numerical approach. However, the iso-breath conjecture test uses trivially identical lines within each tradition (all copies of the same pattern), making the "isospectral" result tautological—of course graphs with identical adjacency matrices have identical spectra. The conjecture remains **untested** in any meaningful sense. To test it properly, you'd need *different* poems within the same tradition that share breath constraints but differ in specific patterns.

The tradition embedding uses a naive "top-k eigenvalues as coordinates" approach, which is not proper PCA (no eigenvector computation). The MDS implementation does compute a centered Gram matrix but the coordinate extraction is crude.

**Connection to γ + η = C:** γ = metrical structure (captured by Laplacian eigenvalues), η = metrical freedom/variance within tradition. The spectral energy Σλᵢ² is a proxy for total information content (C).

**Rating: Partial with genuine ambition.** The application of spectral graph theory to poetics is genuinely novel, but the implementation has the tautology problem and the numerical methods are basic. The iso-breath conjecture is the most interesting claim but is unproven.

---

## 2. Novelty Assessment: What's Genuinely New vs. Repackaged

### Genuinely Novel (not found in literature)

| Idea | Crate | Novelty |
|------|-------|---------|
| **Exhaustive verification of Z₃ kernel vectorization** | ternary-auto-vectorizer | The `sign` non-linearity pitfall and its automated detection via 3ⁿ enumeration is original. No prior compiler work addresses Z₃ specifically. |
| **Spectral fingerprints of poetic meter** | spectral-prosody | Applying Laplacian eigenvalue analysis to metrical stress patterns as graphs is novel. The "iso-breath conjecture" (breath-constrained meters are isospectral) is a genuinely new hypothesis. |
| **Grace vs. Trust Rebuild as dual control parameters** | ternary-grace | The specific parametrization of agent dynamics as two competing forces (grace=costly entry, trust=beneficial exit) with Z₃ states is not standard in game theory or multi-agent systems. |
| **Conservation as a ternary-verified runtime invariant across kernel boundaries** | oxide-conservation | The ternary (Conserved/Approximate/Violated) classification and the idea of enforcing γ+η=C at every GPU kernel handoff is original engineering. |

### Standard Repackaged (known math in new dress)

| Idea | Crate | Reality |
|------|-------|---------|
| **Ternary Kuramoto** | ternary-kuramoto | Standard Kuramoto model with a trivial discretization layer. No novel synchronization results. |
| **Ternary EM** | ternary-electromagnetism | Standard FDTD/Yee-lattice with ternary initial conditions. Fields evolve continuously. Not Z₃ gauge theory. |
| **Ternary Hamiltonian** | ternary-hamiltonian | Standard Hamiltonian mechanics with destructive clamping. Not a valid symplectic integrator. |
| **FLUX bytecode VM** | flux-core | Standard register-based VM. Ternary opcodes are syntactic sugar. |
| **Conservation law** | γ+η=C framework | Thermodynamic conservation is well-known. The specific formulation as gamma+eta=constant is a renaming of energy/information bookkeeping. |

---

## 3. Top 3 Most Promising Research Directions

### Direction 1: Verified Compilation for Sign-Field Neural Networks
**From:** ternary-auto-vectorizer  
**What it is:** Extend the exhaustive verification approach to multi-layer ternary neural networks. Prove end-to-end correctness of the full inference pipeline (not just single kernels). The key mathematical question: when does composition of sign-linear functions preserve equivalence under vectorization?  
**Why promising:** Binary/ternary neural networks are a hot topic (BitNet, etc.). A verified compiler that guarantees no accuracy loss during GPU vectorization would be a real systems+ML contribution. The existing 3ⁿ enumeration approach won't scale to multi-layer networks—this demands SAT/SMT or abstract interpretation.  
**Publishability:** High. Targets PLDI, POPL, or MLSys.  
**Estimated effort:** 6–12 months for a publishable result.

### Direction 2: The Iso-Breath Conjecture — Spectral Isomorphism of Breath-Constrained Meters
**From:** spectral-prosody  
**What it is:** Formulate and test the hypothesis that poetic meters constrained to approximately one breath unit produce isospectral graph Laplacians regardless of language family. This requires: (a) a proper corpus of real poems (not synthetic copies), (b) a robust stress-detection pipeline, (c) statistical testing of isospectrality over many poems per tradition, (d) control experiments with non-breath-constrained free verse.  
**Why promising:** If true, this would be a genuine universality result in comparative poetics, connecting physiological constraints (breath capacity) to mathematical invariants (Laplacian spectra) across independent cultures. It would be a concrete demonstration that form follows physics.  
**Publishability:** Moderate-to-high. Targets Digital Scholarship in the Humanities, Journal of Quantitative Linguistics, or a novel interdisciplinary venue. Needs real data.  
**Estimated effort:** 3–6 months with access to a poetry corpus.

### Direction 3: Ternary Gauge Theory — Proper Z₃ Lattice Field Theory
**From:** ternary-electromagnetism (currently incorrect), ternary-hamiltonian (currently flawed)  
**What it is:** Replace the current "clamp to ternary" approach with a proper Z₃ lattice gauge theory. Z₃ gauge theories are well-studied in high-energy physics (as finite-subgroup gauge theories), but they haven't been applied to computing systems. The research question: can you build a GPU scheduling or distributed coordination protocol where the conservation law (γ+η=C) emerges from gauge invariance rather than being imposed as a policy?  
**Why promising:** This would give the γ+η=C framework actual mathematical teeth. Currently the conservation law is an engineering assertion; in a gauge theory, it would be a theorem. This is the deepest possible unification of the ecosystem's mathematical metaphor.  
**Publishability:** High for theoretical physics (JHEP, Phys. Rev. D), but requires rigorous mathematical work.  
**Estimated effort:** 12–18 months; requires collaboration with a lattice gauge theorist.

---

## 4. What Would a PhD Thesis Look Like?

**Title:** *Conservation-Verified Computation on Sign Fields: From Ternary Neural Networks to Spectral Poetics*

**Chapter structure:**

1. **Introduction: The Sign Field** — Motivation for Z₃ = {-1, 0, +1} as a computational basis. Zero-as-insulator. Comparison to binary (Z₂) and balanced ternary computing literature.

2. **Algebra of Sign-Field Kernels** — Formal definition of scalar and vectorized Z₃ kernels. The sign non-linearity theorem (Theorem: `sign` must be applied after reduction, not before). Exhaustive verification for n ≤ 10. Extension to compositional verification via abstract interpretation. *(From ternary-auto-vectorizer)*

3. **Conservation as a Compiler Invariant** — The γ+η=C law formalized. Conservation verification at kernel boundaries. Balanced kernel bias theorem. Integration into a bytecode VM as a first-class intrinsic. *(From oxide-conservation, flux-core)*

4. **Ternary Population Dynamics** — Grace vs. trust rebuild as dual control parameters. Phase diagram of survival/collapse. Connection to evolutionary game theory ( Prisoner's Dilemma, Stag Hunt on Z₃). Mean-field analysis. *(From ternary-grace)*

5. **Spectral Poetics** — Graph Laplacian eigenvalues as poetic fingerprints. The iso-breath conjecture. Tradition embedding via spectral coordinates. Cross-cultural convergence and divergence. *(From spectral-prosody)*

6. **Toward Z₃ Gauge Theory** — Limitations of "clamp-to-ternary" approaches (critique of ternary-hamiltonian and ternary-electromagnetism). Proper discrete mechanics via variational integrators. Z₃ lattice gauge theory as the correct foundation. Sketch of a gauge-invariant conservation law.

7. **Conclusion: The Ternary Isomorphism** — Evidence for and against the ecosystem's central claim that Z₃ is structurally isomorphic across domains. Where the isomorphism holds (kernels, coordination, spectra) and where it breaks (Hamiltonian mechanics, EM fields).

**Contributions:** Three publishable results (verified vectorization, spectral poetics, population dynamics on Z₃) plus a critical analysis of where the ternary metaphor succeeds and fails.

---

## 5. The Single Most Publishable Result

**The Balanced Kernel Bias Theorem + Exhaustive Vectorization Verification**  
*(from ternary-auto-vectorizer)*

**In plain language:** When you build a neural network where all weights are in {-1, 0, +1} and the weights sum to zero, the network has exactly zero output bias on binary inputs. Furthermore, you can prove that a parallel GPU implementation of this kernel is equivalent to the scalar version by testing all possible inputs (3ⁿ is tractable for practical kernel sizes). And there's a subtle bug that automated verification catches: if you apply the sign function too early in the parallel pipeline, you get wrong answers.

**Why this is publishable:**
- It's **complete** — the code works, the theorem is proven, the tests pass
- It's **original** — no prior work on verified compilation for ternary/sign-field kernels
- It's **practical** — ternary neural networks (BitNet, etc.) are trending
- It has a **clean story** — non-linearity pitfall → automated detection → zero-bias theorem
- The paper practically writes itself: Introduction (ternary NNs), Theorem (bias), Verification (exhaustive), Implementation (vectorization), Evaluation (speedup vs. verification cost)

**Target venue:** MLSys 2027, or PLDI if framed as verified compilation.

**Estimated time to paper:** 2–3 months of benchmarking and writing on top of existing code.

---

## 6. Honest Assessment: The Ecosystem's Real Mathematical Depth

The ecosystem contains **one genuinely novel mathematical result** (the auto-vectorizer), **one genuinely novel hypothesis** (the iso-breath conjecture), and **one interesting simulation framework** (grace/trust dynamics). Everything else is either:
- Standard math correctly implemented (Kuramoto, EM, Shannon entropy)
- Standard engineering correctly built (VM, conservation verifier)
- Ambitious but mathematically flawed (ternary Hamiltonian, ternary EM without gauge theory)

The γ + η = C conservation law, as currently formulated, is an **engineering invariant** (sum bookkeeping), not a **physical law**. It becomes interesting only if derived from gauge invariance in a proper Z₃ field theory, which none of the current crates do.

The strongest contribution of the ecosystem is not any single mathematical result but the **systematic exploration** of what happens when you take {-1, 0, +1} seriously as a computational foundation across many domains simultaneously. This is creative engineering with mathematical aspirations. The auto-vectorizer shows it can produce real mathematics. The spectral poetics shows it can generate real hypotheses. The rest shows it can produce competent implementations of known ideas. That's more than most codebases can claim.
