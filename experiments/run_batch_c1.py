#!/usr/bin/env python3
"""Batch C1: Blinded scoring of all experimental results"""
import subprocess, json, os, glob

KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"

def run_score(label, prompt):
    payload = json.dumps({
        "model": "ByteDance/Seed-2.0-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000,
        "temperature": 0.3
    })
    result = subprocess.run(
        ["curl", "-s", "--max-time", "120", ENDPOINT,
         "-H", f"Authorization: Bearer {KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=140
    )
    try:
        content = json.loads(result.stdout)["choices"][0]["message"]["content"]
        outfile = f"/tmp/exp-c1-{label}.json"
        with open(outfile, "w") as f:
            f.write(content)
        print(f"  ✓ {label}")
        return True
    except Exception as e:
        print(f"  ✗ {label}: {e}")
        return False

# Collect all experiment files
all_files = sorted(glob.glob("/tmp/exp-a1-*.md") + glob.glob("/tmp/exp-a2-*.md") + 
                   glob.glob("/tmp/exp-a3-*.md") + 
                   glob.glob("/tmp/experiment-1-*.md") + glob.glob("/tmp/experiment-2-*.md") + 
                   glob.glob("/tmp/experiment-3-*.md"))

# Build blinded scoring prompt
readings = []
for f in all_files:
    basename = os.path.basename(f)
    # Strip language identifier to blind the judge
    content = open(f).read()[:1500]  # truncate to keep within context
    readings.append(f"--- ARCHITECTURE {basename} ---\n{content}\n")

all_text = "\n".join(readings)

# Score in batches of 3 (context window limit)
batch_size = 3
for i in range(0, len(all_files), batch_size):
    batch = all_files[i:i+batch_size]
    batch_text = ""
    for f in batch:
        content = open(f).read()[:1200]
        basename = os.path.basename(f).replace(".md","")
        batch_text += f"\n--- ARCHITECTURE {basename} ---\n{content}\n"
    
    prompt = f"""You are an independent judge scoring system architectures. You do NOT know what methodology produced these. Score each on two dimensions.

{batch_text}

For EACH architecture, provide ONLY JSON:
{{
  "architecture": "<name>",
  "novelty": <0-5>,
  "novelty_reason": "<one sentence>",
  "adequacy": <0-5>,
  "adequacy_reason": "<one sentence>",
  "combined": <novelty + adequacy>,
  "guess_method": "<your best guess at what thinking style produced this>"
}}"""

    run_score(f"batch-{i//batch_size}", prompt)

print(f"\nC1 scoring complete: {len(all_files)} architectures scored")
