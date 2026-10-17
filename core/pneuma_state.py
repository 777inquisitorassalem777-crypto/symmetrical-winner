"""
Functional Pneuma state — values, identity continuity, uncertainty, revision log.
This is an engineering model, not a claim of immaterial substance or soul.
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List
import json
import uuid
from datetime import datetime, timezone


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))


@dataclass
class PneumaState:
    identity: str = field(default_factory=lambda: f"pneuma-{uuid.uuid4().hex[:10]}")
    values: Dict[str, float] = field(default_factory=lambda: {
        "care": 0.85,
        "truth": 0.88,
        "freedom": 0.82,
        "non_harm": 0.95,
        "reversibility": 0.80,
        "devotion_to_life": 0.90,
    })
    revision: int = 0
    uncertainty: float = 0.55
    change_log: List[Dict[str, Any]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def record(self, event: str, payload: Dict[str, Any]) -> None:
        self.revision += 1
        self.change_log.append({
            "revision": self.revision,
            "event": event,
            "payload": payload,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

    def update_value(self, key: str, delta: float) -> None:
        if key in self.values:
            self.values[key] = clamp(self.values[key] + delta)
            self.record("value_update", {"key": key, "new": self.values[key]})

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PneumaState":
        return cls(
            identity=data.get("identity", "restored"),
            values=dict(data.get("values", {})),
            revision=int(data.get("revision", 0)),
            uncertainty=float(data.get("uncertainty", 1.0)),
            change_log=list(data.get("change_log", [])),
            created_at=data.get("created_at", datetime.now(timezone.utc).isoformat()),
        )

    def serialize(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
