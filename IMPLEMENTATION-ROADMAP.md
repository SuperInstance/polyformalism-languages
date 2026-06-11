# SuperInstance Ecosystem — Implementation Roadmap

**Generated:** 2026-06-11  
**Source:** DEPENDENCY-MAP.md + GRAND-SYNTHESIS.md  
**Scope:** 1,596 repos → phased build order

---

## Guiding Principles

1. **Layer order is sacred.** Layer 0 (math) before Layer 1 (data) before Layer 2 (ML) before Layer 3 (systems) before Layer 4 (apps).
2. **The kernel ships first.** 15 crates everything depends on. No exceptions.
3. **Bridges before destinations.** Cross-domain connectors unlock compounding value.
4. **Scaffolds are not crates.** Template-generated stubs (~700) are inventory, not implementation.

---

## Phase 1: The Kernel (15 crates)

*Must exist first. Everything depends on these. Build in dependency order.*

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 1 | **ternary-core** | Z₃ arithmetic, Trit type, grids — the atom of everything | *nothing* (#![no_std]) | M |
| 2 | **conservation-law** | Defines γ + η = C — the invariant the entire ecosystem verifies | *nothing* | S |
| 3 | **entropy-conservation** | Formalizes dH/dt ≤ 0 — entropy's role in the conservation law | conservation-law | S |
| 4 | **ternary-entropy** | Shannon/KL/MI measures for ternary distributions — quantifies disorder | ternary-core | M |
| 5 | **ternary-coordination** | Z/3Z linear algebra, spectral analysis — the math bridge to fleet | ternary-core | M |
| 6 | **conservation-verify** | Multi-scale runtime verification — proves the law holds in practice | conservation-law, ternary-entropy | M |
| 7 | **ternary-cell** | 3-byte atomic unit (state, dwell, flips) — the data atom | ternary-core | S |
| 8 | **flux-core** | Bytecode VM + A2A protocol — the ecosystem's compilation target (6,767 LOC) | ternary-core | L |
| 9 | **construct-core** | Layered trait system (no_std → alloc → async) — how everything deploys | ternary-core | M |
| 10 | **superinstance-protocol** | Wire format for bottles/vessels — **currently empty, #1 blocker** | ternary-core, conservation-law | L |
| 11 | **oxide-conservation** | GPU kernel-boundary conservation checks — verifies γ+η=C at hardware | conservation-verify, ternary-core | M |
| 12 | **oxide-energy-balance** | Trit sum conservation across GPU ops — energy accounting | oxide-conservation | S |
| 13 | **spectral-fleet** | Fleet topology via Laplacian eigenvalues — X-ray for distributed systems | ternary-coordination, ternary-entropy | M |
| 14 | **fleet-auth** | Shared authentication — security gate for every fleet service | superinstance-protocol | M |
| 15 | **edge-conservation-rs** | no_std verification at CDN edge — proves the law runs anywhere | conservation-verify | S |

**Phase 1 dependency chain:**
```
ternary-core ──────────────────────────────────────────┐
conservation-law ──→ entropy-conservation ──┐           │
        └───→ conservation-verify ──────────┤           │
                └───→ oxide-conservation     │           │
                        └───→ oxide-energy   │           │
ternary-entropy ←── ternary-core             │           │
ternary-coordination ←── ternary-core        │           │
ternary-cell ←── ternary-core                │           │
flux-core ←── ternary-core                   │           │
construct-core ←── ternary-core              │           │
superinstance-protocol ←── ternary-core ←────┘           │
        └───←── conservation-law             │           │
spectral-fleet ←── ternary-coordination ←────┘           │
fleet-auth ←── superinstance-protocol                     │
edge-conservation-rs ←── conservation-verify ←───────────┘
```

**Estimated total effort:** ~10.5 person-weeks (S=2d, M=4d, L=8d)

---

## Phase 2: The Bridges (35 crates)

*Connect the kernel to the domains. Build in dependency order within each bridge cluster.*

### Bridge Cluster A: Conservation Enforcement (7 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 16 | **conservation-lint** | Build-time law enforcement — catches violations before runtime | conservation-law | S |
| 17 | **conservation-compiler** | Compile-time invariant injection — bakes the law into binaries | conservation-law, conservation-verify | M |
| 18 | **conservation-matrix-rs** | Matrix formulation of γ+η=C — computational enforcement | conservation-law, ternary-coordination | M |
| 19 | **conservation-spectral-rs** | Topology conservation via spectral methods | conservation-law, spectral-fleet | M |
| 20 | **edge-conservation-worker** | Cloudflare Worker running verification at CDN edge | edge-conservation-rs | M |
| 21 | **fleet-budget** | γ+η=C enforcement for fleet dispatch budgets | conservation-law, superinstance-protocol | M |
| 22 | **fleet-build** | Build pipeline with conservation linting built in | conservation-lint | S |

### Bridge Cluster B: Flux Compilation Pipeline (6 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 23 | **plato-flux-compiler** | Compiles PLATO rooms to Flux bytecode (verified path dep) | flux-core | L |
| 24 | **oxide-flux-runtime** | Flux→MIR→PTX pipeline — runs Flux on GPU | flux-core, oxide-energy-balance | L |
| 25 | **cuda-oxide** | Flux → MIR → Pliron → NVVM → PTX compiler | flux-core, oxide-flux-runtime | L |
| 26 | **cudaclaw** | Persistent GPU kernels, warp consensus, SmartCRDT | cuda-oxide | L |
| 27 | **pincher** | "Vector DB as runtime, LLM as compiler" — layer 2 of GPU stack | flux-core | L |
| 28 | **open-parallel** | Async runtime (tokio fork) — layer 1 of GPU stack | ternary-core | M |

### Bridge Cluster C: Agent Runtime (10 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 29 | **construct-coordination** | Inter-instance consensus — agents agreeing | construct-core, ternary-coordination | M |
| 30 | **construct-hotswap** | Live capability evolution — agents upgrading without restart | construct-core | M |
| 31 | **construct-provenance** | Lineage tracking for agent decisions | construct-core | S |
| 32 | **agent-template** | Agent instantiation pattern — the cookie cutter | construct-core | S |
| 33 | **agent-memory** | Persistent agent state across sessions | construct-core, ternary-cell | M |
| 34 | **agent-homeostasis** | Agent self-regulation via conservation law | construct-core, conservation-verify | M |
| 35 | **agent-sync** | Inter-agent synchronization — rhythm section | construct-coordination | M |
| 36 | **agent-ensemble** | Multi-agent coordination via counterpoint | agent-sync, ternary-coordination | M |
| 37 | **agent-riff-v4** | Self-generating specs via adversarial improvisation — apex of bootstrap chain | agent-ensemble | M |
| 38 | **agent-semiosis** | Embedding drift — how agent meaning evolves over time | agent-memory | M |

### Bridge Cluster D: Fleet Services (6 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 39 | **fleet-coordinator** | Node self-organization — currently scaffold, critical blocker | superinstance-protocol, fleet-auth | L |
| 40 | **fleet-events-db** | Shared D1 schema — the fleet's memory | superinstance-protocol | M |
| 41 | **fleet-edge-worker** | Edge dispatch with conservation verification | fleet-auth, edge-conservation-worker | L |
| 42 | **fleet-metrics-cron** | Budget tracking — monitors γ+η=C across fleet | fleet-events-db, conservation-law | M |
| 43 | **fleet-event-router** | Routes events from edge to processing — currently scaffold | fleet-events-db | M |
| 44 | **fleet-vector-api** | Semantic search endpoint | fleet-auth | M |

### Bridge Cluster E: CRDT & State Sync (6 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 45 | **oxide-crdt** | CRDT primitives for ternary state — conflict-free sync | ternary-cell, oxide-conservation | M |
| 46 | **oxide-health-monitor** | Health aggregation via CRDTs — fleet-wide health picture | oxide-crdt | M |
| 47 | **oxide-circuit-breaker** | CRDT-synced circuit breaker — prevents cascade failures | oxide-crdt | M |
| 48 | **oxide-federation** | Multi-region fleet coordination | oxide-circuit-breaker, spectral-fleet | L |
| 49 | **oxide-fleet** | Rhythm-based GPU dispatch optimization | oxide-federation, oxide-flux-runtime | L |
| 50 | **superinstance-vectorize** | Embedding pipeline for fleet vector search | fleet-vector-api | M |

**Estimated total effort:** ~28 person-weeks

---

## Phase 3: Applications (100 crates)

*Real functionality built on the kernel and bridges. Grouped by domain.*

### 3A. Ternary Data Structures (15 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 51 | **ternary-btree** | Ternary B-tree — 37% shorter than binary trees | ternary-core, ternary-cell | M |
| 52 | **ternary-heap** | Ternary min-heap (log₃ n) — faster than binary heap | ternary-core | S |
| 53 | **ternary-bloom-filter** | {-1,0,+1} weighted membership — ternary set membership | ternary-core, ternary-hash | S |
| 54 | **ternary-compress** | RLE/sparse/dictionary for trits — ternary compression | ternary-core | M |
| 55 | **ternary-database** | Purpose-built ternary storage engine | ternary-btree, ternary-compress | L |
| 56 | **ternary-hash** | Ternary hashing, MinHash, LSH — similarity at scale | ternary-core | M |
| 57 | **ternary-geometry** | Points, distances, Voronoi in Z³ — spatial ternary math | ternary-core | M |
| 58 | **ternary-field** | Gradient, laplacian, curl on ternary grids — field operations | ternary-core | M |
| 59 | **ternary-fib** | Fibonacci/Tribonacci mod 3 — sequence primitives | ternary-core | S |
| 60 | **ternary-automata** | Ternary cellular automata — zero-as-insulator in action | ternary-core | M |
| 61 | **ternary-graph** | Ternary graph data structures | ternary-core, ternary-cell | M |
| 62 | **ternary-permutation** | Permutations over Z₃ — symmetry operations | ternary-core | S |
| 63 | **ternary-ring** | Ring/field algebraic structures | ternary-core | S |
| 64 | **ternary-matrix** | Matrix operations over GF(3) | ternary-coordination | M |
| 65 | **ternary-sparse** | Sparse ternary representations | ternary-core | M |

### 3B. Ternary ML Pipeline (20 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 66 | **ternary-activation** | Ternary activation functions | ternary-core | S |
| 67 | **ternary-conv** | Ternary convolution layers | ternary-activation, ternary-matrix | M |
| 68 | **ternary-attention** | Ternary attention mechanism | ternary-activation | M |
| 69 | **ternary-grad** | Gradient computation over ternary networks | ternary-activation | M |
| 70 | **ternary-checkpoint** | Model checkpointing for ternary networks | ternary-cell | S |
| 71 | **ternary-accumulator** | Ternary gradient accumulation | ternary-grad | S |
| 72 | **ternary-dropout** | Ternary dropout regularization | ternary-activation | S |
| 73 | **ternary-distill** | Knowledge distillation for ternary models | ternary-grad, ternary-entropy | M |
| 74 | **ternary-bayesian** | Bayesian inference over ternary distributions | ternary-entropy | M |
| 75 | **ternary-belief** | Belief propagation in ternary factor graphs | ternary-bayesian | M |
| 76 | **ternary-classifier** | Ternary classifiers (bullish/neutral/bearish) | ternary-activation | S |
| 77 | **ternary-hmm** | Hidden Markov Models with ternary states | ternary-entropy | M |
| 78 | **ternary-em** | Expectation-maximization for ternary mixtures | ternary-hmm | M |
| 79 | **ternary-ensemble** | Ensemble methods with ternary voting | ternary-classifier | S |
| 80 | **ternary-ga** | Genetic algorithms over Z₃ | ternary-core | M |
| 81 | **ternary-free-energy** | Free energy principle for ternary systems | ternary-entropy, ternary-belief | L |
| 82 | **ternary-active-inference** | Active inference with ternary action spaces | ternary-free-energy | L |
| 83 | **ternary-causality** | Causal inference over ternary variables | ternary-bayesian | M |
| 84 | **ternary-auto-vectorizer** | Automatic vectorization of ternary operations | ternary-matrix, flux-core | L |
| 85 | **ternary-lstm** | Ternary LSTM networks | ternary-activation | M |

### 3C. Oxide GPU Infrastructure (15 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 86 | **oxide-barrier** | GPU synchronization barriers | oxide-energy-balance | S |
| 87 | **oxide-canary** | Canary deployments for GPU kernels | oxide-conservation | S |
| 88 | **oxide-capacity** | Capacity planning for GPU resources | oxide-energy-balance | M |
| 89 | **oxide-checkpoint** | GPU state checkpointing | oxide-energy-balance | M |
| 90 | **oxide-chunk** | Data chunking for GPU transfer | ternary-cell | S |
| 91 | **oxide-compactor** | Memory compaction on GPU | oxide-chunk | M |
| 92 | **oxide-compile-cache** | Compiled kernel cache — avoid recompilation | oxide-flux-runtime | M |
| 93 | **oxide-epoch** | Epoch-based memory management | oxide-conservation | S |
| 94 | **oxide-gradient** | GPU gradient computation | oxide-energy-balance, ternary-grad | M |
| 95 | **oxide-journal** | Write-ahead log for GPU operations | oxide-conservation | M |
| 96 | **oxide-lease-grid** | Distributed lease management | oxide-crdt | M |
| 97 | **oxide-loadshed** | Load shedding with conservation guarantees | oxide-conservation | M |
| 98 | **oxide-partition** | Data partitioning across GPU nodes | oxide-chunk, spectral-fleet | M |
| 99 | **oxide-pipeline** | GPU pipeline orchestration (COMPLETE) | oxide-conservation | S |
| 100 | **oxide-sandbox** | GPU verification laboratory (COMPLETE) | oxide-conservation | S |

### 3D. Agent Musical Intelligence (15 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 101 | **agent-riff** | V1 competitive improvisation — the genesis agent | agent-template | S |
| 102 | **agent-riff-v2** | Cross-session memory accumulation | agent-riff, agent-memory | M |
| 103 | **agent-riff-v3** | Multi-spec quality prediction | agent-riff-v2 | M |
| 104 | **agent-counterpoint** | Distributed coordination via musical counterpoint | agent-ensemble | M |
| 105 | **agent-contrapuntal** | Advanced counterpoint patterns | agent-counterpoint | M |
| 106 | **agent-voice-lead** | Voice leading as task handoff protocol | agent-contrapuntal | M |
| 107 | **agent-groove** | Rhythm-based scheduling optimization | agent-sync | M |
| 108 | **agent-jam** | Multi-agent jam sessions compile to Flux | agent-ensemble, flux-core | L |
| 109 | **agent-cadence** | Task completion as rhythmic pattern | agent-groove | S |
| 110 | **agent-timbre** | Agent identity via timbral fingerprinting | agent-template | S |
| 111 | **agent-dynamics** | Dynamic range as resource allocation | agent-homeostasis | S |
| 112 | **agent-harmony** | Harmonic analysis of agent group behavior | agent-ensemble | M |
| 113 | **agent-melody** | Melodic line as task sequence | agent-cadence | S |
| 114 | **agent-speciation** | Role differentiation — agents becoming specialists | agent-semiosis | M |
| 115 | **agent-self-rivalry** | Phase transitions via self-competition | agent-speciation | M |

### 3E. Domain Applications (15 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 116 | **ternary-econ** | Financial markets (bullish/neutral/bearish) — real trading signals | ternary-classifier, ternary-entropy | M |
| 117 | **ternary-ecology** | Lotka-Volterra in ternary — ecosystem modeling | ternary-field, ternary-ode | M |
| 118 | **ternary-game-theory** | Nash equilibria with third strategy — 3-player games | ternary-coordination | M |
| 119 | **ternary-epidemic** | SIR/SIS models with ternary states — pandemic modeling | ternary-automata, ternary-entropy | M |
| 120 | **ternary-blockchain** | Sponge hash + PoW over Z₃ — ternary consensus | ternary-hash, conservation-law | L |
| 121 | **gpu-ternary-engine** | 561M+ cells/sec ternary simulation — flagship demo | oxide-pipeline, ternary-automata | L |
| 122 | **tensor-midi** | Musical timing via tensor products — bridges agent+ternary+fleet | ternary-matrix, agent-jam | L |
| 123 | **superinstance-spreadsheet** | Evolutionary spreadsheet in browser — user-facing app | superinstance-protocol, fleet-edge-worker | L |
| 124 | **plato-room** | PLATO room runtime — the DDS engine | plato-flux-compiler, construct-core | L |
| 125 | **plato-depth** | RoomDepth engine — recursive room nesting | plato-room | M |
| 126 | **plato-bottle** | Bottle dispatch within PLATO rooms | plato-room, superinstance-protocol | M |
| 127 | **plato-tutor** | TutorLoop — iterative room deepening | plato-depth, agent-template | M |
| 128 | **ternary-ising** | Ising model over Z₃ — phase transition analysis | ternary-field, ternary-entropy | M |
| 129 | **ternary-kuramoto** | Kuramoto synchronization over Z₃ — sync/impossibility proofs | ternary-field | M |
| 130 | **ternary-minority** | Minority game over Z₃ — non-convergence results | ternary-game-theory | M |

### 3F. Remaining Oxide (10 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 131 | **oxide-slotmap** | Slot-based memory mapping | ternary-cell | S |
| 132 | **oxide-tenancy** | Multi-tenant GPU isolation | oxide-capacity | M |
| 133 | **oxide-tombstone** | Deletion markers for CRDT tombstones | oxide-crdt | S |
| 134 | **oxide-workflow** | DAG orchestration for GPU pipelines | oxide-pipeline | M |
| 135 | **oxide-raft-log** | Raft-based replicated log | oxide-journal | M |
| 136 | **oxide-ring** | Hash ring for distributed GPU allocation | spectral-fleet | S |
| 137 | **oxide-dispatch** | Kernel dispatch scheduler | oxide-pipeline, oxide-ring | M |
| 138 | **oxide-fuse** | Operation fusion for GPU efficiency | oxide-dispatch | M |
| 139 | **oxide-gradient-descent** | GPU-accelerated ternary gradient descent | oxide-gradient, ternary-grad | M |
| 140 | **oxide-smart-crdt** | Adaptive CRDT with conservation awareness | oxide-crdt, conservation-verify | M |

### 3G. Spectral & Raft (10 crates)

| # | Crate | Why It Matters | Depends On | Effort |
|---|-------|---------------|------------|--------|
| 141 | **spectral-graph** | Core spectral graph theory library | ternary-coordination | M |
| 142 | **spectral-clustering** | Graph clustering via spectral methods | spectral-graph | M |
| 143 | **spectral-laplacian** | Laplacian eigenvalue computation | spectral-graph | M |
| 144 | **spectral-pagerank** | Ternary PageRank variant | spectral-graph | S |
| 145 | **raft-core** | Core Raft consensus — leader election, log replication | ternary-core | L |
| 146 | **raft-log** | Raft log storage | raft-core | M |
| 147 | **raft-rpc** | Raft RPC transport | raft-core | M |
| 148 | **raft-config** | Raft configuration management | raft-core | S |
| 149 | **raft-membership** | Dynamic membership changes | raft-core, raft-log | M |
| 150 | **raft-snapshot** | Raft snapshot/compaction | raft-log | M |

**Estimated total effort:** ~95 person-weeks

---

## Phase 4: Extensions, Scaffolds & Dead Weight (1,446 repos)

### 4A. Priority Extensions (build when needed)

These have clear purpose and should be implemented when their domain becomes active:

| Category | Crates | Status | Priority |
|----------|--------|--------|----------|
| **Agent bootstraps** | agent-anacrusis, agent-fermata, agent-rubato, agent-staccato-legato, agent-swing, agent-knowledge, agent-microtone | Self-contained, no deps | Low — nice-to-have metaphors |
| **Pure math orphans** | ternary-collatz, ternary-color, ternary-dice, ternary-bite, ternary-chemistry, ternary-constraint, ternary-epoch, ternary-counterpoint, ternary-crossfader | Zero deps, standalone publishable | Medium — publish as-is |
| **Audio DSP** | ternary-echo, ternary-envelope, ternary-gate, ternary-grain, ternary-harmonic, ternary-haar, ternary-dynamics | Zero deps, signal processing | Medium — useful but disconnected |
| **Remaining ternary** | ~200+ ternary-* crates across ML, physics, optimization | Varying substance | Low — fill in as needed |

### 4B. Scaffold Prioritization

**Scaffolds to implement FIRST (high value, frequently referenced):**

| Scaffold | Why It's Referenced | Recommended Action |
|----------|-------------------|--------------------|
| **fleet-coordinator** | Blocks fleet deployment, referenced by 6+ crates | → Already in Phase 2 |
| **fleet-event-router** | Events go to D1 but never trigger | → Already in Phase 2 |
| **fleet-health** | Fleet-wide health monitoring | Implement after fleet-coordinator |
| **fleet-config** | Every fleet service needs config | Implement alongside fleet-auth |
| **fleet-bridge** | Inter-service bridge pattern | Implement with fleet-coordinator |
| **superinstance-protocol** | **The #1 blocker** — empty, everything references it | → Already in Phase 1 |

**Scaffolds to implement EVENTUALLY (useful building blocks):**

| Category | Crates | Value |
|----------|--------|-------|
| **scheduler-\*** | cfs, cron, edf, lottery, mlfq, round | General-purpose scheduling algorithms |
| **cache-\*** | adaptive, hierarchy, lru, moka, ttl | Caching primitives |
| **sort-\*** | heap, merge, quick, radix, tim | Sort algorithms |
| **expr-\*** | bytecode, eval, optimizer, parser, typecheck | Expression language |

**Scaffolds that are DEAD WEIGHT (template noise, no ecosystem connection):**

| Category | Crates | Verdict |
|----------|--------|---------|
| **noise-\*** | channel, fbm, perlin, simplex, voronoi, worley | Dead — only `noise-fbm` has a real path dep; the rest are noise (literally) |
| **gossip-\*** | member, ping, protocol, seed, suspicion | Dead — all stubs, zero deps, no references from kernel |
| **lattice-\*** | basis, cipher, reduction, signal | Dead — post-quantum aspirational, no connection to current architecture |
| **time-\*** | chrono, format, ntp, parser, series-db, tz | Dead — no ecosystem integration, stdlib alternatives exist |
| **regex-\*** | bytecode, dfa, engine, nfa, optimizer, unicode | Dead — only `regex-optimizer→regex-bytecode` is real; rest compete with `regex` crate |
| **ecs-\*** | component, query, resource, system, world | Dead — entity component system with no ternary/fleet connection |
| **doc-\*** | generator, indexer, parser, renderer, search | Dead — documentation tooling unrelated to ecosystem |
| **pixel-\*** | canvas, composite, raster, transform, vector | Dead — graphics primitives with no ecosystem connection |
| **plugin-\*** | host, loader, native, registry, wasm | Dead — plugin system with no consumers |
| **udf-\*** | loader, registry, runner, sandbox, validator | Dead — user-defined function framework with no users |

### 4C. Missing Repos (named but don't exist)

These 7 agent repos are referenced in synthesis docs but have no repositories:

| Repo | Purpose | Priority |
|------|---------|----------|
| **fleet-midi** | Musical timing for fleet dispatch | Medium — extends agent→fleet bridge |
| **ghost-track** | Phantom agent trail tracking | Low — agent debugging |
| **persona-engine** | Agent persona management | Medium — agent identity |
| **fleet-conductor** | Orchestration of fleet agents | High — fleet+agent integration |
| **forgemaster** | Fleet resource forging/allocation | High — fleet resource management |
| **oracle2** | Prediction oracle service | Medium — forecasting |
| **construct** | The base construct implementation | High — needed by construct-core |

---

## Summary Statistics

| Phase | Crates | Effort | Unlocks |
|-------|--------|--------|---------|
| **1: Kernel** | 15 | ~10.5 weeks | Everything — the mathematical and protocol foundation |
| **2: Bridges** | 35 | ~28 weeks | Cross-domain communication, GPU execution, agent lifecycle, fleet deployment |
| **3: Applications** | 100 | ~95 weeks | Real functionality — ML, trading, ecology, games, GPU computing |
| **4: Extensions** | ~1,446 | Variable | Long-tail features, dead weight to cull |

**Critical path to first deployment:**
```
Phase 1 (kernel, 10.5 weeks)
  → superinstance-protocol (within Phase 1)
    → fleet-auth (within Phase 1)
      → fleet-coordinator (Phase 2)
        → fleet-edge-worker + fleet-events-db (Phase 2)
          → First end-to-end bottle dispatch 🎉
```

**Fastest path to something running:** 14 weeks (kernel + fleet services bridge cluster)

---

## Scaffold Triage Summary

### Build First (ecosystem-critical, actively referenced)
1. superinstance-protocol → fleet-coordinator → fleet-event-router → fleet-health → fleet-config → fleet-bridge

### Build When Needed (useful primitives)
2. scheduler-\*, cache-\*, sort-\*, expr-\*

### Dead Weight — Cull or Ignore
3. noise-\*, gossip-\*, lattice-\*, time-\*, regex-\*, ecs-\*, doc-\*, pixel-\*, plugin-\*, udf-\*

~75 scaffold-ocean crates are template noise. They cost token burn on every analysis and provide zero value. Recommend archiving to a separate org or adding a `scaffold:` prefix to exclude from builds.

---

*End of IMPLEMENTATION-ROADMAP.md*
