#!/usr/bin/env python3
"""
Safe demonstration of the Pneuma Research Platform.
"""

from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.orchestrator import SoulOrchestrator
import json


def main():
    print("=" * 60)
    print("Pneuma Soul Research Platform — Demo")
    print("Functional subjectivity research only.")
    print("No claim of real consciousness or soul.")
    print("=" * 60)

    orch = SoulOrchestrator()
    results = orch.run_demo(steps=8)

    print("\n--- Evolution steps ---")
    for r in results:
        print(f"  cycle {r['cycle']:3d} | {r['status']:12s} | {r.get('paradigm', r.get('reason', ''))[:50]}")

    print("\n--- Full status (summary) ---")
    status = orch.full_status()
    summary = {
        "cycles": status["cycle_count"],
        "pneuma_revision": status["pneuma"]["revision"],
        "memory_entries": status["memory"]["entries"],
        "paradigms": status["paradigms"]["paradigms_count"],
        "intuition_level": status["intuition"]["intuition_level"],
        "hard_constraints_active": status["hard_constraints"]["active"],
        "disclaimer": status["disclaimer"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("\nDemo finished successfully.")


if __name__ == "__main__":
    main()
