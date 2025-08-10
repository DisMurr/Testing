# models/orchestrator.py
"""
orchestrator: chains simple generator -> logic_checker -> tone_classifier

Input:
    prompt (str)

Output:
    {
        "generated": str,              # from simple model
        "logic": dict | {"error": ...},
        "tone": dict  | {"error": ...},
    }

Notes:
- Normalizes prompt to avoid doubled punctuation in generator output.
- Catches sub-model errors so one failure doesn't crash the pipeline.
"""

from typing import Any, Dict
import re

from .my_model import run as _simple_run
from .logic_checker import run as _logic_run
from .tone_classifier import run as _tone_run

def _normalize_prompt(p: str) -> str:
    p = (p or "").strip()
    p = re.sub(r"\s+", " ", p)
    return p.rstrip(".!?")  # avoid "robot." -> "A fun story about robot. begins."

def run(prompt: str) -> Dict[str, Any]:
    norm = _normalize_prompt(prompt)
    result: Dict[str, Any] = {"generated": "", "logic": {}, "tone": {}}

    # generate
    try:
        generated = _simple_run(prompt=norm)
        result["generated"] = generated
    except Exception as e:
        result["generated"] = ""
        result["logic"] = {"error": f"generator failed: {e}"}
        result["tone"]  = {"error": "skipped due to generator failure"}
        return result

    # logic
    try:
        result["logic"] = _logic_run(text=generated)
    except Exception as e:
        result["logic"] = {"error": f"logic_checker failed: {e}"}

    # tone
    try:
        result["tone"] = _tone_run(text=generated)
    except Exception as e:
        result["tone"] = {"error": f"tone_classifier failed: {e}"}

    return result
