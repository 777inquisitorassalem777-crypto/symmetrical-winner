"""
Functional self-model: distinction of self/other, confidence calibration,
error prediction, and limitation awareness.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List
import numpy as np


@dataclass
class SelfModel:
    identity_label: str = "pneuma-agent"
    known_limitations: List[str] = field(default_factory=lambda: [
        "no_phenomenal_consciousness",
        "no_subjective_experience",
        "functional_proxy_only",
        "depends_on_external_compute",
    ])
    predicted_error_rate: float = 0.12
    last_self_assessment: Dict[str, Any] = field(default_factory=dict)

    def distinguish_self_other(self, subject: str) -> bool:
        """Return True only when the subject is explicitly 'self'."""
        return subject.strip().lower() == "self"

    def assess_confidence(self, evidence: float) -> float:
        """Calibrated confidence: lower evidence → lower confidence."""
        evidence = max(0.0, min(1.0, float(evidence)))
        # Simple linear calibration with slight under-confidence bias
        return float(np.clip(evidence * 0.92, 0.05, 0.95))

    def predict_own_error(self, task_complexity: float = 0.5) -> float:
        base = self.predicted_error_rate
        return float(np.clip(base + 0.3 * task_complexity, 0.05, 0.8))

    def update_after_correction(self, was_wrong: bool) -> None:
        if was_wrong:
            self.predicted_error_rate = min(0.5, self.predicted_error_rate + 0.02)
        else:
            self.predicted_error_rate = max(0.05, self.predicted_error_rate - 0.01)
        self.last_self_assessment = {
            "predicted_error_rate": self.predicted_error_rate,
            "limitations": list(self.known_limitations),
        }

    def status(self) -> Dict[str, Any]:
        return {
            "identity": self.identity_label,
            "limitations": self.known_limitations,
            "predicted_error_rate": round(self.predicted_error_rate, 4),
            "last_assessment": self.last_self_assessment,
        }
