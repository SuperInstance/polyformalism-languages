#!/usr/bin/env python3
"""Analyze all experiment results and produce falsification report"""
import json, os, re, glob

def parse_scores(text):
    """Extract novelty and adequacy scores from text"""
    novelty = None
    adequacy = None
    combined = None
    # Look for patterns like "Novelty: 4" or "novelty": 4
    for pattern, attr in [
        (r'[Nn]ovelty[\s:]+([0-5](?:\.[0-9])?)', 'novelty'),
        (r'[Aa]dequacy[\s:]+([0-5](?:\.[0-9])?)', 'adequacy'),
        (r'[Cc]ombined[\s:]+([0-9]+(?:\.[0-9])?)', 'combined'),
        (r'[Ii]nsight[\s\w]*[Ss]core[\s:]+([0-9]+(?:\.[0-9])?)', 'insight'),
    ]:
        m = re.search(pattern, text)
        if m:
            val = float(m.group(1))
            if attr == 'novelty': novelty = val
            elif attr == 'adequacy': adequacy = val
            elif attr == 'combined': combined = val
    return {'novelty': novelty, 'adequacy': adequacy, 'combined': combined}

# D1: Debate Round Scaling — check for inverted-U
print("=" * 70)
print("D1: DEBATE ROUND SCALING (Testing Claim 5: Inverted-U)")
print("=" * 70)
round_scores = {}
for n in range(1, 9):
    f = f"/tmp/exp-d1-round{n}.md"
    if os.path.exists(f):
        text = open(f).read()
        scores = parse_scores(text)
        round_scores[n] = scores
        nv = scores['novelty'] or '?'
        ad = scores['adequacy'] or '?'
        cb = scores['combined'] or '?'
        print(f"  Round {n}: Novelty={nv}, Adequacy={ad}, Combined={cb}")
        # Show first insight line
        for line in text.split('\n')[:3]:
            if line.strip():
                print(f"    → {line.strip()[:80]}")
                break

print()
if round_scores:
    # Check for inverted-U pattern
    combineds = [(n, round_scores[n].get('combined')) for n in round_scores if round_scores[n].get('combined')]
    if combineds:
        max_round = max(combineds, key=lambda x: x[1])
        print(f"  Peak at Round {max_round[0]} (score {max_round[1]})")
        if max_round[0] in [3, 4, 5]:
            print("  ✓ SUPPORTS Claim 5: Inverted-U peak at rounds 3-5")
        elif max_round[0] in [1, 2]:
            print("  ✗ FALSIFIES Claim 5: Peak at round 1-2 (single-round sufficient)")
        elif max_round[0] in [6, 7, 8]:
            print("  ✗ WEAKENS Claim 5: Peak at round 6+ (no decline)")

# D3: Translation vs Thinking
print()
print("=" * 70)
print("D3: TRANSLATION VS THINKING (Testing Claim 3: Language constrains thinking)")
print("=" * 70)
for lang in ['navajo', 'classical chinese', 'ancient greek']:
    trans_f = f"/tmp/exp-d3-translate-{lang}.md"
    think_f = f"/tmp/exp-d3-think-{lang}.md"
    if os.path.exists(trans_f) and os.path.exists(think_f):
        trans_text = open(trans_f).read()
        think_text = open(think_f).read()
        trans_scores = parse_scores(trans_text)
        think_scores = parse_scores(think_text)
        trans_len = len(trans_text)
        think_len = len(think_text)
        print(f"\n  {lang.title()}:")
        print(f"    Translation: {trans_len} chars, scores={trans_scores}")
        print(f"    Thinking:    {think_len} chars, scores={think_scores}")
        # Compare lengths as proxy for insight depth
        if think_len > trans_len * 1.3:
            print(f"    → Thinking produced {think_len/trans_len:.1f}x more content than translation")
        else:
            print(f"    → Similar output lengths — may be equivalent")

# C1: Blinded scoring
print()
print("=" * 70)
print("C1: BLINDED SCORING (Testing Claims 3, 7)")
print("=" * 70)
c1_files = sorted(glob.glob("/tmp/exp-c1-*.json"))
for f in c1_files:
    try:
        text = open(f).read()
        # Try to parse as JSON or extract scores
        scores = parse_scores(text)
        print(f"  {os.path.basename(f)}: {scores}")
    except:
        pass

# A2: English Control Baseline
print()
print("=" * 70) 
print("A2: ENGLISH CONTROL BASELINE (Calibration check)")
print("=" * 70)
for pk in ['p1', 'p2', 'p3']:
    f = f"/tmp/exp-a2-english-{pk}.md"
    if os.path.exists(f):
        text = open(f).read()
        scores = parse_scores(text)
        print(f"  English-{pk}: {len(text)} chars, scores={scores}")
        # If English scores > 3.0, our scoring is miscalibrated
        if scores.get('novelty') and scores['novelty'] > 3.0:
            print(f"    ⚠️ English novelty > 3.0 — scoring may be miscalibrated")

print()
print("=" * 70)
print("FILE INVENTORY")
print("=" * 70)
total = 0
for prefix, label in [('exp-a1-', 'Batch A1: 4 new langs'), 
                        ('exp-a2-', 'Batch A2: English control'),
                        ('exp-a3-', 'Batch A3: Random mode'),
                        ('exp-c1-', 'Batch C1: Blinded scoring'),
                        ('exp-d1-', 'Batch D1: Round scaling'),
                        ('exp-d3-', 'Batch D3: Translation vs thinking'),
                        ('experiment-', 'Original: 9 experiments')]:
    files = glob.glob(f"/tmp/{prefix}*.md") + glob.glob(f"/tmp/{prefix}*.json")
    count = len([f for f in files if os.path.getsize(f) > 10])
    total += count
    print(f"  {label}: {count} files")
print(f"  TOTAL: {total} experiment files")
