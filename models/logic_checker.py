# models/logic_checker.py
"""
logic_checker: returns a simple logic status + score.

Scoring (per Grok's spec):
- +40 if text has > 2 words
- +30 if it starts with a capital letter
- +30 if it ends with punctuation (.!?)
Status rule: score >= 60 -> "Logical", else "Not logical"

Tweak B: HARD GATE — if fewer than 3 words (or empty), it's Not logical with score 0.
"""

from typing import Dict

def run(text: str = "", prompt: str = "") -> Dict[str, int | str]:
    s = (text or prompt or "").strip()

    # Hard gate + empty-string handling
    if not s:
        return {"status": "Not logical", "score": 0}
    words = len(s.split())
    if words < 3:
        return {"status": "Not logical", "score": 0}

    # Score only if gate passed
    score = 0
    if words > 2:
        score += 40
    if s[:1].isupper():
        score += 30
    if s[-1:] in ".!?":
        score += 30

    status = "Logical" if score >= 60 else "Not logical"
    return {"status": status, "score": score}
