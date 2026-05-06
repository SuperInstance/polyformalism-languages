# Falsification & Verification Experiment Plan

**Goal:** Subject every claim from the polyformalism research to rigorous falsification.
**Principle:** A single clean disproof outweighs a thousand confirmations.

---

## Testable Claims Inventory

### CLAIM 1: Different languages produce genuinely different insights
**Prediction:** O(L₁, L₂) > 0.4 for maximally divergent pairs (Greek↔Navajo, Chinese↔Finnish)
**Null hypothesis:** All linguistic modes produce equivalent insights (O > 0.4 is random noise)
**Falsification:** If O(Greek, Navajo) < 0.3 across 5+ problems, linguistic mode doesn't matter

### CLAIM 2: 4 universal concepts are truly universal
**Prediction:** Process>nouns, future=present, midwife posture, conflict=misperception appear in ≥80% of languages for ≥80% of problems
**Null:** These 4 appeared in Greek/Chinese/Navajo by coincidence
**Falsification:** If they fail to appear in Arabic, Finnish, Quechua, or Korean at ≥60% rate

### CLAIM 3: "Language IS the constraint system" (intersection insight)
**Prediction:** The problem changes shape depending on linguistic mode, not just the answer
**Null:** Same problem is being solved, just with different vocabulary
**Falsification:** If blinded judges can predict the linguistic mode from the ANSWER but not the PROBLEM REFORMULATION

### CLAIM 4: Complete cognitive set (Greek + Chinese + Navajo + Arabic + Finnish) is necessary
**Prediction:** Removing any one language loses a unique cognitive dimension
**Null:** 3-4 languages are sufficient; the "complete" set adds nothing
**Falsification:** If adding a 6th language or removing the "weakest" produces no measurable change in insight coverage

### CLAIM 5: Inverted-U for debate rounds (3-5 optimal)
**Prediction:** Insight quality peaks at rounds 3-5 and declines after
**Null:** More rounds = better (monotonically increasing)
**Falsification:** If insight scores at round 7+ are higher than round 3-5

### CLAIM 6: The 7-type constraint taxonomy is exhaustive
**Prediction:** No language produces an 8th constraint type outside the taxonomy
**Null:** The 7 types are an artifact of the languages we studied
**Falsification:** If a new language produces constraint concepts that don't fit any of the 7 types

### CLAIM 7: Greek produces most adequate insights, Navajo most novel
**Prediction:** Greek consistently scores adequacy > 4.0, Navajo consistently scores novelty > 4.5
**Null:** Scoring is subjective noise
**Falsification:** If scoring by independent blinded judges shows no consistent pattern

### CLAIM 8: The 3-rewrite rule minimum is necessary
**Prediction:** 3 rewrites through orthogonal formalisms produces insights invisible to single-formalism thinking
**Null:** 1 rewrite (translation only) produces the same quality insights
**Falsification:** If single-formalism solutions score as high as 3-formalism solutions

---

## EXPERIMENT BATCH A: Expand Language Coverage (Falsifies Claims 2, 6)

### A1: Four New Languages × Three Problems
Run the same 3 problems (violation detection, conflict resolution, creative constraint) through:
- **Arabic** (root-and-pattern, deep structure)
- **Finnish** (15 cases, abessive/instrumental)
- **Quechua** (evidentiality, epistemic grammar)
- **Korean** (7 honorific levels, social grammar)

That's 12 new experiments. For each:
1. Check if 4 universal concepts appear
2. Classify constraint types using 7-type taxonomy
3. Score novelty/adequacy against existing results
4. Compute O(L_new, L_existing) for each existing language

**Success criteria:**
- ≥3 of 4 universal concepts appear in ≥3 of 4 new languages
- All constraint types fit existing taxonomy (or we discover type 8)
- O(Arabic, Greek) < O(Arabic, Navajo) (predictable from family distance)

### A2: English Control Baseline
Run all 3 problems through standard English thinking as explicit control.
Score against the same rubric. This should score ~1.5-2.0 combined.
If English scores > 3.0, our scoring is miscalibrated.

### A3: Random Language Pairing
Take 3 problems and solve them in "Random Mode" — randomly mixing grammar features
from different languages. If this produces equivalent insights to coherent linguistic modes,
then the GRAMMAR doesn't matter, only the features. If it produces worse insights,
the coherence of a real language matters.

---

## EXPERIMENT BATCH B: Problem Coverage (Falsifies Claims 1, 4)

### B1: 5 New Problems × 5 Languages
Select 5 problems from PROBLEM-LIBRARY.md that maximize diversity:
- **S3: Fault Tolerance** (systems, survival-focused)
- **C3: Create a Ritual** (creative, social)
- **P4: What Is Time?** (philosophical, fundamental)
- **A3: Optimization** (algorithmic, measurable)
- **S5: Scaling** (systems, growth-focused)

Run through complete cognitive set: Greek, Chinese, Navajo, Arabic, Finnish.
That's 25 experiments.

**Metrics per problem:**
- Insight count per language
- Unique insights (appearing in only 1 language)
- Orthogonality O(L_i, L_j) for all pairs
- Completeness score: what fraction of the 8 insight dimensions are covered

### B2: Drop-One Test
For each of the 5 problems, systematically drop one language from the cognitive set
and measure how much insight coverage is lost.

If dropping Finnish (instrumental thinking) loses < 5% coverage → Finnish isn't necessary.
If dropping Navajo (process thinking) loses > 15% → Navajo is essential.

This directly tests Claim 4 (complete cognitive set necessity).

---

## EXPERIMENT BATCH C: Blinded Verification (Falsifies Claims 3, 7)

### C1: Blinded Judge Experiment
Take outputs from all experiments (A1 + B1). Strip all language identifiers.
Have independent models (DeepSeek-v4-pro, Qwen3-397B) score them on:
1. Novelty (0-5)
2. Adequacy (0-5)
3. Guess which linguistic mode produced this output

**If judges can't guess the mode:** The thinking IS genuinely different (supports Claim 3)
**If judges CAN guess the mode reliably (>70%):** The differences are surface-level

**If blind scores correlate >0.8 with our scores:** Our scoring is reliable
**If blind scores don't correlate:** Our scoring is biased

### C2: Paraphrase Detection
For each experiment pair (e.g., Greek conflict + Navajo conflict), test:
Are these saying the same thing in different words, or genuinely different?

Method: Use a model to rewrite each output in neutral English.
If the neutral-English versions are semantically equivalent → paraphrase, not insight.
If they remain different → genuine linguistic divergence.

---

## EXPERIMENT BATCH D: Mechanism Tests (Falsifies Claims 5, 8)

### D1: Debate Round Scaling
Take one problem. Run the polyformalism debate protocol for rounds 1 through 8.
Score insight quality at each round.

**Expected:** Inverted-U peak at rounds 3-5
**Falsification:** Monotonic increase or peak at round 1

### D2: Rewrite Depth Scaling
Take one problem. Solve in 1 formalism, 2 formalisms, 3, 4, 5, 6, 7.
Score insight quality at each depth.

**Expected:** Diminishing returns after 3, near-zero after 5
**Falsification:** Linear increase (no diminishing returns)

### D3: Translation vs Thinking Control
For 3 problems, compare:
- Group A: "Translate this solution into [language] style"
- Group B: "Think in [language] mode from scratch"

If Group A produces equivalent insights → it's just stylistic rewording
If Group B produces significantly better insights → the THINKING actually differs

---

## EXPERIMENT BATCH E: Robustness & Edge Cases

### E1: Temperature Sensitivity
Run same problem × same language at temperatures 0.2, 0.5, 0.8, 1.0.
If insights are highly temperature-dependent, the "linguistic mode" effect might
just be temperature-driven randomness.

### E2: Model Independence
Run same 3 problems × 3 languages using 3 different models:
- Seed-2.0-pro
- DeepSeek-v4-flash
- Qwen3-235B (or Hermes-405B)

If results are model-independent → linguistic effect is real
If results vary wildly by model → it's a model artifact

### E3: Problem Order Effects
Run the same 5 problems in different orders for the same language.
If order changes results significantly → priming effects, not linguistic effects

---

## Execution Plan

### Phase 1: Batch A (Language Expansion) — 17 experiments
- A1: 4 languages × 3 problems = 12 calls
- A2: 1 English control × 3 problems = 3 calls
- A3: 2 random mixes × 3 problems = 6 calls
- **Total: 21 calls**

### Phase 2: Batch B (Problem Coverage) — 25 + 25 experiments
- B1: 5 problems × 5 languages = 25 calls
- B2: 5 problems × 5 drop-one = 25 calls (recompute from B1 data)
- **Total: 25 calls (B2 is computation, not new calls)**

### Phase 3: Batch C (Blinded Verification) — scoring only
- C1: Blinded scoring of all ~50 existing results = ~50 scoring calls
- C2: Paraphrase detection on 15 pairs = 30 calls
- **Total: ~80 calls (fast scoring)**

### Phase 4: Batch D (Mechanism Tests) — ~30 experiments
- D1: 1 problem × 8 rounds = 8 calls
- D2: 1 problem × 7 depths = 7 calls
- D3: 3 problems × 2 groups = 6 calls + 9 control calls
- **Total: ~30 calls**

### Phase 5: Batch E (Robustness) — ~30 experiments
- E1: 1 problem × 1 language × 4 temps = 4 calls
- E2: 3 problems × 3 languages × 3 models = 27 calls
- E3: 5 problems × 2 orders = 10 calls
- **Total: ~41 calls**

**GRAND TOTAL: ~197 calls across 5 phases**

---

## Falsification Criteria Summary

| Claim | Experiment | Falsified If |
|-------|-----------|-------------|
| 1: Different languages → different insights | B1, E2 | O(L₁,L₂) < 0.3 for divergent pairs, OR model-dependent results |
| 2: 4 universals | A1 | Universals appear in <60% of new languages |
| 3: Language constrains problem shape | C1, C2 | Blinded judges can't tell modes apart, OR paraphrase equivalence |
| 4: Complete set necessary | B2 | Drop-one loses <5% for any member |
| 5: Inverted-U rounds | D1 | Monotonic increase or single-round peak |
| 6: 7-type taxonomy exhaustive | A1 | 8th type discovered that doesn't fit |
| 7: Greek=adequate, Navajo=novel | C1 | Blinded scores show no pattern |
| 8: 3-rewrite minimum | D2, D3 | Linear returns OR translation=thinking |

**If ≥3 claims are falsified:** The framework needs fundamental revision.
**If ≤1 claim is falsified:** Framework is robust, proceed to publication.
**If 0 claims falsified:** Suspicious — our experiments may not be stringent enough.
