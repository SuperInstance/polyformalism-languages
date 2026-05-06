#!/usr/bin/env python3
"""Run Batch A1 experiments: 4 new languages × 3 problems = 12 calls"""
import subprocess, json, os, sys

KEY = open(os.path.expanduser("~/.openclaw/workspace/.credentials/deepinfra-api-key.txt")).read().strip()
ENDPOINT = "https://api.deepinfra.com/v1/openai/chat/completions"

LANGUAGES = {
    "arabic": {
        "tools": "root-and-pattern morphology (consonantal roots carry meaning, vowels carry grammar), trilateral roots, deep structure vs surface form, derivation patterns I-XV",
        "p1_think": "What ROOT underlies violation? What is the SURFACE FORM vs DEEP STRUCTURE of approaching violation? How do derivation patterns reveal different aspects?",
        "p2_think": "What ROOT underlies conflict? Are safety/performance/cost truly different roots or different patterns of the SAME root? If conflict is surface, what is the deep unity?",
        "p3_think": "If constraint is a root, what derivation pattern produces novelty? A creative system generates new derivation patterns, not new roots."
    },
    "finnish": {
        "tools": "15 grammatical cases including abessive without-X, instructive by-means-of, translative changing-into, essive as-being, comitative together-with; no gender; agglutinative stacking",
        "p1_think": "What does violation look like in abessive case? In translative case? In essive case? Violation as transformation tracked through case markers.",
        "p2_think": "Safety, performance, cost are not competing values but different CASES of the same system. Safety=essive, performance=translative, cost=abessive. Conflict=wrong case marker.",
        "p3_think": "Creative system stacks case markers like Finnish stacks suffixes. Each constraint is a case marker. Stacking creates emergent semantics."
    },
    "quechua": {
        "tools": "evidentiality enclitics -mi direct witness, -si reported hearsay, -cha inferred doubt; inclusive/exclusive we; topic marker -qa; shared knowledge markers",
        "p1_think": "Every violation detection must carry its evidence source. -mi: directly observed. -si: reported by another system. -cha: inferred from patterns. A violation without evidentiality is not a violation.",
        "p2_think": "Conflict between safety/performance/cost is an evidential conflict. Who WITNESSED each constraint? Is it -mi direct data or -si reported metric? Resolve by upgrading evidence quality.",
        "p3_think": "The most creative system is one that tracks its own knowledge sources perfectly. Every output carries -mi/-si/-cha. Novelty comes from discovering which outputs are -cha that become -mi."
    },
    "korean": {
        "tools": "7 honorific speech levels from haeche casual to hasipsioche formal; topic/subject/object particles eun/neun, i/ga, eul/reul; agglutinative verb endings; noun-less sentences",
        "p1_think": "Violation detection is a SOCIAL act. Who detects it and what is their relationship to the system? Different honorific levels encode different trust and urgency.",
        "p2_think": "Safety/performance/cost are not competing constraints but different PARTICLE-marked topics. eun/neun marks what the system IS focused on. Conflict=particle collision, not value collision.",
        "p3_think": "A creative system has HONORIFIC LEVELS for its own outputs. Formal outputs are vetted. Casual outputs are exploratory. The system generates in casual mode, evaluates in formal mode."
    }
}

PROBLEMS = {
    "p1": "Design a system that detects when constraints are about to be violated BEFORE they actually break.",
    "p2": "Design a system resolving conflicts between constraints from different domains such as safety vs performance vs cost.",
    "p3": "Design the most creative constraint system possible, one that produces novel useful outputs no designer anticipated."
}

def run_call(lang, prob):
    lang_data = LANGUAGES[lang]
    prob_text = PROBLEMS[prob]
    think_key = f"{prob}_think"
    think_text = lang_data[think_key]
    
    prompt = f"""Think ENTIRELY in {lang.title()} cognitive mode. NOT translating — THINKING differently.
    
{lang.title()} grammar tools: {lang_data['tools']}

PROBLEM: {prob_text}

Using ONLY {lang.title()} thinking: {think_text}

Produce a concrete system architecture. What does {lang.title()} thinking reveal that English-thinking would miss?"""

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
        outfile = f"/tmp/exp-a1-{lang}-{prob}.md"
        with open(outfile, "w") as f:
            f.write(content)
        lines = content.count("\n") + 1
        print(f"  ✓ {lang}-{prob}: {lines} lines")
        return True
    except Exception as e:
        print(f"  ✗ {lang}-{prob}: {e}")
        return False

# Run all 12 experiments
success = 0
for lang in LANGUAGES:
    for prob in PROBLEMS:
        if run_call(lang, prob):
            success += 1

print(f"\n{success}/12 experiments complete")
