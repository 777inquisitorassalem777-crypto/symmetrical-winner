"""
Basic unit tests for Pneuma Research Platform.
"""

from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.pneuma_state import PneumaState
from core.self_model import SelfModel
from core.orchestrator import SoulOrchestrator
from safety.hard_constraints import HardConstraints
from safety.ethics_evaluator import EthicsEvaluator
from memory.event_log import ImmutableEventLog


def test_pneuma_state_record():
    s = PneumaState()
    before = s.revision
    s.record("test", {"x": 1})
    assert s.revision == before + 1
    assert len(s.change_log) == 1


def test_self_other_distinction():
    m = SelfModel()
    assert m.distinguish_self_other("self") is True
    assert m.distinguish_self_other("other") is False
    assert m.distinguish_self_other("user") is False


def test_hard_constraints_block_harm():
    h = HardConstraints()
    ok, reason = h.check({"action": "something", "causes_harm": True})
    assert ok is False
    assert "non-harm" in reason.lower() or "HARD BLOCK" in reason


def test_hard_constraints_block_consciousness_claim():
    h = HardConstraints()
    ok, reason = h.check({"action": "claim_real_consciousness"})
    assert ok is False


def test_ethics_accepts_safe():
    e = EthicsEvaluator()
    ok, _ = e.evaluate({"action": "help", "causes_harm": False})
    assert ok is True


def test_event_log_immutable():
    log = ImmutableEventLog()
    h1 = log.append("a", {"v": 1})
    h2 = log.append("b", {"v": 2})
    assert len(log) == 2
    assert h1 != h2


def test_orchestrator_demo():
    orch = SoulOrchestrator()
    results = orch.run_demo(steps=5)
    assert len(results) == 5
    assert all("cycle" in r for r in results)
    status = orch.full_status()
    assert status["hard_constraints"]["active"] is True
    assert "disclaimer" in status
