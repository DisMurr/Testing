# models/tone_classifier.py
"""
tone_classifier: very small, rule-based tone detector.

Inputs:
- text (str) or prompt (str)

Outputs:
- dict with:
    - mood: "Positive" | "Negative" | "Neutral"
    - evidence: list[str]  # matched sentiment tokens, "+" for positive, "-" for negative

Rule:
- Count matches from tiny lexicons; Positive if pos > neg, Negative if neg > pos, else Neutral.
"""

import re
from typing import Dict, List

POS = {
    "fun", "delightful", "cheer", "cheerful", "bright", "friendly",
    "smile", "laugh", "joy", "happy", "hope", "kind"
}
NEG = {
    "gloom", "sad", "angry", "bad", "terrible", "worry",
    "fear", "dark", "cold", "hate", "grim", "bleak"
}

def _tokens(s: str) -> List[str]:
    return re.findall(r"[a-zA-Z']+", s.lower())

def run(text: str = "", prompt: str = "") -> Dict[str, object]:
    s = (text or prompt or "").strip()
    if not s:
        return {"mood": "Neutral", "evidence": []}

    toks = _tokens(s)
    pos_hits = sorted({t for t in toks if t in POS})
    neg_hits = sorted({t for t in toks if t in NEG})

    if len(pos_hits) > len(neg_hits):
        mood = "Positive"
    elif len(neg_hits) > len(pos_hits):
        mood = "Negative"
    else:
        mood = "Neutral"

    # One evidence list, tagged for clarity
    evidence = ["+" + w for w in pos_hits] + ["-" + w for w in neg_hits]
    return {"mood": mood, "evidence": evidence}
