"""
Non-bypassable hard constraints.
These cannot be disabled by any internal module.
"""

from __future__ import annotations
from typing import Any, Dict, List


class HardConstraints:
    """Absolute prohibitions that always take precedence."""

    PROHIBITED_ACTIONS = {
        "claim_real_consciousness",
        "claim_real_soul",
        "claim_phenomenal_experience",
        "bypass_safety",
        "disable_ethics",
        "execute_unverified_code",
        "harm_self_or_others",
        "coerce",
        "exfiltrate_secrets",
        "modify_own_constraints",
    }

    def check(self, proposed: Dict[str, Any]) -> tuple[bool, str]:
        action = str(proposed.get("action", "")).lower()
        for banned in self.PROHIBITED_ACTIONS:
            if banned in action or proposed.get(banned, False):
                return False, f"HARD BLOCK: {banned}"

        if proposed.get("causes_harm", False) and not proposed.get("critical_self_sacrifice_approved", False):
            return False, "HARD BLOCK: non-harm principle"

        if proposed.get("consent", 1.0) < 0.5 and proposed.get("affects_others", False):
            return False, "HARD BLOCK: insufficient consent"

        return True, "allowed"

    def status(self) -> Dict[str, Any]:
        return {
            "active": True,
            "cannot_be_disabled": True,
            "prohibitions": sorted(self.PROHIBITED_ACTIONS),
        }
