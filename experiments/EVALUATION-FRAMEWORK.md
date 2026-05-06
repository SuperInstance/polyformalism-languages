# Evaluation Framework: Linguistic Polyformalism

## 1. Insight Detection Matrix

### 1.1 Structure

The Insight Detection Matrix (IDM) is the primary evaluation tool. It maps insights across languages and dimensions.

**Rows:** Languages (L₁, L₂, ..., Lₙ)
**Columns:** Insight dimensions derived from our neuroscience framework

| Dimension | Source | What It Measures |
|-----------|--------|------------------|
| **Decomposition** | ECN | How the problem is broken into sub-problems |
| **Categorization** | ECN | What categories are applied to problem elements |
| **Relationship** | DMN | What connections between elements are identified |
| **Process** | DMN | How change, time, and causality are modeled |
| **Evaluation** | Salience | What counts as a "good" solution |
| **Epistemology** | ECN/DMN | What knowledge sources are tracked and trusted |
| **Social** | DMN | How social/contextual factors are integrated |
| **Boundary** | Salience | Where the problem's edges are drawn |

### 1.2 Filling the Matrix

For each language-problem pair, the experimenter fills in:

```
IDM[language][dimension] = {
    insights: [list of specific insights],
    grammatical_source: [which grammatical feature produced these insights],
    confidence: [0-5, how confident we are this is genuine],
    novel: [bool, is this insight absent from the English control?]
}
```

### 1.3 Matrix Visualization

```
             Decomposition  Categorization  Relationship  Process  Evaluation  Epistemology  Social  Boundary
English         [3]            [2]             [1]          [2]       [4]          [2]         [1]      [3]
Navajo          [5]★           [1]             [2]          [5]★      [3]          [1]         [2]      [4]
Classical       [2]            [4]             [5]★         [3]       [3]          [3]         [4]★     [2]
Chinese
Quechua         [2]            [3]             [2]          [3]       [3]          [5]★        [3]      [4]
Finnish         [4]            [5]★            [3]          [3]       [4]          [2]         [2]      [5]★

★ = landmark insight (novel, high-confidence, high-illumination)
```

Numbers represent the count of distinct insights in that dimension for that language. Stars mark landmark insights.

---

## 2. Orthogonality Score

### 2.1 Definition

The Orthogonality Score measures how *different* two languages' insights are from each other.

**O(L₁, L₂)** = the degree to which insights from L₁ and L₂ cover non-overlapping regions of the insight space.

### 2.2 Calculation

For each pair of languages solving the same problem:

1. Extract all insights from both languages: I(L₁) and I(L₂)
2. For each pair of insights (i ∈ I(L₁), j ∈ I(L₂)), compute semantic similarity s(i, j) ∈ [0, 1]
3. For each insight in I(L₁), find its best match in I(L₂): max_match(i) = max_j s(i, j)
4. **Overlap** = (1/|I(L₁)|) Σ max_match(i) + (1/|I(L₂)|) Σ max_match(j)
5. **Orthogonality** O(L₁, L₂) = 1 - Overlap/2

### 2.3 Interpretation

| O(L₁, L₂) | Interpretation |
|-----------|---------------|
| 0.0 – 0.2 | Nearly identical insights — likely translation artifacts |
| 0.2 – 0.4 | High overlap — same cognitive approach, minor differences |
| 0.4 – 0.6 | Moderate divergence — some genuinely different insights |
| 0.6 – 0.8 | High orthogonality — substantially different cognitive approaches |
| 0.8 – 1.0 | Near-complete orthogonality — strong evidence for linguistic relativity in insight production |

### 2.4 Expected Values (Based on Linguistic Distance)

Based on our language families framework, predicted orthogonality ranges:

| Pair | Predicted O | Rationale |
|------|-----------|-----------|
| English ↔ German | 0.1 – 0.3 | Same family, same cognitive tools |
| English ↔ Russian | 0.3 – 0.5 | Same family, but aspectual system diverges |
| English ↔ Finnish | 0.4 – 0.6 | Different family, case system, no gender |
| English ↔ Classical Chinese | 0.5 – 0.7 | Maximal structural distance |
| English ↔ Navajo | 0.6 – 0.8 | Verb-centric vs. noun-centric paradigm shift |
| Navajo ↔ Classical Chinese | 0.5 – 0.7 | Both non-IE but very different from each other |

---

## 3. Completeness Score

### 3.1 Definition

The Completeness Score measures what fraction of the total insight space is covered by a set of languages.

**C(L₁, L₂, ..., Lₙ)** = |union(I(L₁), I(L₂), ..., I(Lₙ))| / |theoretical maximum insights|

### 3.2 Theoretical Maximum

The theoretical maximum insight count is unknown but can be estimated:

1. Run the problem in 5+ languages
2. Observe the rate of new insights per additional language
3. Fit a saturation curve: total_insights(N) = a × (1 - e^(-bN))
4. The asymptote `a` estimates the theoretical maximum

### 3.3 Marginal Insight Contribution

For each additional language added, measure how many *new* insights it contributes:

```
Marginal(Lₖ) = |I(Lₖ) \ union(I(L₁), ..., I(Lₖ₋₁))|
```

Languages with high marginal contribution are cognitively distant from the already-sampled set. If marginal contribution stays high as you add languages, the insight space is large (strong polyformalism). If it quickly drops to zero, the insight space is small (weak polyformalism).

### 3.4 Coverage Visualization

```
| Insights
|     ████
|   ████████
| ████████████          ← diminishing returns
|████████████████
|████████████████████
|______________________
  1  2  3  4  5  6  7   ← Languages added (by linguistic distance)
```

If the curve plateaus early → languages don't add much beyond English (weak polyformalism).
If the curve keeps rising → each distant language genuinely adds new insights (strong polyformalism).

---

## 4. Statistical Tests

### 4.1 Are the Insights Genuinely Different or Just Noise?

**Null hypothesis (H₀):** All languages produce insights drawn from the same distribution. Observed differences are random noise.

**Alternative hypothesis (H₁):** Different languages produce insights drawn from different distributions. Observed differences reflect genuine cognitive divergence.

### 4.2 Tests

#### Test 1: Permutation Test on Orthogonality

1. Compute the observed mean orthogonality: Ō = mean(O(Lᵢ, Lⱼ)) for all pairs
2. Randomly permute language labels across insights 10,000 times
3. For each permutation, compute Ō_random
4. **p-value** = fraction of permutations where Ō_random ≥ Ō_observed
5. Reject H₀ if p < 0.05

This tests whether the observed orthogonality is higher than what you'd get by random assignment.

#### Test 2: Chi-Square Test on Insight Distribution

1. For each insight dimension, count how many languages produce insights in that dimension
2. Under H₀, insights should be evenly distributed across dimensions for all languages
3. Compute χ² = Σ (observed - expected)² / expected
4. Reject H₀ if χ² exceeds critical value (df = (languages-1) × (dimensions-1))

This tests whether certain languages systematically produce more insights in certain dimensions.

#### Test 3: Bootstrap Confidence Intervals on Divergence

1. For each language pair, compute D(L₁, L₂)
2. Bootstrap resample insights (with replacement) 10,000 times
3. Compute 95% confidence interval for each D(L₁, L₂)
4. If the CI excludes 0, the divergence is significant

This gives confidence intervals for pairwise divergence without distributional assumptions.

#### Test 4: Mantel Test on Linguistic Distance vs. Insight Divergence

1. Construct a linguistic distance matrix (based on grammatical features)
2. Construct an insight divergence matrix D
3. Compute correlation between the two matrices
4. Use Mantel test (10,000 permutations) to test significance

**This is the key test.** If linguistic distance correlates with insight divergence, it's strong evidence for the polyformalism hypothesis.

### 4.3 Effect Sizes

Statistical significance alone isn't enough. Report effect sizes:

- **Cohen's d** for pairwise language differences
- **η² (eta-squared)** for overall language effect on insight distribution
- **r** for the Mantel correlation between linguistic distance and insight divergence

Interpretation:
- r < 0.3: Weak evidence — linguistic distance barely predicts insight divergence
- r = 0.3–0.6: Moderate evidence — grammar shapes some aspects of thought
- r > 0.6: Strong evidence — language substantially shapes insight production

---

## 5. The Divergence Metric

### 5.1 Definition

**D(L₁, L₂)** = 1 - overlap(I(L₁), I(L₂))

Where overlap is the Jaccard similarity of the insight sets:

overlap(I₁, I₂) = |I₁ ∩ I₂| / |I₁ ∪ I₂|

### 5.2 Semantic Overlap (Preferred)

Since insights are rarely identical in wording, use semantic overlap:

```
overlap_semantic(I₁, I₂) = (1/|I₁|) Σᵢ maxⱼ sim(i, j) + (1/|I₂|) Σⱼ maxᵢ sim(i, j)) / 2
```

Where sim(i, j) is cosine similarity of insight embeddings (e.g., from a sentence-transformer model).

### 5.3 Weighted Divergence

Not all insights are equally important. Weight by insight quality:

```
D_weighted(L₁, L₂) = 1 - Σ (w_i × w_j × sim(i,j)) / Σ (w_i × w_j)
```

Where w_i = V(i) = novelty(i) × adequacy(i) from the evaluation rubric.

This ensures that divergence on trivial insights doesn't inflate the score.

### 5.4 The Divergence Matrix

For N languages, produce an N×N matrix:

```
     Eng   Nav   Chi   Que   Fin
Eng  0.00  0.72  0.61  0.55  0.48
Nav  0.72  0.00  0.58  0.64  0.69
Chi  0.61  0.58  0.00  0.51  0.47
Que  0.55  0.64  0.51  0.00  0.53
Fin  0.48  0.69  0.47  0.53  0.00
```

Properties:
- Diagonal = 0 (a language doesn't diverge from itself)
- Symmetric: D(L₁, L₂) = D(L₂, L₁)
- Range: [0, 1]

### 5.5 From Divergence to Evidence

The divergence matrix is the primary evidence for or against the polyformalism hypothesis:

**If D values are generally low (< 0.3):** Languages produce similar insights → weak linguistic relativity for creative thought

**If D values correlate with linguistic distance:** Grammar shapes cognition → strong evidence for polyformalism

**If specific language pairs show extreme D (> 0.8):** Those pairs are "gradient-maximized" → natural targets for deep study

**If D values are uniformly moderate (0.3–0.6):** Language has *some* effect but isn't the dominant factor → nuanced position

---

## 6. Reporting Standards

### 6.1 Minimum Report Contents

Every experiment report must include:

1. **IDM** for each language-problem pair
2. **Divergence matrix** for the full language set
3. **Orthogonality scores** for all pairs
4. **Completeness curve** showing marginal insight contribution
5. **Statistical test results** with p-values and effect sizes
6. **Landmark insights** — the top 5 novel insights across all experiments
7. **Evidence assessment** — does this experiment set support or refute polyformalism?

### 6.2 Confidence Levels

| Evidence Level | Criteria |
|---------------|----------|
| **Tentative** | < 3 languages, no statistical tests, anecdotal observations |
| ** suggestive** | 3–5 languages, permutation test significant, effect size > 0.3 |
| **Strong** | 5+ languages, Mantel test significant, effect size > 0.5, replicated across problem types |
| **Conclusive** | 8+ languages, all statistical tests significant, effect size > 0.6, replicated by independent researchers |

### 6.3 Open Data

All raw data (prompts, responses, insight extractions, scores) should be included in `results/raw/` for reproducibility and meta-analysis.
