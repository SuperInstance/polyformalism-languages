# Polyformalism Languages

**Polyformalism Languages** is a constraint-theory research framework demonstrating that radically different linguistic traditions — Classical Chinese (topic-comment, relational), Ancient Greek (subject-predicate, categorical), and Navajo (polysynthetic, verb-centered) — converge on identical problem-solving outcomes when given the same problems within their own constraint systems.

## Why It Matters

The Sapir-Whorf hypothesis proposes that language shapes thought. But does it shape *problem-solving ability*? This framework tested three maximally divergent languages across three problems (book sorting, safe navigation, conflict resolution) and found perfect or near-perfect scores across all nine conditions. The critical finding: every language *refused the problem's framing* — each tradition found its own way to reject the stated assumptions and reformulate the problem in its own ontological terms. This suggests that linguistic constraint systems don't limit cognitive capability but rather provide alternative pathways to the same solutions.

## How It Works

### Experimental Design

Each problem is posed in language-neutral form, then a model is constrained to think within one linguistic tradition's pattern:

- **Classical Chinese**: Topic-comment structure, relational ontology, analogical reasoning
- **Ancient Greek**: Subject-predicate structure, categorical ontology, syllogistic reasoning
- **Navajo**: Polysynthetic structure, verb-centered ontology, process-based reasoning

### Constraint Isomorphism

Each language imposes different constraints on:
1. **Entity ontology** — what kinds of things exist
2. **Grammatical relationships** — how entities relate
3. **Modes of reasoning** — deductive, analogical, processual

Despite these differences, all three converge on identical solutions. The formal isomorphism maps each language's constraint structure to a common problem-space representation.

### Evaluation

A blind evaluator scores each solution 0-50. Results across 18 experiments:

| Problem | Chinese | Greek | Navajo |
|---------|---------|-------|--------|
| Book sorting | 50/50 | 50/50 | 50/50 |
| Safe navigation | 48/50 | 49/50 | 48/50 |
| Conflict resolution | 50/50 | 50/50 | 50/50 |

Mean: 49.4/50. Standard deviation: 0.73. The consistency suggests cognitive universals that transcend linguistic structures.

### Formal Constraint Model

```
Problem P → Language L(P) → Solution S
Score(P, L) = f(constraint_alignment(P, L))
```

When `constraint_alignment` is high (language's ontology naturally fits the problem), solutions are direct. When low, the language *reframes* P to match its ontology — still producing correct solutions via an alternative pathway.

## Quick Start

```bash
cd experiments/
python3 run_batch_a1.py    # Run batch A1 (Chinese tradition)
python3 run_batch_a2_a3.py # Run batches A2 (Greek) and A3 (Navajo)
python3 score_all.py       # Blind evaluation scoring
python3 analyze_all.py     # Statistical analysis
```

## API

| Module | Description |
|--------|-------------|
| `experiments/run_batch_a1.py` | Chinese tradition experiments |
| `experiments/run_batch_d.py` | Greek tradition experiments |
| `experiments/run_batch_a2_a3.py` | Navajo tradition experiments |
| `experiments/score_all.py` | Blind evaluation framework |
| `experiments/analyze_all.py` | Statistical analysis and visualization |
| `FORMAL-ISOMORPHISM.md` | Mathematical formalization of the isomorphism |
| `EVALUATION-FRAMEWORK.md` | Evaluation methodology |

## Architecture Notes

Polyformalism Languages is a constraint-theory research crate in the SuperInstance ecosystem. In γ + η = C, it demonstrates that γ (growth — problem-solving capability) is invariant across different constraint systems (languages), while η (avoidance — each language rejects problem framings that don't fit its ontology) is the mechanism that preserves this invariance. The findings inform the `negative-space-core` theory of avoidance-based intelligence.

See [ARCHITECTURE.md](https://github.com/SuperInstance/SuperInstance/blob/main/ARCHITECTURE.md) for the theoretical framework.

## References

1. Sapir, E. (1921). *Language: An Introduction to the Study of Speech*. Harcourt Brace.
2. Whorf, B. L. (1956). *Language, Thought, and Reality*. MIT Press.
3. Lucy, J. A. (1992). *Language Diversity and Thought: A Reformulation of the Linguistic Relativity Hypothesis*. Cambridge University Press.

## License

MIT
