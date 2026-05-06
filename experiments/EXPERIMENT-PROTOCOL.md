# Experiment Protocol: Linguistic Polyformalism

## 1. Prompt Construction: Forcing Linguistic Mode

A proper polyformalism prompt does **not** ask the model to translate. It asks the model to *think* in the grammatical and cognitive framework of a target language.

### 1.1 The Linguistic Mode Prompt Template

```
You are thinking in [LANGUAGE]. Not translating into [LANGUAGE] — 
thinking IN it. Your cognitive tools are the grammatical structures 
of [LANGUAGE]:

[LIST 3-5 KEY GRAMMATICAL FEATURES]

These structures shape what you CAN think and how you MUST organize 
thought. You cannot use concepts that require grammatical tools 
[LANGUAGE] lacks.

Problem: [PROBLEM STATEMENT]

Solve this problem using ONLY the cognitive tools available to a 
[LANGUAGE] thinker. Do not translate an English solution. Start 
from the grammar and reason forward.

After your solution, list:
1. Which grammatical features of [LANGUAGE] shaped your approach
2. What aspects of the problem your language makes VISIBLE
3. What aspects your language makes INVISIBLE or hard to express
```

### 1.2 Grammatical Feature Lists (Quick Reference)

| Language | Key Grammatical Features to Specify |
|----------|-------------------------------------|
| Navajo | Verb-centric; shape/classificatory verbs; no "to be"; animacy hierarchy; polysynthetic incorporation |
| Ancient Greek | Inflectional case (5 cases); aspect (not tense)-dominant; middle voice; participles as noun-verbs; definite article with abstract nouns |
| Classical Chinese | Topic-prominent; no inflection; classifier system; counterfactuals via context; serial verb constructions; no subject requirement |
| Russian | Perfective/imperfective aspect pairs; 6 cases; verbal prefix derivation; impersonal constructions; zero copula in present |
| Quechua | Evidential suffixes (-mi direct, -si hearsay, -chá conjecture); SOV order; object incorporation; inclusive/exclusive "we" |
| Finnish | 15 cases; no grammatical gender; agglutinative; partitive case for partiality; possessive suffixes; no future tense |
| Arabic (MSA) | Root-and-pattern morphology; dual number; definite/indefinite via prefix; broken plurals; verb-subject-object flexibility |
| Japanese | Honorific levels; topic marker は; subject omission; agglutinative; evidential sentence-final particles; no grammatical gender |
| Yoruba | Tonal (3 tones); isolating; serial verb constructions; no inflection; noun classification; question words in-situ |
| Korean | Honorific system; agglutinative; topic-prominent; evidential markers; different counting systems; subject-object symmetry |

### 1.3 Anti-Translation Checks

Before accepting a response as "genuinely thinking in [LANGUAGE]," verify:

1. **No calques** — The solution doesn't mirror English sentence structure with foreign words
2. **Grammar-driven** — The solution's *structure* follows from the language's grammar, not just its vocabulary
3. **Feature exploitation** — The solution actively uses distinctive grammatical features (evidentials, cases, classifiers, etc.)
4. **Feature respect** — The solution doesn't use concepts that require grammar the language lacks
5. **Organic reasoning** — The chain of reasoning follows a path natural to the language, not an English thought-translated

---

## 2. The 5-Step Evaluation Process

### Step 1: Grammar Fidelity Check
- Did the response genuinely use the language's grammatical tools?
- Score: 0 (pure translation) to 5 (deep grammatical engagement)
- **Gate**: Scores below 3 are rejected — they're English thinking with foreign vocabulary

### Step 2: Insight Extraction
- List every distinct insight, observation, or solution element in the response
- For each insight, tag which grammatical feature enabled or shaped it
- Record insights in standardized form: `INSIGHT_LANG_ID: description [grammatical_feature]`

### Step 3: Novelty Assessment
- Compare each insight against:
  - The English-language control solution
  - All other language solutions for this problem
  - Known solutions in the literature
- Score novelty: 0 (identical to English) to 5 (completely novel, unavailable in English)

### Step 4: Adequacy Assessment
- Is the insight correct/useful/relevant to the problem?
- Score adequacy: 0 (irrelevant) to 5 (directly solves or illuminates the problem)
- Apply neuroscience valuation: **V = novelty × adequacy** (mirrors DMN generative × ECN evaluative)

### Step 5: Cross-Reference Integration
- Place insights on the Insight Detection Matrix (see EVALUATION-FRAMEWORK.md)
- Calculate orthogonality with other languages
- Flag insights that appear in multiple languages (possible universal) vs. single language (possible linguistic novelty)

---

## 3. Scoring Genuine Novelty vs. Translation Artifact

### 3.1 The Translation Artifact Test

A translation artifact is an insight that:
- Can be expressed equally well in English without losing content
- Follows English logical structure with different vocabulary
- Doesn't depend on any grammatical feature of the target language
- Would be produced by a competent English thinker given enough time

### 3.2 The Genuine Novelty Test

A genuinely novel insight:
- **Requires** a specific grammatical feature to discover (not just express)
- Follows a reasoning path that English grammar makes unnatural or invisible
- Reveals aspects of the problem that English's cognitive bias obscures
- Cannot be "reverse-engineered" by simply thinking harder in English

### 3.3 Scoring Rubric

| Score | Label | Description |
|-------|-------|-------------|
| 0 | **Translation** | Identical to what English thinking produces, just in different words |
| 1 | **Paraphrase** | Minor rewording of English insight; no structural difference |
| 2 | **Reframing** | Same insight seen from a different angle, but reachable from English |
| 3 | **Extension** | Goes beyond English insights, but the path is traceable from English |
| 4 | **Qualitative shift** | A genuinely different insight that depends on grammatical tools English lacks |
| 5 | **Paradigm shift** | An insight that is *impossible* to reach through English cognitive tools alone |

### 3.4 Red Flags for Translation Artifacts

- Solution structure mirrors English (problem → analysis → solution)
- Uses English logical connectives directly (if/then, because, therefore)
- Insight can be stated in English with no information loss
- No grammatical feature of the target language is *necessary* for the insight
- The "different" perspective is just a metaphor swap (e.g., "journey" vs. "destination")

---

## 4. Insight Detection Rubric (0–5 Scale)

### Dimension 1: Grammatical Depth (GD)
How deeply does the insight engage with the language's distinctive grammar?

| Score | Meaning |
|-------|---------|
| 0 | No grammatical engagement — pure vocabulary substitution |
| 1 | Surface grammar (word order, basic morphology) |
| 2 | Feature awareness (uses cases, aspects, or classifiers) |
| 3 | Feature exploitation (leverages grammar for reasoning advantage) |
| 4 | Grammar-shapes-thought (reasoning path follows grammatical structure) |
| 5 | Grammar-enables-discovery (insight is *impossible without* the grammatical feature) |

### Dimension 2: Problem Illumination (PI)
How much does the insight illuminate the problem itself?

| Score | Meaning |
|-------|---------|
| 0 | No relevant insight about the problem |
| 1 | Trivial or obvious observation |
| 2 | Minor clarification of a known aspect |
| 3 | Useful new perspective on the problem |
| 4 | Significant reframing that changes how the problem is understood |
| 5 | Paradigm-shifting insight that redefines the problem space |

### Dimension 3: Cross-Linguistic Divergence (CLD)
How different is this insight from what other languages produce?

| Score | Meaning |
|-------|---------|
| 0 | Identical to all other languages |
| 1 | Minor wording differences only |
| 2 | Same insight, different emphasis |
| 3 | Partially novel — some new elements |
| 4 | Mostly novel — fundamentally different approach |
| 5 | Completely novel — no overlap with any other language |

### Composite Score
**Insight Score = GD × PI × CLD / 25** (normalized to 0–5 scale)

An insight scoring 4+ on all three dimensions is a **landmark insight** — evidence that the language genuinely produces different cognition.

---

## 5. Cross-Reference Protocol

### 5.1 Pairwise Comparison

For every pair of languages (L₁, L₂) solving the same problem:

1. Extract insight sets: I(L₁) and I(L₂)
2. Identify overlaps: insights that are semantically equivalent
3. Identify unique insights: I(L₁) \ I(L₂) and I(L₂) \ I(L₁)
4. Calculate Divergence: D(L₁, L₂) = 1 - |overlap(I(L₁), I(L₂))| / |union(I(L₁), I(L₂))|
5. Record the *type* of divergence (structural, categorical, process, relational, or epistemic)

### 5.2 Divergence Types

| Type | Description | Example |
|------|-------------|---------|
| **Structural** | Different decomposition of the problem | Navajo decomposes "scheduling" into motion events; English into resource allocation |
| **Categorical** | Different categories applied | Yoruba's noun classification groups concepts English keeps separate |
| **Process** | Different temporal/causal framing | Russian's aspectual pairs treat process and result as fundamentally different |
| **Relational** | Different connections identified | Classical Chinese's topic-prominence reveals hidden relationships |
| **Epistemic** | Different knowledge-source tracking | Quechua's evidentiality forces explicit sourcing of every claim |

### 5.3 Cluster Analysis

After running all language pairs for a problem:
1. Build a divergence matrix D[i][j] for all language pairs
2. Cluster languages by divergence (low divergence = similar cognitive output)
3. Identify "lonely" languages — those with high divergence from all others (highest potential for novel insights)
4. Identify "bridge" languages — those with moderate divergence to many others (good for integration)

---

## 6. Minimum Experiment Set

### 6.1 Language Selection (minimum 3)

Choose languages that maximize **linguistic distance** (gradient amplitude):

- **Tier 1 (required):** English (control)
- **Tier 2 (pick 2+):** One language from a maximally distant family
  - **Process-oriented:** Navajo, Nahuatl
  - **Relationship-oriented:** Classical Chinese, Japanese
  - **Epistemic-oriented:** Quechua, Turkish
  - **Case-rich/means-oriented:** Finnish, Russian
  - **Pattern-oriented:** Arabic (MSA)

Recommended minimum set: **English + Navajo + Classical Chinese**
- Navajo = verb-centric, process/shape-oriented, polysynthetic
- Classical Chinese = topic-prominent, isolating, relationship-oriented
- Maximum structural distance from each other AND from English

### 6.2 Problem Selection (minimum 3)

Pick problems from different domains (see PROBLEM-LIBRARY.md):
- 1 algorithmic (concrete, verifiable)
- 1 systems (structural, design-oriented)
- 1 creative/philosophical (open-ended, maximum cognitive diversity)

### 6.3 Experiment Matrix

**Minimum: 3 languages × 3 problems = 9 experiments**

|  | Algorithmic | Systems | Creative |
|--|------------|---------|----------|
| English | Exp 1 | Exp 2 | Exp 3 |
| Language B | Exp 4 | Exp 5 | Exp 6 |
| Language C | Exp 7 | Exp 8 | Exp 9 |

**Recommended: 5 languages × 5 problems = 25 experiments** for statistical power.

### 6.4 Controls

Every experiment set must include:
1. **English control** — Same problem solved in English, same prompt structure
2. **Translation control** — Solve in English, then translate to target language (detects translation artifacts)
3. **Random control** — Solve in English with random vocabulary substitution (establishes baseline for "different words, same thinking")

---

## 7. Detecting Paraphrase vs. Genuine Thinking

### 7.1 The Paraphrase Detection Protocol

For each response, apply these tests in order:

**Test 1: Structural Isomorphism**
- Map the logical structure of the response as a dependency tree
- Compare with the English control's dependency tree
- If the trees are isomorphic (same structure, different labels), it's likely paraphrase
- Pass threshold: structural overlap < 60%

**Test 2: Information Content**
- List every factual claim or insight in both responses
- Calculate Jaccard similarity of claim sets
- If similarity > 70%, the "different language" response is just paraphrasing English
- Pass threshold: Jaccard similarity < 50%

**Test 3: Grammatical Necessity**
- Remove all target-language-specific grammatical features from the response
- Does the solution still hold? If yes, the grammar wasn't doing cognitive work
- Pass threshold: removing grammatical features degrades ≥ 30% of insights

**Test 4: Category Boundary Test**
- Does the response draw category boundaries differently than English?
- English: "scheduling = resource allocation over time"
- Navajo: "scheduling = event-shapes in motion"
- If all categories map 1:1 to English categories, it's paraphrase
- Pass threshold: ≥ 1 category boundary that doesn't map to English

**Test 5: Impossible Thought Test**
- Does the response contain an insight that would be *awkward, impossible, or very unlikely* in English?
- Not just "hard to express" but genuinely following a different reasoning path
- Pass threshold: ≥ 1 insight that a panel of English thinkers wouldn't produce

### 7.2 Verdict

| Tests Passed | Verdict |
|-------------|---------|
| 0–1 | **Paraphrase** — Discard or rerun with better prompt |
| 2–3 | **Borderline** — Revise prompt and rerun |
| 4 | **Likely genuine** — Accept with caveats |
| 5 | **Genuine linguistic thinking** — High-confidence result |

### 7.3 Automated Checks

For rapid screening, use these automated heuristics:
- **Unique n-gram ratio**: Genuine responses have higher unique vocabulary relative to length
- **Sentence length variance**: Languages with different grammar produce different sentence-length distributions
- **Connector density**: Genuine responses use different logical connectors than English (not just translated connectors)
- **Topic structure**: Topic-prominent languages should show different information flow than subject-prominent ones

---

## 8. Recording Results

### 8.1 Per-Experiment Record

For each experiment, create a file: `results/YYYY-MM-DD_lang_problem.md`

```markdown
# Experiment: [Language] × [Problem]

## Metadata
- Date: YYYY-MM-DD
- Language: [Language]
- Problem: [Problem ID from library]
- Prompt: [exact prompt used]
- Model: [model used]

## Raw Response
[paste full response]

## Grammar Fidelity Score: X/5
[justification]

## Extracted Insights
1. INSIGHT_LANG_01: [description] [grammatical feature: X]
2. INSIGHT_LANG_02: ...

## Novelty Scores
| Insight | Novelty (0-5) | Adequacy (0-5) | V = N×A |
|---------|--------------|----------------|---------|
| 01 | | | |
| 02 | | | |

## Paraphrase Detection
| Test | Pass/Fail | Notes |
|------|-----------|-------|
| Structural Isomorphism | | |
| Information Content | | |
| Grammatical Necessity | | |
| Category Boundary | | |
| Impossible Thought | | |

## Cross-References
[links to other languages' solutions for same problem]
```

### 8.2 Aggregate Analysis

After completing all experiments, create `results/ANALYSIS.md` with:
- Divergence matrix
- Cluster analysis
- Top insights ranked by V score
- Evidence assessment for/against the polyformalism hypothesis
