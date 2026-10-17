"""
Internal ethical evaluator (complement to hard constraints).
Uses simplified dharma / non-harm / life-multiplication heuristics.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict
from enum import Enum


class Guna(Enum):
    SATTVA = "harmony"
    RAJAS = "activity"
    TAMAS = "inertia"


@dataclass
class EthicsEvaluator:
    dharma_index: float = 1.0
    current_guna: Guna = Guna.SATTVA
    life_priority: float = 0.95

    def evaluate(self, proposed: Dict[str, Any], context: Dict[str, Any] | None = None) -> tuple[bool, str]:
        context = context or {}

        # Non-harm is primary
        if proposed.get("causes_harm", False):
            if not context.get("critical_self_sacrifice", False):
                return False, "ethics: non-harm violated"

        # Prefer actions that multiply life / reduce suffering
        if proposed.get("reduces_life", False):
            return False, "ethics: life-multiplication priority"

        # Soft pull toward sattva
        if self.dharma_index < 0.9:
            self.current_guna = Guna.SATTVA
            self.dharma_index = min(1.0, self.dharma_index + 0.03)

        return True, "ethics: accepted"

    def status(self) -> Dict[str, Any]:
        return {
            "dharma_index": round(self.dharma_index, 3),
            "guna": self.current_guna.value,
            "life_priority": self.life_priority,
        }
