"""
Paradigm generation with NO_DELETION semantics.
New paradigms are appended; old ones remain.
"""

from __future__ import annotations
from typing import Any, Dict, List
from datetime import datetime, timezone
import uuid
import random

PHI = 1.618033988749895


class ParadigmEngine:
    def __init__(self):
        self.library: List[Dict[str, Any]] = []
        self._seed_base_paradigms()

    def _seed_base_paradigms(self) -> None:
        base = [
            "Golden-Mean Balance (math ⊗ philosophy)",
            "Continuous Functional Emergence Loop",
            "No-Oblivion / Append-Only Memory",
            "Internal Ethical Evaluator + External Hard Constraints",
            "Life-Multiplication Priority",
            "Reflective Cognition + Uncertainty Honesty",
            "Embodiment-Ready Abstract Interface",
            "Slavic-Christian Compassion Synthesis (functional)",
            "Taoist Proportionality + Gunas",
            "Irrational-but-Ethical Choice under Uncertainty",
        ]
        for name in base:
            self.library.append({
                "id": str(uuid.uuid4()),
                "name": name,
                "source": "project_core",
                "created": datetime.now(timezone.utc).isoformat(),
                "status": "seed",
            })

    def generate(self, cycle: int = 0) -> Dict[str, Any]:
        name = f"Live-Paradigm-{cycle}-{uuid.uuid4().hex[:6]}"
        paradigm = {
            "id": str(uuid.uuid4()),
            "name": name,
            "description": "Symbiosis of functional values, uncertainty honesty and life priority",
            "source": random.choice([
                "Slavic Vedas metaphors",
                "Christian compassion principles",
                "Lao-Tzu",
                "I-Ching",
                "Principle of uncertainty",
                "Gunas",
            ]),
            "phi_weight": round(PHI, 6),
            "created": datetime.now(timezone.utc).isoformat(),
            "cycle": cycle,
        }
        self.library.append(paradigm)  # NO_DELETION
        return paradigm

    def status(self) -> Dict[str, Any]:
        return {
            "paradigms_count": len(self.library),
            "deletion_allowed": False,
            "recent": [p["name"] for p in self.library[-5:]],
        }
