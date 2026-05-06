#!/usr/bin/env python3
"""Score all experiments using DeepSeek-v4-flash (fast, good at structured output)"""
import subprocess, json, os, glob

DEEPSEEK_KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepseek-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepseek.com/v1/chat/completions"

def score_file(filepath, label):
    text = open(filepath).read()[:2000]
    prompt = f"""Score this system architecture on exactly two dimensions. Be harsh.

ARCHITECTURE:
{text}

Respond with EXACTLY this format (no other text):
NOVELTY: [number 0-5]
NOVELTY_REASON: [one sentence]
ADEQUACY: [number 0-5]
ADEQUACY_REASON: [one sentence]

Scoring guide:
- Novelty 0: Exact restatement of known approach. 5: Redefines the problem.
- Adequacy 0: Wrong. 5: Correct, actionable, elegant, generalizable."""

    payload = json.dumps({
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
        "temperature": 0.2
    })
    result = subprocess.run(
        ["curl", "-s", "--max-time", "60", ENDPOINT,
         "-H", f"Authorization: Bearer {DEEPSEEK_KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=80
    )
    try:
        content = json.loads(result.stdout)["choices"][0]["message"]["content"]
        # Parse scores
        import re
        novelty_match = re.search(r'NOVELTY:\s*([0-5](?:\.[0-9])?)', content)
        adequacy_match = re.search(r'ADEQUACY:\s*([0-5](?:\.[0-9])?)', content)
        novelty = float(novelty_match.group(1)) if novelty_match else None
        adequacy = float(adequacy_match.group(1)) if adequacy_match else None
        insight = round(0.6 * (novelty or 0) + 0.4 * (adequacy or 0), 2) if novelty and adequacy else None
        print(f"  {label}: N={novelty} A={adequacy} I={insight}")
        return {"novelty": novelty, "adequacy": adequacy, "insight": insight, "raw": content}
    except Exception as e:
        print(f"  {label}: FAILED ({e})")
        return None

# Collect all files to score
all_files = {}
# Original 9 experiments
for exp in [1, 2, 3]:
    for lang in ['greek', 'chinese', 'navajo']:
        f = f"/tmp/experiment-{exp}-{lang}.md"
        if os.path.exists(f):
            all_files[f"orig-{exp}-{lang}"] = f

# Batch A1
for lang in ['arabic', 'finnish', 'quechua', 'korean']:
    for p in ['p1', 'p2', 'p3']:
        f = f"/tmp/exp-a1-{lang}-{p}.md"
        if os.path.exists(f):
            all_files[f"a1-{lang}-{p}"] = f

# Batch A2
for p in ['p1', 'p2', 'p3']:
    f = f"/tmp/exp-a2-english-{p}.md"
    if os.path.exists(f):
        all_files[f"a2-english-{p}"] = f

# Batch A3
for f in glob.glob("/tmp/exp-a3-*.md"):
    name = os.path.basename(f).replace('.md','').replace('exp-a3-','a3-')
    all_files[name] = f

# Batch D1
for n in range(1, 9):
    f = f"/tmp/exp-d1-round{n}.md"
    if os.path.exists(f):
        all_files[f"d1-round{n}"] = f

# Batch D3
for f in glob.glob("/tmp/exp-d3-*.md"):
    name = os.path.basename(f).replace('.md','').replace('exp-d3-','d3-')
    all_files[name] = f

print(f"Scoring {len(all_files)} architectures...\n")

results = {}
for label, filepath in sorted(all_files.items()):
    r = score_file(filepath, label)
    if r:
        results[label] = r
    # Rate limit
    import time
    time.sleep(0.5)

# Save full results
with open("/tmp/all-scores.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

# Analysis
print("\n" + "=" * 70)
print("SCORE SUMMARY BY CATEGORY")
print("=" * 70)

categories = {
    "Original (Greek)": [k for k in results if k.startswith("orig-") and "greek" in k],
    "Original (Chinese)": [k for k in results if k.startswith("orig-") and "chinese" in k],
    "Original (Navajo)": [k for k in results if k.startswith("orig-") and "navajo" in k],
    "A1 (Arabic)": [k for k in results if k.startswith("a1-arabic")],
    "A1 (Finnish)": [k for k in results if k.startswith("a1-finnish")],
    "A1 (Quechua)": [k for k in results if k.startswith("a1-quechua")],
    "A1 (Korean)": [k for k in results if k.startswith("a1-korean")],
    "A2 (English control)": [k for k in results if k.startswith("a2-")],
    "A3 (Random mode)": [k for k in results if k.startswith("a3-")],
    "D1 (Debate rounds)": [k for k in results if k.startswith("d1-")],
    "D3 (Translation)": [k for k in results if k.startswith("d3-translate")],
    "D3 (Thinking)": [k for k in results if k.startswith("d3-think")],
}

for cat, keys in categories.items():
    if not keys:
        continue
    scores = [results[k] for k in keys if k in results]
    novelties = [s['novelty'] for s in scores if s and s.get('novelty') is not None]
    adequacies = [s['adequacy'] for s in scores if s and s.get('adequacy') is not None]
    insights = [s['insight'] for s in scores if s and s.get('insight') is not None]
    
    avg_n = sum(novelties)/len(novelties) if novelties else 0
    avg_a = sum(adequacies)/len(adequacies) if adequacies else 0
    avg_i = sum(insights)/len(insights) if insights else 0
    print(f"  {cat:30s}: N={avg_n:.1f} A={avg_a:.1f} I={avg_i:.2f} (n={len(scores)})")

print("\n" + "=" * 70)
print("FALSIFICATION CHECKS")
print("=" * 70)

# Check English control vs linguistic modes
english_insights = [results[k]['insight'] for k in results if k.startswith("a2-") and results[k].get('insight')]
linguistic_insights = [results[k]['insight'] for k in results if k.startswith(("orig-","a1-")) and results[k].get('insight')]
if english_insights and linguistic_insights:
    eng_avg = sum(english_insights) / len(english_insights)
    ling_avg = sum(linguistic_insights) / len(linguistic_insights)
    print(f"  English avg insight: {eng_avg:.2f}")
    print(f"  Linguistic avg insight: {ling_avg:.2f}")
    print(f"  Ratio: {ling_avg/eng_avg:.2f}x")
    if ling_avg > eng_avg * 1.3:
        print("  ✓ Linguistic modes produce significantly higher insight scores")
    else:
        print("  ✗ FALSIFICATION: Linguistic modes not significantly better than English")

# Check translation vs thinking
trans_insights = [results[k]['insight'] for k in results if k.startswith("d3-translate") and results[k].get('insight')]
think_insights = [results[k]['insight'] for k in results if k.startswith("d3-think") and results[k].get('insight')]
if trans_insights and think_insights:
    trans_avg = sum(trans_insights) / len(trans_insights)
    think_avg = sum(think_insights) / len(think_insights)
    print(f"\n  Translation avg insight: {trans_avg:.2f}")
    print(f"  Thinking avg insight: {think_avg:.2f}")
    if think_avg > trans_avg * 1.2:
        print("  ✓ Thinking mode produces higher insights than translation")
    else:
        print("  ✗ FALSIFICATION: Translation equivalent to thinking")

# Check debate rounds for inverted-U
round_insights = {}
for n in range(1, 9):
    k = f"d1-round{n}"
    if k in results and results[k].get('insight'):
        round_insights[n] = results[k]['insight']
if len(round_insights) >= 5:
    print(f"\n  Debate round insights: {round_insights}")
    peak_round = max(round_insights, key=round_insights.get)
    print(f"  Peak at round {peak_round}")
    if peak_round in [3, 4, 5]:
        print("  ✓ SUPPORTS inverted-U at rounds 3-5")
    else:
        print(f"  ⚠ Peak at round {peak_round} — check if supports/falsifies")
