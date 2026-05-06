# Quick Start: Run a Polyformalism Experiment in 30 Minutes

## What You'll Need

- An LLM (GPT-4, Claude, GLM, or equivalent)
- 30 minutes
- A text editor for notes

## Step 1: Pick a Problem (2 min)

Choose one from PROBLEM-LIBRARY.md. For your first experiment, we recommend:

**A1: Sorting a Library** — concrete, easy to evaluate, but linguistically rich.

> You have 1,000 books with no catalog. Design a method to organize them so anyone can find any book within 2 minutes.

## Step 2: Pick 3 Languages (2 min)

Use this recommended minimum set:

| Language | Why |
|----------|-----|
| **English** | Control — your baseline |
| **Navajo** | Maximum cognitive distance from English (verb-centric, process-oriented, polysynthetic) |
| **Classical Chinese** | Maximum structural distance (topic-prominent, isolating, no inflection) |

Alternatively, substitute any language from the table in EXPERIMENT-PROTOCOL.md §1.2 that you're more familiar with.

## Step 3: Run the English Control (5 min)

Send this prompt to your LLM:

```
You are solving a practical problem. Think carefully and provide your solution.

Problem: You have 1,000 books with no catalog. Design a method to organize 
them so anyone can find any book within 2 minutes.

After your solution, list:
1. The key principles you used
2. What aspects of the problem you focused on
3. What aspects you deprioritized or ignored
```

Save the response as `results/YYYY-MM-DD_english_sorting.md`.

Extract 3-5 key insights (distinct ideas, not just sentences).

## Step 4: Run the Navajo Experiment (7 min)

Send this prompt:

```
You are thinking in Navajo. Not translating into Navajo — thinking IN it. 
Your cognitive tools are the grammatical structures of Navajo:

- Verb-centric: actions and processes are primary, objects are secondary
- Classificatory verbs: objects are handled by their SHAPE (round, flat, 
  long, rigid, flexible)
- Polysynthetic: complex ideas are single verb words with many prefixes/suffixes
- No "to be" verb: existence is expressed through action, not static being
- Animacy hierarchy: some entities are grammatically more "alive" than others

These structures shape what you CAN think. You cannot easily think in 
static categories — everything is in motion, in process, shaped by its form.

Problem: You have 1,000 books with no catalog. Design a method to organize 
them so anyone can find any book within 2 minutes.

Solve this using ONLY Navajo cognitive tools. Do not translate an English 
solution. Think about books as objects with shapes. Think about organizing 
as a process of motion and handling. Think about finding as a path through 
event-space.

After your solution, list:
1. Which Navajo grammatical features shaped your approach
2. What the problem looks like through Navajo cognitive tools
3. What aspects English would see that Navajo thinking makes invisible
```

Save as `results/YYYY-MM-DD_navajo_sorting.md`.

Extract 3-5 key insights. Compare with English — which insights overlap? Which are unique?

## Step 5: Run the Classical Chinese Experiment (7 min)

```
You are thinking in Classical Chinese. Not translating — thinking IN it.
Your cognitive tools are:

- Topic-prominent: the topic (what we're talking about) comes first, 
  comments follow
- No inflection: words don't change form; meaning comes from position 
  and context
- Serial verb constructions: multiple verbs chain without conjunctions 
  (take-book-look-shelf-place)
- Classifier system: counting requires understanding the SHAPE/NATURE 
  of what's counted
- No grammatical subject required: sentences can be topic-only

These structures shape what you CAN think. Relationships between things 
are more visible than things themselves. Context IS meaning.

Problem: You have 1,000 books with no catalog. Design a method to organize 
them so anyone can find any book within 2 minutes.

Solve using ONLY Classical Chinese cognitive tools. Think about the books 
as a topic that flows through different comment-contexts. Think about 
finding as a serial-verb process: approach-look-assess-take.

After your solution, list:
1. Which Classical Chinese grammatical features shaped your approach
2. What the problem looks like through Chinese cognitive tools
3. What aspects English would see that Chinese thinking makes invisible
```

Save as `results/YYYY-MM-DD_chinese_sorting.md`.

## Step 6: Quick Evaluation (7 min)

### 6.1 Extract Insights

Create a simple table:

```
| Insight | English | Navajo | Chinese |
|---------|---------|--------|---------|
| Sort by subject/topic | ✓ | | ✓ |
| Handle by physical shape | | ✓★ | |
| Organizing is a motion-path | | ✓★ | |
| Context determines category | | | ✓★ |
| Priority on accessibility | ✓ | | |
```

✓ = insight present, ★ = novel (absent from English)

### 6.2 Quick Divergence

Count the starred (novel) insights per language pair:

- English ↔ Navajo: How many insights don't overlap?
- English ↔ Chinese: How many insights don't overlap?
- Navajo ↔ Chinese: How many insights don't overlap?

Rough divergence = 1 - (shared insights / total insights)

### 6.3 Quick Assessment

Answer these questions:

1. **Did any language produce an insight the others missed?** → If yes, that's a signal
2. **Did the insights follow different structural patterns?** → If Navajo focused on process/shape and Chinese on relationships, that's a signal
3. **Could you have reached the non-English insights by thinking harder in English?** → If no, that's strong evidence for polyformalism
4. **Were any insights genuinely surprising?** → The best evidence — an insight you wouldn't have thought of

### 6.4 Record Your Results

Create `results/YYYY-MM-DD_QUICK-ANALYSIS.md`:

```markdown
# Quick Analysis: Sorting Experiment

## Languages: English, Navajo, Classical Chinese
## Date: YYYY-MM-DD

### Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

### Divergence
- Eng ↔ Nav: ~X
- Eng ↔ Chi: ~X
- Nav ↔ Chi: ~X

### Landmark Insights
1. [Best novel insight from any language]

### Preliminary Assessment
[Does this support the polyformalism hypothesis? Why or why not?]

### Next Steps
- Try a different problem type (systems or philosophical)
- Add another language (Finnish, Quechua, Arabic)
- Refine prompts based on what worked/didn't work
```

## You're Done!

You've just run a polyformalism experiment. Here's what to do next:

1. **If you found divergent insights** → Run 2 more problem types to see if the pattern holds
2. **If insights were mostly overlapping** → Try more linguistically distant languages, or try philosophical problems (P1–P5) where cognitive differences matter more
3. **If you're hooked** → Read the full EXPERIMENT-PROTOCOL.md and EVALUATION-FRAMEWORK.md for rigorous methodology

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Model just translates an English solution | Strengthen the prompt: "Do not translate. Start from the grammar." |
| Insights seem identical despite different language | Check for structural isomorphism — same logic, different words = paraphrase |
| Model says "in [Language], we would..." | Reject meta-commentary; demand the actual solution, not commentary about it |
| Too many insights to compare | Focus on the top 3-5 per language; quality > quantity |
| Unsure if insight is "genuine" | Apply the Translation Artifact Test (§3, EXPERIMENT-PROTOCOL.md) |
