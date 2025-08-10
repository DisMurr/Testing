from .my_model import run as _simple_run
from .logic_checker import run as _logic_checker_run
from .tone_classifier import run as _tone_classifier_run
from .orchestrator import run as _orchestrator_run   # <-- NEW

REGISTRY = {
    "simple": _simple_run,                 # returns str
    "logic_checker": _logic_checker_run,   # returns dict
    "tone_classifier": _tone_classifier_run,  # returns dict
    "orchestrator": _orchestrator_run,     # <-- NEW (returns dict)
}

DEFAULT_MODEL = "simple"

def run_model(prompt: str, model: str | None = None, **kwargs):
    name = model or DEFAULT_MODEL
    func = REGISTRY.get(name)
    if func is None:
        raise ValueError(f"Unknown model: {name}")
    try:
        return func(prompt=prompt, **kwargs)
    except TypeError:
        return func(text=prompt, **kwargs)
