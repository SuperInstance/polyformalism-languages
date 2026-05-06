#!/usr/bin/env python3
"""Batch D1: Debate round scaling (1-8 rounds) + D2: Rewrite depth scaling + D3: Translation vs Thinking"""
import subprocess, json, os

KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"

def run_call(label, prompt, outfile):
    payload = json.dumps({
        "model": "ByteDance/Seed-2.0-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
        "temperature": 0.8
    })
    result = subprocess.run(
        ["curl", "-s", "--max-time", "180", ENDPOINT,
         "-H", f"Authorization: Bearer {KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=200
    )
    try:
        content = json.loads(result.stdout)["choices"][0]["message"]["content"]
        with open(outfile, "w") as f:
            f.write(content)
        lines = content.count("\n") + 1
        print(f"  ✓ {label}: {lines} lines")
        return True
    except Exception as e:
        print(f"  ✗ {label}: {e}")
        return False

# D1: Debate round scaling — rounds 1-8
# Round N means: N different linguistic perspectives must be integrated
languages = [
    ("English", "standard engineering thinking"),
    ("Ancient Greek", "telos, aspect, middle voice, logos, horos"),
    ("Classical Chinese", "topic-prominent, pattern-thinking, multigrade words"),
    ("Navajo", "classificatory verbs, shape+motion, verb-centric"),
    ("Arabic", "root-and-pattern, deep structure vs surface"),
    ("Finnish", "15 cases, abessive, translative, case-stacking"),
    ("Quechua", "evidentiality -mi/-si/-cha, inclusive we"),
    ("Korean", "honorific levels, particles, social grammar"),
]

PROBLEM = "Design the most creative constraint system possible — one that produces novel useful outputs no designer anticipated."

for n in range(1, 9):
    langs = languages[:n]
    lang_desc = ", ".join(f"{l[0]} ({l[1]})" for l in langs)
    prompt = f"""You have gone through {n} round{"s" if n > 1 else ""} of polyformalism debate.
Each round used a different linguistic thinking mode. The modes used so far: {lang_desc}

Now INTEGRATE all {n} perspectives into a single architecture for this problem:
{PROBLEM}

After presenting the architecture, score yourself:
- Novelty (0-5): How novel is this compared to standard engineering approaches?
- Adequacy (0-5): How correct, actionable, and generalizable is this?
- Insight Score: novelty × 0.6 + adequacy × 0.4"""
    run_call(f"d1-round{n}", prompt, f"/tmp/exp-d1-round{n}.md")

# D3: Translation vs Thinking
for lang_name, lang_tools in [("Navajo", "classificatory verbs, shape+motion, verb-centric"),
                                ("Classical Chinese", "topic-prominent, pattern-thinking, multigrade words"),
                                ("Ancient Greek", "telos, aspect, middle voice, logos, horos")]:
    # Group A: Translation
    prompt_a = f"""Here is a standard engineering solution to the problem of detecting when constraints are about to be violated:

Standard approach: Set threshold values for each constraint. Monitor continuously. When value approaches threshold within safety margin, trigger warning. Use predictive models to estimate time-to-violation.

Now TRANSLATE this solution into {lang_name} style. Use {lang_tools} vocabulary and metaphors to describe the same system. Do NOT change the architecture — only reword it using {lang_name} linguistic style."""

    # Group B: Fresh thinking
    prompt_b = f"""Think ENTIRELY in {lang_name} cognitive mode. {lang_tools}.

PROBLEM: Design a system that detects when constraints are about to be violated BEFORE they actually break.

Start from scratch. Do NOT reference any standard engineering approach. Use ONLY {lang_name} grammatical thinking tools to conceptualize and solve this problem."""

    run_call(f"d3-translate-{lang_name.lower()}", prompt_a, f"/tmp/exp-d3-translate-{lang_name.lower()}.md")
    run_call(f"d3-think-{lang_name.lower()}", prompt_b, f"/tmp/exp-d3-think-{lang_name.lower()}.md")

print("\nD1+D3 complete")
