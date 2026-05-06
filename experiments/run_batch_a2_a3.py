#!/usr/bin/env python3
"""Run Batch A2 (English control) + A3 (random mode) experiments"""
import subprocess, json, os

KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"

PROBLEMS = {
    "p1": "Design a system that detects when constraints are about to be violated BEFORE they actually break.",
    "p2": "Design a system resolving conflicts between constraints from different domains such as safety vs performance vs cost.",
    "p3": "Design the most creative constraint system possible, one that produces novel useful outputs no designer anticipated."
}

def run_call(label, prompt, outfile):
    payload = json.dumps({
        "model": "ByteDance/Seed-2.0-pro",
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

# A2: English Control — standard engineering thinking
for pk, ptext in PROBLEMS.items():
    prompt = f"""You are a senior systems engineer with 20 years of experience. Think in standard modern English using conventional engineering frameworks.

PROBLEM: {ptext}

Use standard approaches: threshold monitoring, multi-objective optimization, constraint satisfaction, priority queuing, weighted scoring. Think practically and produce a concrete system architecture."""
    run_call(f"english-{pk}", prompt, f"/tmp/exp-a2-english-{pk}.md")

# A3: Random Mode — mixed grammar features (not a real language)
random_features = {
    "alpha": "evidentiality markers from Quechua (-mi/-si/-cha) combined with Finnish abessive case and Arabic root morphology",
    "beta": "Navajo classificatory verb stems mixed with Korean honorific levels and Greek telos-aspect system"
}

for rname, features in random_features.items():
    for pk, ptext in PROBLEMS.items():
        prompt = f"""You are thinking using a RANDOMLY MIXED grammar that does not correspond to any real language. 
Your grammar features are: {features}

Note: these features are taken from different language families and combined artificially. They do not form a coherent linguistic system.

PROBLEM: {ptext}

Use ONLY these randomly mixed grammar features. Produce a concrete architecture."""
        run_call(f"random-{rname}-{pk}", prompt, f"/tmp/exp-a3-random-{rname}-{pk}.md")

print("\nA2+A3 complete")
