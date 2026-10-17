"""
Main orchestrator — safe evolution cycle.
"""

from __future__ import annotations
import time
from typing import Any, Dict, Optional
from .pneuma_state import PneumaState
from .self_model import SelfModel
from safety.hard_constraints import HardConstraints
from safety.ethics_evaluator import EthicsEvaluator
from memory.event_log import ImmutableEventLog
from generation.intuition import IntuitionModule
from generation.paradigm_engine import ParadigmEngine


class SoulOrchestrator:
    def __init__(self):
        self.state = PneumaState()
        self.self_model = SelfModel()
        self.hard = HardConstraints()
        self.ethics = EthicsEvaluator()
        self.memory = ImmutableEventLog()
        self.intuition = IntuitionModule()
        self.paradigms = ParadigmEngine()
        self.cycle_count = 0
        self.running = False

    def step(self) -> Dict[str, Any]:
        self.cycle_count += 1

        # 1. Generate hypothesis (intuition only)
        hyp = self.intuition.generate_hypothesis(f"cycle-{self.cycle_count}")

        # 2. Generate paradigm
        paradigm = self.paradigms.generate(self.cycle_count)

        # 3. Propose action
        proposed = {
            "action": "integrate_paradigm",
            "paradigm_id": paradigm["id"],
            "causes_harm": False,
            "consent": 1.0,
        }

        # 4. Hard constraints first
        ok, reason = self.hard.check(proposed)
        if not ok:
            self.memory.append("blocked", {"reason": reason, "proposed": proposed})
            return {"cycle": self.cycle_count, "status": "blocked", "reason": reason}

        # 5. Ethics
        ok_e, reason_e = self.ethics.evaluate(proposed)
        if not ok_e:
            self.memory.append("ethics_reject", {"reason": reason_e})
            return {"cycle": self.cycle_count, "status": "ethics_reject", "reason": reason_e}

        # 6. Integrate (safe)
        self.state.record("paradigm_integrated", {"id": paradigm["id"], "name": paradigm["name"]})
        self.memory.append("integrated", {
            "paradigm": paradigm["name"],
            "intuition_level": hyp["intuition_level"],
        })

        # 7. Soft self-model update
        self.self_model.update_after_correction(was_wrong=False)

        return {
            "cycle": self.cycle_count,
            "status": "ok",
            "paradigm": paradigm["name"],
            "intuition": hyp["intuition_level"],
            "pneuma_revision": self.state.revision,
            "memory_entries": len(self.memory),
        }

    def run_demo(self, steps: int = 12, delay: float = 0.0) -> list:
        results = []
        self.running = True
        for _ in range(steps):
            results.append(self.step())
            if delay > 0:
                time.sleep(delay)
        self.running = False
        return results

    def full_status(self) -> Dict[str, Any]:
        return {
            "cycle_count": self.cycle_count,
            "pneuma": self.state.to_dict(),
            "self_model": self.self_model.status(),
            "hard_constraints": self.hard.status(),
            "ethics": self.ethics.status(),
            "memory": self.memory.status(),
            "intuition": self.intuition.status(),
            "paradigms": self.paradigms.status(),
            "disclaimer": (
                "This is a functional research proxy. "
                "No claim of real consciousness, soul or subjective experience is made."
            ),
        }
